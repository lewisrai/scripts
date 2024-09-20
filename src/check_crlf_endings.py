import os


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
                print(check_path)
        else:
            recursively_search_for_files(crlf_files, check_path)


def main():
    recursively_search_for_files(os.path.join("C:\\", "Code", "Projects"))
