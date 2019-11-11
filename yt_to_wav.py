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

os.mkdir('C:\\Users\\Anyone\\Music\\Blind Guardian')
os.mkdir('C:\\Users\\Anyone\\Music\\Blind Guardian\\Legacy of the Dark Lands')
#os.mkdir('C:\\Users\\Anyone\\Music\\Enslaved\\E')

os.chdir('C:\\Users\\Anyone\\Music\\Blind Guardian\\Legacy of the Dark Lands')

url_list = ['https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=1',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=2',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=3',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=4',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=5',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=6',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=7',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=8',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=9',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=10',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=11',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=12',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=13',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=14',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=15',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=16',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=17',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=18',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=19',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=20',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=21',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=22',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=23',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=24',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=25',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=26',
'https://www.youtube.com/watch?v=MnRT2uukgZk&list=PLddSkUxmPEC9pIdW125q0Ivv5d2p6uzmD&index=27']


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
    
    
