import math
class Cal(object):
    def __init__(self,name,grade):
       self.name = name
       self.grade = grade

    def add(self):
       mname = self.name
       print('You have chosen addition',mname)
       num1 = int(input('Enter first addend : '))
       num2 = int(input('Enter second addend : '))
       print('The sum is',num1+num2)
       print(num1,'+',num2,'=',num1+num2)

    def subtract(self):
        m_name = self.name
        print('You have chosen Subtraction',m_name)  
        num3 = int(input('Enter the minuend(first number) : '))
        num4 = int(input('Enter subtrahend(second number) : '))
        print('The difference between',num3,'and',num4,'is',num3-num4)
        print(num3,'-',num4,'=',num3-num4)
        
    def multipy(self):
      mname = self.name
      print('You have chosen multiplication',mname)
      num1 = int(input('Enter multiplicand(the first number) : '))
      num2 = int(input('Enter multiplier(the second number) : '))
      print('The product is',num1*num2)
      print(num1,'*',num2,'=',num1*num2)   

    def division(self):
        mname = self.name
        print('You have chosen division',mname)
        num1 = int(input('Enter the dividend(the big number) : '))
        num2 = int(input('Enter the divisor(the small number) : ')) 
        ans = divmod(num1,num2)
        print('The quotient is',ans[0],'and the remainder is',ans[1]) 
        print(num1,'/',num2,'=',ans[0])

    def root(self):
        mname = self.name
        print('You have chosen square root',mname)
        num1 = int(input('Enter number to find square root : '))
        ans = math.sqrt(num1)
        print('The square root of',num1, 'is',ans)
        print('√',num1,'=',ans)

    def square(self):
        mname = self.name
        print('You have chosen to find the square',mname)
        num1 = int(input('Enter number to find the square : '))    
        ans = num1*num1
        print('The square of',num1,'is',ans)
        print(num1,'^2','=',ans)

    def cube(self):
        mname = self.name
        print('You have chosen to find the cube',mname)   
        num1  = int(input('Enter number to find the cube : ')) 
        ans = num1*num1*num1
        print('The cube of',num1,'is',ans)
        print(num1,'^3','=',ans)

    def cube_root(x):
        return x**(1/3)

    def croot(self):
        mname = self.name
        print('You have chosen cube root',mname)
        num1 = int(input('Enter number to find cube root : '))
        ans = Cal.cube_root(num1)
        print('The cube root of',num1, 'is',ans)
        print('3√',num1,'=',ans)   



def main():
    
    nm = input('Enter your name : ') 
    gr = input('Enter your grade : ')
    user = Cal(nm,gr)
    print('Hello',nm,'. You can use me for calculation')
    print('You have to chose the operation you want to perform.')
    print('Enter A for addition , S for subtraction , M for multiplication , D for division')
    print('Enter Sq to find the square , Sqr to find square root , C to find cube , cr to find cube root')
    bore = input('You have chosen : ')
    if(bore == 'A' or bore == 'a'):
        user.add()
    elif(bore == 'S' or bore == 's'):
        user.subtract()
    elif(bore == 'M' or bore == 'm'):
        user.multipy()
    elif(bore == 'D' or bore == 'd'):
        user.division()
    elif(bore == 'C' or bore == 'c'):
        user.cube()  
    elif(bore == 'Cr' or bore == 'cr'):
        user.croot()   
    elif(bore == 'Sq' or bore == 'sq'):
        user.square()  
    elif(bore == 'Sqr' or bore == 'squr'):
        user.root()            
    else:
        print('Enter correct operation')             


main()
        
