import requests

from config.cfg import BOT_TOKEN
from data.constants.my_constants import ADMIN, SUB_POSITION_CREO
from data.repository import MyRepository


class TelegramManagerMessage(MyRepository):
    url_send_message = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    def send_message(self, name, url, message, id_order):

        # print(id_order)

        for user in self.get_users_by_position(ADMIN):
            try:
                if user['sub_position'] == SUB_POSITION_CREO or user['sub_position'] is None:
                    json_data_pass = {"chat_id": user['id'], "text": f"{name}\n\n{message}\n\n{url}"}
                    result = requests.request(method='POST', url=self.url_send_message, data=json_data_pass)
                    # print(result.json())
            except Exception as e:
                print(f"send_message {e}")

