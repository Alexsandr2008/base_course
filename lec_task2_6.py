print("ax^2 + bx + c = 0") 
a = int(input("Введите коэффициент a: "))
b = int(input("Введите коэффициент b: "))
c = int(input("Введите коэффициент с: "))
print("Получилось крадратное уравнение:", a,"x^2 + ", b,"x + ",c,"= 0")
d = b**2 - 4*a*c
x1  = (-b - d * 0.5)/2*a
x2 = (-b + d * 0.5)/2*a
x3 = (-(b/2*a))
print("Дискриминант данного уравнения равен:", d)
if d < 0:
    print("Дискриминант меньше нуля,соответсвенно нет корней")
elif d == 0:
    print("Дискриминант равен нулю, соответсвенно уравнение имеет 1 корень, x =",x3)
else:
    print ("Дискриминант больше нуля, соответсвенно уравнение имеет 2 корня, x1 =",x1,",x2 =",x2)

    
    


