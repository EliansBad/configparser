from configparser import *
config = ConfigParser()
config.read('config.ini')
config['Settings']
config['Settings']['lowest']
config['Settings']['highest']
low = int(config.get("Settings","lowest"))
high = int(config.get("Settings","highest")) 
status = True
from random import randrange as r
num = r(low, high)
print(f'enter a number beetwen {low} - {high}')
while status:
  inp = input('> ')
  if int(inp) == int(num):
    status = False
    print('GOOD JOB!')
  elif int(inp) > int(num): print('too big try again')
  else: print('too small try again')
