import psycopg2

class VectorService:

    def __init__(self):

        self.conn = psycopg2.connect(
            host="localhost",
            database="enterprise_ai",
            user="postgres",
            password="postgres",
            port=5433
        )

    def store_embedding(
        self,
        content,
        embedding
    ):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            INSERT INTO policy_embeddings
            (content, embedding)
            VALUES (%s, %s)
            """,
            (
                content,
                embedding
            )
        )

        self.conn.commit()

        cursor.close()

    def search_similar(
        self,
        embedding
    ):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT
                content,
                embedding <-> %s::vector
                AS distance
            FROM policy_embeddings
            ORDER BY distance
            LIMIT 3
            """,
            (embedding,)
        )

        results = cursor.fetchall()

        cursor.close()

        return results