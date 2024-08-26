import asyncio
import hashlib
import hmac
import json

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from flask import Flask, request
from flask_babel import Babel
from flask_i18n import I18n
from gevent.pywsgi import WSGIServer

from data.repository.invoices import InvoiceRepository
from data.repository.users import UserRepository
from domain.notification.NotificationAdmin import NotificationAdmin
from domain.notification.NotificationClient import NotificationClient
from private_cfg import WHITE_PAY_WEBHOOK_TOKEN, BOT_TOKEN

app = Flask(__name__)


@app.route("/masonspayment", methods=['POST'])
async def transaction_completed():
    # print(request.json)
    print(request.json)
    data = request.json

    received_signature = request.headers.get('X-Signature')

    # Серіалізація JSON payload і кодування ключа в байти
    payload_json = json.dumps(data, separators=(',', ':'))  # Використовуйте ті ж сепаратори, що і в JavaScript
    signature = hmac.new(WHITE_PAY_WEBHOOK_TOKEN.encode('utf-8'), payload_json.encode('utf-8'),
                         hashlib.sha256).hexdigest()

    # print(f"Received Signature: {received_signature}\n")
    # print(f"Generated Signature: {signature}\n")

    if hmac.compare_digest(received_signature, signature):

        if data['transaction']['status'] == "COMPLETE":

            # check is invoice exist and simular value in invoice and transaction
            invoice = InvoiceRepository().invoice(data['transaction']['id'])
            # print(invoice)
            if not invoice or not float(data['transaction']['value']) == invoice['value'] or invoice['status'] == "COMPLETE":
                print("ERROR: Value transaction and Invoice no the same or status already completed")
                return "Bad request", 400

            default_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)
            bot = Bot(token=BOT_TOKEN, default=default_properties)
            # notify admins and user
            await NotificationAdmin.invoice_completed(data['transaction']['id'], bot)
            await NotificationClient.invoice_completed(data['transaction']['id'], bot)
            await bot.session.close()

            # try update invoice status into database
            update_status = InvoiceRepository().update(data['transaction']['status'], data['transaction']['id'])
            if not update_status:
                print("ERROR: Can't update status into db")
                return "Bad request", 400

            # update_balance
            user = UserRepository().user(invoice['user_id'])
            update_balance = UserRepository().update_balance(invoice['user_id'], invoice['value']+user['balance'])
            if not update_balance:
                print("ERROR: Can't update user balance into db")
                return "Bad request", 400

        return 'Verified', 200
    else:
        return "Bad request", 400  # Bad request


# { Withdrawal Complete/Declined
#   "transaction": {
#     "id": "4176141e-bd97-4f13-a71a-6547a230cf4a",
#     "order_id": "283585b1-16c6-496d-b493-ab17a574ffd6",
#     "external_order_id": "INV-123",
#     "stock_orders": [],
#     "currency": "USDT",
#     "value": "11",
#     "is_internal": false,
#     "status": "COMPLETE",
#     "hash": "null",
#     "created_at": "2022-03-22 10:09:34",
#     "completed_at": null
#   },
#   "event_type": "withdrawal::declined"
# }


# if __name__ == '__main__':
    # payload1 = {
    #     "transaction": {
    #         "id": "da472b36-00e2-43d8-84e8-c0eee3c30b7a",
    #         "order_id": "283585b1-16c6-496d-b493-ab17a574ffd6",
    #         "stock_orders": [],
    #         "external_order_id": "INV-123",
    #         "currency": "USDT",
    #         "value": "34.45",
    #         "status": "COMPLETE",
    #         "is_internal": "false",
    #         "hash": "null",
    #         "created_at": "2022-03-22 10:09:34",
    #         "completed_at": "null"
    #     },
    #     "event_type": "withdrawal::completed"
    # }
    #
    # # Серіалізація JSON payload і кодування ключа в байти
    # payload_json1 = json.dumps(payload1, separators=(',', ':'))  # Використовуйте ті ж сепаратори, що і в JavaScript
    # signature1 = hmac.new(WHITE_PAY_WEBHOOK_TOKEN.encode('utf-8'), payload_json1.encode('utf-8'),
    #                       hashlib.sha256).hexdigest()

    # print(signature1)
    # app.run(threaded=True)
    # http_server = WSGIServer(("0.0.0.0", 5100), app)
    # http_server.serve_forever()
