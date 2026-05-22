# 조건 생성 (세 제조사 중 하나라도 포함되어 있으면 True)
cond_make = exam10['Make'].str.contains('Chevrolet|Pontiac|Hyundai')

# 데이터프레임 조회하기!
print(exam10[cond_make])

cond_make = exam10['Make'].str.startswith(('Chevrolet', 'Pontiac', 'Hyundai'))
print(exam10[cond_make])

# 만약 Manufacturer 컬럼을 쓴다면 이렇게 정확하게 매칭할 수 있습니다.
cond_manufacturer = exam10['Manufacturer'].isin(['Chevrolet', 'Pontiac', 'Hyundai'])
print(exam10[cond_manufacturer])