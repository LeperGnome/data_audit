import os
import re
import io
from collections import defaultdict
from docx import Document


class DocParser:
    def __init__(self, keywords, data_path="test_data/test_1.docx"):
        self.document = self.read_doc(data_path)
        self.keywords = keywords

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
    def format_cell(cell):
        cell.text.replace(u'\xa0', '')
        cell.text = cell.text.strip()
        # cell.text = re.sub(r'\\x..', '', cell.text)
        cell.text = re.sub(',', '.', cell.text)
        return cell

    def clear_vetors(self, vectors):
        for table_vectors in vectors:
            del_rows = set()
            for key in table_vectors.keys():
                if len(table_vectors[key].items()) < len(self.keywords):
                    del_rows.add(key)
            table_vectors = self.del_dict_empty(table_vectors, del_rows)
        vectors = [dict(x) for x in vectors if x]
        return vectors

    def parse_tables(self):
        tbls = self.document.tables
        vectors = []
        for table in tbls:
            table_values = defaultdict(dict)
            for column in table.columns:
                header = ''
                for row_n, cell in enumerate(column.cells):
                    cell = self.format_cell(cell)
                    if header and cell.text:
                        table_values[row_n][header] = cell.text
                    elif self.is_header(cell):
                        header = cell.text
            vectors.append(table_values)
        vectors = self.clear_vetors(vectors)
        return vectors


if __name__ == "__main__":
    keywords = ['площадь', 'стоимость']
    parser = DocParser(keywords)
    print(parser.parse_tables())
