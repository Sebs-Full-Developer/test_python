import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Datos de conexión cargados desde .env
db_config = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT')
}

def connect():
    """Establece una conexión con la base de datos."""
    try:
        conn = psycopg2.connect(**db_config)
        print("Conexión exitosa a la base de datos")
        return conn
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

def create_user(conn, nombre, email):
    """Crea un nuevo usuario en la tabla users."""
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users (nombre, email) VALUES (%s, %s) RETURNING id;",
                (nombre, email)
            )
            user_id = cur.fetchone()[0]
            conn.commit()
            print(f"Usuario creado con ID: {user_id}")
    except Exception as e:
        print(f"Error al crear el usuario: {e}")
        conn.rollback()

def read_users(conn):
    """Lee todos los usuarios de la tabla users."""
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, nombre, email, create_at, update_at FROM users;")
            users = cur.fetchall()
            for user in users:
                print(user)
    except Exception as e:
        print(f"Error al leer los usuarios: {e}")

def update_user(conn, user_id, nombre, email):
    """Actualiza un usuario en la tabla users."""
    try:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE users SET nombre = %s, email = %s, update_at = CURRENT_TIMESTAMP WHERE id = %s;",
                (nombre, email, user_id)
            )
            conn.commit()
            print(f"Usuario con ID {user_id} actualizado")
    except Exception as e:
        print(f"Error al actualizar el usuario: {e}")
        conn.rollback()

def delete_user(conn, user_id):
    """Elimina un usuario de la tabla users."""
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id = %s;", (user_id,))
            conn.commit()
            print(f"Usuario con ID {user_id} eliminado")
    except Exception as e:
        print(f"Error al eliminar el usuario: {e}")
        conn.rollback()

if __name__ == "__main__":
    # Conectar a la base de datos
    conn = connect()

    if conn:
        # Operaciones CRUD

        # Crear un nuevo usuario
        create_user(conn, "Juan Pérez", "juan.perez@example.com")

        # Leer todos los usuarios
        print("Usuarios en la tabla:")
        read_users(conn)

        # Actualizar un usuario (ej. ID 1)
        update_user(conn, 1, "Juan Updated", "juan.updated@example.com")

        # Leer todos los usuarios después de la actualización
        print("Usuarios después de la actualización:")
        read_users(conn)

        # Eliminar un usuario (ej. ID 1)
        delete_user(conn, 1)

        # Leer todos los usuarios después de la eliminación
        print("Usuarios después de la eliminación:")
        read_users(conn)

        # Cerrar la conexión
        conn.close()