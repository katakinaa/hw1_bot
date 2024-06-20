class Queries:
    CREATE_REVIEW_TABLE = """
        CREATE TABLE IF NOT EXISTS review_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            contact TEXT,
            date TEXT,
            food_quality INTEGER,
            cleanliness INTEGER,
            comment TEXT
        )
    """