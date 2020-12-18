# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:33:54 2019

Grab audio from yt and save to disc in wav format
Requires youtube_dl as well as ffmpeg

https://ostechnix.com/youtube-dl-tutorial-with-examples-for-beginners/

@author: Harry Ahlas
"""

from __future__ import unicode_literals
import os
import youtube_dl
import json

os.mkdir('C:\\Users\\Anyone\\Music\\My Little Pony\\disc4')

# no longer needed
os.chdir('C:\\Users\\Anyone\\Music\\My Little Pony\\disc4')

files_directory = "'C:/Users/Anyone/Music/My Little Pony/disc4'"

#https://www.youtube.com/watch?v=LW7ilujFKlw # a couple hours

url_list = [
'https://www.youtube.com/watch?v=Ea-xt3jh9GY', #christmas
'https://www.youtube.com/watch?v=c2UhUtBzxHM',
'https://www.youtube.com/watch?v=qsqkPJFmAIQ',
'https://www.youtube.com/watch?v=444eT_yh6So',
'https://www.youtube.com/watch?v=HzvwJ4dAzbQ&list=PLA3378A1CEEFAA3FF&index=2',
'https://www.youtube.com/watch?v=b9EqoWzTKRY&list=PLA3378A1CEEFAA3FF&index=4',
'https://www.youtube.com/watch?v=dahyYs8PFdE&list=PLA3378A1CEEFAA3FF&index=5',
'https://www.youtube.com/watch?v=jNw_vmu4VeQ&list=PLA3378A1CEEFAA3FF&index=6',
'https://www.youtube.com/watch?v=nUMY5L7TzDk&list=PLA3378A1CEEFAA3FF&index=7',
'https://www.youtube.com/watch?v=5spYX1Q1dOI&list=PLA3378A1CEEFAA3FF&index=9',
'https://www.youtube.com/watch?v=VhU-zrwPtuU&list=PLA3378A1CEEFAA3FF&index=10',
'https://www.youtube.com/watch?v=ES6JtmUSyfk&list=PLA3378A1CEEFAA3FF&index=12',
'https://www.youtube.com/watch?v=sASS6bsjOw4&list=PLA3378A1CEEFAA3FF&index=13',
'https://www.youtube.com/watch?v=5y0o2BLf2VI&list=PLA3378A1CEEFAA3FF&index=15',
'https://www.youtube.com/watch?v=5pjMMM0ycRc&list=PLA3378A1CEEFAA3FF&index=16',
'https://www.youtube.com/watch?v=EqV0LjMLCAo&list=PLA3378A1CEEFAA3FF&index=17',
'https://www.youtube.com/watch?v=W5TVsWl9d_I&list=PLA3378A1CEEFAA3FF&index=18',
'https://www.youtube.com/watch?v=ZM4OBQT59ow&list=PLA3378A1CEEFAA3FF&index=20',
'https://www.youtube.com/watch?v=Z88Y7bfRueI&list=PLA3378A1CEEFAA3FF&index=22',
'https://www.youtube.com/watch?v=wUxhX7nPdgw&list=PLA3378A1CEEFAA3FF&index=23',
'https://www.youtube.com/watch?v=f8r4gYMmjlk&list=PLA3378A1CEEFAA3FF&index=24',
'https://www.youtube.com/watch?v=C7R2YA1FEHc&list=PLA3378A1CEEFAA3FF&index=25',
'https://www.youtube.com/watch?v=FAjN_kz095I&list=PLA3378A1CEEFAA3FF&index=26',
'https://www.youtube.com/watch?v=ln7fy5w2WJ4&list=PLA3378A1CEEFAA3FF&index=28',
'https://www.youtube.com/watch?v=F94xjzbpLtc&list=PLA3378A1CEEFAA3FF&index=29',
'https://www.youtube.com/watch?v=sMbUUmfg6ok&list=PLA3378A1CEEFAA3FF&index=30',
'https://www.youtube.com/watch?v=6GkDlO_hMI8&list=PLA3378A1CEEFAA3FF&index=32',
'https://www.youtube.com/watch?v=OLE3DmidjBI&list=PLA3378A1CEEFAA3FF&index=35',
'https://www.youtube.com/watch?v=1Rpq4RRpTeU&list=PLA3378A1CEEFAA3FF&index=36',
'https://www.youtube.com/watch?v=qr5hDJtL0tE&list=PLA3378A1CEEFAA3FF&index=39',
'https://www.youtube.com/watch?v=mtsle9CeEQA&list=PLA3378A1CEEFAA3FF&index=41',
'https://www.youtube.com/watch?v=Uqq45CVuzK0&list=PLA3378A1CEEFAA3FF&index=42',
'https://www.youtube.com/watch?v=x_JI18l_Nco&list=PLA3378A1CEEFAA3FF&index=43',
'https://www.youtube.com/watch?v=0PZBsLqkiRM&list=PLA3378A1CEEFAA3FF&index=45',
'https://www.youtube.com/watch?v=Xcu0Lb9VA1M&list=PLA3378A1CEEFAA3FF&index=46',
'https://www.youtube.com/watch?v=HENvEjgA2Lw&list=PLA3378A1CEEFAA3FF&index=47',
]

## Example cmd call
#os.system('youtube-dl.exe -x --audio-format wav "https://www.youtube.com/watch?v=NtgeA31nghk"')

def download_youtube_wav(url_address):
    os_command = str('cd ' + files_directory + ' & youtube-dl.exe -x --audio-format wav "' + url_address + '"')
    print(str("running " + url_address))
    os.system(os_command)

## Example function use
#download_youtube_wav("https://www.youtube.com/watch?v=EPH8YXHNrIs&list=PLfJpfTZK5SWCiYXqfwRxwsu0om4Cfus8g")

for url in url_list:
    download_youtube_wav(url) 

