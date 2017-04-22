##########################################################
# Code to convert all the captions in the form of structured data.
# The structured data will be used for labelling and running text classifiers
# Input- allcaps_final.srt
# Output- a csv file
##########################################################

from collections import OrderedDict
import csv
import re

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def analyze(f):
    stats = OrderedDict()
    id = 0
    lines = f.readlines()
    for idx in range(len(lines)):
        if(is_number(lines[idx])):
            if (int(lines[idx]) == 1):
                stream = lines[idx-1]
                print(stream,lines[idx])
            #print(idx,lines[idx])
            stats[id] = {}
            stats[id]['stream'] = stream
            stats[id]['line_number'] = lines[idx]
            stats[id]['time_stamp'] = lines[idx+1]
            stats[id]['text'] = lines[idx+2]+lines[idx+3]
#            print(stats[id]['text'])
#            print(lines[idx+2],lines[idx+3],lines[idx+2]+lines[idx+3])
            id = id+1
    return stats

def write_stats(stats, f):
    out = csv.writer(f)
    out.writerow(['Key','Stream','Line_number','Time_stamp','Text'])
    for var in stats:
        out.writerow([var,stats[var]['stream'],stats[var]['line_number'],stats[var]['time_stamp'],stats[var]['text']])

def main(input_filename, output_filename):
    with open(input_filename) as input_file:
        stats = analyze(input_file)
    with open(output_filename, 'w') as output_file:
       write_stats(stats, output_file)

if __name__ == '__main__':
    main(r'allcaps_final.srt',
         r'ParsedOutput.csv')
