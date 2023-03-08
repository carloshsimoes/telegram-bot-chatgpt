import os

#--------------------------------------------------------------------
# OpenAI and Telegram
#--------------------------------------------------------------------

openaiApiKey = os.getenv("OPENAI_API_TOKEN")
telegramApiToken = os.getenv("TELEGRAM_API_TOKEN")


#--------------------------------------------------------------------
# BotName and Commands
#--------------------------------------------------------------------

botName = "BarbaRoots"

botCommands = {
    "chat": "barba",
    "image": "criar",
    "start": ['start', 'olá', 'oi', 'help', 'ajuda']
}