#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render

"""
項目介紹
    概要情況:香港教育学院，UGC資助部門等
"""      
def intro(request):
    return render(request, 'corpus/intro.html', {})
    
"""
項目縮寫
    縮略語表
"""      
def abbreviation(request):
    return render(request, 'corpus/abbreviation.html', {})
    
"""
項目下載
    論文，資料等
"""  
def download(request):
    return render(request, 'corpus/download.html', {})

"""
項目聯繫方式
    主要是朱老師的地址
"""      
def contact(request):
    return render(request, 'corpus/contact.html', {})

"""
項目歷史
    修訂記錄
"""      
def history(request):
    return render(request, 'corpus/history.html', {})


