from os import listdir as os_listdir, remove as os_remove, rmdir as os_rmdir
from os.path import isfile as os_isfile, join as os_join


SCAN_FOLDER = os_join("C:\\", "Code", "Projects")

DELETE_FOLDERS = ["__pycache__", "bin", "target"]


def delete_folder(folder_path):
    for file_or_folder in os_listdir(folder_path):
        check_path = os_join(folder_path, file_or_folder)

        if os_isfile(check_path):
            os_remove(check_path)
        else:
            delete_folder(check_path)

    os_rmdir(folder_path)


def recursively_search_for_folders(delete_folders, folder_path):
    for file_or_folder in os_listdir(folder_path):
        check_path = os_join(folder_path, file_or_folder)

        if not os_isfile(check_path):
            if file_or_folder in DELETE_FOLDERS:
                delete_folders.append(check_path)
            else:
                recursively_search_for_folders(delete_folders, check_path)


def delete_temp_files():
    delete_folders = []

    recursively_search_for_folders(delete_folders, SCAN_FOLDER)

    if len(delete_folders) == 0:
        print("No folders found")
        return

    for folder_path in delete_folders:
        print(folder_path)

    confirmation = input(
        f"Would you like to delete the following {len(delete_folders)} folders? (y / n) > "
    )

    if confirmation == "y":
        for folder_path in delete_folders:
            delete_folder(folder_path)
        print(f"{len(delete_folders)} folders successfully deleted")
    else:
        print("User cancelled")
