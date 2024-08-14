import unittest
from unittest.mock import patch, MagicMock
from comandos import create_user, read_users, update_user, delete_user  # Asegúrate de importar las funciones correctamente

class TestDatabaseFunctions(unittest.TestCase):

    @patch('comandos.psycopg2.connect')
    def setUp(self, mock_connect):
        # Simular la conexión a la base de datos
        self.mock_conn = MagicMock()
        mock_connect.return_value = self.mock_conn
        self.conn = mock_connect()

    def test_create_user(self):
        # Simular el cursor y el comportamiento de la función
        mock_cursor = self.mock_conn.cursor.return_value.__enter__.return_value
        mock_cursor.fetchone.return_value = [1]

        create_user(self.conn, "Test User", "test.user@example.com")
        
        # Verificar que se ejecutó la consulta SQL correcta
        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO users (nombre, email) VALUES (%s, %s) RETURNING id;",
            ("Test User", "test.user@example.com")
        )
        self.conn.commit.assert_called_once()

    def test_read_users(self):
        # Simular el cursor y el comportamiento de la función
        mock_cursor = self.mock_conn.cursor.return_value.__enter__.return_value
        mock_cursor.fetchall.return_value = [
            (1, "Test User", "test.user@example.com", "2024-01-01 00:00:00", "2024-01-01 00:00:00")
        ]

        read_users(self.conn)

        # Verificar que se ejecutó la consulta SQL correcta
        mock_cursor.execute.assert_called_once_with(
            "SELECT id, nombre, email, create_at, update_at FROM users;"
        )
    
    def test_update_user(self):
        # Simular el cursor y el comportamiento de la función
        mock_cursor = self.mock_conn.cursor.return_value.__enter__.return_value

        update_user(self.conn, 1, "Updated User", "updated.user@example.com")

        # Verificar que se ejecutó la consulta SQL correcta
        mock_cursor.execute.assert_called_once_with(
            "UPDATE users SET nombre = %s, email = %s, update_at = CURRENT_TIMESTAMP WHERE id = %s;",
            ("Updated User", "updated.user@example.com", 1)
        )
        self.conn.commit.assert_called_once()

    def test_delete_user(self):
        # Simular el cursor y el comportamiento de la función
        mock_cursor = self.mock_conn.cursor.return_value.__enter__.return_value

        delete_user(self.conn, 1)

        # Verificar que se ejecutó la consulta SQL correcta
        mock_cursor.execute.assert_called_once_with(
            "DELETE FROM users WHERE id = %s;", (1,)
        )
        self.conn.commit.assert_called_once()

if __name__ == "__main__":
    unittest.main()