# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.events import SlotSet
import requests
import sqlite3

class ActionSoulfulMusic(Action):

    def name(self) -> Text:
        return "action_soulful_music_call"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        endpoint = "https://api.spotify.com/v1/search?q=soulful&type=track&include_external=audio&limit=5"
        headers = {"Authorization": "Bearer BQAYJyMFBDSekpOe-Xj9g-RJn_19XWXDgH-CxCswhZu2rN0VKHHx1mkE4iaRIstNQkNdBzYU3qLny3AQHd_LmGWhUoIHqZzARksDT1gsWHH22-fV9kKJdRorkKOY_zotWQ0CYRJ2LVVlNoJSVwV3Ya5DrXq13slppT3qDDCbhLWOa1WAjDQXV05r39eJhw8"}

        response = requests.get(endpoint,  headers=headers)
        response_data=response.json()

        #print(response_data)
        tracks = response_data['tracks']['items']
        for item in tracks:
            track_name = item['name']
            track_url = item['external_urls']['spotify']
            artist_name = item['artists'][0]['name']
            message = "Track Name: " + track_name + "\n" + "Artist Name: " + artist_name + "\n" + "Track URL: " + track_url
            message = message + "\n" + "=================================================================="

            dispatcher.utter_message(message)

        return []

class ActionPartyMusic(Action):

    def name(self) -> Text:
        return "action_party_music_call"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        endpoint = "https://api.spotify.com/v1/search?q=party&type=track&include_external=audio&limit=5"
        headers = {"Authorization": "Bearer BQAYJyMFBDSekpOe-Xj9g-RJn_19XWXDgH-CxCswhZu2rN0VKHHx1mkE4iaRIstNQkNdBzYU3qLny3AQHd_LmGWhUoIHqZzARksDT1gsWHH22-fV9kKJdRorkKOY_zotWQ0CYRJ2LVVlNoJSVwV3Ya5DrXq13slppT3qDDCbhLWOa1WAjDQXV05r39eJhw8"}

        response = requests.get(endpoint,  headers=headers)
        response_data=response.json()

        #print(response_data)
        tracks = response_data['tracks']['items']
        for item in tracks:
            track_name = item['name']
            track_url = item['external_urls']['spotify']
            artist_name = item['artists'][0]['name']
            message = "Track Name: " + track_name + "\n" + "Artist Name: " + artist_name + "\n" + "Track URL: " + track_url
            message = message + "\n" + "=================================================================="

            dispatcher.utter_message(message)

        return []

class ActionRomanticMusic(Action):

    def name(self) -> Text:
        return "action_romantic_music_call"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        endpoint = "https://api.spotify.com/v1/search?q=romantic&type=track&include_external=audio&limit=5"
        headers = {"Authorization": "Bearer BQAYJyMFBDSekpOe-Xj9g-RJn_19XWXDgH-CxCswhZu2rN0VKHHx1mkE4iaRIstNQkNdBzYU3qLny3AQHd_LmGWhUoIHqZzARksDT1gsWHH22-fV9kKJdRorkKOY_zotWQ0CYRJ2LVVlNoJSVwV3Ya5DrXq13slppT3qDDCbhLWOa1WAjDQXV05r39eJhw8"}

        response = requests.get(endpoint,  headers=headers)
        response_data=response.json()

        #print(response_data)
        tracks = response_data['tracks']['items']
        for item in tracks:
            track_name = item['name']
            track_url = item['external_urls']['spotify']
            artist_name = item['artists'][0]['name']
            message = "Track Name: " + track_name + "\n" + "Artist Name: " + artist_name + "\n" + "Track URL: " + track_url
            message = message + "\n" + "=================================================================="

            dispatcher.utter_message(message)

        return []


class ActionMotivationPodcast(Action):

    def name(self) -> Text:
        return "action_motivation_podcast_call"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = requests.get("https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=5&q=motivation+podcast&key=AIzaSyBRvCgg98aLUA5NpMRxKTOUQrP1DlCeWEQ")
        response_data = response.json()
        #print("Response data:", response_data)
        response_items = response_data['items']
        for item in response_items:
            url = item['id']
            if 'videoId' in url:
                url = url['videoId']
                final_url = "https://www.youtube.com/watch?v="+url
                title = item['snippet']['title']
                desc = item['snippet']['description']
                message = "Title: " + title + "\n" + "URL: " + final_url + "\n" + "Description: " + desc 
                message = message + "\n" + "=================================================================="
                
                dispatcher.utter_message(message)

        return []

class ActionHappyPodcast(Action):

    def name(self) -> Text:
        return "action_happy_podcast_call"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = requests.get("https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=5&q=happy+podcast&key=AIzaSyBRvCgg98aLUA5NpMRxKTOUQrP1DlCeWEQ")
        response_data = response.json()
        #print("Response data:", response_data)
        response_items = response_data['items']
        for item in response_items:
            
            url = item['id']
            if 'videoId' in url:
                url = url['videoId']
                final_url = "https://www.youtube.com/watch?v="+url
                title = item['snippet']['title']
                desc = item['snippet']['description']
                message = "Title: " + title + "\n" + "URL: " + final_url + "\n" + "Description: " + desc
                message = message + "\n" + "=================================================================="
                
                dispatcher.utter_message(text=message)
        return []

class ActionCrimePodcast(Action):

    def name(self) -> Text:
        return "action_crime_podcast_call"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = requests.get("https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=5&q=crime+podcast&key=AIzaSyBRvCgg98aLUA5NpMRxKTOUQrP1DlCeWEQ")
        response_data = response.json()
        #print("Response data:", response_data)
        response_items = response_data['items']
        for item in response_items:
            url = item['id']
            if 'videoId' in url:
                url = url['videoId']
                final_url = "https://www.youtube.com/watch?v="+url
                title = item['snippet']['title']
                desc = item['snippet']['description']
                message = "Title: " + title + "\n" + "URL: " + final_url + "\n" + "Description: " + desc
                message = message + "\n" + "=================================================================="
                
                dispatcher.utter_message(message)
        return []

class ActionThrillerBook(Action):

    def name(self) -> Text:
        return "action_thriller_book_call"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = requests.get("https://www.googleapis.com/books/v1/volumes?q=thriller&maxResults=5")
        response_data = response.json()
        #print("Response data:", response_data)
        response_items = response_data['items']
        for item in response_items:
            temp = item['volumeInfo']
            if "subtitle" in temp:

                title = item['volumeInfo']['title']
                subtitle = item['volumeInfo']['subtitle']
                preview_link = item['volumeInfo']['previewLink']
                message = "Title: " + title + "\n" + "Subtitle: " + subtitle + "\n" + "You can have a look at the book here: " + preview_link
                message = message + "\n" + "=================================================================="
            else:
                title = item['volumeInfo']['title']
                preview_link = item['volumeInfo']['previewLink']
                message = "Title: " + title + "\n" + "You can have a look at the book here: " + preview_link
                message = message + "\n" + "=================================================================="

            dispatcher.utter_message(message)
        return []

class ActionSelfHelpBook(Action):

    def name(self) -> Text:
        return "action_selfhelp_book_call"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = requests.get("https://www.googleapis.com/books/v1/volumes?q=self+help&maxResults=5")
        response_data = response.json()
        #print("Response data:", response_data)
        response_items = response_data['items']
        for item in response_items:
            temp = item['volumeInfo']
            if "subtitle" in temp:

                title = item['volumeInfo']['title']
                subtitle = item['volumeInfo']['subtitle']
                preview_link = item['volumeInfo']['previewLink']
                message = "Title: " + title + "\n" + "Subtitle: " + subtitle + "\n" + "You can have a look at the book here: " + preview_link
                message = message + "\n" + "=================================================================="
            else:
                title = item['volumeInfo']['title']
                preview_link = item['volumeInfo']['previewLink']
                message = "Title: " + title + "\n" + "You can have a look at the book here: " + preview_link
                message = message + "\n" + "=================================================================="

            dispatcher.utter_message(message)
        return []

class ActionFictionalBook(Action):

    def name(self) -> Text:
        return "action_fictional_book_call"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = requests.get("https://www.googleapis.com/books/v1/volumes?q=fiction&maxResults=5")
        response_data = response.json()
        #print("Response data:", response_data)
        response_items = response_data['items']
        for item in response_items:
            temp = item['volumeInfo']
            if "subtitle" in temp:

                title = item['volumeInfo']['title']
                subtitle = item['volumeInfo']['subtitle']
                preview_link = item['volumeInfo']['previewLink']
                message = "Title: " + title + "\n" + "Subtitle: " + subtitle + "\n" + "You can have a look at the book here: " + preview_link
                message = message + "\n" + "=================================================================="
            else:
                title = item['volumeInfo']['title']
                preview_link = item['volumeInfo']['previewLink']
                message = "Title: " + title + "\n" + "You can have a look at the book here: " + preview_link
                message = message + "\n" + "=================================================================="


            dispatcher.utter_message(message)
        return []


class ActionSaveFirstname(Action):

    def name(self) -> Text:
        return "action_save_firstname"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print(tracker.get_slot('firstname'))
        return [SlotSet('firstname',tracker.latest_message['text'])]

class ActionSaveFeedback(Action):

    def name(self) -> Text:
        return "action_save_feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_to_ask")
        print(tracker.get_slot('feedback'))
        return [SlotSet('feedback',tracker.latest_message['text'])]

# class ActionSavePodcastGenre(Action):

#     def name(self) -> Text:
#         return "action_save_podcast_genre"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_to_ask")
#         print(tracker.get_slot('podcast_genre'))
#         return [SlotSet('podcast_genre',tracker.latest_message['text'])]

# class ActionSaveBookGenre(Action):

#     def name(self) -> Text:
#         return "action_save_book_genre"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_to_ask")
#         print(tracker.get_slot('book_genre'))
#         return [SlotSet('book_genre',tracker.latest_message['text'])]

# class ActionSaveMusicGenre(Action):

#     def name(self) -> Text:
#         return "action_save_music_genre"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_to_ask")
#         print(tracker.get_slot('music_genre'))
#         return [SlotSet('music_genre',tracker.latest_message['text'])]

def datastore(firstname,feedback):
    conn=sqlite3.connect('test.db')
    mycursor = conn.cursor()
    mycursor.execute("""CREATE TABLE IF NOT EXISTS new_data (Name TEXT, Feedback TEXT);""")
    mycursor.execute("INSERT INTO new_data VALUES (?,?)",(firstname,feedback))
    conn.commit()
    print(mycursor.rowcount,"record inserted")

class ActionStore(Action):

    def name(self) -> Text:
        return "action_store"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        x=tracker.get_slot('firstname')
        y=tracker.get_slot('feedback')
        datastore(x,y)
        dispatcher.utter_message("Thank you! Your information has been stored.")
        return []