# Part 2(작업형1) 5/22 오답 및 핵심 요약 노트

## 4. 정규화된 값에 필터링!

| 오답 | 정답 |
| :--- | :--- |
| `cond1 = df[mms < 0.5].var()` | `cond1 = mms[mms < 0.5].var()` |
| `cond2 = df[mms > 0.5].var()` | `cond2 = mms[mms > 0.5].var()` |

* **피드백:** 내가 적은 방식으로 하면... 정규화 시키기 전의 값으로 필터링 하게 됨! 정규화를 거친 값에 필터링이 되게 하려면 필터링 할 때도 정규화 시킨 값을 제시해야!

---

## 5. 함수 숙지

* **`drop_duplicates()` 함수 숙지 필요**
* **`sub_str` 숙지 필요**
  * `exam5['sub_str'] = exam5['Manufacturer'].str[:2]`

---

## 6. `groupby` 함수 숙지 필요

* `groupby([column])(record)` : one column
* `groupby([[column1, column2]])(record)` : many columns

---

## 7. Z점수 표준화 공식 숙지 필요

* **공식:** `(컬럼 값 - 컬럼 값의 평균) / 컬럼 값의 표준편차`
* **예시:**
  ```python
  (exam7['Wheelbase'] - exam7['Wheelbase'].mean()) / exam7['Wheelbase'].std()