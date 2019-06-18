#!/usr/bin/python


import argparse
import os
import sys




print(sys.argv[0])
exit()
# Creating parser 
my_parser = argparse.ArgumentParser(description='List the content of a folder')


# Adding arguments



my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to list')


args = my_parser.parse_args() #Namespace Object


print(args[0])
exit()


input_path = args.Path


if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))