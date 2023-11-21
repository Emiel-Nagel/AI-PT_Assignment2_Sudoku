import os
import openpyxl


class Excel_Writer:
    def __init__(self):
        current_directory = os.getcwd()
        mother_directory = os.path.split(current_directory)[0]
        self.output_directory = os.path.join(mother_directory, "Data")
        self.filename = "Data.xlsx"
        self.data = {
            "Sudoku": "",
            "Heuristic": "",
            "Step Count": "",
            "Victory": "",
        }
        self.delimiter = ';'

    def append_data(self, datatype, data):
        """
        This method appends output data
        """
        self.data[datatype] += data + self.delimiter

    def fill_out_file(self):
        """
        This method will fill out the excel file with the data
        """
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        for row_index, key in enumerate(self.data.keys()):
            data = self.data.get(key)
            for column_index, cell in enumerate(data.split(self.delimiter)):
                sheet.cell(row=row_index + 1, column=column_index + 1, value=cell)
        workbook.save(os.path.join(self.output_directory, self.filename))
