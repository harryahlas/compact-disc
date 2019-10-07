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

os.chdir('C:\\Users\\Anyone\\Music\\Enslaved\\E')

url_list = ['https://www.youtube.com/watch?v=Y8HX_vGPCz8&list=OLAK5uy_noFAGW-89cd1HrRCnBFYrufZxuB7UUu6g&index=1',
'https://www.youtube.com/watch?v=Y8HX_vGPCz8&list=OLAK5uy_noFAGW-89cd1HrRCnBFYrufZxuB7UUu6g&index=2',
'https://www.youtube.com/watch?v=Y8HX_vGPCz8&list=OLAK5uy_noFAGW-89cd1HrRCnBFYrufZxuB7UUu6g&index=3',
'https://www.youtube.com/watch?v=Y8HX_vGPCz8&list=OLAK5uy_noFAGW-89cd1HrRCnBFYrufZxuB7UUu6g&index=4',
'https://www.youtube.com/watch?v=Y8HX_vGPCz8&list=OLAK5uy_noFAGW-89cd1HrRCnBFYrufZxuB7UUu6g&index=5',
'https://www.youtube.com/watch?v=Y8HX_vGPCz8&list=OLAK5uy_noFAGW-89cd1HrRCnBFYrufZxuB7UUu6g&index=6',
'https://www.youtube.com/watch?v=Y8HX_vGPCz8&list=OLAK5uy_noFAGW-89cd1HrRCnBFYrufZxuB7UUu6g&index=7',
'https://www.youtube.com/watch?v=Y8HX_vGPCz8&list=OLAK5uy_noFAGW-89cd1HrRCnBFYrufZxuB7UUu6g&index=8']

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
    
    
#### Automata I
os.mkdir('C:\\Users\\Anyone\\Music\\Between the Buried and Me\\')
os.mkdir('C:\\Users\\Anyone\\Music\\Between the Buried and Me\\Automata I')

os.chdir('C:\\Users\\Anyone\\Music\\Between the Buried and Me\\Automata I')

url_list = ['https://www.youtube.com/watch?v=kPU9YTN-faQ&list=OLAK5uy_nujrpDLn0uRH01q9YEHfFVt4IQIoWD4u8&index=1',
'https://www.youtube.com/watch?v=kPU9YTN-faQ&list=OLAK5uy_nujrpDLn0uRH01q9YEHfFVt4IQIoWD4u8&index=2',
'https://www.youtube.com/watch?v=kPU9YTN-faQ&list=OLAK5uy_nujrpDLn0uRH01q9YEHfFVt4IQIoWD4u8&index=3',
'https://www.youtube.com/watch?v=kPU9YTN-faQ&list=OLAK5uy_nujrpDLn0uRH01q9YEHfFVt4IQIoWD4u8&index=4',
'https://www.youtube.com/watch?v=kPU9YTN-faQ&list=OLAK5uy_nujrpDLn0uRH01q9YEHfFVt4IQIoWD4u8&index=5',
'https://www.youtube.com/watch?v=kPU9YTN-faQ&list=OLAK5uy_nujrpDLn0uRH01q9YEHfFVt4IQIoWD4u8&index=6']
      
for url in url_list:
    download_youtube_music(url)     
    
    
#### Automata II
#os.mkdir('C:\\Users\\Anyone\\Music\\Between the Buried and Me\\')
os.mkdir('C:\\Users\\Anyone\\Music\\Between the Buried and Me\\Automata II')
os.chdir('C:\\Users\\Anyone\\Music\\Between the Buried and Me\\Automata II')

url_list = ['https://www.youtube.com/watch?v=7W8u1IFK7Y8&list=PLHJQ__I7nFk9XJ-9p4LVWrG4BcCqyL0Ig&index=7',
'https://www.youtube.com/watch?v=7W8u1IFK7Y8&list=PLHJQ__I7nFk9XJ-9p4LVWrG4BcCqyL0Ig&index=8',
'https://www.youtube.com/watch?v=7W8u1IFK7Y8&list=PLHJQ__I7nFk9XJ-9p4LVWrG4BcCqyL0Ig&index=9',
'https://www.youtube.com/watch?v=7W8u1IFK7Y8&list=PLHJQ__I7nFk9XJ-9p4LVWrG4BcCqyL0Ig&index=10']
      
for url in url_list:
    download_youtube_music(url)     
    
   
#### Exhorder Topic
os.mkdir('C:\\Users\\Anyone\\Music\\Exhorder')
os.mkdir('C:\\Users\\Anyone\\Music\\Exhorder\\Topic')
os.chdir('C:\\Users\\Anyone\\Music\\Exhorder\\Topic')

url_list = ['https://www.youtube.com/watch?v=QezU673nHhk&list=OLAK5uy_l7fA0T2vfnBu6j3B5WO0tAjAwS7fparcM&index=1',
'https://www.youtube.com/watch?v=QezU673nHhk&list=OLAK5uy_l7fA0T2vfnBu6j3B5WO0tAjAwS7fparcM&index=1',
'https://www.youtube.com/watch?v=QezU673nHhk&list=OLAK5uy_l7fA0T2vfnBu6j3B5WO0tAjAwS7fparcM&index=1',
'https://www.youtube.com/watch?v=QezU673nHhk&list=OLAK5uy_l7fA0T2vfnBu6j3B5WO0tAjAwS7fparcM&index=1',
'https://www.youtube.com/watch?v=QezU673nHhk&list=OLAK5uy_l7fA0T2vfnBu6j3B5WO0tAjAwS7fparcM&index=1',
'https://www.youtube.com/watch?v=QezU673nHhk&list=OLAK5uy_l7fA0T2vfnBu6j3B5WO0tAjAwS7fparcM&index=1',
'https://www.youtube.com/watch?v=QezU673nHhk&list=OLAK5uy_l7fA0T2vfnBu6j3B5WO0tAjAwS7fparcM&index=1',
'https://www.youtube.com/watch?v=QezU673nHhk&list=OLAK5uy_l7fA0T2vfnBu6j3B5WO0tAjAwS7fparcM&index=1',
'https://www.youtube.com/watch?v=QezU673nHhk&list=OLAK5uy_l7fA0T2vfnBu6j3B5WO0tAjAwS7fparcM&index=1',
'https://www.youtube.com/watch?v=QezU673nHhk&list=OLAK5uy_l7fA0T2vfnBu6j3B5WO0tAjAwS7fparcM&index=1']
      
for url in url_list:
    download_youtube_music(url)     
    
    