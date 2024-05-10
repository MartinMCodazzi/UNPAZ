// Martín Nahuel Muñoz Codazzi 09/05/2024

package punto8;

import java.util.HashMap;
import java.util.LinkedList;

public class Aerolinea {

	private Vuelo[] vuelos;

	public Aerolinea(Vuelo[] vuelos) {
		this.vuelos = vuelos;
	}

	public Vuelo[] getVuelos() {
		return vuelos;
	}

	public void setVuelos(Vuelo[] vuelos) {
		this.vuelos = vuelos;
	}

	public int vuelosEn(Tripulante tripulante, Aviones avion) {
		int resultado = 0;
		for (int i = 0; i < this.vuelos.length; i++) {
			Vuelo vueloActual = this.vuelos[i];
			if (vueloActual.getAvion().getAvion() == avion) {
				for (int indexTripulante = 0; indexTripulante < vueloActual
						.getTripulacion().length; indexTripulante++) {
					if (vueloActual.getTripulacion()[indexTripulante] == tripulante) {
						resultado++;
					}
				}
			}
		}
		return resultado;
	}

	public int antiguedadPromedio(Aviones tipoAvion) {
		int resultado = 0;
		int acumEdad = 0;
		int acumTripulacion = 0;
		for (int i = 0; i < this.vuelos.length; i++) {
			Vuelo vueloActual = this.vuelos[i];
			if (vueloActual.getAvion().getAvion() == tipoAvion) {
				for (int indexTripulante = 0; indexTripulante < vueloActual
						.getTripulacion().length; indexTripulante++) {
					acumEdad += vueloActual.getTripulacion()[indexTripulante].getAntiguedad();
					acumTripulacion++;
				}
			}
		}
		try {
			resultado = acumEdad / acumTripulacion;
		} catch (ArithmeticException e) {
			resultado = 0;
		}
		return resultado;
	}

	public LinkedList<Vuelo> vuelosSobrecargados() {
		LinkedList<Vuelo> vuelosSobrecargados = new LinkedList<>();
		paraCadaVuelo: for (int i = 0; i < this.vuelos.length; i++) {
			Vuelo vueloActual = this.vuelos[i];
			int acumAeromozos = 0;
			for (int indexTripulante = 0; indexTripulante < vueloActual.getTripulacion().length; indexTripulante++) {
				if (vueloActual.getTripulacion()[indexTripulante].getCargo() == Cargos.AEROMOZO) {
					acumAeromozos++;
				}
			}

//			System.out.println("Capacidad del avion: " + vueloActual.getAvion().getCapacidad());
//			System.out.println("Cantidad de aeromozos: " + acumAeromozos);
//			System.out.println(
//					"La divisón es: " + (float) (acumAeromozos * 100) / (float) vueloActual.getAvion().getCapacidad());
//			System.out.println("--------------------------------");

			try {
				if ((float) (acumAeromozos * 100) / (float) vueloActual.getAvion().getCapacidad() >= 10) {
					vuelosSobrecargados.add(vueloActual);
				}
			} catch (ArithmeticException e) {
				continue paraCadaVuelo;
			}
		}
		return vuelosSobrecargados;
	}

	public Aviones masInspeccionado() {
		HashMap<Aviones, Integer> tablaAvionesInspectores = new HashMap<>();
		for (int i = 0; i < this.vuelos.length; i++) {
			Vuelo vueloActual = this.vuelos[i];
			for (int indexTripulante = 0; indexTripulante < vueloActual.getTripulacion().length; indexTripulante++) {
				if (vueloActual.getTripulacion()[indexTripulante].getCargo() == Cargos.INSPECTOR) {
					if (tablaAvionesInspectores.containsKey(vueloActual.getAvion().getAvion())) {
						tablaAvionesInspectores.put(vueloActual.getAvion().getAvion(),
								tablaAvionesInspectores.get(vueloActual.getAvion().getAvion()) + 1);
					} else {
						tablaAvionesInspectores.put(vueloActual.getAvion().getAvion(), 1);
					}
				}
			}
		}
		Aviones masInspeccionado = null;
		int cantidadMasInspeccionado = 0;
		for (Aviones key : tablaAvionesInspectores.keySet()) {
			if (tablaAvionesInspectores.get(key) >= cantidadMasInspeccionado) {
				masInspeccionado = key;
				cantidadMasInspeccionado = tablaAvionesInspectores.get(key);
			}
		}

//		for (Aviones key : tablaAvionesInspectores.keySet()) {
//			System.out.println("Tipo de avion: " + key + ", Veces inspeccionado: " +
//					tablaAvionesInspectores.get(key)); }

		return masInspeccionado;
	}

	public LinkedList<Aviones> avionesPilotadosPor(String nombreTripulante) {
		LinkedList<Aviones> avionesPilotadosPor = new LinkedList<>();
		for (int i = 0; i < this.vuelos.length; i++) {
			Vuelo vueloActual = this.vuelos[i];
			for (int indexTripulante = 0; indexTripulante < vueloActual.getTripulacion().length; indexTripulante++) {
				if (vueloActual.getTripulacion()[indexTripulante].getNombre() == nombreTripulante
						&& vueloActual.getTripulacion()[indexTripulante].getCargo() == Cargos.PILOTO) {
					if (!avionesPilotadosPor.contains(vueloActual.getAvion().getAvion())) {
						avionesPilotadosPor.add(vueloActual.getAvion().getAvion());
					}

				}
			}
		}

//		for (Aviones avion : avionesPilotadosPor) {
//			System.out.println(nombreTripulante + " piloteó el " + avion ); 
//		} 
//		if(avionesPilotadosPor.size() == 0) { 
//			System.out.println(nombreTripulante +" no piloteó ningún avión."); 
//		}

		return avionesPilotadosPor;
	}

	public Tripulante empleadoDelMes() {
		HashMap<Tripulante, Integer> tablaTripulanteViajes = new HashMap<>();
		for (int i = 0; i < this.vuelos.length; i++) {
			Vuelo vueloActual = this.vuelos[i];
			for (int indexTripulante = 0; indexTripulante < vueloActual.getTripulacion().length; indexTripulante++) {
				if (tablaTripulanteViajes.containsKey(vueloActual.getTripulacion()[indexTripulante])) {
					tablaTripulanteViajes.put(vueloActual.getTripulacion()[indexTripulante],
							tablaTripulanteViajes.get(vueloActual.getTripulacion()[indexTripulante]) + 1);
				} else {
					tablaTripulanteViajes.put(vueloActual.getTripulacion()[indexTripulante], 1);
				}
			}
		}
		
//		for (Tripulante tripulante : tablaTripulanteViajes.keySet()){
//			System.out.println(tripulante.getNombre() + " tuvo " + tablaTripulanteViajes.get(tripulante) + " viajes." );
//		}
		
		Tripulante masViajero = null;
		int cantidadMasViajes = 0;
		for (Tripulante tripulante : tablaTripulanteViajes.keySet()) {
			if (tablaTripulanteViajes.get(tripulante) >= cantidadMasViajes) {
				masViajero = tripulante;
				cantidadMasViajes = tablaTripulanteViajes.get(tripulante);
			} 
		}
		return masViajero;
	}
	
}
