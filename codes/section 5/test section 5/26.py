# def say_hello():
#     name = input("your name: ")
#     print("hello " +name)


# say_hello()




#new function say_hello
# def say_hello(name):
#     print("hello " +name)


# say_hello("ahmed")
# say_hello("sara")
# say_hello("mahmoud")


# def some(nom1, nome2):
#     print(nom1 + nome2)


# some(12, 12)
# some(31, 15)


# def square(n):
#     print(n * n)


# square(4)
# square(16)


# def send_mail(to, sub, message):
#     print(f"send mail to {to} the subjact is {sub} the message is {message}")


# send_mail("ahmed sami2020@gmail.com", "about python course", "hi ahmed")


def add_friend(*args):
    print(args)
    print(type(args))


add_friend("ahmed", "mohamed", "noor", "jermaine", "sara", "mahmoud")
