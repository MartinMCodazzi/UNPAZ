// Martín Nahuel Muñoz Codazzi 10/04/2024

public class Persona {
	private String nombre;
	private int edad;

	public Persona(String nombre, int edad) {
		this.edad = edad;
		this.nombre = nombre;
	}	
	
	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public int getEdad() {
		return edad;
	}

	public void setEdad(int edad) {
		this.edad = edad;
	}

	public boolean masJovenQue(Persona persona) {
		//return this.edad < persona.edad ? true : false;
		if (this.edad < persona.edad){
			return true;
		} else return false;
	}
	
	public boolean tocayo(Persona persona) {
		if (this.nombre == persona.nombre) {
			
		}
		return this.nombre.toUpperCase().equals(persona.nombre.toUpperCase());				
	}
	
	public boolean mismaPersona(Persona persona) {
//		if (this.equals(persona)) {
//			return true;
//		} else return false;		
		if (this.tocayo(persona) && this.edad == persona.edad){
			return true;
		} else return false;
	}
	
	static Persona personaMasJoven(Persona[] grupo) {
		Persona masJoven = grupo[0];		
		for (int i = 1 ; i < grupo.length ; i++) {
			if (masJoven.getEdad() > grupo[i].getEdad()){
				masJoven = grupo[i];
			}
		}
		return masJoven;		
	}
	
	static Persona buscar(Persona[] grupo, String nombreBuscado) {
		for (int i = 0 ; i < grupo.length ; i++) {
			if (grupo[i].getNombre().toUpperCase().equals(nombreBuscado.toUpperCase())) {
				return grupo[i];
			}
		}		
		return null;		
	}


	public static void main(String args[]) {
		Persona persona2 = new Persona("martín",35);
		Persona persona3 = new Persona("Guadalupe",35);
		Persona persona4 = new Persona("Alicia",20);
		Persona persona5 = new Persona("Osvaldo",15);
		Persona[] grupo = new Persona[] {persona2,persona3,persona4,persona5};
		Persona personaBuscada = Persona.buscar(grupo,"Alicia");
		System.out.println(personaBuscada.getEdad());
	}
}