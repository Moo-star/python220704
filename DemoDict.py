# DemoDict.py

device = {"이어폰" : 5, "아이패드" : 10, "윈도우": 11}
device["갤럭시"] = 12

for item in device.items():
    print(item)

for k, v in device.items():
    print(k, v)

key = list(device.keys())
print(key)
print(device.values())

del device["이어폰"]
print(device)


print("=====================================")
device2 = device
device2["what"] = 10

for key in device2.keys():
    print(key)


print(1 < 2)