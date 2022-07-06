# DemoRE.py

import re

#print(dir(re))

#특정 규칙이 있는지?
result = re.search("[0-9]*th", "  35th")
print(result)
print(type(result))
print(result.group())

# match 함수
# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

# 우편번호, 연도 검색
result = re.search("\d{4}", "올해는 2022년입니다.")
print(result.group())

result = re.search("\d{5}", "우리 동네는 52300입니다.")
print(result.group())

