# part3_practice.py

print("연습 문제1.")
import pandas as pd
exam1 = pd.read_csv('data/연습문제/Cars93.csv')

"""
(a): 표본 평균을 계산하는 것으로 데이터로부터 (실험군 혈압 변화-대조건 혈압변화)을 계산한 후 문제에서 요구하는 형태에 맞게 출력한다.
"""
import pandas as pd
exam1 = pd.read_csv('data/연습문제/Rabbit_Five.csv', encoding= 'cp949')

from scipy.stats import ttest_rel

# 필요한 컬럼 각각 할당
bp_change = exam1['BP_change']
treatment = exam1['Treatment']

# Treatment가 Control인 경우(대조군)와 MDL인 경우(실험군)의 BP_change 값 각각 할당
bpc_treat = bp_change[treatment == "MDL"].reset_index(drop = True)
bpc_control = bp_change[treatment == "Control"].reset_index(drop = True)

# (a) 점추정량 = mean(PC_Treat - PC_Control)
diff_avg = (bpc_treat - bpc_control).mean()
diff_avg = round(diff_avg, 2)
print(diff_avg) # 출력값 -4.68

"""
(b)-(c) ttest_rel() 함수를 통해 가설 검정을 수행하고 결과에서 제공하는 검정통계량과 p-값을 각각 문제에서 요구하는 형태에 맞게
출력한다. p-값이 0.001이므로 본 가설 검정은 '기각'한다.
"""
# (b)-(c)

# 대응표본 t검정 수행
a = ttest_rel(bpc_treat, bpc_control)

# (b) 검정 통계량
stat = a.statistic
stat = round(stat, 2)
print(stat) # 출력값 -3.67

# (c) p-값/기각여부
pval = a.pvalue
pval = round(pval, 3)
print(pval) # 출력값 0.001
print('기각')

print("\n 연습 문제2.")
import pandas as pd
exam2 = pd.read_csv('data/연습문제/mtcars2.csv', encoding = 'cp949')

from scipy.stats import f

am = exam2['am']
hp = exam2['hp']

# 수동변속기(am=1)인 자동차의 마력(hp), 자동변속기(am=0)인 자동차의 마력(hp) 각각 할당
manual = hp[am==1].reset_index(drop = True)
auto = hp[am==0].reset_index(drop = True)

# (a) 수동변속 표본분산 / 자동변속 표본분산
var_ratio = manual.var() / auto.var()
print(round(var_ratio, 2)) # 출력값 2.43

# (b)-(c)

# F검정 수행
# (b) 검정통계량 = (a)와 같음
stat = var_ratio
print(stat)

# (c) 유의 확률
# 자유도
df1, df2 = len(manual) - 1, len(auto) -1

# F분포로 확률 계산
pval = 1 - f.cdf(stat, dfn = df1, dfd = df2) # Pr[F> stat]

# 반올림
a = round(var_ratio, 2)
b = round(stat, 2)
c = round(pval, 3)

# 출력
print(a) # (a) 출력값 2.43
print(b) # (b) 검정통계량, 출력값 2.43
print(c) # (c) p-값 , 출력값 0.043
print('기각') # 유의수준 0.05 이내!