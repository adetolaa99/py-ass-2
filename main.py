from fastapi import FastAPI
from .api.endpoints import customer, product, order

app = FastAPI()

app.include_router(customer.router)
app.include_router(product.router)
app.include_router(order.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
