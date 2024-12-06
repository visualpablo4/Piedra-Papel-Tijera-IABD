# Piedra-Papel-Tijera-IABD

IES de Teis - Curso de especialización en Inteligencia Artificial y Big Data
==================================================================================================================

### Información
Este proyecto esta hecho por el alumno: **Pablo Conde Soto**
Durante el proyecto me referiré al juego con el nombre de RPS (por sus siglas en inglés, Rock, Paper and Scissors)

### ¿En qué consiste el proyecto?
Este proyecto es una práctica del Curso de Especialización de Inteligencia Artificial y Big Data.
Consiste en la creación de un agente inteligente para jugar al juego: Piedra, papel y tijera.
El juego será CPU vs Humano.

### Especificación del entorno de trabajo
| Entorno de trabajo | Observable | Determinista | Episódico | Estático | Discreto | Conocido | Agentes |
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| RPS | Parcialmente observable | Estocástico | Secuencial | Estático | Discreto | Conocido | Multiagente competitivo |

#### Totalmente observable VS Parcialmente observable
Se trata de un entorno **parcialmente observable** dado que en el RPS ningún jugador puede saber que elección realizará su rival, por lo tanto no tienes acceso completo al estado del mundo antes de tomar una decisión.

#### Determinista VS Secuencial
Se trata de un entorno **estocástico** dado que el movimiento de tu rival no puede ser anticipado con certeza, por lo tanto el resultado de la partida depende de la acción tomada por cada jugador (computadora y humano).

#### Episódico VS Secuencial
Se trata de un entorno **secuencial** dado que en este proyecto, para desarrollar las estrategias de la computadora, se creará un historial de todas las partidas de cada jugador para que en base a esas estadísticas podamos desarrollar las mejores estrategias. Teniendo en cuenta esto, las rondas no son completamente independientes y las decisiones del jugador humano presente afectarán a las decisiones futuras de la computadora,por esta razón considero que el entorno de este proyecto será **secuencial**.

#### Estático VS Dinámico
Se trata de un entorno **estático** dado que en el RPS, en cada ronda, el estado del mundo no cambia hasta que ambos jugadores realizan una acción, además ambos jugadores podrían tomarse todo el tiempo que quieran para tomar su decisión y el estado del mundo no cambiaría.

#### Discreto vs Continuo
Se trata de un entorno **discreto** dado que ambos jugadores tienen un conjunto limitado y finito de acciones posibles (piedra, papel o tijera) y también tienen un número limitado de combinaciones posibles (tijera vs piedra, papel vs tijera, etc).

#### Conocido VS Desconocido
Se trata de un entorno **conocido** dado que ambos agentes conocen y entienden las reglas del juego y no necesitan aprender sobre el entorno.

#### Agente individual VS Multiagente
Se trata de un entorno de un sistema **multiagente competitivo** dado que hay dos agentes interactuando (la computadora y el jugador humano en este caso) y son éstos los cuales toman las decisiones que afectan directamente al resultado de cada ronda. Es de tipo claramente competitivo ya que los dos agentes compiten por ganar y no hay ningún tipo de cooperación en este juego.