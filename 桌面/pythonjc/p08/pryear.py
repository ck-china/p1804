years=int(input("今年是哪一年啊？"))
if years % 4 == 0 and years % 100 != 0:
    print('闰年')
elif years % 400 == 0:
    print('闰年')
else:
    print('平年')
