import argparse
from zipfile import ZipFile
from pathlib import Path

parser = argparse.ArgumentParser(description='Index Zip Files')
parser.add_argument('--file', type=str, required=False)
parser.add_argument('--dir', type=str, required=False)
parser.add_argument('--search', type=str, required=False)
args = parser.parse_args()



def index_file(file):
    listOfiles = []
    with ZipFile(file, 'r') as zf:
        for member in zf.namelist():
            if member.endswith('/') == False:
                listOfiles.append(member)
    return listOfiles

def write_index(zipfile, listOfiles):
    with open("zipindex.csv", 'a') as f:
        for item in listOfiles:
            f.write(str(zipfile) + "," + item + '\n')

if args.file:
    index = index_file(args.file)
    write_index(args.file ,index)

if args.dir:
    for file in Path(args.dir).rglob('*.zip'):
        index = index_file(file)
        write_index(file, index)

if args.search:
    detected = []
    with open("zipindex.csv", 'r') as f:
        for line in f:
            split = line.split(',')
            if args.search in split[1]:
                
                if split[0] not in detected:
                    print(split[0])
                    detected.append(split[0])
