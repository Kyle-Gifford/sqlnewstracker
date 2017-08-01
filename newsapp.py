#!python3
import psycopg2
import datetime

conn = psycopg2.connect("dbname=news")
c = conn.cursor()
command = 'select articles.title as article, subtable.count as views from articles join (select substring(path, 10) as slug_log, count(*) from log group by path order by count desc limit 3 offset 1) as subtable on articles.slug = subtable.slug_log order by count desc;'
c.execute(command)
rows = c.fetchall()
print('Three most popular articles:')
for row in rows:
    print('"' + row[0] + '" \u2014 ' + str(row[1]) + ' views')

command = 'select a.name as author, s.sum as "total views" from authors as a join (select sub.author, sum(sub.views) from (select articles.author as author, subtable.count as views from articles join (select substring(path, 10) as slug_log, count(*) from log group by path order by count desc offset 1) as subtable on articles.slug = subtable.slug_log order by count desc) as sub group by sub.author) as s on a.id = s.author order by sum desc;'
c.execute(command)
rows = c.fetchall()
print('\n')
print('Most popular authors:')
for row in rows:
    print(row[0] + ' \u2014 ' + str(row[1]) + ' views')
print('\n')

command = """
select * from (select ecodes.month, ecodes.day, ecodes.year, round(ecodes.errors*100.0/allent.count, 1) as errorpct from (select extract (month from time) "month", extract(day from time) "day", extract(year from time) "year", count(*) as errors from log where status like '4%' group by (month, day, year) order by errors desc) as ecodes left join (select extract (month from time) "month", extract(day from time) "day", extract(year from time) "year", count(*) from log group by (month, day, year)) as allent on (ecodes.month = allent.month) and (ecodes.day = allent.day) and (ecodes.year = allent.year)) as q where q.errorpct > 1;
"""
c.execute(command)
rows = c.fetchall()
print('Days with more than 1% errors:')
for row in rows:
    month = (str(int(row[0])))
    day = (str(int(row[1])))
    year = (str(int(row[2])))
    pct = (str(float(row[3])))
    input = day + '/' + month + '/' + year
    my_date = datetime.datetime.strptime(input, "%d/%m/%Y")
    print(my_date.strftime("%b %d, %Y") + ' \u2014 ' + pct + '% errors')

conn.close()
