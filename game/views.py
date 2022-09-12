from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">小芽是最可爱的！</h1>'
    line2 = "<img src='https://sukiui.com/i/2022/09/12/kk7q7h.jpg' width=1000>"
    line3 = "<p style='text-align: center'> <img src='https://sukiui.com/i/2022/09/12/kk7q7h.jpg' alt=''> </p>"
    line4 = "<a href='http://101.43.169.252:8000/play'>小芽是猪猪吗?</a>"
    return HttpResponse(line1+line4+line3)
# Create your views here

def play(request):
    line = '<h1 style="text-align:center">猪猪小芽</h1>'
    line1 = '<a href="http://101.43.169.252:8000">返回主界面</a>'
    return HttpResponse(line+line1)
