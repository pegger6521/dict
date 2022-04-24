# 擷取前面reviews-analytics的前半段及資料庫

data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 100000 == 0:
            print(len(data))

print('檔案讀取完了, 總共有', len(data), '筆資料')


#文字計數
wc = {} # word_count
for d in data:
    words = d.split() # 先針對每一筆留言, 用空格去做切割, 如果裡面不放東西, 預設就是空格啦!
    for word in words:
        if word in wc: # 檢查word是否有在wc字典中
            wc[word] += 1 # 如果這個word有出現在字典中,我們就把它目前的value再+1
        else:
            wc[word] = 1 # 如果這個word沒出現在字典中,我們就把它目前的value新增為1

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

print(len(wc)) #查詢字典中有幾個key
print(wc['Allen']) #查詢字典中出現過幾次Allen

while True:
    word = input('請問您想要查詢什麼字: ')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為: ', wc[word])
    else:
        print('這個字沒有出現過喔!')

print('感謝使用本查詢功能!')
