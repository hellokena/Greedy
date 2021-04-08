box_num, book_num = map(int, input().split())
box_size = list(map(int, input().split()))
book_size = list(map(int, input().split()))

trash = 0 # 남아있는 용량
box = 0 # 현재 박스 번호
book = 0 # 현재 책 번호

while True:
    if box_size[box] >= book_size[book]: # 남아있는 용량이 있으면
        box_size[box] -= book_size[book]
        #if box_size[box] == 0: box += 1 # 넣은 다음에 박스 크기가 0이면 다음 박스 가져옴
        book += 1 # 다음 책 가져옴
    else: # 남아있는 용량이 없음
        #trash += (box_size[box]) # 쓰레기 용량 더하기
        box += 1 # 다음 박스 가져오기
    if book == book_num: # 모든책을 담았으면 break
        break
        #for i in range(box,box_num): # [주의] 뒤에 남아 있는 박스가 있는지 확인하고
            #trash += box_size[i] # 쓰레기 용량에 더해주기
        #break
print(sum(box_size))
