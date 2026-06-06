def cal():
    print("0.Exit \n1.Addtion \n2.Subtraction \n3.Multiplication\n4.Division\n5.Modulus %\n6.Power ^\n7.Square\n8.Cube\n9.Sqaure root\n10.Temperature\n11.History")
    history=[]
    while True:
        choose=int(input("Choose:"))
        if choose==0: break
        match choose:
            case 1:
                  no1=int(input("Enter First Number:"))
                  no2=int(input("Enter Secound Number:")) 
                  print("Result:",no1+no2),history.append(f"{no1}+{no2}={no1+no2}")
            case 2:
                  no1=int(input("Enter First Number:"))
                  no2=int(input("Enter Secound Number:"))
                  print("Result:",no1-no2),history.append(f"{no1}-{no2}={no1-no2}")
            case 3:
                  no1=int(input("Enter First Number:"))
                  no2=int(input("Enter Secound Number:"))
                  print("Result:",no1*no2),history.append(f"{no1}*{no2}={no1*no2}")
            case 4:
                no1=int(input("Enter First Number:"))
                no2=int(input("Enter Secound Number:"))
                if no2==0: print("Cannot Divide By Zero"),history.append(f"{no1}+{no2}=Cannot Divide By Zero")
                else:print("Result:",no1/no2),history.append(f"{no1}/{no2}={no1/no2}")
            case 5:
                no1=int(input("Enter First Number:"))
                no2=int(input("Enter Secound Number:"))
                if no2==0: print("Cannot Divide By Zero")
                else:print("Result:",no1%no2),history.append(f"{no1}%{no2}={no1%no2}")
            case 6:
                  no1=int(input("Enter First Number:"))
                  no2=int(input("Enter Secound Number:"))
                  print("Result:",no1**no2),history.append(f"{no1}**{no2}={no1**no2}")
            case 7:
                no1=int(input("Enter Number:"))
                print("Result Power of no1:",no1**2),history.append(f"{no1} Square={no1**2}")
            case 8:
                  no1=int(input("Enter Number:"))
                  print("Result Power of no1:",no1**3),history.append(f"{no1} Cube={no1**3}")
            case 9:
                  no1=int(input("Enter Number:"))
                  print("Result Power of no1:",no1**0.5),history.append(f"{no1} power={no1**0.5}")
            case 10:
                  temp=int(input("Enter The Temperature:"))
                  con=int(input("1.Convert from Celsius to Fahrenheit\n2.Convert from Fahrenheit to Celsius\n"))
                  if con==1:
                       result=(temp*9/5)+32 
                       print(f"result:{result}F")
                       history.append(f"{temp} Converted from Celsius to Fahrenheit={result}")  
                  elif con==2:
                       result=(temp-32)*5/9
                       print(f"result:{result}C")
                       history.append(f"{temp} Converted from Fahrenheit to Celsius={result}") 
                  else: print("Enter From the above options Only..")
            case 11:
                  for iteam in history:
                        print(iteam)
            case _: print("Invalid Input...")
        
cal()