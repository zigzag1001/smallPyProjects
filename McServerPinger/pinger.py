from mcstatus import MinecraftServer
from time import sleep
from datetime import datetime
from datetime import date

prev = ""

server = MinecraftServer.lookup("[ip adress]:[port]")

while 1:
  status = server.status()

  now = datetime.now()
  today = date.today()
  
  print("Server has", status.players.online, "players online", now.strftime("%H:%M"))
  
  with open(".\\log.txt", "a") as log:
    if str(status.players.online) != prev:
      log.write("(" + today.strftime("%b-%d-%Y") + ") " + now.strftime("%H:%M") + "  -> " + str(status.players.online) + "\n")
      
  prev = str(status.players.online)
  sleep(60)
