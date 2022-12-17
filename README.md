# Album Art Cover Colors and Genre

## Repository Contents

This repository contains code, data and figures for a data science project investigating colors in album art covers and their relation to different genres using a convolutional neural network (CNN) machine learning model. This project was created as part of the Data Science Project Course (DS 4002) at the University of Virginia in the Fall of 2022.

## Source Code

### Installing/Building Code in this Repository

After cloning or forking this repository, its contents can be used to recreate different parts of this project. A Spotify developer account is required to access the Spotify API and recreate the data collection portion of this project. Additionally, the Python modules used in this project are listed below.

### Modules Used in this Project

#### Python Modules

This project makes use of the following Python modules:
- `colorthief` - to record predominant color of an image
- `glob` - to read image files across desktop folder
- `json` - to manage json data files
- `keras` - to create the CNN model
- `matplotlib.pyplot` - to create visuals
- `numpy` - to arrange data for modeling prediction
- `pandas` - to manipulate data
- `PIL.Image` - to write album art images to files
- `requests` - to make API requests to the Spotify API and download images
- `sklearn` - to split data for modeling
- `subprocess` - to run shell script to generate API token
- `tensorflow` - to access the keras API
- `time` - to record code execution time
- `tqdm` - to assist data arrangement for modeling
- `webcolors` - to convert RGB values to colors

### Usage of Code in this Repository

#### Data Collection

The main file for the code used to collect the data for this project is located in `getAlbumArtImages.py` ([src](src/dataCollection/getAlbumArtImages.py)). The code first runs the bash shell script `getApiToken.sh` ([src](src/dataCollection/getApiToken.sh)) to get the Spotify API authentication token before making the API queries necessary to collect the JSON containing links to the album art images. It then iterates through the JSON data and downloads every unique album art image for each genre from the relevant link, placing each image in the folder corresponding to its genre.

#### Exploratory Data Analysis

The file `predominantColorVisual.py` ([src](src/exploratoryDataAnalysis/predominantColorVisual.py)) reads certain images into Python, finds the predominant color of the image and subsequently visualizes the RGB values and colors for the different genres in three-dimensional scatterplots.

#### Modeling

The code contained in `dataClassification.py` ([src](src/modeling/dataClassification.py)) classifies the images into each genre and splits the data into training and testing datasets to use for the CNN model. Testing of the model with the test dataset is then performed in `testModel.ipynb` ([src](src/modeling/testModel.ipynb)) and training using the training dataset is done in `trainModel.ipynb` ([src](src/modeling/trainModel.ipynb)).

## Data

The data for this project was collected using the Spotify API. Data for 6 different genres was collected using Python. For each genre, 20 queries were made with each containing 50 records to reach Spotify's maximum limit of 1000 records. The results from the API requests are in JSON format in the folder corresponding to the genre name in the `data` folder of this repository. The 3184 total album art images that were downloaded from these request responses can be found in the `images` folder of each genre in the `data` folder of this repository. The number of images varies for each genre as many of the image URLS provided in the request responses were duplicates. A list of the collected genres and their corresponding JSON data file can be found below. Note that the data for this project was collected using the Spotify API, which requires a Spotify developer account.

- Alternative - `alternative.json` ([src](data/alternative/alternative.json))
- Country - `country.json` ([src](data/country/country.json))
- Hip-hop - `hip-hop.json` ([src](data/hip-hop/hip-hop.json))
- Jazz - `jazz.json` ([src](data/jazz/jazz.json))
- Pop - `pop.json` ([src](data/pop/pop.json))
- Rock - `rock.json` ([src](data/rock/rock.json))

### Data Dictionary

There are several data dictionaries included here as some items in the JSON data are arrays. The first data dictionary is for the key labeled `items` in each JSON data file and the next are for each array included in the first data dictionary. For each array corresponding to a separate data dictionary, the Example column includes a link to that data dictionary in this README. Additionally, an example for the `available_markets` value is included separately below the data dictionaries to preserve table formatting and can be accessed via the link in the Example column of the corresponding data dictionary.

| Value | Data Type | Description | Example |
|-------|-----------|-------------|---------|
| album | array of objects | A set of albums | see [album section](#album) |
| artists | array of objects | The artists of the album. Each artist object includes a link in href to more detailed information about the artist. | see [artists section](#artists) |
available_markets | array of strings | The markets in which the album is available: ISO 3166-1 alpha-2 country codes. NOTE: an album is considered available in a market when at least 1 of its tracks is available in that market. | see [example of available_markets array](#example-of-available_markets-array) |
disc_number | integer | The disc number (usually 1 unless the album consists of more than one disc). | 1 |
duration_ms | integer | The track length in milliseconds. | 163880 |
explicit | boolean | Whether or not the track has explicit lyrics (true = yes it does; false = no it does not OR unknown). | false |
external_ids | object | Known external IDs for the track. | "isrc": "GB01A0700157" |
external_urls | object | Known external URLs for this track. | "spotify": "https://open.spotify.com/track/2yE3bwbhqypdsuhmv48Svn" |
href | string | A link to the Web API endpoint providing full details of the track. | "https://api.spotify.com/v1/tracks/2yE3bwbhqypdsuhmv48Svn" |
id | string | The Spotify ID for the track. | "2yE3bwbhqypdsuhmv48Svn" |
is_local | boolean | Whether or not the track is from a local file. | false |
name | string | The name of the track. | "Alternative Ulster" |
popularity | integer | The popularity of the track. The value will be between 0 and 100, with 100 being the most popular. | 54 |
preview_url | string | A link to a 30 second preview (MP3 format) of the track. | "https://p.scdn.co/mp3-preview/794d7815a0e57839211a52783d278b39918ac4d4?cid=d803d7f0719c4e7e833291c8b7ded5fd" |
track_number | integer | The number of the track. If an album has several discs, the track number is the number on the specified disc. | 12 |
type | string | The object type. | "track" |
uri | string | The Spotify URI for the track. | "spotify:track:2yE3bwbhqypdsuhmv48Svn" |

##### `album`

| Value | Data Type | Description | Example |
|-------|-----------|-------------|---------|
| album_type | string | The type of album. Allowed values: "album", "single", "compilation". | "album" |
| artists | array of objects | The artists of the album. | see [artists section](#artists) |
| available_markets | array of strings | The markets in which the album is available: ISO 3166-1 alpha-2 country codes. NOTE: an album is considered available in a market when at least 1 of its tracks is available in that market. | see [example of available_markets array](#example-of-available_markets-array) |
| external_urls | object | Known external URLs for this album. | "spotify": "https://open.spotify.com/album/2uXYm7SqdQlOgrx2FEWlkD" |
| href | string | A link to the Web API endpoint providing full details of the album. | "https://api.spotify.com/v1/albums/2uXYm7SqdQlOgrx2FEWlkD" |
| id | string | The Spotify ID for the album. | "2uXYm7SqdQlOgrx2FEWlkD" |
| images | array of objects | The cover art for the album in various sizes, widest first. | see [images section](#images) |
| name | string | The name of the album. | "Inflammable Material" |
| release_date | string | The date the album was first released. | "1979" |
| release_date_precision | string | The precision with which release_date value is known. | "year" |
| total_tracks | integer | The number of tracks in the album. | 16 |
| type | string | The object type. | "album" |
| uri | string | The Spotify URI for the album. | "spotify:album:2uXYm7SqdQlOgrx2FEWlkD" |

##### `images`

| Value | Data Type | Description | Example |
|-------|-----------|-------------|---------|
| height | integer | The image height in pixels. | 640 |
| url | string | The source URL of the image. | "https://i.scdn.co/image/ab67616d0000b273466cbdbfa0f61e469beca2a1" |
| width | integer | The image width in pixels. | 640 |

##### `artists`

| Value | Data Type | Description | Example |
|-------|-----------|-------------|---------|
| external_urls | object | Known external URLs for this artist. | "spotify": "https://open.spotify.com/artist/2bt3I0VkmYuPvP57sxokab" |
| href | string | A link to the Web API endpoint providing full details of the artist. | "https://api.spotify.com/v1/artists/2bt3I0VkmYuPvP57sxokab" |
| id | string | The Spotify ID for the artist. | "2bt3I0VkmYuPvP57sxokab" |
| name | string | The name of the artist. | "Stiff Little Fingers" |
| type | string | The object type. | "artist" |
| uri | string | The Spotify URI for the artist. | "spotify:<zero-width space>artist:2bt3I0VkmYuPvP57sxokab" |

##### Example of `available_markets` Array

["AD", "AE", "AG", "AL", "AM", "AO", "AR", "AT", "AU", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BN", "BO", "BR", "BS", "BT", "BW", "BY", "BZ", "CA", "CD", "CG", "CH", "CI", "CL", "CM", "CO", "CR", "CV", "CW", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "ES", "FI", "FJ", "FM", "FR", "GA", "GB", "GD", "GE", "GH", "GM", "GN", "GQ", "GR", "GT", "GW", "GY", "HK", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IN", "IQ", "IS", "IT", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KR", "KW", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MG", "MH", "MK", "ML", "MN", "MO", "MR", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NE", "NG", "NI", "NL", "NO", "NP", "NR", "NZ", "OM", "PA", "PE", "PG", "PH", "PK", "PL", "PS", "PT", "PW", "PY", "QA", "RO", "RS", "RW", "SA", "SB", "SC", "SE", "SG", "SI", "SK", "SL", "SM", "SN", "SR", "ST", "SV", "SZ", "TD", "TG", "TH", "TJ", "TL", "TN", "TO", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "US", "UY", "UZ", "VC", "VE", "VN", "VU", "WS", "XK", "ZA", "ZM", "ZW"]

##### Example of Album Art Image

This is an example of an album art image for artist Stiff Little Fingers' album *Inflammable Material* from the examples in the data dictionary above.

![InflammableMaterial.jpg](data/alternative/images/InflammableMaterial.jpg)

## Figures

Figures for this project can be found in the `figures` folder of this repository.

### Table of Contents

| Figure Name | Variables | Summary |
|-------------|-----------|---------|
| Accuracy Bar Graph ([src](figures/AccuracyPlot.png)) | x = Genre, y = Test Accuracy | A two-dimensional bar graph showing the test accuracy of the CNN model by genre. |
| Alternative 3D Scatterplot ([src](figures/alternativeScatterplot.jpg)) | x = R, y = G, z = B | A three-dimensional scatterplot showing the predominant color distribution of select album art images in the alternative genre. The three axes represent the color values red, green and blue. |
| Country 3D Scatterplot ([src](figures/countryScatterplot.jpg)) | x = R, y = G, z = B | A three-dimensional scatterplot showing the predominant color distribution of select album art images in the country genre. The three axes represent the color values red, green and blue. |
| Jazz 3D Scatterplot ([src](figures/jazzScatterplot.jpg)) | x = R, y = G, z = B | A three-dimensional scatterplot showing the predominant color distribution of select album art images in the jazz genre. The three axes represent the color values red, green and blue. |
| Hip-Hop 3D Scatterplot ([src](figures/hip-hopScatterplot.jpg)) | x = R, y = G, z = B | A three-dimensional scatterplot showing the predominant color distribution of select album art images in the hip-hop genre. The three axes represent the color values red, green and blue. |
| Pop 3D Scatterplot ([src](figures/popScatterplot.jpg)) | x = R, y = G, z = B | A three-dimensional scatterplot showing the predominant color distribution of select album art images in the pop genre. The three axes represent the color values red, green and blue. |
| Rock 3D Scatterplot ([src](figures/rockScatterplot.jpg)) | x = R, y = G, z = B | A three-dimensional scatterplot showing the predominant color distribution of select album art images in the rock genre. The three axes represent the color values red, green and blue. |

## References

[1]	E. Pereira, “Judge an Album by its Colours,” AlbumCoverZone, Oct. 28, 2020. [Online]. Available: https://albumcoverzone.com/blog/judge-an-album-by-its-colour. [Accessed Nov. 2, 2022].

[2]	B. Milano, “Can You Judge An Album By Its Cover? How Artwork Reflects The Music,” UDiscoveryMusic. Sept. 20, 2022. [Online]. Available: https://www.udiscovermusic.com/stories/can-you-judge-an-album-by-its-cover/. [Accessed Nov. 2, 2022].

[3]	G. Smith, “Why is Every Music Poster Orange and Blue,” OBSEV. [Online]. Available: https://www.obsev.com/entertainment/orange-and-blue-movie-posters/. [Accessed Nov. 2, 2022].

[4]	G. Barney and K. Kaya, “Predicting Genre from Movie Posters,” Stanford University. [Online]. Available: https://cs229.stanford.edu/proj2019spr/report/9.pdf. [Accessed Nov. 2, 2022].

[5]	R. Chokshi and S. Sung, “Classification of Movie Posters to Movie Genres,” Stanford University. [Online]. Available: http://cs230.stanford.edu/projects_winter_2020/reports/32643471.pdf. [Accessed Nov. 2, 2022].

[6]	L. Dhakar, “Color Thief,” Color thief. [Online]. Available: https://lokeshdhakar.com/projects/color-thief/. [Accessed: Nov. 9, 2022].

[7] F. Lima, "Convolutional Neural Networks in R," R-bloggers. [Online]. Available: https://www.r-bloggers.com/2018/07/convolutional-neural-networks-in-r/. [Accessed: Nov. 16, 2022].

##

Files documenting the previous 2 milestones of this project can be found in the `milestones` folder of this repository in `M1Hypothesis.pdf` ([src](milestones/MI1Hypothesis.pdf)) and `MI2EstablishDataAndAnalysisPlan.pdf` ([src](milestones/MI2EstablishDataAndAnalysisPlan.pdf)).