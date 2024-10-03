import os
import shutil


PROJECT_FOLDER = "C:\\Code\\Projects"
DELETE_FOLDERS = ["__pycache__", "bin", "target"]
OTHER_LOCATIONS = ["C:\\Users\\raiwin\\AppData\\Local\\D3DSCache"]


def delete_folder(path):
    confirmation = input(f'INPUT < Delete "{path}"? ')

    if confirmation != "y":
        return

    try:
        shutil.rmtree(path)
    except OSError as e:
        print(f"Error deleting folder {path} > {e}")


def recursively_search_for_folders(folder_path):
    for file_or_folder in os.listdir(folder_path):
        check_path = os.path.join(folder_path, file_or_folder)

        if not os.path.isfile(check_path):
            if file_or_folder in DELETE_FOLDERS:
                delete_folder(file_or_folder)
            else:
                recursively_search_for_folders(check_path)


def main():
    recursively_search_for_folders(PROJECT_FOLDER)

    for folder_path in OTHER_LOCATIONS:
        delete_folder(folder_path)


if __name__ == "__main__":
    main()
