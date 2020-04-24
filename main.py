import telepot
import time
from lib import data_handler

chat = {'id': []}
handler = data_handler.handler()

def on_chat_message(id_chat):
  content_type, chat_type, chat_id = telepot.glance(id_chat)
  if content_type == 'text':
    chat['id'].append(chat_id)

token = '1162437785:AAFPaS8YW4qjJP8PVC4BPvW3vR1RkxUIU9w'

print('Sto attendendo...')

bot = telepot.Bot(token)
bot.message_loop(on_chat_message)

while True:
  handler.genData()
  crit = handler.getCritical()
  
  if (not len(chat['id']) == 0):
    for c in chat['id']:
      for p in crit:
        msg = "PAZIENTE CRITICO!!!\n{0} {1} ha un valore SpO2 di {2}".format(p['paziente']['cognome'], p['paziente']['nome'], p['valore'])
        bot.sendMessage(c, msg)

      bot.sendMessage(c, ".")

  time.sleep(10)