from fastapi import FastAPI
import uvicorn
from district.router import dist_router


app = FastAPI(title="dsf")
app.include_router(router=dist_router, prefix="/district")


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)