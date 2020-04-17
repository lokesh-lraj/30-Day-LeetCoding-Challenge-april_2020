def isHappy(self, n: int) -> bool:
        square_list = []
        while True :
            
            sq = 0
            while n :
                rem = n % 10
                n = n // 10
                sq += rem ** 2
                
            if sq == 1:
                return True
            if sq in square_list:
                return False
            square_list.append(sq)
            n = sq
