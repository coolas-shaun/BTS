import openpyxl


class ExcelUtils:



    def __int__(self, path):
        self.path = path

    # return sheet object of current excel
    def load_excel_sheet(self):
        wb_obj = openpyxl.load_workbook(self.path)
        sheet_obj = wb_obj.active
        return sheet_obj
