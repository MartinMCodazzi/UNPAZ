// Martín Nahuel Muñoz Codazzi - 2 may. 2024

package punto7;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

/**
 * 
 */
class EstudianteTest {
	Estudiante estudiante1;
	
	/**
	 * @throws java.lang.Exception
	 */
	@BeforeEach
	void setUp() throws Exception {
		estudiante1 = new Estudiante("estudiante1", 1234);
	}

	/**
	 * Test method for {@link punto7.Estudiante#getNombre()}.
	 */
	@Test
	void testGetNombre() {		
		assertEquals(estudiante1.getNombre(), "estudiante1");
	}

	/**
	 * Test method for {@link punto7.Estudiante#setNombre(java.lang.String)}.
	 */
	@Test
	void testSetNombre() {		
		estudiante1.setNombre("estudiante_1");
		assertEquals(estudiante1.getNombre(), "estudiante_1");
	}

	/**
	 * Test method for {@link punto7.Estudiante#getLegajo()}.
	 */
	@Test
	void testGetLegajo() {
		assertEquals(estudiante1.getLegajo(), 1234);
	}

	/**
	 * Test method for {@link punto7.Estudiante#setLegajo(int)}.
	 */
	@Test
	void testSetLegajo() {
		estudiante1.setLegajo(12345);
		assertEquals(estudiante1.getLegajo(), 12345);
	}
	/**
	 * Test method for {@link punto7.Estudiante#toString()}.
	 */
	@Test
	void testToString() {		
		assertEquals(estudiante1.toString(), "Estudiante [nombre: estudiante1, legajo: 1234]" );
	}

}
