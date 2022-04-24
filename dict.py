# dictionary 字典
# 筆記: 記得兩個詞中間要放"逗號"
# 筆記: 左邊叫key, 右邊叫value, 這是字典的核心概念, key-value pair
# 筆記: 有等號的話, 要嘛是改變現有的值, 要嘛就是新增(要看目前字典中是否有該字存在)

#字典範例
words = {
    'ramen': '拉麵', 
    'pasta': '義大利麵'
    }

#如何查字典
print(words['ramen']) #會印出拉麵
print(words['pasta']) #會印出義大利麵
# print(words['tea']) #字典找不到, 會出現error

#字典新增一組key-value pair
words['tea'] = '茶'
print(words['tea'])

#字典範例2
#清單與字典的混用
p0 = {
    'name': '麥香奶茶'
    'price': '10'
}
p1 = {
    'name:': '珍珠奶茶'
    'price': '60'
}

drinks = [p0, p1] #drinks是一個清單
drinks[0]['name'] # '麥香奶茶'- drinks[0]是指p0字典,所以後面又可以用查詢的功能去查出p0的name是什麼值
drinks[1]['price'] # 60