from django import template
from django.utils.safestring import mark_safe

register = template.Library()  # register 這個名稱是固定的

# 自定義標籤
@register.simple_tag
def mul(v1, v2, v3):
    return v1*v2*v3

@register.simple_tag
def my_input(v1, v2):
    temp_html = """<div class = 'input-group mb-3>
                        <span class ='input-group-text' id = '%s'>@</span>
                        <input type ='text' class='form-control' placeholder='%s' aria-label='Username'
                    </div> """%(v1,v2)
    return mark_safe(temp_html)

# 自定義過濾器，接受參數最多2個
@register.filter
def my_filter(v1,v2):
    return v1*v2