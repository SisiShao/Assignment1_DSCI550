# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
import requests
import pandas as pd
import json


# %%
APIKEY = open('GoogleAPIKey.txt').read()


# %%
def get_image(Address,satellite=False):
    url = 'https://maps.googleapis.com/maps/api/staticmap'
    params = {
        'key':APIKEY,
        'center':Address,
        'zoom':16,
        'size':'800x800',
        'maptype':'satellite' if satellite else 'roadmap',
    }
    headers = {
    }
    r = requests.get(url, params=params,headers=headers)
    r.raise_for_status()
    temp = r.content
    folder = 'satellite_view' if satellite else 'roadmap_view'
    with open(f'../{folder}/{Address.strip()}.png','wb') as file:
        file.write(temp)




# %%
import cv2
import numpy as np

def count_water(img):
    count=0
    for row in img:
        for pixel in row:
            try:
                if (pixel == [255,218,170]).all():
                    count+=1
            except:
                print(pixel)
                print(pixel== [255,218,170])

    return count >= 25000

def count_park(img):
    count=0
    for row in img:
        for pixel in row:
            try:
                if (pixel == [197,232,197]).all():
                    count+=1
            except:
                print(pixel)
                print(pixel== [255,218,170])
                
    return count >= 40000

def get_green_pct(re_img1):
    b, g, r = cv2.split(re_img1)

    ttl = re_img1.size / 3 #divide by 3 to get the number of image PIXELS

    """b, g, and r are actually numpy.ndarray types,
    so you need to use the appropriate method to sum
    all array elements"""
    B = float(np.sum(b)) / ttl #convert to float, as B, G, and R will otherwise be int
    G = float(np.sum(g)) / ttl
    R = float(np.sum(r)) / ttl
    return '{:.2%}'.format(G/(R+G+B))
