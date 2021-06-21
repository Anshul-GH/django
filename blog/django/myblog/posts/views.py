from django.shortcuts import render

## (C)reate
# This is our create post view.
def create_post_view(request):
    return render(request, 'posts/create.html')

## (R)etrieve
# This is to view one specific blog post.
def detail_post_view(request):
    return render(request, 'posts/detail.html')

# This is to view all of our blog posts.
def list_post_view(request):
    return render(request, 'posts/list.html')

## (U)pdate
# This will be to update one specific post.
def update_post_view(request):
    return render(request, 'posts/update.html')

## (D)elete
# This will be to delete one specific post.
def delete_post_view(request):
    return render(request, 'posts/delete.html')
