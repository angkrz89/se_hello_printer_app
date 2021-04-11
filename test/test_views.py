import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output(self):
        test_data = {"imie": "Angelika", "msg": "Hello World!"}
        rv = self.app.get('/?output=json')
        self.assertEqual(json.dumps(test_data), rv.data)
    #    self.assertEqual(b'{ "imie":"Angelika", "msg":"Hello World!"}', rv.data)

    def test_msg_with_xml_output(self):
        rv = self.app.get('/?output=xml')
        self.assertEqual(b'<imie>Angelika</imie><msg>Hello World</msg>', rv.data)
