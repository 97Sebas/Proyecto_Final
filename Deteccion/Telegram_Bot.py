import requests
<<<<<<< HEAD
import datetime



class BotHandler:
    def __init__(self, token):
            self.token = token
            self.api_url = "https://api.telegram.org/bot{}/".format(token)

    #url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update


token = '1206079818:AAHGNu0_ALjcMCBs6_nnHwDTsL7iHnDeWxw' #Token of your bot
magnito_bot = BotHandler(token) #Your bot's name



def main():
    new_offset = 0
    print('hi, now launching...')

    while True:
        #all_updates=magnito_bot.get_updates(new_offset)

        #f = open("Movimiento.txt", "r")
        all_updates = "1" #= f.readlines()
       
        if len(all_updates) > 0:
            #print(all_updates)
            if all_updates == '1':
                magnito_bot.send_message(first_chat_id, 'Nueva Alerta en el sendero Las Dos Rocas ' + first_chat_name)
                new_offset = first_update_id + 1
            else:
                magnito_bot.send_message(first_chat_id, ' '+first_chat_name)
                new_offset = first_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
=======
import paramiko

def telegram_bot_sendtext(bot_message):
	
   bot_token = '1206079818:AAHGNu0_ALjcMCBs6_nnHwDTsL7iHnDeWxw'
   bot_chatID = '192194744'
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()
	
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.1.7',username='root',password='1234',port=22)
sftp_client=ssh.open_sftp()

while True:
    sftp_client.get('/home/root/Movimiento.txt','Movimiento.txt')
	f=open("Movimiento.txt", "r")
	valor=f.readline()
	#valor="1"
	f.close()

	if (valor=="1"):
		test = telegram_bot_sendtext("Se ha detectado presencia en la zona de las dos rocas.")
		print(test)
		
		sftp_client.get('/home/root/Movimiento.txt','Movimiento.txt')
		f=open("Movimiento.txt", "r")
		valor=f.readline()
		f.close()
		time.sleep(30)

sftp_client.close()
ssh.close()
>>>>>>> d23e668a9e87749d6326c96d89b4c8636a65c9d0
