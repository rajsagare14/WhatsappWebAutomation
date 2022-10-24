import pyautogui as auto
from time import sleep

while True:
    auto.write('You good ? ')  # message
    auto.press('enter')
    sleep(1) #delay
