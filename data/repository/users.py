from data.database import MyDataBase


class UserRepository(MyDataBase):

    def add(self, user_id, username, lang):
        query = "INSERT INTO `users` (`user_id`, `username`, `lang`) VALUES (%s, %s, %s);"
        return self._insert(query, (user_id, username, lang))

    def user(self, user_id):
        query = "SELECT * FROM `users` WHERE `user_id` = %s;"
        return self._select_one(query, (user_id,))

    def users(self):
        query = "SELECT * FROM `users`;"
        return self._select(query)

    def admins(self):
        query = "SELECT * FROM `users` WHERE `role` = 'admin';"
        return self._select(query)

    def clients(self):
        query = "SELECT * FROM `users` WHERE `role` = 'client';"
        return self._select(query)

    # temporary for update data in new structure tables database
    def update_lang(self, user_id, lang):
        query = "UPDATE `users` SET `lang` = %s WHERE `user_id` = %s;"
        return self._select_one(query, (lang, user_id))

    def update_ban_by_id(self, user_id, ban_state):
        query = "UPDATE `users` SET `banned` = %s WHERE `user_id` = %s AND `role` != 'admin';"
        return self._update(query, (ban_state, user_id))

    def update_ban_by_username(self, username, ban_state):
        query = "UPDATE `users` SET `banned` = %s WHERE `username` = %s AND `role` != 'admin';"
        return self._update(query, (ban_state, username))

    def banned_users(self):
        query = "SELECT * FROM `users` WHERE `banned` = '1';"
        return self._select(query)

    def update_balance(self, user_id, value):
        query = "UPDATE `users` SET `balance` = %s WHERE `user_id` = %s;"
        return self._update(query, (value, user_id))

    # def add_user(self, telegram_id, name, time):
    #     return self._add_user_sql(telegram_id, name, time)
    #
    # def get_user(self, telegram_id):
    #     return self._get_user_sql(telegram_id)
    #
    # def get_users(self, position):  # get users by position or All by default
    #     return self._get_users_sql(position)
    #
    # def ban_user_by_id(self, user_id):
    #     COMMAND_ = "UPDATE `users` SET `banned` = 1 WHERE `id` = %s;"
    #     return self._update(COMMAND_, (user_id,))
    #
    # def ban_user_by_username(self, username):
    #     COMMAND_ = "UPDATE `users` SET `banned` = 1 WHERE `name` = %s;"
    #     return self._update(COMMAND_, (username,))
    #
    # def update_ban_message_by_id(self, user_id, user_ban_message):
    #     COMMAND_ = "UPDATE `users` SET `banned_message` = %s WHERE `id` = %s;"
    #     return self._update(COMMAND_, (user_ban_message, user_id))
    #
    # def update_ban_message_by_username(self, username, user_ban_message):
    #     COMMAND_ = "UPDATE `users` SET `banned_message` = %s WHERE `name` = %s;"
    #     return self._update(COMMAND_, (user_ban_message, username))
    #
    # def get_all_banned_users(self):
    #     COMMAND_ = "SELECT * FROM `users` WHERE `banned` = 1;"
    #     return self._select(query=COMMAND_)
