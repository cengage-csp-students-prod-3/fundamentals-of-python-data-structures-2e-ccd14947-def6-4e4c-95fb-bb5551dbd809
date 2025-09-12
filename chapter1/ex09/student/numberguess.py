import math

def main():
    low =int(input("Enter the smaller number:"))
    
    high =int(input("Enter the larger number:"))

    yourNumber = round(math.log(high - low + 1,2))
    count=0
    
    print("Your number is", yourNumber)

    user_response = input("Enter =, <, or >:")

    count+=1

    if user_response == ">":
        print("Your number is", yourNumber)
    elif user_response == "<":
            print("Your number is", yourNumber)
    elif user_response == "=":
            print("Hooray, I got it in", count, "tries!")

            if __name__ == "__main__":
                main()
