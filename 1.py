qs = ["What is your name?",
    "What is your favorite color?",
    "What do you do?"
     ]
n = 0
while True:
    print("Enter X to exit")
    a = input(qs[n])
    if n == "X":
        break
    n = (n + 1) % 3   