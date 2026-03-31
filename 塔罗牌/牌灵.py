import random

tarot_cards = [ "愚者", "魔术师", "女祭司", "女皇", "皇帝", "教皇", "恋人", "战车",
    "力量", "隐士", "命运之轮", "正义", "倒吊人", "死神", "节制", "恶魔",
    "高塔", "星星", "月亮", "太阳", "审判", "世界"]  # 同上

num = int(input("想抽几张牌？"))
if num > len(tarot_cards):
    print("抽牌数量不能超过78张")
else:
    selected = random.sample(tarot_cards, num)  # 不重复抽取
    for i, card in enumerate(selected, 1):
        orientation = random.randint(1, 2)
        print(f"{i}. {card} - {'正位' if orientation == 1 else '逆位'}")