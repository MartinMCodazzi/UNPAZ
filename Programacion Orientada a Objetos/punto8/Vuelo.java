// Martín Nahuel Muñoz Codazzi 09/05/2024

package punto8;

public class Vuelo {
	
	private Avion avion;
	private Tripulante[] tripulacion;	
	
	public Vuelo(Avion avion, Tripulante[] tripulacion) {		
		this.avion = avion;
		this.tripulacion = tripulacion;
	}
	
	public Avion getAvion() {
		return avion;
	}
	public void setAvion(Avion avion) {
		this.avion = avion;
	}
	public Tripulante[] getTripulacion() {
		return tripulacion;
	}
	public void setTripulacion(Tripulante[] tripulacion) {
		this.tripulacion = tripulacion;
	}	
}
