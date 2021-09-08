import os
import pyautogui
from time import sleep

i = 0
toSend = ""

with open('thing.txt') as text:
  other = text.read()
sleep(1)
print(1)
sleep(1)
print(2)
sleep(1)
print(3)
sleep(1)

for t in other:
  toSend += t
  i += 1
  if i >= 500 and t == ".":
    sleep(1)
    pyautogui.write(toSend)
    pyautogui.press("enter")
    toSend = ""
    i = 0
pyautogui.write(toSend)
