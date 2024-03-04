with open("requirements.txt", "r") as file:
    packages = file.read()

packages = packages.replace("==", ">=")

with open("requirements.txt", "w") as file:
    file.write(packages)
