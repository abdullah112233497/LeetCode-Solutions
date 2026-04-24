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
                if sample[i]!=box.pop():
                    return False
        return len(box)==0
