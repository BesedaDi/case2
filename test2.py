"""Case-study #0 My first code
Developers:
Besedina D. (100%)
"""
print('Введите сумму налогового вычета')
a=int(input())
print('Введите свой месячный доход')
b=int(input())
s=b*12
s1=s-a
print('Введите свое семейное положение')
c=input()
if c=='один субъект':
    if s<=9075:
        n=0.1*s1
        print(n)
    elif 9076<=s<=36900:
        n=0.1*s1+0.15*(s1-9075)
        print(n)
    elif 36901<=s<=89350:
        n=0.1*s1+0.15*(s1-9075)+0.25*(s1-36900)
        print(n)
    elif 89351<=s<=186350:
        n=0.1*s1+0.15*(s1-9075)+0.25*(s1-36900)+0.28*(s1-89350)
        print(n)
    elif 186351<=s<=405100:
        n = 0.1 * s1 + 0.15 * (s1 - 9075) + 0.25 * (s1 - 36900) + 0.28 * (s1 - 89350)+0.33*(s1-186350)
        print(n)
    elif 405101<=s<=406750:
        n = 0.1 * s1 + 0.15 * (s1 - 9075) + 0.25 * (s1 - 36900) + 0.28 * (s1 - 89350) + 0.33 * (s1 - 186350)+0.35*(s1-405100)
        print(n)
    elif 406751<=s:
        n = 0.1 * s1 + 0.15 * (s1 - 9075) + 0.25 * (s1 - 36900) + 0.28 * (s1 - 89350) + 0.33 * (s1 - 186350) + 0.35 * (
                s1 - 405100)+0.396*(s1-406750)
        print(n)
elif c=='супружеская пара':
    if s<=18150:
        n=0.1*s1
        print(n)
    elif 18151<=s<=73800:
        n=0.1 * s1 + 0.15 * (s1 - 18150)
        print(n)
    elif 73801<=s<=148500:
        n=0.1 * s1 + 0.15 * (s1 - 18150)+0.25*(s1-73800)
        print(n)
    elif 148501<=s<=226850:
        n=0.1 * s1 + 0.15 * (s1 - 18150)+0.25*(s1-73800)+0.28*(s1-148500)
        print(n)
    elif 226851<=s<=405100:
        n=0.1 * s1 + 0.15 * (s1 - 18150) + 0.25 * (s1 - 73800) + 0.28 * (s1 - 148500)+0.33*(s1-226850)
        print(n)
    elif 405101<=s<=457600:
        n=0.1 * s1 + 0.15 * (s1 - 18150) + 0.25 * (s1 - 73800) + 0.28 * (s1 - 148500) + 0.33 * (s1 - 226850)+0.35*(s1-405100)
        print(n)
    elif 457601<=s:
        n=0.1 * s1 + 0.15 * (s1 - 18150) + 0.25 * (s1 - 73800) + 0.28 * (s1 - 148500) + 0.33 * (
                    s1 - 226850) + 0.35 * (s1 - 405100)+0.396*(s1-457600)
        print(n)
elif c=='родитель-одиночка':
    if 12950>=s:
        n=0.1*s1
        print(n)
    elif 12951<=s<=49400:
        n=0.1 * s1 + 0.15 * (s1 - 12950)
        print(n)
    elif 49401<=s<=127550:
        n=0.1 * s1 + 0.15 * (s1 - 12950) + 0.25 * (s1 - 49400)
        print(n)
    elif 127551<=s<=206600:
        n=0.1 * s1 + 0.15 * (s1 - 12950) + 0.25 * (s1 - 49400) + 0.28 * (s1 - 127550)
        print(n)
    elif 206601<=s<=405100:
        n=0.1 * s1 + 0.15 * (s1 - 12950) + 0.25 * (s1 - 49400) + 0.28 * (s1 - 127550) + 0.33*(s1-206600)
        print(n)
    elif 405101<=s<=432200:
        n=0.1 * s1 + 0.15 * (s1 - 12950) + 0.25 * (s1 - 49400) + 0.28 * (s1 - 127550) + 0.33 * (s1 - 206600)+0.35*(s1-405100)
        print(n)
    elif 432201<=s:
        n=0.1 * s1 + 0.15 * (s1 - 12950) + 0.25 * (s1 - 49400) + 0.28 * (s1 - 127550) + 0.33 * (s1 - 206600) + 0.35 * (
                s1 - 405100)+0.396*(s1-432200)
        print(n)
