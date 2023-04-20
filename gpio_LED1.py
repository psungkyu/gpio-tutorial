import RPi.GPIO as GPIO # 사용하기 편리하도록 GPIO로 alias
import time # sleep을 주기 위해 임포트

GPIO.setmode(GPIO.BCM) # 사용할 핀모드 설정(BCM 모드)
GPIO.setup(17,GPIO.OUT) # 17번 GPIO 셋팅
GPIO.setup(27,GPIO.OUT) # 27번 GPIO 셋팅

while(True):
    GPIO.output(17,False) # 끄기
    GPIO.output(27,False)
    time.sleep(1) # 1초 sleep	

    GPIO.output(17,True) # 켜기
    GPIO.output(27,True)
    time.sleep(1) # 1초 sleep
