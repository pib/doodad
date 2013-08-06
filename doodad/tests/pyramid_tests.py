from doodad import Doodad, pyramid_support
from pyramid import testing, threadlocal
from pyramid.renderers import render
from unittest import TestCase


class PyramidRenderTest(TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.config.include(pyramid_support)
        self.req = threadlocal.get_current_request()

    def tearDown(self):
        testing.tearDown()

    def test_basic_render(self):
        doodad = Doodad()
        expected = '<div class="doodad"></div>'
        self.assertEqual(render('doodad', doodad, request=self.req), expected)
