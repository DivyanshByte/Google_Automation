from selenium import webdriver
import sys
from time import sleep
import speech_recognition as sr
driver = webdriver.Edge(executable_path = 'H:\\edgedriver_win64\\Edge.exe')
driver.get('https:///www.google.com')
def get_audio(): 

	rObject = sr.Recognizer() 
	audio = ""

	with sr.Microphone() as source: 
		print("Speak...") 
		
		# recording the audio using speech recognition 
		audio = rObject.listen(source, phrase_time_limit = 5) 
	print("Stop.") # limit 5 secs 

	try: 

		text = rObject.recognize_google(audio, language ='en-IN') 
		print("You Speak: ", text) 
		return text

	except: 
		print("Could Not Understand your audio")
		sys.exit()
		driver.close()
sm = int(input("Choose Mode(1 - Text Search, 2 - Voice Search, Any Other No. - Exit): "))
if sm == 1:
	s = input('What Do You Want To Search Google: ')
	sb = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
	sb.send_keys(s)
	sb.submit()
	sleep(2)
elif sm == 2:
	sleep(1)
	s = get_audio()
	sb = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
	sb.send_keys(s)
	sb.submit()
	sleep(2)
else:
	driver.close()
	sys.exit()
driver.close()
sys.exit()