''' 5) დაწერეთ ფუნქცია რომელიც მომხმარებლისგან იღებს რიცხვს და თუ რიცხვი 1-დან 10-მდეა დაბეჭდავს თუარა დაუბეჭდავს "არასწორი რიცხვი" '''

def number():
    num = int(input("Enter number: "))
    if 10 > num > 0:
        print("GOOD")
    else:
        print("Error") 
number()