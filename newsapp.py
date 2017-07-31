#!python3
import psycopg2
# import os

#  VVVVVVV  writes/overwites file
# fn = 'outfile.txt'

# try:
#     os.remove(fn)
# except OSError:
#     pass

# file = open(fn, 'w')

# file.write('yoohooo')
# file.close()
# ^^^^^^^^^  writes/overwrites file

conn = psycopg2.connect("dbname=news")
c = conn.cursor()
c.execute("select * from authors;")
rows = c.fetchall()
conn.close()

print(rows)
