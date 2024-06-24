class Queries:
    CREATE_REVIEW_TABLE = """
            CREATE TABLE IF NOT EXISTS review_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                contact TEXT,
                date TEXT,
                food_quality TEXT,
                cleanliness TEXT,
                comment TEXT
            )
    """
    DROP_CATEGORIES_TABLE = "DROP TABLE IF EXISTS categories"
    DROP_DISHES_TABLE = "DROP TABLE IF EXISTS dishes"
    CREATE_CATEGORIES_TABLE = """
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            ) 
    """
    CREATE_DISHES_TABLE = """
            CREATE TABLE IF NOT EXISTS dishes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price INTEGER,
                image TEXT,
                category_id INTEGER,
                FOREIGN KEY (category_id) REFERENCES categories(id)
            )
    """
    POPULATE_CATEGORIES = """
            INSERT INTO categories (name)
            VALUES ("Напитки"),
            ("Первые блюда"),
            ("Вторые блюда"),
            ("Десерты")
        """
    POPULATE_DISHES = """
            INSERT INTO dishes (name, price, image, category_id)
            VALUES ("Коктейль", 150, "images/Коктейль.jpg", 1),
            ("Макаронс", 500, "images/Макаронс.jpg", 2),
            ("Солянка", 300, "images/Солянка.jpg", 3),
            ("Латте", 90, "images/Латте.jpg", 1),
            ("Бублик с семгой", 250, "images/Бублик с семгой.jpg", 4),
            ("Лагман", 200, "images/Лагман.jpg", 3)
        """
