import asyncio
from asyncio import run
from datetime import datetime

from aiogram import Bot

from data.repository.invoices import InvoiceRepository
from data.repository.users import UserRepository
from locales.locales import translate
from private_cfg import BOT_TOKEN


class NotificationClient:

    @staticmethod
    async def invoice_completed(external_id, bot):
        invoice = InvoiceRepository().invoice(external_id)
        user = UserRepository().user(invoice['user_id'])

        try:
            locale = user.get('lang', 'en')

            # Отримуємо шаблон повідомлення
            message_template = translate(locale, "NOTIFICATION-BALANCE_UPDATED_USER")

            # Підставляємо динамічні значення в шаблон
            message = message_template.format(
                value=invoice['value'],
                balance=user['balance'],
                date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                number=invoice['number'],
                id=invoice['external_id'],
            )

            await bot.send_message(
                chat_id=user['user_id'],
                text=message
            )
        except Exception as e:
            print(f"invoice_completed user error: {e}")

        print(f"messaging invoice_completed good")

