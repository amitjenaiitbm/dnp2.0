import csv
import os

#Python libraries
from fpdf import FPDF

def create_first_page(pdf):
    #Top banner
    pdf.image("./resources/topBanner-1.png", x=0, y=0, w=WIDTH)

def create_second_page(pdf):


def create_third_page(pdf):


def create_fourth_page(pdf):


def create_report(filename):
    pdf = FPDF()

    #Add custom fonts
    pdf.add_font('Roboto-Regular', '',
                './custom_fonts/Roboto-Regular.ttf',
                uni=True)
    pdf.add_font('Roboto-Bold', 'B',
                './custom_fonts/Roboto-Bold.ttf',
                uni=True)

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
    path = 'generated_dnp/comparable_dnp_english'
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
        filename="{}-{}".format(district, state)
        create_report(filename)
