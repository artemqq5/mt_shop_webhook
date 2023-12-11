from data.database import MyDataBase


class MyRepository(MyDataBase):

    def get_users_by_position(self, position):
        return self.get_users_by_position_sql(position)

    def update_order_status(self, status, id_order):
        return self.update_order_status_sql(status, id_order)
