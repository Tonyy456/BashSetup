
import sys

def main():
    # read input from bash
    if(len(sys.argv) != 3):
        exit("Usage: getPath.py [save file] [key]")
    save_file = sys.argv[1]
    get_key = sys.argv[2]

    # open save location and dictionary
    file_stream = open(save_file)
    lines = file_stream.readlines()
    pathDict = {}
    for line in lines:
        parts = line.replace("\n","").split(" ", 1)
        if(len(parts) < 2): continue
        k, p = parts
        pathDict[k] = p
    file_stream.close()

    path = pathDict.get(get_key)
    if(path is None):
        print("#ERROR")
    else:
        print(path)


if(__name__ == "__main__"):
    main()
