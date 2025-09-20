import math
import random
#
def main():
    low =int(input("Enter the smaller number:")) #User enters the lower bound as a clue. Only needs to happen once.
    high =int(input("Enter the larger number:")) #User enters the upper bound as a clue. Only needs to happen once.
    guessCount = round(math.log(high - low + 1, 2))
    count=0
    
    yourNumber = random.randint(low, high) #this is the computer's guess

    print("Your number is", yourNumber)

    while True:
        count += 1 #Increase the attempt count by one.

        if count > guessCount: 
            print ("You're cheating!")
            break
        else: 
            user_response = input("Enter =, <, or >:") #User tells computer if its higher or lower.

            if user_response == "<":
                high = yourNumber - 1 #Whatever computer guessed -1, because we're saying it's less than that number. Update the higher bound.
                yourNumber = random.randint(low, high) #Should generate a higher number.
                
                print("Your number is", yourNumber)
            elif user_response == ">":
                low = yourNumber + 1 #Whatever computer guessed +1, because we're saying it's greater than that number. Update the lower bound.
                yourNumber = random.randint(low, high) #Should generate a lower number
                
                print("Your number is ", yourNumber)
            elif user_response == "=":
                print("Hooray, I've got it in", count, "tries!")
                break
            else:
                print("Invalid entry, try again.")
            

if __name__ == "__main__":
    main()
