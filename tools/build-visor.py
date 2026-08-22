#!/usr/bin/env python3
"""Genera visor.html: un solo archivo autocontenido con todo el repo de juegos.

Uso:  python3 tools/build-visor.py
Salida: visor.html (en la raíz del repo)

El HTML resultante se publica como Artifact. Se puede regenerar cuantas veces
haga falta: las notas de revisión guardadas en el Artifact NO viven aquí, viven
en la versión publicada, así que al regenerar hay que volver a pegarlas si se
quieren conservar (el script acepta --state notas.json para reinyectarlas).
"""
import json, base64, re, sys, os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "visor.html"

# ---------------------------------------------------------------- recolección

GRUPOS = [
    ("inicio",      "Inicio",                    ["README.md"]),
    ("motor",       "Motor",                     ["motor/00-el-motor.md", "motor/01-guia-de-autoria.md", "motor/02-hoja-de-diseno.md"]),
    ("plantillas",  "Plantillas",                None),
    ("herencia",    "La Herencia de la Abuela",  None),
    ("mansion",     "Asesinato en la Mansión",   None),
]

def recolectar():
    archivos = []
    def add(path, grupo):
        p = ROOT / path
        txt = p.read_text(encoding="utf-8")
        m = re.search(r"^#\s+(.+)$", txt, re.M)
        titulo = m.group(1).strip() if m else p.stem
        titulo = re.sub(r"[\U0001F000-\U0001FAFF☀-➿️]", "", titulo).strip()
        m2 = re.search(r"^###\s+(.+)$", txt, re.M)
        sub = m2.group(1).strip() if m2 else ""
        sub = re.sub(r"[*_`]", "", sub)
        sub = re.sub(r"[\U0001F000-\U0001FAFF☀-➿️]", "", sub).strip()
        archivos.append({
            "id": path, "grupo": grupo, "titulo": titulo, "sub": sub[:120],
            "palabras": len(txt.split()), "md": txt,
        })

    add("README.md", "inicio")
    for f in ["motor/00-el-motor.md", "motor/01-guia-de-autoria.md", "motor/02-hoja-de-diseno.md"]:
        add(f, "motor")
    for f in sorted((ROOT / "motor/plantillas").glob("*.md")):
        add(str(f.relative_to(ROOT)), "plantillas")
    for juego, grupo in [("la-herencia-de-la-abuela", "herencia"), ("asesinato-en-la-mansion", "mansion")]:
        base = ROOT / "juegos" / juego
        for f in sorted(base.glob("*.md")):
            add(str(f.relative_to(ROOT)), grupo)
        for f in sorted((base / "personajes").glob("*.md")):
            add(str(f.relative_to(ROOT)), grupo)
    return archivos

# ---------------------------------------------------------------------- shell

SHELL = r"""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Zilla+Slab:wght@400;500;600;700&family=Karla:ital,wght@0,400;0,500;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<title>Expediente del Misterio</title>
<style>
:root{
  --ground:#EDEBE4; --surface:#F8F7F3; --surface-2:#E4E2D9; --raised:#FFFFFF;
  --ink:#1E2224; --ink-mid:#4A514D; --ink-soft:#6E756F; --ink-faint:#98A099;
  --rule:#D3D1C7; --rule-soft:#E1DFD6;
  --accent:#8C2B2B; --accent-soft:#B4534E; --accent-wash:#F0E4E1; --on-accent:#FFFFFF;
  --brass:#8A6E32; --brass-wash:#F1EAD8;
  --ok:#3F6E4F; --ok-wash:#E2EDE3;
  --warn:#96631C; --warn-wash:#F4EAD6;
  --shadow:0 1px 2px rgba(30,34,36,.06),0 8px 24px -12px rgba(30,34,36,.18);
  --rail:288px; --aside:300px;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --ground:#131618; --surface:#191D20; --surface-2:#22282B; --raised:#1E2427;
    --ink:#E7E8E3; --ink-mid:#B6BDB7; --ink-soft:#8F978F; --ink-faint:#6B736C;
    --rule:#2C3337; --rule-soft:#232A2D;
    --accent:#D97B72; --accent-soft:#E9A099; --accent-wash:#2E2220; --on-accent:#16191B;
    --brass:#C9A961; --brass-wash:#2A2519;
    --ok:#7FB08A; --ok-wash:#1D2A21;
    --warn:#DFA84C; --warn-wash:#2C2418;
    --shadow:0 1px 2px rgba(0,0,0,.4),0 8px 24px -12px rgba(0,0,0,.7);
  }
}
:root[data-theme="dark"]{
  --ground:#131618; --surface:#191D20; --surface-2:#22282B; --raised:#1E2427;
  --ink:#E7E8E3; --ink-mid:#B6BDB7; --ink-soft:#8F978F; --ink-faint:#6B736C;
  --rule:#2C3337; --rule-soft:#232A2D;
  --accent:#D97B72; --accent-soft:#E9A099; --accent-wash:#2E2220; --on-accent:#16191B;
  --brass:#C9A961; --brass-wash:#2A2519;
  --ok:#7FB08A; --ok-wash:#1D2A21;
  --warn:#DFA84C; --warn-wash:#2C2418;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 8px 24px -12px rgba(0,0,0,.7);
}

*{box-sizing:border-box}
body{
  margin:0; background:var(--ground); color:var(--ink);
  font-family:"Karla","Helvetica Neue",Arial,sans-serif;
  font-size:16px; line-height:1.6; -webkit-font-smoothing:antialiased;
}
button,input,textarea,select{font:inherit;color:inherit}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:3px}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}

.mono{font-family:"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace}
.lbl{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:10.5px;letter-spacing:.13em;text-transform:uppercase;color:var(--ink-faint)}

/* ---------------------------------------------------------------- topbar */
.top{
  position:sticky;top:0;z-index:40;display:flex;align-items:center;gap:18px;
  padding:12px 20px;background:var(--surface);border-bottom:1px solid var(--rule);
  flex-wrap:wrap;
}
.brand{display:flex;align-items:baseline;gap:10px;margin-right:auto}
.seal{
  width:22px;height:22px;border-radius:50%;background:var(--accent);flex:none;
  align-self:center;position:relative;box-shadow:inset 0 0 0 3px var(--surface),inset 0 0 0 4px var(--accent);
}
.brand h1{
  font-family:"Zilla Slab",Georgia,serif;font-weight:600;font-size:19px;
  margin:0;letter-spacing:-.01em;
}
.brand .sub{font-size:12.5px;color:var(--ink-soft)}
.tabs{display:flex;gap:2px;background:var(--surface-2);padding:3px;border-radius:7px}
.tab{
  border:0;background:none;padding:6px 13px;border-radius:5px;cursor:pointer;
  font-size:13.5px;font-weight:600;color:var(--ink-soft);
}
.tab[aria-selected="true"]{background:var(--raised);color:var(--ink);box-shadow:var(--shadow)}
.find{
  display:flex;align-items:center;gap:7px;background:var(--raised);
  border:1px solid var(--rule);border-radius:7px;padding:6px 11px;min-width:210px;
}
.find input{border:0;background:none;outline:none;width:100%;font-size:14px}
.find input::placeholder{color:var(--ink-faint)}
.btn{
  border:1px solid var(--rule);background:var(--raised);border-radius:7px;
  padding:7px 13px;cursor:pointer;font-size:13.5px;font-weight:600;
  display:inline-flex;align-items:center;gap:7px;white-space:nowrap;
}
.btn:hover{border-color:var(--ink-faint)}
.btn[disabled]{opacity:.45;cursor:not-allowed}
.btn-primary{background:var(--accent);border-color:var(--accent);color:var(--on-accent)}
.btn-primary:hover{background:var(--accent-soft);border-color:var(--accent-soft)}
.savenote{font-size:12.5px;color:var(--ink-soft);min-width:96px}
.savenote[data-tone="ok"]{color:var(--ok)}
.savenote[data-tone="bad"]{color:var(--accent)}

/* ------------------------------------------------------------------ panes */
.panes{display:grid;grid-template-columns:var(--rail) minmax(0,1fr) var(--aside);
  height:calc(100vh - 58px);min-height:520px}
.board{display:none}
body[data-view="board"] .panes{display:none}
body[data-view="board"] .board{display:block}

/* --------------------------------------------------------------- rail */
.rail{border-right:1px solid var(--rule);overflow-y:auto;background:var(--surface);padding-bottom:40px}
.railgroup{border-bottom:1px solid var(--rule-soft)}
.railgroup > .lbl{display:block;padding:16px 18px 7px}
.item{
  display:grid;grid-template-columns:9px 1fr auto;gap:10px;align-items:baseline;
  width:100%;text-align:left;border:0;background:none;cursor:pointer;
  padding:7px 16px 7px 14px;border-left:3px solid transparent;color:inherit;
}
.item:hover{background:var(--surface-2)}
.item[aria-current="true"]{background:var(--surface-2);border-left-color:var(--accent)}
.item .dot{width:7px;height:7px;border-radius:50%;background:var(--rule);align-self:center;flex:none}
.item[data-st="revisado"] .dot{background:var(--ok)}
.item[data-st="cambiar"] .dot{background:var(--warn)}
.item .t{font-size:13.5px;line-height:1.35;font-weight:500}
.item[aria-current="true"] .t{font-weight:700}
.item .n{font-family:"IBM Plex Mono",monospace;font-size:10.5px;color:var(--ink-faint);font-variant-numeric:tabular-nums}
.item.hide{display:none}
.emptyfind{padding:22px 18px;font-size:13px;color:var(--ink-soft)}

/* --------------------------------------------------------------- doc */
.doc{overflow-y:auto;background:var(--ground)}
.dochead{
  position:sticky;top:0;z-index:20;background:var(--ground);
  border-bottom:1px solid var(--rule);padding:16px 40px 13px;
  display:flex;align-items:flex-end;gap:16px;flex-wrap:wrap;
}
.dochead .path{font-family:"IBM Plex Mono",monospace;font-size:11px;color:var(--ink-faint);margin-bottom:3px}
.dochead h2{font-family:"Zilla Slab",Georgia,serif;font-size:20px;margin:0;font-weight:600;text-wrap:balance}
.dochead .acts{margin-left:auto;display:flex;gap:8px}
.paper{max-width:74ch;margin:0 auto;padding:34px 40px 120px}

/* markdown */
.paper h1,.paper h2,.paper h3,.paper h4{font-family:"Zilla Slab",Georgia,serif;line-height:1.22;text-wrap:balance;margin:0}
.paper h1{font-size:29px;font-weight:700;margin:38px 0 6px;letter-spacing:-.015em}
.paper h1:first-child{margin-top:0}
.paper h2{font-size:22px;font-weight:600;margin:34px 0 6px;padding-top:16px;border-top:1px solid var(--rule-soft)}
.paper h3{font-size:17px;font-weight:600;margin:26px 0 4px;color:var(--ink)}
.paper h4{font-size:14px;font-weight:600;margin:20px 0 3px;color:var(--ink-mid);
  font-family:"IBM Plex Mono",monospace;letter-spacing:.03em}
.paper p{margin:11px 0}
.paper ul,.paper ol{margin:11px 0;padding-left:22px}
.paper li{margin:5px 0}
.paper li::marker{color:var(--brass)}
.paper strong{font-weight:700}
.paper em{font-style:italic}
.paper a{color:var(--accent);text-underline-offset:2px}
.paper hr{border:0;border-top:1px solid var(--rule);margin:30px 0}
.paper code{font-family:"IBM Plex Mono",monospace;font-size:.87em;background:var(--surface-2);
  padding:1.5px 5px;border-radius:4px}
.paper pre{background:var(--surface);border:1px solid var(--rule);border-radius:8px;
  padding:15px 17px;overflow-x:auto;margin:15px 0}
.paper pre code{background:none;padding:0;font-size:12.5px;line-height:1.5;white-space:pre}
.paper blockquote{
  margin:15px 0;padding:12px 18px;background:var(--surface);
  border-left:3px solid var(--brass);border-radius:0 7px 7px 0;color:var(--ink-mid);
}
.paper blockquote p{margin:7px 0}
.paper blockquote p:first-child{margin-top:0}
.paper blockquote p:last-child{margin-bottom:0}
.tablewrap{overflow-x:auto;margin:16px 0;border:1px solid var(--rule);border-radius:8px}
.paper table{border-collapse:collapse;width:100%;font-size:13.5px}
.paper th,.paper td{padding:8px 12px;text-align:left;border-bottom:1px solid var(--rule-soft);vertical-align:top}
.paper th{background:var(--surface-2);font-weight:700;font-size:12px;
  letter-spacing:.02em;white-space:nowrap}
.paper tr:last-child td{border-bottom:0}

/* --------------------------------------------------------------- aside */
.aside{border-left:1px solid var(--rule);background:var(--surface);overflow-y:auto;
  padding:18px 18px 60px;display:flex;flex-direction:column;gap:16px}
.aside h3{font-family:"Zilla Slab",serif;font-size:15px;margin:0;font-weight:600}
.chips{display:flex;gap:6px}
.chip{
  flex:1;border:1px solid var(--rule);background:var(--raised);border-radius:6px;
  padding:8px 4px;cursor:pointer;font-size:12px;font-weight:600;color:var(--ink-soft);
}
.chip:hover{border-color:var(--ink-faint)}
.chip[aria-pressed="true"]{color:var(--ink)}
.chip[data-v="pendiente"][aria-pressed="true"]{background:var(--surface-2);border-color:var(--ink-faint)}
.chip[data-v="revisado"][aria-pressed="true"]{background:var(--ok-wash);border-color:var(--ok);color:var(--ok)}
.chip[data-v="cambiar"][aria-pressed="true"]{background:var(--warn-wash);border-color:var(--warn);color:var(--warn)}
.aside textarea{
  width:100%;min-height:190px;resize:vertical;background:var(--raised);
  border:1px solid var(--rule);border-radius:7px;padding:11px 12px;
  font-size:13.5px;line-height:1.55;outline:none;
}
.aside textarea:focus{border-color:var(--accent)}
.meta{font-size:12.5px;color:var(--ink-soft);display:flex;flex-direction:column;gap:5px}
.meta .row{display:flex;justify-content:space-between;gap:10px}
.meta .row span:last-child{font-family:"IBM Plex Mono",monospace;font-variant-numeric:tabular-nums;color:var(--ink-mid)}
.hint{font-size:11.5px;color:var(--ink-faint);line-height:1.45}

/* --------------------------------------------------------------- board */
.board{padding:28px 32px 90px;max-width:1180px;margin:0 auto}
.board > header{margin-bottom:22px}
.board h2{font-family:"Zilla Slab",serif;font-size:24px;margin:0 0 4px;font-weight:600}
.board .lede{color:var(--ink-soft);font-size:14px;margin:0}
.tally{display:flex;gap:10px;margin:18px 0 24px;flex-wrap:wrap}
.stat{background:var(--surface);border:1px solid var(--rule);border-radius:9px;
  padding:12px 16px;min-width:118px}
.stat b{display:block;font-family:"IBM Plex Mono",monospace;font-size:22px;font-weight:600;
  font-variant-numeric:tabular-nums;line-height:1.2}
.stat[data-k="revisado"] b{color:var(--ok)}
.stat[data-k="cambiar"] b{color:var(--warn)}
.bgroup{margin-bottom:26px}
.bgroup > .lbl{display:block;margin-bottom:8px}
.brow{
  display:grid;grid-template-columns:4px 1fr 150px 88px;gap:14px;align-items:center;
  background:var(--surface);border:1px solid var(--rule);border-radius:8px;
  padding:11px 14px 11px 0;margin-bottom:6px;overflow:hidden;
}
.brow .stripe{align-self:stretch;background:var(--rule)}
.brow[data-st="revisado"] .stripe{background:var(--ok)}
.brow[data-st="cambiar"] .stripe{background:var(--warn)}
.brow .who{min-width:0}
.brow .who b{display:block;font-size:14px;font-weight:600}
.brow .who .p{font-family:"IBM Plex Mono",monospace;font-size:10.5px;color:var(--ink-faint);
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.brow .nota{font-size:12.5px;color:var(--ink-soft);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.brow .go{border:0;background:none;cursor:pointer;font-size:12.5px;font-weight:600;color:var(--accent);text-align:right}

/* --------------------------------------------------------------- responsive */
.railtoggle{display:none}
@media (max-width:1180px){
  :root{--aside:262px}
  .paper{padding:30px 26px 110px}
  .dochead{padding:14px 26px 12px}
}
@media (max-width:980px){
  .panes{grid-template-columns:1fr;height:auto}
  .rail{position:fixed;inset:58px auto 0 0;width:290px;z-index:35;transform:translateX(-101%);
    transition:transform .18s ease;box-shadow:var(--shadow)}
  body[data-rail="open"] .rail{transform:none}
  .aside{border-left:0;border-top:1px solid var(--rule)}
  .doc{overflow:visible}
  .railtoggle{display:inline-flex}
  .brow{grid-template-columns:4px 1fr 78px}
  .brow .nota{display:none}
}
@media (max-width:560px){
  .top{gap:10px;padding:10px 14px}
  .brand .sub{display:none}
  .find{min-width:0;flex:1}
  .paper{padding:24px 16px 90px}
  .dochead{padding:12px 16px 10px}
}
</style>

<header class="top">
  <div class="brand">
    <div class="seal" aria-hidden="true"></div>
    <div>
      <h1>Expediente del Misterio</h1>
      <div class="sub">Motor, plantillas y juegos &middot; <span id="nfiles"></span></div>
    </div>
  </div>
  <button class="btn railtoggle" id="railBtn" aria-label="Mostrar índice">Índice</button>
  <div class="tabs" role="tablist">
    <button class="tab" role="tab" id="tabDocs" aria-selected="true">Documentos</button>
    <button class="tab" role="tab" id="tabBoard" aria-selected="false">Revisión</button>
  </div>
  <label class="find">
    <span class="lbl" aria-hidden="true">Buscar</span>
    <input id="find" type="search" placeholder="Texto en todos los documentos…" aria-label="Buscar en todos los documentos">
  </label>
  <span class="savenote" id="saveNote"></span>
  <button class="btn btn-primary" id="saveBtn">Guardar revisión</button>
</header>

<div class="panes">
  <nav class="rail" id="rail" aria-label="Índice de documentos"></nav>

  <main class="doc" id="docPane">
    <div class="dochead">
      <div>
        <div class="path mono" id="docPath"></div>
        <h2 id="docTitle"></h2>
      </div>
      <div class="acts">
        <button class="btn" id="copyBtn">Copiar</button>
        <button class="btn" id="dlBtn">Bajar .md</button>
      </div>
    </div>
    <article class="paper" id="paper"></article>
  </main>

  <aside class="aside" aria-label="Revisión del documento">
    <div>
      <h3>Revisión</h3>
      <p class="hint" style="margin:4px 0 0">Marca el estado y deja notas. Se guardan en el artefacto cuando presionas <b>Guardar revisión</b>.</p>
    </div>
    <div class="chips" role="group" aria-label="Estado del documento">
      <button class="chip" data-v="pendiente" aria-pressed="true">Pendiente</button>
      <button class="chip" data-v="revisado" aria-pressed="false">Revisado</button>
      <button class="chip" data-v="cambiar" aria-pressed="false">Cambiar</button>
    </div>
    <div>
      <label class="lbl" for="nota">Notas</label>
      <textarea id="nota" placeholder="Qué cambiarías, qué falta, ideas…"></textarea>
    </div>
    <div class="meta">
      <div class="row"><span>Palabras</span><span id="mWords"></span></div>
      <div class="row"><span>Grupo</span><span id="mGroup"></span></div>
      <div class="row"><span>Revisados</span><span id="mDone"></span></div>
    </div>
    <div style="display:flex;gap:8px;flex-wrap:wrap">
      <button class="btn" id="dlAll">Bajar todo .md</button>
      <button class="btn" id="dlNotes">Bajar notas</button>
    </div>
    <p class="hint">Atajos: <b class="mono">j</b> / <b class="mono">k</b> cambian de documento, <b class="mono">/</b> va a la búsqueda.</p>
  </aside>
</div>

<section class="board" id="board" role="tabpanel" aria-labelledby="tabBoard">
  <header>
    <h2>Estado de la revisión</h2>
    <p class="lede" id="boardLede">Cada documento del repositorio, con su estado y tus notas. Haz clic en cualquiera para abrirlo.</p>
  </header>
  <div class="tally" id="tally"></div>
  <div id="boardList"></div>
</section>

<script id="corpus" type="application/json">__CORPUS__</script>
<script id="state" type="application/json">__STATE__</script>
<script id="shell" type="text/plain">__SHELL_B64__</script>
<script>
(function(){
"use strict";
var DOCS  = JSON.parse(document.getElementById("corpus").textContent);
var STATE = JSON.parse(document.getElementById("state").textContent);
var GROUPS = __GROUPS__;
var byId = {}; DOCS.forEach(function(d){ byId[d.id] = d; });
if(!STATE.files) STATE.files = {};
function rec(id){ if(!STATE.files[id]) STATE.files[id] = {status:"pendiente", nota:""}; return STATE.files[id]; }

var $ = function(s){ return document.querySelector(s); };
var body = document.body, dirty = false, current = DOCS[0].id, readOnly = false;

/* ------------------------------------------------------------ markdown */
function esc(s){ return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }
function inline(s){
  s = esc(s);
  s = s.replace(/`([^`]+)`/g, function(_,c){ return "<code>"+c+"</code>"; });
  s = s.replace(/\*\*\*([^*]+)\*\*\*/g, "<strong><em>$1</em></strong>");
  s = s.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  s = s.replace(/(^|[^*])\*([^*\n]+)\*/g, "$1<em>$2</em>");
  s = s.replace(/~~([^~]+)~~/g, "<del>$1</del>");
  s = s.replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, function(_,t,h){
    return /^https?:/.test(h) ? '<a href="'+h+'" target="_blank" rel="noopener">'+t+"</a>"
                              : '<a href="#" data-jump="'+h+'">'+t+"</a>";
  });
  s = s.replace(/&lt;br\s*\/?&gt;/g, "<br>");
  s = s.replace(/&lt;\/?div[^&]*&gt;/g, "");
  return s;
}
function render(md){
  var L = md.replace(/\r/g,"").split("\n"), out = [], i = 0;
  function flushList(tag, items){ out.push("<"+tag+">"+items.map(function(x){return "<li>"+inline(x)+"</li>";}).join("")+"</"+tag+">"); }
  while(i < L.length){
    var ln = L[i];
    if(/^```/.test(ln)){
      var buf = []; i++;
      while(i < L.length && !/^```/.test(L[i])){ buf.push(L[i]); i++; }
      i++;
      out.push("<pre><code>"+esc(buf.join("\n"))+"</code></pre>");
      continue;
    }
    if(/^\s*$/.test(ln)){ i++; continue; }
    var h = ln.match(/^(#{1,6})\s+(.*)$/);
    if(h){ var lv = Math.min(h[1].length,4); out.push("<h"+lv+">"+inline(h[2])+"</h"+lv+">"); i++; continue; }
    if(/^\s*(---+|\*\*\*+|___+)\s*$/.test(ln)){ out.push("<hr>"); i++; continue; }
    if(/^\s*\|/.test(ln) && i+1 < L.length && /^\s*\|[\s:|-]+\|\s*$/.test(L[i+1])){
      var cells = function(r){ return r.trim().replace(/^\||\|$/g,"").split("|").map(function(c){return c.trim();}); };
      var head = cells(ln); i += 2;
      var rows = [];
      while(i < L.length && /^\s*\|/.test(L[i])){ rows.push(cells(L[i])); i++; }
      out.push('<div class="tablewrap"><table><thead><tr>'
        + head.map(function(c){return "<th>"+inline(c)+"</th>";}).join("")
        + "</tr></thead><tbody>"
        + rows.map(function(r){ return "<tr>"+r.map(function(c){return "<td>"+inline(c)+"</td>";}).join("")+"</tr>"; }).join("")
        + "</tbody></table></div>");
      continue;
    }
    if(/^\s*>/.test(ln)){
      var q = []; while(i < L.length && /^\s*>/.test(L[i])){ q.push(L[i].replace(/^\s*>\s?/,"")); i++; }
      out.push("<blockquote>"+render(q.join("\n"))+"</blockquote>");
      continue;
    }
    if(/^\s*[-*+]\s+/.test(ln)){
      var ui = []; while(i < L.length && /^\s*[-*+]\s+/.test(L[i])){ ui.push(L[i].replace(/^\s*[-*+]\s+/,"")); i++; }
      flushList("ul", ui); continue;
    }
    if(/^\s*\d+\.\s+/.test(ln)){
      var oi = []; while(i < L.length && /^\s*\d+\.\s+/.test(L[i])){ oi.push(L[i].replace(/^\s*\d+\.\s+/,"")); i++; }
      flushList("ol", oi); continue;
    }
    var p = []; while(i < L.length && !/^\s*$/.test(L[i]) && !/^(#{1,6}\s|```|\s*[-*+]\s|\s*\d+\.\s|\s*>|\s*\|)/.test(L[i])){ p.push(L[i]); i++; }
    out.push("<p>"+inline(p.join("\n"))+"</p>");
  }
  return out.join("\n");
}

/* ------------------------------------------------------------ rail */
function buildRail(){
  var html = "";
  GROUPS.forEach(function(g){
    var list = DOCS.filter(function(d){ return d.grupo === g.k; });
    if(!list.length) return;
    html += '<div class="railgroup"><span class="lbl">'+g.n+"</span>";
    list.forEach(function(d){
      html += '<button class="item" data-id="'+d.id+'" data-st="'+rec(d.id).status+'">'
           +  '<span class="dot"></span><span class="t">'+esc(d.titulo)+"</span>"
           +  '<span class="n">'+d.palabras+"</span></button>";
    });
    html += "</div>";
  });
  html += '<p class="emptyfind" id="noHits" hidden>Sin resultados.</p>';
  $("#rail").innerHTML = html;
  $("#rail").addEventListener("click", function(e){
    var b = e.target.closest(".item"); if(b) open(b.dataset.id);
  });
}
function syncRail(){
  document.querySelectorAll(".item").forEach(function(b){
    b.dataset.st = rec(b.dataset.id).status;
    b.setAttribute("aria-current", b.dataset.id === current ? "true" : "false");
  });
}

/* ------------------------------------------------------------ open doc */
function open(id){
  if(!byId[id]) return;
  current = id;
  var d = byId[id];
  $("#docPath").textContent = d.id;
  $("#docTitle").textContent = d.titulo;
  $("#paper").innerHTML = render(d.md);
  $("#mWords").textContent = d.palabras;
  var g = GROUPS.filter(function(x){ return x.k === d.grupo; })[0];
  $("#mGroup").textContent = g ? g.n : "—";
  var r = rec(id);
  $("#nota").value = r.nota;
  document.querySelectorAll(".chip").forEach(function(c){
    c.setAttribute("aria-pressed", c.dataset.v === r.status ? "true" : "false");
  });
  syncRail(); tally();
  if(body.dataset.view === "board") setView("docs");
  body.dataset.rail = "closed";
  $("#docPane").scrollTop = 0; window.scrollTo(0,0);
  var el = document.querySelector('.item[data-id="'+CSS.escape(id)+'"]');
  if(el && el.scrollIntoView) el.scrollIntoView({block:"nearest"});
}

/* ------------------------------------------------------------ board */
function tally(){
  var c = {pendiente:0, revisado:0, cambiar:0};
  DOCS.forEach(function(d){ c[rec(d.id).status]++; });
  $("#tally").innerHTML =
      '<div class="stat"><b>'+DOCS.length+"</b><span class='lbl'>Documentos</span></div>"
    + '<div class="stat" data-k="revisado"><b>'+c.revisado+"</b><span class='lbl'>Revisados</span></div>"
    + '<div class="stat" data-k="cambiar"><b>'+c.cambiar+"</b><span class='lbl'>Por cambiar</span></div>"
    + '<div class="stat"><b>'+c.pendiente+"</b><span class='lbl'>Pendientes</span></div>";
  $("#mDone").textContent = c.revisado + " / " + DOCS.length;
  return c;
}
function buildBoard(){
  var html = "";
  GROUPS.forEach(function(g){
    var list = DOCS.filter(function(d){ return d.grupo === g.k; });
    if(!list.length) return;
    html += '<div class="bgroup"><span class="lbl">'+g.n+"</span>";
    list.forEach(function(d){
      var r = rec(d.id);
      html += '<div class="brow" data-st="'+r.status+'"><div class="stripe"></div>'
           +  '<div class="who"><b>'+esc(d.titulo)+'</b><div class="p">'+esc(d.id)+"</div></div>"
           +  '<div class="nota">'+(r.nota ? esc(r.nota) : "—")+"</div>"
           +  '<button class="go" data-go="'+d.id+'">Abrir</button></div>";
    });
    html += "</div>";
  });
  $("#boardList").innerHTML = html;
  tally();
}
$("#boardList").addEventListener("click", function(e){
  var b = e.target.closest("[data-go]"); if(b) open(b.dataset.go);
});

/* ------------------------------------------------------------ views */
function setView(v){
  body.dataset.view = v;
  $("#tabDocs").setAttribute("aria-selected", v === "docs");
  $("#tabBoard").setAttribute("aria-selected", v === "board");
  if(v === "board") buildBoard();
}
$("#tabDocs").onclick  = function(){ setView("docs"); };
$("#tabBoard").onclick = function(){ setView("board"); };
$("#railBtn").onclick  = function(){ body.dataset.rail = body.dataset.rail === "open" ? "closed" : "open"; };

/* ------------------------------------------------------------ search */
$("#find").addEventListener("input", function(e){
  var q = e.target.value.trim().toLowerCase(), hits = 0;
  document.querySelectorAll(".item").forEach(function(b){
    var d = byId[b.dataset.id];
    var on = !q || d.titulo.toLowerCase().indexOf(q) > -1 || d.id.toLowerCase().indexOf(q) > -1
             || d.md.toLowerCase().indexOf(q) > -1;
    b.classList.toggle("hide", !on); if(on) hits++;
  });
  $("#noHits").hidden = hits > 0;
});

/* ------------------------------------------------------------ review edits */
document.querySelectorAll(".chip").forEach(function(c){
  c.onclick = function(){
    rec(current).status = c.dataset.v;
    document.querySelectorAll(".chip").forEach(function(x){
      x.setAttribute("aria-pressed", x === c ? "true" : "false");
    });
    syncRail(); tally(); mark();
  };
});
$("#nota").addEventListener("input", function(e){ rec(current).nota = e.target.value; mark(); });
function mark(){
  dirty = true;
  $("#saveNote").dataset.tone = "";
  $("#saveNote").textContent = "Sin guardar";
}

/* ------------------------------------------------------------ downloads */
var dl = null, dlReady = false;
function downloads(){
  if(dlReady) return Promise.resolve(dl);
  return (window.claude && claude.use ? claude.use("downloads") : Promise.resolve(null))
    .then(function(x){ dl = x; dlReady = true; return x; })
    .catch(function(){ dlReady = true; return null; });
}
function save(filename, data, btn){
  var old = btn.textContent;
  downloads().then(function(d){
    if(!d){ btn.textContent = "No disponible"; setTimeout(function(){ btn.textContent = old; }, 2200); return; }
    return d.save({filename:filename, data:data}).then(function(){
      btn.textContent = "Guardado";
      setTimeout(function(){ btn.textContent = old; }, 1800);
    }).catch(function(err){
      var code = err && err.code;
      btn.textContent = code === "declined" ? "Cancelado" : (code === "too_large" ? "Muy grande" : "No se pudo");
      setTimeout(function(){ btn.textContent = old; }, 2200);
    });
  });
}
$("#dlBtn").onclick = function(){
  var d = byId[current];
  save(d.id.split("/").pop(), d.md, this);
};
$("#dlAll").onclick = function(){
  var parts = DOCS.map(function(d){
    return "<!-- ===== " + d.id + " ===== -->\n\n" + d.md;
  });
  save("expediente-del-misterio.md", parts.join("\n\n\n---\n\n\n"), this);
};
$("#dlNotes").onclick = function(){
  var out = ["# Notas de revisión\n"];
  GROUPS.forEach(function(g){
    var list = DOCS.filter(function(d){ return d.grupo === g.k; });
    if(!list.length) return;
    out.push("\n## " + g.n + "\n");
    list.forEach(function(d){
      var r = rec(d.id);
      if(r.status === "pendiente" && !r.nota) return;
      out.push("- **" + d.titulo + "** (`" + d.id + "`) — _" + r.status + "_"
               + (r.nota ? "\n  - " + r.nota.replace(/\n/g, "\n  - ") : ""));
    });
  });
  save("notas-de-revision.md", out.join("\n"), this);
};
$("#copyBtn").onclick = function(){
  var b = this, md = byId[current].md;
  var done = function(ok){
    b.textContent = ok ? "Copiado" : "Selecciona y copia";
    setTimeout(function(){ b.textContent = "Copiar"; }, 1800);
  };
  if(navigator.clipboard && navigator.clipboard.writeText){
    navigator.clipboard.writeText(md).then(function(){ done(true); }, function(){ done(false); });
  } else done(false);
};

/* ------------------------------------------------------------ publish */
function pageSource(){
  var b64 = document.getElementById("shell").textContent.trim();
  var bin = atob(b64), bytes = new Uint8Array(bin.length);
  for(var i=0;i<bin.length;i++) bytes[i] = bin.charCodeAt(i);
  var shell = new TextDecoder("utf-8").decode(bytes);
  STATE.updated = new Date().toISOString().slice(0,16).replace("T", " ");
  return "<!doctype html>\n<html lang=\"es\"><head><meta charset=\"utf-8\">"
       + "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"></head><body>\n"
       + shell.replace("__SHELL_B64__", function(){ return b64; })
              .replace("__CORPUS__", function(){ return document.getElementById("corpus").textContent; })
              .replace("__STATE__", function(){ return JSON.stringify(STATE); })
       + "\n</body></html>";
}
$("#saveBtn").onclick = function(){
  var btn = this, note = $("#saveNote");
  btn.disabled = true; note.dataset.tone = ""; note.textContent = "Guardando…";
  (window.claude && claude.use ? claude.use("artifact") : Promise.resolve(null))
  .then(function(a){
    if(!a) throw {code:"unavailable"};
    return a.publish(pageSource());
  })
  .then(function(){
    dirty = false; note.dataset.tone = "ok"; note.textContent = "Guardado";
    btn.disabled = false;
    setTimeout(function(){ if(!dirty) note.textContent = ""; }, 3000);
  })
  .catch(function(err){
    var c = err && err.code;
    note.dataset.tone = "bad";
    if(c === "conflict"){ note.textContent = "Hubo otra versión; recargando"; }
    else if(c === "not_writer" || c === "not_granted" || c === "consent_required"){
      readOnly = true; note.textContent = "Solo lectura"; btn.hidden = true;
    }
    else if(c === "rate_limited"){ note.textContent = "Espera un momento"; btn.disabled = false; }
    else { note.textContent = "No se pudo guardar"; btn.disabled = false; }
  });
};
window.addEventListener("beforeunload", function(e){ if(dirty){ e.preventDefault(); e.returnValue = ""; } });

/* ------------------------------------------------------------ keys + jumps */
document.addEventListener("keydown", function(e){
  var t = e.target.tagName;
  if(t === "INPUT" || t === "TEXTAREA"){
    if(e.key === "Escape") e.target.blur();
    return;
  }
  if(e.key === "/"){ e.preventDefault(); $("#find").focus(); return; }
  if(e.key === "j" || e.key === "k"){
    var vis = Array.prototype.filter.call(document.querySelectorAll(".item"), function(b){ return !b.classList.contains("hide"); });
    var ids = vis.map(function(b){ return b.dataset.id; });
    var n = ids.indexOf(current) + (e.key === "j" ? 1 : -1);
    if(n >= 0 && n < ids.length) open(ids[n]);
  }
});
$("#paper").addEventListener("click", function(e){
  var a = e.target.closest("[data-jump]"); if(!a) return;
  e.preventDefault();
  var here = current.split("/").slice(0,-1), rel = a.dataset.jump.split("/");
  rel.forEach(function(seg){
    if(seg === ".." ) here.pop();
    else if(seg !== "." && seg !== "") here.push(seg);
  });
  var target = here.join("/");
  if(byId[target]) open(target);
  else if(byId[target.replace(/\/$/,"") + "/README.md"]) open(target.replace(/\/$/,"") + "/README.md");
});

/* ------------------------------------------------------------ go */
$("#nfiles").textContent = DOCS.length + " documentos";
buildRail(); setView("docs"); open(DOCS[0].id);
if(STATE.updated) { $("#saveNote").textContent = "Revisión de " + STATE.updated; }
})();
</script>
"""

# ------------------------------------------------------------------- ensamble

def main():
    docs = recolectar()
    grupos = [{"k": k, "n": n} for k, n, _ in GRUPOS]

    estado = {"version": 1, "updated": "", "files": {}}
    if "--state" in sys.argv:
        sp = Path(sys.argv[sys.argv.index("--state") + 1])
        estado = json.loads(sp.read_text(encoding="utf-8"))
        print("estado reinyectado desde", sp)

    shell = SHELL.replace("__GROUPS__", json.dumps(grupos, ensure_ascii=False))
    b64 = base64.b64encode(shell.encode("utf-8")).decode("ascii")

    def j(o):
        return json.dumps(o, ensure_ascii=False).replace("</", "<\\/")

    html = (shell
            .replace("__SHELL_B64__", b64)
            .replace("__CORPUS__", j(docs))
            .replace("__STATE__", j(estado)))

    OUT.write_text(html, encoding="utf-8")
    kb = len(html.encode("utf-8")) / 1024
    print("visor.html  %d documentos  %.0f KB" % (len(docs), kb))
    for g in GRUPOS:
        n = len([d for d in docs if d["grupo"] == g[0]])
        print("   %-28s %d" % (g[1], n))

if __name__ == "__main__":
    main()
