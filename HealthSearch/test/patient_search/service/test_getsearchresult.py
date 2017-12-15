from django.test import TestCase
from patientSearch.service import get_search_result


class GetSearchResultTestCase(TestCase):
  def test_age_domain(self):
    self.assertEqual(get_search_result.get_age_domain(age=8), 'child')
    self.assertEqual(get_search_result.get_age_domain(age=16), 'child')
    self.assertEqual(get_search_result.get_age_domain(age=44), 'youth')
    self.assertEqual(get_search_result.get_age_domain(age=53), 'middle age')
    self.assertEqual(get_search_result.get_age_domain(age=88), 'old age')

  def test_get_searchparam(self):
    self.assertEqual(
      get_search_result.get_search_param(24, 'heart failure', 'headache'),
      'youth+heart failure+headache')

  def test_search_url(self):
    self.assertEqual(get_search_result.get_search_url(
      'https://www.webmd.com/search/search_results/default.aspx', 24,
      'heart failure', 'headache'),
                     'https://www.webmd.com/search/search_results/default.aspx?query=youth+heart failure+headache')
