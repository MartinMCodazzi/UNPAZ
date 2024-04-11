// Martín Nahuel Muñoz Codazzi 07/04/2024

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertThrows;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class FraccionTest {

	Fraccion fraccion;

	private final PrintStream standardOut = System.out;
	private final ByteArrayOutputStream outputStreamCaptor = new ByteArrayOutputStream();

	@BeforeEach
	void crearFraccion() {
		fraccion = new Fraccion(1, 2);
		System.setOut(new PrintStream(outputStreamCaptor));
	}

	@AfterEach
	public void tearDown() {
		System.setOut(standardOut);
	}

	@Test
	@DisplayName("Se debe crear el objeto con paráametros correctos")
	void seDebeCrearFraccion() {
		assertNotNull(fraccion);
		Throwable exception = assertThrows(IllegalArgumentException.class, () -> {
			fraccion = new Fraccion(0, 2);
		});
		assertEquals("El numerador no puede ser 0", exception.getMessage());
		Throwable exception2 = assertThrows(IllegalArgumentException.class, () -> {
			fraccion = new Fraccion(1, 0);
		});
		assertEquals("El denominador no puede ser 0", exception2.getMessage());

	}

	@Test
	@DisplayName("Debe imprimir la fracción en algún formato cómodo")
	void seDebeMostrarLaFracción() {
		fraccion.imprimir();
		assertEquals("la fracción es 1 / 2\n", outputStreamCaptor.toString());
	}

	@Test
	@DisplayName("Debe imprimir la fracción con el signo invertido")
	void seDebeInvertirElSigno() {
		fraccion.invertirSigno();
		assertEquals("la fracción es -1 / 2\n", outputStreamCaptor.toString());
	}

	@Test
	@DisplayName("Cuando se invierte un número negativo, se debe obtener una fracción positiva")
	void inviertiEnDosVeces() {
		fraccion = new Fraccion(-1, 2);
		fraccion.invertirSigno();
		assertEquals("la fracción es 1 / 2\n", outputStreamCaptor.toString());
	}

	@Test
	@DisplayName("Debe imprimir la fracción invirtiendo numerador y denominador")
	void seDebeInvertirFraccion() {
		fraccion.invertir();
		assertEquals("la fracción es 2 / 1\n", outputStreamCaptor.toString());
	}

	@Test
	@DisplayName("Debe imprimir la fracción invirtiendo numerador y denominador")
	void seDebeInvertirFraccion2() {
		fraccion = new Fraccion(-2, 1);
		fraccion.invertir();
		assertEquals("la fracción es -1 / 2\n", outputStreamCaptor.toString());
	}

	@Test
	@DisplayName("Se convertir la fracción a double")
	void seDebeConvertirLaFraccion() {
		fraccion = new Fraccion(-8, 4);
		assertEquals(-2.0, fraccion.aDouble(), 0);
		fraccion = new Fraccion(8, 4);
		assertEquals(2.0, fraccion.aDouble(), 0);
		fraccion = new Fraccion(10, 4);
		assertEquals(2.5, fraccion.aDouble(), 0);
	}

	@Test
	@DisplayName("Se debe simplificar la fracción")
	void seDebeReducirLaFraccion() {
		fraccion = new Fraccion(8, 4);
		fraccion.reducir();
		assertEquals("la fracción es 2 / 1\n", outputStreamCaptor.toString());
	}

	@Test
	@DisplayName("Se debe simplificar la fracción 2do caso")
	void seDebeReducirLaFraccion2DoCaso() {
		fraccion = new Fraccion(-10, 5);
		fraccion.reducir();
		assertEquals("la fracción es -2 / 1\n", outputStreamCaptor.toString());
	}

	@Test
	@DisplayName("Se debe multiplicar dos fracciones y simplificar el resultado")
	void seMultiplicaDosFracciones() {
		Fraccion fraccion1 = new Fraccion(8, 4);
		Fraccion fraccion2 = new Fraccion(5, 6);
		Fraccion resultado = Fraccion.producto(fraccion1, fraccion2);
		resultado.imprimir();
		assertEquals("la fracción es 5 / 3\n", outputStreamCaptor.toString());
	}

	@Test
	@DisplayName("Se debe multiplicar dos fracciones y simplificar el resultado CASO2")
	void seMultiplicaDosFraccionesnegativo() {
		Fraccion fraccion1 = new Fraccion(-8, 4);
		Fraccion fraccion2 = new Fraccion(5, 6);
		Fraccion resultado = Fraccion.producto(fraccion1, fraccion2);
		resultado.imprimir();
		assertEquals("la fracción es -5 / 3\n", outputStreamCaptor.toString());
	}

	@Test
	@DisplayName("Se debe sumar dos fracciones y simplificar el resultado")
	void sesumaDosFracciones() {
		Fraccion fraccion1 = new Fraccion(8, 4);
		Fraccion fraccion2 = new Fraccion(5, 6);
		Fraccion resultado = Fraccion.suma(fraccion1, fraccion2);
		resultado.imprimir();
		assertEquals("la fracción es 17 / 6\n", outputStreamCaptor.toString());
	}

	@Test
	@DisplayName("Se debe sumar dos fracciones y simplificar el resultado CASO2")
	void sesumaDosFraccionesNegativo() {
		Fraccion fraccion1 = new Fraccion(-8, 4);
		Fraccion fraccion2 = new Fraccion(5, 6);
		Fraccion resultado = Fraccion.suma(fraccion1, fraccion2);
		resultado.imprimir();
		assertEquals("la fracción es -7 / 6\n", outputStreamCaptor.toString());
	}

	@Test
	@DisplayName("Se debe sumar dos fracciones y simplificar el resultado CASO3")
	void sesumaDosFraccionesNegativo2() {
		Fraccion fraccion1 = new Fraccion(-8, 4);
		Fraccion fraccion2 = new Fraccion(-5, 6);
		Fraccion resultado = Fraccion.suma(fraccion1, fraccion2);
		resultado.imprimir();
		assertEquals("la fracción es -17 / 6\n", outputStreamCaptor.toString());
	}

}
