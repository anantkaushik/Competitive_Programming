n = int(input())
result = {}
msg = []
for _ in range(n):
    msg.append(list(input().split()))
for i in range(n):
    for j in range(len(msg[i])):
        if msg[i][j].isdigit():
            if msg[i][j] not in result:
                result[msg[i][j]]=0
            if msg[i][0] == 'G:':
                result[msg[i][j]]+=2
            else:
                result[msg[i][j]]+=1
if len(result) == 0:
    print('No Date')
else:
    Keymax = max(result, key= lambda x: result[x]) 
    if Keymax == '19' or Keymax == '20':
        print('Date')
    else:
        print('No Date')
