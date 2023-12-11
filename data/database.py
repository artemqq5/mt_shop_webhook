import pymysql

from config.cfg import DB_PASSWORD


class MyDataBase:

    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password=DB_PASSWORD,
            db="mt_shop_db",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )

    def get_users_by_position_sql(self, position):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = f'''SELECT * FROM `users` WHERE `position` = %s;'''
                    cursor.execute(_command, position)
                connection.commit()
                return cursor.fetchall()
        except Exception as e:
            print(f"get_users_by_position_sql: {e}")
            return None

    def update_order_status_sql(self, status, id_order):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    _command = f'''UPDATE `orders` SET `status` = %s WHERE `id_order` = %s;'''
                    cursor.execute(_command, (status, id_order))
                connection.commit()
                return True
        except Exception as e:
            print(f"update_order_status_sql: {e}")
            return None
