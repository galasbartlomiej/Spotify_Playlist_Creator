import spotipy
import spotipy.util as util
import json

scope = 'playlist-modify-public'


def spotify_configuration():
    try:
        configuration_file = open("spotify_configuration", encoding="utf-8")
        configuration = json.load(configuration_file)
        configuration_file.close()

        return configuration

    except FileNotFoundError:
        print("Brak pliku konfiguracyjnego!")
        configuration = {
            "id": "",
            "secret": "",
            "redirect": "",
            "username": "",
        }
        return configuration


def save_configuration(id, secret, redirect, username):
    configuration = {
        "id": id,
        "secret": secret,
        "redirect": redirect,
        "username": username,
    }
    configuration_file = open("spotify_configuration", mode="w", encoding="utf-8")
    json_object = json.dumps(configuration, indent=4)
    configuration_file.write(json_object)
    configuration_file.close()


def create_playlist(conf, playlist_name, list_of_songs_input):
    token = util.prompt_for_user_token(username=conf["username"], scope=scope, client_id=conf["id"], client_secret=conf["secret"], redirect_uri=conf["redirect"])
    sp = spotipy.Spotify(auth=token)

    list_of_songs = []
    list_of_no_songs = []

    for song in list_of_songs_input.split("\n"):
        result = sp.search(q=song.replace("-", " "))
        try:
            list_of_songs.append(result['tracks']['items'][0]['uri'])
        except IndexError:
            print("Can't search: " + song.replace("-", " "))
            list_of_no_songs.append(song.replace("-", " "))

    if list_of_songs:
        sp.user_playlist_create(user=conf["username"], name=playlist_name, public=True)
        pre_playlist = sp.user_playlists(user=conf["username"],)
        playlist = pre_playlist['items'][0]['id']
        sp.user_playlist_add_tracks(user=conf["username"], playlist_id=playlist, tracks=list_of_songs)

    return list_of_no_songs
