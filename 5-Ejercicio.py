import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="ventas"
    )

def crear_cliente():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    cedula = input("Cédula: ")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO clientes (NombreCliente, ApellidoCliente, TelefonoCliente, CedulaCliente) VALUES (%s, %s, %s, %s)",
        (nombre, apellido, telefono, cedula)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print("Cliente creado exitosamente.")

def leer_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()

def actualizar_cliente():
    id_cliente = input("ID del cliente a actualizar: ")
    nombre = input("Nuevo nombre: ")
    apellido = input("Nuevo apellido: ")
    telefono = input("Nuevo teléfono: ")
    cedula = input("Nueva cédula: ")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE clientes SET NombreCliente=%s, ApellidoCliente=%s, TelefonoCliente=%s, CedulaCliente=%s WHERE id=%s",
        (nombre, apellido, telefono, cedula, id_cliente)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print("Cliente actualizado exitosamente.")

def eliminar_cliente():
    id_cliente = input("ID del cliente a eliminar: ")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id=%s", (id_cliente,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Cliente eliminado exitosamente.")

def menu():
    while True:
        print("\n--- Menú CRUD Clientes ---")
        print("1. Crear cliente")
        print("2. Leer clientes")
        print("3. Actualizar cliente")
        print("4. Eliminar cliente")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_cliente()
        elif opcion == "2":
            leer_clientes()
        elif opcion == "3":
            actualizar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()