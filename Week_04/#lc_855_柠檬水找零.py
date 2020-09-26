#lc_855_柠檬水找零

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        b5, b10 = 0, 0
        for i in range(len(bills)):
            if bills[i] == 5:
                b5 += 1
            elif bills[i] == 10:
                b5 -= 1
                if b5 < 0:
                    return False
                b10 += 1
            else:
                if b10 > 0:
                    b10 -= 1
                    b5 -= 1
                else:
                    b5 -= 3
                if b5 < 0 or b10 < 0:
                    return False         
        return True 