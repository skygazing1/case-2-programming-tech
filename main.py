import playlist_duration as pd

playlist_e = """
Sunday 5:09
Why Does My Heart Feel so Bad? 4.23
Everlong 3.25
To Let Myself Go
Golden 2.56
Daisuke 2.41
Miami 3.31
Chill Bill Lofi 2.05
The Perfect Girl 1.48
Resonance 3.32
"""

playlist_b = {
	'Портофино': 3.32,
	'Снег': 4.35,
	'Попытка №5': 3.23,
	'Тополиный Пух': 3.53,
	'Если хочешь остаться': 4.48,
	'Зеленоглазое такси': 5.52,
	'Ты не верь слезам': 3.1,
	'Nowhere to Run': 2.58,
	'Салют, Вера': 4.44,
	'Улетаю': 3.24,
	'Опять метель': 3.37,
	}


def main():
    
    print(
        pd.get_duration(playlist=playlist_e, n=3), 
        pd.get_duration(playlist=playlist_b, n=3), # TODO - TypeError: unsupported operand type(s) for +: 'datetime.timedelta' and 'float'
        sep="\n"
        )


if __name__ == "__main__":
    main()