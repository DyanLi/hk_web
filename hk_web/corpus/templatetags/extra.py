#coding=utf-8
import re
import operator


from django import template
register = template.Library()

@register.filter
def mul(value, arg): 
    return int(value)*int(arg) 
    
@register.filter
def add(value, arg): 
    return int(value)+int(arg)     
    
@register.filter
def sub(value, arg): 
    return int(value)-int(arg)     
    
@register.filter
def highlight(value, arg):
    if arg=="":
        return value
    dst = u'<span style="background-color:#ffff00;">'+ arg + '</span>'
    return value.replace(arg, dst)

import sys
    
"""
@register.filter
def return_item(l, i):
    print >> sys.stderr, repr(l), repr(i)
    try:
        return operator.getitem(l,i)
    except:
        return ''
"""

@register.filter
def return_item(l, i):
    #print >> sys.stderr, repr(l), repr(i)
    try:
        return getattr(l,i)
    except:
        return ''
        
        
@register.filter
def sub_url(value, arg): 
    #pa, rep, str
    repl = u"<sup> <a href='%s'> [\\1] </a></sup>" % arg
    w = re.sub(u"@(\\S+)", repl, value, re.U)        
    return w
    