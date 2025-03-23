# (Завдання_1)

import json
import pickle

class MusicGroups:
    def __init__(self):
        self.groups = {}

    def add_band(self, band_name):
        if band_name not in self.groups:
            self.groups[band_name] = []
            print(f"Гурт '{band_name}' додано.")
        else:
            print(f"Гурт '{band_name}' вже існує.")

    def add_album(self, band_name, album_name):
        if band_name in self.groups:
            if album_name not in self.groups[band_name]:
                self.groups[band_name].append(album_name)
                print(f"Альбом '{album_name}' додано до гурту '{band_name}'.")
            else:
                print(f"Альбом '{album_name}' вже існує в гурті '{band_name}'.")
        else:
            print(f"Гурт '{band_name}' не знайдено.")

    def save_to_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.groups, f, ensure_ascii=False, indent=4)
        print(f"Дані збережено у форматі JSON в файл '{filename}'.")

    def load_from_json(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.groups = json.load(f)
            print(f"Дані завантажено з файлу '{filename}'.")
        except FileNotFoundError:
            print(f"Файл '{filename}' не знайдено.")

    def save_to_pickle(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.groups, f)
        print(f"Дані збережено у форматі Pickle в файл '{filename}'.")

    def load_from_pickle(self, filename):
        try:
            with open(filename, 'rb') as f:
                self.groups = pickle.load(f)
            print(f"Дані завантажено з файлу '{filename}'.")
        except FileNotFoundError:
            print(f"Файл '{filename}' не знайдено.")
        except pickle.UnpicklingError:
            print(f"Помилка при завантаженні даних з файлу '{filename}'.")

# Приклад використання
if __name__ == "__main__":
    music_db = MusicGroups()
    music_db.add_band("The Beatles")
    music_db.add_album("The Beatles", "Abbey Road")
    music_db.add_album("The Beatles", "Sgt. Pepper's Lonely Hearts Club Band")
    music_db.save_to_json("music_groups.json")
    music_db.save_to_pickle("music_groups.pkl")

    # Завантаження даних
    new_music_db = MusicGroups()
    new_music_db.load_from_json("music_groups.json")
    new_music_db.load_from_pickle("music_groups.pkl")