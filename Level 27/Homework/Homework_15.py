'''     5) შექმენით სია რომელშიც გექნებათ ოცი სხვადასხვა რიცხვი შემდეგ კი დაბეჭდეთ მხოლოდ 20 ზე მეტი რიცხვები ისე რომ იყოს თან სამის ჯერადი გამოიყენეთ for loop '''

list = [100, 20, 321, 12, 90, 23, 28, 30, 10, 16, 7, 3, 13, 1, 222, 333, 902, 1000, 123, 2009]
new_list = []
for num in list:
    if num % 3 == 0 and num > 20:
        new_list.append(num)
print(new_list)