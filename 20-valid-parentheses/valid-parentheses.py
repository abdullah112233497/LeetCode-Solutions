class Solution:
    def isValid(self, s: str) -> bool:
        bag=[]
        ids = {
    '}': '{',
    ']': '[',
    ')': '('
}
        for i in s:
            if i in '{[(':
                bag.append(i)
            else:
                if not bag:
                    return False
                sem=bag.pop()
                if ids[i]!=sem:
                    return False
        return len(bag)==0
