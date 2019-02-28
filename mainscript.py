# f = open('data.txt')
# arr = f.read().split()
# n= arr[0]
# print(n)
# f.close()
dic = {}
with open('data.txt','r') as f:
    for line in f:
        real_line = line.split()
        if len(real_line) == 1:
            continue
        t = real_line[0]
        count = real_line[1]
        for i in range(int(count)):
            dic[real_line[2 + i]].append({i, t})
            print(dic[t])
	
	
	
def evaluateScore(slides):
	totalScore = 0;
	for i in (range(len(slides))-1):
		scoreList = []
		commScore = getIntersection(slides[i],slides[i+1])
		scoreList.append(commScore)
		scoreList.append(len(slides[i]) - commScore)
		scoreList.append(len(slides[i+1]) - commScore)
		totalScore = totalScore + min(scoreList)
	return totalScore
		
def getIntersection(arr1, arr2): 
    combined = [value for value in arr1 if value in arr2] 
    return len(combined) 