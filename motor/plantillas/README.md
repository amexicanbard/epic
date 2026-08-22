# 📁 Plantillas
### Los siete documentos que forman un juego completo

---

## Cómo se usa esta carpeta

```
1. Copia TODA esta carpeta a  juegos/mi-juego-nuevo/
2. Borra este README de la copia
3. Busca y reemplaza los marcadores globales en todos los archivos de una vez
4. Duplica plantilla-hoja-personaje.md una vez por personaje y llena los {{P_...}}
5. Renombra los archivos quitando el prefijo "plantilla-"
6. Corre la lista de verificación de ../01-guia-de-autoria.md
```

**Antes de tocar nada de aquí**, llena las nueve tablas de
**[../02-hoja-de-diseno.md](../02-hoja-de-diseno.md)**. Rellenar plantillas sin haber hecho el
diseño es la forma más rápida de terminar con un juego roto.

---

## Los archivos

| Archivo | Quién lo lee | Cuántas copias se imprimen |
|---|---|---|
| `plantilla-guia-del-anfitrion.md` | Solo el anfitrión | 1 |
| `plantilla-como-jugar.md` | Todos | 1 o una por jugador |
| `plantilla-hoja-personaje.md` | Un jugador | **Duplícala por personaje.** 1 por jugador, solo la suya |
| `plantilla-evidencias.md` | Solo el anfitrión | 1 |
| `plantilla-cartas.md` | Se reparten | 1 carta por jugador |
| `plantilla-menus.md` | Todos | 1 por comensal (solo mesa sentada) |
| `plantilla-invitaciones.md` | Se envían | 1 por invitado |
| `plantilla-boletas.md` | Todos | 1 boleta por jugador |

---

## Marcadores

El diccionario completo está en
**[../00-el-motor.md](../00-el-motor.md#9-diccionario-de-marcadores)**.

**Globales** (mismos en todos los archivos): `{{JUEGO}}` `{{SEDE}}` `{{OCASION}}` `{{VICTIMA}}`
`{{VICTIMA_CORTO}}` `{{INCIDENTE}}` `{{PREGUNTA_CENTRAL}}` `{{CULPABLE_ROL}}` `{{OBJETO_CLAVE}}`
`{{VENTANA}}` `{{HORA_DESCUBRIMIENTO}}` `{{RASTRO}}` `{{N_PERSONAJES}}` `{{EDAD_MINIMA}}`

**Por personaje** (solo en la hoja, las cartas y las invitaciones): todos empiezan con `{{P_`.

**Truco:** haz el reemplazo global primero, en todos los archivos a la vez. Después, personaje por
personaje. Si al final buscas `{{` y no aparece nada, terminaste.

---

## Ejemplo ya rellenado

Si en algún momento no sabes qué va en un marcador, abre el juego
[**La Herencia de la Abuela**](../../juegos/la-herencia-de-la-abuela/): está hecho con estas mismas
plantillas, sin excepciones. Las catorce hojas de `personajes/` son
`plantilla-hoja-personaje.md` rellenada catorce veces.

---

## Verificación rápida antes de imprimir

- ☐ Busqué `{{` en todos los archivos y no queda ninguno
- ☐ El número de cartas de sorteo = número de jugadores, y **solo una** dice culpable
- ☐ Cada hoja de personaje trae su presentación, sus 3 datos, sus 9 preguntas y **las dos ramas**
- ☐ Ninguna evidencia señala a menos de tres personas
- ☐ Los personajes tienen todos un hueco en su coartada
- ☐ Corrí la **prueba de los catorce**: con cualquiera de culpable, la historia cierra
