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