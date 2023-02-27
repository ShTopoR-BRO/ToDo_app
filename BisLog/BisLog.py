import random
import requests

class BisLog:
    def __init__(self, connect):
        self.connect = connect
        self.cur = self.connect.cursor()

    def show(self):
        self.cur.execute("""SELECT * FROM todo;""")
        result = self.cur.fetchall()
        # res = []
        # for i in range(len(result)):
        #     res.append(list(result[i]))
        return result

    def add(self, bisness):
        id = random.randint(1000, 15000)
        self.cur.execute("""INSERT INTO todo ("id", "bisness") VALUES (%s, %s)""",
                         (id, bisness))
        self.connect.commit()

    def del_(self, bisness: str = ""):
        self.cur.execute("""DELETE FROM todo WHERE bisness=%s""", (bisness,))
        self.connect.commit()