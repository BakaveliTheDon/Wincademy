__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

from concurrent.futures import process
import os
import shutil
import zipfile
import glob
import re

zip = 'C:/Users/HRLMR SHOP/documents/wincademy/files/data.zip'

def clean_cache():

    current_path = os.getcwd()
    directory = 'cache'
    full_path = os.path.join(current_path, directory) 
    if os.path.exists(full_path):
        shutil.rmtree(full_path)
        os.mkdir(full_path)      
    else:
        os.mkdir(full_path)        


def cache_zip(zip_path, cache_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(cache_path)


def cached_files():
    cache = os.path.join(os.getcwd(), 'cache')
    files_list = [os.path.join(cache, file) for file in os.listdir(cache)]
   
    return files_list


def find_password(list_files):
    for file in list_files:
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if 'password' in line:
                    password = line.split(' ')[1].rstrip('\n')
                    return password
