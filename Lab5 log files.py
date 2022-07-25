import re
from collections import Counter
import csv

## open and close log file
def reader(filename):
    with open(filename) as f:
        log = f.read()
        
        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ips_list = re.findall(regexp, log)
        return(ips_list)

def reader2(filename):
    with open(filename) as r:
        log2 = r.read()
        
        regexp2 = r"^(.{6}) (.*) myth.* user (.*) from (.*)"
        ips_list2 = re.finditer(regexp2, log2, re.MULTILINE)
        return(ips_list2)

## counts ips
def count(ips_list):
    return Counter(ips_list)

def count2(ips_list2):
    return Counter(ips_list2)

def write_csv(counter):
    with open('output.csv', 'w') as csvfile:
        write = csv.writer(csvfile)

        header = ['IP Address', 'Times']
        write.writerow(header)

        for item in counter:
            write.writerow((item, counter[item]))

def write_csv2(counter):
    with open('output2.csv', 'w') as csvfile:
        write = csv.writer(csvfile)

        header = ['Date','Time','Username', 'IP Address']
        write.writerow(header)

        for item in counter:
            write.writerow((item[1],item[2],item[3],item[4]))



    
if __name__ == '__main__':
    write_csv(count(reader('log')))
    write_csv2(count2(reader2('log')))
    