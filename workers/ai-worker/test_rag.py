from rag.retrieval_service import (
    RetrievalService
)

retrieval_service = RetrievalService()

results = retrieval_service.retrieve(
    "Can employees use casinos during travel?"
)

print(results)