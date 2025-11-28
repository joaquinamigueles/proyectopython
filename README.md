# Proyecto Final – Aplicación Web en Django  
### Alumna: *Priscila Pereyra Salvador*

---

## 📌 Descripción del Proyecto

Este proyecto es una aplicación web tipo **blog**, desarrollada con **Python + Django**, que permite:

- Gestionar páginas/entradas estilo blog.
- Visualizar información del proyecto de eficiencia energética.
- Registrarse, iniciar sesión y administrar un perfil.
- Crear, editar y eliminar publicaciones (solo usuarios autenticados).
- Enviar y recibir mensajes entre usuarios dentro del sitio.
- Ver información personal en la sección “Acerca de mí”.

El objetivo fue cumplir todos los requisitos solicitados para el **proyecto final del Playground (Coderhouse)**.

---

## 🧩 Funcionalidades Principales

### 🔹 Navegación (Navbar)
- Home  
- About  
- Pages (listado)  
- Crear página (solo usuario logueado)  
- Login  
- Registro  
- Perfil  
- Logout  
- Mensajes (si el usuario está logueado)

---

## 🔹 Home
Pantalla inicial con presentación del proyecto + imagen estática desde `/static/img/`.

---

## 🔹 About
Ruta: `/about/`  
Vista que muestra información personal (Acerca de mí).

---

## 🔹 Pages (Blog)
Ruta principal: `/pages/`

Incluye:
- ✔️ Listado de páginas  
- ✔️ Botón **Leer más** para ver el detalle  
- ✔️ Mensaje “No hay páginas aún” si la lista está vacía  
- ✔️ Crear página  
- ✔️ Editar página  
- ✔️ Eliminar página  
- ✔️ Requiere iniciar sesión para crear/editar/borrar  
- ✔️ Cada página contiene:
  - Título  
  - Subtítulo  
  - Texto enriquecido (CKEditor)  
  - Imagen  
  - Fecha  

---

## 🔹 Sistema de Usuarios (Accounts)
Incluye:
- ✔️ Registro (username, email, password)  
- ✔️ Login  
- ✔️ Logout  
- ✔️ Perfil del usuario  
  - nombre  
  - apellido  
  - email  
  - avatar  
  - biografía / link / otros datos  
- ✔️ Editar perfil  
- ✔️ Cambiar contraseña

---

## 🔹 Sistema de Mensajería (App “mensajes”)
Los usuarios pueden:
- Enviar mensajes privados  
- Ver bandeja de entrada  
- Ver mensajes enviados  
- Abrir el detalle de cada mensaje  

Rutas:
- `/mensajes/`
- `/mensajes/nuevo/`
- `/mensajes/enviados/`
- `/mensajes/<id>/`

---

## 🔹 Panel de Administración (Admin)
Todos los modelos están registrados y administrables desde `/admin/`:

- Mediciones Energéticas  
- Pages  
- Usuarios  
- Mensajes  
- Empleados  

---

## 🗄️ Estructura del Proyecto

proyecto/
│── inicio/
│── pages/
│── usuarios/
│── mensajes/
│── seguimiento/ (settings y urls principales)
│── static/
│ └── img/
│── templates/
│── requirements.txt
│── manage.py
└── .gitignore


---
## 🎥 Video de demostración

Video mostrando el funcionamiento de la app (máx. 10 minutos):

👉 [Ver video de la demo](https://drive.google.com/file/d/1CffFbwNRHzhY0tkBD6GWlsZM0DgiCvM-/view?usp=drive_link)


## ⚙️ Instalación del Proyecto

### 1️.  Clonar repositorio
```bash
git clone <url-del-repo>
cd proyecto
2️. Crear entorno virtual
python -m venv .venv

3️. Activar entorno virtual

Windows:

.venv\Scripts\activate

4️. Instalar dependencias
pip install -r requirements.txt

5️. Aplicar migraciones
python manage.py migrate

6️. Correr el servidor
python manage.py runserver
