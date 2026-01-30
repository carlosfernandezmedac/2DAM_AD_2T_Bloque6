# Proyecto FARM Stack – Sistema de Gestión

Proyecto Full Stack basado en el **FARM Stack (FastAPI + React + MongoDB)**.
La aplicación implementa un sistema de gestión tipo CRUD, siguiendo una
arquitectura sencilla y alineada con el temario y el vídeo de referencia.

---

## Stack Tecnológico

- **Frontend**: React
- **Backend**: FastAPI (Python)
- **Base de datos**: MongoDB
- **Modelos y validación**: Pydantic
- **Comunicación**: HTTP + JSON (GET, POST, PUT, DELETE)

---

## Arquitectura General

```
React (Frontend)
   ↓
FastAPI (main.py - Endpoints)
   ↓
models.py (Modelos de datos)
   ↓
database.py (Acceso a datos / CRUD)
   ↓
MongoDB (Base de datos)
```

Esta arquitectura separa claramente cada responsabilidad del sistema.

---

## Backend con FastAPI

### main.py – Endpoints

`main.py` contiene los **endpoints**, que son los métodos públicos del sistema.
Desde aquí se reciben las peticiones del frontend.

Ejemplo:

```python
from fastapi import FastAPI
from database import get_all_tasks

app = FastAPI()

@app.get("/tasks")
async def get_tasks():
    return await get_all_tasks()
```

Los endpoints usan métodos HTTP:
- GET → consultar datos
- POST → crear datos
- PUT → modificar datos
- DELETE → eliminar datos

---

### models.py – Modelos (Pydantic)

Los modelos definen la estructura de los datos y validan la información.

Ejemplo:

```python
from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    id: Optional[str] = None
    title: str
    description: Optional[str] = None
    completed: bool = False
```

Aquí se define por ejemplo qué es una tarea y qué campos tiene.

---

### database.py – Acceso a datos

Este archivo se encarga de todas las operaciones con MongoDB.
Aquí se implementa el CRUD.

Ejemplo:

```python
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.todo_db
collection = db.tasks

async def get_all_tasks():
    tasks = []
    async for task in collection.find():
        tasks.append(task)
    return tasks

async def insert_task(task):
    await collection.insert_one(task)
```

El resto de la aplicación **no accede directamente a la base de datos**.

---

## MongoDB – Base de datos

MongoDB almacena los datos de forma persistente.
Cada tarea se guarda como un documento.

Ejemplo de documento:

```json
{
  "title": "Estudiar FastAPI",
  "description": "Ver el vídeo del proyecto",
  "completed": false
}
```

---

## Operaciones CRUD

El sistema permite las operaciones básicas:
- Crear (POST)
- Leer (GET)
- Actualizar (PUT)
- Eliminar (DELETE)

Estas operaciones se usan tanto en el backend como desde el frontend.

---

## Frontend con React

El frontend se encarga de:
- Mostrar formularios
- Mostrar tablas de datos
- Enviar peticiones al backend

Ejemplo de petición desde React:

```javascript
fetch("http://localhost:8000/tasks")
  .then(res => res.json())
  .then(data => console.log(data));
```

---

## Infografía del Proyecto

La infografía del repositorio muestra visualmente:
- El stack FARM
- El flujo de datos
- Dónde encajan `main.py`, `models.py` y `database.py`

![alt text](farm.png)

---

## Conclusión

Este proyecto demuestra:
- Uso de FastAPI con endpoints
- Uso de modelos con Pydantic
- Acceso a datos con MongoDB
- Operaciones CRUD completas
- Arquitectura clara y sencilla, alineada con el temario


## Webgrafía

Inspirado en el vídeo:
https://www.youtube.com/watch?v=7WE6v2EKm7M