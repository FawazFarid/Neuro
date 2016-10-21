# Neuro

![Genius logo](http://assets.rapgenius.com/images/apple-touch-icon.png?1432674944)

**This project was done in fullfillment of the application process for Andela Cohort 10**

## Introduction
**`Neuro`** is A Command Line Application for Finding Lyrics for a particular song using [Rap Genius API](http://genius.com/developers)

### Back End Dependencies
*  This app's functionality depends on multiple Python packages including;
  *  **[Click](http://www.click.pocoo.org)** - Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary
  *  **[SQLAlchemy ORM](http://docs.sqlalchemy.org/en/latest/orm/)** - This is a powerful and flexible database abstraction layer and object relational mapper that presents a method of associating user-defined Python classes with database tables, and instances of those classes (objects) with rows in their corresponding tables
  *  **[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)** - Beautiful Soup is a Python library for Scraping/pulling data out of HTML and XML files

## Installation

1. First git clone this project at `https://github.com/FawazFarid/bc-10-neuro.git`

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


#Bugs

A few bugs were encountered during the creation of Neuro.

1. There is a googleads tag displayed in the lyrics, since the lyrics are scraped from a html page.


#Resources

1. [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

2. [Click Documentation](http://www.click.pocoo.org)

3. [SQLAlchemy](http://docs.sqlalchemy.org/en/latest/)
