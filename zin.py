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

def write_index(listOfiles):
    with open("zipindex.txt", 'a') as f:
        for item in listOfiles:
            f.write(item + '\n')

if args.file:
    index = index_file(args.file)
    write_index(index)

if args.dir:
    for file in Path(args.dir).rglob('*.zip'):
        index = index_file(file)
        write_index(index)

if args.search:
    with open("zipindex.txt", 'r') as f:
        for line in f:
            if args.search in line:
                print(line)
