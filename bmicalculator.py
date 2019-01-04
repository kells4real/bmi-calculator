def hmeters (x, y):
    return round(x / y, 3)
def cmeter (x, y):
    return round(x / y, 3)
def grandcm (x, y):
    return x / y
def bmi (x,y,z):
    return round(x / y / z)
meter = 3.28
c_meter = 0.394
grand = 100

print("................................................................KELLS'S BMI CALCULATOR...........................................................................")
print()
def re_run(): #This is the main function to allow for re-running the program to calculate for another BMI
    try: #Try block to catch errors due to wrong input from user 
        num1 = float(input("Enter height in ft: "))#Get input from the user
        num2 = float(input("Enter remaining height in inches: "))#Get input from the user
        weight = float(input('Enter weight in Kg: '))#Get input from the user
        sex = input("Gender:- m/f: ")#Get input from the user
    except IndexError:
        print("Index Error, please try again..")
        re_run()
    except ValueError:
        print("Value Error, please enter a valid input..")
        re_run()
    except Exception:
        print("An Error occured, please input correct values..")
        re_run()

    def main(): #This is the main function within the main function
        result1 = hmeters(num1, meter)#Store the result of hmeters() inputed value in variable result1
        result2 = cmeter(num2, c_meter)#Store the result if cmeters() inputed value in variable result2
        print(num1,'ft',num2,'inch','= ',end='')
        print (result1,'Meters ',sep='', end=' ' )
        print(result2,'CM',sep='')
        
        grand_cmeter = grandcm(result2, grand)#This is actually to convert to cm
        grand_meter = result1 + grand_cmeter #This is actually to convert to Meter
        grand_bmi = bmi(weight, grand_meter, grand_meter)#This calculates the BMI and store it in the variable grand_bmi

        print('Your height in metres =', round(grand_meter, 2))
        print()
        #conditional statements to determine if the user is at an ideal weight or not.
        if grand_bmi < 19:
            print('Your BMI =', grand_bmi,':', 'You are under weight and below the recommended Body Mass Index (BMI), consume about 1500 and 2500 calories daily and do only light excersises daily to acheieve the recommended body weight and BMI. If you dont attain the recommended weight and BMI within six months, please do see a doctor.')
        elif grand_bmi >= 19 and grand_bmi <= 25 and weight >= 60 and weight <= 76 and grand_meter >= 1.74 and grand_meter <= 1.79:
            print('Your BMI =', grand_bmi,':', 'You are at your ideal weight and Body Mass Index (BMI), Your recommended weight is between 60 and 76 Kg and BMIs between 19 and 24.9 are considered optimum by most professionals. To maintain this ideal weight and BMI, consume between -10% t0 10% more the calories you expel.')
        elif grand_bmi >= 19 and grand_bmi <= 25:
            print('Your BMI =', grand_bmi,':', 'You are at your ideal weight and Body Mass Index (BMI), BMIs between 19 and 24.9 are considered optimum by most professionals. To maintain this ideal weight and BMI, consume between -10% t0 10% more the calories you expel.')
        elif grand_bmi >25 and grand_bmi <=30:
            print('Your BMI =', grand_bmi,':', 'You are over weight and over the recommended Body Mass Index (BMI) which is between 19 and 24.9, loose between 1000 and 2000 calories daily and reduce your general calories intake to attain the recommended weight and BMI for a healthy living.')
        elif grand_bmi >30: 
            print('Your BMI =', grand_bmi,':', 'You are obese and way over your ideal Body Mass Index (BMI) which is between 19 and 24.9, loose between 2000 and 4000 calories daily and reduce your calories intake by 80% to attain a healthy life. If you are above 40 years, please see your doctor immediately for a health consult on how to reduce your weight, as you may be prone to numerous heart complications.')

    def agge():
        try:
            age = int(input('Enter your age: '))
            if age >= 18:
                main()
            elif age < 18:
                print('You must be 18 and above to calculate BMI')
                agge()
        except IndexError:
            print("Index Error, please try again..")
            agge()
        except ValueError:
            print("Value Error, please try again..")
            agge()
        except Exception:
            print("An Error occured, please input correct values..")
            agge()
    def sex_t(): # This is just for formalities, as bmi calculation is actually the same for both male and female..
        try:
            sex = input("m/f: ")
            if sex == 'f' or sex == 'm' or sex == 'F' or sex == 'M': 
                agge()
            else:
                print('Invalid input, please enter either m for male, or f for female.')
                sex_t()
        except IndexError:
            print("Index Error, please try again..")
            sex_t()
        except ValueError:
            print("Value Error, please try again..")
            sex_t()
        except Exception:
            print("An Error occured, please input correct values..")
            sex_t()
    try:
        if sex == 'f' or sex == 'm' or sex == 'M' or sex == 'F':
            agge()
        elif sex != 'f' or sex != 'm' or sex != 'M' or sex != 'F':
            print('Invalid input, please enter either m for male, or f for female.')
            sex_t()
    except IndexError:
        print("Index Error, please try again..")
        sex_t()
    except ValueError:
        print("Value Error, please try again..")
        sex_t()
    except Exception:
        print("An Error occured, please input correct values..")
        sex_t()
re_run()

def re_ent():
    try:
        re_do = input("Would You like to check the BMI for a different person? Y/N: ")
    
        if re_do == 'Y' or re_do == 'y':
            re_run()
            print()
            re_ent()
        elif re_do == 'N' or re_do == 'n':
            print()
            print("Thanks for Using BMI Calculator! Bye...")
        else:
            print('Invalid input, please try again...')
            print()
            re_ent()
    except IndexError:
        print("Index Error, please try again..")
        re_run()
    except ValueError:
        print("Value Error, please try again..")
        re_run()
    except Exception:
        print("An Error occured, please input correct values..")
        re_run()
print()
re_ent()
print() 
    



