# DemoStr.py

# print(dir(str))

strA = "python is very powerful"
strB = "파이썬은 강력해"

print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.count("P"))
print(strA.count("P", 7))
print(strA.startswith("python"))
print(strA.endswith("ful"))
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("MBC2580".isdecimal())

u = "<<<>'''spam and ham>dd>>"
result = u.strip("<> 'd")
print(u)
print(result)

result = result.replace("spam", "spam egg")
print(result)
#productlist.csv, customer.tsv 형식
result = "spam::egg::ham"
lst = result.split("::")
print(lst)
print(":)".join(lst))




