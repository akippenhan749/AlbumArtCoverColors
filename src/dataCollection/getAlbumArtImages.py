from PIL import Image
import json
import requests
import subprocess
import time

# Make requests to the Spotify API for 1000 albums in each of various genres and download the album art images for each

def getTracksFromGenre(genre, authToken):
    offset = 0
    data = {'records': []} # dictionary to append each request's records to
    for i in range(20): # need to do 20 requests to get 1000 records since individual requests are limited to 50 records
        print('Collecting data for genre: ' + genre + ' (request ' + str(i+1).zfill(2) + ' of 20)') # zfill() to format number to desired digits to increase output readability
        # make API request with provided authToken
        response = requests.get('https://api.spotify.com/v1/search?q='+genre+'&type=track&limit=50'+'&offset='+str(offset), headers={'Authorization':'Bearer '+authToken}, timeout=10).json()
        data['records'].append(response) # append this loop iteration's records
        offset += 50
    json.dump(data, open(genre+'/'+genre+'.json', 'w')) # dump data into json file
    print('Data collected for genre: ' + genre)

def downloadImagesFromGenre(genre):
    data = json.load(open(genre+'/'+genre+'.json')) # open json file for given genre
    failedURLs = [] # list to keep track of failed image download URLs to download manually later
    imgCount = 1
    downloadedImageNames = [] # list to keep track of image names to prevent duplicate images
    for i in range(20): # loop through each of 20 requests
        for j in range(50): # loop through each request's 50 records
            print('Downloading album art image for genre: ' + genre + ' (image ' + str(imgCount).zfill(4) + ' of 1000)')
            name = data['records'][i]['tracks']['items'][j]['album']['name'].replace(':', '\ua789').replace(' ', '').replace('/', '').replace('\\', '').replace('\'', '').replace('...', '') # remove characters that are not filename-friendly; '\ua789' is modifer letter colon
            if name in downloadedImageNames:
                print('Attempted to download duplicate image: \'' + name + '.jpg\'. Skipping this image')
                continue
            else:
                downloadedImageNames.append(name)
            try:
                Image.open(requests.get(data['records'][i]['tracks']['items'][j]['album']['images'][0]['URL'], stream=True, timeout=10).raw).save(genre+'/images/'+name+'.jpg') # save image to file with album name as filename
            except requests.exceptions.RequestException: # catch any requests exception
                failedURLs.append(data['records'][i]['tracks']['items'][j]['album']['images'][0]['URL']) # append to failedURLs list to report for downloading manually later
                print('requests.exceptions.RequestException occured while attempting to download to \'./' + genre + '/images/' + name + '.jpg\' from URL \'' + data['records'][i]['tracks']['items'][j]['album']['images'][0]['URL'] + '\'')
            imgCount += 1
    print('Album art images downloaded for genre: ' + genre + ' (Successfully downloaded ' + str((imgCount - 1) - len(failedURLs)) + ' of 1000 images)')
    return [failedURLs, (imgCount - 1) - len(failedURLs)] # return failed URLs and number of images successfully dowloaded as a list

t0 = time.time() # mark start time to record time elapsed

genres = ['alternative', 'country', 'hip-hop', 'jazz', 'pop', 'rock'] # list of desired genres

authToken = subprocess.run(['./getApiToken.sh'], stdout=subprocess.PIPE).stdout.decode('utf-8').replace('\n', '') # run 'getApiToken.sh' script to get fresh token from Spotify API

for genre in genres:
    getTracksFromGenre(genre, authToken)

failedURLs = [] # list to keep track of all failed URLs from all loop iterations
imagesDownloaded = [] # list to keep track of images downloaded successfully for each genre

for genre in genres:
    output = downloadImagesFromGenre(genre)
    genreFailedURLs = output[0]
    if genreFailedURLs:
        failedURLs.append(genreFailedURLs)
    imagesDownloaded.append(output[1])

t1 = time.time() # mark end time and report time elapsed in format hh:mm:ss

print('All album art image downloads have completed')
for i in range(len(genres)):
    print('Successfully downloaded ' + str(imagesDownloaded[i]).zfill(4) + ' of 1000 images for genre: ' + genres[i])

if len(failedURLs) > 0: # print all failed URLs from all loop iterations if any
    print('Album art images from the following URLs failed to download:')
    for failedURL in failedURLs:
        print(failedURL)

timeElapsed = (t1-t0)%(24*3600)
print('Total time elapsed: %02d:%02d:%02d' % (timeElapsed // 3600, timeElapsed // 60, timeElapsed % 60))