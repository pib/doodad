from doodad import Column, Doodad, Row

from unittest import TestCase


class ToStrTest(TestCase):
    def test_str_empty(self):
        self.assertEqual(str(Row()), '<div class="row"></div>')
        self.assertEqual(str(Column()), '<div class="columns"></div>')
        self.assertEqual(str(Doodad()), '<div class="doodad"></div>')

    def test_str_extra_class(self):
        row = Row()
        column = Column()
        doodad = Doodad()
        row.extra_class = 'foo'
        column.extra_class = 'bar'
        doodad.extra_class = 'baz'
        self.assertEqual(str(row), '<div class="foo row"></div>')
        self.assertEqual(str(column), '<div class="bar columns"></div>')
        self.assertEqual(str(doodad), '<div class="baz doodad"></div>')

    def test_children_in_column(self):
        self.assertEqual(
            str(Column(Row(), Doodad())),
            '<div class="columns"><div class="row"></div>'
            '<div class="doodad"></div></div>')

    def test_columns_in_rows(self):
        col1 = Column()
        col2 = Column()
        self.assertEqual(str(Row(col1)),
                         '<div class="row">'
                         '<div class="large-12 columns"></div>'
                         '</div>')
        self.assertEqual(str(col1), '<div class="columns"></div>')

        self.assertEqual(str(Row(col1, col2)),
                         '<div class="row">'
                         '<div class="large-6 columns"></div>'
                         '<div class="large-6 columns"></div>'
                         '</div>')
        self.assertEqual(str(col1), '<div class="columns"></div>')
        self.assertEqual(str(col2), '<div class="columns"></div>')
