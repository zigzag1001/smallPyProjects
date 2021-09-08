import random
import pyautogui
import os
import time

wordList = []

with open("words.txt") as words:
	wordList = words.read().split("\n")

for i in range(len(wordList)):
	time.sleep(random.randint(120, 300))
	current = random.choice(wordList)
	pyautogui.write(current)
	pyautogui.press("enter")
	wordList.remove(current)
	print(i, "->", current)