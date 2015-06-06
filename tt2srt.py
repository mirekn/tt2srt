#!/usr/bin/python

"""
Youtube timed text subtitle file converter

Usage:
	python tt2srt.py <xml-file> [<srt-file>]

Where:
	xml-file ... XML file of timed text file
	srt-file ... SRT output file
"""


from xml.dom.minidom import parse
import sys
import os


def get_args():
	"""Get command line arguments"""

	if len(sys.argv) < 2:
		print __doc__
		raise SystemExit

	iname = sys.argv[1]
	if not os.path.exists(iname) or not iname.endswith('.xml'):
		print __doc__
		raise SystemExit

	oname = iname.replace('.xml', '.srt')
	if len(sys.argv) > 2:
		oname = sys.argv[2]

	return iname, oname


def main():
	"""Solve the main task"""

	iname, oname = get_args()

	i = 1
	dom = parse(iname)
	out = open(oname, 'wb')
	body = dom.getElementsByTagName("timedtext")[0]
	paras = body.getElementsByTagName("text")

	for para in paras:

		out.write((str(i) + "\r\n").encode("utf-8"))
		sub = para.attributes['t'].value
		t = int(sub)
		sub1 = str(t%1000).zfill(3)
		sub2 = str(int(t/1000)%60).zfill(2)
		sub3 = str(int(t/60000)%60).zfill(2)
		sub4 = str(int(t/3600000)%60).zfill(2)
		start = sub4 + ':' + sub3 + ':' + sub2 + ',' + sub1

		sub = para.attributes['d'].value
		d = int(sub) + t
		sub1 = str(d%1000).zfill(3)
		sub2 = str(int(d/1000)%60).zfill(2)
		sub3 = str(int(d/60000)%60).zfill(2)
		sub4 = str(int(d/3600000)%60).zfill(2)
		end = sub4 + ':' + sub3 + ':' + sub2 + ',' + sub1

		out.write((start + ' --> ' + end + '\r\n').encode("utf8"))

		for child in para.childNodes:
			if child.nodeName == '#text':
				out.write(child.data.replace('&#39;', '\'').replace('&quot;', '\"').encode("utf8"))
		out.write(("\r\n\r\n").encode("utf8"))
		i += 1

	out.close()


if __name__ == '__main__':
	main()
