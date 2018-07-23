person=[]

import json
import sqlite3  # SQLite3 탑재

class start:

    def create_table(self):
        conn = sqlite3.connect('my_project.db')  # 데이터베이스 커넥션 생성

        cur = conn.cursor()  # 커서 확보

        # 테이블 생성
        cur.execute('''CREATE TABLE my_project (
                            name text,
                            python integer,
                            linux integer,
                            iot integer
                    )'''
                    )

        conn.commit()       # 데이터베이스 반영

        conn.close()        # 커넥션 닫기


    # 데이터 입력 함수
    def insert_project(self, input_data):

        with open('jsondata.json', 'w', encoding="utf-8") as make_file:
            json.dump(input_data, make_file, ensure_ascii=False, indent="\t")

        with open('jsondata.json', 'r', encoding="utf-8") as data_file:
            data = json.load(data_file)

        conn = sqlite3.connect('my_project.db')  # 데이터베이스 커넥션 생성
        cur = conn.cursor()  # 커서 확보

        # 데이터 입력 SQL
        insert_sql = 'INSERT INTO my_project VALUES (?, ?, ?, ?)'

        # 여러 데이터 입력
        cur.executemany(insert_sql, data)

        conn.commit()       # 데이터베이스 반영

        conn.close()        # 커넥션 닫기
        print("".center(60, '-'))


    # 전체 조회용 함수
    def select_project(self, input_name):
        conn = sqlite3.connect('my_project.db')         # 데이터베이스 커넥션 생성
        cur = conn.cursor()                             # 커서 확보

        if input_name == 'all':
            cur.execute('SELECT * FROM my_project')

        elif input_name != 'all':
            cur.execute('SELECT * FROM my_project WHERE name = "%s"' %input_name)

        project_data = cur.fetchall()                          # 조회한 데이터 불러오기
        print()
        print("이름".center(10), "python 점수".center(10), "linux 점수".center(10), "iot 점수".center(10), "3과목 총점".center(10), "평균".center(10))

        for x in project_data:  # 데이터 출력하기
            sum = int(x[1]) + int(x[2]) + int(x[3])
            print(x[0].center(9), str(x[1]).center(11), str(x[2]).center(13), str(x[3]).center(11), str(sum).center(15), str("%.2f").center(10) %(sum/3))
           #print("%s       %d      %.2f" % (x[0], sum, sum / 3), sep='')

        conn.close()                                    # 커넥션 닫기
        print("".center(60, '-'))


    # 데이터 삭제용 함수
    def delete_project(self, input_name):
        conn = sqlite3.connect('my_project.db')  # 데이터베이스 커넥션 생성
        cur = conn.cursor()  # 커서 확보

        if input_name == 'all':
            print("delete all")
            delete_sql = 'DELETE FROM my_project'

        elif input_name != 'all':
            delete_sql = 'DELETE FROM my_project WHERE name is "%s"' % input_name

        # 데이터 삭제 SQL ( 데이터 전체 삭제)

        cur.execute(delete_sql)

        conn.commit()  # 데이터베이스 반영
        conn.close()  # 커넥션 닫기
        print("".center(60, '-'))

list=start()

try:
    list.create_table()
except sqlite3.OperationalError:
    print("")
finally:

    while True:
        print("1. 학생 정보 입력")
        print("2. 학생 정보 찾기")
        print("3. 학생 정보 삭제")
        print("4. 종료")

        select=int(input("선택 : "))

        if select == 1:
            print("학생 정보 입력".center(60, '-'))
            name = input("이름 : ")
            python = input("python 점수 : ")
            linux = input("linux 점수 : ")
            iot = input("iot 점수 : ")

            data=[(name, python, linux, iot)]
            list.insert_project(data)

        elif select == 2:
            print("학생 정보 찾기".center(60, '-'))
            print("1. 전체 리스트")
            print("2. 선택 검색")

            search=int(input("선택 : "))

            if search == 1:
                list.select_project("all")
            elif search == 2:
                search_name = input("이름 : ")
                list.select_project(search_name)

        elif select == 3:
            print("학생 정보 삭제".center(60, '-'))
            print("1. 전체 삭제")
            print("2. 선택 삭제")
            search=int(input("선택 : "))

            if search ==1:
                list.delete_project("all")
            elif search ==2:
                search_name = input("학생 이름 : ")
                list.delete_project(search_name)

        else:
            break


