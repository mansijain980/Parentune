from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Parent, Child, Blog
import json

@csrf_exempt
def create_parent(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        parent = Parent.objects.create(name=data['name'], email=data['email'], password=data['password'], parent_type=data['parent_type'])
        return JsonResponse({'message': 'Parent created successfully', 'parent_id': parent.id})
    return HttpResponseBadRequest('Invalid request method')

def get_parent(request, parent_id):
    parent = get_object_or_404(Parent, pk=parent_id)
    return JsonResponse({'name': parent.name, 'email': parent.email, 'parent_type': parent.parent_type})

@csrf_exempt
def update_parent(request, parent_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        parent = get_object_or_404(Parent, pk=parent_id)
        parent.name = data.get('name', parent.name)
        parent.email = data.get('email', parent.email)
        parent.password = data.get('password', parent.password)
        parent.parent_type = data.get('parent_type', parent.parent_type)
        parent.save()
        return JsonResponse({'message': 'Parent updated successfully'})
    return HttpResponseBadRequest('Invalid request method')

@csrf_exempt
def delete_parent(request, parent_id):
    if request.method == 'DELETE':
        parent = get_object_or_404(Parent, pk=parent_id)
        parent.delete()
        return JsonResponse({'message': 'Parent deleted successfully'})
    return HttpResponseBadRequest('Invalid request method')

# Similar CRUD operations for Child and Blog models

def generate_home_feed(request, parent_id):
    parent = get_object_or_404(Parent, pk=parent_id)
    children = parent.child_set.all()
    home_feed = []

    for child in children:
        # Example logic to fetch relevant blogs
        relevant_blogs = Blog.objects.filter(age_group=child.age, gender=child.gender)

        for blog in relevant_blogs:
            home_feed.append({
                'title': blog.title,
                'content': blog.content,
                'created_at': blog.created_at,
            })

    return JsonResponse(home_feed, safe=False)
