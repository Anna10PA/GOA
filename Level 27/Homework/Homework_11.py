''' 1) შექმენით სია რომელშიც გექნებათ 1 დან 20-მდე რიცხვები დაბეჭდეთ თითოეული სიის ელემენტი და თითოეულ მათგანს მიუწერეთ ლუწია თუ კენტი, გამოიყენეთ for loop'''

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for num in list:
    if num % 2 == 0:
        print(f'{num} არის ლუწი')
    else:
        print(f'{num} არის კენტი')