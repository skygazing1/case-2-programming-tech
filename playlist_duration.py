import random
from datetime import timedelta
from typing import Union

def get_duration(playlist: Union[str, dict], n: int):
    if isinstance(playlist, str):
        playlist_dict = {}
        lines = playlist.strip().splitlines()
        for line in lines:
            parts = line.rsplit(' ', 1)
            if len(parts) == 2 and '.' in parts[1]:
                song, duration = parts[0], parts[1]
                minutes, seconds = map(int, duration.split('.'))
                playlist_dict[song] = timedelta(minutes=minutes, seconds=seconds)
    else:
        playlist_dict = playlist

    if len(playlist_dict) < n:
        raise ValueError("Плейлист содержит меньше песен, чем запрошенное количество.")

    random_songs = random.sample(list(playlist_dict.values()), n)
    total_duration = sum(random_songs, timedelta())

    return total_duration


def time_counter(song_list: dict) -> float:
    pass
