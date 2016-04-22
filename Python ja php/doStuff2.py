#!/usr/bin/env python
#Argumentteina kulma mihin kaannetaan
#Ilman argumentteja keskiasentoon

import RPi.GPIO as GPIO
import time
import sys
import thread

tonePin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(tonePin, GPIO.IN)
GPIO.setup(tonePin, GPIO.OUT)
p = GPIO.PWM(tonePin, 100)
tempo = 1.25
lastState = "false"
lastTurn = 0.0015

def delay(times):
    time.sleep(times/1000.0)

def turn(varON):
	varLOOPS=10
	varCOUNTER=0
	varTOTAL = 0.02
	while varCOUNTER < varLOOPS :
	    GPIO.output(17, True)
	    time.sleep(varON)
	    GPIO.output(17, False)
	    time.sleep(varTOTAL-varON)
	    varCOUNTER = varCOUNTER + 1

def tone(pin, pitch, duration):
    global lastState
    global lastTurn
    while True :
	fTurn = open('/var/www/turn', 'r')
	varTurn = fTurn.read()
	fTurn.close()
	
	if varTurn != "" :
		varON = float(varTurn)
	else :
		varON = 0.0015
	
	if lastTurn != varON :
		turn(varON)
		lastTurn = varON
	
        fMove = open('/var/www/move', 'r')
        varMove = fMove.read()
        fMove.close()
	varMove.strip()
#	print(varMove)
        if varMove == "true" :
		if lastState != "true" :
			print "Start pin 24"
			GPIO.output(24, True)
			lastState = "true"
        	break
	if varMove == "back" :
		if lastState != "back" :
			print "Start pin 23"
			GPIO.output(23, True)
			lastState = "back"
		break;	
	if lastState != "false" :
		print "Stop pin 24"
		GPIO.output(24, False)
		GPIO.output(23, False)
		lastState = "false"
        time.sleep(0.3)

    if pitch == 0:
        delay(duration)
        return
    p = GPIO.PWM(tonePin, pitch)
    
    # Change the duty-cycle to 50 if you wish
    p.start(30)
    delay(duration * tempo)
    p.stop()
    
    # Delay used to discourage overlap of PWM cycles
    delay(2)
    
def midi():
    tone(tonePin, 391, 204.54525)
    tone(tonePin, 440, 102.272625)
    delay(113.63625)
    tone(tonePin, 493, 102.272625)
    delay(113.63625)
    tone(tonePin, 523, 409.0905)
    tone(tonePin, 587, 102.272625)
    delay(113.63625)
    tone(tonePin, 659, 102.272625)
    delay(340.90875)
    tone(tonePin, 415, 818.181)
    delay(909.09)
    tone(tonePin, 440, 204.54525)
    tone(tonePin, 349, 102.272625)
    delay(113.63625)
    tone(tonePin, 440, 102.272625)
    delay(113.63625)
    tone(tonePin, 391, 409.0905)
    delay(568.18125)
    tone(tonePin, 415, 102.272625)
    tone(tonePin, 440, 204.54525)
    tone(tonePin, 349, 102.272625)
    delay(113.63625)
    tone(tonePin, 349, 204.54525)
    tone(tonePin, 440, 102.272625)
    tone(tonePin, 391, 306.817875)
    delay(113.63625)
    tone(tonePin, 369, 102.272625)
    tone(tonePin, 391, 102.272625)
    tone(tonePin, 369, 102.272625)
    tone(tonePin, 391, 102.272625)
    tone(tonePin, 369, 102.272625)
    tone(tonePin, 391, 409.0905)
    tone(tonePin, 391, 102.272625)
    delay(568.18125)
    tone(tonePin, 391, 204.54525)
    tone(tonePin, 349, 204.54525)
    tone(tonePin, 391, 204.54525)
    tone(tonePin, 415, 409.0905)
    tone(tonePin, 415, 102.272625)
    delay(454.545)
    tone(tonePin, 311, 306.817875)
    tone(tonePin, 349, 102.272625)
    delay(113.63625)
    tone(tonePin, 369, 102.272625)
    delay(113.63625)
    tone(tonePin, 391, 409.0905)
    tone(tonePin, 466, 409.0905)
    tone(tonePin, 349, 409.0905)
    tone(tonePin, 391, 409.0905)
    tone(tonePin, 415, 102.272625)
    delay(909.09)
    tone(tonePin, 415, 306.817875)
    tone(tonePin, 391, 102.272625)
    delay(113.63625)
    tone(tonePin, 369, 102.272625)
    delay(113.63625)
    tone(tonePin, 349, 409.0905)
    tone(tonePin, 440, 204.54525)
    tone(tonePin, 440, 102.272625)
    tone(tonePin, 466, 511.363125)
    tone(tonePin, 554, 409.0905)
    tone(tonePin, 523, 306.817875)
    tone(tonePin, 523, 306.817875)
    tone(tonePin, 466, 204.54525)
    tone(tonePin, 415, 102.272625)
    delay(340.90875)
    tone(tonePin, 830, 102.272625)
    delay(340.90875)
    tone(tonePin, 415, 306.817875)
    tone(tonePin, 349, 306.817875)
    tone(tonePin, 293, 306.817875)
    tone(tonePin, 246, 306.817875)
    tone(tonePin, 207, 204.54525)
    tone(tonePin, 155, 204.54525)
    tone(tonePin, 523, 306.817875)
    tone(tonePin, 523, 306.817875)
    tone(tonePin, 466, 204.54525)
    tone(tonePin, 415, 102.272625)
    delay(340.90875)
    tone(tonePin, 830, 102.272625)
    delay(340.90875)
    tone(tonePin, 391, 204.54525)
    tone(tonePin, 440, 102.272625)
    delay(113.63625)
    tone(tonePin, 493, 102.272625)
    delay(113.63625)
    tone(tonePin, 523, 409.0905)
    tone(tonePin, 587, 102.272625)
    delay(113.63625)
    tone(tonePin, 659, 102.272625)
    delay(340.90875)
    tone(tonePin, 415, 818.181)
    delay(909.09)
    tone(tonePin, 440, 204.54525)
    tone(tonePin, 349, 102.272625)
    delay(113.63625)
    tone(tonePin, 440, 102.272625)
    delay(113.63625)
    tone(tonePin, 391, 409.0905)
    delay(568.18125)
    tone(tonePin, 415, 102.272625)
    tone(tonePin, 440, 204.54525)
    tone(tonePin, 349, 102.272625)
    delay(113.63625)
    tone(tonePin, 349, 204.54525)
    tone(tonePin, 440, 102.272625)
    tone(tonePin, 391, 306.817875)
    delay(113.63625)
    tone(tonePin, 369, 102.272625)
    tone(tonePin, 391, 102.272625)
    tone(tonePin, 369, 102.272625)
    tone(tonePin, 391, 102.272625)
    tone(tonePin, 369, 102.272625)
    tone(tonePin, 391, 409.0905)
    tone(tonePin, 391, 102.272625)
    delay(568.18125)
    tone(tonePin, 391, 204.54525)
    tone(tonePin, 349, 204.54525)
    tone(tonePin, 391, 204.54525)
    tone(tonePin, 415, 409.0905)
    tone(tonePin, 415, 102.272625)
    delay(454.545)
    tone(tonePin, 311, 306.817875)
    tone(tonePin, 349, 102.272625)
    delay(113.63625)
    tone(tonePin, 369, 102.272625)
    delay(113.63625)
    tone(tonePin, 391, 409.0905)
    tone(tonePin, 466, 409.0905)
    tone(tonePin, 349, 409.0905)
    tone(tonePin, 391, 409.0905)
    tone(tonePin, 415, 102.272625)
    tone(tonePin, 207, 204.54525)
    tone(tonePin, 195, 102.272625)
    delay(113.63625)
    tone(tonePin, 184, 102.272625)
    delay(113.63625)
    tone(tonePin, 174, 102.272625)
    delay(113.63625)
    tone(tonePin, 174, 102.272625)
    delay(113.63625)
    tone(tonePin, 233, 102.272625)
    delay(113.63625)
    tone(tonePin, 233, 102.272625)
    delay(113.63625)
    tone(tonePin, 277, 102.272625)
    tone(tonePin, 277, 102.272625)
    tone(tonePin, 277, 102.272625)
    tone(tonePin, 349, 306.817875)
    delay(227.2725)
    tone(tonePin, 155, 102.272625)
    delay(113.63625)
    tone(tonePin, 155, 102.272625)
    delay(113.63625)
    tone(tonePin, 207, 102.272625)
    delay(113.63625)
    tone(tonePin, 207, 102.272625)
    delay(113.63625)
    tone(tonePin, 261, 102.272625)
    tone(tonePin, 261, 102.272625)
    tone(tonePin, 261, 102.272625)
    tone(tonePin, 311, 306.817875)
    delay(227.2725)
    tone(tonePin, 138, 102.272625)
    delay(113.63625)
    tone(tonePin, 138, 102.272625)
    delay(113.63625)
    tone(tonePin, 174, 102.272625)
    delay(113.63625)
    tone(tonePin, 174, 102.272625)
    delay(113.63625)
    tone(tonePin, 233, 102.272625)
    tone(tonePin, 233, 102.272625)
    tone(tonePin, 233, 102.272625)
    tone(tonePin, 277, 306.817875)
    tone(tonePin, 523, 306.817875)
    tone(tonePin, 523, 306.817875)
    tone(tonePin, 466, 204.54525)
    tone(tonePin, 415, 102.272625)
    delay(340.90875)
    tone(tonePin, 830, 102.272625)

# Ikiloop
while True :
	midi()

