import os


DELETE_FOLDERS = ["__pycache__", "bin", "target"]
OTHER_LOCATIONS = []


def delete_folder(folder_path):
    for file_or_folder in os.listdir(folder_path):
        check_path = os.path.join(folder_path, file_or_folder)

        if os.path.isfile(check_path):
            os.remove(check_path)
        else:
            delete_folder(check_path)

    os.rmdir(folder_path)


def recursively_search_for_folders(delete_folders, folder_path):
    for file_or_folder in os.listdir(folder_path):
        check_path = os.path.join(folder_path, file_or_folder)

        if not os.path.isfile(check_path):
            if file_or_folder in DELETE_FOLDERS:
                confirmation = input(f'INPUT < Delete "{file_or_folder}"? ')

                if confirmation == "y":
                    delete_folder(check_path)
            else:
                recursively_search_for_folders(delete_folders, check_path)


def main():
    recursively_search_for_folders(os.path.join("C:\\", "Code", "Projects"))

    for folder_path in OTHER_LOCATIONS:
        confirmation = input(f'INPUT < Delete "{folder_path}"? ')

        if confirmation == "y":
            delete_folder(folder_path)
