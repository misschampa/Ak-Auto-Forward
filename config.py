from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "b642a25aee67b2aed02116df4a916bca")
      API_ID = int(getenv("API_ID", "29882686"))
      AS_COPY = True if getenv("AS_COPY", False) == "True" else False
      BOT_TOKEN = getenv("BOT_TOKEN", "")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "").replace("\n", " ").split(' '))