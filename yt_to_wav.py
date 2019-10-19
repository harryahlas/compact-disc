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

os.mkdir('C:\\Users\\Anyone\\Music\\My Little Pony\\Movie Soundtrack')
#os.mkdir('C:\\Users\\Anyone\\Music\\Enslaved\\E')

os.chdir('C:\\Users\\Anyone\\Music\\My Little Pony\\Movie Soundtrack')

url_list = ['https://www.youtube.com/watch?v=BsS0bD83y1A&list=PLfc6_O5ggVzJkPKlM7AU0hye5tE-UMRy9',
'https://www.youtube.com/watch?v=ueU7NmVC3JQ&list=PLfc6_O5ggVzJkPKlM7AU0hye5tE-UMRy9&index=2',
'https://www.youtube.com/watch?v=ueU7NmVC3JQ&list=PLfc6_O5ggVzJkPKlM7AU0hye5tE-UMRy9&index=3',
'https://www.youtube.com/watch?v=ueU7NmVC3JQ&list=PLfc6_O5ggVzJkPKlM7AU0hye5tE-UMRy9&index=4',
'https://www.youtube.com/watch?v=ueU7NmVC3JQ&list=PLfc6_O5ggVzJkPKlM7AU0hye5tE-UMRy9&index=5',
'https://www.youtube.com/watch?v=ueU7NmVC3JQ&list=PLfc6_O5ggVzJkPKlM7AU0hye5tE-UMRy9&index=6',
'https://www.youtube.com/watch?v=ueU7NmVC3JQ&list=PLfc6_O5ggVzJkPKlM7AU0hye5tE-UMRy9&index=7',
'https://www.youtube.com/watch?v=ueU7NmVC3JQ&list=PLfc6_O5ggVzJkPKlM7AU0hye5tE-UMRy9&index=8',
'https://www.youtube.com/watch?v=ueU7NmVC3JQ&list=PLfc6_O5ggVzJkPKlM7AU0hye5tE-UMRy9&index=9',
'https://www.youtube.com/watch?v=ueU7NmVC3JQ&list=PLfc6_O5ggVzJkPKlM7AU0hye5tE-UMRy9&index=10',
'https://www.youtube.com/watch?v=ueU7NmVC3JQ&list=PLfc6_O5ggVzJkPKlM7AU0hye5tE-UMRy9&index=11',
'https://www.youtube.com/watch?v=ueU7NmVC3JQ&list=PLfc6_O5ggVzJkPKlM7AU0hye5tE-UMRy9&index=12',
'https://www.youtube.com/watch?v=ueU7NmVC3JQ&list=PLfc6_O5ggVzJkPKlM7AU0hye5tE-UMRy9&index=13',
'https://www.youtube.com/watch?v=ueU7NmVC3JQ&list=PLfc6_O5ggVzJkPKlM7AU0hye5tE-UMRy9&index=14']


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
    
    
