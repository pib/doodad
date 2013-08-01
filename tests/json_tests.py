from doodad import Column, Doodad, Layout, Row
from unittest import TestCase


class ToDictTest(TestCase):
    def test_empty_layout(self):
        layout = Layout()
        expected = {
            'rows': []
        }
        self.assertEqual(layout.to_dict(), expected)

    def test_empty_row(self):
        row = Row()
        expected = {
            'columns': []
        }
        self.assertEqual(row.to_dict(), expected)

    def test_empty_column(self):
        column = Column()
        expected = {
            'doodads': [],
            'rows': []
        }
        self.assertEqual(column.to_dict(), expected)

    def test_column_with_explicit_empty_rows(self):
        column = Column(rows=[])
        expected = {
            'doodads': [],
            'rows': []
        }
        self.assertEqual(column.to_dict(), expected)

    def test_column_with_rows(self):
        column = Column(rows=[Row()])
        expected = {
            'doodads': [],
            'rows': [{'columns': []}]
        }
        self.assertEqual(column.to_dict(), expected)

    def test_column_with_doodad(self):
        column = Column(Doodad())
        expected = {
            'doodads': [{'type': 'Doodad'}],
            'rows': []
        }
        self.assertEqual(column.to_dict(), expected)

    def test_with_bad_children(self):
        self.assertRaises(AssertionError, Layout, "Wait, I'm not a row!")
        self.assertRaises(AssertionError, Row, "Wait, I'm not a column!")
        self.assertRaises(AssertionError, Column, "Wait, I'm not a doodad!")

    def test_layout_with_empty_row(self):
        layout = Layout(Row())
        expected = {
            'rows': [{'columns': []}]
        }
        self.assertEqual(layout.to_dict(), expected)

    def test_layout_with_row_with_empty_column(self):
        layout = Layout(Row(Column()))
        expected = {
            'rows': [{'columns': [{'doodads': [], 'rows': []}]}]
        }
        self.assertEqual(layout.to_dict(), expected)

    def test_layout_with_empty_and_nonempty_rows(self):
        layout = Layout(Row(), Row(Column()))
        expected = {
            'rows': [
                {'columns': []},
                {'columns': [{'doodads': [], 'rows': []}]}
            ]
        }
        self.assertEqual(layout.to_dict(), expected)
