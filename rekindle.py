import sys
import re
import decimal
from pyPdf import PdfFileWriter, PdfFileReader
from copy import copy

if len(sys.argv) <= 1:
  print "No input filename given."
  exit()
  
filename = sys.argv[1]

output = PdfFileWriter()
input = PdfFileReader(file(filename, "rb"))

print "Input doc has %s pages." % input.getNumPages()
print "title = %s" % (input.getDocumentInfo().title)

page = input.getPage(0)
leftMediaBox = copy(page.mediaBox)
rightMediaBox = copy(page.mediaBox)

margin = (leftMediaBox.getUpperRight_x() - leftMediaBox.getUpperLeft_x()) * decimal.Decimal(".07")

leftMediaBox.upperRight = (
  (leftMediaBox.getUpperLeft_x() + leftMediaBox.getUpperRight_x()) / 2,
  leftMediaBox.getUpperRight_y(),
)
leftMediaBox.upperLeft = (
  leftMediaBox.getUpperLeft_x() + margin,
  leftMediaBox.getUpperLeft_y(),
)
rightMediaBox.upperLeft = (
  (rightMediaBox.getUpperLeft_x() + rightMediaBox.getUpperRight_x()) / 2,
  rightMediaBox.getUpperRight_y(),
)
rightMediaBox.upperRight = (
  rightMediaBox.getUpperRight_x() - margin,
  rightMediaBox.getUpperRight_y(),
)

left2 = copy(leftMediaBox)
left2.upperLeft = (
  leftMediaBox.getUpperLeft_x(),
  leftMediaBox.getUpperLeft_y() / 2 + margin / 2,
)
left1 = copy(leftMediaBox)
left1.lowerLeft = (
  leftMediaBox.getUpperLeft_x(),
  leftMediaBox.getUpperLeft_y() / 2 - margin / 2,
)

right2 = copy(rightMediaBox)
right2.upperRight = (
  rightMediaBox.getUpperRight_x(),
  rightMediaBox.getUpperRight_y() / 2 + margin / 2,
)
right1 = copy(rightMediaBox)
right1.lowerRight = (
  rightMediaBox.getUpperRight_x(),
  rightMediaBox.getUpperRight_y() / 2 - margin / 2,
)

for i in range(0, input.getNumPages()):
  page = copy(input.getPage(i))
  page.mediaBox = left1
  output.addPage(page)
  page = copy(input.getPage(i))
  page.mediaBox = left2
  output.addPage(page)
  page = copy(input.getPage(i))
  page.mediaBox = right1
  output.addPage(page)
  page = copy(input.getPage(i))
  page.mediaBox = right2
  output.addPage(page)

filename = re.sub("(\\.pdf)?$", ".kindle.pdf", filename) 

outputStream = file(filename, "wb")
output.write(outputStream)
outputStream.close()