import asyncio
from asyncio import run
from datetime import datetime

from aiogram import Bot

from data.repository.transactions import TransactionRepository
from data.repository.users import UserRepository
from locales.locales import translate
from private_cfg import BOT_TOKEN


class NotificationClient:

    @staticmethod
    async def transaction_completed(external_id, value, bot):
        transaction = TransactionRepository().transaction(external_id)
        user = UserRepository().user(transaction['user_id'])

        try:
            locale = user.get('lang', 'en')

            # Отримуємо шаблон повідомлення
            message_template = translate(locale, "NOTIFICATION-TRANSACTION_COMPLETED_USER")

            # Підставляємо динамічні значення в шаблон
            message = message_template.format(
                value=value,
                balance=user['balance'],
                date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                number=transaction['number'],
                id=transaction['external_id'],
            )

            await bot.send_message(
                chat_id=user['user_id'],
                text=message
            )
        except Exception as e:
            print(f"transaction_completed user error: {e}")

        print(f"messaging transaction_completed good")

    # @staticmethod
    # async def transaction_part_completed(external_id, value, bot):
    #     transaction = TransactionRepository().transaction(external_id)
    #     user = UserRepository().user(transaction['user_id'])
    #
    #     try:
    #         locale = user.get('lang', 'en')
    #
    #         # Отримуємо шаблон повідомлення
    #         message_template = translate(locale, "NOTIFICATION-TRANSACTION_PART_COMPLETED_USER")
    #
    #         # Підставляємо динамічні значення в шаблон
    #         message = message_template.format(
    #             value1=value,
    #             expected_amount=transaction['expected_amount'],
    #             value2=transaction['expected_amount'] - value,
    #             date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #             number=transaction['number'],
    #             id=transaction['external_id'],
    #         )
    #
    #         await bot.send_message(
    #             chat_id=user['user_id'],
    #             text=message
    #         )
    #     except Exception as e:
    #         print(f"transaction_completed user error: {e}")
    #
    #     print(f"messaging transaction_completed good")

    @staticmethod
    async def transaction_declined(external_id, bot):
        transaction = TransactionRepository().transaction(external_id)
        user = UserRepository().user(transaction['user_id'])

        try:
            locale = user.get('lang', 'en')

            # Отримуємо шаблон повідомлення
            message_template = translate(locale, "NOTIFICATION-TRANSACTION_DECLINED_USER")

            # Підставляємо динамічні значення в шаблон
            message = message_template.format(
                value=transaction['expected_amount'],
                balance=user['balance'],
                date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                number=transaction['number'],
                id=transaction['external_id'],
            )

            await bot.send_message(
                chat_id=user['user_id'],
                text=message
            )
        except Exception as e:
            print(f"transaction_declined user error: {e}")

        print(f"messaging transaction_declined good")

