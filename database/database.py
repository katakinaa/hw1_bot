import aiosqlite
from database.queries import Queries


class Database:
    def __init__(self, path):
        self.path = path

    async def create_tables(self):
        async with aiosqlite.connect(self.path) as conn:
            await conn.execute(Queries.CREATE_REVIEW_TABLE)
            await conn.execute(Queries.DROP_CATEGORIES_TABLE)
            await conn.execute(Queries.DROP_DISHES_TABLE)
            await conn.execute(Queries.CREATE_CATEGORIES_TABLE)
            await conn.execute(Queries.CREATE_DISHES_TABLE)
            await conn.execute(Queries.POPULATE_CATEGORIES)
            await conn.execute(Queries.POPULATE_DISHES)
            await conn.commit()

    async def execute(self, query: str, params: tuple = ()):
        async with aiosqlite.connect(self.path) as conn:
            await conn.execute(query, params)
            await conn.commit()
