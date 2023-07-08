
# PYGAME SOULS

Bienvenidos a PYGAME SOULS, un proyecto hecho en PYGAME para la entrega final de Programación 1 y Lab. Programación 1 de la Tecnicatura de Programación Superior en UTN FRA.

ALUMNO:
Joaquín Abal
Div E

## Descripción del juego

PYGAME SOULS es un juego de plataformas y acción 2D, en el cuál tu objetivo es avanzar en los niveles dentro del bosque oscuro, para poder derrotar al Rey Esqueleto.

En este juego, controlas a Adventurer, un arquero cuyo pueblo fue destruido por los séquitos del Rey Esqueleto y que se encuentra con sed de venganza.

![adventurer](https://github.com/joaquinabal/game_py_new/assets/88854241/4a1299d2-d189-4e8b-9ac2-9c032546955d)
## Controles
Para controlar a nuestro héroe, podremos utilizar las siguientes teclas:

TECLA →: movimiento hacia la derecha.

TECLA ←: movimiento hacia la izquierda

TECLA BARRA ESPACIADORA: salto

TECLA Q: disparar flecha. (Necesitas cargar el ataque para que sea lanzado!)
## Cómo avanzar de nivel
El juego consta de tres niveles.
Tanto para el primer como para el segundo, el objetivo es acumular una cantidad de puntos necesaria.

En el caso del nivel 3, el objetivo para ganar es derrotar al Rey Esqueleto. Ten cuidado! Este enemigo es más resistente que sus esbirros, deberás golpearlo varias veces.
## Cómo perder
Nuestro héroe posee 5 vidas. Hay varias maneras de perder una vida:

- Al tocar o ser tocado por un enemigo.
- Al recibir un proyectil de un enemigo.
- Al encontrarnos en el piso cuando el Rey Esqueleto golpea el piso.

Sabrás que habrás perdido una vida, porque el escenario tomará un color rojizo.

A su vez, cada nivel tiene un tiempo de 120 segundos, en el caso de que el tiempo llegue a cero, perderás el nivel y volverás al menu principal.

## Enemigos

### - Mushroom:
![mushroom](https://github.com/joaquinabal/game_py_new/assets/88854241/fc5db7f7-f0db-4045-a318-d2a298f31326)

Estos hongos eran amigos del bosque, pero fueron corrompidos por el Rey Esqueleto, cuidado al tocarlos!

### - Ojo Volador:
![oneye](https://github.com/joaquinabal/game_py_new/assets/88854241/c862f782-a7fd-4e96-b9a6-d1032c1c2467)

Estos esbirros fueron productos de una mutación en los murciélagos de la zona, suelen volar en busca de un enemigo. Si te llegan a ver, te dispararán!

### - Esqueleto:
![skeleton](https://github.com/joaquinabal/game_py_new/assets/88854241/ad4a2341-1ea8-46b1-b51d-6673e86e8f9c)

Soldados leales del Rey Esqueleto. Aparecen cada vez que el Rey Esqueleto golpea el piso.

### - Rey Esqueleto
![boss](https://github.com/joaquinabal/game_py_new/assets/88854241/29401a77-cd2b-4192-8df6-a634e5132f68)

El Jefe Final. Es considerado el culpable de la corrupción del bosque. No te perseguirá, no cree necesario hacer ese esfuerzo, en cambio, golpeará el piso con tal fuerza que te lanzará por los aires. 
## Consumibles
### - Monedas ![coin_points](https://github.com/joaquinabal/pygame_pp1_lab_joaquin_abal/assets/88854241/4305e808-7f3c-4041-b96d-14a1a00229a5)

Las monedas son el botín proveniente de la muerte de tus enemigos. Las monedas suman 300 puntos.

### Corazón Corrompido ![bad_heart](https://github.com/joaquinabal/pygame_pp1_lab_joaquin_abal/assets/88854241/b7ede235-1f0b-4515-9e79-3fd34fdb32fd)

Aunque parezcan que nos ayudarán a curarnos, estos corazones ya fueron corrompidos por el Rey Esqueleto. Si llegamos a tocar uno, perderemos una vida.

