import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
print(sys.path)

from fastapi import FastAPI
from app.routers import category, products
import uvicorn

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "My e-commerce app"}

if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True, port=8000)

app.include_router(category.router)
app.include_router(products.router)
