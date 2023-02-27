import os

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = os.getenv("OWNER_ID")
GROUP_LINK = os.getenv("GROUP_LINK")
CHANNEL_LINK = os.getenv("CHANNEL_LINK")
PREMIUM_GROUP_LINK = os.getenv("PREMIUM_GROUP_LINK")
DONATION_PAYTM_LINK = os.getenv("DONATION_PAYTM_LINK")
DONATION_UPI_ID = os.getenv("DONATION_UPI_ID")

#You can define environment variables for each of these values and import them in your main script like this:

from settings import API_ID, API_HASH, BOT_TOKEN, OWNER_ID, GROUP_LINK, CHANNEL_LINK, PREMIUM_GROUP_LINK, DONATION_PAYTM_LINK, DONATION_UPI_ID

# Create bot instance
bot = Client(
    "Donate",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

#This way you can keep all sensitive information like API credentials, bot token, etc. in a separate file and not expose them in your main script.



