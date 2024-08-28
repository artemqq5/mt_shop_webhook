import asyncio
from asyncio import run
from datetime import datetime

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from flask_babel import gettext

from data.repository.transactions import TransactionRepository
from data.repository.users import UserRepository
from locales.locales import translate
from private_cfg import BOT_TOKEN


class NotificationAdmin:

    @staticmethod
    async def transaction_completed(external_id, value, bot):
        counter = 0
        admins = UserRepository().admins()
        transaction = TransactionRepository().transaction(external_id)
        user = UserRepository().user(transaction['user_id'])

        for admin in admins:
            try:
                locale = admin.get('lang', 'en')
                username = f"@{user['username']}" if user['username'] else translate(locale, "NOTIFICATION-USERNAME_HAVNT")

                message_template = translate(locale, "NOTIFICATION-TRANSACTION_COMPLETED")

                # Підставляємо динамічні значення в шаблон
                message = message_template.format(
                    balance=user['balance'],
                    value=value,
                    number=transaction['number'],
                    id=transaction['external_id'],
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
                print(f"transaction_completed error: {e}")

        print(f"messaging transaction_completed {counter}/{len(admins)}")

    # @staticmethod
    # async def transaction_part_completed(external_id, value, bot):
    #     counter = 0
    #     admins = UserRepository().admins()
    #     transaction = TransactionRepository().transaction(external_id)
    #     user = UserRepository().user(transaction['user_id'])
    #
    #     for admin in admins:
    #         try:
    #             locale = admin.get('lang', 'en')
    #             username = f"@{user['username']}" if user['username'] else translate(locale,
    #                                                                                  "NOTIFICATION-USERNAME_HAVNT")
    #
    #             message_template = translate(locale, "NOTIFICATION-TRANSACTION_PART_COMPLETED")
    #
    #             # Підставляємо динамічні значення в шаблон
    #             message = message_template.format(
    #                 value1=value,
    #                 expected_amount=transaction['expected_amount'],
    #                 value2=transaction['expected_amount'] - value,
    #                 number=transaction['number'],
    #                 id=transaction['external_id'],
    #                 date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #                 user_id=user['user_id'],
    #                 username=username
    #             )
    #
    #             await bot.send_message(
    #                 chat_id=admin['user_id'],
    #                 text=message
    #             )
    #             counter += 1
    #         except Exception as e:
    #             print(f"transaction_part_completed error: {e}")
    #
    #     print(f"messaging transaction_part_completed {counter}/{len(admins)}")

    @staticmethod
    async def transaction_declined(external_id, bot):
        counter = 0
        admins = UserRepository().admins()
        transaction = TransactionRepository().transaction(external_id)
        user = UserRepository().user(transaction['user_id'])

        for admin in admins:
            try:
                locale = admin.get('lang', 'en')
                username = f"@{user['username']}" if user['username'] else translate(locale,
                                                                                     "NOTIFICATION-USERNAME_HAVNT")

                # Отримуємо шаблон повідомлення з gettext
                message_template = translate(locale, "NOTIFICATION-TRANSACTION_DECLINED")

                # Підставляємо динамічні значення в шаблон
                message = message_template.format(
                    balance=user['balance'],
                    value=transaction['expected_amount'],
                    number=transaction['number'],
                    id=transaction['external_id'],
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
                print(f"transaction_declined error: {e}")

        print(f"messaging transaction_declined {counter}/{len(admins)}")

