# -*- coding: utf-8 -*-

import requests
import urllib
from bs4 import BeautifulSoup
from models import DbAbsLayer, Song

db = DbAbsLayer()
session = db.create_session().session


class LyricsViews(object):
    def __init__(self):
        self.headers = {
            # Access Token
            'Authorization': 'Bearer I01LPneQJjxNd9qsMdOukM2Z64MzuUekMRnuxubPGWvpL90WncPVl0uOYMBpXDny'
        }

    def search(self, search_criteria):
        # url encode the search string
        query = urllib.quote(str(search_criteria))
        search_url = 'http://api.genius.com/search?q=' + query
        r = requests.get(search_url, headers=self.headers)

        data = r.json()

        results = data['response']['hits']
        return results

    def get_song_by_id(self, song_id):
        results = {}
        # check if there is local copy in database
        song = session.query(Song).get(song_id)
        if song is not None:
            results['id'] = song.id
            results['title'] = song.name
            results['lyrics'] = song.lyrics.encode('utf-8')
        # if no copy exists, get it from the Api
        else:

            song_url = 'http://api.genius.com/songs/' + str(song_id)
            r = requests.get(song_url, headers=self.headers)

            data = r.json()

            # find the lyrics page
            lyrics_url = data['response']['song']['url']
            response = requests.get(lyrics_url)

            # scrap the lyrics from the <lyrics> tag, in the html page
            soup = BeautifulSoup(response.text, "html.parser")
            lyrics = soup.find("lyrics", class_="lyrics").text.encode('utf-8')

            results['id'] = data['response']['song']['id']
            results['title'] = data['response']['song']['title']
            results['lyrics'] = lyrics

        return results

    def save_song(self, song_id):
        data = self.get_song_by_id(song_id)
        new_song = Song(id=data['id'], name=data['title'],
                        lyrics=data['lyrics'].decode('utf-8'))
        session.add(new_song)
        session.commit()

    def clear_db(self):
    	db.clear_db()



# song = LyricsViews()
# # song.add_song(2494028)
# print song.get_song_by_id(378195)['lyrics']
