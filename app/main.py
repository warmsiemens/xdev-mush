import uvicorn
from fastapi import FastAPI
from app.routers import mushroom, basket


app = FastAPI()

app.include_router(mushroom.router, prefix="/mushrooms", tags=["Mushrooms"])
app.include_router(basket.router, prefix="/baskets", tags=["Baskets"])


if __name__ == '__main__':
    uvicorn.run("main:app")
