#Esabelle Gervasio
#Project 5
#Analysis of words

def main ():
    words= input("Please enter a sentance: ").lower() #Input sentance
    num=len(words) #counts the length of the sentance
    print("The number of characters in your sentance is: ", num)
    count=len(words.split())#splits the sentance and counts the individual words
    print("The number of words is: ", count)
    avg= float(num/count) # divides the number of characters by the number of words
    print("The average word length is: ", avg)
main()
