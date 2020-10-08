def match_num():
    import random
    
    name=input("What's your name? ")
    print("Hi {}! Then Let's play game!".format(name))
    print()
    print('I choiced one number!')
    print()
    print('Take one number between 1 and 20')
    
    rng=[1,20]
    answer=random.randint(rng[0],rng[1])
    
    cnt=0
    while True:
        try:
            cnt+=1
            if cnt<6:
                num=int(input('what number? '))
                if answer == num:
                    print('congratulation! You win!')
                    break
                elif num < rng[0] or num > rng[1]:
                    cnt-=1
                    print('This number not include range')
                else:
                    if answer < num:
                        print('your answer is too hight')
                    else:
                        print('your answer is too low')
            else:
                print()
                print('Sorry You lose!')
                break
        except:
            cnt-=1
            print('enter an integer')
          