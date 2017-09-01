#coding=utf-8
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from .models import Lotus




CLIST = [["sanskrit", u"梵語"], ["sanskrit_eq",u"梵語非連聲形式"], ["tag",u"梵語標註"], 
       ["chinese_explain",u"現代漢譯"], ["note", u"注"],
       ["d", u"護譯"], ["k", u"什譯"] ]
       # ["dnote", u"注"], ["knote", u"注"]    ] #此兩項目作爲附庸
       
       
"""
法華經首页；引出編寫說明，瀏覽和檢索選單
"""
def lotus_index(request): 
    return render(request, 'corpus/lotus_index.html', {})

"""
法華經編寫說明
"""    
def lotus_intro(request): 
    return render(request, 'corpus/lotus_intro.html', {})


"""
法華經语料库浏览 
"""   
def lotus_list(request): 
    all = Lotus.objects.filter(level=1)
    return render(request, 'corpus/lotus_list.html', {"items": all})

"""
法華經語料庫
"""
def lotus_view(request, code):
    t = Lotus.objects.get(code=code)
    level = t.level
    total_num = Lotus.objects.filter(level=level).count() #總數
    cur_id = Lotus.objects.filter(level=level, pk__lte=t.pk).count() #總數
    
    children = Lotus.objects.filter(level=level+1, code__startswith=code+"-")
    childlist = []
    for c in children:
        childlist.append( [c.code, c.sanskrit])
    
    return render(request, 'corpus/lotus_view1.html', 
            {"totalpage":total_num, "current":cur_id, "code":code, 
             "level":level, "v1": t, "children":childlist, "clist": CLIST})
             
def lotus_go(request):
    if "to" in request.GET:
        dst = request.GET["to"]
    else:
        dst = None
    if "level" in request.GET:
        level = request.GET["level"]
    else:
        level = None
    if "base" in request.GET:
        code = request.GET["base"]
    else:
        code = None
    if "bottom" in request.GET:
        showbottom = "#bottom"
    else:
        showbottom = ""
    try:
        if dst=="first":
            x = Lotus.objects.filter(level=int(level))[0]
            return HttpResponseRedirect("/c/lotus/view/%s%s" % (x.code, showbottom))
        elif dst=="last":
            all_x = Lotus.objects.filter(level=int(level))
            x = all_x[all_x.count()-1]
            return HttpResponseRedirect("/c/lotus/view/%s%s" % (x.code, showbottom))
        elif dst=="up":
            x = Lotus.objects.get(code=code)
            try:
                p = Lotus.objects.get(id=x.parent)
                return HttpResponseRedirect("/c/lotus/view/%s%s" % (p.code, showbottom))
            except:
                return HttpResponseRedirect("/c/lotus/view/%s%s" % (code, showbottom))
        elif dst=="prev":
            x = Lotus.objects.get(code=code)
            prev = Lotus.objects.filter(level=x.level, id__lt=x.id).order_by('-id')
            if prev.count()>0:
                c = prev[0].code
            else:
                c = code
            return HttpResponseRedirect("/c/lotus/view/%s%s" % (c, showbottom))
        elif dst=="next":
            x = Lotus.objects.get(code=code)
            nextx = Lotus.objects.filter(level=x.level, id__gt=x.pk).order_by('id')
            if nextx.count()>0:
                c = nextx[0].code
            else:
                c = code
            return HttpResponseRedirect("/c/lotus/view/%s%s" % (c, showbottom))
        else:
            raise Http404()
    except:
        raise             