# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "0"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-100"))
	SHORTLINK_URL = os.environ.get('SHORTLINK_URL')
	SHORTLINK_API = os.environ.get('SHORTLINK_API')
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1445283714"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))

	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File.I can Work In Channel too Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸🤖 **My Name:** [FileStores Bot](https://t.me/{BOT_USERNAME})
│
├🔸📝 **Language:** [Python 3](https://www.python.org) 
│
├🔹📚 **Library:** [Pyrogram](https://docs.pyrogram.org)
│
├🔹📡 **Hosted On:** [heroku](https://heroku.com)
│
├🔸👨‍💻 **Developer:** [ツAʙʜɪsʜᴇᴋ Kᴜᴍᴀʀ](https://t.me/PredatorHackerzZ) 
│
├🔹👥 **Dramas Support:** [KDramas Request](https://t.me/kdrama_requests)
│
├🔸🔔 **Dramas Files:** [KDramasFlix File](https://t.me/KDramasFlix)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
Hi there, I'm Abhishek Kumar, a student and a Learner. I love to play with TG and I'm always trying to learn more. I created this bot to help people store their files securely and easily. If you have any questions or suggestions, feel free to contact me!

You can reach me on: @TeleRoid14

🧑🏻‍💻 GitHub: https://github.com/PredatorHackerzZ

My UPI & Link is On @DonateXRobot

	Want to Buy Bots : @OwnYourBotz 
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Private **FileStore Bot**.

You can get any KDramas Files of any language available on Telegram.

For More Requests Here : @kdrama_requests

❌ **PORNOGRAPHY CONTENTS** are strictly prohibited & get Permanent Ban.
"""
