# 🇬🇧 JyS — English Language Office

**JyS English Language Office** es una página web institucional desarrollada para una academia de inglés ubicada en **Resistencia, Chaco, Argentina**.

El proyecto busca brindar a la academia una presencia digital profesional, presentar de forma clara su propuesta educativa y facilitar el contacto con alumnos y familias interesadas.

> 🎓 **Tipo de proyecto:** Sitio web institucional / Proyecto de portfolio
> 🚧 **Estado:** Completado — con posibles extensiones futuras

---

## 📖 Sobre el proyecto

**JyS English Language Office** es una academia de inglés fundada en **2013**, orientada a la enseñanza del idioma para niños y estudiantes de diferentes niveles.

La institución ofrece distintas modalidades de aprendizaje, incluyendo clases **presenciales y online**, además de preparación para exámenes internacionales.

El sitio web fue desarrollado para centralizar esta información y ofrecer una experiencia moderna, clara y accesible para quienes buscan conocer la academia.

El proyecto se centra principalmente en tres objetivos:

* 🌐 Presentar la academia y su propuesta educativa.
* 📚 Comunicar los cursos y modalidades disponibles.
* 📩 Facilitar el contacto con la institución.

También se destacan los programas de preparación para exámenes internacionales y la condición de la academia como centro asociado a organismos internacionales de evaluación del idioma inglés.

---

## 🎯 Objetivos

Los principales objetivos del proyecto fueron:

* 🌐 Crear una página web institucional profesional.
* 🏫 Presentar la historia e identidad de la academia.
* 📚 Mostrar los cursos y propuestas educativas.
* 🇬🇧 Presentar información sobre exámenes internacionales.
* 📱 Crear una experiencia adaptable a diferentes dispositivos.
* 📩 Facilitar el contacto entre la academia y potenciales alumnos.
* 🎨 Desarrollar una identidad visual acorde a la institución.
* 🧭 Facilitar una navegación sencilla e intuitiva.
* 🚀 Desplegar la aplicación en un entorno de producción.

---

# ✨ Funcionalidades

## 🏠 Página de inicio

La página principal funciona como punto de entrada al sitio.

Cuenta con una sección principal o **hero** que utiliza un video de fondo para generar una presentación visual más dinámica de la academia.

Sobre este contenido se encuentra la barra de navegación, permitiendo acceder rápidamente a las diferentes secciones.

La navegación principal incluye:

* Inicio
* Nosotros
* Cursos
* Exámenes Internacionales
* Contacto

---

## 🏫 Nosotros

La sección **Nosotros** presenta información institucional sobre la academia.

Permite conocer aspectos como:

* Historia de la institución.
* Año de fundación.
* Propuesta educativa.
* Identidad de la academia.
* Orientación de sus cursos.
* Modalidades de enseñanza.

El objetivo es que los visitantes puedan conocer la institución antes de consultar por un curso.

---

## 📚 Cursos

La sección **Cursos** presenta la propuesta educativa de la academia.

Se muestran diferentes opciones de aprendizaje y aspectos relevantes como:

* Edad de los estudiantes.
* Modalidad de cursado.
* Clases presenciales.
* Clases online.
* Grupos reducidos.

La información está organizada para que potenciales alumnos o familiares puedan identificar rápidamente qué propuesta puede resultar adecuada para ellos.

---

## 👧 Enseñanza para niños

Uno de los aspectos destacados de la academia es la enseñanza del idioma inglés desde edades tempranas.

La propuesta contempla alumnos desde aproximadamente **5 años**, buscando presentar el aprendizaje del idioma de una manera accesible y adecuada para los más pequeños.

El sitio utiliza recursos visuales y una estética amigable para comunicar esta propuesta a las familias.

---

## 💻 Modalidades de cursado

La academia ofrece diferentes alternativas de cursado.

Entre ellas se encuentran:

* 🏫 Clases presenciales.
* 💻 Clases online.
* 👥 Grupos reducidos.

Esto permite presentar una propuesta educativa flexible y adaptada a diferentes necesidades.

---

## 🏅 Exámenes internacionales

Una sección específica del sitio está destinada a los **exámenes internacionales**.

La academia se encuentra asociada a programas internacionales de evaluación del idioma inglés.

### Cambridge

La institución figura como:

**Cambridge Preparation Centre**

```text
Centre ID: RPC006027
```

### Trinity College London

También funciona como:

**Trinity College London Examination Centre**

```text
Centre N.º 69012
```

La sección permite presentar esta información de manera clara y explicar a los visitantes las posibilidades de preparación y certificación internacional.

---

## 📩 Formulario de contacto

El sitio incorpora un formulario para que los visitantes puedan comunicarse directamente con la academia.

El usuario puede completar sus datos y enviar una consulta desde la propia página.

El formulario se comunica con el servicio encargado del envío de correos electrónicos, evitando que el visitante tenga que abandonar el sitio para realizar una consulta.

El flujo general es:

```text
Usuario
   │
   ▼
Completa formulario
   │
   ▼
Frontend
   │
   ▼
Backend / API
   │
   ▼
Servicio de email
   │
   ▼
Academia
```

---

# 🏗️ Arquitectura

El proyecto utiliza una arquitectura **monolítica basada en Django**, utilizando el patrón **MVT (Model - View - Template)**.

```text
                    USUARIO
                       │
                       ▼
              ┌─────────────────┐
              │     Navegador    │
              │   HTML / CSS /   │
              │   JavaScript     │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │      URLs       │
              │     Django      │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │      Views      │
              │     Django      │
              └───────┬─────────┘
                      │
             ┌────────┴─────────┐
             │                  │
             ▼                  ▼
      ┌──────────────┐   ┌───────────────┐
      │    Models    │   │   Templates   │
      │  Django ORM  │   │ HTML / Django │
      └──────┬───────┘   └───────────────┘
             │
             ▼
      ┌──────────────┐
      │   SQLite     │
      │  Base datos  │
      └──────────────┘
```

### Flujo de una solicitud

Cuando un usuario accede a una página:

1. El navegador realiza una solicitud HTTP.
2. Django recibe la solicitud.
3. El sistema de URLs determina qué vista debe procesarla.
4. La **View** ejecuta la lógica correspondiente.
5. Si es necesario, se consulta la base de datos mediante el ORM.
6. La información se envía al template correspondiente.
7. Django genera el HTML.
8. El navegador muestra el resultado al usuario.

---

# 🛠️ Tecnologías utilizadas

| Tecnología       | Utilización                         |
| ---------------- | ----------------------------------- |
| **Python**       | Lenguaje principal                  |
| **Django 5.1.1** | Framework backend                   |
| **HTML5**        | Estructura de las páginas           |
| **CSS3**         | Diseño y estilos                    |
| **JavaScript**   | Interacciones del lado del cliente  |
| **Bootstrap 5**  | Diseño responsive y componentes     |
| **SQLite**       | Base de datos durante el desarrollo |
| **Git**          | Control de versiones                |
| **GitHub**       | Repositorio y colaboración          |
| **Render**       | Despliegue de la aplicación         |

---

# 🎨 Diseño e identidad visual

El diseño fue desarrollado específicamente para una academia de idiomas.

La interfaz utiliza:

* 🟡 Amarillo como color de acento.
* 🔴 Rojo como color complementario.
* 🎥 Video en la sección principal.
* 🧭 Barra de navegación transparente.
* ➡️ Elementos gráficos decorativos.
* 📱 Diseño adaptable.
* 📚 Recursos visuales relacionados con la educación.

El objetivo fue crear una identidad que combinara una apariencia **moderna, educativa y amigable**, evitando una interfaz excesivamente formal.

---

# 📱 Diseño responsive

El sitio fue desarrollado pensando en diferentes tamaños de pantalla.

Se utilizan **Bootstrap 5** y CSS personalizado para adaptar los componentes.

La interfaz contempla:

* 💻 Computadoras de escritorio.
* 💻 Notebooks.
* 📱 Smartphones.
* 📱 Tablets.

Entre los elementos adaptables se encuentran:

* Barra de navegación.
* Hero principal.
* Secciones informativas.
* Tarjetas de cursos.
* Imágenes.
* Formularios.
* Tipografías.
* Espaciados.

---

# 📂 Estructura del proyecto

La estructura puede variar según la evolución del proyecto, pero conceptualmente sigue una organización similar a la siguiente:

```text
JyS-PaginaWeb/
│
├── manage.py
│
├── proyecto/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── ...
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── nosotros.html
│   ├── cursos.html
│   ├── examenes.html
│   └── contacto.html
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── ...
│
├── media/
│   └── ...
│
├── db.sqlite3
├── requirements.txt
└── README.md
```

> **Nota:** La estructura mostrada representa la organización conceptual del proyecto. Los nombres exactos de las aplicaciones y carpetas pueden variar según la versión actual del repositorio.

---

# 🗄️ Base de datos

Durante el desarrollo se utilizó **SQLite** como sistema de base de datos.

SQLite resulta práctico para el desarrollo de aplicaciones Django porque no requiere configurar un servidor de base de datos independiente.

Django permite interactuar con la base de datos mediante su **ORM (Object-Relational Mapping)**.

De esta manera, los modelos definidos en Python representan las estructuras almacenadas en la base de datos.

Por ejemplo:

```python
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
```

Django se encarga de transformar las operaciones realizadas sobre estos modelos en las consultas correspondientes a la base de datos.

---

# 📩 Sistema de contacto

Una de las funcionalidades dinámicas del proyecto es el formulario de contacto.

El proceso puede resumirse de la siguiente manera:

```text
┌──────────────┐
│    Usuario   │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   Formulario │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    Django    │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  API / Email │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   Academia   │
└──────────────┘
```

Esto permitió incorporar una funcionalidad real de comunicación dentro del sitio institucional.

---

# 🚀 Instalación

## Requisitos

Para ejecutar el proyecto localmente se necesita:

* Python 3.x
* pip
* Git

---

## 1. Clonar el repositorio

```bash
git clone https://github.com/martinvernazza42/JyS-PaginaWeb.git
```

Ingresar al proyecto:

```bash
cd JyS-PaginaWeb
```

---

## 2. Crear un entorno virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 4. Ejecutar migraciones

```bash
python manage.py migrate
```

---

## 5. Crear usuario administrador

Si el proyecto utiliza el panel administrativo de Django:

```bash
python manage.py createsuperuser
```

Seguir las instrucciones mostradas por Django.

---

## 6. Ejecutar el servidor

```bash
python manage.py runserver
```

La aplicación estará disponible normalmente en:

```text
http://127.0.0.1:8000/
```

---

# ☁️ Despliegue

El proyecto fue desplegado utilizando **Render**, permitiendo acceder a la aplicación desde Internet.

Durante el proceso de despliegue se trabajó con aspectos como:

* Configuración de Django para producción.
* Variables de entorno.
* Dependencias de Python.
* Servidor WSGI.
* Archivos estáticos.
* Configuración del servicio.
* Integración con servicios externos.

### 🌐 Demo

**Sitio web:**
https://jysenglishacademy.onrender.com/

> ℹ️ Al utilizar un servicio con recursos bajo demanda, el servidor puede tardar unos segundos en responder cuando se encuentra inactivo.

---

# 🔮 Evolución futura

El proyecto fue pensado con la posibilidad de evolucionar desde un sitio institucional hacia una plataforma educativa.

Algunas funcionalidades planteadas para futuras versiones son:

### 👨‍🏫 Módulo para profesores

* [ ] Inicio de sesión.
* [ ] Gestión de cursos.
* [ ] Publicación de material.
* [ ] Carga de videos.
* [ ] Publicación de anuncios.
* [ ] Registro de calificaciones.
* [ ] Gestión de asistencia.

### 👨‍🎓 Módulo para alumnos

* [ ] Cuenta personal.
* [ ] Acceso a cursos.
* [ ] Material de estudio.
* [ ] Videos.
* [ ] Anuncios.
* [ ] Consulta de calificaciones.
* [ ] Consulta de asistencia.

### 💬 Funcionalidades futuras

* [ ] Sistema de comunicación entre profesores y alumnos.
* [ ] Notificaciones.
* [ ] Calendario académico.
* [ ] Sistema de tareas.
* [ ] Integración con una API REST.
* [ ] Aplicación móvil.
* [ ] Panel administrativo avanzado.

---


# 📚 Conocimientos aplicados

El desarrollo del proyecto permitió aplicar conocimientos relacionados con:

* Desarrollo web.
* Python.
* Django.
* Arquitectura MVT.
* HTML5.
* CSS3.
* JavaScript.
* Bootstrap.
* Diseño responsive.
* Bases de datos.
* ORM.
* Formularios.
* Integración con APIs.
* Gestión de archivos multimedia.
* Git y GitHub.
* Deployment.
* Configuración de aplicaciones Django en producción.

---

# 🎓 Contexto académico y profesional

**JyS English Language Office** fue desarrollado como un proyecto orientado a resolver una necesidad real: crear una presencia digital para una institución educativa.

El proyecto permitió trabajar más allá de una página estática, incorporando un **backend desarrollado con Django**, funcionalidades dinámicas, comunicación mediante formularios y despliegue en un entorno accesible públicamente.

Por este motivo, el proyecto también funciona como una muestra práctica de conocimientos en **desarrollo web full-stack**, particularmente en el ecosistema Python/Django.

---

# 👨‍💻 Autor

**Martin Vernazza**

Proyecto desarrollado como parte de mi formación como desarrollador y como proyecto de portfolio.

---

# 📄 Licencia

Este proyecto fue desarrollado principalmente con fines **educativos, académicos y de portfolio**.

Las condiciones de uso y distribución pueden definirse posteriormente según la evolución del proyecto.
