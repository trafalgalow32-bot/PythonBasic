SECTION 01 | 신용 등급 예측

■ 은행 정보로 신용 등급을 예측하시오.
* 제공된 데이터 목록: score_train.csv, score_test.csv
* 예측할 컬럼: Credit_Score(Good, Standard, Poor)

■ 학습용 데이터(train)를 이용해 신용 등급을 예측하는 모델을 만든 후 이를 평가용 데이터(test)에 적용해 얻은 예측값을 다음과 같은 형식의 CSV 파일로 생성하시오.

제출 파일은 다음 1개의 컬럼을 포함해야 한다.
* pred: 예측값
* 제출 파일명: 'result.csv'

제출한 모델의 성능은 f1-macro 평가지표에 따라 채점한다.
* 제출 csv 파일명 및 형태: result.csv

pred
Poor
Good
Standard
…

---


<br>
<br>

SECTION 02 | 약물 종류 예측

■ 주어진 데이터에서 약물의 종류를 예측하시오.

* 제공된 데이터 목록: drug_train.csv, drug_test.csv
* 예측할 컬럼: Drug(DrugY, drugX, drugA, drugC, drugB)

■ 학습용 데이터(train.csv)를 이용해 약물의 종류를 예측하는 모델을 만든 후 이를 평가용 데이터(test.csv)에 적용해 얻은 예측값을 다음과 같은 형식의 CSV 파일로 생성하시오.

제출 파일은 다음 1개의 컬럼을 포함해야 한다.
* pred: 예측값
* 제출 파일명: 'result.csv'

제출한 모델의 성능은 f1-macro 평가지표에 따라 채점한다.
* 제출 csv 파일명 및 형태: result.csv

pred
drugX
drugA
drugB
…

---

<br>
<br>

SECTION 03 | 유리 종류 예측

■ 유리 식별 데이터에서 유리의 종류를 예측하시오.

* 제공된 데이터 목록: glass_train.csv, glass_test.csv
* 예측할 컬럼: Type(1, 2, 3, 5, 6, 7)

■ 학습용 데이터(train.csv)를 이용해 유리 종류를 예측하는 모델을 만든 후 이를 평가용 데이터(test.csv)에 적용해 얻은 예측값을 다음과 같은 형식의 CSV 파일로 생성하시오.

제출 파일은 다음 1개의 컬럼을 포함해야 한다.
* pred: 예측값
* 제출 파일명: 'result.csv'

제출한 모델의 성능은 f1-weighted 평가지표에 따라 채점한다.
* 제출 csv 파일명 및 형태: result.csv

pred
1
2
3
…

---

<br>
<br>