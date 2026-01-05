from django.shortcuts import render, get_object_or_404,redirect
from .models import Student, Parent
from django.contrib import messages
from django.http import  HttpResponseForbidden
from skool.views import create_notification
from skool.models import Notification
# Create your views here.

def add_student(request):
    if request.method == "POST":
        first_name  = request.POST.get('first_name')
        last_name  = request.POST.get('last_name')
        student_id  = request.POST.get('student_id')
        gender  = request.POST.get('gender')
        date_of_birth  = request.POST.get('date_of_birth')
        student_class  = request.POST.get('student_class')
        religion  = request.POST.get('religion')
        joining_date  = request.POST.get('joining_date')
        mobile_number  = request.POST.get('mobile_number')
        admission_number  = request.POST.get('admission_number')
        section  = request.POST.get('section')
        student_image  = request.FILES.get('student_image')

        #parents
        father_name  = request.POST.get('father_name')
        father_occupation  = request.POST.get('father_occupation')
        father_mobile  = request.POST.get('father_mobile')
        father_email  = request.POST.get('father_email')
        mother_name  = request.POST.get('mother_name')
        mother_occupation  = request.POST.get('mother_occupation')
        mother_mobile  = request.POST.get('mother_mobile')
        mother_email  = request.POST.get('mother_email')

        # extra

        present_address = request.POST.get('present_address')
        permanent_address  = request.POST.get('permanent_address')

        parent = Parent.objects.create(
            father_name=father_name,
            father_occupation=father_occupation,
            father_mobile=father_mobile,
            father_email=father_email,
            mother_name=mother_name,
            mother_mobile=mother_mobile,
            mother_email=mother_email,
            present_address=present_address,
            permanent_address=permanent_address,
            mother_occupation=mother_occupation
        )

        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            student_id=student_id,
            gender = gender,
            date_of_birth=date_of_birth,
            student_class=student_class,
            religion=religion,
            joining_date=joining_date,
            mobile_number=mobile_number,
            admission_number=admission_number,
            section=section,
            student_image=student_image,
            parent=parent
        )
        if getattr(request, 'user', None) and getattr(request.user, 'is_authenticated', False):
            create_notification(request.user, f"New student {first_name} {last_name} added.")
        messages.success(request,"Student added successfully")
        return redirect('student-list')




    return render(request,"students/add-student.html")

def student_list(request):
    student_list = Student.objects.select_related('parent').all()
    student_count = student_list.count()
    if getattr(request, 'user', None) and getattr(request.user, 'is_authenticated', False):
        unread_notifications = Notification.objects.filter(user=request.user, is_read=False)
    else:
        unread_notifications = Notification.objects.none()
    unread_notifications_count = unread_notifications.count()

    context = {
        'student_list': student_list,
        'student_count': student_count,
        'unread_notifications': unread_notifications,
        'unread_notifications_count': unread_notifications_count,
    }
    return render(request,"students/students.html")

def edit_student(request,slug):
    student = get_object_or_404(Student, slug=slug)
    parent  = student.parent if hasattr(student, 'parent') else None
    if request.method == "POST":
        first_name  = request.POST.get('first_name')
        last_name  = request.POST.get('last_name')
        student_id  = request.POST.get('student_id')
        gender  = request.POST.get('gender')
        date_of_birth  = request.POST.get('date_of_birth')
        student_class  = request.POST.get('student_class')
        religion  = request.POST.get('religion')
        joining_date  = request.POST.get('joining_date')
        mobile_number  = request.POST.get('mobile_number')
        admission_number  = request.POST.get('admission_number')
        section  = request.POST.get('section')
        student_image  = request.FILES.get('student_image')

        #parents
        parent.father_name  = request.POST.get('father_name')
        parent.father_occupation  = request.POST.get('father_occupation')
        parent.father_mobile  = request.POST.get('father_mobile')
        parent.father_email  = request.POST.get('father_email')
        parent.mother_name  = request.POST.get('mother_name')
        parent.mother_occupation  = request.POST.get('mother_occupation')
        parent.mother_mobile  = request.POST.get('mother_mobile')
        parent.mother_email  = request.POST.get('mother_email')
        # extra

        parent.present_address = request.POST.get('present_address')
        parent.permanent_address  = request.POST.get('permanent_address')
        parent.save()

        student.first_name=first_name
        student.last_name=last_name
        student.student_id=student_id
        student.gender = gender
        student.date_of_birth=date_of_birth
        student.student_class=student_class
        student.religion=religion
        student.joining_date=joining_date
        student.mobile_number=mobile_number
        student.admission_number=admission_number
        student.section=section
        student.student_image=student_image
        student.save()
        
        
        messages.success(request,"Student updated successfully")
        if getattr(request, 'user', None) and getattr(request.user, 'is_authenticated', False):
            create_notification(request.user, f"Student {student.first_name} {student.last_name} updated.")
        return redirect('student-list')
   
    return render(request,"students/edit-student.html", context = {
            'student': student,
            'parent': parent
        })

def view_student(request, slug):
    student = get_object_or_404(Student, slug=slug)
    context  = {
        'student': student
    }
    return render(request, "students/student-details.html", context)

def delete_student(request, slug):
    if request.method == "POST":
        student = get_object_or_404(Student, slug=slug)
        student_name = f"{student.first_name} {student.last_name}"
        student.delete()
        if getattr(request, 'user', None) and getattr(request.user, 'is_authenticated', False):
            create_notification(request.user, f"Student {student_name} deleted.")
        messages.success(request,"Student deleted successfully")
        return redirect('student-list')
    return HttpResponseForbidden()