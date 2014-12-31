#! /usr/bin/env python

import os
import magic
import argparse
from termcolor import colored
from subprocess import Popen, PIPE

parser = argparse.ArgumentParser(description='Toby', epilog='Yes, a queer mongrel, with a most amazing power of scent')
parser.add_argument('-i', dest='case', action='store_true', default=False, help='Ignore case distinctions')
parser.add_argument('-s', dest='string', metavar='string', required=True, type=str, help='String to search for')
parser.add_argument('-d', dest='directory', metavar='directory', required=True, type=str, help='Directory to search')

args = parser.parse_args()

for root, dirs, files in os.walk(args.directory):
	if files:
		for file in files:
			filepath = root + '/' + file
			if os.path.exists(filepath):

				with magic.Magic() as m:
					filetype = m.id_filename(filepath)

				with magic.Magic(flags=magic.MAGIC_MIME_TYPE) as m:
					mime = m.id_filename(filepath)

				with magic.Magic(flags=magic.MAGIC_MIME_ENCODING) as m:
					encoding = m.id_filename(filepath)

				grep_args = ["grep", "--color=always"]
				strings_args = ["strings"]

				if args.case:
					grep_args.append('-i')

				#we will ignore symlinks since most of them will be broken anyway
				if 'inode/symlink' not in mime:
					if 'binary' in encoding:
						strings_args.append(filepath)
						grep_args.append(args.string)
						p1 = Popen(strings_args , stdout=PIPE)
						p2 = Popen(grep_args, stdin=p1.stdout, stdout=PIPE)
						p1.stdout.close()
					else:
						grep_args.extend(["-n", args.string, filepath])
						p2 = Popen(grep_args, stdout=PIPE)

					output = p2.communicate()[0]
					if output:
						print colored(filepath, 'magenta', attrs=['bold']),  colored(mime, 'blue'), colored(encoding, 'blue')
						print output