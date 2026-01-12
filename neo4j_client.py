from neo4j import GraphDatabase
import json

class Neo4jClient:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def store_document(self, doc_id: str, content: list):
        with self.driver.session() as session:
            session.run(
                """
                MERGE (d:Document {id: $id})
                SET d.content = $content
                """,
                id=doc_id,
                content=json.dumps(content)   # 🔥 serialize
            )

    def fetch_document(self):
        with self.driver.session() as session:
            result = session.run(
                "MATCH (d:Document) RETURN d.content AS content ORDER BY d.id DESC LIMIT 1"
            )
            record = result.single()
            return json.loads(record["content"]) if record else []