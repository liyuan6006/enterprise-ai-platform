import json
import os
import asyncio

from aiokafka import AIOKafkaProducer

class KafkaProducerService:

    def __init__(self):

        self.bootstrap_servers = os.getenv(
            "KAFKA_BOOTSTRAP_SERVERS",
            "127.0.0.1:9092"
        )
        self.producer = None
        self.started = False

    async def start(self):

        if self.started:
            return

        self.producer = AIOKafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            request_timeout_ms=10000
        )

        await self.producer.start()
        self.started = True

    async def stop(self):

        if self.producer is not None and self.started:
            await self.producer.stop()

        self.started = False
        self.producer = None

    async def publish(
        self,
        topic: str,
        event: dict
    ):

        if not self.started or self.producer is None:
            await self.start()

        await asyncio.wait_for(
            self.producer.send_and_wait(
                topic,
                json.dumps(event).encode("utf-8")
            ),
            timeout=10
        )


kafka_producer = KafkaProducerService()
