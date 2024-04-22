from django.shortcuts import render, redirect

from .models import Post
from .forms import CreatePostForm, UpdatePostForm


def index(request):
	"""
		Page with all posts
	"""
	posts = Post.objects.all() # get all post
	data = {
		"posts": posts,
	}

	return render(request, "blog/index.html", context=data)


def detail_post(request, id):
	"""
		Page of individual post
	"""
	post = Post.objects.get(id=id) # get post by id
	data = {
		"post": post,
	}

	return render(request, "blog/detail_post.html", context=data)


def create_post(request):
	"""
		Page with form of creating post
	"""
	form = CreatePostForm()

	if request.method == "POST":
		form = CreatePostForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data["title"] # get post title from form
			text = form.cleaned_data["text"] # get post text from form
			
			# creating post, data from form
			Post.objects.create(
				title=title,
				text=text,
				author=request.user
			)
			return redirect("index") # redirect to page with all posts

	return render(request, "blog/create_post.html", {"form": form})


def update_post(request, id):
	"""
		Page with form of update post data
	"""
	post = Post.objects.get(id=id) # get post which you wanna update
	form = UpdatePostForm(instance=post) # get form with previous data inside

	if request.method == "POST":
		form = UpdatePostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post.save() # save updated data
			
			return redirect("index") # redirect to page with all posts

	if post.author == request.user:
		return render(request, "blog/update_post.html", {"form": form})
	else:
		return redirect("index")


def delete_post(request, id):
	"""
		Page of deleting post
	"""
	post = Post.objects.get(id=id) # get post

	if post.author == request.user:
		post.delete() # delete post
		return redirect("index") # redirect to page with all posts

	return redirect("index") # redirect to page with all posts
