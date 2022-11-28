import glob
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import unidecode
import os  

# Defining empty data frame
data = pd.DataFrame(columns = ['Image Path','Pop','Hip Hop','Country','Jazz','Rock','Alternative'])

# Append pop
folder_dir = '/Users/johnhope/Desktop/GitHub/AlbumArtCoverColors/data/pop/images'
for image in glob.iglob(f'{folder_dir}/*'):
    
    data2 = {'Image Path': unidecode.unidecode(image), 'Pop':1, 'Hip Hop':0, 'Country':0, 'Jazz':0,
             'Rock':0, 'Alternative':0}
    data = data.append(data2, ignore_index = True)
    os.rename(image,unidecode.unidecode(image))
    
# Append hip hop
folder_dir = '/Users/johnhope/Desktop/GitHub/AlbumArtCoverColors/data/hip-hop/images'
for image in glob.iglob(f'{folder_dir}/*'):
    
    data2 = {'Image Path': unidecode.unidecode(image), 'Pop':0, 'Hip Hop':1, 'Country':0, 'Jazz':0,
             'Rock':0, 'Alternative':0}
    data = data.append(data2, ignore_index = True)
    os.rename(image,unidecode.unidecode(image))
    
# Append country
folder_dir = '/Users/johnhope/Desktop/GitHub/AlbumArtCoverColors/data/country/images'
for image in glob.iglob(f'{folder_dir}/*'):
    
    data2 = {'Image Path': unidecode.unidecode(image), 'Pop':0, 'Hip Hop':0, 'Country':1, 'Jazz':0,
             'Rock':0, 'Alternative':0}
    data = data.append(data2, ignore_index = True)
    os.rename(image,unidecode.unidecode(image))
    
# Append jazz
folder_dir = '/Users/johnhope/Desktop/GitHub/AlbumArtCoverColors/data/jazz/images'
for image in glob.iglob(f'{folder_dir}/*'):
    
    data2 = {'Image Path': unidecode.unidecode(image), 'Pop':0, 'Hip Hop':0, 'Country':0, 'Jazz':1,
             'Rock':0, 'Alternative':0}
    data = data.append(data2, ignore_index = True)
    os.rename(image,unidecode.unidecode(image))
    
# Append rock
folder_dir = '/Users/johnhope/Desktop/GitHub/AlbumArtCoverColors/data/rock/images'
for image in glob.iglob(f'{folder_dir}/*'):
    
    data2 = {'Image Path': unidecode.unidecode(image), 'Pop':0, 'Hip Hop':0, 'Country':0, 'Jazz':0,
             'Rock':1, 'Alternative':0}
    data = data.append(data2, ignore_index = True)
    os.rename(image,unidecode.unidecode(image))
    
# Append alt
folder_dir = '/Users/johnhope/Desktop/GitHub/AlbumArtCoverColors/data/alternative/images'
for image in glob.iglob(f'{folder_dir}/*'):
    
    data2 = {'Image Path': unidecode.unidecode(image), 'Pop':0, 'Hip Hop':0, 'Country':0, 'Jazz':0,
             'Rock':0, 'Alternative':1}
    data = data.append(data2, ignore_index = True)
    os.rename(image,unidecode.unidecode(image))

# Split data into training and testing
train = data.sample(frac=0.8, random_state=25)
test = data.drop(train.index)

# Write dataframes to csv format
data.to_csv('/Users/johnhope/Desktop/GitHub/AlbumArtCoverColors/data/classifiedData.csv',
            index=False)

train.to_csv('/Users/johnhope/Desktop/GitHub/AlbumArtCoverColors/data/trainingData.csv',
            index=False)

test.to_csv('/Users/johnhope/Desktop/GitHub/AlbumArtCoverColors/data/testingData.csv',
            index=False)
