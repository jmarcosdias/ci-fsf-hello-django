from django.test import TestCase
from .forms import ItemForm 

class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = ItemForm({'name':''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        # we use index 0 here to get the first error in field name (only error expected)
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])


