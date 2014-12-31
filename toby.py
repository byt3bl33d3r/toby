#! /usr/bin/env python

import os
import magic
import argparse
from subprocess import Popen, PIPE

parser = argparse.ArgumentParser(description='Toby', epilog='Here you are, doggy! Good old Toby! Smell it, Toby, smell it!')
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

				#we will ignore symlinks since most of them will be broken anyway
				if 'inode/symlink' not in mime:
					if 'binary' in encoding:
						p1 = Popen(["strings", filepath], stdout=PIPE)
					else:
						p1 = Popen(["cat", filepath], stdout=PIPE)

					p2 = Popen(["grep", args.string], stdin=p1.stdout, stdout=PIPE)
					p1.stdout.close()
					output = p2.communicate()[0]
					if output:
						print filepath, mime, encoding
						print output