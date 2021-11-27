import sqlite3 as sql


class Database:
    def __init__(self):
        self.con = sql.connect("users.db")
        self.cur = self.con.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS base (
                    snils STRING,
                    id INTEGER,
                    speciality STRING,
                    sub BOOl
                    )""")
        self.con.commit()

    # добавить пользователя в БД
    def add_user(self, id, snils, speciality):
        with self.con:
            return self.cur.execute("INSERT INTO base VALUES (?, ?, ?, ?)", (snils, id, speciality, False,))

    # проверить наличие пользователя БД
    def user_exists(self, id):
        result = self.cur.execute("SELECT id FROM base WHERE id = ?", (id,))
        return bool(len(result.fetchall()))

    # получить все строчку с подпиской
    def get_sub(self, status=True):
        with self.con:
            return self.cur.execute("SELECT * FROM base WHERE sub = ?", (status,)).fetchall()

    # обновить поле подписки для пользователя
    def update_sub(self, id, status=True):
        with self.con:
            return self.cur.execute("UPDATE base SET sub = ? WHERE id = ?", (status, id,))

    # получить все строчки нужного пользователя
    def get_info(self, id):
        result = self.cur.execute("SELECT * FROM base WHERE id = ?", (id,))
        return result.fetchall()

    # удалить определенную специальность
    def delete_spec(self, id, spec):
        with self.con:
            return self.cur.execute("DELETE FROM base WHERE (id, speciality) = (?,?)", (id, spec,))

    def close(self):
        self.con.close()
