import requests
import pandas as pd
import csv
import json
import os
from colorthief import ColorThief
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import webcolors as wc
import glob


R = []
G = []
B = []
Color = []

folder_dir = '/Users/johnhope/Desktop/GitHub/AlbumArtCoverColors/data/pop/images'
for image in glob.iglob(f'{folder_dir}/*'):
   
    if len(R) >= 50:
        break
    
    # check if the image ends with png
    if (image.endswith(".jpg")):
        color_thief = ColorThief(image)
        dom = color_thief.get_color(quality=1)
        R.append(dom[0])
        G.append(dom[1])
        B.append(dom[2])
        Color.append(wc.rgb_to_hex(dom))

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection='3d')
ax.scatter(xs=R,ys=G,zs=B, color = Color, s=200)
plt.title('Pop', size=50)
ax.set_xlabel('R', size = 20)
ax.set_ylabel('G', size = 20)
ax.set_zlabel('B', size = 20)
plt.show()

####

R = []
G = []
B = []
Color = []

folder_dir = '/Users/johnhope/Desktop/GitHub/AlbumArtCoverColors/data/hip-hop/images'
for image in glob.iglob(f'{folder_dir}/*'):
   
    if len(R) >= 50:
        break
    
    # check if the image ends with png
    if (image.endswith(".jpg")):
        color_thief = ColorThief(image)
        dom = color_thief.get_color(quality=1)
        R.append(dom[0])
        G.append(dom[1])
        B.append(dom[2])
        Color.append(wc.rgb_to_hex(dom))

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection='3d')
ax.scatter(xs=R,ys=G,zs=B, color = Color, s=200)
plt.title('Hip-Hop', size=50)
ax.set_xlabel('R', size = 20)
ax.set_ylabel('G', size = 20)
ax.set_zlabel('B', size = 20)
plt.show()

####

R = []
G = []
B = []
Color = []

folder_dir = '/Users/johnhope/Desktop/GitHub/AlbumArtCoverColors/data/country/images'
for image in glob.iglob(f'{folder_dir}/*'):
   
    if len(R) >= 50:
        break
    
    # check if the image ends with png
    if (image.endswith(".jpg")):
        color_thief = ColorThief(image)
        dom = color_thief.get_color(quality=1)
        R.append(dom[0])
        G.append(dom[1])
        B.append(dom[2])
        Color.append(wc.rgb_to_hex(dom))

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection='3d')
ax.scatter(xs=R,ys=G,zs=B, color = Color, s=200)
plt.title('Country', size=50)
ax.set_xlabel('R', size = 20)
ax.set_ylabel('G', size = 20)
ax.set_zlabel('B', size = 20)
plt.show()

####

R = []
G = []
B = []
Color = []

folder_dir = '/Users/johnhope/Desktop/GitHub/AlbumArtCoverColors/data/rock/images'
for image in glob.iglob(f'{folder_dir}/*'):
   
    if len(R) >= 50:
        break
    
    # check if the image ends with png
    if (image.endswith(".jpg")):
        color_thief = ColorThief(image)
        dom = color_thief.get_color(quality=1)
        R.append(dom[0])
        G.append(dom[1])
        B.append(dom[2])
        Color.append(wc.rgb_to_hex(dom))

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection='3d')
ax.scatter(xs=R,ys=G,zs=B, color = Color, s=200)
plt.title('Rock', size=50)
ax.set_xlabel('R', size = 20)
ax.set_ylabel('G', size = 20)
ax.set_zlabel('B', size = 20)
plt.show()

####

R = []
G = []
B = []
Color = []

folder_dir = '/Users/johnhope/Desktop/GitHub/AlbumArtCoverColors/data/jazz/images'
for image in glob.iglob(f'{folder_dir}/*'):
   
    if len(R) >= 50:
        break
    
    # check if the image ends with png
    if (image.endswith(".jpg")):
        color_thief = ColorThief(image)
        dom = color_thief.get_color(quality=1)
        R.append(dom[0])
        G.append(dom[1])
        B.append(dom[2])
        Color.append(wc.rgb_to_hex(dom))

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection='3d')
ax.scatter(xs=R,ys=G,zs=B, color = Color, s=200)
plt.title('Jazz', size=50)
ax.set_xlabel('R', size = 20)
ax.set_ylabel('G', size = 20)
ax.set_zlabel('B', size = 20)
plt.show()

####

R = []
G = []
B = []
Color = []

folder_dir = '/Users/johnhope/Desktop/GitHub/AlbumArtCoverColors/data/alternative/images'
for image in glob.iglob(f'{folder_dir}/*'):
   
    if len(R) >= 50:
        break
    
    # check if the image ends with png
    if (image.endswith(".jpg")):
        color_thief = ColorThief(image)
        dom = color_thief.get_color(quality=1)
        R.append(dom[0])
        G.append(dom[1])
        B.append(dom[2])
        Color.append(wc.rgb_to_hex(dom))

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection='3d')
ax.scatter(xs=R,ys=G,zs=B, color = Color, s=200)
plt.title('Alternative', size=50)
ax.set_xlabel('R', size = 20)
ax.set_ylabel('G', size = 20)
ax.set_zlabel('B', size = 20)
plt.show()