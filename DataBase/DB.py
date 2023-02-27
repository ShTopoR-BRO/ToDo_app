import psycopg2


class DataBase:
        def __init__(self, database, user, password, host, port):
            self.database = database
            self.user = user
            self.password = password
            self.host = host
            self.port = port

        def connect(self):
            connection = psycopg2.connect(
                database=self.database,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            return connection