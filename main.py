def generarSerie(n):
  serie = []
  a, b = 0, 1
  while a <= n:
    serie.append(a)
    a, b = b, a + b
  return serie

def main():
  import os
  estado = True
  while estado:
    os.system('clear')
    print("Programa que genera la serie Fibonacci.")
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    try:
      n = int(input("Ingrese el límite de la serie: "))
      if n > 0:
        serie = generarSerie(n)
        print(f"La serie Fibonacci es:\n{serie}\n")
      else:
        print("Error, se esperaba un valor numérico entero positivo...")
    except ValueError:
      print("Error, se esperaba un valor numérico entero positivo...")
    sal = input("Desea generar otra serie(s/n): ")
    if sal == '' or sal[0].upper() != 'S':
      estado = False
      print("Gracias...")

if __name__ == '__main__':
  main()
  