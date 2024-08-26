import hashlib
import hmac
import json

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from flask import Flask, request
from gevent.pywsgi import WSGIServer

from data.repository.invoices import InvoiceRepository
from data.repository.users import UserRepository
from domain.notification.NotificationAdmin import NotificationAdmin
from domain.notification.NotificationClient import NotificationClient
from private_cfg import WHITE_PAY_WEBHOOK_TOKEN, BOT_TOKEN

app = Flask(__name__)


@app.route("/masonspayment", methods=['POST'])
async def invoice_completed():
    # print(request.json)
    print(request.json)
    data = request.json

    if request.headers.get('X-Signature', None) is None:
        print("ERROR: hasn't X-Signature in request")
        return "Bad request", 400

    received_signature = request.headers.get('X-Signature')

    # Серіалізація JSON payload і кодування ключа в байти
    payload_json = json.dumps(data, separators=(',', ':'))  # Використовуйте ті ж сепаратори, що і в JavaScript
    signature = hmac.new(WHITE_PAY_WEBHOOK_TOKEN.encode('utf-8'), payload_json.encode('utf-8'),
                         hashlib.sha256).hexdigest()

    # print(f"Received Signature: {received_signature}\n")
    # print(f"Generated Signature: {signature}\n")

    if hmac.compare_digest(received_signature, signature):

        if data['order']['status'] == "COMPLETE":

            # check is invoice exist and simular value in invoice
            invoice = InvoiceRepository().invoice(data['order']['id'])
            # print(invoice)
            if not invoice:
                print("ERROR: Invoice not exist in database")
                return "Bad request", 400
            if not float(data['order']['value']) == invoice['value']:
                print("ERROR: Value Invoice no the same")
                return "Bad request", 400
            if not invoice['status'] != "INIT":
                print("ERROR: Invoice status already changed from INIT")
                return "Bad request", 400

            default_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)
            bot = Bot(token=BOT_TOKEN, default=default_properties)
            # notify admins and user
            await NotificationAdmin.invoice_completed(data['order']['id'], bot)
            await NotificationClient.invoice_completed(data['order']['id'], bot)
            await bot.session.close()

            # try update invoice status into database
            update_status = InvoiceRepository().update(data['order']['status'], data['order']['id'])
            if not update_status:
                print("ERROR: Can't update status into db")
                return "Bad request", 400

            # update_balance
            user = UserRepository().user(invoice['user_id'])
            update_balance = UserRepository().update_balance(invoice['user_id'], invoice['value'] + user['balance'])
            if not update_balance:
                print("ERROR: Can't update user balance into db")
                return "Bad request", 400

        return 'Verified', 200
    else:
        print("ERROR: No compare_digest in signature")
        return "Bad request", 400  # Bad request

#   {
#     "order": {
#     "id": "08d585b1-86c6-496d-b493-ab17a574fdd6",
#     "currency": "UAH",
#     "value": "200",
#     "expected_amount": "200",
#     "status": "DECLINED",
#     "external_order_id": "423se231-f351-234g-g324-g35gd3452f45",
#     "created_at": "2022-03-22 14:01:34",
#     "completed_at": null,
#     "acquiring_url": "https://merchant.pay.whitepay.com/fiat-order/08d585b1-86c6-496d-b493-ab17a574fdd6",
#     "is_internal": false
#   },
#   "event_type": "order::declined"
# }


if __name__ == '__main__':
    payload1 = {
        "order": {
        "id": "1f336422-8b84-442d-a085-1b06d6316c3f",
        "currency": "USDT",
        "value": "5",
        "expected_amount": "5",
        "status": "COMPLETED",
        "external_order_id": "423se231-f351-234g-g324-g35gd3452f45",
        "created_at": "2022-03-22 14:01:34",
        "completed_at": "null",
        "acquiring_url": "https://merchant.pay.whitepay.com/fiat-order/08d585b1-86c6-496d-b493-ab17a574fdd6",
        "is_internal": "false"
      },
      "event_type": "order::completed"
    }


    # Серіалізація JSON payload і кодування ключа в байти
    payload_json1 = json.dumps(payload1, separators=(',', ':'))  # Використовуйте ті ж сепаратори, що і в JavaScript
    signature1 = hmac.new(WHITE_PAY_WEBHOOK_TOKEN.encode('utf-8'), payload_json1.encode('utf-8'),
                          hashlib.sha256).hexdigest()

    print(signature1)
    app.run(threaded=True)
    http_server = WSGIServer(("0.0.0.0", 5100), app)
    http_server.serve_forever()
