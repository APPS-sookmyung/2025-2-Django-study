import openpyxl as excel

#새로운 워크북을 생성
book = excel.Workbook()

#엑셀의 시트를 활성화하고, 시트의 셀 A1에 작성
sheet = book.active

for i in range(10):
    row_cell = sheet.cell(row=(i+1), column=1)
    row_cell.value = str(i+1) + " 번째 데이터 저장"

sheet.column_dimensions['A'].width=25
# 열 너비 조정

book.save("py_excel05.xlsx")