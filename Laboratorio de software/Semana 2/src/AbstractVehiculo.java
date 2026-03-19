//Martín Muñoz Codazzi - 19/03/26

// Se puede usar el prefijo "Abstract", pero en Java moderno, no se acostumbra
// Tambien se puede usar el sufijo "Base", pero no es tan común

public abstract class AbstractVehiculo implements Alquilable {
    private String marca;
    private String modelo;
    private double costo_por_dia;

    public AbstractVehiculo(String marca, String modelo, double costo_por_dia) {
        this.marca = marca;
        this.modelo = modelo;
        this.costo_por_dia = costo_por_dia;
    }

    @Override //Override se usa para soberescribir un método de la clase padre o de una interfaz
    public double calcularCostoAlquiler(int dias) {
        return this.costo_por_dia * dias;
    }

    //Setters y getters
    public void setMarca(String marca) {
        this.marca = marca;
    }
    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public void setCosto_por_dia(double costo_por_dia) {
        this.costo_por_dia = costo_por_dia;
    }

    public double getCosto_por_dia() {
        return this.costo_por_dia;
    }

    public String getMarca() {
        return this.marca;
    }

    public String getModelo() {
        return modelo;
    }

    public double getCostoPorDia() {
        return this.costo_por_dia;
    }

}
