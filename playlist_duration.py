import random
from datetime import timedelta
from typing import Union


def get_duration(playlist: Union[str, dict], n: int) -> timedelta:
    """
    Функция принимает плейлист с песнями и временем звучания в виде коллекции и возвращает время звучания

    :param playlist: исходная коллекция с песнями
    :type playlist: str | dict

    :param n: количество песен
    :type n: int

    :return: время звучания
    :rtype: timedelta
    """
    match playlist:
        case str():
            playlist_dict = {}
            lines = playlist.strip().splitlines()
            for line in lines:
                parts = line.rsplit(' ', 1)
                if len(parts) == 2 and '.' in parts[1]:
                    song, duration = parts[0], parts[1]
                    minutes, seconds = map(int, duration.split('.'))
                    playlist_dict[song] = timedelta(minutes=minutes, seconds=seconds)
        case dict():
            playlist_dict = playlist

    if len(playlist_dict) < n:
        raise ValueError("Плейлист содержит меньше песен, чем запрашиваемое количество.")

    # Преобразуем длительность в timedelta для всех песен в словаре, если они представляют собой float
    for song, duration in playlist_dict.items():
        if isinstance(duration, float):
            minutes = int(duration)  # Целая часть — это минуты
            seconds = int((duration - minutes) * 60)  # Оставшаяся часть — это секунды
            playlist_dict[song] = timedelta(minutes=minutes, seconds=seconds)

    random_songs = random.sample(list(playlist_dict.values()), n)
    total_duration = sum(random_songs, timedelta())  # Складываем продолжительности песен

    return total_duration