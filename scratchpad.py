from foundation import *

saved_playlists, all_songs = load_local_playlists('.')

for index, song_a in enumerate(list(all_songs.values())):
    #song_a.user_ratings = dict()
    for song_b_index in range(index+1, len(all_songs.values())):
        song_b = list(all_songs.values())[song_b_index]
        #print("DEBUG: Checking " + song_a.name + " and " + song_b.name)
        if song_a.user_ratings is song_b.user_ratings:
            print("Shared ratings object between " + song_a.name + " and " + song_b.name)

#write_song_db(all_songs)