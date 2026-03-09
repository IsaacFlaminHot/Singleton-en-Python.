# TECNOLÓGICO NACIONAL DE MÉXICO  
## INSTITUTO TECNOLÓGICO DE TIJUANA  

### SUBDIRECCIÓN ACADÉMICA  
### DEPARTAMENTO DE SISTEMAS Y COMPUTACIÓN  

---

**SEMESTRE:** Enero - Julio 2026  
**CARRERA:** Ingeniería en Sistemas Computacionales  
**MATERIA:** Patrones de Diseño  
**UNIDAD A EVALUAR:** Unidad 2  

---

**Alumno:** Jair Isaac Perez Ricardez  
**Matrícula:** 21211920  

---

# Implementación del Patrón Singleton en una Central de Emergencias 911

## 1. Descripción General

Este proyecto implementa el **patrón de diseño Singleton** en Python para simular una **Central de Emergencias 911**. En este escenario, es crítico que todas las llamadas sean gestionadas por **una única instancia del sistema central** para evitar la fragmentación de la información y asegurar una respuesta coordinada.

### El Patrón Singleton
El objetivo es garantizar que una clase tenga **una única instancia** y proporcionar un punto de acceso global a ella. En este sistema:
* `Central_911` es la instancia única (Singleton).
* `Operador` representa a los distintos usuarios que interactúan con el sistema.



---

## 2. Estructura del Código

El código se divide en tres bloques fundamentales para mantener la cohesión y el orden:

### A. Clase Singleton `Central_911`
Utiliza un mecanismo de **Thread-Safe** (seguro para hilos) mediante un bloqueo (`Lock`), asegurando que incluso en condiciones de alta concurrencia, solo se cree una central.

```python
import threading

class Central_911:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        # Atributo de inicialización única
        self.central = "Central 911"

    @classmethod
    def obtener_instancia(cls):
        """Implementación de Singleton con Double-Checked Locking"""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance

    def conectar_llamada(self, operador, tipo_emergencia):
        print(f"[{self.central}] Conectando llamada con {operador.nombre}...")
        operador.atiende_emergencia(tipo_emergencia)

class Operador:
    def __init__(self, id_operador, nombre):
        self.id_operador = id_operador
        self.nombre = nombre

    def atiende_emergencia(self, tipo_emergencia):
        # Diccionario de despacho de unidades
        unidades = {
            "Intento de suicidio": "Unidades de Rescate Psicológico",
            "Incendio": "Cuerpo de Bomberos",
            "Accidente de tráfico": "Ambulancia y Policía Vial",
            "Violeta": "Patrulla de Protección Familiar",
            "Robo": "Policía Municipal",
            "Infarto": "Ambulancia Paramédica"
        }
        
        respuesta = unidades.get(tipo_emergencia, "Unidades Generales de Emergencia")
        print(f" > Operador {self.nombre} despachando: {respuesta}\n")

if __name__ == "__main__":
    # Intentamos obtener la instancia desde distintos puntos
    llamada1 = Central_911.obtener_instancia()
    llamada2 = Central_911.obtener_instancia()
    llamada3 = Central_911.obtener_instancia()
    llamada4 = Central_911.obtener_instancia()

    # Operadores disponibles
    op1 = Operador(1, "Laura")
    op2 = Operador(2, "Carlos")  
    op3 = Operador(3, "Ana")
    op4 = Operador(4, "Miguel")

    print("--- SIMULACIÓN DE CENTRAL 911 ---")
    llamada1.conectar_llamada(op1, "Incendio")
    llamada2.conectar_llamada(op2, "Violeta")
    llamada3.conectar_llamada(op3, "Robo")
    llamada4.conectar_llamada(op4, "Infarto")

    print("--- VERIFICACIÓN DEL PATRÓN SINGLETON ---")
    print(f"¿Llamada 1 y 2 son la misma instancia?: {llamada1 is llamada2}")
    print(f"¿Llamada 3 y 4 son la misma instancia?: {llamada3 is llamada4}")

```

### El Atributo Estático de la Instancia (`_instance`)
En el desarrollo de software, un atributo estático es una variable que pertenece a la **clase** y no a los objetos individuales. 

* **Identificación en el código:** Se define al inicio de la clase como `_instance = None`.
* **Explicación:** Este atributo es el **pilar del Singleton**. Funciona como un contenedor global dentro de la clase que almacena la referencia al único objeto creado. Al ser estático, su valor persiste durante toda la ejecución del programa. Todas las llamadas al método de acceso consultan primero este atributo; si ya contiene un objeto, se devuelve ese mismo, evitando duplicidad.

### El Constructor (`__init__`)
El constructor es el método encargado de inicializar el estado de un objeto nuevo.

* **Identificación en el código:** Se define mediante el método especial `def __init__(self):`.
* **Explicación:** En una implementación Singleton, el constructor no debe ser invocado libremente por el usuario. Su función es configurar los atributos iniciales (como el nombre de la central o la lista de operadores) **una sola vez**. En Python, aunque no podemos bloquearlo totalmente como en otros lenguajes, controlamos su ejecución a través del método estático de obtención, asegurando que la configuración inicial ocurra solo cuando se crea la instancia original.

---

## ¿Por qué no se pueden crear múltiples objetos?

La restricción para evitar la creación de múltiples instancias de la `Central_911` se basa en tres mecanismos de control:

1. **Intercepción del Punto de Acceso:** No permitimos que el flujo del programa utilice la creación estándar de objetos. En su lugar, obligamos al uso de `obtener_instancia()`. Este método actúa como un **filtro inteligente** que decide si es necesario fabricar un objeto o entregar uno ya existente.
2. **Identidad de Memoria Única:** Independientemente de cuántas variables intenten "crear" la central (ej. `llamada1`, `llamada2`, `llamada3`), el método de control siempre retorna la **misma dirección de memoria**. En términos de Python, esto significa que `id(llamada1) == id(llamada2)`.
3. **Control de Concurrencia (Thread-Safety):** Para evitar que en sistemas con múltiples hilos se creen dos centrales por accidente al mismo tiempo, se implementa un **Bloqueo (Lock)**. Esto garantiza que el proceso de "preguntar y crear" sea atómico: solo una solicitud puede entrar a la vez, asegurando que la segunda solicitud siempre encuentre la instancia ya creada por la primera.

## Diagrama UML

classDiagram
    class Central_911 {
        -static _instance: Central_911
        -static _lock: Lock
        +central: String
        +static obtener_instancia() Central_911
        +conectar_llamada(operador, tipo)
    }

    class Operador {
        +id_operador: int
        +nombre: String
        +atiende_emergencia(tipo)
    }

    Central_911 --> Operador : "asigna llamada a"

## 3. Conclusiones

Creo que poco a poco va teniendo mas logica el uso funcional de estos patrones, en este caso, aprendi algo nuevo, como el threading, y el tema de los hilos a la hora de querer invocar varias instancia y verificar que ya exista una sola. Un patron que definitivamente necesito explorar más.

