// Martín Nahuel Muñoz Codazzi 09/05/2024

package punto8;

public class Tripulante {
	private String nombre;
	private Cargos cargo;
	private int antiguedad;	
	
	public Tripulante(String nombre, Cargos cargo, int antiguedad) {
		this.nombre = nombre;
		this.cargo = cargo;
		this.antiguedad = antiguedad;
	}
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public Cargos getCargo() {
		return cargo;
	}
	public void setCargo(Cargos cargo) {
		this.cargo = cargo;
	}
	public int getAntiguedad() {
		return antiguedad;
	}
	public void setAntiguedad(int antiguedad) {
		this.antiguedad = antiguedad;
	}
	
	
	
}
