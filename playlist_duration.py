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
    if isinstance(playlist, str):
        playlist_dict = {}
        lines = playlist.strip().splitlines()
        for line in lines:
            parts = line.rsplit(' ', 1)
            if len(parts) == 2 and ':' in parts[1]:
                song, duration = parts[0], parts[1]
                minutes, seconds = map(int, duration.split(':'))
                playlist_dict[song] = timedelta(minutes=minutes, seconds=seconds)
    else:
        playlist_dict = {}
        for song, duration in playlist.items():
            if isinstance(duration, float):
                minutes = int(duration)
                seconds = int((duration - minutes) * 100)
                playlist_dict[song] = timedelta(minutes=minutes, seconds=seconds)
            else:
                playlist_dict[song] = duration

    if len(playlist_dict) < n:
        raise ValueError("Плейлист содержит меньше песен, чем запрошенное количество.")

    total_duration = sum(
        list(playlist_dict.values())[:n], timedelta()
    )

    return total_duration
