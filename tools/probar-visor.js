const fs = require("fs");
const { JSDOM } = require("jsdom");

const frag = fs.readFileSync("visor.html", "utf8");
const page = "<!doctype html><html lang=es><head><meta charset=utf-8></head><body>" + frag + "</body></html>";

const errores = [];
const dom = new JSDOM(page, {
  runScripts: "dangerously",
  resources: undefined,
  beforeParse(win){
    win.scrollTo = () => {};                                  // no implementado en jsdom
    win.Element.prototype.scrollIntoView = function(){};      // idem
    if (!win.CSS) win.CSS = {};
    if (!win.CSS.escape) win.CSS.escape = s => String(s).replace(/[^\w-]/g, c => "\\" + c);
    // finge las capacidades del artefacto para poder probar el guardado
    win.claude = { use: n => Promise.resolve(
      n === "artifact"  ? { publish: html => { win.__publicado = html; return Promise.resolve({version:"v2"}); } } :
      n === "downloads" ? { save: req => { win.__bajado = req; return Promise.resolve({status:"saved"}); } } : null) };
  },
  virtualConsole: new (require("jsdom").VirtualConsole)()
    .on("jsdomError", e => errores.push("jsdomError: " + (e.detail || e.message)))
    .on("error", (...a) => errores.push("console.error: " + a.join(" ")))
});

const w = dom.window, d = w.document;
const q = s => d.querySelector(s);
const t = s => (q(s) ? q(s).textContent.trim() : "<<falta " + s + ">>");

if (errores.length) { console.log("ERRORES AL CARGAR:"); errores.forEach(e => console.log("  " + e)); process.exit(1); }

console.log("subtítulo #nfiles :", t("#nfiles"));
console.log("documento abierto :", t("#docPath"), "|", t("#docTitle"));
console.log("palabras / grupo  :", t("#mWords"), "/", t("#mGroup"), "| revisados:", t("#mDone"));
console.log("html renderizado  :", q("#paper").innerHTML.length, "bytes,",
            q("#paper").querySelectorAll("h1,h2,h3,p,table,pre").length, "nodos");
console.log("chips de salto    :", d.querySelectorAll(".jchip").length,
            "->", [...d.querySelectorAll(".jchip")].map(b => b.textContent).join(" · "));
console.log("items del árbol   :", d.querySelectorAll(".item").length);
console.log("grupos con ancla  :", d.querySelectorAll(".railgroup[id]").length);

// navegar a un documento de la Mansión
const objetivo = "juegos/asesinato-en-la-mansion/personajes/01-ema-fatal.md";
const btn = [...d.querySelectorAll(".item")].find(b => b.dataset.id === objetivo);
if (!btn) { console.log("FALLA: no está", objetivo); process.exit(1); }
btn.dispatchEvent(new w.MouseEvent("click", { bubbles: true }));
console.log("\ntras clic         :", t("#docPath"), "|", t("#docTitle"));
console.log("contenido         :", q("#paper").innerHTML.length, "bytes");

// marcar revisado y comprobar que se refleja
q('.chip[data-v="revisado"]').dispatchEvent(new w.MouseEvent("click", { bubbles: true }));
console.log("estado en árbol   :", btn.dataset.st, "| aviso:", t("#saveNote"), "| revisados:", t("#mDone"));

// tablero
q("#tabBoard").dispatchEvent(new w.MouseEvent("click", { bubbles: true }));
console.log("filas del tablero :", d.querySelectorAll(".brow").length,
            "| revisadas:", d.querySelectorAll('.brow[data-st="revisado"]').length);

// búsqueda
q("#tabDocs").dispatchEvent(new w.MouseEvent("click", { bubbles: true }));
const f = q("#find"); f.value = "candelabro";
f.dispatchEvent(new w.Event("input", { bubbles: true }));
console.log("busca 'candelabro':", [...d.querySelectorAll(".item")].filter(b => !b.classList.contains("hide")).length, "resultados");

// --- guardado: la pagina se republica a si misma con el estado dentro ---
q("#saveBtn").dispatchEvent(new w.MouseEvent("click", { bubbles: true }));
// --- descarga ---
q("#dlBtn").dispatchEvent(new w.MouseEvent("click", { bubbles: true }));

setTimeout(() => {
  const pub = w.__publicado;
  if (!pub) { console.log("\nFALLA: publish nunca se llamó"); process.exit(1); }
  console.log("\npágina republicada :", (pub.length/1024).toFixed(0), "KB | aviso:", t("#saveNote"));
  console.log("empieza con doctype:", /^<!doctype html>/i.test(pub));

  const est = JSON.parse(pub.match(/<script id="state" type="application\/json">(.*?)<\/script>/s)[1]);
  const marcados = Object.entries(est.files).filter(([,v]) => v.status !== "pendiente");
  console.log("estado guardado    :", marcados.length, "documento(s) ->", marcados.map(([k,v]) => k.split("/").pop()+"="+v.status).join(", "));

  const a = pub.lastIndexOf("<script>"), b = pub.indexOf("</script>", a);
  const app = pub.slice(a + 8, b);
  console.log("script republicado :", app.length, "bytes (debe ser ~15000, no ~570000)");
  fs.writeFileSync("/tmp/app-republicado.js", app);
  try { require("child_process").execFileSync("node", ["--check", "/tmp/app-republicado.js"]); console.log("sintaxis tras guardar: ok"); }
  catch(e){ console.log("FALLA: el script republicado no es válido"); process.exit(1); }

  const dl = w.__bajado;
  console.log("descarga ofrecida  :", dl ? dl.filename + " (" + dl.data.length + " bytes)" : "NINGUNA");

  if (errores.length) { console.log("\nERRORES:"); errores.forEach(e => console.log("  " + e)); process.exit(1); }
  console.log("\nsin errores de ejecución");
}, 300);
