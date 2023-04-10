class Database:
    __instance = None

    def __init__(self):
        if Database.__instance is not None:
            raise Exception("Database class is a singleton")
        else:
            Database.__instance = self

    @staticmethod
    def get_instance():
        if Database.__instance is None:
            Database()
        return Database.__instance


database1 = Database.get_instance()
database2 = Database.get_instance()

print(database1 is database2)  # True
