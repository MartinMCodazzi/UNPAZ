// Martín Nahuel Muñoz Codazzi - 2 may. 2024

package punto7;

import java.util.HashMap;
import java.util.LinkedList;

public class UNPAZ {
	private Comision[] comisiones;

	public UNPAZ(Comision[] comisiones) {
		this.comisiones = comisiones;
	}

	public Comision[] getComisiones() {
		return comisiones;
	}

	public void setComisiones(Comision[] comisiones) {
		this.comisiones = comisiones;
	}

	public boolean cursaCon(Estudiante estudianteBuscado, Docente docenteBuscado) {
		for (int i = 0; i < this.comisiones.length; i++) {
			Comision comisionActual = this.comisiones[i];
			for (int indexDocente = 0; indexDocente < comisionActual.getDocentes().length; indexDocente++) {
				if (docenteBuscado.equals(comisionActual.getDocentes()[indexDocente])) {
					// Si encuentro el docente, prosigo a buscar el estudiante dentro de la comisión
					for (int indexEstudiante = 0; indexEstudiante < comisionActual
							.getInscriptos().length; indexEstudiante++) {
						if (estudianteBuscado.equals(comisionActual.getInscriptos()[indexEstudiante])) {
							return true;
						}
					}
				}
			}
		}
		return false;
	}

	public boolean suficientesDocentes() {
		for (int i = 0; i < this.comisiones.length; i++) {
			Comision comisionActual = this.comisiones[i];
			if ((float) comisionActual.getDocentes().length / comisionActual.getInscriptos().length <= 0.05) {
				return false;
			}
		}
		return true;
	}

	public LinkedList<Estudiante> losMejores() {
		LinkedList<Estudiante> resultado = new LinkedList<Estudiante>();
		for (int i = 0; i < this.comisiones.length; i++) {
			Comision comisionActual = this.comisiones[i];
			int notaMasAlta = comisionActual.getCalificaciones()[0];
			for (int indexCalificaciones = 1; indexCalificaciones < comisionActual
					.getCalificaciones().length; indexCalificaciones++) {
				if (comisionActual.getCalificaciones()[indexCalificaciones] >= notaMasAlta) {
					notaMasAlta = comisionActual.getCalificaciones()[indexCalificaciones];
				}
			}
			for (int indexCalificaciones = 0; indexCalificaciones < comisionActual
					.getCalificaciones().length; indexCalificaciones++) {
				if (notaMasAlta == comisionActual.getCalificaciones()[indexCalificaciones]) {
					resultado.add(comisionActual.getInscriptos()[indexCalificaciones]);
				}
			}
		}
		return resultado;
	}

	public LinkedList<Estudiante> alumnosDe(Docente docenteBuscado) {
		LinkedList<Estudiante> resultado = new LinkedList<Estudiante>();
		for (int i = 0; i < this.comisiones.length; i++) {
			Comision comisionActual = this.comisiones[i];
			for (int indexDocente = 0; indexDocente < this.comisiones[i].getDocentes().length; indexDocente++) {
				if (comisionActual.getDocentes()[indexDocente].equals(docenteBuscado)) {
					for (int indexEstudiante = 0; indexEstudiante < comisionActual
							.getInscriptos().length; indexEstudiante++) {
						if (!resultado.contains(comisionActual.getInscriptos()[indexEstudiante])) {
							resultado.add(comisionActual.getInscriptos()[indexEstudiante]);
						}
					}
				}
			}

		}
		return resultado;
	}

	public LinkedList<String> unicaComision() {
		LinkedList<String> resultado = new LinkedList<String>();
		loopExterior: for (int indexComision1 = 0; indexComision1 < this.getComisiones().length; indexComision1++) {
			for (int indexComision2 = 0; indexComision2 < this.getComisiones().length; indexComision2++) {
				if (indexComision1 == indexComision2)
					continue;
				if (this.getComisiones()[indexComision1].getMateria() == this.getComisiones()[indexComision2]
						.getMateria()) {
					continue loopExterior;
				}
			}
			resultado.add(this.getComisiones()[indexComision1].getMateria());
		}
		// System.out.println(resultado);
		return resultado;
	}

	public Estudiante elMasEstudioso() {
		HashMap<Estudiante, Integer> tablaEstudiantesYMateriasAprobadas = new HashMap<>();
		for (int indexComision = 0; indexComision < this.getComisiones().length; indexComision++) {
			for (int indexEstudiante = 0; indexEstudiante < this.getComisiones()[indexComision]
					.getInscriptos().length; indexEstudiante++) {

				// Para facilitar la lectura:
				Estudiante estudianteActual = this.getComisiones()[indexComision].getInscriptos()[indexEstudiante];
				int calificacionActual = this.getComisiones()[indexComision].getCalificaciones()[indexEstudiante];

				if (calificacionActual >= 4) {
					if (tablaEstudiantesYMateriasAprobadas.containsKey(estudianteActual)) {
						tablaEstudiantesYMateriasAprobadas.put(estudianteActual, tablaEstudiantesYMateriasAprobadas.get(estudianteActual) + 1);
					} else {
						tablaEstudiantesYMateriasAprobadas.put(estudianteActual, 1);
					}
				}
			}
		}

		for (Estudiante estudiante : tablaEstudiantesYMateriasAprobadas.keySet()) {
			System.out.println("Estudiante :"+ estudiante.getNombre() + " Tiene " + tablaEstudiantesYMateriasAprobadas.get(estudiante) + " materias aprobadas.");
		}

		Estudiante elMasEstudioso = null;
		int masMateriasAprobadas = 0;
		for (Estudiante estudiante : tablaEstudiantesYMateriasAprobadas.keySet()) {
			if (tablaEstudiantesYMateriasAprobadas.get(estudiante) >= masMateriasAprobadas) {
				elMasEstudioso = estudiante;
				masMateriasAprobadas = tablaEstudiantesYMateriasAprobadas.get(estudiante);
			}
		}
		return elMasEstudioso;
	}

}
