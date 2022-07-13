# 5 call stacks will be made
def fact(x):
    if x==1:
        return 1
    else:
        return x * fact(x-1)

def test(mine,expected):
    return "passed" if mine == expected else f'mine: {mine} vs expected: {expected}'

if __name__ == "__main__":
    print(test(120, fact(5))) # expected 120