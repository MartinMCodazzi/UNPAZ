import static org.junit.Assert.assertEquals;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class PuntoTest {
	Punto punto;

	private final PrintStream standardOut = System.out;
	private final ByteArrayOutputStream outputStreamCaptor = new ByteArrayOutputStream();

	@BeforeEach
	void Punto() {
		punto = new Punto(1.5, 2.5);
		System.setOut(new PrintStream(outputStreamCaptor));
	}

	@AfterEach
	public void tearDown() {
		System.setOut(standardOut);
	}

	@Test
	@DisplayName("El constructor Punto() inicializa las dos coordenadas a 0.")
	void ConstructorInicializaA0() {
		punto = new Punto();
		assertEquals(punto.x, 0, 0);
		assertEquals(punto.y, 0, 0);
	}

	@Test
	@DisplayName("Al llamar a imprimir, se debe mostrar por consola los valores del punto")
	void llamadaAImprimir() {
		punto.imprimir();
		assertEquals("Los valores del punto ingresado son: x = 1.5 ; y = 2.5\n", outputStreamCaptor.toString());
	}

	@Test
	@DisplayName("Al llamar a desplazar(double desp_x, double desp_y) se debe desplazar según los parámetros dados")
	void llamadaADesplazar() {
		punto.desplazar(9.4, 5.2);
		punto.imprimir();
		assertEquals("Los valores del punto ingresado son: x = 10.9 ; y = 7.7\n", outputStreamCaptor.toString());
	}

	@Test
	@DisplayName("Al llamar a distancia(Punto p1, Punto p2) se debe obtener la distancia entre esos dos puntos")
	void llamadaAStaticDistancia() {
		Punto puntoA = new Punto(2, 4);
		Punto puntoB = new Punto(3, 1);
		double distancia = Punto.distancia(puntoA, puntoB);
		assertEquals(distancia, 3.1622776601683795, 0);

		puntoA = new Punto(3, 4);
		puntoB = new Punto(6, 8);
		distancia = Punto.distancia(puntoA, puntoB);
		assertEquals(distancia, 5.0, 0);

		puntoA = new Punto(0, 0);
		puntoB = new Punto(0, 0);
		distancia = Punto.distancia(puntoA, puntoB);
		assertEquals(distancia, 0.0, 0);

		puntoA = new Punto(-3, -4);
		puntoB = new Punto(-6, -8);
		distancia = Punto.distancia(puntoA, puntoB);
		assertEquals(distancia, 5.0, 0);

		puntoA = new Punto(3, 4);
		puntoB = new Punto(-6, -8);
		distancia = Punto.distancia(puntoA, puntoB);
		assertEquals(distancia, 15.0, 0);
	}

}
