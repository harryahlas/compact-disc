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

#os.mkdir('C:\\Users\\Anyone\\Music\\Enslaved\\')
#os.mkdir('C:\\Users\\Anyone\\Music\\Enslaved\\E')

os.chdir('C:\\Users\\Anyone\\Music\\Possessed\\Revelations of Oblivion')

url_list = ['https://www.youtube.com/watch?v=tq0y5Vs-heI&list=PLfUV806q_Ri7wcsLO8hjbCEG-jXEBqrzS&index=1',
'https://www.youtube.com/watch?v=tq0y5Vs-heI&list=PLfUV806q_Ri7wcsLO8hjbCEG-jXEBqrzS&index=2',
'https://www.youtube.com/watch?v=tq0y5Vs-heI&list=PLfUV806q_Ri7wcsLO8hjbCEG-jXEBqrzS&index=3',
'https://www.youtube.com/watch?v=tq0y5Vs-heI&list=PLfUV806q_Ri7wcsLO8hjbCEG-jXEBqrzS&index=4',
'https://www.youtube.com/watch?v=tq0y5Vs-heI&list=PLfUV806q_Ri7wcsLO8hjbCEG-jXEBqrzS&index=5',
'https://www.youtube.com/watch?v=tq0y5Vs-heI&list=PLfUV806q_Ri7wcsLO8hjbCEG-jXEBqrzS&index=6',
'https://www.youtube.com/watch?v=tq0y5Vs-heI&list=PLfUV806q_Ri7wcsLO8hjbCEG-jXEBqrzS&index=7',
'https://www.youtube.com/watch?v=tq0y5Vs-heI&list=PLfUV806q_Ri7wcsLO8hjbCEG-jXEBqrzS&index=8',
'https://www.youtube.com/watch?v=tq0y5Vs-heI&list=PLfUV806q_Ri7wcsLO8hjbCEG-jXEBqrzS&index=9',
'https://www.youtube.com/watch?v=tq0y5Vs-heI&list=PLfUV806q_Ri7wcsLO8hjbCEG-jXEBqrzS&index=10',
'https://www.youtube.com/watch?v=tq0y5Vs-heI&list=PLfUV806q_Ri7wcsLO8hjbCEG-jXEBqrzS&index=11',
'https://www.youtube.com/watch?v=tq0y5Vs-heI&list=PLfUV806q_Ri7wcsLO8hjbCEG-jXEBqrzS&index=12'
]

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
    
    
