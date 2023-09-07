
import sys

def main():
    # read input from bash
    if(len(sys.argv) != 4):
        exit("Usage: set.py [save file] [key] [path]")
    save_file = sys.argv[1]
    new_key = sys.argv[2]
    new_path = sys.argv[3]

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
    path_val = pathDict.get(new_key)
    append_to_file = path_val is None
    pathDict[new_key] = new_path

    # add new key to save location
    if(append_to_file):
        # not in dict, append to file
        with open(save_file, 'a') as file:
            file.write(f"{new_key} {new_path}\n")
        pass
    else:
        # in dict, rewrite whole file
        with open(save_file, 'w') as file:
            for k in pathDict:
                v = pathDict[k]
                file.write(f"{k} {v}\n")
        pass

if(__name__ == "__main__"):
    main()
