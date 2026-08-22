# ⚙️ EL MOTOR
### Las reglas que nunca cambian, sin importar la historia

> Este documento describe la **mecánica pura**. No habla de mansiones, ni de herencias, ni de
> ningún personaje. Es el esqueleto que se rellena con cualquier narrativa.
>
> Si vas a escribir un juego nuevo, lee esto una vez, y después trabaja con
> **[01-guia-de-autoria.md](01-guia-de-autoria.md)**, que es el manual de instrucciones.

---

## 1. Qué es este motor

Un sistema para armar juegos de misterio para fiestas donde:

- **El culpable se sortea la misma noche.** Nadie lo sabe de antemano, ni el anfitrión. El mismo
  juego se puede repetir con la misma gente y dar otro resultado.
- **Nadie tiene que actuar.** Cada jugador recibe una hoja con respuestas escritas palabra por
  palabra. Busca la pregunta que le hicieron y lee. Quien quiera actuar, actúa encima.
- **No hay personajes de relleno.** Todos tienen motivo, secreto y coartada con agujeros.
- **El anfitrión juega.** Solo tiene tres trabajos extra: repartir, leer evidencias y marcar
  el ritmo.

**El crimen no tiene que ser un asesinato.** El motor funciona igual con un robo, un fraude, un
sabotaje, una traición, una filtración o una carta anónima. Lo único que necesita es: **un hecho
irreversible, una ventana de tiempo, y un grupo cerrado de personas que estuvo ahí.**

---

## 2. Los cinco componentes obligatorios

Todo juego construido con este motor tiene exactamente estas cinco piezas. Si te falta una, el
juego no funciona.

| # | Componente | Qué es | Cuántos |
|---|---|---|---|
| **1** | **El Incidente** | Lo que pasó. Irreversible, con hora y objeto | 1 |
| **2** | **El Reparto** | Los sospechosos, cada uno con motivo + secreto + coartada + datos | 6 a 14 |
| **3** | **La Red de Coartadas** | Quién estaba dónde, con quién, y el hueco de cada uno | 1 por personaje |
| **4** | **Las Evidencias** | 4 tandas: inicial, Acto 1, Acto 2, Acto 3 | 6 + 4 + 5 + 4 |
| **5** | **Las Cartas** | N−1 de INOCENTE, 1 de CULPABLE | 1 por jugador |

---

## 3. La estructura de la noche

Esto es fijo. No lo cambies.

```
  LLEGADA
     │
     ├─ Presentaciones en personaje (cada quien lee su presentación)
     ├─ REPARTO DE CARTAS  ← aquí nace el culpable
     └─ Lectura privada (5 min: cada quien lee su rama INOCENTE o CULPABLE)
     │
  EVIDENCIA INICIAL  (6 hechos)  ─── el anfitrión lee en voz alta
     │
  ╔═ ACTO 1 ═══════════════════════════════ 30-40 min ═╗
  ║  Tema: MOTIVOS. Quién ganaba algo con el incidente. ║
  ║  Cierre: evidencias E1.1 a E1.4                     ║
  ╚═════════════════════════════════════════════════════╝
     │
  ╔═ ACTO 2 ═══════════════════════════════ 35-45 min ═╗
  ║  Tema: COARTADAS. Dónde estaba cada quien.          ║
  ║  ★ Declaración pública de coartadas (obligatoria)   ║
  ║  Cierre: evidencias E2.1 a E2.5                     ║
  ╚═════════════════════════════════════════════════════╝
     │
  ╔═ ACTO 3 ═══════════════════════════════ 30-40 min ═╗
  ║  Tema: SECRETOS. Se acaba la protección.            ║
  ║  Cierre: evidencias E3.1 a E3.4                     ║
  ║  ★ LA ÚLTIMA VERDAD (10 min)                        ║
  ╚═════════════════════════════════════════════════════╝
     │
  VOTACIÓN  →  ALEGATOS  →  REVELACIÓN  →  CONFESIÓN
```

**Por qué los tres actos son así y no de otra forma:**

- **Acto 1 = motivos.** Todos quedan bajo sospecha por igual. Nadie tiene que recordar horarios
  todavía; solo hay que odiar a la víctima, y eso es fácil y divertido.
- **Acto 2 = coartadas.** Aquí entra la información dura. La declaración pública en voz alta es el
  corazón del juego: es donde se generan las contradicciones que después se explotan.
- **Acto 3 = secretos.** Se levanta la protección, todo el mundo confiesa cosas horribles que no
  tienen nada que ver con el crimen, y el ruido tapa la señal. Es el acto más divertido.

---

## 4. Las cinco reglas de oro

Se leen en voz alta antes del Acto 1 y van impresas en cada hoja de personaje.

**1. Todos se declaran inocentes.** Nadie admite nada hasta la revelación final.

**2. Los inocentes no pueden mentir sobre hechos.** Ante una pregunta directa, leen la respuesta
que trae su hoja. Pueden ser evasivos, ofenderse o cambiar de tema, pero si insisten, contestan.

**3. Los inocentes sí pueden ocultar su secreto… hasta el Acto 3.** En el Acto 3 están obligados a
confesarlo si se lo preguntan de frente.

**4. El culpable miente en lo que quiera.** Es la única persona sin obligación de decir la verdad.
Una sola excepción: **La Última Verdad**.

**5. No se registran bolsillos, bolsos ni celulares ajenos.** Se investiga con la boca.

**Y la regla que más se olvida:** nadie enseña su carta a nadie, nunca, ni de broma. El único que
la muestra es el culpable, al final.

---

## 5. El sorteo

```
  N jugadores  →  N cartas
                  ├─ 1 carta:  "TÚ LO HICISTE"
                  └─ N−1 cartas: "ERES INOCENTE"
```

1. Todas las cartas se imprimen **en la misma hoja, del mismo papel**, y se cortan juntas.
2. Se baraja **a la vista de todos**, boca abajo. Alguien corta el mazo.
3. Se reparte una carta boca abajo a cada jugador, **incluido el anfitrión**.
4. Todos miran su carta pegada al pecho y se la guardan.
5. Cinco minutos de pausa privada: cada quien lee en su hoja la rama que le tocó.

**Por qué el anfitrión puede jugar:** porque las cartas son genéricas. El motivo específico está
en la hoja del personaje, no en la carta. El anfitrión reparte sin saber qué reparte.

---

## 6. La Última Verdad

Mecánica del Acto 3. Es lo que convierte la votación en deducción y no en corazonada.

> Después de la última evidencia, el anfitrión anuncia: **la primera pregunta de hecho que alguien
> le haga directamente al culpable, el culpable tiene que contestarla con la verdad.** Una sola.
> Después vuelve a mentir. No vale preguntar "¿fuiste tú?": tiene que ser sobre un hecho concreto
> —dónde estuvo, qué tocó, a quién vio, qué hora era—. Diez minutos.

- Solo aplica al culpable, una vez, y solo después del anuncio.
- **Contrajugada del culpable:** provocar rápido una pregunta trivial para quemar la obligación
  con algo inofensivo. Es legal y es astuto.
- **Jugada del detective:** no preguntar nada hasta tener lista la pregunta que mata, y hacérsela
  a todos, uno por uno, en voz alta.

---

## 7. Votación y puntajes

Cada jugador escribe **a quién acusa** y **por qué motivo**, en silencio. El culpable también vota,
y le conviene votar por otro.

| Logro | Puntos |
|---|---|
| Acertar quién fue | **2** |
| Acertar además el motivo | **+1** |
| Ser el culpable y que te acuse menos de la mitad de la mesa | **3** |
| Ser el culpable y que no te acuse nadie | **5** |
| Confesar tu secreto voluntariamente en el Acto 3 | **+1** |
| Mejor interpretación / mejor disfraz (voto a mano alzada) | **+1** c/u |

Después de la votación: revelación (*«que se ponga de pie quien tenga la carta que dice TÚ LO
HICISTE»*), el culpable muestra su carta y **lee su confesión** desde su hoja.

---

## 8. Las leyes de diseño

Estas cinco leyes son lo que hace que el motor funcione con culpable aleatorio. Rómpelas y el
juego se desarma. Están explicadas con ejemplos en la
**[guía de autoría](01-guia-de-autoria.md)**.

### Ley 1 — Ley del hueco
**Todo personaje, sin excepción, tiene un hueco en su coartada de entre 6 y 30 minutos.**
Nadie puede quedar limpio, porque cualquiera puede resultar culpable.

### Ley 2 — Ley del tres
**Ninguna evidencia puede apuntar a menos de tres personajes.**
Si una evidencia señala a uno solo, el juego se acaba cuando la lees.

### Ley 3 — Ley del espejo
**El motivo es público; el secreto es privado y no tiene que ver con el crimen.**
El motivo es lo que todos sospechan. El secreto es peor, es vergonzoso, y es una pista falsa
andante. Los secretos son los que hacen que los inocentes parezcan culpables.

### Ley 4 — Ley del triángulo
**Cada personaje sabe exactamente tres cosas verdaderas sobre otros personajes.**
Cada personaje es, a su vez, conocido por unos tres. Así se teje la red: preguntar siempre
produce información, y ninguna persona concentra todo.

### Ley 5 — Ley de la frase detonante
**Cada personaje culpable actuó por UNA frase concreta que la víctima le dijo.**
No por dinero abstracto, no por "resentimiento acumulado": por una frase, dicha en un lugar, a
una hora. Esa frase es el corazón de la confesión y es lo que hace que el final funcione.

---

## 9. Diccionario de marcadores

Las plantillas de **[plantillas/](plantillas/)** usan estos marcadores. Reemplázalos todos.
Cualquier editor de texto hace buscar-y-reemplazar; también sirve el buscador de Google Docs.

### Marcadores globales

| Marcador | Qué va ahí | Ejemplo (Mansión) | Ejemplo (Herencia) |
|---|---|---|---|
| `{{JUEGO}}` | Título del juego | Asesinato en la Mansión | La Herencia de la Abuela |
| `{{SEDE}}` | Dónde pasa todo | la mansión Pantano Húmedo | la casa de la abuela en San Pedro |
| `{{OCASION}}` | Por qué está reunida la gente | la cena de boda de Lord Heathcliff | el novenario de doña Chayo |
| `{{VICTIMA}}` | Nombre completo del centro del caso | Lord Reginald Heathcliff | Rosario "Chayo" Villarreal |
| `{{VICTIMA_CORTO}}` | Cómo lo llaman | el Lord | la abuela |
| `{{INCIDENTE}}` | Qué pasó, en una frase | lo mataron de un golpe y lo ahogaron | desapareció el testamento |
| `{{PREGUNTA_CENTRAL}}` | Lo que hay que resolver | ¿Quién lo mató y por qué? | ¿Quién se lo llevó y por qué? |
| `{{CULPABLE_ROL}}` | Cómo se le dice al culpable | el asesino | el que se lo llevó |
| `{{OBJETO_CLAVE}}` | El arma / el objeto del delito | el candelabro de plata | el sobre de la notaría |
| `{{VENTANA}}` | La ventana de tiempo | entre las 21:15 y las 21:45 | entre las 20:15 y las 20:50 |
| `{{HORA_DESCUBRIMIENTO}}` | Cuándo se supo | 22:04 | 21:00 |
| `{{RASTRO}}` | La pista física ambigua del inicio | un botón de latón | una nota que dice «Ya saben quién» |

### Marcadores por personaje

| Marcador | Qué va ahí |
|---|---|
| `{{P_NOMBRE}}` | Nombre del personaje |
| `{{P_ETIQUETA}}` | Quién es, en una línea |
| `{{P_PRESENTACION}}` | El párrafo que lee en voz alta al presentarse |
| `{{P_MOTIVO}}` | Su motivo **público** (lo que todos sospechan) |
| `{{P_SECRETO}}` | Su secreto **privado** (vergonzoso, no relacionado con el crimen) |
| `{{P_COARTADA}}` | Dónde estaba durante la ventana |
| `{{P_TESTIGO}}` | Quién lo vio (o "nadie") |
| `{{P_HUECO}}` | Los minutos en que estuvo solo, y por qué |
| `{{P_DATO_1}}` a `{{P_DATO_3}}` | Las tres cosas verdaderas que sabe de otros |
| `{{P_FRASE}}` | La frase detonante que le dijo la víctima |
| `{{P_COMO}}` | Cómo lo hizo, si es culpable |
| `{{P_MENTIRA}}` | La mentira que sostiene si es culpable |
| `{{P_CONFESION}}` | Su confesión final, para leer en voz alta |
| `{{P_DISFRAZ}}` | Qué ponerse |
| `{{P_ACCESORIO}}` | El objeto que hace el personaje |

---

## 10. Qué NO cambiar

Puedes cambiar absolutamente todo el contenido. Estas ocho cosas son el motor y si las tocas
tienes otro juego, no una variante de este:

1. El culpable se sortea la misma noche, con cartas, delante de todos.
2. Tres actos + evidencia inicial, en ese orden y con esos tres temas.
3. Todos tienen motivo, secreto, coartada con hueco y tres datos sobre otros.
4. Los inocentes no mienten sobre hechos; el culpable miente en todo.
5. Los secretos se protegen hasta el Acto 3 y ahí se caen.
6. La declaración pública de coartadas, en voz alta, en el Acto 2.
7. La Última Verdad en el Acto 3.
8. Votación en silencio → alegatos → revelación → confesión leída.
