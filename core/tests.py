from django.test import TestCase

# Create your tests here.
class TestClass(TestCase):
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")