import os
import sys

def change_name(new_name, folder_path):
    if not os.path.isdir(folder_path):
        print(f"Podana ścieżka '{folder_path}' nie jest folderem.")
        return

    # Pobierz listę plików w folderze
    files = os.listdir(folder_path)

    count = 1
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)

        # Sprawdź, czy to faktycznie plik (pomijamy katalogi)
        if not os.path.isfile(file_path):
            continue

        try:
            # Pobierz rozszerzenie pliku
            name, ext = os.path.splitext(file_name)
            # Utwórz nową nazwę z "(count)" przed rozszerzeniem
            new_filename = f"{new_name}({count}){ext}"
            new_filepath = os.path.join(folder_path, new_filename)
            # Zmień nazwę pliku
            os.rename(file_path, new_filepath)
            print(f"Zmieniono nazwę pliku '{file_name}' na '{new_filename}'")
            count += 1
        except Exception as e:
            print(f"Nie udało się zmienić nazwy pliku '{file_name}': {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python rename.py <new_name> <folder_path>")
    else:
        new_name = sys.argv[1]
        folder_path = sys.argv[2]
        change_name(new_name, folder_path)
