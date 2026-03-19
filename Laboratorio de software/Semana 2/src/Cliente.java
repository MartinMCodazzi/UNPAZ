//Martín Muñoz Codazzi - 19/03/26

public class Cliente {
    private String nombre;
    private String DNI;
    
    public Cliente(String nombre, String DNI) {
        this.nombre = nombre;
        this.DNI = DNI;
    }

    public String getNombre() {
        return this.nombre;
    }

    public String getDNI() {
        return this.DNI;
    }
    
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setDNI(String DNI) {
        this.DNI = DNI;
    }
}