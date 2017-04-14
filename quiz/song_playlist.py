#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 13:01:55 2017

@author: umesh
"""

def find_next_song_idx(songs, played, max_size):
    """ Find the next smallest sized songs not yet played"""
    N = len(songs)
    min_size = max_size
    song_idx = None
    for idx in range(N):
        if not played[idx] and songs[idx][2] < max_size:
            if songs[idx][2] < min_size:
                song_idx = idx
                min_size = songs[idx][2]
    return song_idx

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order
             in which they were chosen.
    """
    playlist = []
    played = [False] * len(songs)
    if songs[0][2] > max_size:
        return playlist
    else:
        playlist.append(songs[0][0])
        played[0] = True
        max_size -= songs[0][2]

        next_idx = find_next_song_idx(songs, played, max_size)
        while next_idx:
            playlist.append(songs[next_idx][0])
            played[next_idx] = True
            max_size -= songs[next_idx][2]
            next_idx = find_next_song_idx(songs, played, max_size)
        return playlist


#songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),
#         ('Timber', 5.1, 6.9), ('Wannabe',2.7, 1.2)]

# songs = [('a', 4.0, 4.4), ('b', 7.7, 3.5), ('c', 6.9, 5.1), ('d', 1.2, 2.7)]
songs = [('a', 4.0, 4.4), ('b', 7.7, 3.5), ('c', 6.9, 5.1), ('d', 1.2, 2.7)]
fin_list = song_playlist(songs, 12.3)
print(fin_list)