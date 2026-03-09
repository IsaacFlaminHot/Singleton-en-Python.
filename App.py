import threading

# Singleton Central_911
class Central_911:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        self.central = "Central 911"
    
    @classmethod
    def obtener_instancia(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance
    
    def conectar_llamada(self, operador, tipo_emergencia):
        print(f"\nLlamada conectada con el operador {operador.nombre}")
        operador.atiende_emergencia(tipo_emergencia)

# Class Operador 
class Operador:
    def __init__(self, id_operador, nombre):
        self.id_operador = id_operador
        self.nombre = nombre
    
    def atiende_emergencia(self, tipo_emergencia):
        print(f"Operador {self.nombre} atendiendo emergencia de tipo: {tipo_emergencia}")

        if tipo_emergencia == "Intento de suicidio":
            print("Enviando unidades de apoyo y rescate.")

        elif tipo_emergencia == "Incendio":
            print("Enviando unidades de bomberos.")

        elif tipo_emergencia == "Accidente de tráfico":
            print("Enviando unidades de ambulancia y policía.")

        elif tipo_emergencia == "Violeta":
            print("Enviando una patrulla.")

        elif tipo_emergencia == "Robo":
            print("Enviando unidades de policía.")

        elif tipo_emergencia == "Infarto":
            print("Enviando unidades de ambulancia.")

        else:
            print("Tipo de emergencia no reconocido. Enviando unidades de emergencia generales.")

#Main

if __name__ == "__main__":

    llamada1 = Central_911.obtener_instancia()
    llamada2 = Central_911.obtener_instancia()
    llamada3 = Central_911.obtener_instancia()
    llamada4 = Central_911.obtener_instancia()

    op1 = Operador(1, "Laura")
    op2 = Operador(2, "Carlos")  
    op3 = Operador(3, "Ana")
    op4 = Operador(4, "Miguel")

    llamada1.conectar_llamada(op1, "Incendio")
    llamada1.conectar_llamada(op2, "Violeta")
    llamada3.conectar_llamada(op3, "Robo")
    llamada1.conectar_llamada(op1, "Accidente de tráfico")
    llamada2.conectar_llamada(op2, "Intento de suicidio")
    llamada3.conectar_llamada(op3, "Desconocido")
    llamada4.conectar_llamada(op4, "Infarto")

    

    print(f"\nReferenceEquals:", llamada1 is llamada2)
    print(f"ReferenceEquals:", llamada2 is llamada4)
    print(f"ReferenceEquals:", llamada1 is llamada3)
