import os
import sys
from PIL import Image
import pillow_heif  # Dodajemy obsługę HEIC

# Rejestrujemy plugin dla Pillow
pillow_heif.register_heif_opener()

def convert_images_to_jpg(folder_path):
    # Sprawdzenie, czy podana ścieżka jest folderem
    if not os.path.isdir(folder_path):
        print(f"Podana ścieżka '{folder_path}' nie jest folderem.")
        return

    # Pobranie listy plików w folderze
    files = os.listdir(folder_path)

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)

        # Sprawdzamy, czy ścieżka wskazuje na plik
        if not os.path.isfile(file_path):
            continue

        # Próbujemy otworzyć plik jako obraz
        try:
            with Image.open(file_path) as img:
                # Konwersja na format RGB (jeśli to wymagane)
                img = img.convert('RGB')
                
                # Zmiana rozszerzenia na .jpg
                new_file_name = os.path.splitext(file_name)[0] + '.jpg'
                new_file_path = os.path.join(folder_path, new_file_name)

                # Zapisanie pliku jako .jpg
                img.save(new_file_path, 'JPEG')

                print(f"Plik '{file_name}' został przekonwertowany na '{new_file_name}'.")

        except Exception as e:
            print(f"Nie udało się przekonwertować pliku '{file_name}': {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Użycie: python convert_to_jpg.py <ścieżka_do_folderu>")
    else:
        folder_path = sys.argv[1]
        convert_images_to_jpg(folder_path)
