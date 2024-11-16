// Martín Nahuel Muñoz Codazzi - 2 may. 2024

package punto7;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

/**
 * 
 */
class DocenteTest {

	Docente docente1;
	/**
	 * @throws java.lang.Exception
	 */
	@BeforeEach
	void setUp() throws Exception {
		docente1 = new Docente("docente1",1234);
	}

	/**
	 * Test method for {@link punto7.docente#getNombre()}.
	 */
	@Test
	void testGetNombre() {		
		assertEquals(docente1.getNombre(), "docente1");
	}

	/**
	 * Test method for {@link punto7.docente#setNombre(java.lang.String)}.
	 */
	@Test
	void testSetNombre() {		
		docente1.setNombre("docente_1");
		assertEquals(docente1.getNombre(), "docente_1");
	}

	/**
	 * Test method for {@link punto7.docente#getDni()}.
	 */
	@Test
	void testGetLegajo() {
		assertEquals(docente1.getDni(), 1234);
	}

	/**
	 * Test method for {@link punto7.docente#setDni(int)}.
	 */
	@Test
	void testSetLegajo() {
		docente1.setDni(12345);
		assertEquals(docente1.getDni(), 12345);
	}
	/**
	 * Test method for {@link punto7.docente#toString()}.
	 */
	@Test
	void testToString() {		
		assertEquals(docente1.toString(), "Docente [nombre: docente1, dni: 1234]" );
	}

}
