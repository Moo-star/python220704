# DemoList.py

strB = """이 문장은
다음 라인으로 
저장합니다.
"""
# 디버깅시에 중단점(Break point)
print(strB)

#list
colors = ["red", "blue", "green"]
print(len(colors))
print(colors[0])
print("===============")

colors.append("white")
colors.insert(1, "yellow")
colors += "red"


#colors.remove("red")
colors.remove("blue")


# tuple
tp = (1, 2, 3)
print(len(tp))
print(tp[0])
print("id : %s, name: %s" % ("kim", "La"))


print("--형식변환--")
a = set((1,2,3))
b = list(a)
b.append(4)


