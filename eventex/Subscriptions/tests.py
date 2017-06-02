from django.test import TestCase
from eventex.Subscriptions.forms import SubscriptionForm

class SubcribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        """ Get /inscricao/ must return status code 200 """
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        """ Must use Subscriptions/subscriptions_form.thml """
        self.assertTemplateUsed(self.resp, 'Subscriptions/subscription_form.html')

    def test_html(self):
        """ html must contain inputs tags """
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="test"', 3)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        """ Html must constain csrf """
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """ Context must have subscription form """
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        """ Form must have 4 fields """
        form = self.resp.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'emal', 'fone'], list(form.fields))