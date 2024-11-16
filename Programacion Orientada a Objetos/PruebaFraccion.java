
public class PruebaFraccion {

	public static void main(String[] args) {
		Fraccion f1 = new Fraccion(3,5);
		Fraccion f2 = new Fraccion(4,10);
		Fraccion resultado = Fraccion.producto(f1, f2);
		resultado.imprimir();
		
		

	}

}
