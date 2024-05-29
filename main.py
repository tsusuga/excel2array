from lxml import etree
from openpyxl import load_workbook

def excel_to_xml(file_path):
  wb = load_workbook(file_path) # Load the Excel file
  xml_data = []

  for sheet_name in wb.sheetnames:
    ws = wb[sheet_name]
    root = etree.Element("sheet_name")

    for row in ws.iter_rows(values_only=True):
      xml_row = etree.SubElement(root, 'row')
      for value in row:
        etree.SubElement(xml_row, 'cell').text = str(value)

    xml_data.append(etree.tostring(root, pretty_print=True).decode('utf-8'))

  return xml_data


excel_file = "data.xlsx"

xml_data_list = excel_to_xml(excel_file)

for i, xml_data in enumerate(xml_data_list, start=1):
  with open(f"dest/data{i}.txt", "w", newline="") as f:
    f.write(xml_data)