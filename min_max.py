import random

p1_score=0
p2_score=0
while(True):
    p1=random.randint(1,5)
    print("P1 chooses: ", p1)
    p2=random.randint(1,5)
    print("P2 chooses: ", p2)
    if p1-p2==1:
        p2_score+=(p1+p2)
    elif p2-p1==1:
        p1_score+=(p1+p2)
    else:
        p1_score+=p1
        p2_score+=p2
    print("P1 score now is: ", p1_score)
    print("P2 score now is: ", p2_score)
    print("----------------------------")
    if p1_score>=100 or p2_score>=100:
        break

if p1_score>p2_score:
    print("P1 wins")
elif p1_score<p2_score:
    print("P2 wins")
else:
    print("draw")