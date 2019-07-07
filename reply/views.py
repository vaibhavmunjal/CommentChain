from .models import Comment
from .forms import Comment_Form
from django.shortcuts import render, redirect
from django.http import JsonResponse

def home(request):
    form = Comment_Form(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            temp = form.save(commit=False)
            parent = form['parent'].value()

            if parent == '':
                temp.path = ''
                temp.save()
                temp.path = f"{temp.id}"
            else:
                node = Comment.objects.get(id=parent)
                temp.path = f"{node.path}"

                temp.save()
                temp.path += f"{temp.id}"

            temp.save()
            return redirect('home')

    comment_list = Comment.objects.all()
    context = {'comment_list': comment_list,
	'form': form}

    return render(request, 'reply/index.html', context)


def delete_comment(request, method=["POST"]):
    id = request.POST.get('id')
    print(id)
    try:
        Comment.objects.filter(path__contains=id).delete()
        result = {"deleted": True}
    except:
        result = {"deleted": False}
    return JsonResponse(result)
