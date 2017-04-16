from collections import OrderedDict
import csv
import re

def analyze_log(f):
    stats = OrderedDict()
    for line in f:
        print(line)        
    return stats

def main(input_filename, output_filename):
    with open(input_filename) as input_file:
        stats = analyze_log(input_file)
#    with open(output_filename, 'w') as output_file:
#       write_stats(stats, output_file)

if __name__ == '__main__':
    main(r'allcaps.srt',
         r'ParsedOutput.csv')
