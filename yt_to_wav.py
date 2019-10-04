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

os.chdir('C:\\Users\\Anyone\\Music\\My Little Pony')

url_list = ['https://www.youtube.com/watch?v=z8uFbzbtyJg',
    'https://www.youtube.com/watch?v=dM0d9uUgVSc',
    'https://www.youtube.com/watch?v=lQKaAlMNvm8',
    'https://www.youtube.com/watch?v=LH75e2vjowE',
    'https://www.youtube.com/watch?v=Eb-GsRpiezk',
    'https://www.youtube.com/watch?v=OJM2g-3K2T0',
    'https://www.youtube.com/watch?v=5tCPxXW_9qI',
    'https://www.youtube.com/watch?v=lQKaAlMNvm8',
    'https://www.youtube.com/watch?v=jW5n3k2VgZE',
    'https://www.youtube.com/watch?v=hAXX_bPxIzY',
    'https://www.youtube.com/watch?v=fktlkNNp8Mw',
    'https://www.youtube.com/watch?v=uDo9KFvMNX8',
    'https://www.youtube.com/watch?v=DGsVZZtxcP8']

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