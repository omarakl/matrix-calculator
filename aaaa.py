import RPI_emu.GPIO as GPIO
import os
import time
import random


GPIO.setmode(GPIO.BCM)


# initializing pins 7,11 and 12 as output pin

GPIO.setup(7, OUT)
GPIO.setup(11, OUT)
GPIO.setup(12, OUT)

# generating a random number between 0 and 100
number = random.randint(0,100)

counter = 10

# clears the screen
os.system('clear')

print('Guess the number between 0 & 100')
guess = input("Enter your number :")

if guess = number:
	print("You are correct ! The Magic number is " + str(number))
	while count > 0:
		flash_led([7], counter)


elif guess > number:
	print('Your guess is too high')
	while count > 0:
		flash_led([12], counter)

else:
	print('Your guess is too low')
	flash_led([11], counter)



def flash_led(pinList, count, interval = 1):
	for i in range(count):
		for pin in pinList:
			GPIO.output(pin, GPIO.HIGH)
		time.sleep(interval)
		for pin in pinList:
			GPIO.output(pin, GPIO.LOW)
		time.sleep(interval)
		GPIO.cleanup()
