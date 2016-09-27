import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("main.db")
        self.c = self.conn.cursor()

    def create_tables(self):
        self.c.execute("DROP TABLE IF EXISTS testTable")
        create_columns = "p_id INT NOT NULL, info TEXT NOT NULL, variable TEXT, char CHAR"
        self.c.execute("CREATE TABLE testTable (%s)" % create_columns)
        self.conn.commit()

    def insert_data(self, p_id, name, info, variable, char):
        try:
            self.c.execute("INSERT INTO testTable VALUES(?, ?, ?, ?)", (p_id, info, variable, char))
            self.conn.commit()
        except sqlite3.Error:
            print("ERROR : INSERT")

    def delete_data(self, column_name, parameter):
        try:
            self.c.execute("DELETE FROM testTable WHERE %s = %s" % (column_name, parameter))
            self.conn.commit()
        except sqlite3.Error:
            print("ERROR : DELETE")

    def update_data(self, c1, update, c2, parameter):
        try:
            self.c.execute("UPDATE testTable SET %s = %s WHERE %s = %s" % (c1, update, c2, parameter))
            self.conn.commit()
        except sqlite3.Error:
            print("ERROR : UPDATE")

    def print_all(self):
        self.c.execute("SELECT * FROM testTable")
        for i in self.c:
            print(i)

    def shutdown(self):
        self.c.close()

o = Database()

o.create_tables()

for j in ['A', 'B', 'C', 'D', 'E', 'F']:
    for i in range(1, 5):
        o.insert_data(i, "Stuff, Stuff and more Stuff", "abc", j)

o.print_all()

o.shutdown()
