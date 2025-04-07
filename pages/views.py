from django.shortcuts import render

# Create your views here.
def session_summary(request):
    return render(request, 'pages/session_summary.html')

def choonsik_intro(request):
    context = {
        'name': '춘식이',
        'species': '고양이',
        'hobby': '고구마 먹기, 낮잠 자기',
        'personality': '순하고 귀여운 성격',
        'image_url': 'https://i.namu.wiki/i/p5cxk4A6XJYgA2f_OihzPhWznFdzkY_Nlh4w3rTXk4ltzFhUePbWXo4sdKPCoUwHUTbXyMjkPTTxhrNo3DFvKA.webp'
    }
    return render(request, 'pages/choonsik_intro.html', context)