import pandas as pd

class RawRepo:

    def __init__(self, conf):
        params = conf.params


    @staticmethod
    def show_tables(table_name, tables_pdf) -> bool:

        if tables_pdf.shape[0] >= 1:
            tables_pdf.display()
            return True
        print(f"{table_name} Table not found")
        return False
