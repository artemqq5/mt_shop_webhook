import asyncio
from asyncio import run
from datetime import datetime

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from flask_babel import gettext

from data.repository.invoices import InvoiceRepository
from data.repository.users import UserRepository
from locales.locales import translate
from private_cfg import BOT_TOKEN


class NotificationAdmin:

    @staticmethod
    async def invoice_completed(external_id, bot):
        counter = 0
        admins = UserRepository().admins()
        invoice = InvoiceRepository().invoice(external_id)
        user = UserRepository().user(invoice['user_id'])

        for admin in admins:
            try:
                locale = admin.get('lang', 'en')
                username = f"@{user['username']}" if user['username'] else translate(locale, "NOTIFICATION-USERNAME_HAVNT")

                # Отримуємо шаблон повідомлення з gettext
                message_template = translate(locale, "NOTIFICATION-INVOICE_COMPLETED")

                # Підставляємо динамічні значення в шаблон
                message = message_template.format(
                    balance=user['balance'],
                    value=invoice['value'],
                    number=invoice['number'],
                    id=invoice['external_id'],
                    date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    user_id=user['user_id'],
                    username=username
                )

                await bot.send_message(
                    chat_id=admin['user_id'],
                    text=message
                )
                counter += 1
            except Exception as e:
                print(f"invoice_completed error: {e}")

        print(f"messaging invoice_completed {counter}/{len(admins)}")

    @staticmethod
    async def invoice_declined(external_id, bot):
        counter = 0
        admins = UserRepository().admins()
        invoice = InvoiceRepository().invoice(external_id)
        user = UserRepository().user(invoice['user_id'])

        for admin in admins:
            try:
                locale = admin.get('lang', 'en')
                username = f"@{user['username']}" if user['username'] else translate(locale,
                                                                                     "NOTIFICATION-USERNAME_HAVNT")

                # Отримуємо шаблон повідомлення з gettext
                message_template = translate(locale, "NOTIFICATION-INVOICE_DECLINED")

                # Підставляємо динамічні значення в шаблон
                message = message_template.format(
                    balance=user['balance'],
                    value=invoice['value'],
                    number=invoice['number'],
                    id=invoice['external_id'],
                    date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    user_id=user['user_id'],
                    username=username
                )

                await bot.send_message(
                    chat_id=admin['user_id'],
                    text=message
                )
                counter += 1
            except Exception as e:
                print(f"invoice_declined error: {e}")

        print(f"messaging invoice_declined {counter}/{len(admins)}")

