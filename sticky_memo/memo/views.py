from django.shortcuts import render, HttpResponse
from memo.models import Memo

# Create your views here.
def get_all_memo(request):
    memo_list = Memo.objects.all()
    return HttpResponse("<h1> 메모들 </h1>"+ str(memo_list))