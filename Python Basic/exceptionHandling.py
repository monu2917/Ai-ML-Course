
try :
    x=int(input("enter a number"))
    ans =5/x
except  ZeroDivisionError :
    print("zero division error")
except ValueError :
    print("invalid input")
else:
    print("no exception")
print(ans)
finally:
    print("finally block")