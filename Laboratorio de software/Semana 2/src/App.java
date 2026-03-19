//Martín Muñoz Codazzi - 19/03/26

import java.util.Arrays;

public class App {
    public static void main(String[] args) throws Exception {
        
    AbstractVehiculo auto1 = new Auto("Toyota", "Corolla", 1000, 4);
    AbstractVehiculo moto1 = new Moto("Honda", "CB500", 500, 500);
    
    Cliente cliente1 = new Cliente("Juan Perez", "12345678");
    Cliente cliente2 = new Cliente("Maria Gomez", "87654321");

    Repository<AbstractVehiculo> vehiculosRepository = new Repository<>(Arrays.asList(auto1, moto1));
    Repository<Cliente> clientesRepository = new Repository<>(Arrays.asList(cliente1, cliente2));

    Reserva reserva1 = new Reserva(cliente1, auto1, 5);
    System.out.println(reserva1.confirmarReserva());

    Reserva reserva2 = new Reserva(cliente2, moto1, 3);
    System.out.println(reserva2.confirmarReserva());
    
    }
}
