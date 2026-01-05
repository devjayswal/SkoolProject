from django.shortcuts import render
from django.http import HttpResponse
from .models import Notification
from django.http import JsonResponse, HttpResponseForbidden

# Create your views here.

def index(request):
    return render(request, 'authentication/login.html' )

def dashboard(request):
    if getattr(request, 'user', None) and getattr(request.user, 'is_authenticated', False):
        unread_notifications = Notification.objects.filter(user=request.user, is_read=False)
    else:
        unread_notifications = Notification.objects.none()
    unread_notifications_count = unread_notifications.count()
    context = {
        'unread_notifications': unread_notifications,
        'unread_notifications_count': unread_notifications_count,
    }
    return render(request, 'students/student-dashboard.html' , context)

def mark_notifications_as_read(request):
    if request.method == 'POST':
        if not getattr(request, 'user', None) or not getattr(request.user, 'is_authenticated', False):
            return HttpResponseForbidden()
        notification  = Notification.objects.filter(user=request.user, is_read=False)
        notification.update(is_read=True)
        return JsonResponse({'status':'success'})
    return HttpResponseForbidden()


def clear_all_notifications(request):
    if request.method == 'POST':
        if not getattr(request, 'user', None) or not getattr(request.user, 'is_authenticated', False):
            return HttpResponseForbidden()
        notifications = Notification.objects.filter(user=request.user)
        notifications.delete()
        return JsonResponse({'status':'success'})
    return HttpResponseForbidden()


def create_notification(user, message):
    """Create a Notification for a given authenticated user with the provided message."""
    if not user or not getattr(user, 'is_authenticated', False):
        return None
    return Notification.objects.create(user=user, message=message)