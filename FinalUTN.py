import re
import os

def clear_console():
    os.system('cls')

ventas_diarias = {}

nombres_juegos = [
    "Spiderman 2", "The Last of Us Part II", "Starfield", "God of War"
]


def agregar_ventas_juego():
  while True:
    fecha = input("Ingrese la fecha (DD-MM-YYYY): ")

    if not re.match(r'\d{2}-\d{2}-\d{4}', fecha):
      print("Formato de fecha incorrecto. Debe ser DD-MM-YYYY.")
    else:
      juego = None
      monto = None

      print("\nNombres de juegos disponibles:")
      for i, juego in enumerate(nombres_juegos, 1):
        print(f"{i}. {juego}")

      seleccion = int(input("\nSeleccione el número del juego: "))

      if 1 <= seleccion <= len(nombres_juegos):
        juego = nombres_juegos[seleccion - 1]
        monto = int(input(f"\nIngrese el monto de ventas para '{juego}': "))

      if fecha in ventas_diarias:
        if juego in ventas_diarias[fecha]:
          ventas_diarias[fecha][juego] += monto
        else:
          ventas_diarias[fecha][juego] = monto
      else:
        ventas_diarias[fecha] = {juego: monto}

      print(f"\nVentas del juego '{juego}' el {fecha} registradas con éxito.")

      continuar = input(
          "\n¿Desea continuar ingresando ventas? (S para Sí / cualquier otra tecla para No): "
      ).strip().upper()
      if continuar != "S":
        break


def consultar_resumen_juego():
  while True:
    fecha = input("Ingrese la fecha para consultar el resumen (DD-MM-YYY): ")

    if fecha in ventas_diarias:
      print(f"\nResumen de ventas del {fecha}:")
      for juego, monto in ventas_diarias[fecha].items():
        print(f"'{juego}': {monto: } unidades")
    else:
      print(f"No hay ventas registradas para el {fecha}.")

    continuar = input(
        "\n¿Desea continuar consultando resumen? (S para Sí / cualquier otra tecla para No): "
    ).strip().upper()
    if continuar != "S":
      break


def resumen_final_dia():
  while True:
    fecha = input("Ingrese la fecha para el resumen final (DD-MM-YYYY): ")

    if fecha in ventas_diarias:
      total_ventas = sum(ventas_diarias[fecha].values())
      print(f"Resumen final de ventas del {fecha}:")
      print(f"Total de ventas del día: {total_ventas: }")
      print("Detalles de ventas por juego:")
      for juego, monto in ventas_diarias[fecha].items():
        print(f"'{juego}': {monto: }")
    else:
      print(f"No hay ventas registradas para el {fecha}.")

    continuar = input(
        "\n¿Desea continuar consultando resumen final? (S para Sí / cualquier otra tecla para No): "
    ).strip().upper()
    if continuar != "S":
      break


while True:
  os.system('cls' if os.name == 'nt' else 'clear')  #Limpia la consola
  print("Bienvenido a nuestro sistema de gestión de ventas de juegos.")
  ascii_art = '''
         |||||||||||  |||||||||||  ||||||   ||||||
         |||    ||||  |||            ||||| |||||
         |||||||||||  |||             |||| ||||
         ||| |||      |||||||||||       ||||||
         |||   |||    |||                |||
         |||    |||   |||                |||
         |||      ||| |||||||||||        ||| 
         '''
  print(ascii_art)
  print("1. Agregar ventas diarias de juegos")
  print("2. Consultar resumen diario de ventas de juegos")
  print("3. Ver resumen final del día")
  print("4. Salir")
  opcion = input("Seleccione una opción (1/2/3/4): ")

  if opcion == '1':
    agregar_ventas_juego()
  elif opcion == '2':
    consultar_resumen_juego()
  elif opcion == '3':
    resumen_final_dia()
  elif opcion == '4':
    print("Gracias por usar el sistema. ¡Hasta luego!")
    break
  else:
    print("Opción no válida. Por favor, seleccione una opción válida.")

  input("Presione Enter para continuar...")  


