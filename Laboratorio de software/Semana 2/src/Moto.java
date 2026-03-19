//Martín Muñoz Codazzi - 19/03/26

public class Moto extends AbstractVehiculo {
    private int cilindrada;

    public Moto(String marca, String modelo, double costo_por_dia, int cilindrada) {
        super(marca, modelo, costo_por_dia);
        this.cilindrada = cilindrada;
    }

    public int getCilindrada() {
        return this.cilindrada;
    }

    public void setCilindrada(int cilindrada) {
        this.cilindrada = cilindrada;
    }
}
