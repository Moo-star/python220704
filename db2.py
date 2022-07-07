# db1.py

import sqlite3
#from this import s

# 영구적으로 파일에 저장
con = sqlite3.connect("c:\\work\\sample.db")

# 메모리에 저장
#con = sqlite3.connect(":memory:")

# 커서객체를 리턴
cur = con.cursor()
# 데이터를 저장할 테이블 생성
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
# 1건 입력
cur.execute("insert into PhoneBook values ('derick', '010-222');")
#입력 파라메터 처리
name = "gildong"
phoneNumber = "010-123"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))
# 다중 레코드 입력
datalist = (("tom", "010-345"), ("dsp", "010-333"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

# 검색
cur.execute("select * from PhoneBook;")

print("---fetchone---")
print(cur.fetchone())
print("---fetchmany---")
print(cur.fetchmany(2))
print("---fetchall()---")
print(cur.fetchall())

# 정상적으로 완료
con.commit()