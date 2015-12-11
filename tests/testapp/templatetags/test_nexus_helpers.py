from bs4 import BeautifulSoup
from django.template import Context, Template
from django.test import SimpleTestCase

import nexus


class NexusHelpersTests(SimpleTestCase):

    def test_nexus_media_prefix(self):
        out = Template('''
            {% load nexus_media_prefix from nexus_helpers %}
            {% nexus_media_prefix %}
        ''').render(Context()).strip()
        assert out == '/nexus/media'

    def test_nexus_version(self):
        out = Template('''
            {% load nexus_version from nexus_helpers %}
            {% nexus_version %}
        ''').render(Context()).strip()
        assert out == nexus.__version__

    def test_show_navigation(self):
        out = Template('''
            {% load show_navigation from nexus_helpers %}
            {% show_navigation %}
        ''').render(Context()).strip()
        BeautifulSoup(out)  # checks it is valid HTML
