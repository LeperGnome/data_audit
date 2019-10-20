import os
import re
import io
from collections import defaultdict
from docx import Document


class DocParser:
    def __init__(self, keywords, data_path="test_data/test_1.docx"):
        self.document = self.read_doc(data_path)
        self.keywords = keywords
        self.vectors = []

    def read_doc(self, data_path):
        current_path = os.path.dirname(__file__)
        full_data_path = os.path.join(current_path, data_path)
        document = Document(full_data_path)
        return document

    def is_header(self, cell):
        if any(keyword in cell.text.lower() for keyword in self.keywords):
            return True
        else:
            return False

    @staticmethod
    def del_dict_empty(the_dict, entries):
        for key in entries:
            if key in the_dict:
                del the_dict[key]
        return the_dict

    @staticmethod
    def format_cell(cell, is_header=False):
        regex = re.compile(r'[\n\r\t]')
        cell.text = regex.sub("", cell.text)
        cell.text = cell.text.strip()
        cell.text = cell.text.lower()
        if not is_header:
            cell.text = cell.text.replace(u'\xa0', ' ')
            cell.text = re.sub(r' ', '', cell.text)
            cell.text = re.sub(',', '.', cell.text)
        return cell

    def clear_table_vetors(self, table_vectors):
        del_rows = set()
        for key in table_vectors.keys():
            row = table_vectors[key]
            if not all(any(keyword in vector_key for vector_key in table_vectors[key].keys()) for keyword in self.keywords):
                del_rows.add(key)
        table_vectors = self.del_dict_empty(table_vectors, del_rows)
        return table_vectors

    def parse_tables(self):
        tbls = self.document.tables
        for table in tbls:
            table_values = defaultdict(dict)
            for column in table.columns:
                header = ''
                for row_n, cell in enumerate(column.cells):
                    if header and cell.text:
                        cell = self.format_cell(cell)
                        table_values[row_n][header] = cell.text
                    elif self.is_header(cell):
                        cell = self.format_cell(cell, is_header=True)
                        header = cell.text
            table_values = self.clear_table_vetors(table_values)
            self.vectors.append(table_values)
        self.vectors = [vector for vector in self.vectors if vector]


if __name__ == "__main__":
    keywords = ['площадь', 'дней', 'стоимость']
    parser = DocParser(keywords, 'test_data/test_1.docx')
    parser.parse_tables()
    print(parser.vectors)
