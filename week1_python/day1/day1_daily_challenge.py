#!/usr/bin/python

# execution : $>python day1_daily_challenge.py

if __name__ == "__main__":
    # Challenge#1
    # n=7, len=5 => [7, 14, 21, 28, 35]
    n,long=input("Give number,length ? ").split(",")

    i=1
    l=[]
    while len(l)<int(long):
        l.append(int(n)*i)
        i += 1
    print(f"Challenge#1: liste obtenue de multiples du nombre de longeur {long}:\n", l)

    # Challenge#2
    print()
    # user's word : "ppoeemm" ➞ "poem"
    # user's word : "wiiiinnnnd" ➞ "wind"
    # user's word : "ttiiitllleeee" ➞ "title"
    # user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
    s=input("donner une chaine svp? ")
    print("Challenge#2: chaine sans doublons =>", ''.join(dict.fromkeys("wiiiinnnnd") ) )#dict.fromkeys(keys, value),key classée

#EOF
