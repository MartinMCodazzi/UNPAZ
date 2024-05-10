// Martín Nahuel Muñoz Codazzi - 2 may. 2024

package punto7;

public class Estudiante {
	private String nombre;
	private int legajo;
	
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public int getLegajo() {
		return legajo;
	}
	public void setLegajo(int legajo) {
		this.legajo = legajo;
	}
	
	Estudiante(String nombre, int legajo){
		this.nombre = nombre;
		this.legajo = legajo;
	}
	
	@Override
	public String toString() {
		return "Estudiante [nombre: " + nombre + ", legajo: " + legajo + "]\n";
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj) {
			return true;
		}
		if (obj == null || getClass() != obj.getClass()) {
            return false;
        }
		Estudiante otro = (Estudiante) obj;
		if (otro.nombre == this.nombre && this.legajo == otro.legajo) {
			return true;
		}
		return super.equals(obj);
	}
	
		
}	
