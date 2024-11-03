from fastapi import FastAPI
import uvicorn


app = FastAPI(title="dsf")


@app.get("/")
def hello():
    return {"Hello": "World"}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)