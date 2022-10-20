#Author: Sophia Philips
#GitHub Username: sophiacphilips
#Date: 10/19/22
#This code runs a hailstone sequence on a given integer
#and the calculates the amount of steps it took to reach 1 in the sequence

#def num input for hailstone sequence
def hailstone(num):
    #steps = amt of steps it will take the hailstone sequence to max out
    steps=0

    while num!=1:
        if num%2==0:
            """num//2 is used for next sequence number in hailstone when value is pos"""
            num=num//2
        else:
            """(3*num)+1 is used for next sequence number in hailstone when value is neg"""
            num=(3*num)+1
        steps=steps+1
    return steps
#these were used for the testing inputs
answer=hailstone(1000)
#print(answer)