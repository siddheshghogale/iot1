'''import RPi.GPIO as gp
import time
from tm1637 import TM1637
gp.setwarnings(False)

clk=17
dio=4

display=TM1637(clk,dio)
def display_time():
	current_time=time.strftime("%H%M")
	display.number(int(current_time))
	time.sleep(1)
	print("display...")
	print(current_time)
	
	try:
		for i in range(30):
			display_time()
	except keyboardInterrept:
		print("exiting...")
	finally:
		display.clear()
		gp.cleanup()
display_time()
'''
import RPi.GPIO as gp
import time
from tm1637 import TM1637
gp.setwarnings(False)

clk=17
dio=4

display=TM1637(clk,dio)
def display_time():
	current_time=time.strftime("%H%M")
	display.number(int(current_time))
	time.sleep(1)
	print("display...")
	print(current_time)
	display.show("12 C")
	time.sleep(1)
	
	display.show("temp")
	time.sleep(6)
	try:
		for i in range(10):
			display_time()
	except keyboardInterrept:
		print("exiting...")
	finally:
		display.clear()
		gp.cleanup()
display_time()

