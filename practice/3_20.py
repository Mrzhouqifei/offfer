"""
有一叠扑克牌，每张牌介于1和10之间
有四种出牌方法：

单出1张
出2张对子
出五张顺子，如12345
出三连对子，如112233

给10个数，表示1-10每种牌有几张，问最少要多少次能出完
"""


def remove(new_boxes):
    res = 0
    i = 0
    while i < len(new_boxes):
        t = i
        k = 0
        tmp_boxes = new_boxes.copy()
        while (i < len(new_boxes)) and (new_boxes[t] == new_boxes[i]):
            k += 1
            i += 1
            tmp_boxes.pop(t)
        res = max(res, k * k + remove(tmp_boxes))
    return res

boxes = [1,3,2,2,2,3,4,3,1]
print(remove(boxes))

