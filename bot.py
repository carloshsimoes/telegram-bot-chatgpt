from libs.chat import *
from config import telegramApiToken, botName, botCommands

import telebot

bot = telebot.TeleBot(telegramApiToken)


botCommandStart = botCommands.get("start",'start')
botCommandChat = botCommands.get("chat",'gpt')
botCommandImage = botCommands.get("image",'create')



@bot.message_handler(commands=[command for command in botCommandStart])
def sendWelcome(message):
    responseText = f"""
    Olá, eu sou o {botName} e estou aqui para te ajudar!

    Para fazer alguma pergunta, digite um dos comandos disponíveis:
    
    /{botCommandChat} SUA PERGUNTA

    /{botCommandImage} DESCRIÇÃO DA IMAGEM QUE DESEJA CRIAR
    """
    bot.reply_to(message, responseText)



@bot.message_handler(commands=[botCommandChat])
def sendResponse(message):
    try:
        askToSendGpt = message.text[len(botCommandChat)+2:]
        print(f'[/{botCommandChat}] askToSendGpt ==> {askToSendGpt}')
        #print(f'[/{botCommandChat}] len(askToSendGpt.split()) ==> {len(askToSendGpt.split())}')

        if len(askToSendGpt.split()) <= 50:
            response = askToGPT(askToSendGpt)
            responseText = response["choices"][0]["text"]
        else:
            responseText = "Hum... sua pergunta é muito grande... Tente reduzir o tamanho da sua pergunta... =]"

        bot.reply_to(message, responseText)

    except Exception as e:
        responseText = "Ops... Não consegui processar sua pergunta nesse momento. Provavelmente estou passando por instabilidade. Por favor tente mais tarde... =["
        bot.reply_to(message, responseText)
        print(f"[LOG ERROR: {e}")



@bot.message_handler(commands=[botCommandImage])
def createImage(message):
    try:
        askToImageGptCreate = message.text[len(botCommandImage)+2:]
        print(f'[/{botCommandImage}] askToImageGptCreate ==> {askToImageGptCreate}')
        #print(f'[/{botCommandImage}] len(askToImageGptCreate.split()) ==> {len(askToImageGptCreate.split())}')

        if len(askToImageGptCreate.split()) <= 50:
            respondeImageUrl = createImageGPT(askToImageGptCreate)
            bot.reply_to(message, respondeImageUrl)
        else:
            responseText = "Hum... sua descrição é muito grande... Tente reduzir o tamanho da sua descrição... =]"
            bot.reply_to(message, responseText)

    except Exception as e:
        responseText = "Ops... Não consegui processar/gerar a imagem nesse momento. Provavelmente estou passando por instabilidade. Por favor tente mais tarde... =["
        bot.reply_to(message, responseText)
        print(f"[LOG ERROR: {e}")


# Start polling BOT
bot.infinity_polling()
