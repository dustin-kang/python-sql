dataset = ['LOVE DIVE', 'TOMBOY', 'THAT THAT', '사랑인가봐', '우리들의 블루스', '정이라고 하자', '사랑은 늘 도망가',
'나의 X에게', '다시 만날 수 있을까', '봄여름가을겨울', 'Yet to Come', 'LOVE me', 'FEARLESS', '취중고백', 'POP!', '신호등', '너를 사랑해']

count = 0
for data in dataset:
    for l in range(len(data)):
        if data[l] == 'L':
            count += 1

print(count)