M, N = 25, 6
S = M*N
f = open('input8.txt', 'r')
img = ''.join(f.readlines())
lst = [img[S*i: S*(i+1)].count('0') for i in range(100)]
i = lst.index(min(lst))
print(img[S*i: S*(i+1)].count('1') * img[S*i: S*(i+1)].count('2'))
parsed = [img[i::S]+'10' for i in range(S)]
decoded = [pixel[min(pixel.index('1'), pixel.index('0'))] for pixel in parsed]
picture = [' ' if ch == '0' else '*' for ch in decoded]
for i in range(N):
    print(''.join(picture[M*i: M*(i+1)]))
