import os


SCAN_FOLDER = os.path.join("C:\\", "Code", "Projects")


def check_crlf_ending(file_path):
    with open(file_path, "rb") as file:
        content = file.read()

    if b"\r\n" in content:
        return True

    return False


def recursively_search_for_files(crlf_files, folder_path):
    for file_or_folder in os.listdir(folder_path):
        check_path = os.path.join(folder_path, file_or_folder)

        if os.path.isfile(check_path):
            if check_crlf_ending(check_path):
                crlf_files.append(check_path)
        else:
            recursively_search_for_files(crlf_files, check_path)


def check_crlf_endings():
    crlf_files = []

    recursively_search_for_files(crlf_files, SCAN_FOLDER)

    for file in crlf_files:
        print(file)

    print(f"There are {len(crlf_files)} files containing CRLF characters")
    print("These may be data files that contains the CRLF characters as binary")
