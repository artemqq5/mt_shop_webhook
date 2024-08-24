from data.database import MyDataBase


class InvoiceRepository(MyDataBase):

    def invoice(self, external_id):
        query = "SELECT * FROM `invoices` WHERE `external_id` = %s;"
        return self._select_one(query, (external_id, ))

    def add(self, external_id, number, value, user_id, username, firstname, date):
        query = "INSERT INTO `invoices` (`external_id`, `number`, `value`, `user_id`, `username`, `firstname`, `date`) VALUE (%s, %s, %s, %s, %s, %s, %s);"
        return self._insert(query, (external_id, number, value, user_id, username, firstname, date))

    def update(self, status, external_id):
        query = "UPDATE `invoices` SET `status` = %s WHERE `external_id` = %s;"
        return self._update(query, (status, external_id))
