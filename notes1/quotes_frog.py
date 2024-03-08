with open('quotes.txt', "r", encoding = "UTF-8") as file:
    for line in file:
        print(line)


author = input("Who wrote these lines? ")
with open('quotes.txt', "a",  encoding = "UTF-8") as file:
    file.write("("+author+")"+"\n")


while True:
    answer = input("Want to add another quote? (yes/no)")
    answer = answer.lower()
    if answer == "yes":
        quote = input("Enter a quotes: ")
        author = input("Enter an author: ")
        file = open("quotes.txt", "a",  encoding = "UTF-8")
        file.write(quote+"\n"+"("+author+")"+"\n")
        file.close()
    else:
        break


with open('quotes.txt', "r", encoding = "UTF-8") as file:
    for line in file:
        print(line)
