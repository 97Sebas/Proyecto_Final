import requests
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