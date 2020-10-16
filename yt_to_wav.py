# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:33:54 2019

Grab audio from yt and save to disc in wav format
Requires youtube_dl as well as ffmpeg

@author: Harry Ahlas
"""

from __future__ import unicode_literals
import os
import youtube_dl
import json

os.mkdir('C:\\Users\\Anyone\\Music\\Rodrigo y Gabriela\\yt1')

os.chdir('C:\\Users\\Anyone\\Music\\Rodrigo y Gabriela\\yt1')





def paste0(string1, range1 ):
#    texts = [string1 + str(num1)  for num1 in zip(range1)]
    texts = [string1 + str(num1)  for num1 in (range1)]
    return texts

url_list = paste0("https://www.youtube.com/watch?v=b3lCjBjexWQ&list=PLpcGjv9eMpOPH2bbR1t6GnhQXdaHignQA&index=", 
               range(1, 43))

url_list = [
'https://www.youtube.com/watch?v=oAemYgwNCBo',
'https://www.youtube.com/watch?v=fphUZV7dKUw', #doesn't work
'https://www.youtube.com/watch?v=xthcbwng0Uo',
'https://www.youtube.com/watch?v=hAXX_bPxIzY&t=65s', #doesn't work
'https://www.youtube.com/watch?v=utyk5gHOAU0',
'https://www.youtube.com/watch?v=hZUew-9HPI8', #doesn't work
'https://www.youtube.com/watch?v=-bboX3LpWpE',
'https://www.youtube.com/watch?v=tao1Ic8qVkM',
'https://www.youtube.com/watch?v=dkTPatXRyh0',
'https://www.youtube.com/watch?v=L9BAeyZhAdE',
'https://www.youtube.com/watch?v=WOF3BkkRPSs',
'https://www.youtube.com/watch?v=GpDcVY4F3QQ',
'https://www.youtube.com/watch?v=ExgxOxPFVj4',
'https://www.youtube.com/watch?v=ep0uCcIF2Y8',
'https://www.youtube.com/watch?v=GU1zVxYNDRY',
'https://www.youtube.com/watch?v=9aJyDsL2wMU',
'https://www.youtube.com/watch?v=F5-BAYPoqdY', #christmas
'https://www.youtube.com/watch?v=tjVWPszPP5I',
'https://www.youtube.com/watch?v=Jqd88q-7wI0', #less
'https://www.youtube.com/watch?v=7qhsmjeQyyA', #less
'https://www.youtube.com/watch?v=EmVRhL1ocjA',
'https://www.youtube.com/watch?v=U3RGU90y79k']


def download_youtube_music(url_address):
    ydl_opts = {
        'noplaylist':True,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            #'preferredcodec': 'mp3',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url_address])


     
download_youtube_music(url_list[1]) 
download_youtube_music('https://www.youtube.com/watch?v=b3lCjBjexWQ&list=PLpcGjv9eMpOPH2bbR1t6GnhQXdaHignQA')
            
      
for url in url_list:
    download_youtube_music(url) 
    
    #download_youtube_music(url_list[3])
