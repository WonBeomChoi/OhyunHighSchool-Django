from django.shortcuts import render, HttpResponse
from memo.models import Memo

# Create your views here.
def get_all_memo(request):
    memo_list = Memo.objects.all()
    html = """
    <h1>메모들!</h1>
    """
    for memo in memo_list:
        html += f"<h2>{memo.title}</h2>"
        html += f"<p>{memo.content}</p>"
    return HttpResponse(html)