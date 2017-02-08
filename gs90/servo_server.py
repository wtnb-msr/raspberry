#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import signal
import sys 

from bottle import route, run, template


class ServoMotor():

  def __init__():
    self.gpio_num = 13

  def run():
    # 終了処理用のシグナルハンドラを準備
    signal.signal(signal.SIGINT, exit_handler)
    
    GPIO.setmode(GPIO.BCM)
    
    # GPIO 12番を使用 (PWM 0)
    GPIO.setup(self.gpio_num, GPIO.OUT)
    # 20ms / 50Hzに設定、らしい
    self.servo = GPIO.PWM(self.gpio_num, 50)
    
    # 初期化
    servo.start(0.0)


  def exit_handler(signal, frame):
    # Ctrl+Cが押されたときにデバイスを初期状態に戻して終了する。
    print("\nExit")
    servo.stop()
    GPIO.cleanup()
    sys.exit(0)


class ServoControlServer():

  def __init__(self):
    self.servo = ServoMotor()

  @route('/angle')
  def get_angle():
    return 'ok\n'

  @route('/angle/<angle>')
  def set_angle(angle):
    dc = angle
    servo.ChangeDutyCycle(dc)
    print("angle = {a}, dc = {dc}".format(a=angle, dc=dc))
    return 'ok\n'

  def serve(self):
    run(host='localhost', port=8080, debug=True, reloader=True)


server = ServoControlServer()
server.serve()

# ChangeDutyCycleに渡す値は 0.0 <= dc <= 100.0
# ……のはずだが、なぜか2から12の間で動作している。
#dc = 0.0
#while True:
#  #for dc in range(2, 12, 1):
#  for dc in [2,8,12]:
#    servo.ChangeDutyCycle(dc)
#    print("dc = %d" % dc)
#    time.sleep(0.5)
#    time.sleep(0.5)
#
#  #for dc in range(12, 2, -1):
#  for dc in [12,8,2]:
#    servo.ChangeDutyCycle(dc)
#    print("dc = %d" % dc)
#    time.sleep(0.5)
#    time.sleep(0.5)
