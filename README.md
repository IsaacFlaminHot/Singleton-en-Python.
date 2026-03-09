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

