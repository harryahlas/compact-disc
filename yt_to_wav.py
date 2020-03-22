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

os.mkdir('C:\\Users\\Anyone\\Music\\My Little Pony\\cd3')

os.chdir('C:\\Users\\Anyone\\Music\\My Little Pony\\cd3')

url_list = [
'https://www.youtube.com/watch?v=oAemYgwNCBo',
'https://www.youtube.com/watch?v=fphUZV7dKUw',
'https://www.youtube.com/watch?v=xthcbwng0Uo',
'https://www.youtube.com/watch?v=hAXX_bPxIzY&t=65s',
'https://www.youtube.com/watch?v=utyk5gHOAU0',
'https://www.youtube.com/watch?v=hZUew-9HPI8',
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
        
for url in url_list:
    download_youtube_music(url) 
    
    
