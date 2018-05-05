from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse
from hexiao.models import *
import random


# 主页视图处理函数
def index(req):
    # 查询对应码的数量
    allCode = HXCodeInfo.objects.all().count()
    yesCode = HXCodeInfo.objects.filter(codeStatus=True).count()
    noCode = HXCodeInfo.objects.filter(codeStatus=False).count()
    deCode = HXCodeInfo.objects.filter(isDelete=True).count()
    list = {
        'allCodeNumber': allCode,
        'noCodeNumber': noCode,
        'yesCodeNumber': yesCode,
        'deCodeNumber': deCode
    }
    return render(req, 'index.html', list)


# 查询页视图处理函数
def query(req):
    codeStatus = req.GET.get('codeStatus')
    pIndex = req.GET.get('pIndex')
    status = 0
    numbr = 0
    page_range = None
    if codeStatus == '已核销':
        codeStatus = True
        objs = HXCodeInfo.objects.filter(codeStatus=codeStatus)
        numbr = len(objs)
        page_range = Paginator(objs, 20).page_range
        num_page = Paginator(objs, 20).num_pages
        objs = Paginator(objs, 20).page(pIndex)
        status = 1
        num_page = 0
    elif codeStatus == '未核销':
        codeStatus = False
        objs = HXCodeInfo.objects.filter(codeStatus=codeStatus)
        numbr = len(objs)
        page_range = Paginator(objs, 20).page_range
        num_page = Paginator(objs, 20).num_pages
        objs = Paginator(objs, 20).page(pIndex)
        status = 2
    else:
        objs = HXCodeInfo.objects.all()
        numbr = len(objs)
        page_range = Paginator(objs, 20).page_range
        num_page = Paginator(objs, 20).num_pages
        objs = Paginator(objs, 20).page(pIndex)
    return render(req, 'query.html',
                  {'objs': objs, 'status': status, 'number': numbr, 'page_range': page_range, 'pIndex': pIndex,
                   'num_page': num_page})


# 添加视图处理函数
def add_code(req):
    return render(req, 'add_code.html')


# 核销视图处理函数
def verify(req):
    code = req.GET.get('code')
    pIndex = req.GET.get('pIndex')
    data = {
        'code': code
    }
    all_objs = HXCodeInfo.objects.filter(code__contains=code)
    if code and all_objs:
        fy_objs = Paginator(all_objs, 20)
        data['code_objects'] = fy_objs.page(int(pIndex))
        data['number'] = len(all_objs)
        data['page_range'] = fy_objs.page_range
        data['pIndex'] = pIndex
        data['count'] = len(fy_objs.page_range)
    else:
        data['code_objects'] = []
        data['number'] = 0
        data['page_range'] = []
        data['pIndex'] = 1
        data['count'] = 0
    return render(req, 'verify.html', data)  # 核销码查询处理


# 确认核销处理视图函数
def okCode(req):
    try:
        code = req.GET.get('code')
        obj = HXCodeInfo.objects.filter(code=code)[0]
        obj.codeStatus = True
        obj.save()
        return JsonResponse({'status': True})
    except Exception:
        return JsonResponse({'status': False})

# 添加核销码视图
def add(req):
    number = int(req.GET.get('number'))
    print('111111111111')
    description = req.GET.get('description')
    jishu = 0
    while number > jishu:
        while True:
            a = random.randint(00000000000,99999999999)
            obj = HXCodeInfo.objects.filter(code=str(a))
            if len(obj):
                continue
            else:
                obj1 = HXCodeInfo()
                obj1.code = str(a)
                obj1.description = description
                obj1.save()
                break
        jishu += 1
    return JsonResponse({'status': 'ok'})

