
public class PruebaPersona {

	public static void main(String[] args) {
		Persona persona1 = new Persona("Agustin",25); 
		//Persona persona2 = new Persona("Clara",3);
		//Persona persona2 = new Persona("AgustIN",3);
		Persona persona2 = new Persona("AgustIN",25);
		
		//System.out.println(persona1.masJovenQue(persona2));		
		//System.out.println(persona1.tocayo(persona2));
		System.out.println(persona1.mismaPersona(persona2));
	}

}
