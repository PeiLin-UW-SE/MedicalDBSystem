import sqlite3
import time
import datetime

f = open("error_log.txt", "a")


def getTime():
    unixTime = time.time()
    date = str(datetime.datetime.fromtimestamp(unixTime).strftime('%b %d %Y %I:%M:%S %p'))
    return date


class DBInteraction:
    def __init__(self):
        self.conn = sqlite3.connect("medDB.db")
        self.c = self.conn.cursor()

        self.p_id = -1
        self.name = "Not Found"
        self.age = 0
        self.gender = "Not Found"
        self.lastVisit = "Not Found"
        self.allergies = "Not Found"
        self.diseases = "Not Found"
        self.history = "Not Found"
        self.comments = "Not Found"

    def create_tables(self):
        create_columns = "p_id INT NOT NULL, name TEXT NOT NULL," \
                         " age INT NOT NULL, gender TEXT NOT NULL, lastVisit TEXT," \
                         "allergies TEXT, diseases TEXT, history TEXT, comments TEXT, lastMod TEXT"
        self.c.execute("CREATE TABLE IF NOT EXISTS mainTable (%s)" % create_columns)

    def insert_data(self, p_id, name, age, gender, lastVisit, allergies, diseases, history, comments):
        try:
            self.c.execute("INSERT INTO mainTable "
                           "(p_id, name, age, gender, lastVisit, allergies, diseases, history, comments, lastMod) "
                           "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                           (p_id, name, age, gender, lastVisit, allergies, diseases, history, comments, getTime()))
            self.conn.commit()
        except sqlite3.Error:
            f.write("INSERT :: sqlite3.Error" + "\t" + str(getTime()) + "\n")

    def load_data(self, p_id):
        try:
            self.c.execute("SELECT p_id, name, age, gender, lastVisit, allergies, diseases, history, comments "
                           "FROM mainTable WHERE p_id == (?)", str(p_id))
            p_id, name, age, gender, lastVisit, allergies, diseases, history, comments = self.c.fetchone()

            self.p_id = p_id
            self.name = name
            self.age = age
            self.gender = gender
            self.lastVisit = lastVisit
            self.allergies = allergies
            self.diseases = diseases
            self.history = history
            self.comments = comments

        except sqlite3.Error:
            print("LOAD :: sqlite3.Error")
            f.write("LOAD :: sqlite3.Error" + "\t" + str(getTime()) + "\n")
        except TypeError:
            print("LOAD :: TypeError")
            f.write("LOAD :: TypeError" + "\t" + str(getTime()) + "\n")
        except sqlite3.ProgrammingError:
            print("LOAD :: sqlite3.ProgrammingError")
            f.write("LOAD :: sqlite3.ProgrammingError" + "\t" + str(getTime()) + "\n")

    def update_data(self, p_id, name, age, gender, lastVisit, allergies, diseases, history, comments):
        try:
            self.c.execute("UPDATE mainTable "
                           "SET p_id = ?, name = ?, age = ?, gender = ?, lastVisit = ?, "
                           "allergies = ?, diseases = ?, history = ?, comments = ?, lastMod = ? "
                           "WHERE p_id = ?", (int(p_id), name, int(age), gender, lastVisit, allergies, diseases,
                                              history, comments, getTime(), int(p_id)))
            self.conn.commit()
        except sqlite3.Error:
            f.write("UPDATE :: sqlite3.Error" + "\t" + str(getTime()) + "\n")
        except ValueError:
            f.write("UPDATE :: ValueError" + "\t" + str(getTime()) + "\n")

    def shutdown(self):
        # self.print_all()
        self.c.close()
        self.conn.close()
        f = open('error_log.txt', 'a')
        f.write("SHUTDOWN TIME :: " + str(getTime()) + "\n")
        f.close()

    def search_data(self, name):
        try:
            self.c.execute("SELECT p_id, name, age, gender FROM mainTable WHERE name LIKE ?", (str(name), ))
            return self.c.fetchall()
        except sqlite3.Error:
            f.write("SEARCH :: sqlite3.Error" + "\t" + str(getTime()) + "\n")

# ===============================================================================================================
# ============================================== DEVELOPER METHODS ==============================================
# ===============================================================================================================

    def print_all(self):
        self.c.execute("SELECT * FROM mainTable")
        for row in self.c:
            print(row)

    def delete_data(self, p_id):
        try:
            self.c.execute("DELETE FROM mainTable WHERE p_id = ?", p_id)
            self.conn.commit()
        except sqlite3.Error:
            print("ERROR : DELETE")
