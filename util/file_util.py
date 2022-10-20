import json
import os

from util.date_util import now_str

current_breath_cache_file = ""
breath_cache_files = []


def breath_new_cache_file_name():
    return "static/breath_new_cache-" + now_str() + ".json"


def breath_new_cache_file(breath_map):
    tf = open(breath_new_cache_file_name(), "w")
    json.dump(breath_map, tf)
    tf.close()
    remove_breath_cache_files()
    breath_cache_files.append(breath_new_cache_file_name())


def has_breath_new_cache_file():
    return os.path.exists(breath_new_cache_file_name())


def remove_breath_cache_files():
    for cache_file in breath_new_cache_file_name():
        os.remove(cache_file)
