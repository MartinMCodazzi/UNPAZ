// Martín Nahuel Muñoz Codazzi 07/04/2024

public class Fraccion {
	private int numerador;
	private int denominador;

	public Fraccion(int numeradorIngresado, int denominadorIngresado) {
		if (numeradorIngresado != 0) {
			numerador = numeradorIngresado;
		} else {
			throw new IllegalArgumentException("El numerador no puede ser 0");
		}
		if (denominadorIngresado != 0) {
			denominador = denominadorIngresado;
		} else {
			throw new IllegalArgumentException("El denominador no puede ser 0");
		}

	}

	public void imprimir() {
		System.out.println("la fracción es " + numerador + " / " + denominador);
	}

	public void invertirSigno() {
		numerador = numerador * -1;
		imprimir();
	}

	public void invertir() {
		/*
		 * Hubiera preferido que este método devuelva una fracción, en vez de ser void
		 */
		int temporal;
		if (numerador < 0) {
			temporal = numerador * -1;
			numerador = denominador * -1;
		} else {
			temporal = numerador;
			numerador = denominador;
		}
		denominador = temporal;
		imprimir();
	}

	public double aDouble() {
		return (double) numerador / denominador;
	}

	public void reducir() {
		/*
		 * Hubiera preferido que este método devuelva una fracción, en vez de ser void,
		 * podría haber hecho más fácil la impresión
		 */
		int a, b;
		if (numerador < 0) {
			a = numerador * -1;
		} else {
			a = numerador;
		}
		b = denominador;
		while (b != 0) {
			int temp = b;
			b = a % b;
			a = temp;
		}
		numerador = numerador / a;
		denominador = denominador / a;
		imprimir();

	}

	static Fraccion producto(Fraccion q1, Fraccion q2) {

		Fraccion resultado = new Fraccion(q1.numerador * q2.numerador, q1.denominador * q2.denominador);
		int a, b;
		// Raro que me deje acceder a los atributos directamente, si son privados
		// Redundante, pero no quiero hacer más métodos de los pedidos por consigna
		if (resultado.numerador < 0) {
			a = resultado.numerador * -1;
		} else {
			a = resultado.numerador;
		}
		b = resultado.denominador;
		while (b != 0) {
			int temp = b;
			b = a % b;
			a = temp;
		}
		resultado.numerador = resultado.numerador / a;
		resultado.denominador = resultado.denominador / a;

		return resultado;
	}

	static Fraccion suma(Fraccion q1, Fraccion q2) {
		Fraccion resultado = new Fraccion(
				(q1.numerador * q2.denominador) + (q2.numerador * q1.denominador),
				q1.denominador * q2.denominador);
		int a, b;
		// Redundante, pero no quiero hacer más métodos de los pedidos por consigna
		if (resultado.numerador < 0) {
			a = resultado.numerador * (-1);
		} else {
			a = resultado.numerador;
		}
		b = resultado.denominador;
		while (b != 0) {
			int temp = b;
			b = a % b;
			a = temp;
		}
		resultado.numerador = resultado.numerador / a;
		resultado.denominador = resultado.denominador / a;

		return resultado;
		
	}

}
