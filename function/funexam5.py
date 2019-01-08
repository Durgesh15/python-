def fn(a, b) :     
    temp = 1
    for iter in range(b) :
        temp = temp*a
    return temp

print(fn(2, 4))

print(temp) # error : can not access 'temp' out of scope of function 'fn'
print(iter)