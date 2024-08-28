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
        "USERNAME_HAVNT": "⚠️ Відстутній юзернейм",
        "NOTIFICATION": {
            "TRANSACTION_COMPLETED": "<b>🎉 Користувач успішно поповнив баланс! 💸</b>"
                                     "\n\n💰 Користувач має баланс: <b>{balance}$</b>"
                                     "\n💵 Поповнив на суму: <b>{value}$</b>"
                                     "\n\n🔢 Номер транзакції: <code>{number}</code>"
                                     "\n🆔 ID транзакції: <code>{id}</code>"
                                     "\n\n📅 Дата: <b>{date}</b>"
                                     "\n\n👤 <b>Користувач:</b>"
                                     "\n🆔 Телеграм ID: <code>{user_id}</code>"
                                     "\n🔗 Юзернейм: {username}",
            "TRANSACTION_PART_COMPLETED": "<b>Користувач поповнив ЧАСТИНУ балансу! 💸</b>"
                                          "\n💵 Поповнив на суму: <b>{value1}$</b> з <b>{expected_amount}$</b>"
                                          "\n💵 Залишилося поповнити до зарахування: <b>{value2}$</b>"
                                          "\n\n🔢 Номер транзакції: <code>{number}</code>"
                                          "\n🆔 ID транзакції: <code>{id}</code>"
                                          "\n\n📅 Дата: <b>{date}</b>"
                                          "\n\n👤 <b>Користувач:</b>"
                                          "\n🆔 Телеграм ID: <code>{user_id}</code>"
                                          "\n🔗 Юзернейм: {username}",
            "TRANSACTION_DECLINED": "<b>Користувач відмінив інвойс! ❌</b>"
                                    "\n\n💰 Користувач має баланс: <b>{balance}$</b>"
                                    "\n\n💵 Сума зарахування: <b>{value}$</b>"
                                    "\n\n🔢 Номер транзакції: <code>{number}</code>"
                                    "\n🆔 ID транзакції: <code>{id}</code>"
                                    "\n\n📅 Дата: <b>{date}</b>"
                                    "\n\n👤 <b>Користувач:</b>"
                                    "\n🆔 Телеграм ID: <code>{user_id}</code>"
                                    "\n🔗 Юзернейм: {username}",
            "TRANSACTION_COMPLETED_USER": "<b>Ваш баланс успішно поповнено! ✅💰</b>"
                                          "\n\n💵 Сума зарахування: <b>{value}$</b>"
                                          "\n💸 Баланс: <b>{balance}$</b>"
                                          "\n\n📅 Дата: <b>{date}</b>"
                                          "\n\n🔢 Номер транзакції: <code>{number}</code>"
                                          "\n🆔 ID транзакції: <code>{id}</code>",
            "TRANSACTION_PART_COMPLETED_USER": "<b>Ваша транзакція частково завершина</b>"
                                               "\n\n💵 Сума транзакції: <b>{value1}$</b> з <b>{expected_amount}$</b>"
                                               "\n💸 Залишилось до успішного зарахування: <b>{value2}$</b>"
                                               "\n\n📅 Дата: <b>{date}</b>"
                                               "\n\n🔢 Номер транзакції: <code>{number}</code>"
                                               "\n🆔 ID транзакції: <code>{id}</code>",
            "TRANSACTION_DECLINED_USER": "<b>Ваш платіж просрочено, час вийшов ❌</b>"
                                         "\n\n💵 Сума зарахування: <b>{value}$</b>"
                                         "\n💸 Баланс: <b>{balance}$</b>"
                                         "\n\n📅 Дата: <b>{date}</b>"
                                         "\n\n🔢 Номер транзакції: <code>{number}</code>"
                                         "\n🆔 ID транзакції: <code>{id}</code>",
        },
    },
    "en": {
        "USERNAME_HAVNT": "⚠️ Username is missing",
        "NOTIFICATION": {
            "TRANSACTION_COMPLETED": "<b>🎉 User successfully topped up the balance! 💸</b>"
                                     "\n\n💰 User's balance: <b>{balance}$</b>"
                                     "\n💵 Topped up by: <b>{value}$</b>"
                                     "\n\n🔢 Transaction number: <code>{number}</code>"
                                     "\n🆔 Transaction ID: <code>{id}</code>"
                                     "\n\n📅 Date: <b>{date}</b>"
                                     "\n\n👤 <b>User:</b>"
                                     "\n🆔 Telegram ID: <code>{user_id}</code>"
                                     "\n🔗 Username: {username}",
            "TRANSACTION_PART_COMPLETED": "<b>The user has partially topped up their balance! 💸</b>"
                                          "\n💵 Topped up by: <b>{value1}$</b> out of <b>{expected_amount}$</b>"
                                          "\n💵 Remaining to top up for credit: <b>{value2}$</b>"
                                          "\n\n🔢 Transaction number: <code>{number}</code>"
                                          "\n🆔 Transaction ID: <code>{id}</code>"
                                          "\n\n📅 Date: <b>{date}</b>"
                                          "\n\n👤 <b>User:</b>"
                                          "\n🆔 Telegram ID: <code>{user_id}</code>"
                                          "\n🔗 Username: {username}",

            "TRANSACTION_COMPLETED_USER": "<b>Your balance has been successfully topped up! ✅💰</b>"
                                          "\n\n💵 Amount credited: <b>{value}$</b>"
                                          "\n💸 Balance: <b>{balance}$</b>"
                                          "\n\n📅 Date: <b>{date}</b>"
                                          "\n\n🔢 Transaction number: <code>{number}</code>"
                                          "\n🆔 Transaction ID: <code>{id}</code>",
            "TRANSACTION_DECLINED": "<b>The user canceled the invoice! ❌</b>"
                                    "\n\n💰 User's balance: <b>{balance}$</b>"
                                    "\n\n🔢 Transaction number: <code>{number}</code>"
                                    "\n🆔 Transaction ID: <code>{id}</code>"
                                    "\n\n📅 Date: <b>{date}</b>"
                                    "\n\n👤 <b>User:</b>"
                                    "\n🆔 Telegram ID: <code>{user_id}</code>"
                                    "\n🔗 Username: {username}",
            "TRANSACTION_PART_COMPLETED_USER": "<b>Your transaction is partially completed</b>"
                                               "\n\n💵 Transaction amount: <b>{value1}$</b> out of <b>{expected_amount}$</b>"
                                               "\n💸 Remaining for successful credit: <b>{value2}$</b>"
                                               "\n\n📅 Date: <b>{date}</b>"
                                               "\n\n🔢 Transaction number: <code>{number}</code>"
                                               "\n🆔 Transaction ID: <code>{id}</code>",
            "TRANSACTION_DECLINED_USER": "<b>Your payment is overdue, time has run out ❌</b>"
                                         "\n\n💵 Replenishment amount: <b>{value}$</b>"
                                         "\n💸 Balance: <b>{balance}$</b>"
                                         "\n\n📅 Date: <b>{date}</b>"
                                         "\n\n🔢 Transaction number: <code>{number}</code>"
                                         "\n🆔 Transaction ID: <code>{id}</code>",

        },
    },
    "ru": {
        "USERNAME_HAVNT": "⚠️ Имя пользователя отсутствует",
        "NOTIFICATION": {
            "TRANSACTION_COMPLETED": "<b>🎉 Пользователь успешно пополнил баланс! 💸</b>"
                                     "\n\n💰 Баланс пользователя: <b>{balance}$</b>"
                                     "\n💵 Пополнил на сумму: <b>{value}$</b>"
                                     "\n\n🔢 Номер транзакции: <code>{number}</code>"
                                     "\n🆔 ID транзакции: <code>{id}</code>"
                                     "\n\n📅 Дата: <b>{date}</b>"
                                     "\n\n👤 <b>Пользователь:</b>"
                                     "\n🆔 Телеграм ID: <code>{user_id}</code>"
                                     "\n🔗 Имя пользователя: {username}",
            "TRANSACTION_PART_COMPLETED": "<b>Пользователь частично пополнил баланс! 💸</b>"
                                          "\n💵 Пополнил на сумму: <b>{value1}$</b> из <b>{expected_amount}$</b>"
                                          "\n💵 Осталось пополнить до зачисления: <b>{value2}$</b>"
                                          "\n\n🔢 Номер транзакции: <code>{number}</code>"
                                          "\n🆔 ID транзакции: <code>{id}</code>"
                                          "\n\n📅 Дата: <b>{date}</b>"
                                          "\n\n👤 <b>Пользователь:</b>"
                                          "\n🆔 Telegram ID: <code>{user_id}</code>"
                                          "\n🔗 Имя пользователя: {username}",
            "TRANSACTION_COMPLETED_USER": "<b>Ваш баланс успешно пополнен! ✅💰</b>"
                                          "\n\n💵 Сумма зачисления: <b>{value}$</b>"
                                          "\n💸 Баланс: <b>{balance}$</b>"
                                          "\n\n📅 Дата: <b>{date}</b>"
                                          "\n\n🔢 Номер транзакции: <code>{number}</code>"
                                          "\n🆔 ID транзакции: <code>{id}</code>",
            "TRANSACTION_DECLINED": "<b>Пользователь отменил инвойс! ❌</b>"
                                    "\n\n💰 Баланс пользователя: <b>{balance}$</b>"
                                    "\n\n💵 Сумма зачисления: <b>{value}$</b>"
                                    "\n\n🔢 Номер транзакции: <code>{number}</code>"
                                    "\n🆔 ID транзакции: <code>{id}</code>"
                                    "\n\n📅 Дата: <b>{date}</b>"
                                    "\n\n👤 <b>Пользователь:</b>"
                                    "\n🆔 Telegram ID: <code>{user_id}</code>"
                                    "\n🔗 Имя пользователя: {username}",
            "TRANSACTION_PART_COMPLETED_USER": "<b>Ваша транзакция частично завершена</b>"
                                               "\n\n💵 Сумма транзакции: <b>{value1}$</b> из <b>{expected_amount}$</b>"
                                               "\n💸 Осталось до успешного зачисления: <b>{value2}$</b>"
                                               "\n\n📅 Дата: <b>{date}</b>"
                                               "\n\n🔢 Номер транзакции: <code>{number}</code>"
                                               "\n🆔 ID транзакции: <code>{id}</code>",
            "TRANSACTION_DECLINED_USER": "<b>Ваш платеж просрочен, время вышло ❌</b>"
                                         "\n\n💵 Сумма зачисления: <b>{value}$</b>"
                                         "\n💸 Баланс: <b>{balance}$</b>"
                                         "\n\n📅 Дата: <b>{date}</b>"
                                         "\n\n🔢 Номер транзакции: <code>{number}</code>"
                                         "\n🆔 ID транзакции: <code>{id}</code>",

        },
    }
}
