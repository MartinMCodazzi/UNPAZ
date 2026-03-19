//Martín Muñoz Codazzi - 19/03/26

public class Reserva {
    private Cliente cliente;
    private AbstractVehiculo vehiculo;
    private int dias;

    public Reserva(Cliente cliente, AbstractVehiculo vehiculo, int dias) {
        this.cliente = cliente;
        this.vehiculo = vehiculo;
        this.dias = dias;
    }

    public double calcularCostoTotal() {
        return this.vehiculo.calcularCostoAlquiler(this.dias);
    }

    // Si quisiera agregar ña reserva a un repository, se me ocurre que podría pasar el Repo por parámetro a la hora de construir el el objeto Reserva
    public String confirmarReserva() {
        return "=====GESTIÓN DE RESERVAS=====\nReserva confirmada para " + this.cliente.getNombre() + "\ncon el vehículo " + this.vehiculo.getMarca() + " " + this.vehiculo.getModelo() + "\npor " + this.dias + " días." + "\nCosto total: $" + this.calcularCostoTotal();
    }

    public Cliente getCliente() {
        return this.cliente;
    }

    public AbstractVehiculo getVehiculo() {
        return this.vehiculo;
    }

    public int getDias() {
        return this.dias;
    }
    
    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public void setVehiculo(AbstractVehiculo vehiculo) {
        this.vehiculo = vehiculo;
    }

    public void setDias(int dias) {
        this.dias = dias;
    }

    
}
