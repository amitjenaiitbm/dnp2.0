import csv
import os

#Python libraries
from fpdf import FPDF

WIDTH = 210
HEIGHT = 297

def create_first_page(pdf):
    #Top banner
    pdf.image("./resources/topBanner-1.png", x=0, y=0, w=WIDTH)

    #Add logos
    pdf.image("./resources/logos.png", x=30, y=275, w=150, h=18)

def create_second_page(pdf):
    #First Rectangle Children and district name
    pdf.set_fill_color(41, 119, 115)
    pdf.rect(x=7, y=5, w=WIDTH-14, h=10, style = 'F')
    #Left Title

    #Page number-2
    pdf.image("./resources/page_no_2.png", x=0, y=290, w=WIDTH)

def create_third_page(pdf):
    pdf.image("./resources/topBanner-1.png", x=0, y=0, w=WIDTH)

    #Page number-3
    pdf.image("./resources/page_no_3.png", x=0, y=290, w=WIDTH)

def create_fourth_page(pdf):
    pdf.image("./resources/topBanner-1.png", x=0, y=0, w=WIDTH)

    #Page number-4
    pdf.image("./resources/page_no_4.png", x=0, y=290, w=WIDTH)

def create_report(filename):
    pdf = FPDF()

    # First Page
    pdf.add_page()
    create_first_page(pdf)

    # Second Page
    pdf.add_page()
    create_second_page(pdf)

    # Third Page
    pdf.add_page()
    create_third_page(pdf)

    # Fourth Page
    pdf.add_page()
    create_fourth_page(pdf)

    #create a sub-folder
    path = 'generated_dnp/comparable_eng'
    dirName = path + '/{}'.format(state)
    if not os.path.exists(dirName):
        os.mkdir(dirName)
    pdf.output(dirName+'/'+filename, "F")

#Read CSV file
with open("state_2016.csv", 'r') as infile:
    reader = csv.reader(infile, delimiter=",")
    header = next(reader)
    for row in reader:
        state = row[0]
        district = "Jena"
        children_stunted = row[1]
        children_wasted = row[2]

        #Generated DNP file name
        filename="{}_{}".format(state, district)
        create_report(filename)
