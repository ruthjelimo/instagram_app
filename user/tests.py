# Create your tests here.
from django.test import TestCase
from .models import Profile, User, Comment


class ProfileTest(TestCase):

    def setUp(self):
        self.new_user = User(username='mimoh', email='mimoh@gmail.com', password='mimoh12345')
        self.new_user.save()
        self.new_profile = Profile(picture='sports.jpeg', bio='sports', user=self.new_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_save_method(self):
        self.new_profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)
    
  