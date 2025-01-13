import sqlite3

class Training_sessions:
    pass

class Training:
    pass


class User:

    def __init__(self, id: int, name: str, verification: bool, password: str):
        self.__id = id
        self.__name = name
        self.__verification = verification
        self.__password = password
        self.__training_session = Training_sessions()



# class User:
#
#     def __init__(self, name: str, phone: str, surname: str = None, email: str = None):
#         self._name = name
#         self._phone = phone
#         self._surname = surname
#         self._email = email
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def phone(self):
#         return self._phone
#
#     @property
#     def surname(self):
#         return self._surname
#
#     @property
#     def email(self):
#         return self._email
#
#     def __str__(self):
#         contact_info = f"Имя: {self._name}, номер телефона: {self._phone}"
#         return contact_info
#

class ContactBook:

    def __init__(self):
        self._current_id = 1
        self._contacts = {}
        self._free_ids = []

    @property
    def contacts_count(self):
        return len(self._contacts)

    def __iter__(self):
        for contact_id, contact in self._contacts.items():
            yield contact

    def _get_free_id(self):
        if self._free_ids:
            return self._free_ids.pop()
        old_id = self._current_id
        self._current_id += 1
        return old_id

    def add_contact(self, contact: User):
        new_id = self._get_free_id()
        self._contacts[new_id] = contact

    def find_contact_by_name(self, name: str):
        name = name.lower()

        found_contacts = []
        for contact in self:
            contact_name = contact.name.lower()

            if name.startswith(contact_name) or contact_name.startswith(name):
                found_contacts.append(contact)

        return found_contacts

    def _find_contact_id(self, needed_contact: User):
        for user_id, contact in self._contacts.items():
            if contact == needed_contact:
                return user_id
        return None

    def remove_contact(self, contact: User):
        contact_id = self._find_contact_id(contact)
        if contact_id is not None:
            self._contacts.pop(contact_id)
            self._free_ids.append(contact_id)


class ContactBookSql:

    def __init__(self):
        self._connection = sqlite3.connect("users.db")
        self._cursor = self._connection.cursor()
        self._initialize()

    def _initialize(self):
        self._cursor.execute("""
            CREATE TABLE IF NOT EXISTS Contacts (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                contact_name    TEXT NOT NULL,
                contact_surname TEXT,
                contact_phone   TEXT NOT NULL,
                contact_email   TEXT
            );
        """)

    def __iter__(self):
        self._cursor.execute("SELECT * FROM Contacts")
        contact_tuples = self._cursor.fetchall()

        for contact_id, contact_name, contact_surname, contact_phone, contact_email in contact_tuples:
            contact = User(contact_name, contact_phone, contact_surname, contact_email)
            yield contact

    @property
    def contacts_count(self):
        self._cursor.execute("SELECT count(*) FROM Contacts")
        count = self._cursor.fetchone()[0]
        return count

    def add_contact(self, contact: User):
        name = contact.name
        surname = contact.surname
        phone = contact.phone
        email = contact.email

        self._cursor.execute(f"""
            INSERT INTO Contacts(contact_name, contact_surname, contact_phone, contact_email) VALUES
                (?, ?, ?, ?)                             
            """,
                             (name, surname, phone, email)
                             )

    def find_contact_by_name(self, name: str):
        self._cursor.execute(f"""
            SELECT * FROM Contacts WHERE "{name}" = contact_name
        """)

        contacts = []
        contact_tuples = self._cursor.fetchall()
        for (contact_id, contact_name, contact_surname, contact_phone, contact_email) in contact_tuples:
            contact = User(contact_name, contact_phone, contact_surname, contact_email)
            contacts.append(contact)

        return contacts

    def _find_contact_id(self, contact: User):
        name = contact.name
        phone = contact.phone

        self._cursor.execute(f"""
            SELECT * FROM Contacts WHERE "{name}" = contact_name AND "{phone}" = contact_phone
        """)

        ids = []
        contact_tuples = self._cursor.fetchall()
        for (contact_id, contact_name, contact_surname, contact_phone, contact_email) in contact_tuples:
            ids.append(contact_id)

        return ids

    def remove_contact(self, contact: User):
        ids = self._find_contact_id(contact)
        if ids:
            contact_id = ids[0]
            self._cursor.execute(f"""DELETE FROM Contacts WHERE id = {contact_id}""")
