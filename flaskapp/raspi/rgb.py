#!/usr/bin/env python
import subprocess
import argparse
from rgbinterface import RGBInterface

# parsing arguments
parser = argparse.ArgumentParser(description='reconfigure led stripe')
parser.add_argument('red', metavar='r', type=int)
parser.add_argument('green', metavar='g', type=int)
parser.add_argument('blue', metavar='b', type=int)
parser.add_argument('lightness', metavar='l', type=int)
parser.add_argument('position', metavar='p', type=int)

args = parser.parse_args()
r = args.red
g = args.green
b = args.blue
l = args.lightness
p = args.position

# initializing
ri = RGBInterface()

# do stuff
ri.update_colors(r, g, b, l, p)