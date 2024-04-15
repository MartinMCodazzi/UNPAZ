// Martín Nahuel Muñoz Codazzi - 14 abr. 2024

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

/**
 * 
 */
class AgendaTest {

	Persona persona1 ;
	Persona persona2 ;
	Persona persona3 ;
	Persona persona4 ;
	Persona persona5 ;

	/**
	 * @throws java.lang.Exception
	 */
	@BeforeEach
	void setUp() throws Exception {
		persona1 = new Persona("Guillermo",22);
		persona2 = new Persona("Martín",35);
		persona3 = new Persona("Guadalupe",35);
		persona4 = new Persona("Alicia",20);
		persona5 = new Persona("Osvaldo",15);
	}

	@Test
	@DisplayName("Se debe crear la agenda con el tamaño dado")
	void testConstructor() {
		Agenda agenda = new Agenda(5);
		assertNotNull(agenda);
		assertEquals(agenda.getContactos().length,5);
	}
	
	@Test
	@DisplayName("guardar() toma una persona y un telefono. Guarda el contacto")
	void testGuardar() {
		Agenda agenda = new Agenda(1);
		agenda.guardar(persona1, "123456789");
		assertEquals(agenda.getContactos()[0].getNombre(), "Guillermo");
		assertEquals(agenda.getContactos().length, 1);
		agenda.guardar(persona2, "123456789");
		assertEquals(agenda.getContactos()[1].getNombre(), "Martín");
		assertEquals(agenda.getContactos().length, 2);
	}
	
	@Test
	@DisplayName("eliminar() recibe una Persona, la busca en contactos y si la encuentra, la convierte en null")
	void testEliminar() {
		Agenda agenda = new Agenda(1);
		agenda.guardar(persona1, "123456789");
		agenda.guardar(persona2, "123456789");
		agenda.guardar(persona3, "123456789");
		agenda.guardar(persona4, "123456789");
		assertFalse(agenda.pertenece(persona5));
		assertTrue(agenda.pertenece(persona1));
		agenda.eliminar(persona1);
		assertFalse(agenda.pertenece(persona1));
	}
	
	@Test
	@DisplayName("dameTelefono recibe una Persona,devuelve su número de teléfono")
	void testDameTelefono() {
		Agenda agenda = new Agenda(1);
		agenda.guardar(persona1, "123456789");
		agenda.guardar(persona2, "987654321");
		agenda.guardar(persona3, "000000000");
		agenda.guardar(persona4, "123456789");		
		assertEquals(agenda.dameTelefono(persona1),"123456789");
		assertEquals(agenda.dameTelefono(persona2),"987654321");
		assertEquals(agenda.dameTelefono(persona3),"000000000");
		assertNull(agenda.dameTelefono(persona5));
	}

}
