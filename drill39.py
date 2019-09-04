cities = {
    '京': '北京', 
    '津': '天津',
    '冀': '河北',
    '晋': '山西',
    '渝': '重庆'
}

print(cities)

cities['蒙'] = "内蒙古"
cities['辽'] = "辽宁"

abb = ['苏', '浙', '皖']
cit = ['江苏', '浙江', '安徽']

for i in range(0, 3):
    cities[abb[i]] = cit[i]

for abbrev, city in list(cities.items()):
    print(f"{abbrev} is {city}")

del cities['浙'] # 删除项

ff = cities.get('浙', '没找到') # get()查找dict里的item, 没有给默认值
print(ff)