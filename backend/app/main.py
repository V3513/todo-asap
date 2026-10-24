from fastapi import FastAPI

app = FastAPI(title="todo-asap API")

@app.get("/")
def root():
    return {"message": "todo-asap API"}
