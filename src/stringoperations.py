str = 'Ma point bulletball'
strR = 'llabtellub tniop aM'


def slicing():
    print(str[1:])
    print(str[1:3])
    print(reversed(str))
    print(str[:5])
    print(str[:])
    print(str[-1])
    print(str[-2])
    print(str[::])
    print(str[::-1])


def palindrome():
    rev = reversed(str)
    rev2 = str[::-1]
    print(rev == strR)
    print(rev2 == strR)


def capitalize():
    print(str.upper())
    print(str.capitalize())
    print(str.lower())
    print(str.casefold())


capitalize()