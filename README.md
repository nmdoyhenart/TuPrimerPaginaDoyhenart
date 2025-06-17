# 🎬 Gestión de Cine

Proyecto web desarrollado con Django como parte del curso de Python de Coderhouse. Permite gestionar películas, directores y géneros, con funcionalidades CRUD, buscador, herencia de plantillas, formularios y administración.

## 📌 Funcionalidades principales

- 🔍 Búsqueda de películas por nombre
- 📋 Listado de películas, géneros y directores
- ➕ Agregado de nuevas películas, géneros y directores
- 🧩 Herencia de plantillas con `base.html`
- 📄 Formularios personalizados para cada modelo
- 📂 Navegación amigable entre páginas
- 🔐 Acceso al panel de administración de Django

## 🛠️ Tecnologías utilizadas

- **Python 3.13**
- **Django 5.x**
- HTML + CSS (con Bootstrap básico)
- Base de datos SQLite3

## 🚀 Cómo correr el proyecto

### 1. Clonar el repositorio:

```bash
git clone https://github.com/nmdoyhenart/TuPrimerPaginaDoyhenart.git
```

### 2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

### 3. Aplicar migraciones:

```bash
python manage.py migrate
```

### 4. Crear un superusuario para acceder al panel de administración:

```bash
python manage.py createsuperuser
```

### 5. Correr el servidor Django:

```bash
python manage.py runserver
```

### 6. Acceder:

- Sitio principal: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🗂 Estructura del proyecto:

```
Core/
├── static/
│   └── favicon.ico
├── templates/Core/
│   ├── agregar_director.html
│   ├── agregar_genero.html
│   ├── agregar_pelicula.html
│   ├── base.html
│   ├── buscar.html
│   ├── buscar_pelicula.html
│   ├── home.html
│   └── inicio.html
├── __init__.py
├── admin.py
├── apps.py
├── forms.py
├── models.py
├── tests.py
├── urls.py
└── views.py
```
📌 Autor
Nicolás Doyhenart - 2025
