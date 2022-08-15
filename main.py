import json
import os
import sys
from operator import itemgetter
from collections import Counter

retweeted_top = []
days_top = []
users_top = []
with open(os.path.join(sys.path[0], "farmers-protest-tweets-2021-03-5.json"), "r") as json_file:
    data = json.load(json_file)
    for i in data:
      retweeted_top.append([i['retweetCount'], i['content']])
      date = (i['date'])[0:10]
      days_top.append(date)
      username = i['user'][0]
      users_top.append(username)

def tweets():
  sorted(retweeted_top, key=itemgetter(0), reverse=True)
  for i in range(10):
    print(retweeted_top[i][1])
    print("\n")

def users():
    result_users = [item for items, c in Counter(users_top).most_common() for item in [items] * c]
    for i in range(10):
      print(result_users[i])
      print("\n")

def days():
    result = [item for items, c in Counter(days_top).most_common() for item in [items] * c]
    for i in range(10):
      print(result[i])
      print("\n")

def hashtags():
  print("No alcancé uwu")

def main():
  print("Qué deseas hacer:")
  print("[1] Ver el top 10 de tweets más retweted")
  print("[2] Ver el top 10 de usuarios en función de la cantidad de tweets que emitieron")
  print("[3] Ver el top 10 de días donde hay más tweets")
  print("[4] Ver el top 10 de hashtags más usados")
  opcion = input("Escribe 1, 2, 3 o 4")
  if opcion == '1':
    tweets()
  elif opcion == '2':
    users()
  elif opcion == '3':
    days()
  elif opcion == '4':
    hashtags()

a = main()