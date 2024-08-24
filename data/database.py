import pymysql
import private_cfg as config


class MyDataBase:

    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password=config.DB_PASSWORD,
            db=config.DB_NAME,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def _insert(self, query, args=None):
        try:
            with self.connection as con:
                with con.cursor() as cursor:
                    return cursor.execute(query, args)
        except Exception as e:
            print(f"_insert\n({query}): {e}")

    def _select_one(self, query, args=None):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query, args)
                    return cursor.fetchone()
        except Exception as e:
            print(f"_select_one\n({query}): {e}")

    def _select(self, query, args=None):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query, args)
                    return cursor.fetchall()
        except Exception as e:
            print(f"_select\n({query}): {e}")

    def _update(self, query, args=None):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    return cursor.execute(query, args)
        except Exception as e:
            print(f"_update\n({query}): {e}")

    def _delete(self, query, args=None):
        try:
            with self.connection as con:
                with con.cursor() as cursor:
                    return cursor.execute(query, args)
        except Exception as e:
            print(f"_delete\n({query}): {e}")
