#Umm... this got TLE on spoj
def even(num):
    left = num[: len(num)//2]
    right = num[len(num)//2:]
    out = ""
    if int(left[::-1]) <= int(right):
        out += str(int(num[ : len(num) // 2]) + 1)
        out = out + out[: len(num) // 2][::-1]
        return int(out)

    out += num[ : len(num) // 2 + 1]
    out = out + out[: len(num) // 2][::-1]
    return out

def odd(num):
    left = num[: len(num)//2]
    right = num[len(num)//2 + 1:]
    out = ""
    if int(left[::-1]) <= int(right):
        out += str(int(num[ : len(num) // 2 + 1]) + 1)
        out = out + out[: len(num) // 2][::-1]
        return int(out)

    out += num[ : len(num) // 2 + 1]
    out = out + out[: len(num) // 2][::-1]
    return out

    
tc = int(input())
for _ in range(tc):
    num = input()
    if num == num[::-1]:
        num = str(int(num) + 1)
    if int(len(num)) % 2 == 0:
        print(even(num))
    else:
        print(odd(num))







#OPTIMISED
import math

def helper(word):
    word_new = ''
    # check is the length of character list is even or odd
    if len(word) % 2 == 1:
        for i in range(len(word)//2 + 1):
            word_new += str(word[i])
        word_new += word_new[:len(word)//2 ][::-1]
    else:
        for i in range(len(word)//2):
            word_new += str(word[i])
        word_new += word_new[::-1]
    return word_new



def solve(word, n):
    string = ''.join([str(x) for x in word])
    z = helper(word)
    if z > string:
        return z
    else:
        # increase the middle character(s) and return the pallindrome
        inc = 1
        for i in range(math.ceil(len(word)/2) - 1,-1,-1):
            word[i] += inc 
            inc = word[i]//10
            word[i] %= 10
        return helper(word)

N = int(input())
for i in range(N):
    word = list(map(int, input()))
    word_len = len(word)

    # for cases like '999','99999'
    if len(set(word))==1 and word[0]==9:
        print('1'+'0'*(word_len-1)+'1')
    else:
        print(solve(word, word_len)) 
