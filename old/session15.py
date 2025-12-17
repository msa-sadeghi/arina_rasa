# variable
# if
# for   while
# list   tuple      dict    function     class 


# numbers = []
# numbers.append(1)
# numbers.append(2)
# numbers.append(3)
# print(numbers)
# numbers.remove(2)
# print(numbers)

# for n in numbers:
#     print(n)


# names = []
# for i in range(3):
#     n = input("enter a name: ")
#     names.append(n)

# print(names)

# numbers = [1,2,3]
# s = 0
# for n in numbers:
#     s += n

# print(s)

# numbers = (1,2,3)

# favorite_sport = {}

# for i in range(3):
#     name = input("enter the name: ")
#     sport = input("enter the sport: ")
#     favorite_sport[name] = sport

# name = input("enter the name: ")
# print(favorite_sport[name])


# def greet(name, family):
#     return f"hello {name} {family}"

# print(greet("armin", "rezaei"))
# print(greet("sara", "blalal"))
# print(greet("reza", "bababab"))


# def add(a, b, c):
#     return a + b + c


# print(add(1,2,3))
# print(add(88,4, 567))

# def my(x):
#     if x % 2 == 0:
#         return "even"
#     else:
#         return "odd"
    
# print(my(12))
# print(my(13))


def x(numbers):
    new_list = []
    for n in numbers:
        if n % 2 != 0:
            new_list.append(n)
    return new_list


print(x([1,2,3,4,5,6,7,8,9]))
