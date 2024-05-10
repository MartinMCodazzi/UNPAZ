// Martín Nahuel Muñoz Codazzi - 5 may. 2024

package punto7;

import static org.junit.Assert.assertNotNull;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

/**
 * 
 */
class ComisionTest {
	String materia;
	int numero;
	Docente[] docentes;
	Estudiante[] estudiantes;
	int[] calificaciones;	
	Comision comision1;
	
	/**
	 * @throws java.lang.Exception
	 */
	@BeforeEach
	void setUp() throws Exception {							
		docentes = new Docente[2];
		docentes[0] = new Docente("docente1",1234);
		docentes[1] = new Docente("docente2",2345);
		estudiantes = new Estudiante[6];
		estudiantes[0] = new Estudiante("estudiante1",1234);
		estudiantes[1] = new Estudiante("estudiante2",2345);
		estudiantes[2] = new Estudiante("estudiante3",3456);
		estudiantes[3] = new Estudiante("estudiante4",4567);
		estudiantes[4] = new Estudiante("estudiante5",5678);
		estudiantes[5] = new Estudiante("estudiante6",6789);
		calificaciones = new int[6];
		calificaciones[0] = 1;
		calificaciones[1] = 2;
		calificaciones[2] = 3;
		calificaciones[3] = 4;
		calificaciones[4] = 5;
		calificaciones[5] = 6;
		materia = "Programación Orientada a Objetos";
		numero = 1;
		comision1 = new Comision(materia, numero, docentes, estudiantes, calificaciones);
	}

	/**
	 * Test method for {@link punto7.Comision#Comision(java.lang.String, int, punto7.Docente[], punto7.Estudiante[], int[])}.
	 */
	@Test
	void testComision() {		
		assertNotNull(comision1);		
	}

	/**
	 * Test method for {@link punto7.Comision#getMateria()}.
	 */
	@Test
	void testGetMateria() {
		assertEquals(comision1.getMateria(),"Programación Orientada a Objetos");
	}

	/**
	 * Test method for {@link punto7.Comision#setMateria(java.lang.String)}.
	 */
	@Test
	void testSetMateria() {
		comision1.setMateria("Administración 2");
		assertEquals(comision1.getMateria(),"Administración 2");
	}

	/**
	 * Test method for {@link punto7.Comision#getNumero()}.
	 */
	@Test
	void testGetNumero() {
		assertEquals(comision1.getNumero(),1);
	}

	/**
	 * Test method for {@link punto7.Comision#setNumero(int)}.
	 */
	@Test
	void testSetNumero() {
		comision1.setNumero(2);
		assertEquals(comision1.getNumero(),2);		
	}

	/**
	 * Test method for {@link punto7.Comision#getDocentes()}.
	 */
	@Test
	void testGetDocentes() {
		Docente[] docentes2 = comision1.getDocentes();
		Docente docente01 = docentes2[0];
		assertEquals(docente01.getNombre(),"docente1");		
	}

	/**
	 * Test method for {@link punto7.Comision#setDocentes(punto7.Docente[])}.
	 */
	@Test
	void testSetDocentes() {
		docentes = new Docente[1];
		docentes[0] = new Docente("docente01",1234);
		comision1.setDocentes(docentes);
		Docente[] docentes2 = comision1.getDocentes();
		Docente docente01 = docentes2[0];
		assertEquals(docentes2.length,1);
		assertEquals(docente01.getNombre(),"docente01");	
	}

	/**
	 * Test method for {@link punto7.Comision#getInscriptos()}.
	 */
	@Test
	void testGetInscriptos() {
		fail("Not yet implemented");
	}

	/**
	 * Test method for {@link punto7.Comision#setInscriptos(punto7.Estudiante[])}.
	 */
	@Test
	void testSetInscriptos() {
		fail("Not yet implemented");
	}

	/**
	 * Test method for {@link punto7.Comision#getCalificaciones()}.
	 */
	@Test
	void testGetCalificaciones() {
		fail("Not yet implemented");
	}

	/**
	 * Test method for {@link punto7.Comision#setCalificaciones(int[])}.
	 */
	@Test
	void testSetCalificaciones() {
		fail("Not yet implemented");
	}

	/**
	 * Test method for {@link punto7.Comision#toString()}.
	 */
	@Test
	void testToString() {
		fail("Not yet implemented");
	}

}
