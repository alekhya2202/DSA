#https://www.hackerrank.com/challenges/balanced-brackets/problem?isFullScreen=true&utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

BRACKETS_MAP = {
    '[': ']',
    '{': '}',
    '(': ')',
}
def isOpen(bracket):
    return bracket in BRACKETS_MAP.keys()

def isClose(bracket):
    return bracket in BRACKETS_MAP.values()

def isBalanced(s):
    stack = []
    for bracket in s:
        if(isOpen(bracket)):
            stack.append(bracket)
        elif(isClose(bracket)):
            if(stack == [] or bracket != BRACKETS_MAP.get(stack.pop())):
                return ("NO")
    if(stack != []):
        return ("NO")
    return ("YES")
