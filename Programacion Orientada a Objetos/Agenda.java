// Martín Nahuel Muñoz Codazzi - 14 abr. 2024

import java.util.function.BooleanSupplier;

public class Agenda {
	private Persona[] contactos;
	private String[] telefonos;

	public Persona[] getContactos() {
		return this.contactos;
	}

	public String[] getTelefonos() {
		return this.telefonos;
	}

	public Agenda(int tamanio) {
		this.contactos = new Persona[tamanio];
		this.telefonos = new String[tamanio];
	}

	public void guardar(Persona persona, String telefono) {
		boolean contactoAgregado = false;
		// Primero, reviso si alguno de los contactos es null
		for (int i = 0; i < this.contactos.length; i++) {
			if (this.contactos[i] == null) {
				// Acá se entra cuando se intenta leer un dato null
				this.contactos[i] = persona;
				this.telefonos[i] = telefono;
				contactoAgregado = true;
			}
		}
		if (!contactoAgregado) {
			// Acá se entra si no se agregó el contacto
			Agenda nuevaAgenda = new Agenda(this.contactos.length + 1);	
			//Creo un nuevo array con lugar para un contacto más, luego lo recorro y le asigno lo del array anterior
			for (int j = 0; j < this.contactos.length; j++) {
				nuevaAgenda.contactos[j] = this.contactos[j];
				nuevaAgenda.telefonos[j] = this.telefonos[j];
			}
			//Acá agrego al nnuevo array la nueva persona
			nuevaAgenda.contactos[nuevaAgenda.contactos.length - 1] = persona;
			nuevaAgenda.telefonos[nuevaAgenda.telefonos.length - 1] = telefono;
			//Acá reemplazo el array viejo por el nuevo
			this.contactos = nuevaAgenda.contactos;
			this.telefonos = nuevaAgenda.telefonos;
		}
	}
	
	public boolean pertenece(Persona persona) {
		for (int i = 0 ; i < this.contactos.length; i++) {
			if (this.contactos[i] != null && this.contactos[i].mismaPersona(persona)) return true;
		}
		return false;
	}


	public void eliminar(Persona persona) {
		for (int i = 0 ; i < this.contactos.length; i++) {
			if (this.contactos[i].mismaPersona(persona)) {
				this.contactos[i] = null;
				this.telefonos[i] = null;
			}
		}
		
	}

	public String dameTelefono(Persona persona) {
		for (int i = 0 ; i < this.contactos.length; i++) {
			if (this.contactos[i] != null && this.contactos[i].mismaPersona(persona)) {
				return this.telefonos[i];
			}
		}
		
		return null;
	}
	

//	public static void main(String args[]) {
//		Persona persona1 = new Persona("Guillermo", 22);
//		Persona persona2 = new Persona("Martín", 35);
//		Persona persona3 = new Persona("Guadalupe", 35);
//		Persona persona4 = new Persona("Alicia", 20);
//		Persona persona5 = new Persona("Osvaldo", 15);
//		Agenda agenda = new Agenda(1);
//		agenda.guardar(persona1, "12345678");
//		for (int i = 0; i < agenda.getContactos().length; i++) {
//			System.out.println(agenda.getContactos()[i].getNombre());
//		}
//	}

	

}
