import sqlite3

class Training_sessions:
    pass

class Training:
    pass

class Database:
        
    def __init__(self):
        self._connection = sqlite3.connect("users.db")
        self._cursor = self._connection.cursor()
        self._initialize()

    def _initialize(self):
        self._cursor.execute("""
            CREATE TABLE IF NOT EXISTS Contacts (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                id_user INTEGER NOT NULL,
                user_name    TEXT NOT NULL,
                verification BOOL,
                password   TEXT
            );
        """)

    def add_user(self, user):
        id_user = user.id
        user_name = user.name
        verification = user.verification
        password = user.password


        self._cursor.execute(f"""
    INSERT INTO Contacts(id_user, user_name, verification, password) VALUES
        (?, ?, ?, ?)                             
    """,
                        (id_user, user_name, verification, password)
                        )



class User:

    def __init__(self, id: int, name: str, verification: bool, password: str):
        self.__id = id
        self.__name = name
        self.__verification = verification
        self.__password = password
        self.__training_session = Training_sessions()
    
    @property
    def name(self):
        return self.__name
    
    @property
    def id(self):
        return self.__id
    
    @property
    def verification(self):
        return self.__verification
    
    @property
    def password(self):
        return self.__password
    
    @property
    def training_session(self):
        return self.__training_session