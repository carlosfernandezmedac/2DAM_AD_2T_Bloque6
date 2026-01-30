# Proyecto FARM Stack – Sistema de Gestión

Proyecto Full Stack basado en el **FARM Stack (FastAPI, React y MongoDB)**.
La aplicación implementa un sistema de gestión tipo CRUD / ERP básico,
siguiendo una **arquitectura modular por componentes desacoplados**, orientada
a aplicaciones empresariales.

Inspirado en el vídeo:
https://www.youtube.com/watch?v=7WE6v2EKm7M

---

## Stack Tecnológico

- Frontend: React
- Backend: FastAPI (Python)
- Base de datos: MongoDB
- Validación de datos: Pydantic
- Comunicación: API REST (JSON)

---

## Arquitectura General (FARM Stack)

React (Frontend)
↓
FastAPI (API REST / Endpoints)
↓
Servicios / Lógica de Negocio
↓
Repositorio / Acceso a Datos
↓
MongoDB

---

## Componentes del Backend

### Modelos (Pydantic)
Definen la estructura y validación de los datos.  
Archivo: `models.py`

### Repositorio / Acceso a Datos
Encapsula el acceso a MongoDB y realiza operaciones CRUD.  
Archivo: `database.py`

### Servicios / Lógica de Negocio
Implementan reglas de negocio y eventos del sistema.

### Endpoints / API REST
Interfaz pública del sistema (GET, POST, PUT, DELETE).  
Archivo: `main.py` o `routers/`

---

## Encapsulación y Desacoplamiento

- El frontend no accede directamente a la base de datos.
- MongoDB solo se usa desde el repositorio.
- Los endpoints no contienen lógica de persistencia.

Esto permite escalabilidad y mantenimiento.

---

## Eventos del Sistema

Cada operación representa un evento lógico:
- Crear datos (POST)
- Consultar datos (GET)
- Modificar datos (PUT)
- Eliminar datos (DELETE)

---

## Documentación Automática

FastAPI genera documentación automática:
- Swagger UI: /docs
- ReDoc: /redoc

---

## Infografía del Proyecto

La siguiente infografía resume toda la arquitectura y los conceptos del proyecto:

![Infografía FARM Stack](A_detailed_infographic_in_Spanish_illustrates_Tema.png)

---

## Conclusión

Este proyecto demuestra:
- Arquitectura por componentes
- Acceso a datos encapsulado
- Uso del FARM Stack
- Buenas prácticas para aplicaciones empresariales
