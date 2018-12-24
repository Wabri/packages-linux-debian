import glob
import os
import pickle

def get_package_info(info):
    description = ""
    url = ""
    info = info.strip("\n").strip("# ")
    precedent_character = ""
    get_url = False
    for character in info:
        if not get_url and precedent_character == "-":
            get_url = character == " "
            if get_url:
                continue
            description += character
        elif get_url:
            url += character
        else:
            description += character
        precedent_character = character
    if not url:
        url = "no url"
    del precedent_character, get_url
    return description[:-2], url

def load_packages_from_directory(directory, *ignore_file):
    packages_loaded = dict()
    os.chdir(directory)
    counter_packages = 1
    for file in glob.glob("*.sh"):
        package_name = file.split(".")[0]
        package_description = ""
        with open(file, "r") as open_file:
            package_info = str(open_file.readline())
            if package_info[0] == "#":
                package_description, package_url = get_package_info(
                    package_info)
            else:
                package_description = package_url = package_name
        if file in ignore_file:
            print("File {} ignored".format(file))
        else:
            packages_loaded[counter_packages] = [
                package_name,
                package_description,
                package_url,
                str(directory + file)
            ]
            counter_packages += 1
    os.chdir("..")
    return packages_loaded

def get_packages(directory, *test):
    if os.path.exists(directory):
        packages = load_packages_from_directory(directory, *test)
        return packages
    else:
        print("[LOG] {} directory not found".format(directory))
    return {}


packages = get_packages("scripts/", "test.sh")

readme_file = "README.md"
start_update = True
continue_read = True
readme_updated = list()
with open(readme_file, "r") as readme:
    for line in readme.readlines():
        if not continue_read:
            if start_update:
                for package_counter in packages:
                    readme_updated.append(
                        str("- {0} - {1} - {2}".format(
                            packages[package_counter][0].capitalize(),
                            packages[package_counter][1],
                            packages[package_counter][2])))
                start_update = False
            if line == "<!--readme_update end -->\n":
                readme_updated.append(line)
                continue_read = True
        else:
            continue_read = line != "<!--readme_update start -->\n"
            readme_updated.append(line)
del start_update, continue_read

with open(readme_file, "w") as readme:
    for line in readme_updated:
        print(line.strip("\n"), file=readme)
del readme_file, readme_updated
