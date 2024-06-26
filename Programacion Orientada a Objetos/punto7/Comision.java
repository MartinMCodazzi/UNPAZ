// Martín Nahuel Muñoz Codazzi - 2 may. 2024

package punto7;

import java.util.Arrays;

public class Comision {
	private String materia;
	private int numero;
	private Docente[] docentes;
	private Estudiante[] inscriptos;
	private int[] calificaciones;
	
	/**
	 * @param materia
	 * @param numero
	 * @param docentes
	 * @param inscriptos
	 * @param calificaciones
	 */
	public Comision(String materia, int numero, Docente[] docentes, Estudiante[] inscriptos, int[] calificaciones) {		
		this.materia = materia;
		this.numero = numero;
		this.docentes = docentes;
		this.inscriptos = inscriptos;
		this.calificaciones = calificaciones;
	}
	
	public String getMateria() {
		return materia;
	}
	public void setMateria(String materia) {
		this.materia = materia;
	}
	public int getNumero() {
		return numero;
	}
	public void setNumero(int numero) {
		this.numero = numero;
	}
	public Docente[] getDocentes() {
		return docentes;
	}	
	public void setDocentes(Docente[] docentes) {
		this.docentes = docentes;
	}
	public Estudiante[] getInscriptos() {
		return inscriptos;
	}
	public void setInscriptos(Estudiante[] inscriptos) {
		this.inscriptos = inscriptos;
	}
	public int[] getCalificaciones() {		
		return calificaciones;
	}
	public void setCalificaciones(int[] calificaciones) {
		this.calificaciones = calificaciones;
	}

	
	@Override
	public String toString() {
		return "Comision [materia=" + materia + ", numero=" + numero + ", docentes=" + Arrays.toString(docentes)
				+ ", inscriptos=" + Arrays.toString(inscriptos) + ", calificaciones=" + Arrays.toString(calificaciones)
				+ "]";
	}
	
	
}
