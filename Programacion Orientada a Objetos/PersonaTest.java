// Martín Nahuel Muñoz Codazzi - 10/04/2024	

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class PersonaTest {
	Persona persona1;
	
	@BeforeEach
	void crearPersona() {
		persona1 = new Persona("Martín",35);
	}
	
	@Test
	@DisplayName("Se debe crear la clase Persona")
	void VerificarPersona() {		
		assertNotNull(persona1);
	}	
	
	@Test
	@DisplayName("El método masJovenQue(Persona persona2) debe devolver true si la persona que se le ingresa alguien que es más joven que la persona")
	void testMasJovenQue() {
		Persona persona2 = new Persona("Patricia",40);
		Persona persona3 = new Persona("Horacio",30);
		assertTrue(persona1.masJovenQue(persona2));
		assertFalse(persona1.masJovenQue(persona3));
	}
	
	@Test
	@DisplayName("Prueba de el método tocayo(Persona persona2) que devuelve true si comparten el mismo nombre")
	void testTocayo() {
		Persona persona2 = new Persona("martín",5);
		Persona persona3 = new Persona("Alicia",15);
		assertTrue(persona1.tocayo(persona2));
		assertFalse(persona1.tocayo(persona3));
	}
	
	@Test
	@DisplayName("El Método Misma Persona compara si dos personas tienen el mismo nombre y la misma edad")
	void testMismaPersona() {
		Persona persona2 = new Persona("martín",35);
		Persona persona3 = new Persona("Martín",50);
		Persona persona4 = new Persona("Alicia",15);
		Persona persona5 = new Persona("Osvaldo",35);
		assertTrue(persona1.mismaPersona(persona2));
		assertFalse(persona1.mismaPersona(persona3));
		assertFalse(persona1.mismaPersona(persona4));
		assertFalse(persona1.mismaPersona(persona5));
		
	}
}
