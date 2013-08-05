from doodad import Column, Doodad, Row
from unittest import TestCase


class ToDictTest(TestCase):
    def test_empty_row(self):
        row = Row()
        expected = {
            'type': 'doodad.Row',
            'children': []
        }
        self.assertEqual(row.to_dict(), expected)

    def test_empty_column(self):
        column = Column()
        expected = {
            'type': 'doodad.Column',
            'children': []
        }
        self.assertEqual(column.to_dict(), expected)

    def test_column_with_rows(self):
        column = Column(Row())
        expected = {
            'type': 'doodad.Column',
            'children': [{'type': 'doodad.Row', 'children': []}]
        }
        self.assertEqual(column.to_dict(), expected)

    def test_column_with_doodad(self):
        column = Column(Doodad())
        expected = {
            'type': 'doodad.Column',
            'children': [{'type': 'doodad.Doodad'}],
        }
        self.assertEqual(column.to_dict(), expected)

    def test_with_bad_children(self):
        self.assertRaises(AssertionError, Row, "Wait, I'm not a doodad!")
        self.assertRaises(AssertionError, Column, "Wait, I'm not a doodad!")

    def test_column_with_row_with_empty_column(self):
        layout = Column(Row(Column()))
        expected = {
            'type': 'doodad.Column',
            'children': [{
                    'type': 'doodad.Row',
                    'children': [{'type': 'doodad.Column', 'children': []}]
            }]
        }
        self.assertEqual(layout.to_dict(), expected)

    def test_column_with_empty_and_nonempty_rows(self):
        layout = Column(Row(), Row(Column()))
        expected = {
            'type': 'doodad.Column',
            'children': [
                {'type': 'doodad.Row', 'children': []},
                {'type': 'doodad.Row', 'children': [
                    {'type': 'doodad.Column', 'children': []}
                ]}
            ]
        }
        self.assertEqual(layout.to_dict(), expected)

    def test_doodad_attrs(self):
        doodad = Doodad(foo='bar', bar='baz')
        expected = {
            'type': 'doodad.Doodad',
            'foo': 'bar',
            'bar': 'baz'
        }
        self.assertEqual(doodad.to_dict(), expected)

    def test_container_attrs(self):
        doodad = Column(Row(Column(), Column(), fizz='buzz'),
                        foo='bar', bar='baz')
        expected = {
            'type': 'doodad.Column',
            'foo': 'bar',
            'bar': 'baz',
            'children': [{'type': 'doodad.Row',
                          'fizz': 'buzz',
                          'children': [
                              {'type': 'doodad.Column', 'children': []},
                              {'type': 'doodad.Column', 'children': []}]}]}
        self.assertEqual(doodad.to_dict(), expected)


class FromDictTest(TestCase):
    def test_empty_row(self):
        source = {
            'type': 'doodad.Row',
            'children': []
        }
        row = Doodad.from_dict(source)
        self.assertIsInstance(row, Row)
        self.assertEqual(row._children, ())

    def test_empty_column(self):
        source = {
            'type': 'doodad.Column',
            'children': []
        }
        column = Doodad.from_dict(source)
        self.assertIsInstance(column, Column)
        self.assertEqual(column._children, ())

    def test_nested(self):
        source = {
            'type': 'doodad.Column',
            'children': [
                {'type': 'doodad.Row',
                 'children': [{'type': 'doodad.Column'}]},
                {'type': 'doodad.Doodad'}
            ]
        }
        column = Doodad.from_dict(source)
        self.assertIsInstance(column, Column)
        self.assertEqual(len(column._children), 2)
        self.assertIsInstance(column._children[0], Row)
        self.assertEqual(column._children[1].__class__, Doodad)
        self.assertEqual(column._children[0]._children[0].__class__, Column)

    def test_doodad_attrs(self):
        source = {
            'type': 'doodad.Doodad',
            'foo': 'bar',
            'bar': 'baz'
        }
        doodad = Doodad.from_dict(source)
        self.assertEqual(doodad.to_dict(), source)

    def test_container_attrs(self):
        source = {
            'type': 'doodad.Row',
            'one': 'two',
            'three': 'four',
            'children': []
        }
        row = Doodad.from_dict(source)
        self.assertEqual(row.to_dict(), source)

    def test_row_columns_only(self):
        source = {
            'type': 'doodad.Row',
            'children': [{'type': 'doodad.Doodad'}]
        }
        self.assertRaises(AssertionError, Doodad.from_dict, source)
