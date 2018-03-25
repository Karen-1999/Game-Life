import argparse
from myclasses import Maps, print_map

pars = argparse.ArgumentParser()
pars.add_argument('--input-dir', type=str, default='stdin', help='in file')
pars.add_argument('--output-dir', type=str, default='stdout', help='out file')
args = vars(pars.parse_args())
input_dir = args['input_dir']
output_dir = args['output_dir']
"""
установлены опциональные параметры --input-dir и --output-dir,
консольный интерфейс для них:
python3 main.py --input-dir "input.txt" --output-dir "output.txt"
"""
if(input_dir == 'stdin'):
    first_line = input().split(' ')
    list_first_line = [int(x) for x in first_line]
    n = list_first_line[0]
    m = list_first_line[1]
    k = list_first_line[2]
    my_map = Maps([], n, m)
    for i in range(n):
        my_map.start_map.append([str(j) for j in str(input())])
    my_map.upgrade(k)
else:
    with open(input_dir, 'r') as file_in:
        file_lines = file_in.readlines()
        first_line = [int(x) for x in file_lines[0].split(" ")]
        n = first_line[0]
        m = first_line[1]
        k = first_line[2]
        my_map = Maps([], n, m)
        for i in range(1, n+1):
            my_map.start_map.append([str(j) for j in file_lines[i]])
        my_map.upgrade(k)
if(output_dir == 'stdout'):
    print_map(my_map.start_map)
else:
    fout = open(output_dir, 'w')
    for i in my_map.start_map:
        fout.write("".join(i))
