from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase, override_settings

from mozilla_django_oidc.utils import absolutify, import_from_settings


class SettingImportTestCase(TestCase):

    @override_settings(EXAMPLE_VARIABLE='example_value')
    def test_attr_existing_no_default_value(self):
        s = import_from_settings('EXAMPLE_VARIABLE')
        self.assertEqual(s, 'example_value')

    def test_attr_nonexisting_no_default_value(self):
        with self.assertRaises(ImproperlyConfigured):
            import_from_settings('EXAMPLE_VARIABLE')

    def test_attr_nonexisting_default_value(self):
        s = import_from_settings('EXAMPLE_VARIABLE', 'example_default')
        self.assertEqual(s, 'example_default')


class AbsolutifyTestCase(TestCase):
    @override_settings(SITE_URL='http://site-url.com')
    def test_absolutify(self):
        url = absolutify('/foo/bar')
        self.assertEqual(url, 'http://site-url.com/foo/bar')
