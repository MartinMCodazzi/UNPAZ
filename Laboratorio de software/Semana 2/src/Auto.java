//Martín Muñoz Codazzi - 19/03/26

public class Auto extends AbstractVehiculo{
    private int cantidad_puertas;

    public Auto(String marca, String modelo, double costo_por_dia, int cantidad_puertas) {
        super(marca, modelo, costo_por_dia);
        this.cantidad_puertas = cantidad_puertas;
    }

    public int getCantidad_puertas() {
        return this.cantidad_puertas;
    }
    
    public void setCantidad_puertas(int cantidad_puertas) {
        this.cantidad_puertas = cantidad_puertas;
    }
}
