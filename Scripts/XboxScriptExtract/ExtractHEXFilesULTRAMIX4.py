import csv
import io
import sys

g = open("x_data_XBOX_US.bin", 'rb')
data = g.read()
g.close()

with open("ExtractInfo.csv", "r") as f_input:
    csv_input = csv.DictReader(f_input)

    for row in csv_input:
        fnameext = row['fnameext']
        offset = row['offset']
        length = row['length']

        header = hex(int(offset, 16))
        footer = hex(int(offset, 16) + int(length, 16))
        
        headint = int(header, 0)
        footint = int(footer, 0)
        
        vidya = data[headint:footint]
        
        with io.open("ExtractData\\" + fnameext, 'wb+') as f:
            f.write(vidya)
