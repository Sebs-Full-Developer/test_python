-- Verificar si la base de datos 'test' existe; si no, crearla
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT FROM pg_database
        WHERE datname = 'test'
    ) THEN
        PERFORM pg_sleep(0.5);  -- Esperar brevemente para asegurarse de que la base de datos se cree antes de usarla
        PERFORM dblink_exec('dbname=postgres', 'CREATE DATABASE test');
    END IF;
END $$;

-- Cambiar a la base de datos 'test'
\c test

-- Verificar si el usuario 'usermain' existe; si no, crearlo
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT FROM pg_catalog.pg_roles
        WHERE rolname = 'usermain'
    ) THEN
        CREATE USER usermain WITH PASSWORD '12345abcd';
    END IF;
END $$;

-- Asignar todos los privilegios al usuario 'usermain' en la base de datos 'test'
GRANT ALL PRIVILEGES ON DATABASE test TO usermain;

-- Verificar si la tabla 'users' existe; si no, crearla
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT FROM information_schema.tables
        WHERE table_name = 'users'
    ) THEN
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            update_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
        );
    END IF;
END $$;

-- Asignar todos los privilegios al usuario 'usermain' en todas las tablas y secuencias del esquema 'public'
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO usermain;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO usermain;