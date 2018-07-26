import xlrd as read
import xlwt as write
import os

class ExcelOperations:
    filepath =''
    listofLines=[]
    readExcelDatsList=[]

    def getDataFromFile(self):
        file=open('')
        for line in file.readlines():
            ExcelOperations.listofLines.append(line.rstrip())

    def writeInToExcel(self):
        wb =write.Workbook()
        sheet=wb.add_sheet('UserInfo')
        count=0
        cols=[]
        for items in ExcelOperations.listofLines:
            for words in items.spilt(','):
                cols.append(words)

        for num in range(ExcelOperations.listofLines.__len__()):
            row=sheet.row(num)
            for item in range(3):
                row.write(item,cols.__getitem__(count))

        wb.save(ExcelOperations.filepath)

    def readDataFromExcel(self):
        wb = read.open_workbook(ExcelOperations.filepath)

