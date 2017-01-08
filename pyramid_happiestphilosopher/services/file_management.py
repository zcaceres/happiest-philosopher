PATH_TO_PHILOSOPHERS = "/Users/zachcaceres/PycharmProjects/pyramid-happiestphilosopher/pyramid_happiestphilosopher/services/philosophers"
RELATIVE_PATH_TO_FILES = "philosophers"
import os


def prepare_directories_for_processing(path):
    print('––––––––– Searching for files to process –––––––––––––')
    directories_list = []
    path_to_search = path
    top_level_directories_list = os.listdir(path_to_search)
    for directory in top_level_directories_list:
        if directory == '.DS_Store':
            print ('Found a .DS_Store file. skipping...')
        else:
            directories_list.append(directory)
    print("Found {0} directories!".format(len(top_level_directories_list)))
    print("–––––––––– FINISHED ADDING DIRECTORIES ––––––––––––––––")
    return directories_list


def get_all_files_for_processing(directory_list):
    file_paths = []
    work_names = []
    author_names = []
    for directory in directory_list:
        search_path = "{0}/{1}".format(PATH_TO_PHILOSOPHERS, directory)
        all_files = os.listdir(search_path)
        for file in all_files:
            if file == '.DS_Store':
                print('Found a .DS_Store file. skipping...')
            else:
                author_names.append(directory)
                file_paths.append(convert_file_to_relative_path(directory, file))
                work_names.append(file)
    print("Found {0} files!".format(len(file_paths)))
    print('–––––––––– FINISHED ADDING FILES –––––––––––––')
    return file_paths, work_names, author_names


def convert_file_to_relative_path(directory, file):
    return os.path.abspath("{0}/{1}/{2}".format(RELATIVE_PATH_TO_FILES, directory, file))
