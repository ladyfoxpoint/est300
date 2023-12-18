from tinydb import TinyDB
import os

from ..utils.logger import Logger

class Est:
    def __init__(self):
        self.logger = Logger("EST", "green", 4)
        pass

    def handle_csv(self, path):
        # TODO: Implement CSV handling
        pass

    def set_database(self, database, type):
        self.logger.log("info", f"Setting database to {database} of type {type}")
        base_folder = os.getcwd()
        path = os.path.join(base_folder, "data", "db", type, database)
        if os.path.exists(path):
            match type:
                case "json":
                    try:
                        self.db = TinyDB(path)
                    except Exception as exception:
                        self.logger.log("error", "Could not open database.")
                        self.logger.log("debug", exception.__str__())
                    finally:
                        self.logger.log("info", "Database opened successfully.")
                case "csv":
                    self.logger.log("error", "CSV not supported yet.")
                    pass
                case _:
                    self.logger.log("error", "Database type not supported.")
        else:
            self.logger.log("error", f"Database {database} does not exist.")
    
    def read_all(self):
        return self.db.all()

    def insert_data(self, data):
        self.db.insert(data)
    
    def nuke(self):
        self.db.truncate()
        self.logger.log("warn", "Database purged.")

