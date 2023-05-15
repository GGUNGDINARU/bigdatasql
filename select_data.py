import sqlite3

# sqlite db 파일 생성 및 연결
con = sqlite3.connect('dbdb.db')
cursor = con.cursor()
# sql 문장을 실행시키기 위해 준비

sql = '''
SELECT * FROM Person
'''
cursor.execute(sql)
# sql 을 실행
data = cursor.fetchone() #하나만
print(data)

all_data = cursor.fetchall() #전체
print(all_data)