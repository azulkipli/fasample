from fastapi import FastAPI, Form
from routers import user
from routers import item

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/get_name/{name}")
async def get_name(name: str):
    return {"message": f"Hello {name}"}


@app.post('/city')
def submit_city(city: str = Form(...)):
    return {'city': city}


app.include_router(user.router)
app.include_router(item.router)
