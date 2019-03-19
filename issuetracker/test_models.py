from django.test import TestCase
from .models import Issue


class TestItemModel(TestCase):

    def test_done_defaults_to_False(self):
        issue = Issue(name="Create a Test")
        issue.save()
        self.assertEqual(issue.name, "Create a Test")
        self.assertFalse(issue.done)
    
    def test_can_create_an_issue_with_a_name_and_status(self):
        issue = Issue(name="Create a Test", done=True)
        issue.save()
        self.assertEqual(issue.name, "Create a Test")
        self.assertTrue(issue.done)