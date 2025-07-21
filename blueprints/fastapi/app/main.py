from fastapi import FastAPI
from routers import hello, world

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "${{ values.name }} project for development..",
        "api_1":  "/hello",
        "api_2":  "/world"
    }

app.include_router(hello.router)
app.include_router(world.router)