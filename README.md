### Clases
Todas las clases del sistema con sus atributos y métodos correspondientes.

## 1. Clase `Libro`
- **Atributos**:
    - `titulo`: el título del libro.
    - `autor`: el autor o autores del libro.
    - `isbn_libro`: número único para identificar el libro.
    - `editorial`: casa editorial del libro.
    - `año_publicación`: año en que el libro fue publicado.
    - `disponible`: estado de disponibilidad del libro.
- **Métodos**:
    - `__init__`: constructor de la clase.
    - `mostrar_info`: muestra la información del libro.
    - `actualizar_disponibilidad`: cambia el estado de disponibilidad del libro.

## 2. Clase `Usuario`
- **Atributos**:
    - `id_usuario`: identificador único para cada usuario.
    - `nombre`: nombre del usuario.
    - `email`: correo electrónico del usuario.
    - `libros_prestados`: lista de libros que el usuario tiene en préstamo.
- **Métodos**:
    - `__init__`: constructor de la clase.
    - `prestar_libro`: método para prestar un libro a un usuario.
    - `devolver_libro`: método para devolver un libro prestado.

## 3. Clase `Bibliotecario`
- **Atributos**:
    - `id_bibliotecario`: identificador único para cada bibliotecario.
    - `nombre`: nombre del bibliotecario.
- **Métodos**:
    - `__init__`: constructor de la clase.
    - `añadir_libro`: método para añadir un nuevo libro al sistema.
    - `eliminar_libro`: método para eliminar un libro del sistema.
    - `buscar_libro`: método para buscar un libro por título, autor o ISBN.

## 4. Clase `Biblioteca`
- **Atributos**:
    - `libros`: lista de todos los libros en la biblioteca.
    - `usuarios`: lista de todos los usuarios registrados.
    - `bibliotecarios`: lista de todos los bibliotecarios.
- **Métodos**:
    - `__init__`: constructor de la clase.
    - `registrar_usuario`: método para añadir un nuevo usuario al sistema.
    - `eliminar_usuario`: método para eliminar un usuario del sistema.
    - `registrar_bibliotecario`: método para añadir un nuevo bibliotecario al sistema.
    - `eliminar_bibliotecario`: método para eliminar un bibliotecario del sistema.
    - `listar_libros`: muestra todos los libros disponibles y no disponibles.
    - `listar_usuarios`: muestra todos los usuarios registrados.
    - `listar_bibliotecarios`: muestra todos los bibliotecarios registrados.

## 5. Clase `Prestamo`
- **Atributos**:
    - `id_prestamo`: identificador único para cada préstamo.
    - `libro`: libro prestado.
    - `usuario`: usuario que toma el préstamo.
    - `fecha_prestamo`: fecha en que se realiza el préstamo.
    - `fecha_devolucion`: fecha esperada de devolución.
- **Métodos**:
    - `__init__`: constructor de la clase.
    - `finalizar_prestamo`: método para marcar un préstamo como finalizado.
