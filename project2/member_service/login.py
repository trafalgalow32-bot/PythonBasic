# login.py
from data import db

def login_process(id,pw):
    # if id == "gold" and pw == "123456":
    #     print("로그인 성공")
    # else:
    #     print("아이디 또는 비밀번호를 확인하세요!")

    uid, upw = db.find_by_id(id)
    if uid==id and upw==pw:
        return "로그인 성공했습니다."
    else:
        return "아이디 또는 비밀번호가 잘못됐습니다."