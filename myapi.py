from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

teachers = {
    1: {
        "name": "james",
        "age" : 27,
        "salary": 35000
    }
}

class Teachers(BaseModel):
    name : str
    age : int
    salary : int

class UpdateTeacher(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    salary : Optional[int] = None

@app.get("/")
def index():
    return {"name": "first name"}

@app.get("/get-teacher/{teacher_id}")
def get_teacher(teacher_id: int = Path(..., description="Enter the id of the student you want to view", gt=0)):
    if teacher_id not in teachers:
        return {"Error": "no data found"}
    return teachers[teacher_id]

@app.get("/get-by-teacher")
def get_teacher(name:str):
    for teacher_id in teachers:
        if teachers[teacher_id]["name"] == name:
            return teachers[teacher_id]
        return {"Data": "Not Found"}
    

@app.post("/create-teacher/{teacher_id}")
def Create_teacher(teacher_id: int, teacher: Teachers):
    if teacher_id in teachers:
        return {"Error": "Student already exist"}
    teachers[teacher_id] = teacher
    return teachers[teacher_id]

@app.put("/update-data/{teacher_id}")
def update_data(teacher_id: int, teacher: UpdateTeacher):
    if teacher_id not in teachers:
        return {"Error": "Record not found"}
    
    if  teacher.name != None:
        teachers[teacher_id].name = teacher.name

    if  teacher.age != None:
        teachers[teacher_id].age = teacher.age

    if  teacher.salary != None:
        teachers[teacher_id].salary = teacher.salary
    
    return teachers[teacher_id]
