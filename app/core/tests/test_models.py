from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@test.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(
        email, password
    )


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful."""
        email = 'test@test.com'
        password = 'passSssS123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email, "email is not {0}".format(email))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@Test.com'
        user = get_user_model().objects.create_user(email, 'test123')
        print(user.email)
        self.assertEqual(user.email, email.lower())
        pass

    def test_new_user_invalid_email(self):
        """Teste creating user with no email error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='vegan',
        )
        self.assertEqual(str(tag), tag.name)
