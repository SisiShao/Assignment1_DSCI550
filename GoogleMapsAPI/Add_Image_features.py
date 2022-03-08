# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
import tika
import pandas as pd
import json
import ast
from AlvinGoogleAPI import *
pd.set_option('display.max_columns', None)


# %%
# df = pd.read_csv("../data/Bik dataset - papers with endpoint reached.tsv", sep='\t', encoding = "ISO-8859-1")
# df = df.dropna(subset=['Authors'])
# df.to_csv('../data/Bik dataset.csv',index=False)
# df.shape


# %%
df = pd.read_csv('../data/sisi.csv')


# %%
df.head()


# %%
found = {}
many = set()
failedgreen = set()
failednear = set()


# %%

for index,row in df.iterrows():
    institution_info = row['institution_info']
    
    if type(institution_info) == str:
        try:
            institution_info = ast.literal_eval(institution_info)
            if len(institution_info) ==1:
                institution_info = institution_info[0].split(',')
            else:
                setdata = set(institution_info)
                temp = []
                for i in setdata:
                    temp = temp + i.split(',')
                institution_info = temp
        except:
            institution_info = institution_info.split(',')

    institutions = []
    for institution in institution_info:
        institution = institution.lower().strip()
        if not ('university' in institution or 'college' in institution):
            continue

        institutions.append(institution)

    if len(institutions) == 0:
        df.at[0,'GreenPct'] = 'NA'
        df.at[0,'NearBodyOfWater'] = 'NA'
        continue

    if len(institutions) > 1:
        many.add(i)

    institution = institutions[0]
    if institution in found:
        green, near = found[institution]
    else:
        try:
            # get_image(institution, satellite=True)
            img = cv2.imread(f"satellite_view/{institution}.png")
            green = get_green_pct(img)
        except Exception as e:
            print('sat error', e)
            green = 'NA'
            failedgreen.add(institution)

        try:
            # get_image(institution)
            img = cv2.imread(f"roadmap_view/{institution}.png")
            near = count_water(img)
        except Exception as e:
            print('roadmap error',e)
            near = 'NA'
            failednear.add(institution)

        found[institution] = [green,near]
    # print(index, institution,green,near)

    df.at[index,'University'] = institution
    df.at[index,'GreenPct'] = green
    df.at[index,'NearBodyOfWater'] = near


# %%
df.to_csv('../data/Tiger dataset.csv',index=False)


# %%
df = pd.read_csv('../data/Tiger dataset.csv')
found = {}


# %%
df.head(2)


# %%
for index,row in df.iterrows():
    try:
        institution = row['University'].lower()
    except:
        continue
    
    if institution in found:
        parks = found[institution]
    else:
        try:
            # get_image(institution)
            img = cv2.imread(f"roadmap_view/{institution}.png")
            parks = count_park(img)
        except Exception as e:
            print(index, 'roadmap error',e)
            parks='NA'
        found[institution] = parks
    df.at[index,'NearParks'] = parks


# %%
df.to_csv('Tiger dataset.csv',index=False)


