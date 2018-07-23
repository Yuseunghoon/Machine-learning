import re
id=''
password=''

while True:
    id=input("ID = ")
    result = re.findall(r"(\w+[\w\.]*)@(\w+[\w\.]*)\.([A-Za-z]+)", id)

    if result == []:
        print("이메일 주소를 정확히 작성해주세요.")
    else:
        break

while True:
    password=input("Password = ")

    alphabet = re.findall(r"[a-z]", password)
    Alphabet = re.findall(r"[A-Z]", password)
    number = re.findall(r"[0-9]", password)

    if len(password)<6 or 12<len(password):
        print("비밀번호 6 ~ 12자")
    elif Alphabet==[]:
        print("영문 대문자 포함")
    elif number==[]:
        print("숫자 포함")
    else:
        break

print(id, password)



