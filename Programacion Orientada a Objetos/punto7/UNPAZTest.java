// Martín Nahuel Muñoz Codazzi - 2 may. 2024

package punto7;

import static org.junit.jupiter.api.Assertions.*;

import java.util.LinkedList;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

/**
 * 
 */
class UNPAZTest {
	String materia;
	int numero;
	Docente[] docentes;
	Estudiante[] estudiantes;
	int[] calificaciones;	
	Comision comision1;
	Comision comision2;
	Comision comision3;
	Comision comision4;
	UNPAZ unpaz;
	Estudiante estudiante1;
	Estudiante estudiante5;
	Estudiante estudianteBuscado;
	Estudiante estudianteNoBuscado;
	Docente docenteBuscado;
	Docente docenteNoBuscado;
	Docente docente1;

	/**
	 * @throws java.lang.Exception
	 */
	@BeforeEach
	void setUp() throws Exception {
		estudiante1 = new Estudiante("estudiante1",1234);
		estudiante5 = new Estudiante("estudiante5",5678);
		docente1 = new Docente("docente1",1234);
		docentes = new Docente[2];
		docentes[0] = docente1;
		docentes[1] = new Docente("docente2",2345);
		estudiantes = new Estudiante[6];
		estudiantes[0] = estudiante1;
		estudiantes[1] = new Estudiante("estudiante2",2345);
		estudiantes[2] = new Estudiante("estudiante3",3456);
		estudiantes[3] = new Estudiante("estudiante4",4567);
		estudiantes[4] = estudiante5;
		estudiantes[5] = new Estudiante("estudiante15",6789);
		calificaciones = new int[6];
		calificaciones[0] = 10;
		calificaciones[1] = 2;
		calificaciones[2] = 3;
		calificaciones[3] = 4;
		calificaciones[4] = 5;
		calificaciones[5] = 6;
		materia = "Programación Orientada a Objetos";
		numero = 1;
		comision1 = new Comision(materia, numero, docentes, estudiantes, calificaciones);
		numero = 4;
		comision4 = new Comision(materia, numero, docentes, estudiantes, calificaciones);
		
		docentes = new Docente[2];
		docentes[0] = new Docente("docente3",1234);
		docentes[1] = docente1;
		estudiantes = new Estudiante[6];
		estudianteNoBuscado = new Estudiante("estudiante6",6789);
		estudiantes[0] = new Estudiante("estudiante1",1234);
		estudiantes[1] = new Estudiante("estudiante2",2345);
		estudiantes[2] = new Estudiante("estudiante3",3456);
		estudiantes[3] = new Estudiante("estudiante154",4567);
		estudiantes[4] = estudiante5;
		estudiantes[5] = estudianteNoBuscado;
		calificaciones = new int[6];
		calificaciones[0] = 1;
		calificaciones[1] = 2;
		calificaciones[2] = 3;
		calificaciones[3] = 4;
		calificaciones[4] = 5;
		calificaciones[5] = 9;
		materia = "Adminsitración 2";
		numero = 2;
		comision2 = new Comision(materia, numero, docentes, estudiantes, calificaciones);
		
		docentes = new Docente[1];
		docenteBuscado = new Docente("docente3",1234); 
		docentes[0] = docenteBuscado;		
		estudiantes = new Estudiante[2];
		estudianteBuscado = new Estudiante("estudiantebuscado",1234);
		estudiantes[0] = estudianteBuscado;
		estudiantes[1] = new Estudiante("estudiante2",2345);
		
		calificaciones = new int[2];
		calificaciones[0] = 10;
		calificaciones[1] = 9;		
		materia = "Análisis Matemático 2";
		numero = 3;
		comision3 = new Comision(materia, numero, docentes, estudiantes, calificaciones);
		
		
		unpaz = new UNPAZ(new Comision[] { comision1,comision2,comision3,comision4} );
	}
	
	@Test
	void testConstructor() {
		assertNotNull(unpaz);
	}

	/**
	 * Test method for {@link punto7.UNPAZ#getComisiones()}.
	 */
	@Test
	void testGetComisiones() {
		Comision comision01 = unpaz.getComisiones()[0];		
		assertEquals(comision01.getMateria(),"Programación Orientada a Objetos");
	}

	/**
	 * Test method for {@link punto7.UNPAZ#setComisiones(punto7.Comision[])}.
	 */
	@Test
	void testSetComisiones() {
		docentes = new Docente[1];
		docentes[0] = new Docente("docente3",1234);	
		estudiantes = new Estudiante[30];
		for (int i = 0 ; i < 30 ; i++ ) {
			Estudiante estudiante = new Estudiante("estudiante",i);
			estudiantes[i] = estudiante;
		}		
		Comision comision1 = new Comision(materia, numero, docentes, estudiantes, calificaciones);
		Comision[] comisiones1 = new Comision[1];
		comisiones1[0] = comision1;
		unpaz.setComisiones(comisiones1);
		assertEquals(unpaz.getComisiones()[0].getInscriptos().length,30);
	}

	/**
	 * Test method for {@link punto7.UNPAZ#cursaCon(punto7.Estudiante, punto7.Docente)}.
	 */
	@Test
	void testCursaCon() {
		assertTrue(unpaz.cursaCon(estudianteBuscado, docenteBuscado));
		assertFalse(unpaz.cursaCon(estudianteNoBuscado, docenteBuscado));
	}

	/**
	 * Test method for {@link punto7.UNPAZ#suficientesDocentes()}.
	 */
	@Test
	void testSuficientesDocentes() {
		assertTrue(unpaz.suficientesDocentes());
		
		docentes = new Docente[1];
		docentes[0] = new Docente("docente3",1234);	
		estudiantes = new Estudiante[30];
		for (int i = 0 ; i < 30 ; i++ ) {
			Estudiante estudiante = new Estudiante("estudiante",i);
			estudiantes[i] = estudiante;
		}		
		Comision comision1 = new Comision(materia, numero, docentes, estudiantes, calificaciones);
		Comision[] comisiones1 = new Comision[1];
		comisiones1[0] = comision1;
		unpaz.setComisiones(comisiones1);
		assertFalse(unpaz.suficientesDocentes());
	}

	/**
	 * Test method for {@link punto7.UNPAZ#losMejores()}.
	 */
	@Test
	void testLosMejores() {
		LinkedList<Estudiante> losMejores = unpaz.losMejores(); 
		assertEquals(losMejores.get(0).getNombre(), "estudiante1" );
	}

	/**
	 * Test method for {@link punto7.UNPAZ#alumnosDe(punto7.Docente)}.
	 */
	@Test
	void testAlumnosDe() {		
		LinkedList<Estudiante> estudiantesPorProfesor = unpaz.alumnosDe(docente1);
		assertNotNull(estudiantesPorProfesor);
	}

	/**
	 * Test method for {@link punto7.UNPAZ#unicaComision()}.
	 */
	@Test
	void testUnicaComision() {
		LinkedList<String> unicasComisiones = unpaz.unicaComision();
		assertEquals(2, unicasComisiones.size());
	}

	/**
	 * Test method for {@link punto7.UNPAZ#elMasEstudioso()}.
	 */
	@Test
	void testElMasEstudioso() {
		assertEquals(estudiante5,unpaz.elMasEstudioso());
	}

}
