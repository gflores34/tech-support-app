import os, fnmatch, re

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                root = re.sub("\\\\", "/", root)
                combined = root + "/" + name
                result.append(combined)
    return result


def drawing_finder(dir, pattern):
    
    file_array = find(pattern + ".*", dir)

    return file_array

