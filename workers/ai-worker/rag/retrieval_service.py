from rag.embedding_service import (
    EmbeddingService
)

from rag.vector_service import (
    VectorService
)

embedding_service = EmbeddingService()

vector_service = VectorService()

class RetrievalService:

    def retrieve(
        self,
        query
    ):

        embedding = (
            embedding_service
            .generate_embedding(query)
        )

        return vector_service.search_similar(
            embedding
        )