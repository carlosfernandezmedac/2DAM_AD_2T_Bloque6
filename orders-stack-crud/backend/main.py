from fastapi import FastAPI, HTTPException
from database import get_all_tasks, create_task, get_one_task, get_one_task_id, delete_task, update_task
from models import Task, UpdateTask

app = FastAPI()

@app.get('/')
def welcome():
    return {'message': 'Bienvenido a my FastApi!'}

@app.get('/api/tasks')
async def get_tasks():
    tasks = await get_all_tasks()
    return tasks

@app.post('/api/tasks', response_model=Task)
async def save_task(task: Task):
    
    taskFound = await get_one_task(task.title)
    if taskFound:
        raise HTTPException(409, 'Task already exists')
    
    response = await create_task(task.dict())
    if response:
        return response
    raise HTTPException(400, 'Something went wrong')

@app.get('/api/tasks/{id}', response_model=Task)
async def get_task(id: str):
    task = await get_one_task_id(id)
    if task:
        return task
    raise HTTPException(404, f"Task with id {id} not found")

@app.put('/api/tasks/{id}', response_model= Task)
async def put_tasks(id: str, task: UpdateTask):
    response = await update_task(id, task)
    if response:
        return response
    raise HTTPException(404, f"Task with id {id} not found")

@app.delete('/api/tasks/{id}')
async def remove_task(id:str):
    response = await delete_task(id)
    if response:
        return "Successfully deleted task"
    raise HTTPException(404, f"Task with id {id} not found")


"""
@app.get('/')
def welcome():
    return {'message': 'Bienvenido a my FastApi!'}

@app.get('/api/tasks')
async def get_tasks():
    tasks = await get_all_tasks()
    return tasks

@app.post('/api/tasks')
async def create_tasks():
    return 'all tasks'

@app.get('/api/tasks/{id}')
async def get_task():
    return 'single task'

@app.put('/api/tasks/{id}')
async def update_tasks():
    return 'updating tasks'

@app.delete('/api/tasks/{id}')
async def delete_task():
    return 'delete task'
"""

