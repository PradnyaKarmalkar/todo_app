

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles



app = FastAPI()

# Add this after your app = FastAPI() line
app.mount("/static", StaticFiles(directory="static"), name="static")

# Add this route for the root path
@app.get("/")
def read_root():
    return FileResponse("static/index.html")

tasks=[]

class Task(BaseModel):
    name: str
    
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/hello123')
def hello():
    return {'msg':'hello from hello123'}

@app.post('/create-task')
def create_task(task: Task):
    print(task)
    tasks.append(task)
    return {'msg':"Task added Successfully"}

@app.get('/get-task')
def get_task():
    return {"tasks":tasks}

@app.put('/update-task/{task_id}')
def update_task(task_id: int, task: Task):
    if task_id < 0 or task_id >= len(tasks):
        return { 'msg': 'Task not found' }
    tasks[task_id] = task
    return { 'msg': 'Task updated succesfully' }

@app.delete('/delete-task/{task_id}')
def delete_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        return { 'msg': 'Task not found' }
    tasks.pop(task_id)
    return { 'msg': 'Task deleted succesfully' }