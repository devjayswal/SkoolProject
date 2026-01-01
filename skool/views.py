from django.shortcuts import render
from django.http import HttpResponse
from .models import Notification
from django.http import JsonResponse, HttpResponseForbidden

# Create your views here.

def index(request):
    return render(request, 'authentication/login.html' )

def dashboard(request):
    unread_notifications = Notification.objects.filter(user=request.user, is_read=False)
    unread_notifications_count = unread_notifications.count()
    context = {
        'unread_notifications': unread_notifications,
        'unread_notifications_count': unread_notifications_count,
    }
    return render(request, 'students/student-dashboard.html' , context)

def mark_notifications_as_read(request):
    if request.method == 'POST':
        notification  = Notification.objects.filter(user=request.user, is_read=False)
        notification.update(is_read=True)
        return JsonResponse({'status':'success'})
    return HttpResponseForbidden()


def clear_all_notifications(request):
    if request.method == 'POST':
        notifications = Notification.objects.filter(user=request.user)
        notifications.delete()
        return JsonResponse({'status':'success'})
    return HttpResponseForbidden()