import sys
import rispy


fpath = sys.argv[1]
print("Segments: "+sys.argv[2])
with open(fpath, 'r', encoding="utf-8-sig") as dataFile:
    data = rispy.load(dataFile)
    i = 0
    for entry in data:
        print(entry['title'])
        i += 1