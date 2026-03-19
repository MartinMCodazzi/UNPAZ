//Martín Muñoz Codazzi - 19/03/26

import java.util.List;

// Esta es la clase genérica Repository, que puede ser utilizada para almacenar cualquier tipo de objeto.
public class Repository<T> {
    //Aunque sea final, no es inmutable, ya que el contenido de la lista puede cambiar, pero no se puede reasignar a otra lista. (Sugerencia de Copilot)
    private final List<T> items;

    public Repository(List<T> items) {
        this.items = items;
    }

    public void addItems(T item) {
        this.items.add(item);
    }

    public List<T> getItems() {
        return this.items;
    }

}
