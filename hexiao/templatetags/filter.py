from django import template

register = template.Library()


# 字符串转换数字过滤器
@register.filter
def go_int(str):
    return int(str)
