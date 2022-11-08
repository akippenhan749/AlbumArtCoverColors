# Album Art Cover Colors and Genre

(This project is a work in progress and as such this repository is not complete)

## Repository Contents

This repository contains code, data and figures for a data science project investigating colors in album art covers and their relation to different genres. This project was created as part of the Data Science Project Course (DS 4002) at the University of Virginia in the Fall of 2022.

## Source Code

### Installing/Building Code in this Repository

After cloning or forking this repository, its contents can be used to recreate different parts of this project. A Spotify developer account is required to access the Spotify API and recreate the data collection portion of this project. Additionally, the Python modules used in this project are listed below.

### Modules Used in this Project

#### Python Modules

This project makes use of the following Python modules:
- `PIL.Image` - to write album art images to files
- `json` - to manage json data files
- `requests` - to make API requests to the Spotify API and download images
- `subprocess` - to run shell script to generate API token
- `time` - to record code execution time

### Usage of Code in this Repository

(This section is currently empty)

## Data

The data for this project was collected using the Spotify API. Data for 6 different genres was collected using Python. For each genre, 20 queries were made with each containing 50 records to reach Spotify's maximum limit of 1000 records. The results from the API requests are in JSON format in the directory corresponding to the genre name in the `data` folder of this repository. The album art images that were downloaded from these request responses can be found in the `images` folder of each genre in the `data` folder of this repository. The number of images varies for each genre as many of the image URLS provide in the request responses were duplicates. A list of the collected genres and their corresponding JSON data file can be found below. Note that the data for this project was collected using the Spotify API, which requires a Spotify developer account.

- Alternative - `alternative.json` [(src)](data/alternative/alternative.json)
- Country - `country.json` [(src)](data/country/country.json)
- Hip-hop - `hip-hop.json` [(src)](data/hip-hop/hip-hop.json)
- Jazz - `jazz.json` [(src)](data/jazz/jazz.json)
- Pop - `pop.json` [(src)](data/pop/pop.json)
- Rock - `rock.json` [(src)](data/rock/rock.json)

### Data Dictionary

There are several data dictionaries included here as some items are arrays. The first data dictionary is key labelled `items` in each JSON data file (labeled and each consecutive data dictionary is for each array included in the first data dictionary. For each array corresponding to a separate data dictionary, the Example column includes a link to that data dictionary in this README. Additionally, an example for the `available_markets` value is included separately below the data dictionaries to preserve table formatting and can be accessed via the link in the Example column.

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
| album_type | The type of album. Allowed values: "album", "single", "compilation". | "album" |
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

##### `artists `

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

## Figures

Figures for this project can be found in the `figures` folder of this repository.

### Table of Contents

| Figure Name | Variables | Summary |
|-------------|-----------|---------|

## References


Files documenting the previous 2 milestones of this project can be found in the `milestones` folder of this repository in `M1Hypothesis.pdf` ([src](milestones/MI1Hypothesis.pdf)) and `MI2EstablishDataAndAnalysisPlan.pdf` ([src](milestones/MI2EstablishDataAndAnalysisPlan.pdf)).
