# 959.Regions Cut By Slashes.py
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        len2 = len(grid) * 2
        list = [[0 for i in range(len2) ] for j in  range(len2)]
        line = 0
        x = 0
        for r,v in enumerate(grid):
            for c, m in enumerate(v):
                if (m == "/"):
                    list[r*2][c*2+1] += 1
                    list[r*2+1][c*2] += 1
                elif (m == "\\"):
                    list[r*2][c*2] = 1
                    list[r*2+1][c*2+1] = 1
        
        

        for i in range(0,len2,2):
            for j in range(len2):
                r = i
                c = j
                count = 0
                flag = 0
                if (i == j and i != 0):
                    continue
                elif j % 2 == 0:               
                    while(c < len2 and r < len2):
                        flag += 1
                        if list[r][c] == 1:
                            count += 1
                        r +=1
                        c += 1
                else:
                    while(c >= 0 and r < len2):
                        flag += 1
                        if list[r][c] == 1:
                            count += 1
                        r += 1
                        c -= 1

                # print(flag, count, i, j)
                if (flag == count):
                    if(i+j+1 != len2):
                        line += 1
                    if (count == len2):
                        x += 1
        # print(line, x)
        
        for i in list:
            print(i)
        if x == 2:
            return 4
        else:
            return line + x + 1
