from random import choice
import time
thislist = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n' ,'m', ',', '.']
print ('Find the key as fast as possible')
t = int(input('How many charecters?\n'))
start = time.time()
for n in range(t):
 key = choice(thislist)
 print ('===', '\n', key.upper(), '\n' + '===')
 inputt = ''
 while (inputt != key):
   inputt = input()
 if (inputt == key):
  i = round(time.time() - start, 2) 
  print('\n\n')
print('Your time:', i , 'seconds')
