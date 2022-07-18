a=int(input("enter marks"))
if a>90:
    print("outstanding:")
elif a>80:
    print("excellent")
elif a>60:
    print('good')
elif a>40:
    print("poor")
elif a<40:
    print("fail")
else:
    print("out of range")
