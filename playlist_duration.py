import random
from datetime import timedelta
from typing import Union

def get_duration(playlist: Union[str, dict], n: int):
    if isinstance(playlist, str):
        playlist_dict = {}
    else:
        playlist_dict = playlist
