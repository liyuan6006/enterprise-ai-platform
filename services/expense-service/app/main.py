from fastapi import FastAPI

from app.routes.expense_routes import router

from app.models.expense import Base
from app.database import engine

from app.messaging.kafka_producer import kafka_producer

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:

        await conn.run_sync(
            Base.metadata.create_all
        )

    await kafka_producer.start()

@app.on_event("shutdown")
async def shutdown():

    await kafka_producer.stop()
