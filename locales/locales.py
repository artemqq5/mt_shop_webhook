def translate(lang, key):
    if lang not in translate_dict.keys():
        lang = "en"

    keys = key.split("-")
    result = translate_dict.get(lang, {})
    for k in keys:
        result = result.get(k)
        if result is None:
            return None

    return result


def format_message(template, **kwargs):
    return template.format(**kwargs)


translate_dict = {
    "uk": {
        "NOTIFICATION": {
            "INVOICE_COMPLETED": "<b>🎉 Користувач успішно поповнив баланс! 💸</b>"
                                 "\n\n💰 Користувач має баланс: <b>{balance}$</b>"
                                 "\n💵 Поповнив на суму: <b>{value}$</b>"
                                 "\n\n🔢 Номер транзакції: <code>{number}</code>"
                                 "\n🆔 ID транзакції: <code>{id}</code>"
                                 "\n\n📅 Дата: <b>{date}</b>"
                                 "\n\n👤 <b>Користувач:</b>"
                                 "\n🆔 Телеграм ID: <code>{user_id}</code>"
                                 "\n🔗 Юзернейм: {username}",
            "USERNAME_HAVNT": "⚠️ Відстутній юзернейм",
            "BALANCE_UPDATED_USER": "<b>Ваш баланс успішно поповнено! ✅💰</b>"
                                    "\n\n💵 Сума зарахування: <b>{value}$</b>"
                                    "\n💸 Баланс: <b>{balance}$</b>"
                                    "\n\n📅 Дата: <b>{date}</b>"
                                    "\n\n🔢 Номер транзакції: <code>{number}</code>"
                                    "\n🆔 ID транзакції: <code>{id}</code>",
            "INVOICE_DECLINED": "<b>Користувач відмінив інвойс! ❌</b>"
                                "\n\n💰 Користувач має баланс: <b>{balance}$</b>"
                                "\n\n💵 Сума зарахування: <b>{value}$</b>"
                                "\n\n🔢 Номер транзакції: <code>{number}</code>"
                                "\n🆔 ID транзакції: <code>{id}</code>"
                                "\n\n📅 Дата: <b>{date}</b>"
                                "\n\n👤 <b>Користувач:</b>"
                                "\n🆔 Телеграм ID: <code>{user_id}</code>"
                                "\n🔗 Юзернейм: {username}",
            "INVOICE_DECLINED_USER": "<b>Ваш платіж просрочено, час вийшов ❌</b>"
                                     "\n\n💵 Сума зарахування: <b>{value}$</b>"
                                     "\n💸 Баланс: <b>{balance}$</b>"
                                     "\n\n📅 Дата: <b>{date}</b>"
                                     "\n\n🔢 Номер транзакції: <code>{number}</code>"
                                     "\n🆔 ID транзакції: <code>{id}</code>",
        },
    },
    "en": {
        "NOTIFICATION": {
            "INVOICE_COMPLETED": "<b>🎉 User successfully topped up the balance! 💸</b>"
                                 "\n\n💰 User's balance: <b>{balance}$</b>"
                                 "\n💵 Topped up by: <b>{value}$</b>"
                                 "\n\n🔢 Transaction number: <code>{number}</code>"
                                 "\n🆔 Transaction ID: <code>{id}</code>"
                                 "\n\n📅 Date: <b>{date}</b>"
                                 "\n\n👤 <b>User:</b>"
                                 "\n🆔 Telegram ID: <code>{user_id}</code>"
                                 "\n🔗 Username: {username}",
            "USERNAME_HAVNT": "⚠️ Username is missing",
            "BALANCE_UPDATED_USER": "<b>Your balance has been successfully topped up! ✅💰</b>"
                                    "\n\n💵 Amount credited: <b>{value}$</b>"
                                    "\n💸 Balance: <b>{balance}$</b>"
                                    "\n\n📅 Date: <b>{date}</b>"
                                    "\n\n🔢 Transaction number: <code>{number}</code>"
                                    "\n🆔 Transaction ID: <code>{id}</code>",
            "INVOICE_DECLINED": "<b>The user canceled the invoice! ❌</b>"
                                "\n\n💰 User's balance: <b>{balance}$</b>"
                                "\n\n🔢 Transaction number: <code>{number}</code>"
                                "\n🆔 Transaction ID: <code>{id}</code>"
                                "\n\n📅 Date: <b>{date}</b>"
                                "\n\n👤 <b>User:</b>"
                                "\n🆔 Telegram ID: <code>{user_id}</code>"
                                "\n🔗 Username: {username}",
            "INVOICE_DECLINED_USER": "<b>Your payment is overdue, time has run out ❌</b>"
                                     "\n\n💵 Replenishment amount: <b>{value}$</b>"
                                     "\n💸 Balance: <b>{balance}$</b>"
                                     "\n\n📅 Date: <b>{date}</b>"
                                     "\n\n🔢 Transaction number: <code>{number}</code>"
                                     "\n🆔 Transaction ID: <code>{id}</code>",

        },
    },
    "ru": {
        "NOTIFICATION": {
            "INVOICE_COMPLETED": "<b>🎉 Пользователь успешно пополнил баланс! 💸</b>"
                                 "\n\n💰 Баланс пользователя: <b>{balance}$</b>"
                                 "\n💵 Пополнил на сумму: <b>{value}$</b>"
                                 "\n\n🔢 Номер транзакции: <code>{number}</code>"
                                 "\n🆔 ID транзакции: <code>{id}</code>"
                                 "\n\n📅 Дата: <b>{date}</b>"
                                 "\n\n👤 <b>Пользователь:</b>"
                                 "\n🆔 Телеграм ID: <code>{user_id}</code>"
                                 "\n🔗 Имя пользователя: {username}",
            "USERNAME_HAVNT": "⚠️ Имя пользователя отсутствует",
            "BALANCE_UPDATED_USER": "<b>Ваш баланс успешно пополнен! ✅💰</b>"
                                    "\n\n💵 Сумма зачисления: <b>{value}$</b>"
                                    "\n💸 Баланс: <b>{balance}$</b>"
                                    "\n\n📅 Дата: <b>{date}</b>"
                                    "\n\n🔢 Номер транзакции: <code>{number}</code>"
                                    "\n🆔 ID транзакции: <code>{id}</code>",
            "INVOICE_DECLINED": "<b>Пользователь отменил инвойс! ❌</b>"
                                "\n\n💰 Баланс пользователя: <b>{balance}$</b>"
                                "\n\n💵 Сумма зачисления: <b>{value}$</b>"
                                "\n\n🔢 Номер транзакции: <code>{number}</code>"
                                "\n🆔 ID транзакции: <code>{id}</code>"
                                "\n\n📅 Дата: <b>{date}</b>"
                                "\n\n👤 <b>Пользователь:</b>"
                                "\n🆔 Telegram ID: <code>{user_id}</code>"
                                "\n🔗 Имя пользователя: {username}",
            "INVOICE_DECLINED_USER": "<b>Ваш платеж просрочен, время вышло ❌</b>"
                                     "\n\n💵 Сумма зачисления: <b>{value}$</b>"
                                     "\n💸 Баланс: <b>{balance}$</b>"
                                     "\n\n📅 Дата: <b>{date}</b>"
                                     "\n\n🔢 Номер транзакции: <code>{number}</code>"
                                     "\n🆔 ID транзакции: <code>{id}</code>",

        },
    }
}
