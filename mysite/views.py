from django.shortcuts import render
import datetime
#  Create your views here...

# Index Page View
def index(request):
    isActive = True
    if request.method=='POST':
        check = request.POST.get('check')
        print(check)
        if check is None: isActive=False
        else: isActive=True
    date = datetime.datetime.now()
    name = "LearnWithTheCodeArmy"
    list_of_program = [
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime factor',
        'WAP to print pascals triangle'
    ]
    student={
        'student_name':'Kamlesh',
        'student_collage': 'Truba',
        'student_city': 'Biaora',
    }
    to_send_data ={
        'date': date,
        'isActive': isActive,
        'name': name,
        'list_of_program': list_of_program,
        'student_data': student
    } 
    return render(request, "index.html",to_send_data)

# Services Page View
def services(request):
    return render(request, "services.html")

# About Page View
def about(request):
    return render(request, "about.html")

# Contact Page View
def contact(request):
    return render(request, "contact.html")

