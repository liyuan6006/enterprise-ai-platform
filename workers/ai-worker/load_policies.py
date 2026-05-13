from rag.chunking_service import (
    ChunkingService
)

from rag.embedding_service import (
    EmbeddingService
)

from rag.vector_service import (
    VectorService
)

with open(
    "documents/travel_policy.txt",
    "r"
) as f:

    text = f.read()

chunking_service = ChunkingService()

embedding_service = EmbeddingService()

vector_service = VectorService()

chunks = chunking_service.chunk_text(
    text
)

for chunk in chunks:

    embedding = (
        embedding_service
        .generate_embedding(chunk)
    )

    vector_service.store_embedding(
        chunk,
        embedding
    )

    print("Stored chunk:")
    print(chunk)