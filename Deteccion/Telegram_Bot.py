import requests

def telegram_bot_sendtext(bot_message):
	
   bot_token = '1206079818:AAHGNu0_ALjcMCBs6_nnHwDTsL7iHnDeWxw'
   bot_chatID = '192194744'
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()
	

while True:
	f=open("Mov.txt", "r")
	valor=f.readline()
	#valor="1"
	f.close()

	if (valor=="1"):
		test = telegram_bot_sendtext("Se ha detectado presencia en la zona de las dos rocas.")
		print(test)

