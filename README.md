# Proyecto La Caleta Club - Backend (Django)

Este repositorio contiene el código fuente del backend para el proyecto "La Caleta Club". El backend está desarrollado en **Python** con el framework **Django** para gestionar toda la lógica de negocio, la interacción con la base de datos y las API's necesarias para la aplicación principal.

## ✨ Características Principales

* **Gestión de Usuarios:** Registro, autenticación (login/logout) y manejo de perfiles de usuario utilizando el sistema de autenticación de Django.
* **API RESTful:** Endpoints bien definidos y creados con **Django REST Framework** para una comunicación eficiente y estandarizada con el frontend.
* **Panel de Administración:** Panel de administrador autogenerado por Django para una fácil gestión de los datos del club (usuarios, reservas, etc.).
* **ORM de Django:** Mapeo objeto-relacional para interactuar con la base de datos de una manera segura y pitónica.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** [Python](https://www.python.org/)
* **Framework:** [Django](https://www.djangoproject.com/)
* **API:** [Django REST Framework](https://www.django-rest-framework.org/)
* **Base de Datos:** *(Añade aquí la base de datos que usas, ej: PostgreSQL, SQLite)*
* **Gestión de Entorno:** *(Menciona si usas Pipenv, Poetry o venv)*

## 🚀 Instalación y Puesta en Marcha

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local.

### **Prerrequisitos**

* Tener instalado [Python](https://www.python.org/downloads/) (versión 3.8 o superior).
* Tener instalado [pip](https://pip.pypa.io/en/stable/installation/) (el gestor de paquetes de Python).
* Tener una instancia de la base de datos *(ej: PostgreSQL)* corriendo (si no usas SQLite).

### **Pasos**

1.  **Clona el repositorio:**
    ```sh
    git clone [https://github.com/ZpectralCrystals/Proyect_LaCaletaClub_Backend.git](https://github.com/ZpectralCrystals/Proyect_LaCaletaClub_Backend.git)
    ```

2.  **Navega al directorio del proyecto:**
    ```sh
    cd Proyect_LaCaletaClub_Backend
    ```

3.  **Crea y activa un entorno virtual:**
    * **Windows:**
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * **macOS / Linux:**
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

4.  **Instala las dependencias del proyecto:**
    Asegúrate de tener un archivo `requirements.txt` en tu repo.
    ```sh
    pip install -r requirements.txt
    ```

5.  **Configura las variables de entorno:**
    * Crea un archivo `.env` en la raíz del proyecto.
    * Añade las configuraciones necesarias. Puedes usar el archivo `.env.example` (si existe) como guía.
        ```dotenv
        # Archivo .env
        SECRET_KEY='TU_SECRET_KEY_AQUI'
        DEBUG=True
        
        # Configuración de la Base de Datos (Ejemplo con PostgreSQL)
        DB_NAME='lacaletaclub_db'
        DB_USER='TU_USUARIO_DE_BD'
        DB_PASSWORD='TU_CONTRASEÑA_DE_BD'
        DB_HOST='localhost'
        DB_PORT='5432'
        ```

6.  **Aplica las migraciones a la base de datos:**
    Este comando creará las tablas necesarias en tu base de datos según los modelos de Django.
    ```sh
    python manage.py migrate
    ```

7.  **Crea un superusuario:**
    Esto te permitirá acceder al panel de administración de Django. Sigue las instrucciones en la consola.
    ```sh
    python manage.py createsuperuser
    ```

8.  **Ejecuta el servidor de desarrollo:**
    ```sh
    python manage.py runserver
    ```

¡Listo! El servidor se estará ejecutando en `http://127.0.0.1:8000/`. Puedes acceder al panel de administración en `http://127.0.0.1:8000/admin`.

## API Endpoints

El proyecto expone varias rutas API para interactuar con los recursos.

* `GET /api/users/` - Obtiene la lista de usuarios.
* `POST /api/token/` - Obtiene un token de autenticación (JWT o similar).
* `POST /api/reservations/` - Crea una nueva reserva.

*(Añade aquí una descripción de las rutas más importantes de tu API. Revisa tu archivo `urls.py` para ver la lista completa).*

## 🤝 Contribuciones

Las contribuciones son siempre bienvenidas. Si quieres mejorar este proyecto, por favor sigue estos pasos:

1.  Haz un "Fork" del proyecto.
2.  Crea una nueva rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3.  Realiza tus cambios y haz "Commit" (`git commit -m 'Añade nueva funcionalidad'`).
4.  Haz "Push" a tu rama (`git push origin feature/nueva-funcionalidad`).
5.  Abre un "Pull Request" para revisión.
