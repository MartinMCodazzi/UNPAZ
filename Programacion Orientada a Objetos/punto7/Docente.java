// Martín Nahuel Muñoz Codazzi - 2 may. 2024

package punto7;

public class Docente {
	private String nombre;
	private int dni;
	
	Docente(String nombre, int dni){
		this.nombre = nombre;
		this.dni = dni;
	}
	
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public int getDni() {
		return dni;
	}
	public void setDni(int dni) {
		this.dni = dni;
	}

	@Override
	public String toString() {
		return "Docente [nombre: " + nombre + ", dni: " + dni + "]\n";
	}
	
	

}
