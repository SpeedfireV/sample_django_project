from django.shortcuts import render
from app.models import ContactForm

def home(request):
    contact_form_list = ContactForm.objects.all()


    for form in contact_form_list:
        print(form.nickname, form.created)
    return render(request, "home.html", {
        "contact_form": contact_form_list,
    })

def contact(request):
    nickname = request.POST.get("nickname")
    message = request.POST.get("message")
    success = False
    if nickname != None and message != None:
        success = True
        cform = ContactForm()
        cform.nickname = nickname
        cform.message = message
        cform.save()
    print("nickname=", nickname, "message=", message)



    return render(request, "contact.html", {
        "message": message,
        "qwe": 15475,
        "success": success,
    })

