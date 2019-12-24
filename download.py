
import os, sys
from termcolor import colored

print(colored('_'*50,'yellow'))
baner= """

  ___ __ _  ___ __ _  ___ _ __ __ _  ___| | __
 / __/ _` |/ __/ _` |/ __| '__/ _` |/ __| |/ /
| (_| (_| | (_| (_| | (__| | | (_| | (__|   <
 \___\__,_|\___\__,_|\___|_|  \__,_|\___|_|\_|
 Youtube : CACACRACK
 Instagram: jeager000
 Code by: jeager
 [Download musik youtube]
 """

print(colored(baner,'green'))
print(colored('Options..','yellow'))
print(colored('1.Download music','yellow'))
print(colored('2.Play music','yellow'))
select=str(input(colored('Select number: ','yellow')))
print(colored('_'*50,'yellow'))

if select == '1':
  link=str(input(colored('Input link: ','yellow')))
  os.system('youtube-dl -x --audio-format mp3 -o "/sdcard/YouTube/%(title)s.%(ext)s" '+link)
  print(colored('Download success','blue'))
  print(colored('Check your file in /sdcard/YouTube','blue'))
elif select == '2':
  folder=str(input(colored('Input path your file: ','yellow')))
  os.system('mpv '+folder )
else:
  print(colored('Number '+select+' not found in options','red'))