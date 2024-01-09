from os import listdir as os_listdir
from os.path import isfile as os_isfile, join as os_join


SCAN_FOLDER = os_join("C:\\", "Code", "Projects")

SKIP_FOLDERS = ["COMSC-Solo", "COMSC-Teams", "Scripts"]


def check_crlf_ending(file_path):
    with open(file_path, "rb") as file:
        content = file.read()

    if b"\r" in content:
        return True

    return False


def recursively_search_for_files(crlf_files, folder_path):
    for directory in os_listdir(folder_path):
        if directory in SKIP_FOLDERS:
            continue

        check_path = os_join(folder_path, directory)

        if os_isfile(check_path):
            if check_crlf_ending(check_path):
                crlf_files.append(check_path)
        else:
            recursively_search_for_files(crlf_files, check_path)


def check_crlf_endings():
    crlf_files = []

    recursively_search_for_files(crlf_files, SCAN_FOLDER)

    for file in crlf_files:
        print(file)

    print(f'There are {len(crlf_files)} files containing CR character')
