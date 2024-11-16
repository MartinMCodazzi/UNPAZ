// Martín Nahuel Muñoz Codazzi 09/05/2024

package punto8;

public class Avion {
	private Aviones avion;
	private int capacidad ;	
		
	public Avion(Aviones avion, int capacidad) {		
		this.avion = avion;
		this.capacidad = capacidad;
	}
	public Aviones getAvion() {
		return avion;
	}
	public void setAvion(Aviones avion) {
		this.avion = avion;
	}
	public int getCapacidad() {
		return capacidad;
	}
	public void setCapacidad(int capacidad) {
		this.capacidad = capacidad;
	}
	
	
	
}
