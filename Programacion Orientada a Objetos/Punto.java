// Martín Nahuel Muñoz Codazzi 09/04/2024

public class Punto {
	double x;
	double y;

	public Punto() {
		x = 0;
		y = 0;
	}

	public Punto(double inputX, double inputY) {
		x = inputX;
		y = inputY;
	}

	public void imprimir() {
		System.out.println("Los valores del punto ingresado son: x = " + x + " ; y = " + y);
	}

	public void desplazar(double desp_x, double desp_y) {
		x = x + desp_x;
		y = y + desp_y;
	}

	static double distancia(Punto puntoA, Punto puntoB) {
		double resultado = Math.sqrt(Math.pow(puntoB.x - puntoA.x, 2) + Math.pow(puntoB.y - puntoA.y, 2));
		return resultado;
	}
}
