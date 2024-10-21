class Postres:
    def __init__(self):
        self.menu = {}

    def imprimir_ingredientes(self, nombre_postre):
        if nombre_postre in self.menu:
            print(f"Ingredientes de {nombre_postre}: {self.menu[nombre_postre]}")
        else:
            print(f"El postre '{nombre_postre}' no existe.")

    def insertar_ingredientes(self, nombre_postre, ingredientes):
        if nombre_postre in self.menu:
            self.menu[nombre_postre].extend(ingredientes)
            print(f"Ingredientes {ingredientes} añadidos a {nombre_postre}: {self.menu[nombre_postre]}")
        else:
            print(f"El postre '{nombre_postre}' no existe.")

    def eliminar_ingredientes(self, nombre_postre, ingrediente):
        if nombre_postre in self.menu:
            if ingrediente in self.menu[nombre_postre]:
                self.menu[nombre_postre].remove(ingrediente)
                print(f"Ingrediente '{ingrediente}' eliminado de {nombre_postre}: {self.menu[nombre_postre]}")
            else:
                print(f"El ingrediente '{ingrediente}' no existe en {nombre_postre}.")
        else:
            print(f"El postre '{nombre_postre}' no existe.")

    def dar_alta_postres(self, nombre_postre, ingredientes):
        if nombre_postre not in self.menu:
            self.menu[nombre_postre] = ingredientes
            print(f"Postre '{nombre_postre}' agregado con ingredientes: {self.menu[nombre_postre]}")
        else:
            print(f"El postre '{nombre_postre}' ya existe.")

    def dar_baja_postres(self, nombre_postre):
        if nombre_postre in self.menu:
            del self.menu[nombre_postre]
            print(f"Postre '{nombre_postre}' eliminado.")
        else:
            print(f"El postre '{nombre_postre}' no existe.")

    def eliminar_repetidos(self):
        for nombre_postre in self.menu:
            ingredientes_unicos = list(set(self.menu[nombre_postre]))
            self.menu[nombre_postre] = ingredientes_unicos
            print(f"Ingredientes únicos en {nombre_postre}: {self.menu[nombre_postre]}")

def main():
    postre = Postres()
    print(
        "\n Elija una acción para poder realizar una tarea en la compañía:"
        "\n 'A' para dar de alta los Postres"
        "\n 'I' para ingresar los ingredientes"
        "\n 'E' para eliminar ingredientes"
        "\n 'D' para dar de baja postres"
        "\n 'M' para mostrar ingredientes de postres"
    )
    while True:
        comando = input("Ingrese un comando de arriba para completar una acción: ").strip().upper()
        if comando[0] == 'A':
            nombre_postre = input("Nombre del postre: ")
            ingredientes = input("Ingredientes (separados por comas): ").split(',')
            postre.dar_alta_postres(nombre_postre, ingredientes)
        elif comando[0] == 'I':
            nombre_postre = input("Nombre del postre: ")
            ingredientes = input("Ingredientes (separados por comas): ").split(',')
            postre.insertar_ingredientes(nombre_postre, ingredientes)
        elif comando[0] == 'E':
            nombre_postre = input("Nombre del postre: ")
            ingrediente = input("Ingrediente a eliminar: ")
            postre.eliminar_ingredientes(nombre_postre, ingrediente)
        elif comando[0] == 'D':
            nombre_postre = input("Nombre del postre a dar de baja: ")
            postre.dar_baja_postres(nombre_postre)
        elif comando[0] == 'M':
            nombre_postre = input("Nombre del postre: ")
            postre.imprimir_ingredientes(nombre_postre)
        else:
            break

    postre.eliminar_repetidos()

if __name__ == "__main__":
    main()
