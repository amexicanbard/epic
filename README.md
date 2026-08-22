# 🕯️ Máquina de Juegos de Misterio

**Un motor para escribir juegos de Murder Mystery Party en español, y los juegos hechos con él.**

---

## La idea

La mecánica es siempre la misma. Lo que cambia es la historia.

En lugar de escribir un juego, este repositorio separa **el motor** (las reglas, los tres actos, el
sorteo del culpable, la estructura de evidencias) del **contenido** (quién es la víctima, qué pasó,
quiénes son los sospechosos). Escribes el contenido, rellenas las plantillas, y sale un juego
completo listo para imprimir.

**Lo que define a estos juegos:**

- **El culpable se sortea la misma noche**, con cartas, delante de todos. Nadie lo sabe de
  antemano — ni el anfitrión, que por eso puede jugar. El mismo juego se repite con la misma gente
  y da otro resultado.
- **Nadie tiene que actuar.** Cada hoja de personaje trae las respuestas escritas palabra por
  palabra: te preguntan, buscas y lees. Quien quiera ponerle acento y drama, se lo pone encima.
- **Nadie es relleno.** Todos los sospechosos tienen motivo, un secreto vergonzoso y media hora sin
  testigos.
- **El crimen no tiene que ser un asesinato.** Un robo, un fraude, un sabotaje o una filtración
  funcionan igual.

---

## Cómo está organizado

```
motor/            ← las reglas y las plantillas. Aquí se escriben juegos nuevos
  00-el-motor.md          las reglas invariables y las 5 leyes de diseño
  01-guia-de-autoria.md   los 7 pasos para escribir un juego, con fórmulas
  02-hoja-de-diseno.md    las 9 tablas vacías que se llenan antes de escribir
  plantillas/             los 8 documentos de un juego, con marcadores {{ASÍ}}

juegos/           ← los juegos terminados, listos para imprimir y jugar
  asesinato-en-la-mansion/
  la-herencia-de-la-abuela/
```

---

## Los juegos

### 🕯️ [La Herencia de la Abuela](juegos/la-herencia-de-la-abuela/)
*6–14 jugadores · 18+ · 2–3 horas · Monterrey*

Se murió doña Chayo, de vieja, dormida. Nueve días después, en el último rosario del novenario, el
notario abre el sobre del testamento delante de toda la familia. **Está vacío.** Adentro solo hay
una hoja arrancada de su libreta que dice, con su letra: *«Ya saben quién.»*

Con la tía que la cuidó seis años, el tío que lleva veinte «en proyectos», el primo que estudió
letras, el sobrino de la troca y la señora que lleva treinta y cuatro años en esa cocina.

### 🎩 [Asesinato en la Mansión](juegos/asesinato-en-la-mansion/)
*6–14 jugadores · 18+ · 2–3 horas · Gótico inglés*

Lord Heathcliff celebra su boda en su mansión. A las 21:15 sale a fumar a la terraza. A las 22:04
aparece flotando en la piscina con la nuca hundida y un candelabro de plata en el fondo.

Con la viuda joven, el ama de llaves de cuarenta años de servicio, la médium que predijo la muerte
por escrito y un detective francés que nunca ha resuelto un caso.

> **Nota:** este fue el primer juego y está escrito en el formato antiguo, semi-guionado (datos y
> frases sugeridas, pero el jugador arma sus respuestas). *La Herencia de la Abuela* usa el formato
> nuevo de **guion cerrado**, donde el jugador solo lee. Se puede convertir cuando haga falta.

---

## Escribir un juego nuevo

1. Lee **[motor/00-el-motor.md](motor/00-el-motor.md)** una vez. Son las reglas que no cambian.
2. Llena las nueve tablas de **[motor/02-hoja-de-diseno.md](motor/02-hoja-de-diseno.md)**.
   *No escribas prosa antes de tener la estructura.*
3. Sigue los siete pasos de **[motor/01-guia-de-autoria.md](motor/01-guia-de-autoria.md)**:
   incidente → reparto → motivos → secretos → coartadas → red de datos → evidencias.
4. Copia **[motor/plantillas/](motor/plantillas/)** a `juegos/tu-juego/` y reemplaza los
   marcadores.
5. Corre la lista de verificación y **la prueba de los catorce**: toma cada personaje, di «este
   fue» y comprueba que la historia cierra. Si con alguno no cierra, ese personaje está roto.

Unas cuatro horas la primera vez. Dos, la tercera.

---

## Las cinco leyes de diseño

Lo que hace que el motor funcione con culpable aleatorio. Están explicadas con ejemplos en la
[guía de autoría](motor/01-guia-de-autoria.md).

| Ley | Qué dice |
|---|---|
| **Del hueco** | Todo personaje tiene entre 6 y 30 minutos sin testigos. Nadie queda limpio |
| **Del tres** | Ninguna evidencia puede señalar a menos de tres personajes |
| **Del espejo** | El motivo es público; el secreto es privado y no tiene que ver con el crimen |
| **Del triángulo** | Cada personaje sabe exactamente tres cosas verdaderas sobre otros |
| **De la frase** | Cada culpable actuó por UNA frase concreta que la víctima le dijo |

---

*Obra original en español. La mecánica de misterio por actos con culpable sorteado es un formato de
juego de uso libre; todos los personajes, textos y evidencias de este repositorio son creación
propia.*
