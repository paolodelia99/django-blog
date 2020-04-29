from django.test import TestCase

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

class IndexViewTest(TestCase):

    def test_no_post(self):
        """
            If no posts exist an appropriate message is displayed
        """
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No posts are available.")
        self.assertQuerysetEqual(response.context['latest_posts'], [])