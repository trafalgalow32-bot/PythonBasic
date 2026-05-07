# tentative05.py

"""
part3. 통계분석
1장. 가설검정
: 추론 통계학에서는 연구자 본인의 의견을 주장하고, 이를 통계적으로 입증하기 위한 방법으로 가설 검정을 이용한다. 
가설 검정은 모집단에 대한 어떤 가설을 설정한 후 그 가설의 타당성 여부를 검정하는 것으로, 주로 모집단의 모수를 검정한다. 
본 장에서는 이러한 가설 검정을 파이썬으로 실습하는 방법에 대해 알아보도록 한다. 

5절. 비모수 검정
- 앞서 배워온 가설 검정들은 모수적 검정으로 알려져 있다. 모수적 검정은 가설 검정 시 분포를 가정하기 때문에 실제 데이터가
가정한 분포와 이질적일수록 잘못된 결론을 내릴 가능성이 높다. 
- 본 수험서에서는 이전 앞의 예제에서는 정규성을 충족한다고 가정하여 제작되었으나 실제 분석에서는 정규성 검정 등이 선행되고,
분포를 충족한 근거가 없을 경우에는 비모수 검정을 수행해야 한다. 
- 이번 절에서는 여러 비모수 검정을 파이썬으로 수행하는 방법에 대해 알아본다.

1. 스피어만 상관계수 겸정
 - 스피어만 상관계수는 spearmanr()로 구할 수 있으며, 이를 사용하는 방법은 어래와 같은 함수를 사용하면 된다. 
 - 파이썬에서 스피어만 상관계수 검정을 수행하기 위해서는 SciPy 패키지의 stats 서브패키지를 호출한 후 stats에서 
 제공하는 spearmanr 함수를 사용한다. 
 
 scipy.stats.spearmanr(a, b)

Q. '1절의 피어슨 상관계수' 대신 스피어만 상관계수로 상관관계를 분석해보자. 
"""
import pandas as pd
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
data = pd.DataFrame(diabetes.data, columns= diabetes.feature_names)

print("비모수 검정 - 스피어만 상관계수")
# scipy.stats.spearmanr
from scipy.stats import spearmanr
print(spearmanr(a = data['sex'], b = data['bmi']))

"""
 - spearmanr()의 결과 상관꼐수가 0.098로 두 컬럼은 서로 상관관계가 적은 것으로 나타났다. 그리고 p-value가 0.039
 로 유의수준 5%에서 귀무가설을 기각하기 때문에 상관계수는 작지만 유의하다는 것을 확인할 수 있다.
 - 스피어만 상관계수도 단순한 상관계수만의 산출은 데이터프레임객체의 메소드 corr()에 옵션 method='spearman'를
 통해 가능하다.
"""

# 단순한 상관계수의 산출은 데이터프레임객체.corr()로 가능
# corr(method = 'spearman')은 스피어만 상관계수를 산출함
print("corr(method = 'spearman')")
print(data[['sex', 'bmi']].corr(method = 'spearman'))

"""
2. 켄달의 타우 검정 : 파이썬에서 켄달(Kendal)의 타우(Tau: τ) 검정을 수행하기 위해서는 SciPy 패키지의 서브 패키지를
호출한 후 stats에서 제공하는 kendalltau 함수를 사용한다. 
scipy.stats.kendalltau(x, y, alternative='two-sided', ...)

Q. 두 개의 등수 데이터를 임의로 생성하고 두 순위 간 상관관계가 있는지 검정해보자. 
"""
print("\n 켄달의 타우 검정")
import numpy as np
# 두 개의 등수 데이터 임의로 생성
x = np.array([5,4,3,6,1,2])
y = np.array([1,5,2,2,2,6])

# 켄달의 타우 검정 실시
from scipy.stats import kendalltau
print(kendalltau(x, y))

"""
 -kendalltau() 함수의 결과는 (상관계수, p-value) 형태로 제공되며, (correlation = -0.29814239699997197, pvalue=0.4205962375999266)
 로 상관계수가 -0.298로 순위 간 상관관계가 거의 없는 것으로 확인되었다.
 - (참고) 스피어만 상관계수 검정은 켄달 타우 검정과 마찬가지로 순위 데이터에 대해서도 검정을 수행할 수 있다.
"""

"""
3. 윌콕슨 부호순위 검정 : 파이썬에서 윌콕슨의 부호순위 검정(Wilcoxon's Signed Rank Test)을 수행하기 위해서는 SciPy
패키지의 stats 서브패키지를 호출한 후 stats에서 제공하는 wilconxon 함수를 사용한다. 
scipy.stats.wilcoxon(x, y, alternative='two-sided',...)

Q. '3절의 단일표본 t-검정' 대신 일표본 우선순위 검정을 수행해보자.
"""
print("\n 윌콕슨 부호순위 검정")
from scipy.stats import wilcoxon

# 일표본 윌콕슨 부호순위 검정
# 몸무게 데이터 임의 생성
kg = np.array([75.5, 83.9, 75.7, 56.2, 73.4, 67.7, 79.0, 50.7, 58.4, 74.1, 65.1, 77.8, 48.1, 46.3])

# 두 샘플의 크기가 다를 수 있으므로 길이를 맞추기
print(wilcoxon(kg - 70)) # 70으로 설정

"""
- wilcoxon() 함수의 결과는 (검정통계량, p-value) 형태로 제공되며, (statistic=42.0, pvalue=0.5416259765625)
로 p-value는 0.542로 귀무가설을 기각하지 못하므로 모집단의 중위수가 70과 같다고 할 수 있다. 

Q. '3절의 대응표본 t-검정' 대신 이표본 부호순위 검정을 수행해보자
"""
print("이표본 윌콕슨 부호순위 검정")

# 남녀 몸무게 데이터를 임의로 생성
female = np.array([50.7, 58.4, 74.1, 65.1, 77.8, 48.1, 46.3])
male = np.array([75.5, 83.9, 75.7, 56.2, 73.4, 67.7, 79.0])

# 두 데이터의 차이
diff = female - male

# 윌콕슨 부호순위 검정 실시
print(wilcoxon(diff))
"""
-wilcoxon() 함수의 결과는 (통계량, p-value) 형태로 제공되며, (statistic=5.0, pvalue=0.15625)
로 p-value는 0.156로 유의수준 5%에서 두 표본의 중앙값에 유의한 차이가 없다는 것을 확인할 수 있다.
"""

"""
4. 윌콕슨의 순위합 검정 : 파이썬에서 윌콕슨의 순위합 검정(Wilcoxon's Rank Sum Test)을 수행하기 위해서는
SciPy 패키지의 stats 서브패키지를 호출한 후 stats에서 제공하는 ranksums 함수를 사용한다.

scipy.stats.ranksums(x, y, alternative='two-sided',...)
Q. '3절의 독립표본 t-검정' 대신 순위합 검정을 수행해보자.
"""
print("\n 윌콕슨의 순위합 검정")
from scipy.stats import ranksums
print(ranksums(female, male))

"""
- ranksums() 함수의 결과는 (검정통계량, p-value) 형태로 제공되며, RanksumsResult(statistic=-1.8527420384998257, pvalue=0.06391934147515746)
로 p-value가 0.064로 유의수준 5%에서 귀무가설을 기각하지 못하므로 두 표본의 중앙값에 유의한 차이가 없다는 것을 확인할 수 있다.
"""

"""
5. 만-위트니 U 검정 : 파이썬에서 만-위트니 U 검정(Mahn-Whitney U Test)을 수행하기 위해서는 SciPy 패키지의
stats 서브패키지를 호출한 후 stats에서 제공하는 mannwhiteyu 함수를 사용한다.

scipy.stats.mannwhitneyu(x, y, alternative='two-sided',...)

Q. '3절의 독립표본 t-검정' 대신 만-위트니 U 검정을 수행해보자.
"""
# 만 위트니 U검정 수행
print("\n 만 위트니 U검정 수행")
from scipy.stats import mannwhitneyu
print(mannwhitneyu(female, male))

"""
- mannwhitneyu() 함수의 결과는 (검정통계량, p-value) 형태로 제공되며, (statistic=10.0, pvalue=0.07284382284382285)
로 p-value가 0.073으로 유의수준 5%에서 귀무가설을 기각하지 못하므로 두 표본의 중앙값에 유의한 차이가 없다는 것을 
확인할 수 있다.
"""

"""
6. 크루스칼-왈리스 H 검정 : 파이썬에서 크루스칼-왈리스 H 검정(Kruskal-Wallis H Test)을 수행하기 위해서는
SciPy 패키지의 stats 서브 패키지를 호출한 후 stats에서 제공하는 kruskal 함수를 사용한다.

scipy.stats.krusal(a, b, c, ...)

Q. '3절의 일원배치 분산분석'에서 사용한 데이터를 활용해 크루스칼-왈리스 H 검정을 수행해보자.
"""
print("\n 크루스칼-왈리스 H 검정")

df = pd.read_csv('data/예제/school_score.csv')

# 입력 형태에 맞게 데이터 추출, 필요한 컬럼 각각 할당
School = df['School']
Final = df['Final']

# School에 대해 각각 기말고사 점수 분리
Final_A = Final[School == 'A'].reset_index(drop = True)
Final_B = Final[School == 'B'].reset_index(drop = True)
Final_C = Final[School == 'C'].reset_index(drop = True)

# 크르수칼-왈리스 검정 수행
from scipy.stats import kruskal
print(kruskal(Final_A, Final_B, Final_C))

"""
-kruskal() 함수의 결과는 (통계량, p-value) 형태로 제공되며 (statistic=1978.1734792103248, pvalue=0.0)
로 귀무가설을 기각하기 때문에 학교 간 기말고사에는 통계적으로 유의미한 차이가 있음을 확인할 수 있다.
"""