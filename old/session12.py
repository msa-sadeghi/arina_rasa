numbers = [10, 20, 30, 40]
names = ["ali", "sara", "reza"]


# print(numbers[0])
# print(names[0])

# names.append("mina")
# new_name = input("enter a name: ")
# names.append(new_name)
# names.remove("ali")
# names.sort()
# print(names)
# print(len(names))

# total = 0
# for n in numbers:
#     if n < 30:
#         total += n
#     # total = total + n

# print("total is:", total)

# text = "hello python"

# # print(text[0])
# for x in text:
#     print(x.upper(), end=" ")


# notes = []

# for i in range(3):
#     n = input("enter a note: ")
#     notes.append(n)

# print("notes:")
# print(notes)
# for n in notes:
#     print(n, end=" ")

names = []
for i in range(5):
    names.append(input("enter a name: "))
names.sort(reverse=True)
print(names)

sen = input("enter asente... ")
# new_sen = sen.replace("a", "*")
# print(new_sen)
new_sen = ""
for c in sen:
    if c == "a":
        new_sen += "*"
    else:
        new_sen += c
print(new_sen)

scores = []
for i in range(5):
    scores.append(float(input("enter a score: ")))

print("avergae is:", sum(scores)/len(sum))