import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# Create bot instance
bot = Client(
    "Donate",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"]
)

# Define home page with three buttons
@bot.on_message(filters.command("start"))
def start(bot, update):
    chat_id = update.chat.id
    first_name = update.chat.first_name

    markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("⚡️AK Imax 2.0⚡️", url="t.me/akimax0"),
            InlineKeyboardButton("⚡️AK IMAX MOVIES⚡️", url="t.me/Akimaxmovies01")
        ],
        [InlineKeyboardButton("Premium", callback_data="premium")],
        [InlineKeyboardButton("Donate 💳", callback_data="donate")]
    ])

    photo_url = "https://te.legra.ph/file/6750eaff7ac29676dbb31.jpg"
    caption = f"Welcome {first_name}! Choose an option below:"
    bot.send_photo(
        chat_id=chat_id,
        photo=photo_url,
        caption=caption,
        reply_markup=markup
    )

# Premium page
@bot.on_callback_query(filters.regex("premium"))
def premium(bot, update):
    chat_id = update.message.chat.id

    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("Join premium group", url="https://t.me/AKImaxPremium1")]
    ])

    photo_url = "https://te.legra.ph/file/a92e3ce02ed084795a865.jpg"
    caption = "Unlock premium features now!"
    bot.send_photo(
        chat_id=chat_id,
        photo=photo_url,
        caption=caption,
        reply_markup=markup
    )



# Donation page
@bot.on_callback_query(filters.regex("donate"))
def donate(bot, update):
    chat_id = update.message.chat.id

    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("Paytm", url="https://paytm.me/your_paytm_link")],
        [InlineKeyboardButton("UPI", callback_data="UPI")]
    ])

    photo_url = "https://te.legra.ph/file/df563479fb5ea116bb55b.jpg"
    caption =(
              f"🌟 To keep AK-IMAX alive, we need your help through monthly donations.\n"
              f"This is necessary to cover the costs of admin and bot hosting servers to provide 24/7 service.\n" 
              f"We have always strived to offer our services for free, but now we need your support to maintain it.\n\n" \

              f"💰 The minimum donation amount is Rs. 3/-, and we appreciate any contribution you can make to keep AK-IMAX running.\n"
              f"If you want to donate, please join our Screenshot Group (https://t.me/AKImaxPremium1) and send us a message.\n\n" \

              f"🙏🏻 Thank you for considering joining the AK-IMAX family and supporting our cause."
    )
                
    bot.send_photo(
        chat_id=chat_id,
        photo=photo_url,
        caption=caption,
        reply_markup=markup
    )

@bot.on_callback_query(filters.regex("UPI"))
def upi_buttons(update, context):
    chat_id = update.effective_chat.id
    message_id = update.message.message_id

    # create a reply markup with inline keyboard
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("Google Pay", url="https://gpay.app/...")],
        [InlineKeyboardButton("Paytm", url="https://paytm.com/...")]
    ])

    try:
        # send the photo with the reply markup
        bot.send_photo(chat_id=chat_id, photo=upi_photo_url, reply_markup=reply_markup)
    except pyrogram.errors.exceptions.bad_request_400.ButtonUrlInvalid as e:
        # log the error and the value of the button URL
        logger.error(f"Button URL is invalid: {e}")
        logger.debug(f"Button URL value: {reply_markup.inline_keyboard[0][0].url}")
    
    # acknowledge the update
    context.bot.delete_message(chat_id=chat_id, message_id=message_id)

    # send photo and message with the same reply markup
    bot.send_photo(
        chat_id=chat_id,
        photo="https://te.legra.ph/file/69d562d0f34f8b92cf904.jpg",
        reply_markup=reply_markup
    )
    
    bot.send_message(
        chat_id=chat_id,
        text="Choose the UPI ID to donate:",
        reply_markup=reply_markup
    )

# Broadcast feature for owner
owner_id = "5143506371"

@bot.on_message(filters.command("broadcast") & filters.user(owner_id))
def broadcast(bot, update):
    message = update.text.split("/broadcast ", maxsplit=1)[1]
    all_chats = bot.get_dialogs()
    for chat in all_chats:
        try:
            bot.send_message(chat.id, message)
        except:
            pass

    bot.send_message(
        chat_id=update.chat.id,
        text=f"Broadcast message sent to {len(all_chats)} chats"
    )

# Start the bot
bot.run()

