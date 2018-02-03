#!/usr/bin/python

import sqlite3
import re
import codecs
import sys
from os import listdir, unlink
from os.path import isfile, join

def get_files(directory):
    return [f for f in listdir(directory) if isfile(join(directory, f))]


def format(string):
    string = re.sub("<[^>]+>", "", string).strip()
    string = re.sub('&nbsp;', ' ', string)
    return re.sub('\s+', ' ', string)

if __name__ == '__main__':
    fname = "/home/kuba/projects/jcubic/kopalinski/www.slownik-online.pl/kopalinski/C0DE03A84FD0096AC12565E20059E117.php"
    if len(sys.argv) != 2:
        print "usage: %s filename" % sys.argv[0]
        exit()
    if isfile(sys.argv[1]):
        unlink(sys.argv[1])
    conn = sqlite3.connect(sys.argv[1])
    c = conn.cursor()
    c.execute('''CREATE TABLE terms(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(500),
                    description text
                 )''')
    path = './www.slownik-online.pl/kopalinski/'
    UTF8Writer = codecs.getwriter('utf8')
    sys.stdout = UTF8Writer(sys.stdout)
    sys.stderr = UTF8Writer(sys.stderr)
    for fname in get_files(path):
        with codecs.open("".join([path,fname]), encoding='utf8') as f:
            page = f.read()
            m = re.search(r"<table border=0>\n<tr><td width=20>\n<A name=.*?<B><FONT[^>]+>([^>]+)</FONT>(.*?)</table>", page, re.DOTALL | re.MULTILINE)
            if m:
                # will fail on index files
                groups = m.groups()
                name = groups[0]
                description = format(groups[1])
                c.execute("INSERT INTO terms(name, description) VALUES(?, ?)", (name, description))
                print name

    conn.commit()
    conn.close()

