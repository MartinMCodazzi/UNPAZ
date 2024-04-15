// Martín Nahuel Muñoz Codazzi - 14 abr. 2024

import static org.junit.jupiter.api.Assertions.*;

import org.junit.Assert;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class ArreglosTest {
	int[] array1;
	int[] array2;
	int[] array3;
	int[] array4;
	int[] array5;
	int[] array6;
	int[] array7;

	@BeforeEach
	void setUp() {
		array1 = new int[] { 1, 2, 3 };
		array2 = new int[] { 4, 5, 6 };
		array3 = new int[] { 7, 8, 9 };
		array4 = new int[] { 1, 1, 1 };
		array5 = new int[] {};
		array6 = new int[] { 4, 1, 5, 9, 15, 0, 54, 100, 4 };
		array7 = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
	}

	@Test
	@DisplayName("esSinRepetidos toma un array, devuelve true si el array no tiene elemenros repetidos")
	void testEsSinRepetidos() {
		assertTrue(Arreglos.esSinRepetidos(array1));
		assertTrue(Arreglos.esSinRepetidos(array5));
		assertFalse(Arreglos.esSinRepetidos(array4));
		assertFalse(Arreglos.esSinRepetidos(array6));
	}

	@Test
	@DisplayName("pegar() toma dos arrays, devuelve nuevo array con ambos elementos concatenados")
	void testPegar() {
		Assert.assertArrayEquals(Arreglos.pegar(array1, array2), new int[] { 1, 2, 3, 4, 5, 6 });
		Assert.assertArrayEquals(Arreglos.pegar(array2, array1), new int[] { 4, 5, 6, 1, 2, 3 });
		Assert.assertArrayEquals(Arreglos.pegar(array1, array3), new int[] { 1, 2, 3, 7, 8, 9 });
		Assert.assertArrayEquals(Arreglos.pegar(array4, array1), new int[] { 1, 1, 1, 1, 2, 3 });
	}

	@Test
	@DisplayName("agregarAlFinal() toma un array y un entero, devuelve nuevo array ambos elementos concatenados")
	void testAgregarAlFinal() {
		Assert.assertArrayEquals(Arreglos.agregarAlFinal(array1, 4), new int[] { 1, 2, 3, 4 });
		Assert.assertArrayEquals(Arreglos.agregarAlFinal(array2, 7), new int[] { 4, 5, 6, 7 });
		Assert.assertArrayEquals(Arreglos.agregarAlFinal(array3, 10), new int[] { 7, 8, 9, 10 });
		Assert.assertArrayEquals(Arreglos.agregarAlFinal(array4, -1), new int[] { 1, 1, 1, -1 });
		Assert.assertArrayEquals(Arreglos.agregarAlFinal(array5, 0), new int[] { 0 });
	}

	@Test
	@DisplayName("sinRepetidos() toma un array y lo devuelve sin repetidos")
	void testSinRepetidos() {
		Assert.assertArrayEquals(Arreglos.sinRepetidos(Arreglos.pegar(array1, array1)), new int[] { 1, 2, 3 });
		Assert.assertArrayEquals(Arreglos.sinRepetidos(Arreglos.pegar(array2, array2)), new int[] { 4, 5, 6 });
		Assert.assertArrayEquals(Arreglos.sinRepetidos(array4), new int[] { 1 });
		Assert.assertArrayEquals(Arreglos.sinRepetidos(array5), new int[] {});
	}
	
	@Test
	@DisplayName("invertir() recibe un array e invierte los elementos")
	void testInvertir() {
		Assert.assertArrayEquals(new int[] { 3, 2, 1 }, Arreglos.invertir(array1));
		Assert.assertArrayEquals(Arreglos.invertir(array2), new int[] { 6, 5, 4 });
		Assert.assertArrayEquals(Arreglos.invertir(array3), new int[] { 9, 8, 7 });
	}

}
