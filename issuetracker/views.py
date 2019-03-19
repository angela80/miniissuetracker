from django.shortcuts import render, HttpResponse, redirect , get_object_or_404
from .models import Issue
from .forms import IssueForm


# Create your views here.
def get_issue_list(request):
    results = Issue.objects.all()
    return render(request, "issue_list.html", {
        'issues': results
    })


def create_an_issue(request):
    if request.method == "POST":
        form = IssueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(get_issue_list)
    
    else:
        form = IssueForm()
        
    return render(request, "issue_form.html" , { 'form':form})
    
def edit_an_issue(request, id):
    issue= get_object_or_404(Issue, pk=id)

    if request.method == "POST":
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect(get_issue_list)
    else:
        form = IssueForm(instance=issue)
    return render(request, "issue_form.html", {'form': form})
    
def toggle_status(request, id):
    issue = get_object_or_404(Issue, pk=id)
    issue.done = not issue.done
    issue.save()
    return redirect(get_issue_list)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    