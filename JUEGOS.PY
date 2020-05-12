import json
import hangman
import reversegam
import tictactoeModificado


def guardarj (nombre, juego, datos):
  if juego == '1':
    datos['ahorcado'].append(nombre)
  elif juego == '2':
    datos['ta-te-ti'].append(nombre)
  else:
    datos['otello'].append(nombre)
  return(datos)
 

def main(args):
  dicc = {'ahorcado': [], 'ta-te-ti': [], 'otello': []}
  sigo_jugando = True
  archivo = open("jueguitosjson.txt", "x")
  while sigo_jugando:
   nombre = input("INGRESA TU NOMBRE")
   print('''
   Elegí con qué juego querés jugar:
   1.- Ahorcado
   2.- Ta-TE-TI
   3.- Otello
   4.- Salir''')

   opcion = input()
   if opcion == '1':
	    hangman.main()
   elif opcion == '2':
	    tictactoeModificado.main()
   elif opcion == '3':
	    reversegam.main()
   elif opcion == '4':
	    sigo_jugando = False
  
   if (opcion != '4'):
      dicc = guardarj(nombre,opcion,dicc)
  json.dump(dicc, archivo) 
  archivo.close()

		
if __name__ == '__main__':
  import sys
  sys.exit(main(sys.argv))
