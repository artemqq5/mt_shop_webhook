import re
from wsgiref.simple_server import WSGIServer

from flask import Flask, request

from config.cfg import *
from data.constants.my_constants import *
from data.repository import MyRepository
from telegram_usecase.send_message_tg import TelegramManagerMessage

app = Flask(__name__)

CHANGE_STATUS_TASK = "action_update_custom_field_item"
MOVE_TASK = "action_move_card_from_list_to_list"


@app.route('/mt_shop_creo', methods=['POST', 'GET'])
def webhook_handler():
    if request.method == 'POST':
        try:
            data = request.get_json()

            name = data['model']['name']
            short_url = data['model']['url']
            translation_key = data['action']['display']['translationKey']

            desc = data['model']['desc']
            id_order_task = re.search(r'id_order:\s*([^\n]+)', desc).group(1)

            if translation_key == CHANGE_STATUS_TASK:
                id_value = data['action']['data']['customFieldItem']['idValue']

                if id_value == COMPLETED_STATUS_TRELLO:
                    status_task = TASK_DONE
                    MyRepository().update_order_status(TASK_DONE, id_order_task)
                elif id_value == ACTIVE_STATUS_TRELLO:
                    status_task = TASK_ACTIVE
                    MyRepository().update_order_status(TASK_ACTIVE, id_order_task)
                else:
                    status_task = id_value

                TelegramManagerMessage().send_message(
                    name=name, url=short_url, message=TASK_CHANGE_STATUS(status_task), id_order=id_order_task
                )

            else:
                print(translation_key)

        except Exception as e:
            print(e)
    else:
        print("GET")

    return "OK", 200


if __name__ == '__main__':
    http_server = WSGIServer(("0.0.0.0", 5010), app)
    http_server.serve_forever()
