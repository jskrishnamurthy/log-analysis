#!/usr/bin/env python
# log analysis project

import psycopg2

DB_Name = "news"

# define sql queries
popularArticles_sql = """select Replace(path,'/article/','') as Article_Name,
count(*) as Total_ArticleViews from log
where path <> '/' group by path
order by count(*) desc limit 3;"""

populatArticleAuthors_sql = """select authors.name as Author_Name,
count(*) as Total_ArticleViews_PerAuthor
from articles inner join authors
on authors.id = articles.author
inner join log on Replace(log.path,'/article/','') = articles.slug
where log.path <> '/' group by authors.name
order by count(*) desc;"""

failurePercentage_sql = """select ErrorLogs.logTimestamp as Error_Date,
cast((ErrorLogs.logCount::decimal/(ErrorLogs.logCount::decimal+
SuccessLogs.logCount::decimal))
* 100 as decimal(18,2)) as FailPercentage
from ErrorLogs join SuccessLogs
on ErrorLogs.logTimestamp = SuccessLogs.logTimestamp
where cast((ErrorLogs.logCount::decimal/(ErrorLogs.logCount::decimal+
SuccessLogs.logCount::decimal))
* 100 as decimal(18,2)) > 1;"""


def executeSql(sqlQuery):
    try:
        conn = psycopg2.connect(database=DB_Name)
        cursor = conn.cursor()
        cursor.execute(sqlQuery)
        results = cursor.fetchall()
        conn.close()
        return results
    except Exception as identifier:
        print("Exception processing:" + sqlQuery + ". Message:" + identifier)
        raise


def popularArticles(sqlQuery):
    results = executeSql(sqlQuery)
    # format and print results
    print('\n 1. Most popular three articles of all time: \n')
    for row in results:
        print('\t' + str(row[0]) + '--' + str(row[1]) + ' views')


def popularArticleAuthors(sqlQuery):
    results = executeSql(sqlQuery)
    # format and print results
    print('\n 2. Most popular article authors of all time: \n')
    for row in results:
        print('\t' + str(row[0]) + '--' + str(row[1]) + ' views')


def failurePercentage(sqlQuery):
    results = executeSql(sqlQuery)
    # format and print results
    print('\n 3. More than 1percent of errors On: \n')
    for row in results:
        print('\t' + str(row[0]) + '--' + str(row[1]) + '%' + ' errors')


if __name__ == '__main__':
    # execute queries and print
    popularArticles(popularArticles_sql)
    popularArticleAuthors(populatArticleAuthors_sql)
    failurePercentage(failurePercentage_sql)
