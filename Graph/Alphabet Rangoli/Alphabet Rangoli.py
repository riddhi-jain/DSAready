from string import ascii_lowercase

list_ch = [al for al in ascii_lowercase]
n = int(input("Enter the size for rangoli(1-26): "))
data = [list_ch[i] for i in range(n)]
width = len('-'.join(data[n-1:n-n:-1] + data[n-n:n]))

for i in range(1, n+1):
    print('-'.join(list_ch[n-1:n-i:-1] + list_ch[n-i:n]).center(width, "-"))
for i in range(n-1, 0, -1):
    print('-'.join(list_ch[n-1:n-i:-1] + list_ch[n-i:n]).center(width, "-"))
