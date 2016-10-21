# Neuro

![Genius logo](http://assets.rapgenius.com/images/apple-touch-icon.png?1432674944)

**This project was done in fullfillment of the application process for Andela Cohort 10**

## Introduction
**`Neuro`** is A Command Line Application for Finding Lyrics for a particular song using [Rap Genius API](http://genius.com/developers)

## Installation

1. First git clone this project at `https://github.com/FawazFarid`

2. Navigate to the `bc-10-neuro` folder.

3. Create a virtual environment using the `virtualenv` command and activate it.

4. Install the requirements via `pip install -r requirements.txt`

5. Run the application in your terminal via `python app.py`

## Usage
The required commands for the application were:

Command| Argument| Explanation
--- | --- | ---
|`song find`| `<search_query_string>` | Returns a list of songs that match the criteria.
|`song view ` | `<song_id>`| View song lyrics based on it’s id. Optimized by checking if there’s a local copy before checking online.
|`song save`| None | Store song details and lyrics locally.
|`song clear`| None | Clear entire local song database.

### Authentication

You'll need to set your access token before using the library. You can create a client and grab an access token from
<http://genius.com/api-clients>. You can then use that like so:

``` python
'Authorization': 'Bearer  your-access-token'
```

At the moment, this library isn't set up for a traditional multi-user OAuth setup - despite the Genius API being [based](https://docs.genius.com/#/authentication-h1) on OAuth. It's built for the use case of just accessing the API with your account. This may change in future.
