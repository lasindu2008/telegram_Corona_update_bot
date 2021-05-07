import os


class Config(object):
    BOTT = os.environ.get("BOTT", "")

    APP_ID = int(os.environ.get("APP_ID", 12345))

    API_HASH = os.environ.get("API_HASH", "")
