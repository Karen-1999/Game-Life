import sys
import argparse
from model import Maps, print_map

pars = argparse.ArgumentParser()
pars.add_argument('--input-file', type=str, default='stdin', help='in file')
pars.add_argument('--output-file', type=str, default='stdout', help='out file')
args = vars(pars.parse_args())
input_file = args['input_file']
output_file = args['output_file']

"""
установлены опциональные параметры --input-file и --output-file,
консольный интерфейс для них:
python3 main.py --input-file "input.txt" --output-file "output.txt"
"""
if input_file != "stdin":
    sys.stdin = open(input_file, 'r')
first_line = input().split(' ')
"""
считаю первую строчку,где n,m,k передаются
"""
height, width, generations = [int(x) for x in first_line]
"""
обработал элеменыт первый строки
param: height = n
param: width = m
param: generations = k
"""
my_map_short_named = []
for i in range(height):
    my_map_short_named.append(list(input().strip()))
"""
считал карту океана как лист из str
"""
my_map = Maps(my_map_short_named)
my_map.upgrade(generations)
if output_file != "stdout":
    sys.stdout = open(output_file, 'w')
print_map(my_map.start_map)
