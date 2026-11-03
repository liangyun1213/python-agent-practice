#定义函数
# def 函数名(参数列表):
#     函数体
#     print("-------------")
#     #return 返回值
# 函数名(参数)
#计算圆的面积
def cicrle_area(r):
    """
    该函数用于根据圆的半径，计算圆的面积
    :param r: 圆的半径
    :return: 圆的面积
    """
    area = 3.14 * r * r
    return area
r = float(input("请输入圆的半径:"))
print("圆的面积为：",cicrle_area(r))
#计算长方形的面积
def rectangle_area(l,w):
    """
    该函数用于根据长方形的长和宽，计算长方形的面积
    :param l: 长方形的长
    :param w: 长方形的宽
    :return: 长方形的面积
    """
    area = l * w
    return area
l = int(input("请输入长方形的长："))
w = int(input("请输入长方形的宽："))
print("长方形的面积为：",rectangle_area(l,w))