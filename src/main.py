from fastapi import FastAPI
import uvicorn
from district.router import dist_router
from fastapi.staticfiles import StaticFiles


app = FastAPI(title="dsf")
app.include_router(router=dist_router, prefix="/district")
app.mount("/", StaticFiles(directory="src/static", html=True), name="static")

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)