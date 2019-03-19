from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Issue



class TestViews(TestCase):

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "issue_list.html")
    
    def test_get_add_issue_page(self):
        page = self.client.get("/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "issue_form.html")
    
    def test_get_edit_issue_page(self):
        issue = Issue(name="Create a Test")
        issue.save()

        page = self.client.get("/edit/{0}".format(issue.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "issue_form.html")
    
    def test_get_edit_page_for_issue_that_does_not_exist(self):
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)
        
    def test_post_create_an_issue(self):
        response = self.client.post("/add", {"name": "Create a Test"})
        issue = get_object_or_404(Issue, pk=1)
        self.assertEqual(issue.done, False)
    
    def test_post_edit_an_issue(self):
        issue = Issue(name="Create a Test")
        issue.save()
        id = issue.id

        response = self.client.post("/edit/{0}".format(id), {"name": "A different name"})
        issue = get_object_or_404(Issue, pk=id)

        self.assertEqual("A different name", issue.name)
    
     