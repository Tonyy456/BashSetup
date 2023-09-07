
import sys

def main():
    # read input from bash
    if(len(sys.argv) != 3):
        exit("Usage: remove_key.py [save file] [key]")
    save_file = sys.argv[1]
    key_to_del = sys.argv[2]

    # open save location and initialize current dictionary
    file_stream = open(save_file)
    lines = file_stream.readlines()
    pathDict = {}
    for line in lines:
        parts = line.replace("\n","").split(" ", 1)
        if(len(parts) < 2): continue
        key, path = parts
        pathDict[key] = path
    file_stream.close()

    # update dictionary
    path_val = pathDict.get(key_to_del)
    not_in_dict = path_val is None

    # add new key to save location
    if(not_in_dict):
        pass
    else:
        del pathDict[key_to_del]
        # in dict, rewrite whole file
        with open(save_file, 'w') as file:
            for k in pathDict:
                v = pathDict[k]
                file.write(f"{k} {v}\n")
        pass

if(__name__ == "__main__"):
    main()
