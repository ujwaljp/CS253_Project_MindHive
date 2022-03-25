from django.test import TestCase

from tags.models import Tag

class TagModelTest(TestCase):
    @classmethod
    def setUp(cls):
        Tag.objects.create(name='test tag')
    
    def test_name_label(self):
        tag = Tag.objects.get(id=1)
        field_label = tag._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
    
    def test_name_max_length(self):
        tag = Tag.objects.get(id=1)
        max_length = tag._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)
    
    
    
    
    
        
# Create your tests here.
