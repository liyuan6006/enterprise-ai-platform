import asyncio
import json

from aiokafka import AIOKafkaConsumer
from services.agent_service import (
    AgentService
)

async def consume():

    consumer = AIOKafkaConsumer(
        "expense-created",
        bootstrap_servers="127.0.0.1:9092",
        group_id="ai-workers",
        session_timeout_ms=30000,
        heartbeat_interval_ms=10000,
        max_poll_interval_ms=300000
    )

    agent_service = AgentService()
    await consumer.start()
    print("AI worker started. Waiting for expense-created events...")

    try:

        async for message in consumer:

            data = json.loads(
                message.value.decode("utf-8")
            )

            print("EVENT RECEIVED")
            print(data)

            result = await agent_service.analyze_expense(
                data
            )

            print("\nAI ANALYSIS")
            print(result)

    finally:

        await consumer.stop()

if __name__ == "__main__":
    asyncio.run(consume())
