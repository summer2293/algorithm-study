# strategy: divide the brown into "sides", simply brown /2
# try different combinations of height and width
def solution(brown, red):
    if brown <= 4:
        return 0
    side = brown//2
    for i in range(1,side//2+1):
        height = i
        width = side - height
        print(height, width)
        area = height * (width-2)
        if area == red:
            return [width, height+2]
    return "error"


print(solution(10,2))

# 1st try: all correct.. but took a long time > 20 min constantly, drawing and stuff