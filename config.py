#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/YukkiChatBot >.
#
# This file is part of < https://github.com/TeamYukki/YukkiChatBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiChatBot/blob/master/LICENSE >
#
# All rights reserved.
#

from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID",2791256))
API_HASH = getenv("API_HASH","cd2fb4cdc795334aee3fbbc83da463ce")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","5006643023:AAFuiTBrxHQWRNAO6i-XKCe0mQ4zlg6RtDM")

# SUDO USERS
SUDO_USER = list(
    map(int, getenv("SUDO_USER", "1916694742").split())
)  # Input type must be interger

# You'll need a Private Group ID for this.
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID","-1001607198858"))

# Message to display when someone starts your bot
PRIVATE_START_MESSAGE = getenv(
    "PRIVATE_START_MESSAGE",
    "Hello! Welcome to my Personal Assistant Bot",
)

# Database to save your chats and stats... Get MongoDB:-  https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/mongodb#4.-youll-see-a-deploy-cloud-database-option.-please-select-shared-hosting-under-free-plan-here
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://erichdaniken:erichdaniken@cluster0.c13qk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
