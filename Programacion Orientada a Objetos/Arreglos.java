//Martin Nahuel Muñoz Codazzi - 14/04/2024

import java.util.ArrayList;
import java.util.List;

// el acceso final es para que NO se pueda heredar de esta clase
final class Arreglos {
	// Constructor privado porque no me interesa que se pueda instanciar Arreglos
	private Arreglos() {
	}

	static boolean esSinRepetidos(int[] array) {
		for (int i = 0; i < array.length; i++) {
			for (int j = i + 1; j < array.length; j++) {
				if (array[i] == array[j])
					return false;
			}
		}
		return true;
	}

	static int[] pegar(int[] array1, int[] array2) {
		int nuevoArray[] = new int[array1.length + array2.length];
		for (int indiceDelNuevoArray = 0; indiceDelNuevoArray < nuevoArray.length;) {

			for (int indiceDelPrimerArray = 0; indiceDelPrimerArray < array1.length; 
					indiceDelPrimerArray++) {
				
				nuevoArray[indiceDelNuevoArray] = array1[indiceDelPrimerArray];
				indiceDelNuevoArray++;
			}
			for (int indiceDelSegundoArray = 0; indiceDelSegundoArray < array2.length; indiceDelSegundoArray++) {
				nuevoArray[indiceDelNuevoArray] = array2[indiceDelSegundoArray];
				indiceDelNuevoArray++;
			}
		}
		return nuevoArray;
	}

	static int[] agregarAlFinal(int[] array1, int numero) {
		return Arreglos.pegar(array1, new int[] { numero });
	}

	static int[] sinRepetidos(int[] array) {
		// Si se ingresa un array vacío, se devuelve el array, no vale la pena seguir
		if (array.length == 0)
			return array;

		// Con una lista, evito el problema de los arrays y el largo dinámico
		List<Integer> sinRepetir = new ArrayList<Integer>();
		// Esto es una "magia" de las listas
		for (int i = 0; i < array.length; i++) {
			// Básicamente, le pregunto a la lista si tiene el elementoque está en array[i]
			if (!sinRepetir.contains(array[i])) {
				// Si no lo tiene, lo guardo
				sinRepetir.add(array[i]);
			}
		}
		// Creo el arreglo con las dimensiones de la lista
		int[] arregloResultado = new int[sinRepetir.size()];
		for (int i = 0; i < arregloResultado.length; i++) {
			arregloResultado[i] = sinRepetir.get(i);
		}
		return arregloResultado;
	}

	static int[] invertir(int[] array) {
		int[] arrayResultado = new int[array.length];
		for (int i = array.length - 1; i >= 0; i--) {
			// 3-1-2 ; 3-1-1 ; 3-1-0
			arrayResultado[array.length - 1 - i] = array[i];
		}
		return arrayResultado;
	}

//	public static void main(String args[]) {
//		int[] array1 = new int[] { 10, 24, -3, 4, 5, 6, 7, 8, 9, 10,35,0 };
//		int[] array2 = new int[] { 4, 5, 6 };
//		array2 = Arreglos.invertir(array2);
//		System.out.println(Arreglos.invertir(array2));
//
//		int[] nuevoArray = Arreglos.pegar(array1, array2);
//
//		System.out.println(nuevoArray.length);
//
//		nuevoArray = Arreglos.sinRepetidos(nuevoArray);
//
//		System.out.println("El largo del array es :" + nuevoArray.length);
//
//		for (int i = 0; i < array2.length; i++) {
//			System.out.println(array2[i]);
//		}
//	}

}
