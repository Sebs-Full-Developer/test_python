[---------------------- Guía de Instalación y Ejecución del Proyecto ----------------------]

Este documento proporciona instrucciones detalladas para configurar y ejecutar el proyecto. Sigue estos pasos para instalar las herramientas necesarias y ejecutar el proyecto correctamente.

1. Instalación de Python
	Paso 1: Descargar e Instalar Python
		1. Visita la página oficial de Python (Versión 3.x para arriba): https://www.python.org/downloads/
		2. Descarga el instalador de la última versión de Python para Windows.
		3. Ejecuta el instalador y asegúrate de seleccionar la opción "Add Python to PATH" antes de hacer clic en "Install Now".
		4. Completa la instalación siguiendo las instrucciones en pantalla.

	Paso 2: Verificar la Instalación
		1. Abre la terminal de Windows (Símbolo del sistema o PowerShell).
		2. Ejecuta el siguiente comando para verificar que Python esté instalado correctamente:
			python --version
		Deberías ver la versión de Python que instalaste.

2. Instalación de PostgreSQL
	Paso 1: Descargar e Instalar PostgreSQL
		1. Visita la página oficial de PostgreSQL (Versión 16): https://www.postgresql.org/download/windows/
		2. Descarga el instalador para Windows y sigue las instrucciones en pantalla para completar la instalación.

	Paso 2: Verificar la Instalación
		1. Abre el "SQL Shell (psql)" que se instala con PostgreSQL.
		2. Conéctate al servidor PostgreSQL usando las credenciales predeterminadas.
		3. Ejecuta el siguiente comando para verificar que PostgreSQL esté funcionando:
			SELECT version();

[---------------------- Video Guía ----------------------]

Para una guía visual sobre la instalación de PostgreSQL, puedes ver el siguiente video: https://www.youtube.com/watch?v=w9ax9-s2jbE



~
~
~
~
~



[---------------------- Ejecucion del Proyecto ----------------------]

3. Preparar el Proyecto
	Paso 1: Ejecutar el Archivo .bat
		1. Abre el Explorador de archivos y navega al directorio que contiene 'setup_and_run.bat'.
		2. Haz doble clic en 'setup_and_run.bat' para ejecutarlo. Esto creará el archivo .env, el entorno virtual, instalará las librerías, ejecutará el script SQL y el script de comandos en el orden correcto.

4. Probar el Proyecto
Para probar el proyecto y asegurarte de que todo funciona correctamente, ejecuta el archivo de pruebas unitarias.

	Paso 1: Ejecutar el Archivo de Pruebas Unitarias
		1. Abre la terminal de Windows (Símbolo del sistema o PowerShell).
		2. Navega al directorio del proyecto si no estás ya en él.
		3. Ejecuta el siguiente comando para correr las pruebas unitarias:
			python test_database.py
		4. Listo
Video Guía
Para una guía visual sobre cómo ejecutar scripts de Python, puedes ver el siguiente video: https://www.youtube.com/watch?v=9ge7IwuZabc

