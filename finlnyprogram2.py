

import pigpio
import time



#Œwiat³a pó³noc-po³udnie samochody
L4 = 24		#czerwone
L5 = 17 	#pomarañczowe
L6 = 27		#zielone

#Œwiat³a wschód-zachód samochody
L1 = 22		#czerwone
L2 = 5		#pomarañczowe
L3 = 6		#zielone

#Œwiat³a wschód-zachód piesi
L7 = 13		#czerwone
L8 = 19		#zielone

#Œwiat³a pó³noc-po³udnie piesi
L9 = 26		#czerwone
L10 = 18	#zielone

# Czas zamiany sekwencji
#time.sleep(x.x)

pi = pigpio.pi() #zamiana pigpio.pi na pi

#inicjacja wyjœæ
pi.set_mode(L4,pigpio.OUTPUT)    #A czerwone
pi.set_mode(L5,pigpio.OUTPUT)    #A pomarañczowe
pi.set_mode(L6,pigpio.OUTPUT)    #A zielone
pi.set_mode(L1,pigpio.OUTPUT)    #C czerwone
pi.set_mode(L2,pigpio.OUTPUT)    #C pomarañczowe
pi.set_mode(L3,pigpio.OUTPUT)    #C zielone
pi.set_mode(L7,pigpio.OUTPUT)    #B czerwone
pi.set_mode(L8,pigpio.OUTPUT)    #B zielone
pi.set_mode(L9,pigpio.OUTPUT)    #D czerwone
pi.set_mode(L10,pigpio.OUTPUT)   #D zielone

while True: #zapetlenie
   
    pi.write(L4,1)
    pi.write(L8,1)
    pi.write(L2,1)
    pi.write(L9,1)
    time.sleep(2.0)   #czas po pierwszej sekwencji

    pi.write(L2,0)
    pi.write(L3,1)
    time.sleep(2.0)   #czas po drugiej sekwencji

    pi.write(L1,0)
    pi.write(L8,0)
    pi.write(L7,1)
    pi.write(L3,0)
    pi.write(L2,1)
    time.sleep(2.0)   #czas po trzeciej sekwencji

    pi.write(L1,0)
    pi.write(L8,1)
    pi.write(L2,0)
    pi.write(L1,1)
    pi.write(L9,0)
    pi.write(L10,1)
    time.sleep(2.0)   #czas po czwartej sekwencji

    pi.write(L5,0)
    pi.write(L6,1)
    time.sleep(2.0)   #czas po pi¹tej sekwencji

    pi.write(L6,0)
    pi.write(L7,0)
    pi.write(L1,0)
    pi.write(L10,0)  
pi.stop()
	
		
def cyklswiatel1():
  print ("****** 1 cykl ********")
  
  print ("ared: high")
  print ("aorange: low")
  print ("agreen: low")

  print ("cred: low")
  print ("corange: high")
  print ("cgreen: low")
  
  print ("dred: high")
  print ("dgreen: low")
  
  print ("bred: low")
  print ("bgreen: high")

def cyklswiatel2():
  print ("****** 2 cykl ********")
  
  print ("ared: high")
  print ("aorange: low")
  print ("agreen: low")
  
  print ("cred: low")
  print ("corange: low")
  print ("cgreen: high")
  
  print ("dred: high")
  print ("dgreen: low")
  
  print ("bred: low")
  print ("bgreen: high")

def cyklswiatel3():
  print ("****** 3 cykl ********")
  
  print ("ared: high")
  print ("aorange: low")
  print ("agreen: low")
  
  print ("cred: low")
  print ("corange: high")
  print ("cgreen: low")
  
  print ("dred: high")
  print ("dgreen: low")
  
  print ("bred: high")
  print ("bgreen: low")

  
def cyklswiatel4():
  print ("****** 4 cykl ********")
  
  print ("ared: low")
  print ("aorange: low")
  print ("agreen: high")
  
  print ("cred: high")
  print ("corange: low")
  print ("cgreen: low")
  
  print ("dred: low")
  print ("dgreen: high")
  
  print ("bred: high")
  print ("bgreen: low")

def cyklswiatel5():
  print ("****** 5 cykl ********")
  
  print ("ared: low")
  print ("aorange: low")
  print ("agreen: high")
  
  print ("cred: high")
  print ("corange: low")
  print ("cgreen: low")
  
  print ("dred: low")
  print ("dgreen: high")
  
  print ("bred: high")
  print ("bgreen: low")
  
def skrzyzowanie():
  while True:
    cyklswiatel1()
    time.sleep(2.0)
    cyklswiatel2()
    time.sleep(2.0)
    cyklswiatel3()
    time.sleep(2.0)
    cyklswiatel4()
    time.sleep(2.0)	
    cyklswiatel5()
    time.sleep(2.0)
	
skrzyzowanie()

#MARCIN PIETRZAK	202526
#PAWE£ W¥GIEL		202544
#DATA ODDANIA		21.11.2017
