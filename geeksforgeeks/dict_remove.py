myDic = {"swaraj": 21, "suahni": 34, "suhani2": 56, "suhani3": 78}
myDic2 = {31: "suhani", 34: "suhani2", 56: "suhani3", 78: "suhani4"}
del myDic["suahni"]
print(myDic)

del myDic2
try:
    print(myDic2)
except:
    print("myDic2 is deleted!")