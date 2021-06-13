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
        num3 = float(input('Enter the minuend(first number) : '))
        num4 = float(input('Enter subtrahend(second number) : '))
        print('The difference between',num3,'and',num4,'is',num3-num4)
        print(num3,'-',num4,'=',num3-num4)
        
    def multipy(self):
      mname = self.name
      print('You have chosen multiplication',mname)
      num1 = float(input('Enter multiplicand(the first number) : '))
      num2 = float(input('Enter multiplier(the second number) : '))
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
        if(num2 == 0):
            print(
                'Divisor cannot be zero'
            )

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

    def area(self):
        print('Choose one of the below shapes to find area. Enter the option number')  
        print('1.Square 2.Rectangle 3.Triangle 4.Circle') 
        shape = int(input('Enter the option number of your choise : '))
        if(shape == 1):
            print('You have chosen square')
            side = int(input('Enter the length of the side of the sqaure in cm : '))
            ans = side*side    
            print('Your answer is',ans)
            work = input('Click w to see workout of the sum : ')
            if(work == 'w'):
                print('The side of the square is',side,'. The formula to find area of square is side*side ')
                print('Therefore the answer is : ',side,'*',side,'=',ans)

        if(shape == 2):
            print('You have chosen square')
            side2 = int(input('Enter the length of the side of the rectangle in cm : '))
            side3 = int(input('Enter the breadth of the side of the rectangle in cm : '))
            ans2 = side2*side3  
            print('Your answer is',ans)
            work2 = input('Click w to see workout of the sum : ')
            if(work2 == 'w'):
                print('The length and breadth of the square is',side2,'and',side3,'respectively. The formula to find area of rectangle is length*breadth ')
                print('Therefore the answer is : ',side2,'*',side3,'=',ans2)

        if(shape == 3):
            print('You have chosen triangle')
            side1 = int(input('Enter the height of triangle in cm : '))                
            base = int(input('Enter base of triangle in cm : '))
            answer = 1/2 * side1 * base
            print('Your answer is',answer)
            work3 = input('Click w to see workout of the sum : ')
            if(work3 == 'w' or work3 =='W'):
                print('The base and height of your triangle is',base,'and',side1,'respectively. The formula to find area of triangle is 1/2 * base * height')
                print('Therefore the answer is : 1/2 * ',base,'*',side1,'=',answer)

        if(shape == 4):
            print('You have chosen circle')  
            radius = int(input('Enter radius of circle in cm  : '))
            answer1 = 22/7*radius*radius
            print('Your answer is',answer1)
            work4 = input('Click w to see workout of the sum')
            if(work4 == 'w'):
                print('The radius provided is',radius,'. The area of circle is pie*radius*radius. note:The formula used is 22/7*r*r')
                print('Therefore answer is : 22/7 *',radius,'*',radius,'=',answer1)

    def volume(self):
        print('You have chosen volume' , self.name)
        print('Choose your shape : 1.Cube 2.Cubeoid') 
        shape = int(input('Enter your choise : '))           
        if(shape == 1):
            cube = float(input('Enter side of cube : '))
            ans = cube*cube*cube
            print('Your answer is',ans)
            work = input('Click w to see workout of the sum')
            if(work == 'w'):
                print('The formula of cube is side cube. The side of the cube is',cube,)
                print('Answer: ',cube,'*',cube,'*',cube,'=',ans)
        elif(shape == 2):
            h = float(input('Enter height of cuboid : '))
            b = float(input('Enter breadth of cuboid : '))
            l = float(input('Enter length of cuboid : '))
            ans2 = l*b*h
            print('Your answer is',ans2)
            work = input('Click w to see workout of the sum')
            if(work == 'w'):
                print('The formula of cuboid is l*b*h. l = ',l,'b = ',b,'h =',h)  
                print('Therefore,',l,'*',b,'*',h,'=',ans2)  




def main():
    
    nm = input('Enter your name : ') 
    gr = input('Enter your grade : ')
    user = Cal(nm,gr)
    print('Hello',nm,'. You can use me for calculation')
    print('You have to chose the operation you want to perform.')
    print('You have to choose between : 1.Simple calculator 2.Complex calculator 3.Area and volume')
    helo = int(input('Enter the number of the option'))
    if(helo == 1) :
        print('Enter A for addition , S for subtraction , M for multiplication , D for division')
        bore = input('Enter your choise')
        if(bore == 'A' or bore == 'a'):
            user.add()
        elif(bore == 'S' or bore == 's'):
            user.subtract()
        elif(bore == 'M' or bore == 'm'):
            user.multipy()
        elif(bore == 'D' or bore == 'd'):
            user.division()
            
    elif(helo == 2 ):
        print('Enter Sq to find the square , Sqr to find square root , C to find cube , Cr to find cube root , ')
        bore3 = input('Enter your choise')
        if(bore3 == 'C' or bore3 == 'c'):
            user.cube()  
        elif(bore3 == 'Cr' or bore3 == 'cr'):
            user.croot()   
        elif(bore3 == 'Sq' or bore3 == 'sq'):
            user.square()  
        elif(bore3 == 'Sqr' or bore3 == 'sqr'):
            user.root() 
    
    elif(helo == 3):
        print('Ar to find area or V to find volume')
        bore2 = input('Enter your choise')
        if(bore2 == 'ar' or bore2 == 'Ar'):
            user.area()

        elif(bore2 == 'V' or bore2 == 'v'):
            user.volume()

                      
     
    else:
        print('Enter correct operation')             

    
         

main()
        
