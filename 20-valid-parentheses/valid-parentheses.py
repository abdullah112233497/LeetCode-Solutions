class Solution:
    def isValid(self, s: str) -> bool:
        box=[]
        sample={
           '}' :'{',
           ']':'[',
           ')':'('
        }
        for i in s:
            if i in '{[(':
                box.append(i)
            else:
                if not box:
                    return False
                t=box.pop()
                if sample[i]!=t:
                    return False
        return len(box)==0
