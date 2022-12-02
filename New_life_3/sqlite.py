import sqlite3 as sq


class Database:
    def __init__(self, db_file):
        self.connection = sq.connect(db_file)
        self.cursor = self.connection.cursor()

    def create_profile(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchmany(1)
            return bool(len(result))
    # if not user:
    #     cur.execute("INSERT INTO profile VALUES(?);", (user_id))
    #     db.commit()

    def edit_profile(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'users' ('user_id') VALUES(?)", (user_id,))

    def set_active(self, user_id, active):
        with self.connection:
            return self.cursor.execute("UPDATE users SET active = ? WHERE user_id = ?", (active, user_id,))

    def get_users(self):
        with self.connection:
            return self.cursor.execute("SELECT user_id, active FROM users").fetchall()
    # async with state.proxy() as data:
        # cur.execute("UPDATE profile SET photo = '{}', age = '{}', description = '{}', name = '{}', WHERE user_id == '{}'".format(
        #     data['photo'], data['age'], data['description'], data['name'], user_id))
        # db.commit()
        # cur.execute('CREATE TABLE IF NOT EXISTS profile(user_id INTEGER)')