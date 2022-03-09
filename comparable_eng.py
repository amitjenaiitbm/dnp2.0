#Python libraries
from fpdf import FPDF

#Local imports

WIDTH = 210
HEIGHT = 297

STATE = "Dadra & Nagar Haveli and Daman & Diu"
DISTRICT = "Dadra & Nagar Haveli"

def create_first_page(pdf):
    #Top banner
    pdf.image("./resources/topBanner-1.png", x=0, y=0, w=WIDTH)

    #Orange rectangle showing the state, district name and month
    pdf.set_fill_color(231, 121, 37)
    pdf.rect(x=0, y=40.5, w=WIDTH, h=10, style = 'F')
    #State, District
    # pdf.add_font('Arial', '', 'Roboto.ttf', uni=True)
    pdf.set_font('Arial', 'B', 13)
    print_text = DISTRICT.upper() + " | " + STATE.upper()
    pdf.set_xy(x=8, y=41)
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.cell(100, 10, print_text, 0, 0, 'L')
    #month
    pdf.set_font('Arial', 'B', 13)
    pdf.set_xy(x=192, y=41)
    pdf.cell(10, 10, 'MARCH 2022', 0, 0, 'R')

    #About DNPs: Title
    pdf.set_font('Arial', 'B', 13)
    pdf.set_xy(x=8, y=54)
    pdf.set_text_color(r=231, g=121, b=37)
    pdf.cell(100, 10, 'About District Nutrition Profiles:', 0, 0, 'L')
    #About DNPs: Description Text
    pdf.set_font('Arial', '', 10)
    pdf.set_xy(x=8, y=63)
    pdf.set_text_color(r=0, g=0, b=0)
    DNP_desc_text = 'District Nutrition Profiles (DNPs) are available for 707 districts in India. They present trends for key nutrition and health outcomes and their cross-sectoral determinants in a district. The DNPs are based on data from the National Family Health Survey (NFHS)-4 (2015-2016) and NFHS-5 (2019-2020). They are aimed primarily at district administrators, state functionaries, local leaders, and development actors working at the district-level.'
    pdf.multi_cell(115, 4.5, DNP_desc_text, 0, 'J')

    #Add state map
    map_path = './Shared/Maps_DNP1.0/Andaman & Nicobar Islands/' + 'NMidAndaman-GS.jpg'
    pdf.image(map_path, x=125, y=53, w=75, h=40)

    #State map caption
    pdf.set_xy(x=125, y=92)
    #Regular text
    # text = 'Figure 1:' + ' Map highlights district ' + DISTRICT + ' in the state/UT of ' + STATE
    # pdf.set_font('Arial', '', 7)
    # pdf.multi_cell(75, 3, text, 0, 'L')
    # Markdown: Bold, regular, bold
    # pdf.set_text_color(r=0, g=0, b=0)
    # pdf.set_font('Arial', 'B', 7)
    # text1 = 'Figure 1:'
    # pdf.multi_cell(50, 7, text1, 0, 'L')
    # pdf.write(7, 'Figure 1:',)
    # pdf.set_font('Arial', '', 7)
    # text2 =  ' Map highlights district ' + DISTRICT + ' in the state/UT of ' + STATE
    # pdf.set_xy(x=130+1+len(text1), y=90)
    # pdf.multi_cell(50, 7, text2, 0, 'L')
    # # pdf.write(7, ' Map highlights district ' + DISTRICT + ' in the state of ',)
    # pdf.set_font('Arial', 'B', 7)
    # pdf.set_xy(x=130+1+len(text1)+len(text2), y=90)
    # pdf.multi_cell(50, 7, STATE, 0, 'L')
    # # pdf.write(7, STATE,)

    #Add framework as image
    pdf.image("./resources/framework.png", x=8, y=105, w=88, h=64)
    #Framework image caption
    pdf.set_text_color(r=0, g=0, b=0)
    pdf.set_xy(8, 170)
    pdf.set_font('Arial', 'B', 7)
    pdf.cell(7, 7, 'Source:', 0, 0, 'L')
    pdf.set_xy(17, 170)
    pdf.set_font('Arial', '', 7)
    pdf.cell(30, 7, ' Adapted from Black et al. (2008)', 0, 0, 'L')

    #Factors for child undernutrition: Title
    pdf.set_font('Arial', 'B', 13)
    pdf.set_xy(x=100, y=100)
    pdf.set_text_color(r=231, g=121, b=37)
    pdf.cell(105, 10, 'What factors lead to child undernutrition?', 0, 0, 'L')
    #Child undernutrition: Description Text
    pdf.set_font('Arial', '', 10)
    pdf.set_xy(x=100, y=110)
    pdf.set_text_color(r=0, g=0, b=0)
    Undernut_desc_text = 'Given the focus of India’s national nutrition mission on child undernutrition , the DNPs focus in on the determinants of child undernutrition (Figure on the left). Multiple determinants of suboptimal child nutrition and development contribute to the outcomes seen at the district-level. Different types of interventions can influence these determinants. Immediate determinants include inadequacies in food, health, and care for infants and young children, especially in the first two years of life. Nutrition-specific interventions such as health service delivery at the right time during pregnancy and early childhood can affect immediate determinants. Underlying and basic determinants include women’s status, household food security, hygiene, and socio-economic conditions. Nutrition-sensitive interventions such as social safety nets, sanitation programs, women’s empowerment, and agriculture programs can affect underlying and basic determinants.'
    pdf.multi_cell(102, 4.5, Undernut_desc_text, 0, 'J')

    #Gray rectangle showing the state values and district name
    pdf.set_fill_color(109, 111, 113)
    pdf.rect(x=7, y=184, w=WIDTH-14, h=10, style = 'F')
    #Left Title
    # pdf.add_font('Arial', '', 'Roboto.ttf', uni=True)
    pdf.set_font('Arial', 'B', 13)
    print_text1 = 'District demographic profile, 2019-20'
    pdf.set_xy(x=10, y=184)
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.cell(100, 10, print_text1, 0, 0, 'L')
    #District
    pdf.set_font('Arial', 'B', 11)
    pdf.set_xy(x=160, y=183)
    pdf.cell(40, 12, DISTRICT, 0, 0, 'R')

    #State nutrition Profiles
    pdf.image("./resources/state_nut_prof.png", x=7, y=195, w=WIDTH-14)

    #Source
    pdf.set_text_color(r=0, g=0, b=0)
    pdf.set_font('Arial', 'B', 7)
    pdf.set_xy(x=8, y=249)
    pdf.multi_cell(20, 7, 'Source:', 0, 'L')
    #First Source
    pdf.set_font('Arial', '', 7)
    pdf.set_xy(x=9, y=254)
    source_one = '1. IFPRI estimates - The headcount was calculated as the product of the undernutrition prevalence and the total eligible projected population for each district in 2019. Projected population for 2019 was estimated using Census 2011.'
    pdf.multi_cell(WIDTH-16, 3, source_one, 0, 'L')
    #Second Source
    pdf.set_font('Arial', '', 7)
    pdf.set_xy(x=9, y=260)
    source_two = '2. NFHS-4 (2015-16) & NFHS-5 district & state factsheets (2019-20).'
    pdf.multi_cell(WIDTH-16, 3, source_two, 0, 'L')

    #Horizontal line
    pdf.set_draw_color(109, 111, 113)
    pdf.set_line_width(0.75)
    pdf.line(0, 265, WIDTH, 265)

    #Add author note
    pdf.set_font('Arial', '', 7)
    pdf.set_xy(x=8, y=267)
    acknowledgement = 'This District Nutrition Profile was prepared by IFPRI in collaboration with NITI Aayog, International Institute for Population Sciences, UNICEF, Institute of Economic Growth and Data Dent with technical support from Amit Jena (Consultant). It was published in March 2022.'
    pdf.multi_cell(WIDTH-14, 3, acknowledgement, 0, 'L')

    #Add logos
    pdf.image("./resources/logos.png", x=30, y=275, w=150, h=18)

def create_second_page(pdf):
    #First Rectangle Children and district name
    pdf.set_fill_color(41, 119, 115)
    pdf.rect(x=7, y=5, w=WIDTH-14, h=10, style = 'F')
    #Left Title
    # pdf.add_font('Arial', '', 'Roboto.ttf', uni=True)
    pdf.set_font('Arial', 'B', 13)
    print_text11 = 'The state of nutrition outcomes among children (<5 years)'
    pdf.set_xy(x=10, y=5)
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.cell(100, 10, print_text11, 0, 0, 'L')
    #District
    pdf.set_font('Arial', 'B', 11)
    pdf.set_xy(x=160, y=4)
    pdf.cell(40, 12, DISTRICT, 0, 0, 'R')

    #First Rectangle Discussion Points
    pdf.set_fill_color(183, 179, 160)
    pdf.rect(x=7, y=51, w=WIDTH-14, h=18, style = 'F')
    #Discussion Points
    pdf.set_text_color(r=0, g=0, b=0)
    pdf.set_font('Arial', 'B', 9)
    pdf.set_xy(x=8, y=52)
    pdf.multi_cell(100, 7, 'Points for discussion:', 0, 'L')
    #First point
    pdf.set_font('Arial', '', 9)
    pdf.set_xy(x=9, y=58)
    page2_dis_one = '* What are the trends in undernutrition among children under five years of age (stunting, wasting, underweight, and anemia)?'
    pdf.multi_cell(WIDTH-16, 4, page2_dis_one, 0, 'L')
    #Second point
    pdf.set_font('Arial', '', 9)
    pdf.set_xy(x=9, y=62)
    page2_dis_two = '* What are the trends in overweight/obesity among children under five years of age in the district?'
    pdf.multi_cell(WIDTH-16, 4, page2_dis_two, 0, 'L')

    #Second Rectangle Women and district name
    pdf.set_fill_color(41, 119, 115)
    pdf.rect(x=7, y=200, w=WIDTH-14, h=10, style = 'F')
    #Left Title
    # pdf.add_font('Arial', '', 'Roboto.ttf', uni=True)
    pdf.set_font('Arial', 'B', 13)
    print_text12 = 'The state of nutrition outcomes among women (15-49 years)'
    pdf.set_xy(x=10, y=200)
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.cell(100, 10, print_text12, 0, 0, 'L')
    #District
    pdf.set_font('Arial', 'B', 11)
    pdf.set_xy(x=160, y=249)
    pdf.cell(40, 12, DISTRICT, 0, 0, 'R')

    #Second Rectangle Discussion Points
    pdf.set_fill_color(183, 179, 160)
    pdf.rect(x=7, y=271, w=WIDTH-14, h=18, style = 'F')
    #Discussion Points
    pdf.set_text_color(r=0, g=0, b=0)
    pdf.set_font('Arial', 'B', 9)
    pdf.set_xy(x=8, y=274)
    # pdf.multi_cell(100, 2, 'Points for discussion:', 0, 'L')
    pdf.write(2, 'Points for discussion:')
    #First point
    # pdf.set_font('Arial', '', 9)
    # pdf.set_xy(x=9, y=275)
    # page2_dis_three = '* What are the trends in underweight and anemia among women (15-49 yrs) in the district?'
    # pdf.multi_cell(WIDTH-16, 1, page2_dis_three, 0, 'L')
    # #Second point
    # pdf.set_font('Arial', '', 9)
    # pdf.set_xy(x=9, y=276)
    # page2_dis_four = '* What are the trends in overweight/obesity and other nutrition-related non-communicable diseases in the district?'
    # pdf.multi_cell(WIDTH-16, 0, page2_dis_four, 0, 'L')

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

    pdf.output(filename, "F")

if __name__ == '__main__':
    filename="DNP2.pdf"
    create_report(filename)
