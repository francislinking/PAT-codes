string = input()
N = len(string)
height = (N+2)//3
width = N-2*height-2
for i in range(height - 1):
    print(string[i] + ' '*(width+2) + string[-i-1])
print(string[height-1:N-height+1])