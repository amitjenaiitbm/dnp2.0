import csv
import os

#Python libraries
from fpdf import FPDF

WIDTH = 210
HEIGHT = 297

def create_first_page(pdf):
    #Top banner
    pdf.image("./resources/topBanner-1.png", x=0, y=0, w=WIDTH)

    # Add "District Nutrition Profile" text
    pdf.set_font('Roboto-Bold', 'B', 20)
    pdf.set_text_color(255, 255, 255)
    banner_text = "district nutrition profile"
    pdf.set_xy(100, 6)
    pdf.cell(80, 20, banner_text.upper())

    # Add orange rectangle banner
    pdf.set_draw_color(231, 121, 37)
    pdf.set_fill_color(231, 121, 37)
    pdf.rect(x=0, y=40.5, w=WIDTH, h=10, style='F')

    # Add District, State and Month
    pdf.set_font('Roboto-Bold', 'B', 13)
    pdf.set_text_color(255, 255, 255)
    orangeBanner_text = district[3].upper() + " | " + district[1].upper()
    pdf.set_xy(7, 41)
    pdf.cell(186, 10, orangeBanner_text, 0, 0, 'L')
    pdf.cell(10, 10, 'MARCH 2022', 0, 0, 'R')

    # About DNPs: Title
    pdf.set_font('Roboto-Bold', 'B', 13)
    pdf.set_text_color(231, 121, 37)
    pdf.set_xy(7, 54)
    aboutDNP_text = "About District Nutrition Profiles:"
    pdf.cell(100, 10, aboutDNP_text, 0, 0, 'L')
    # About DNPs: Description text
    pdf.set_font('Roboto-Regular', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(7, 63)
    DNPdesc_text = "District Nutrition Profiles (DNPs) are available for 707 districts in India. They present trends for key nutrition and health outcomes and their cross-sectoral determinants in a district. The DNPs are based on data from the National Family Health Survey (NFHS)-4 (2015-2016) and NFHS-5 (2019-2020). They are aimed primarily at district administrators, state functionaries, local leaders, and development actors working at the district-level."
    pdf.multi_cell(115, 4.5, DNPdesc_text, 0, 'J')

    # Add district map
    map_path = './data/maps/comparable_maps/{}.jpg'.format(district[4])
    pdf.image(map_path, x=125, y=53, w=75, h=40)
    # map caption
    figure1_text = "Figure 1:"
    mapCaption_text = "Map highlights district {} in the state/UT of {}".format(district[3], district[1])
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Roboto-Bold', 'B', 7)
    pdf.set_xy(125, 92)
    pdf.cell(9, 7, figure1_text, 0, 0, 'L')
    pdf.set_xy(125+9+1.5, 92)
    pdf.set_font('Roboto-Regular', '', 7)
    pdf.cell(60, 7, mapCaption_text[0:55]+'-', 0, 'L')
    pdf.set_xy(125, 95)
    pdf.cell(70, 7, mapCaption_text[55:], 0, 'L')

    # Add framework as image
    pdf.image("./resources/framework.png", x=8, y=105, w=90)
    # Add framework caption
    source_text = "Source:"
    frameworkCaption_text = "Adapted from Black et al. (2008)"
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Roboto-Bold', 'B', 7)
    pdf.set_xy(8, 170)
    pdf.cell(7, 7, source_text, 0, 0, 'L')
    pdf.set_xy(8+7+2, 170)
    pdf.set_font('Roboto-Regular', '', 7)
    pdf.cell(60, 7, frameworkCaption_text, 0, 'L')

    # Factors for child undernutrition: Title
    pdf.set_font('Roboto-Bold', 'B', 13)
    pdf.set_text_color(231, 121, 37)
    pdf.set_xy(100, 100)
    undernutrition_text = "What factors lead to child undernutrition?"
    pdf.cell(100, 10, undernutrition_text, 0, 0, 'L')
    # Child undernutrition: Description text
    pdf.set_font('Roboto-Regular', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(100, 110)
    undernutritionDesc_text = "Given the focus of India’s national nutrition mission on child undernutrition , the DNPs focus in on the determinants of child undernutrition (Figure on the left). Multiple determinants of suboptimal child nutrition and development contribute to the outcomes seen at the district-level. Different types of interventions can influence these determinants. Immediate determinants include inadequacies in food, health, and care for infants and young children, especially in the first two years of life. Nutrition-specific interventions such as health service delivery at the right time during pregnancy and early childhood can affect immediate determinants. Underlying and basic determinants include women’s status, household food security, hygiene, and socio-economic conditions. Nutrition-sensitive interventions such as social safety nets, sanitation programs, women’s empowerment, and agriculture programs can affect underlying and basic determinants."
    pdf.multi_cell(102, 4.5, undernutritionDesc_text, 0, 'J')

    # Add grey rectangle
    pdf.set_draw_color(109, 111, 113)
    pdf.set_fill_color(109, 111, 113)
    pdf.rect(x=7, y=184, w=WIDTH-14, h=10, style='F')
    # Add text into the grey bar
    greyBar_text = "District demographic profile, 2019-20"
    pdf.set_font('Roboto-Bold', 'B', 13)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(10, 184)
    pdf.cell(100, 10, greyBar_text, 0, 0, 'L')
    pdf.set_font('Roboto-Bold', 'B', 12)
    pdf.cell(90, 10, district[3], 0, 0, 'R')

    # State nutrition profiles
    pdf.image("./resources/state_nut_prof.png", x=7, y=195, w=WIDTH-14)
    # Sex ratio number
    pdf.set_font('Roboto-Bold', 'B', 28)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(20, 194)
    pdf.cell(40, 20, str("{:,}".format(round(float(district[5]))))+"/1,000", 0, 0, 'L')
    # Sex ratio text
    sexRatio_text1 = "Sex ratio (females per 1,000"
    sexRatio_text2 = "males) of the total population"
    pdf.set_font('Roboto-Bold', 'B', 10)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(20, 207)
    pdf.cell(55, 10, sexRatio_text1, 0, 0, 'L')
    pdf.set_xy(20, 211)
    pdf.cell(55, 10, sexRatio_text2, 0, 0, 'L')
    # Reproductive age number
    pdf.set_font('Roboto-Bold', 'B', 28)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(85, 194)
    pdf.cell(40, 20, str("{:,}".format(round(float(district[6])))), 0, 0, 'L')
    # Reproductive age text
    reproductive_text1 = "Number of women of"
    reproductive_text2 = "reproductive age (15–49 yrs)"
    pdf.set_font('Roboto-Bold', 'B', 10)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(85, 207)
    pdf.cell(55, 10, reproductive_text1, 0, 0, 'L')
    pdf.set_xy(85, 211)
    pdf.cell(55, 10, reproductive_text2, 0, 0, 'L')
    # Pregnant women number
    pdf.set_font('Roboto-Bold', 'B', 28)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(152, 194)
    pdf.cell(40, 20, str("{:,}".format(round(float(district[7])))), 0, 0, 'L')
    # Pregnant women text
    pregnantWomen_text1 = "Number of"
    pregnantWomen_text2 = "pregnant women"
    pdf.set_font('Roboto-Bold', 'B', 10)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(152, 207)
    pdf.cell(55, 10, pregnantWomen_text1, 0, 0, 'L')
    pdf.set_xy(152, 211)
    pdf.cell(55, 10, pregnantWomen_text2, 0, 0, 'L')
    # Live birth number
    pdf.set_font('Roboto-Bold', 'B', 28)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(20, 221)
    pdf.cell(40, 20, str("{:,}".format(round(float(district[8])))), 0, 0, 'L')
    # Live birth text
    liveBirth_text1 = "Number of live births"
    pdf.set_font('Roboto-Bold', 'B', 10)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(20, 234)
    pdf.cell(55, 10, liveBirth_text1, 0, 0, 'L')
    # Total children number
    pdf.set_font('Roboto-Bold', 'B', 28)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(85, 221)
    pdf.cell(40, 20, str("{:,}".format(round(float(district[9])))), 0, 0, 'L')
    # Total children text
    totalChildren_text1 = "Total number of children"
    totalChildren_text2 = "under 5 yrs"
    pdf.set_font('Roboto-Bold', 'B', 10)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(85, 234)
    pdf.cell(55, 10, totalChildren_text1, 0, 0, 'L')
    pdf.set_xy(85, 238)
    pdf.cell(55, 10, totalChildren_text2, 0, 0, 'L')
    # Births registered number
    pdf.set_font('Roboto-Bold', 'B', 28)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(152, 221)
    pdf.cell(40, 20, str("{:,}".format(round(float(district[10])))), 0, 0, 'L')
    # Births registered text
    birthsRegistered_text1 = "Number of"
    birthsRegistered_text2 = "pregnant women"
    pdf.set_font('Roboto-Bold', 'B', 10)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(152, 234)
    pdf.cell(55, 10, birthsRegistered_text1, 0, 0, 'L')
    pdf.set_xy(152, 238)
    pdf.cell(55, 10, birthsRegistered_text2, 0, 0, 'L')

    # source
    pdf.set_font('Roboto-Bold', 'B', 7)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(8, 249)
    pdf.cell(50, 3, "Source:", align='L')
    source1_text = "1. IFPRI estimates - The headcount was calculated as the product of the undernutrition prevalence and the total eligible projected population for each district in 2019. Projected population for 2019 was estimated using Census 2011."
    pdf.set_font('Roboto-Regular', '', 7)
    pdf.set_xy(8, 252)
    pdf.cell(180, 3, source1_text[0:178], align='L')
    pdf.set_xy(10.5, 255)
    pdf.cell(180, 3, source1_text[179:], align='L')
    source2_text = "2. NFHS-4 (2015-16) & NFHS-5 district & state factsheets (2019-20)."
    pdf.set_xy(8, 258)
    pdf.cell(200, 3, source2_text, align='L')

    # Horizontal line
    pdf.set_draw_color(109, 111, 113)
    pdf.set_line_width(0.75)
    pdf.line(0,262, WIDTH, 262)

    # citation
    citation_text = "Citation:"
    citation_text1 = "Singh. N., P.H. Nguyen, M. Jangid, S.K. Singh, R. Sarwal, N. Bhatia, R. Johnston, W. Joe, and P. Menon. 2022. District Nutrition Profile: {}, {}. New Delhi, India: International Food Policy Research Institute.".format(district[3], district[1])
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Roboto-Bold', 'B', 7)
    pdf.set_xy(8, 264)
    pdf.cell(9, 3, citation_text, 0, 0, 'L')
    pdf.set_xy(8+9+1, 264)
    pdf.set_font('Roboto-Regular', '', 7)
    pdf.cell(170, 3, citation_text1[0:167]+'-', 0, 'L')
    pdf.set_xy(8, 267)
    pdf.cell(170, 3, citation_text1[167:], 0, 'L')

    # Acknowledgement
    acknowledgement_text = "Acknowledgement:"
    acknowledgement_text1 = "Financial support was provided by the Bill & Melinda Gates Foundation through POSHAN, led by the International Food Policy Research Institute. We thank Amit Jena (Independent Researcher) for design and programming support."
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Roboto-Bold', 'B', 7)
    pdf.set_xy(8, 271)
    pdf.cell(9, 3, acknowledgement_text, 0, 0, 'L')
    pdf.set_xy(8+21+0.5, 271)
    pdf.set_font('Roboto-Regular', '', 7)
    pdf.cell(155, 3, acknowledgement_text1[0:152], 0, 'L')
    pdf.set_xy(8, 274)
    pdf.cell(155, 3, acknowledgement_text1[152:], 0, 'L')

    # Logos
    img_width = 120
    pdf.image("./resources/logos.png", x=(WIDTH-img_width)/2+1, y=278, w=img_width)

def create_second_page(pdf):
    # Add top bar
    pdf.set_draw_color(41, 119, 115)
    pdf.set_fill_color(41, 119, 115)
    pdf.rect(x=7, y=5, w=WIDTH-14, h=10, style='F')
    # Add text into the top bar
    top_Bar2_text = "The state of nutrition outcomes among children (<5 years)"
    pdf.set_font('Roboto-Bold', 'B', 13)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(10, 5)
    pdf.cell(100, 10, top_Bar2_text, 0, 0, 'L')
    pdf.set_font('Roboto-Bold', 'B', 12)
    pdf.cell(90, 10, district[3], 0, 0, 'R')

    # Add bottom bar
    pdf.set_draw_color(41, 119, 115)
    pdf.set_fill_color(41, 119, 115)
    pdf.rect(x=7, y=150, w=WIDTH-14, h=10, style='F')
    # Add text into the bottom bar
    bottom_Bar2_text = "The state of nutrition outcomes among women (15-49 years)"
    pdf.set_font('Roboto-Bold', 'B', 13)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(10, 150)
    pdf.cell(100, 10, bottom_Bar2_text, 0, 0, 'L')
    pdf.set_font('Roboto-Bold', 'B', 12)
    pdf.cell(90, 10, district[3], 0, 0, 'R')

def create_third_page(pdf):
    # Add top bar
    pdf.set_draw_color(0, 96, 162)
    pdf.set_fill_color(0, 96, 162)
    pdf.rect(x=7, y=5, w=WIDTH-14, h=10, style='F')
    # Add text into the top bar
    top_Bar3_text = "Immediate determinants"
    pdf.set_font('Roboto-Bold', 'B', 13)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(10, 5)
    pdf.cell(100, 10, top_Bar3_text, 0, 0, 'L')
    pdf.set_font('Roboto-Bold', 'B', 12)
    pdf.cell(90, 10, district[3], 0, 0, 'R')

    # Add bottom bar
    pdf.set_draw_color(152, 56, 87)
    pdf.set_fill_color(152, 56, 87)
    pdf.rect(x=7, y=150, w=WIDTH-14, h=10, style='F')
    # Add text into the bottom bar
    bottom_Bar3_text = "Underlying determinants"
    pdf.set_font('Roboto-Bold', 'B', 13)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(10, 150)
    pdf.cell(100, 10, bottom_Bar3_text, 0, 0, 'L')
    pdf.set_font('Roboto-Bold', 'B', 12)
    pdf.cell(90, 10, district[3], 0, 0, 'R')

def create_fourth_page(pdf):
    # Add top bar
    pdf.set_draw_color(91, 83, 134)
    pdf.set_fill_color(91, 83, 134)
    pdf.rect(x=7, y=5, w=WIDTH-14, h=10, style='F')
    # Add text into the top bar
    top_Bar4_text = "Trends in coverage of interventions across the first 1,000 days"
    pdf.set_font('Roboto-Bold', 'B', 13)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(10, 5)
    pdf.cell(100, 10, top_Bar4_text, 0, 0, 'L')
    pdf.set_font('Roboto-Bold', 'B', 12)
    pdf.cell(90, 10, district[3], 0, 0, 'R')
    

def create_report(filename):
    pdf = FPDF('P', 'mm', 'A4')

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
    dirName = path + '/{}'.format(district[1])
    if not os.path.exists(dirName):
        os.mkdir(dirName)
    pdf.output(dirName+'/'+filename, "F")

#Read CSV file
with open("./data/csv/comparable_district_data_temp.csv", 'r') as infile:
    reader = csv.reader(infile, delimiter=",")
    header = next(reader)
    for district in reader:
        print(district)
        #Generated DNP file name
        filename="{}-{}.pdf".format(district[3], district[1])
        create_report(filename)
