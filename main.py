import hashlib
import hmac
import json

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from flask import Flask, request
from gevent.pywsgi import WSGIServer

from data.repository.transactions import TransactionRepository
from data.repository.users import UserRepository
from data.status_transaction import TRANSACTION_COMPLETE, TRANSACTION_DECLINED, TRANSACTION_INIT
from domain.notification.NotificationAdmin import NotificationAdmin
from domain.notification.NotificationClient import NotificationClient
from private_cfg import WHITE_PAY_WEBHOOK_TOKEN, BOT_TOKEN

app = Flask(__name__)


@app.route("/masonspayment", methods=['POST'])
async def transaction_completed():
    print(request.json)
    print(request.headers)
    data = request.json

    if request.headers.get('Signature', None) is None:
        print("ERROR: hasn't Signature in request")
        return "Bad request", 400

    received_signature = request.headers.get('Signature')

    payload_json = json.dumps(data, separators=(',', ':'))
    new_string_like_php = payload_json.replace("/", "\/")
    signature = hmac.new(WHITE_PAY_WEBHOOK_TOKEN.encode('utf-8'), new_string_like_php.encode('utf-8'),
                         hashlib.sha256).hexdigest()

    # print(f"Received Signature: {received_signature}\n")
    # print(f"Generated Signature: {signature}\n")

    if hmac.compare_digest(received_signature, signature):
        print(str(data['event_type']).split("::")[1])
        if data['event_type'] in (TRANSACTION_COMPLETE, TRANSACTION_DECLINED):
            # check is transaction exist and simular value in transaction
            transaction = TransactionRepository().transaction(data['transaction']['order_id'])

            if not transaction:
                print("ERROR: Transaction not exist in database")
                return "Bad request", 400

            if transaction['status'] != TRANSACTION_INIT:
                print(f"ERROR: Transaction status already changed to {str(data['event_type']).split('::')[1]}")
                return "Bad request", 400

            default_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)
            bot = Bot(token=BOT_TOKEN, default=default_properties)

            if not float(data['transaction']['received_total']) >= transaction['expected_amount']:
                # await NotificationAdmin.transaction_part_completed(
                #     data['transaction']['order_id'],
                #     float(data['transaction']['received_total']),
                #     bot
                # )
                # await NotificationClient.transaction_part_completed(
                #     data['transaction']['order_id'],
                #     float(data['transaction']['received_total']),
                #     bot
                # )
                # await bot.session.close()
                print(f"VERIFIED: Transaction received_total less then expected_amount")
                return f"Verified Transaction received_total less then expected_amount ", 200

            # try update transaction status into database
            update_status = TransactionRepository().update_status(
                str(data['event_type']).split("::")[1],
                data['transaction']['order_id']
            )
            if not update_status:
                print("ERROR: Can't update transaction status into db")

            if data['event_type'] == TRANSACTION_DECLINED:
                # notify admins and user
                await NotificationAdmin.transaction_declined(data['transaction']['order_id'], bot)
                await NotificationClient.transaction_declined(data['transaction']['order_id'], bot)
                await bot.session.close()
                return 'Verified Declined transaction', 200

            # update_balance
            user = UserRepository().user(transaction['user_id'])
            TransactionRepository().update_value(
                float(data['transaction']['received_total']),
                data['transaction']['order_id']
            )
            update_balance = UserRepository().update_balance(
                transaction['user_id'],
                float(data['transaction']['received_total']) + user['balance']
            )
            if not update_balance:
                print("ERROR: Can't update user balance into db")

            # notify admins and user
            await NotificationAdmin.transaction_completed(data['transaction']['order_id'],
                                                          data['transaction']['received_total'], bot)
            await NotificationClient.transaction_completed(data['transaction']['order_id'],
                                                           data['transaction']['received_total'], bot)
            await bot.session.close()

        return 'Verified', 200
    else:
        print("ERROR: No compare_digest in signature")
        return "Bad request", 400  # Bad request


# {
#     'transaction': {
#         'id': 'b091f2f7-35b8-490b-8d37-169967a85840',
#         'order_id': 'b3f5acc0-eb81-4a7f-890e-68874637a53d',
#         'external_order_id': None,
#         'stock_orders': [],
#         'currency': 'USDT',
#         'value': '2.902',
#         'is_internal': False,
#         'type': 'DEPOSIT',
#         'status': 'COMPLETE',
#         'hash': '0x44bac9df15c31a2b4d9d666171c7577fdc5d53b363dc5a7beac9557ee1e16549',
#         'created_at': '2024-08-28 11:23:35',
#         'completed_at': '2024-08-28 11:27:26',
#         'fee_amount': '0.029020',
#         'fee_currency': 'USDT',
#         'received_total': '5.74596',
#         'received_currency': 'USDT',
#         'transaction_received_total': '2.872980'
#     },
#     'event_type': 'transaction::was_final_exchange'
# }

# if __name__ == '__main__':
#     payload1 = {
#         "transaction": {
#             "id": "600c8cad-5614-42a9-a0c6-19cee0e9e48c",
#             "order_id": "a65479ac-b5fe-4bb1-961c-09590a7e3cb1",
#             "external_order_id": "null",
#             "stock_orders": [
#                 {
#                     "id": "35428e8f-a4e0-4922-9e2a-7e3644a2bec7",
#                     "amount": "100",
#                     "result_amount": "38.46003825",
#                     "status": "CLOSED",
#                     "pair": "ADA_USDT",
#                     "currency_from_ticker": "ADA",
#                     "currency_to_ticker": "USDT",
#                     "date": "2024-08-01",
#                     "time": "08:20:26",
#                     "exchange_rate": "0.38460038",
#                     "created_at": "2024-08-01 08:20:26"
#                 }
#             ],
#             "currency": "ADA",
#             "value": "100",
#             "is_internal": "true",
#             "type": "DEPOSIT",
#             "status": "COMPLETE",
#             "hash": "internal_transaction_acd076d1-e166-4b9b-b4a1-dd83b591d0d9",
#             "created_at": "2024-08-01 08:20:24",
#             "completed_at": "2024-08-01 08:20:24",
#             "fee_amount": "0.384601",
#             "fee_currency": "USDT",
#             "external_currencies": [
#                 {
#                     "currency": "USD",
#                     "amount": "38.05"
#                 },
#                 {
#                     "currency": "EUR",
#                     "amount": "35.29"
#                 },
#                 {
#                     "currency": "NGN",
#                     "amount": "63210.77"
#                 }
#             ],
#             "received_total": "5",
#             "received_currency": "USDT",
#             "transaction_received_total": "5"
#         },
#         "event_type": "transaction::was_final_exchange"
#     }
#
#     # Серіалізація JSON payload і кодування ключа в байти
#     payload_json1 = json.dumps(payload1, separators=(',', ':'))  # Використовуйте ті ж сепаратори, що і в JavaScript
#     new_string_like_php1 = payload_json1.replace("/", "\/")
#     signature1 = hmac.new(WHITE_PAY_WEBHOOK_TOKEN.encode('utf-8'), new_string_like_php1.encode('utf-8'),
#                           hashlib.sha256).hexdigest()
#
#     print(signature1)
#     app.run(threaded=True)
#     http_server = WSGIServer(("0.0.0.0", 5000), app)
#     http_server.serve_forever()
