import os
import pyautogui
import pyperclip
from pynput import keyboard
from time import sleep

file = ".\\" + input("input foldername where files are:\n") + "\\" + input("input filename to paste into:\n")

current = set()

with open(file) as checking:
    checkList = checking.read().split(",")

COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='a')},
    {keyboard.Key.shift, keyboard.KeyCode(char='A')}
]


def execute():
  bad = False
  print("Doing")
  pyautogui.click(button='right')
  pyautogui.move(50, 120)
  pyautogui.click()
  pyautogui.move(-50, -120)
  linkFromClipboard = pyperclip.paste()
  if linkFromClipboard in checkList:
    bad = True
    print("Duplicate!")
  if bad == False:
    with open(file, 'a') as linksFile:
      linksFile.write(linkFromClipboard+",")
      checkList.append(linkFromClipboard)
  print("Done")

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()
            current.clear()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.clear()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
