from art import tprint 
import time
import keyboard
import pyautogui



time.sleep(1)
tprint("TEXT-BOMBER")
time.sleep(1)
tprint("  by  Toyirov Programmer!", "italic")
print("")
print("")
print("")
try:
	global necha
	print("Necha marotaba yuborish kerak!")
	necha = int(input("--> "))
except:
	necha = 10
	print("Siz faqat son kiritishingiz mumkin!")
	print("defoul qiymat 10-ga teng!")


time.sleep(1)
print("")
print("Nima yuborish kerak!")
words = input("--> ")


print("15-secund vaqt!")
time.sleep(1)

def countdown(t):
	while t:
		mins, secs = divmod(t,60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1
countdown(int(15))

print("\n\n")

for x in range(necha):
	keyboard.write(words)
	keyboard.press("Enter")
	time.sleep(0.1)

