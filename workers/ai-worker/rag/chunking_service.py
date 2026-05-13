class ChunkingService:

    def chunk_text(
        self,
        text
    ):

        chunks = text.split("\n\n")

        return chunks