// Martín Nahuel Muñoz Codazzi 07/04/2024

public class Fraccion {
	private int numerador;
	private int denominador;

	public Fraccion(int numeradorIngresado, int denominadorIngresado) {
		if (numeradorIngresado != 0) {
			this.numerador = numeradorIngresado;
		} else {
			throw new IllegalArgumentException("El numerador no puede ser 0");
		}
		if (denominadorIngresado != 0) {
			this.denominador = denominadorIngresado;
		} else {
			throw new IllegalArgumentException("El denominador no puede ser 0");
		}
	}

	public void imprimir() {
		System.out.println("la fracción es " + this.numerador + " / " + this.denominador);
	}

	public void invertirSigno() {
		this.numerador = this.numerador * -1;		
	}

	public void invertir() {		
		int temporal;
		if (this.numerador < 0) {
			temporal = this.numerador * -1;
			this.numerador = this.denominador * -1;
		} else {
			temporal = numerador;
			this.numerador = this.denominador;
		}
		denominador = temporal;		
	}

	public double aDouble() {
		return (double) numerador / denominador;
	}

	public void reducir() {		
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
	}

	static Fraccion producto(Fraccion fraccion1, Fraccion fraccion2) {		
		Fraccion resultado = new Fraccion(fraccion1.numerador * fraccion2.numerador,
										fraccion1.denominador * fraccion2.denominador);				
		resultado.reducir();
		return resultado;
	}

	static Fraccion suma(Fraccion q1, Fraccion q2) {
		Fraccion resultado = new Fraccion(
				(q1.numerador * q2.denominador) + (q2.numerador * q1.denominador),
				q1.denominador * q2.denominador);		
		resultado.reducir();
		return resultado;		
	}
	
	
}
