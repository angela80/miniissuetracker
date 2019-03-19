from django.test import TestCase
from .forms import IssueForm

# Create your tests here.
class TestIssuetrackerIssueForm(TestCase):

    def test_can_create_an_issue_with_just_a_name(self):
        form = IssueForm( { 'name':'Create Tests'})
        self.assertFalse(form.is_valid())