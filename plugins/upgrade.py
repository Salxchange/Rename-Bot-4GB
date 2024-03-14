from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GBGB
	Price 0
	
	**🪙 Basic** 
	Daily  Upload  limit 20GB
	
	
	**⚡ Standard**
	Daily Upload limit 50GB

	
	**💎 Pro**
	Daily Upload limit 100GB
	
	
	Pay Using Upi I'd `madflixofficial@axl`
	
	After Payment Send Screenshots Of 
        Payment To Admin @calladminrobot"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("",url = "https://t.me/calladminrobot")], 
        			[InlineKeyboardButton("",url = "https://telegra.ph/file/7f959437f9375b313ed1c.jpg"),
        			InlineKeyboardButton("",url = "https://telegra.ph/file/30b3e45a02766803883cb.jpg")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**🪙 Basic** 
	Daily  Upload  limit 20GB
 
	
	**⚡ Standard**
	Daily Upload limit 50GB

	
	**💎 Pro**
	Daily Upload limit 100GB
	
	
	
	After Payment Send Screenshots Of 
        Payment To Admin @calladminrobot"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("",url = "https://t.me/calladminrobot")], 
        			[InlineKeyboardButton("",url = "https://telegra.ph/file/7f959437f9375b313ed1c.jpg"),
        			InlineKeyboardButton("",url = "https://telegra.ph/file/30b3e45a02766803883cb.jpg")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
