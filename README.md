# RISSplitter
Python script for splitting an RIS file into several chunks for ease of importing

Setup:
```console
pip install -r requirements.txt
```

Usage:
```console
python RISSplitter.py <INPUT_FILE> <NUMBER_OF_SEGMENTS>
```
Files are output to "output/output-X.ris", where X is an index from 0 to NUMBER_OF_SEGMENTS-1