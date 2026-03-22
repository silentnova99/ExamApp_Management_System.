from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Questions, StudentInfo

def HomePage(request):
    return render(request, 'index.html')

# ---------- Question Operations -----------
def Addquestion(request):
    if request.method == "POST":
        qid = request.POST.get('qid')
        qtext = request.POST.get('qtext')
        # ... get other fields ...
        Questions.objects.create(qid=qid, qtext=qtext,)
        return redirect('showallquestions')
    return render(request, 'Question/addquestion.html')

def Showallquestions(request):
    all_ques = Questions.objects.all()
    return render(request, 'Question/showallquestions.html', {'questions': all_ques})


from django.shortcuts import render, redirect
from .models import Questions, StudentInfo

# ---------- Question Operation -----------
def Addquestion(request):
    if request.method == "POST":
        # Pulling data from the HTML form 'name' attributes
        qid = request.POST.get('qid')
        qtext = request.POST.get('qtext')
        op1 = request.POST.get('op1')
        op2 = request.POST.get('op2')
        op3 = request.POST.get('op3')
        op4 = request.POST.get('op4')
        ans = request.POST.get('correct_ans')
        sub = request.POST.get('subject')

        # Saving to MySQL via the Model
        Questions.objects.create(
            qid=qid, qtext=qtext, op1=op1, op2=op2, 
            op3=op3, op4=op4, correct_ans=ans, subject=sub
        )
        return redirect('showallquestions') # Redirect after saving

    return render(request, 'Question/addquestion.html')

def Showallquestions(request):
    data = Questions.objects.all() # Fetch all from MySQL
    return render(request, 'Question/showallquestions.html', {'questions': data})

def Addstudent(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        mno = request.POST.get('mobno')
        
        # Saving to the StudentInfo model
        StudentInfo.objects.create(username=uname, password=pwd, mobno=mno)
        return redirect('showallstudent') # Make sure this name exists in urls.py
        
    return render(request, 'Student/addstudent.html')

def Showallstudent(request):
    students = StudentInfo.objects.all()
    return render(request, 'Student/showallstudent.html', {'students': students})

def Showallquestions(request):
    # Fetch all question objects from MySQL
    questions = Questions.objects.all() 
    
    # Pass the questions to the 'showallquestions.html' template
    return render(request, 'Question/showallquestions.html', {'questions': questions})


# 1. Show the Edit Form with existing data
def Editquestion(request, pk):
    # pk is the Question ID (qid) passed from the URL
    obj = Questions.objects.get(qid=pk)
    return render(request, 'Question/updatequestion.html', {'q': obj})

# 2. Save the updated data
def Updatequestion(request, pk):
    if request.method == "POST":
        obj = Questions.objects.get(qid=pk)
        
        # Update fields from POST data
        obj.qtext = request.POST.get('qtext')
        obj.op1 = request.POST.get('op1')
        obj.op2 = request.POST.get('op2')
        obj.op3 = request.POST.get('op3')
        obj.op4 = request.POST.get('op4')
        obj.correct_ans = request.POST.get('correct_ans')
        obj.subject = request.POST.get('subject')
        
        obj.save() # Save changes to MySQL
        return redirect('showallquestions')
    
    return redirect('showallquestions')

def Starttest(request):
    # We will add logic here later
    return render(request, 'Result/starttest.html')
def LoginView(request):
    return render(request, 'login.html')

from django.shortcuts import render, redirect
from .models import Student

def Addstudent(request):
    if request.method == "POST":
        # Get data from the HTML form
        id = request.POST.get('sid')
        name = request.POST.get('sname')
        email = request.POST.get('semail')
        password = request.POST.get('spassword')
        dept = request.POST.get('sdept')

        # Save to MySQL via Django Model
        obj = Student(sid=id, sname=name, semail=email, spassword=password, sdepartment=dept)
        obj.save()
        
        return redirect('home') # Redirect to home after saving
        
    return render(request, 'Student/addstudent.html')

def Addstudent(request):
    if request.method == "POST":
        # Get data from the HTML form
        id = request.POST.get('sid')
        name = request.POST.get('sname')
        email = request.POST.get('semail')
        password = request.POST.get('spassword')
        dept = request.POST.get('sdept')

        # Save to MySQL via Django Model
        obj = Student(sid=id, sname=name, semail=email, spassword=password, sdepartment=dept)
        obj.save()
        
        return redirect('home') # Redirect to home after saving
        
    return render(request, 'Student/addstudent.html')


def Showstudents(request):
    # Fetch all student objects from the Student model
    students = Student.objects.all()
    return render(request, 'Student/showstudents.html', {'students': students})

from django.shortcuts import render, redirect
from .models import Student

# 1. Show the Edit Form with existing student data
def Editstudent(request, pk):
    # pk is the Student ID (sid)
    student_obj = Student.objects.get(sid=pk)
    return render(request, 'Student/updatestudent.html', {'s': student_obj})

# 2. Save the updated student data
def Updatestudent(request, pk):
    if request.method == "POST":
        student_obj = Student.objects.get(sid=pk)
        
        # Update fields from POST data
        student_obj.sname = request.POST.get('sname')
        student_obj.semail = request.POST.get('semail')
        student_obj.spassword = request.POST.get('spassword')
        student_obj.sdepartment = request.POST.get('sdept')
        
        student_obj.save() # Commit changes to MySQL
        return redirect('showstudents')
    
    return redirect('showstudents')

from django.shortcuts import get_object_or_404, redirect

def Deletestudent(request, pk):
    # Fetch the student using the ID or return 404 if not found
    student_obj = get_object_or_404(Student, sid=pk)
    
    # Delete the record from MySQL
    student_obj.delete()
    
    # Redirect back to the list so the user sees the student is gone
    return redirect('showstudents')
    

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student

def StudentLogin(request):
    if request.method == "POST":
        email = request.POST.get('semail')
        password = request.POST.get('spassword')

        try:
            # Check if a student exists with this email and password
            user = Student.objects.get(semail=email, spassword=password)
            
            # Save student info in the session so they stay logged in
            request.session['student_id'] = user.sid
            request.session['student_name'] = user.sname
            
            return redirect('starttest') # Success! Go to exam
        except Student.DoesNotExist:
            # If not found, show an error message
            messages.error(request, "Invalid Email or Password!")
            return render(request, 'Student/login.html')

    return render(request, 'Student/login.html')

def StudentLogout(request):
    request.session.flush() # Clear the session
    return redirect('home')   

def Starttest(request):
    # If student_id is not in session, they haven't logged in
    if 'student_id' not in request.session:
        messages.warning(request, "Please login first to access the exam!")
        return redirect('login')

    all_questions = Questions.objects.all()
    return render(request, 'Result/starttest.html', {'questions': all_questions})


def Starttest(request):
    if 'student_id' not in request.session:
        return redirect('login')

    # Ensure these keys match what we use in the HTML {{ s_name }}
    context = {
        'questions': Questions.objects.all(),
        's_name': request.session.get('student_name'),
        's_id': request.session.get('student_id'),
    }
    return render(request, 'Result/starttest.html', context)



from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student

def StudentLogin(request):
    if request.method == "POST":
        e = request.POST.get('semail')
        p = request.POST.get('spassword')

        # This line checks the MySQL database for the student
        student_exists = Student.objects.filter(semail=e, spassword=p).exists()

        if student_exists:
            # 1. Fetch the student data
            user = Student.objects.get(semail=e, spassword=p)
            
            # 2. Store their info in a session (important for the header!)
            request.session['student_id'] = user.sid
            request.session['student_name'] = user.sname
            
            # 3. THIS IS THE REDIRECT YOU NEED
            return redirect('starttest')
        else:
            messages.error(request, "Invalid credentials. Please register first.")
            return render(request, 'Student/login.html')

    return render(request, 'Student/login.html')


def CalculateResult(request):
    if request.method == "POST":
        score = 0
        all_questions = Questions.objects.all()
        
        for q in all_questions:
            # This will now get "a", "b", etc.
            selected_letter = request.POST.get(f'q{q.qid}')
            
            # This matches your DB column 'correct_ans' (which is also "a", "b", etc.)
            if selected_letter == q.correct_ans:
                score += 1
        
        
        return render(request, 'Result/score.html', {
            'score': score, 
            'total': all_questions.count(),
            'name': request.session.get('student_name'),
        })       
    