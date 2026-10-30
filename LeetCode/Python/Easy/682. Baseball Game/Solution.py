class Solution:
    def calPoints(self, operations: list[str]) -> int:
        lst=[]
        for ope in operations:
            if ope == 'C':
                lst.pop()
        
            elif ope== "D":
                double=lst[-1] +lst[-1]
                lst.append(double)
            elif ope == "+":
                add=lst[-1]+lst[-2]
                lst.append(add)
            else:
                num=int(ope)
                lst.append(num)
        return sum(lst) 