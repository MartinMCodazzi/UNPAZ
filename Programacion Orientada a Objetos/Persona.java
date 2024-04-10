// Martín Nahuel Muñoz Codazzi - 10/04/2024

public class Persona {
	String nombre;
	int edad;

	public Persona(String nombre, int edad) {
		this.edad = edad;
		this.nombre = nombre;
	}
	
	public boolean masJovenQue(Persona persona) {
		return this.edad < persona.edad ? true : false;
	}
	
	public boolean tocayo(Persona persona) {		
		return this.nombre.toUpperCase().equals(persona.nombre.toUpperCase());				
	}
	
	public boolean mismaPersona(Persona persona) {
		if (this.tocayo(persona) && this.edad == persona.edad){
			return true;
		} else return false;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}	

}
