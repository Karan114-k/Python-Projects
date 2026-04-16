class calculator:
    def add(self,numbers):
        return sum(numbers)

    def substract(self,numbers):
        result= numbers[0]
        for num in numbers[1:]:
            result-=num
        return result

    def multiplication(self,numbers):
        result = numbers[0]
        for num in numbers[1:]:
            result*=num
        return result

    def division(self,numbers):
        result= numbers[0]
        for num in numbers[1:]:
            if num == 0:
                print("Can't divide by 0")
            result/=num
        return result
calc = calculator()
print(": Calculator :")
print("'1'. Addition ")
print("'2'. Substraction ")
print("'3'. Multiplication ")
print("'4'. Division ")
choice = input("Your choice 1/2/3/4 ")
 
numbers=[]
n=int(input("How many Numbers "))
for i in range(n):
    numbers.append(float(input(f"enter number {i+1} ")))

if choice=="1":
    print(calc.add(numbers))
elif choice=='2':
    print(calc.substract(numbers))
elif choice =='3':
    print(calc.multiplication(numbers))
elif choice == '4':
    print(calc.division(numbers))
else:
    print(" please ,enter a valid option")
