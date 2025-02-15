import sys
import os
import rispy


fpath = sys.argv[1]
segs = int(sys.argv[2])
print("Segments: "+str(segs))
with open(fpath, 'r', encoding="utf-8-sig") as dataFile:
    data = rispy.load(dataFile)
    outputContent = [[] for _ in range(segs)]
    totalNum = len(data)
    print("Total Entries: "+str(totalNum))
    numPer = int(totalNum/segs)
    i = 0
    for entry in data:
        fileNo = int(i/numPer)
        if fileNo >= segs:
            fileNo = segs-1
        outputContent[fileNo].append(entry)
        i += 1
    i = 0
    os.makedirs("output", exist_ok = True)
    for content in outputContent:
        print(str(len(content))+" Entries")
        outpath = 'output/output-'+str(i)+'.ris'
        with open(outpath, 'w', encoding="utf-8-sig") as dataFile:
            rispy.dump(content, dataFile)
        i += 1