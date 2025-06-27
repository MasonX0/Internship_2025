with open("12.txt","r",encoding="utf-8") as f:
    List=[list.strip("\n").split(" ") for list in f][1:]
sList = [[int(start), int(end), int(price)] for start, end, price in List]
sList = sorted(sList, key=lambda row: row[1])
dp=[0]*(len(sList)+1)
def lastLower (sList,i):
    left,right=0,i-1
    while left<=right:
        mid=(right+left)//2
        if sList[mid][1]<sList[i][0]:
            left=mid+1
        else:
            right=mid-1
    return right
for i in range(1,len(sList)+1):
    dp[i]=max(dp[i-1],sList[i-1][-1]+dp[lastLower(sList,i-1)+1])
selected = []
i = len(sList)
cnt1=0
while i > 0:
    if dp[i] != dp[i - 1]:
        selected.append(sList[i - 1])
        i=lastLower(sList, i-1)+1
        cnt1+=1
    else:
        i-=1
cnt=sum([ab[1]-ab[0] for ab in selected])
print("Kol-vo: ",cnt1)
print("Длительность: ",cnt)
print("Максимальная выручка: ",dp[-1])
