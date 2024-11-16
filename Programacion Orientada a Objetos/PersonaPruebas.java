
public class PersonaPruebas {

	public static void main(String[] args) {
		Persona persona2 = new Persona("martín",35);
		Persona persona3 = new Persona("Guadalupe",35);
		Persona persona4 = new Persona("Alicia",20);
		Persona persona5 = new Persona("Osvaldo",15);
		Persona[] grupo = new Persona[] {persona2,persona3,persona4,persona5};
		Persona personaMasJoven = Persona.personaMasJoven(grupo);
		System.out.println(personaMasJoven.getNombre());
		
		Persona personaBuscada = Persona.buscar(grupo,"Alicia");
		System.out.println(personaBuscada.getEdad());
	}

}
