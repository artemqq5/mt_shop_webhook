from config.private_cfg import *

is_debug = True

if is_debug:
    BOT_TOKEN = BOT_TOKEN_TEST
    DB_PASSWORD = DB_PASSWORD_TEST
    PAYMENT_TOKEN = PAYMENT_TOKEN_TEST
    TRELLO_KEY = TRELLO_KEY_TEST
    TRELLO_TOKEN = TRELLO_TOKEN_TEST
    TRELLO_SECRET = TRELLO_SECRET_TEST
    TRELLO_LIST_CREO_NEW = TRELLO_LIST_CREO_NEW_TEST
    TRELLO_LIST_CREO_DONE = TRELLO_LIST_CREO_DONE_TEST
    TRELLO_BOARD = TRELLO_BOARD_TEST
    TRELLO_STATUS_FIELD = TRELLO_STATUS_FIELD_TEST
    COMPLETED_STATUS_TRELLO = COMPLETED_STATUS_TRELLO_TEST
    ACTIVE_STATUS_TRELLO = ACTIVE_STATUS_TRELLO_TEST
else:
    BOT_TOKEN = BOT_TOKEN_PROD
    DB_PASSWORD = DB_PASSWORD_PROD
    PAYMENT_TOKEN = PAYMENT_TOKEN_PROD
    TRELLO_KEY = TRELLO_KEY_PROD
    TRELLO_TOKEN = TRELLO_TOKEN_PROD
    TRELLO_SECRET = TRELLO_SECRET_PROD
    TRELLO_LIST_CREO_NEW = TRELLO_LIST_CREO_NEW_PROD
    TRELLO_LIST_CREO_DONE = TRELLO_LIST_CREO_DONE_PROD
    TRELLO_BOARD = TRELLO_BOARD_PROD
    TRELLO_STATUS_FIELD = TRELLO_STATUS_FIELD_PROD
    COMPLETED_STATUS_TRELLO = COMPLETED_STATUS_TRELLO_PROD
    ACTIVE_STATUS_TRELLO = ACTIVE_STATUS_TRELLO_PROD

