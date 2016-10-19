# -*- coding: utf-8 -*-

import requests
import urllib
from bs4 import BeautifulSoup
from models import LyricsModels


class LyricsViews(object):
    def __init__(self):
        self.headers = {
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
        # check if there is local copy in database

        song_url = 'http://api.genius.com/songs/' + str(song_id)

        r = requests.get(song_url, headers=self.headers)

        data = r.json()
        # return data

        lyrics_url = data['response']['song']['url']
        response = requests.get(lyrics_url)

        soup = BeautifulSoup(response.text, "html.parser")
        lyrics = soup.find("lyrics", class_="lyrics").text.encode('utf-8')
        return lyrics

# song = LyricsViews()
# print song.get_song_by_id(2494028)