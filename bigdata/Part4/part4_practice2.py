# part4_practice2.py
print("연습 문제2.")
"""
본 풀이 과정 외 다양한 풀이가 나올 수 있으며 유의하고 최종 제출 코드의 실행 시간이 
1분 이내가 되어야 함을 반드시 고려해야 한다. 또한 본 풀이를 참고하여 여러 가지 방법을 
익히되 실제 시험에서 적용할 경우 다소 코딩에 많은 시간이 소요될 수 있으니 
일부만을 선택하여 사용하는 방법도 고려하자.
"""

import pandas as pd
X_train = pd.read_csv('data/연습문제/College_X_train.csv', encoding='cp949')
X_test = pd.read_csv('data/연습문제/College_X_test.csv', encoding='cp949')
y_train = pd.read_csv('data/연습문제/College_y_train.csv', encoding='cp949')

# 데이터 확인 (라인 바이 라인)
# print(X_train.head())
# print(X_test.head())
# print(y_train.head())

# 데이터셋 요약 정보 확인 (라인 바이 라인)
# print(X_train.info())
# print(X_test.info())
# print(y_train.info())

# 수치형 컬럼들의 기초 통계 확인 (라인 바이 라인)
# print(X_train.describe())
# print(X_test.describe())

#### 데이터셋 전처리
##### 불필요한 컬럼 삭제
# ID 컬럼은 학교에 대한 고유 정보로 key 역할로 모델에는 불필요함
# Name 컬럼도 학교명에 대한 고유 정보로 key 역할로 모델에는 불필요함
# 결과 제출 시에는 X_test의 ID 컬럼이 필요하기 때문에 별도 저장
ID = X_test['ID'].copy()

# 데이터들에서 ID 컬럼 삭제
X_train = X_train.drop(columns = ['ID', 'Name'])
X_test = X_test.drop(columns = ['ID', 'Name'])
y_train = y_train.drop(columns = 'ID')

# 결측치 확인
X_train.isna().sum()
# print(X_train.isna().sum()) 
X_test.isna().sum()
# print(X_test.isna().sum())

##### 수치형 컬럼 전처리
# Top10perc,Top25perc, PhD, Terminal, S.F.Ratio, Grad.Rate, perc.alumni
# 위 7개 컬럼은 비율에 관한 컬럼으로 단위는 백분율임
# 이를 소수점으로 변환
col_per = ['Top10perc','Top25perc', 'PhD', 'Terminal', 'S.F.Ratio', 'Grad.Rate', 'perc.alumni']
X_train[col_per] = X_train[col_per]/100
X_test[col_per] = X_test[col_per]/100

####### 수치형 컬럼 간 상관관계 확인
# print(X_train.corr()) # ??? 
col_del = ['Apps','Accept','F.Undergrad','Top25perc','Terminal']
X_train = X_train.drop(col_del, axis = 1)
X_test = X_test.drop(col_del, axis = 1)

"""
데이터 분할
모델의 과적합(over-fitting) 방지와 적절한 튜닝을 위해 문제에서 주어진 
X_train, y_train을 학습용(X_TRAIN, y_TRAIN)과 검증용(X_VAL, y_VAL)으로 분할하였다. 
분할 비율은 9:1로 정하였다.
"""

# 데이터 분할
from sklearn.model_selection import train_test_split

X_TRAIN, X_VAL, y_TRAIN, y_VAL = train_test_split(X_train, y_train,
                                                  random_state = 1234,
                                                  test_size = 0.1,
                                                  stratify = y_train)

# 분할 후 shape 확인
print(X_TRAIN.shape) # 출력값 (558, 12)

print(X_VAL.shape) # 출력값 (63, 4)

print(y_TRAIN.shape) # 출력값 (558, 1)

print(y_VAL.shape) # 출력값 (63, 1)

"""
스케일링
본 분석에서는 위에서 선별한 수치형 컬럼에 대하여 z-점수 표준화를 수행한다.
스케일링 시 X_TRAIN의 평균과 표준편차를 X_VAL, X_TEST에 반영하기 위하여, 
스케일러 객체 생성 후 .fit() 메소드를 학습데이터에만 적용하고 .transform()은 
모든 데이터에 적용하여 표준화한다.
"""

# 스케일링
from sklearn.preprocessing import StandardScaler

# TRAIN 데이터 기준으로 스케일링
scale = StandardScaler().fit(X_TRAIN) # X_TRAIN_conti은 오타인듯 ㅡㅡ;;

# z점수 표준화
X_TRAIN_STD = scale.transform(X_TRAIN)
X_VAL_STD = scale.transform(X_VAL)
X_TEST_STD = scale.transform(X_test)

# 입력 데이터셋 준비
X_TRAIN = X_TRAIN_STD
X_VAL = X_VAL_STD

y_TRAIN = y_TRAIN.values.ravel()
y_VAL = y_VAL.values.ravel()

"""
모델 학습
준비된 입력 데이터셋 X_TRAIN과 y_TRAIN을 통해 모델을 학습한다. 
본 풀이에서는 Random Forest, Bagging, AdaBoost를 모형 후보로 정하였다.

Random Forest
sklearn.ensemble 내 RandomForestClassifier 클래스를 사용하여 모형 객체를 생성하고 입력 데이터를 통해 
학습하였다.

하이퍼파라미터(트리의 수)는 500, max_depth(트리의 최대 깊이)는 3, 
min_samples_leaf(리프 노드에 있어야 하는 최소 샘플 수)는 10, 
max_features(최적 분할 찾을 때 고려할 컬럼 수)는 'sqrt'(입력 데이터의 컬럼 수의 양의 제곱근)으로 설정하였다.
"""

# 모델 학습
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier

##### Random Forest
rf = RandomForestClassifier(n_estimators = 500,
                            max_depth = 3,
                            min_samples_leaf = 10,
                            max_features = 'sqrt',
                            random_state = 2022)
model_rf = rf.fit(X_TRAIN, y_TRAIN)

"""
Bagging
sklearn.ensemble 내 BaggingClassifier 클래스를 사용하여 모형 객체를 생성하고 입력 데이터를 통해 학습하였다.

하이퍼파라미터는 base_estimator(데이터의 랜덤 부분집합에 적합할 추정기)는 DecisionTreeClassifier, 
n_estimators(앙상블할 추정기의 수)는 500으로 설정하였고 
DecisionTree의 하이퍼파라미터도 max_depth(트리의 최대 깊이)는 3, 
min_samples_leaf(리프 노드에 있어야 하는 최소 샘플 수)는 10으로 설정하였다.
"""

# Bagging
dtr = DecisionTreeClassifier(max_depth = 3, min_samples_leaf = 10)
bag = BaggingClassifier(estimator = dtr, # base_estimator 안씀!
                        n_estimators = 500,
                        random_state = 2022)
model_bag = bag.fit(X_TRAIN, y_TRAIN)

"""
AdaBoost
sklearn.ensemble 내 AdaBoostClassifier 클래스를 사용하여 모형 객체를 생성하고 입력 데이터를 통해 학습하였다.

하이퍼파라미터는 base_estimator(부스팅할 앙상블의 기본 추정기)는 DecisionTreeClassifier, 
n_estimators(부스팅이 종료되는 최대 추정기의 수)는 500으로 설정하였고, 
learning_rate(부스팅 반복 시 각 추정기에 적용되는 가중치)는 0.5로 설정하였다. 
DecisionTree의 하이퍼파라미터도 max_depth는 3, min_samples_leaf는 10으로 설정하였다.
"""

###### AdaBoost
dtr = DecisionTreeClassifier(max_depth = 3, min_samples_leaf =10)
ada = AdaBoostClassifier(estimator = dtr, # base_estimator 안씀! 
                         n_estimators = 500,
                         learning_rate = 0.5,
                         random_state = 2022)
model_ada = ada.fit(X_TRAIN, y_TRAIN)

"""
성능평가를 통한 모델 선정
학습된 세 가지 모델과 검증데이터(X_VAL)를 통해 결과를 예측하고 y_VAL과 비교한 후 
가장 우수한 성능을 가지는 모델을 선택한다.(성능은 문제에 주어진 AUC 기준)

roc_curve() 함수 사용시 현재 주어진 y가 1, 0이 아닌 'Yes', 'No'로 되어있으므로 
pos_label = 'Yes' 옵션을 추가해야 한다.

AUC를 비교한 결과 AdaBoost를 최종 모델로 선정하였다.
"""
###### 성능평가(기준: AUC)를 통한 모델 선정
from sklearn.metrics import roc_curve, auc

# 검증용 데이터셋을 통한 예측
score_rf = model_rf.predict_proba(X_VAL)[:,1]
score_bag = model_bag.predict_proba(X_VAL)[:,1]
score_ada = model_ada.predict_proba(X_VAL)[:,1]

# AUC 계산
fpr, tpr, thresholds = roc_curve(y_VAL, score_rf, pos_label = 'Yes')
auc_rf = auc(fpr, tpr)
print(auc_rf) # 출력값 0.9641943734015346

fpr, tpr, thresholds = roc_curve(y_VAL, score_bag, pos_label = 'Yes')
auc_bag = auc(fpr, tpr)
print(auc_bag) # 출력값 0.938618925831202

fpr, tpr, thresholds = roc_curve(y_VAL, score_ada, pos_label = 'Yes')
auc_ada = auc(fpr, tpr)
print(auc_ada) # 출력값 0.9757033248081841

"""
결과 제출물 구현
학습된 모델과 준비된 X_TEST를 통해 문제에서 요구하는 예측확률을 구하고 .csv 파일로 저장한다.

실제 시험에서 답 제출 시에는 성능이 가장 우수한 모형 하나만 구현하면 되며, 
문제의 요구 사항에 알맞은 형태로 .csv 파일을 제출해야한다.
"""
##### 결과 제출하기
###### 실제 시험에서 답 제출시에는 성능이 가장 우수한 모형 하나만 구현!
X_TEST = X_TEST_STD
y_score = model_ada.predict_proba(X_TEST)[:,1]

# 문제에서 요구하는 형태로 변환
obj = {'ID' : ID, 
       'prob_private' : y_score}
result = pd.DataFrame(obj)

# 12345.csv 이름으로 저장하기
result.to_csv("12345.csv", index = False)

"""
모델 평가(번외)
본 교재에서 제공하는 평가데이터(College_y_test.csv)를 불러와 AUC로 모형을 평가해보자.
"""

##### 채점 모델 평가(번외)
# 실제값
actual = pd.read_csv('data/연습문제/College_y_test.csv', encoding= 'cp949')
actual = actual['Private'] # .ravel()은 삭제

# 채점 기준이 될 성과지표 값
fpr, tpr, thresholds = roc_curve(actual, y_score, pos_label= 'Yes')
final_auc = auc(fpr, tpr)
print(final_auc) # 출력값 0.9641943734015346