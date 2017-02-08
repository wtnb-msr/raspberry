#!/usr/bin/python
# coding: utf-8 

import RPi.GPIO as GPIO
import time
import signal
import sys

def exit_handler(signal, frame):
        # Ctrl+Cが押されたときにデバイスを初期状態に戻して終了する。
        print("\nExit")
        servo.ChangeDutyCycle(2.0)
        time.sleep(0.5)
        servo.stop()
        GPIO.cleanup()
        sys.exit(0)

# 終了処理用のシグナルハンドラを準備
signal.signal(signal.SIGINT, exit_handler)

GPIO.setmode(GPIO.BCM)

# GPIO 21番を使用
gp_out = 13

GPIO.setup(gp_out, GPIO.OUT)
# pwm = GPIO.PWM([チャンネル], [周波数(Hz)])
servo = GPIO.PWM(gp_out, 50)

# 初期化
servo.start(0.0)

while True:
        for angle in range(0, 180, 30):
                dc =(1.0 + angle/180.0)/20.0*100.0 # calculate duty
                servo.ChangeDutyCycle(dc)
                print("Angle = %d" % angle)
                print("dc = %d" % dc)
                time.sleep(0.5)
        for angle in range(180, 0, -30):
                dc =(1.0 + angle/180.0)/20.0*100.0 # calculate duty
                servo.ChangeDutyCycle(dc)
                print("Angle = %d" % angle)
                print("dc = %d" % dc)
                time.sleep(0.5)
