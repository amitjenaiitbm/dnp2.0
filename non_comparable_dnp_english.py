import csv
import os

#Python libraries
from fpdf import FPDF

WIDTH = 210
HEIGHT = 297
NA_desc_text = "Note: NA refers to data is unavailable for a given round of NFHS data."

def round_str(value):
    if value != '':
        return(str("{:,}".format(round(float(value)))))
    else:
        return("NA")
def draw_gridlines(pdf, x1, y1, y2):
        # Draw vertical grids
        pdf.set_draw_color(241, 240, 236)
        pdf.set_line_width(0.5)
        pdf.line(x1, y1, x1, y2)
        pdf.line(x1+10, y1, x1+10, y2)
        pdf.line(x1+20, y1, x1+20, y2)
        pdf.line(x1+30, y1, x1+30, y2)
        pdf.line(x1+40, y1, x1+40, y2)
        pdf.line(x1+50, y1, x1+50, y2)
        #
        pdf.set_draw_color(109, 111, 113)
        pdf.line(x1, y2, x1+50, y2)
        #
        pdf.set_draw_color(109, 111, 113)
        pdf.line(x1, y2, x1, y2+1)
        pdf.line(x1+10, y2, x1+10, y2+1)
        pdf.line(x1+20, y2, x1+20, y2+1)
        pdf.line(x1+30, y2, x1+30, y2+1)
        pdf.line(x1+40, y2, x1+40, y2+1)
        pdf.line(x1+50, y2, x1+50, y2+1)
        #
        pdf.set_font('Roboto-Regular', '', 8)
        pdf.set_text_color(109, 111, 113)
        pdf.set_xy(x1-3, y2+2)
        pdf.cell(4, 3, "0%", align="L")
        pdf.set_xy(x1+10-3, y2+2)
        pdf.cell(4, 3, "20%", align="L")
        pdf.set_xy(x1+20-3, y2+2)
        pdf.cell(4, 3, "40%", align="L")
        pdf.set_xy(x1+30-3, y2+2)
        pdf.cell(4, 3, "60%", align="L")
        pdf.set_xy(x1+40-3, y2+2)
        pdf.cell(4, 3, "80%", align="L")
        pdf.set_xy(x1+50-3, y2+2)
        pdf.cell(4, 3, "100%", align="L")

def draw_dual_lollipop(pdf, x1, y1, district_2016, district_2019):
    if district_2016 != '':
        x2 = x1+(0.5*float(district_2016))
        # Place green circle image
        pdf.image("./resources/green_circle.png", x=x2-1, y=y1-1.5, w=3)
        # Write the district value of 2016
        pdf.set_font('Roboto-Regular', '', 8)
        pdf.set_text_color(136, 180, 64)
        if district_2019 == '' or (float(district_2016) <= float(district_2019)):
            percent_text_pos = x2 - 5
            pdf.set_xy(percent_text_pos, y1-1.5)
            pdf.cell(4, 3, str(round(float(district_2016)))+"%", align="R")
        elif float(district_2016) > float(district_2019):
            percent_text_pos = x2 + 2
            pdf.set_xy(percent_text_pos, y1-1.5)
            pdf.cell(4, 3, str(round(float(district_2016)))+"%", align="L")

    if district_2019 != '':
        x2 = x1+(0.5*float(district_2019))
        # Place green circle image
        pdf.image("./resources/orange_circle.png", x=x2-1, y=y1-1.5, w=3)
        # Write the district value of 2016
        pdf.set_font('Roboto-Regular', '', 8)
        pdf.set_text_color(231, 121, 37)
        if district_2016 == '' or (float(district_2019) >= float(district_2016)):
            percent_text_pos = x2 + 2
            pdf.set_xy(percent_text_pos, y1-1.5)
            pdf.cell(4, 3, str(round(float(district_2019)))+"%", align="L")
        elif float(district_2019) < float(district_2016):
            percent_text_pos = x2 - 5
            pdf.set_xy(percent_text_pos, y1-1.5)
            pdf.cell(4, 3, str(round(float(district_2019)))+"%", align="R")

    # Draw the connecting arrow
    if (district_2016 != '') and (district_2019 != ''):
        # Draw connecting line
        pdf.set_draw_color(0, 0, 0)
        pdf.set_line_width(0.25)
        p = x1+(0.5*float(district_2016))+0.5
        q = x1+(0.5*float(district_2019))+0.5
        pdf.line(p, y1, q, y1)
        # Place arrow
        k = 0.75
        if float(district_2016) < float(district_2019):
            pdf.line(q, y1, q-k, y1-k)
            pdf.line(q, y1, q-k, y1+k)
        elif float(district_2016) > float(district_2019):
            pdf.line(p, y1, p-k, y1-k)
            pdf.line(p, y1, p-k, y1+k)

    # Print NA (2016) and NA (2019) if both are NOT available
    if (district_2016 == '') and (district_2019 == ''):
        # Print green NA (2016)
        pdf.set_font('Roboto-Regular', '', 8)
        pdf.set_text_color(136, 180, 64)
        pdf.set_xy(x1, y1)
        pdf.cell(4, 1, "NA", align="L")
        # Print orange NA (2019)
        pdf.set_text_color(231, 121, 37)
        pdf.set_xy(x1+10, y1)
        pdf.cell(4, 1, "NA", align="L")

def draw_green_lollipop(pdf, x1, y1, district_2016, state_2016):
    if district_2016 != '':
        x2 = x1+(0.5*float(district_2016))
        # Draw green line
        pdf.set_draw_color(136, 180, 64)
        pdf.set_line_width(0.75)
        pdf.line(x1, y1, x2, y1)
        # Place green circle image
        pdf.image("./resources/green_circle.png", x=x2-1, y=y1-1.5, w=3)
        # Draw state mark in grey
        x3 = x1+(0.5*float(state_2016))
        pdf.set_draw_color(109, 111, 113)
        pdf.set_line_width(0.75)
        pdf.line(x3, y1-1.5, x3, y1+1.5)
        # Write the district value of 2016
        pdf.set_font('Roboto-Regular', '', 8)
        pdf.set_text_color(136, 180, 64)
        percent_text_pos = x2 + 3
        pdf.set_xy(percent_text_pos, y1-1.5)
        pdf.cell(4, 3, str(round(float(district_2016)))+"%", align="L")
    else:
        # Print NA
        pdf.set_font('Roboto-Regular', '', 8)
        pdf.set_text_color(136, 180, 64)
        pdf.set_xy(x1, y1)
        pdf.cell(4, 3, "NA", align="L")

def draw_orange_lollipop(pdf,x1, y1, district_2019, state_2019):
    if district_2019 != '':
        x2 = x1+(0.5*float(district_2019))
        # Draw green line
        pdf.set_draw_color(231, 121, 37)
        pdf.set_line_width(0.75)
        pdf.line(x1, y1, x2, y1)
        # Place green circle image
        pdf.image("./resources/orange_circle.png", x=x2-1, y=y1-1.5, w=3)
        # Draw state mark in grey
        x3 = x1+(0.5*float(state_2019))
        pdf.set_draw_color(109, 111, 113)
        pdf.set_line_width(0.75)
        pdf.line(x3, y1-1.5, x3, y1+1.5)
        # Write the district value of 2019
        pdf.set_font('Roboto-Regular', '', 8)
        pdf.set_text_color(231, 121, 37)
        percent_text_pos = x2 + 3
        pdf.set_xy(percent_text_pos, y1-1.5)
        pdf.cell(4, 3, str(round(float(district_2019)))+"%", align="L")
    else:
        # Print NA
        pdf.set_font('Roboto-Regular', '', 8)
        pdf.set_text_color(231, 121, 37)
        pdf.set_xy(x1, y1)
        pdf.cell(4, 3, "NA", align="L")

def put_legends(pdf, state_name, put_state_name, y):
    if put_state_name == 1:
        # Write state's Name
        state_len = len(state_name)
        x = WIDTH - 7 - state_len
        pdf.set_font('Roboto-Bold', 'B', 8)
        pdf.set_text_color(0, 0, 0)
        pdf.set_xy(x-5, y-1.5)
        pdf.cell(state_len+5, 4, state_name, align="R")
        # Put vertical grey line
        x1 = WIDTH - 10 - state_len*1.5
        pdf.set_draw_color(109, 111, 113)
        pdf.set_line_width(0.75)
        pdf.line(x1, y-1.5, x1, y+1.5)

    #Put 2016 and 2019 legends
    # Write 2016
    pdf.image("./resources/green_circle.png", x=WIDTH-18, y=y+5, w=8)
    pdf.set_font('Roboto-Bold', 'B', 8)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(WIDTH-16, y+7)
    pdf.cell(4, 4, "2016", align="C")
    # Write 2019
    pdf.image("./resources/orange_circle.png", x=WIDTH-18, y=y+15, w=8)
    pdf.set_font('Roboto-Bold', 'B', 8)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(WIDTH-16, y+17)
    pdf.cell(4, 4, "2019", align="C")

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
    pdf.cell(186, 10, orangeBanner_text, align='L')
    pdf.cell(10, 10, 'MARCH 2022', align='R')

    # About DNPs: Title
    pdf.set_font('Roboto-Bold', 'B', 13)
    pdf.set_text_color(231, 121, 37)
    pdf.set_xy(7, 54)
    aboutDNP_text = "About District Nutrition Profiles:"
    pdf.cell(100, 10, aboutDNP_text, align='L')
    # About DNPs: Description text
    pdf.set_font('Roboto-Regular', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(7, 63)
    DNPdesc_text = "District Nutrition Profiles (DNPs) are available for 707 districts in India. They present trends for key nutrition and health outcomes and their cross-sectoral determinants in a district. The DNPs are based on data from the National Family Health Survey (NFHS)-4 (2015-2016) and NFHS-5 (2019-2020). They are aimed primarily at district administrators, state functionaries, local leaders, and development actors working at the district-level."
    pdf.multi_cell(115, 4.5, DNPdesc_text, align='J')

    # Add district map
    map_path = './data/maps/comparable_maps/{}.jpg'.format(district[4])
    pdf.image(map_path, x=125, y=53, w=75, h=40)
    # map caption
    figure1_text = "Figure 1:"
    mapCaption_text = "Map highlights district {} in the state/UT of {}".format(district[3], district[1])
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Roboto-Bold', 'B', 7)
    pdf.set_xy(125, 92)
    pdf.cell(9, 7, figure1_text, align='L')
    pdf.set_xy(125+9+1.5, 92)
    pdf.set_font('Roboto-Regular', '', 7)
    pdf.cell(60, 7, mapCaption_text[0:55]+'-', align='L')
    pdf.set_xy(125, 95)
    pdf.cell(70, 7, mapCaption_text[55:], align='L')

    # Add framework as image
    pdf.image("./resources/framework.png", x=8, y=105, w=90)
    # Add framework caption
    source_text = "Source:"
    frameworkCaption_text = "Adapted from Black et al. (2008)"
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Roboto-Bold', 'B', 7)
    pdf.set_xy(8, 170)
    pdf.cell(7, 7, source_text, align='L')
    pdf.set_xy(8+7+2, 170)
    pdf.set_font('Roboto-Regular', '', 7)
    pdf.cell(60, 7, frameworkCaption_text, align='L')

    # Factors for child undernutrition: Title
    pdf.set_font('Roboto-Bold', 'B', 13)
    pdf.set_text_color(231, 121, 37)
    pdf.set_xy(100, 100)
    undernutrition_text = "What factors lead to child undernutrition?"
    pdf.cell(100, 10, undernutrition_text, align='L')
    # Child undernutrition: Description text
    pdf.set_font('Roboto-Regular', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(100, 110)
    undernutritionDesc_text = "Given the focus of India’s national nutrition mission on child undernutrition , the DNPs focus in on the determinants of child undernutrition (Figure on the left). Multiple determinants of suboptimal child nutrition and development contribute to the outcomes seen at the district-level. Different types of interventions can influence these determinants. Immediate determinants include inadequacies in food, health, and care for infants and young children, especially in the first two years of life. Nutrition-specific interventions such as health service delivery at the right time during pregnancy and early childhood can affect immediate determinants. Underlying and basic determinants include women’s status, household food security, hygiene, and socio-economic conditions. Nutrition-sensitive interventions such as social safety nets, sanitation programs, women’s empowerment, and agriculture programs can affect underlying and basic determinants."
    pdf.multi_cell(102, 4.5, undernutritionDesc_text, align='J')

    # Add grey rectangle
    pdf.set_draw_color(109, 111, 113)
    pdf.set_fill_color(109, 111, 113)
    pdf.rect(x=7, y=183, w=WIDTH-14, h=10, style='F')
    # Add text into the grey bar
    greyBar_text = "District demographic profile, 2019-20"
    pdf.set_font('Roboto-Bold', 'B', 13)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(10, 183)
    pdf.cell(100, 10, greyBar_text, align='L')
    pdf.set_font('Roboto-Bold', 'B', 12)
    pdf.cell(90, 10, district[3], align='R')

    # State nutrition profiles
    pdf.image("./resources/state_nut_prof.png", x=7, y=194, w=WIDTH-14)
    # Sex ratio number
    pdf.set_font('Roboto-Bold', 'B', 28)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(20, 193)
    if district[5] != '':
        pdf.cell(40, 20, str("{:,}".format(round(float(district[5]))))+"/1,000", align='L')
    else:
        pdf.cell(40, 20, "NA", 0, 0, 'L')
    # Sex ratio text
    sexRatio_text1 = "Sex ratio (females per 1,000"
    sexRatio_text2 = "males) of the total population"
    pdf.set_font('Roboto-Bold', 'B', 10)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(20, 206)
    pdf.cell(55, 10, sexRatio_text1, align='L')
    pdf.set_xy(20, 210)
    pdf.cell(55, 10, sexRatio_text2, align='L')
    # Reproductive age number
    pdf.set_font('Roboto-Bold', 'B', 28)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(85, 193)
    if district[6] != '':
        pdf.cell(40, 20, str("{:,}".format(round(float(district[6])))), align='L')
    else:
        pdf.cell(40, 20, "NA", 0, 0, 'L')
    # Reproductive age text
    reproductive_text1 = "Number of women of"
    reproductive_text2 = "reproductive age (15–49 yrs)"
    pdf.set_font('Roboto-Bold', 'B', 10)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(85, 206)
    pdf.cell(55, 10, reproductive_text1, align='L')
    pdf.set_xy(85, 210)
    pdf.cell(55, 10, reproductive_text2, align='L')
    # Pregnant women number
    pdf.set_font('Roboto-Bold', 'B', 28)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(152, 193)
    if district[7] != '':
        pdf.cell(40, 20, str("{:,}".format(round(float(district[7])))), align='L')
    else:
        pdf.cell(40, 20, "NA", 0, 0, 'L')
    # Pregnant women text
    pregnantWomen_text1 = "Number of"
    pregnantWomen_text2 = "pregnant women"
    pdf.set_font('Roboto-Bold', 'B', 10)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(152, 206)
    pdf.cell(55, 10, pregnantWomen_text1, align='L')
    pdf.set_xy(152, 210)
    pdf.cell(55, 10, pregnantWomen_text2, align='L')
    # Live birth number
    pdf.set_font('Roboto-Bold', 'B', 28)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(20, 220)
    if district[8] != '':
        pdf.cell(40, 20, str("{:,}".format(round(float(district[8])))), align='L')
    else:
        pdf.cell(40, 20, "NA", 0, 0, 'L')
    # Live birth text
    liveBirth_text1 = "Number of live births"
    pdf.set_font('Roboto-Bold', 'B', 10)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(20, 233)
    pdf.cell(55, 10, liveBirth_text1, align='L')
    # Total children number
    pdf.set_font('Roboto-Bold', 'B', 28)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(85, 220)
    if district[9] != '':
        pdf.cell(40, 20, str("{:,}".format(round(float(district[9])))), align='L')
    else:
        pdf.cell(40, 20, "NA", 0, 0, 'L')
    # Total children text
    totalChildren_text1 = "Total number of children"
    totalChildren_text2 = "under 5 yrs"
    pdf.set_font('Roboto-Bold', 'B', 10)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(85, 233)
    pdf.cell(55, 10, totalChildren_text1, align='L')
    pdf.set_xy(85, 237)
    pdf.cell(55, 10, totalChildren_text2, align='L')
    # Births registered number
    pdf.set_font('Roboto-Bold', 'B', 28)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(152, 220)
    if district[10] != '':
        pdf.cell(40, 20, str("{:,}".format(round(float(district[10])))), align='L')
    else:
        pdf.cell(40, 20, "NA", 0, 0, 'L')
    # Births registered text
    birthsRegistered_text1 = "Number of"
    birthsRegistered_text2 = "pregnant women"
    pdf.set_font('Roboto-Bold', 'B', 10)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(152, 233)
    pdf.cell(55, 10, birthsRegistered_text1, align='L')
    pdf.set_xy(152, 237)
    pdf.cell(55, 10, birthsRegistered_text2, align='L')

    # source
    pdf.set_font('Roboto-Bold', 'B', 7)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(8, 248)
    pdf.cell(50, 3, "Source:", align='L')
    source1_text = "1. IFPRI estimates - The headcount was calculated as the product of the undernutrition prevalence and the total eligible projected population for each district in 2019. Projected population for 2019 was estimated using Census 2011."
    pdf.set_font('Roboto-Regular', '', 7)
    pdf.set_xy(8, 251)
    pdf.cell(180, 3, source1_text[0:178], align='L')
    pdf.set_xy(10.5, 254)
    pdf.cell(180, 3, source1_text[179:], align='L')
    source2_text = "2. NFHS-4 (2015-16) & NFHS-5 district & state factsheets (2019-20)."
    pdf.set_xy(8, 257)
    pdf.cell(200, 3, source2_text, align='L')

    # Horizontal line
    pdf.set_draw_color(109, 111, 113)
    pdf.set_line_width(0.75)
    pdf.line(0,261, WIDTH, 261)

    # citation
    citation_text = "Citation:"
    citation_text1 = "Singh. N., P.H. Nguyen, M. Jangid, S.K. Singh, R. Sarwal, N. Bhatia, R. Johnston, W. Joe, and P. Menon. 2022. District Nutrition Profile: {}, {}. New Delhi, India: International Food Policy Research Institute.".format(district[3], district[1])
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Roboto-Bold', 'B', 7)
    pdf.set_xy(8, 263)
    pdf.cell(9, 3, citation_text, align='L')
    pdf.set_xy(8+9+1, 263)
    pdf.set_font('Roboto-Regular', '', 7)
    pdf.cell(170, 3, citation_text1[0:167]+'-', align='L')
    pdf.set_xy(8, 266)
    pdf.cell(170, 3, citation_text1[167:], align='L')

    # Acknowledgement
    acknowledgement_text = "Acknowledgement:"
    acknowledgement_text1 = "Financial support was provided by the Bill & Melinda Gates Foundation through POSHAN, led by the International Food Policy Research Institute. We thank Amit Jena (Independent Researcher) for design and programming support."
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Roboto-Bold', 'B', 7)
    pdf.set_xy(8, 270)
    pdf.cell(9, 3, acknowledgement_text, align='L')
    pdf.set_xy(8+21+0.5, 270)
    pdf.set_font('Roboto-Regular', '', 7)
    pdf.cell(155, 3, acknowledgement_text1[0:152], align='L')
    pdf.set_xy(8, 273)
    pdf.cell(155, 3, acknowledgement_text1[152:], align='L')

    # Logos
    img_width = 120
    pdf.image("./resources/logos.png", x=(WIDTH-img_width)/2+1, y=277, w=img_width)

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
    pdf.cell(100, 10, top_Bar2_text, align='L')
    pdf.set_font('Roboto-Bold', 'B', 12)
    pdf.cell(90, 10, district[3], align='R')

    # Put Top legends
    put_legends(pdf, district[1], 1, 20)

    # Put the burden details
    # Background box image
    pdf.image("./resources/burden_top2.png", x=WIDTH-85, y=60, w=77)
    # Burden text: Title
    burden_title_top = "Burden on nutrition outcomes (2020)"
    pdf.set_font('Roboto-Regular', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(WIDTH-86, 51)
    pdf.cell(80, 10, burden_title_top, align='C')
    # Burden text: Table header
    pdf.set_font('Roboto-Bold', 'B', 8)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(WIDTH-86.5, 57.5)
    pdf.cell(40, 10, "Indicators", align='C')
    pdf.cell(40, 10, "No. of children (<5 yrs)", align='C')
    # Burden text: Table rows
    pdf.set_font('Roboto-Regular', '', 8)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(WIDTH-84, 63.5)
    pdf.cell(40, 10, "Low-birth weight", align='L')
    pdf.cell(40, 10, "NA", align='L')
    pdf.set_xy(WIDTH-84, 69.5)
    pdf.cell(40, 10, "Stunted", align='L')
    pdf.cell(40, 10, round_str(district[13]), align='L')
    pdf.set_xy(WIDTH-84, 75)
    pdf.cell(40, 10, "Wasted", align='L')
    pdf.cell(40, 10, round_str(district[16]), align='L')
    pdf.set_xy(WIDTH-84, 81)
    pdf.cell(40, 10, "Severely wasted", align='L')
    pdf.cell(40, 10, round_str(district[19]), align='L')
    pdf.set_xy(WIDTH-84, 86.5)
    pdf.cell(40, 10, "Underweight", align='L')
    pdf.cell(40, 10, round_str(district[22]), align='L')
    pdf.set_xy(WIDTH-84, 92.5)
    pdf.cell(40, 10, "Overweight/obesity", align='L')
    pdf.cell(40, 10, round_str(district[25]), align='L')
    pdf.set_xy(WIDTH-84, 98.5)
    pdf.cell(40, 10, "Anemia", align='L')
    pdf.cell(40, 10, round_str(district[28]), align='L')
    pdf.set_xy(WIDTH-84, 104)
    pdf.set_font('Roboto-Bold', 'B', 8)
    pdf.cell(40, 10, "Total children", align='L')
    pdf.cell(40, 10, round_str(district[29]), align='L')

    # Top section - indicator labels
    ch_lowbirth = "Low-birth weight"
    ch_stunt = "Stunted"
    ch_waste = "Wasted"
    ch_wastesev = "Severely wasted"
    ch_uweight = "Underweight"
    ch_over = "Overweight/obesity"
    ch_anemic = "Anemia"

    # Place indicator labels at Place
    ch_indicator_x = 10
    ch_indicator_y = 18
    ch_cell_width = 50
    ch_lollipop_gap = ch_indicator_x + 53

    # Put the grid lines
    draw_gridlines(pdf, ch_lollipop_gap, 19, 118)

    # Put the list of indicators
    pdf.set_font('Roboto-Regular', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(ch_indicator_x, ch_indicator_y)
    pdf.cell(ch_cell_width, 10, ch_lowbirth, align='R')
    pdf.set_xy(ch_indicator_x, ch_indicator_y+15)
    pdf.cell(ch_cell_width, 10, ch_stunt, align='R')
    pdf.set_xy(ch_indicator_x, ch_indicator_y+30)
    pdf.cell(ch_cell_width, 10, ch_waste, align='R')
    pdf.set_xy(ch_indicator_x, ch_indicator_y+45)
    pdf.cell(ch_cell_width, 10, ch_wastesev, align='R')
    pdf.set_xy(ch_indicator_x, ch_indicator_y+60)
    pdf.cell(ch_cell_width, 10, ch_uweight, align='R')
    pdf.set_xy(ch_indicator_x, ch_indicator_y+75)
    pdf.cell(ch_cell_width, 10, ch_over, align='R')
    pdf.set_xy(ch_indicator_x, ch_indicator_y+90)
    pdf.cell(ch_cell_width, 10, ch_anemic, align='R')

    # Put the lollipops
    # ch_lowbirth = "Low-birth weight"
    draw_green_lollipop(pdf, ch_lollipop_gap, 20, '', '')
    draw_orange_lollipop(pdf, ch_lollipop_gap, 24, '', '')
    # ch_stunt = "Stunted"
    draw_green_lollipop(pdf, ch_lollipop_gap, 36, district[11], state[3])
    draw_orange_lollipop(pdf, ch_lollipop_gap, 40, district[12], state[4])
    # ch_waste = "Wasted"
    draw_green_lollipop(pdf, ch_lollipop_gap, 50, district[14], state[5])
    draw_orange_lollipop(pdf, ch_lollipop_gap, 54, district[15], state[6])
    # ch_wastesev = "Severely wasted"
    draw_green_lollipop(pdf, ch_lollipop_gap, 66, district[17], state[7])
    draw_orange_lollipop(pdf, ch_lollipop_gap, 70, district[18], state[8])
    # ch_uweight = "Underweight"
    draw_green_lollipop(pdf, ch_lollipop_gap, 81, district[20], state[9])
    draw_orange_lollipop(pdf, ch_lollipop_gap, 85, district[21], state[10])
    # ch_over = "Overweight/obesity"
    draw_green_lollipop(pdf, ch_lollipop_gap, 96, district[23], state[11])
    draw_orange_lollipop(pdf, ch_lollipop_gap, 100, district[24], state[12])
    # ch_anemic = "Anemia"
    draw_green_lollipop(pdf, ch_lollipop_gap, 111, district[26], state[13])
    draw_orange_lollipop(pdf, ch_lollipop_gap, 115, district[27], state[14])

    # Note for NA description
    pdf.set_font('Roboto-Bold', 'B', 7)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(125, 126)
    pdf.cell(5, 10, NA_desc_text[0:5], align='L')
    pdf.set_font('Roboto-Regular', '', 7)
    pdf.cell(72.5, 10, NA_desc_text[5:], align='R')

    # Top Points of discussion grey bar
    pdf.set_draw_color(183, 179, 160)
    pdf.set_fill_color(183, 179, 160)
    pdf.rect(x=7, y=134, w=WIDTH-14, h=15, style='F')
    # Bottom Points of discussion: text
    pdf.set_font('Roboto-Bold', 'B', 9)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(10, 135)
    pdf.cell(50, 5, "Points of discussion:", align='L')
    ch_pd1_text2 = "• What are the trends in undernutrition among children under five years of age (stunting, wasting, underweight, and anemia)?"
    ch_pd2_text2 = "• What are the trends in overweight/obesity among children under five years of age in the district?"
    pdf.set_font('Roboto-Regular', '', 9)
    pdf.set_xy(12, 139)
    pdf.cell(180, 5, ch_pd1_text2, align='L')
    pdf.set_xy(12, 143)
    pdf.cell(200, 5, ch_pd2_text2, align='L')

    #

    # Add bottom bar
    pdf.set_draw_color(41, 119, 115)
    pdf.set_fill_color(41, 119, 115)
    pdf.rect(x=7, y=150, w=WIDTH-14, h=10, style='F')
    # Add text into the bottom bar
    bottom_Bar2_text = "The state of nutrition outcomes among women (15-49 years)"
    pdf.set_font('Roboto-Bold', 'B', 13)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(10, 150)
    pdf.cell(100, 10, bottom_Bar2_text, align='L')
    pdf.set_font('Roboto-Bold', 'B', 12)
    pdf.cell(90, 10, district[3], align='R')

    # Put Bottom legends
    put_legends(pdf, district[1], 1, 165)

    # Put the burden details
    # Background box image
    pdf.image("./resources/burden_bottom2.png", x=WIDTH-85, y=198, w=77)
    # Burden text: Title
    burden_title_bottom = "Burden on nutrition outcomes (2020)"
    pdf.set_font('Roboto-Regular', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(WIDTH-86, 189)
    pdf.cell(80, 10, burden_title_bottom, align='C')
    # Burden text: Table header
    pdf.set_font('Roboto-Bold', 'B', 8)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(WIDTH-86.5, 195.5)
    pdf.cell(40, 10, "Indicators", align='C')
    pdf.cell(40, 10, "No. of women (15-49 yrs)", align='C')
    # Burden text: Table rows
    pdf.set_font('Roboto-Regular', '', 8)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(WIDTH-84, 201.5)
    pdf.cell(40, 10, "Underweight", align='L')
    pdf.cell(40, 10, round_str(district[32]), align='L')
    pdf.set_xy(WIDTH-84, 207.5)
    pdf.cell(40, 10, "Overweight/obesity", align='L')
    pdf.cell(40, 10, round_str(district[35]), align='L')
    pdf.set_xy(WIDTH-84, 213)
    pdf.cell(40, 10, "Hypertension", align='L')
    pdf.cell(40, 10, round_str(district[37]), align='L')
    pdf.set_xy(WIDTH-84, 218.5)
    pdf.cell(40, 10, "Diabetes", align='L')
    pdf.cell(40, 10, round_str(district[39]), align='L')
    pdf.set_xy(WIDTH-84, 224.5)
    pdf.cell(40, 10, "Anemia (non-preg)", align='L')
    pdf.cell(40, 10, round_str(district[42]), align='L')
    pdf.set_xy(WIDTH-84, 230.5)
    pdf.cell(40, 10, "Anemia (preg)", align='L')
    pdf.cell(40, 10, round_str(district[45]), align='L')
    pdf.set_xy(WIDTH-84, 236)
    pdf.set_font('Roboto-Bold', 'B', 8)
    pdf.cell(40, 10, "Total women (preg)", align='L')
    pdf.cell(40, 10, round_str(district[46]), align='L')
    pdf.set_xy(WIDTH-84, 242)
    pdf.cell(40, 10, "Total women", align='L')
    pdf.cell(40, 10, round_str(district[47]), align='L')

    # Bottom section - indicator labels
    bmi_f_lowbmiout = "Underweight (BMI <18.5 kg/m²)"
    bmi_f_highbmi = "Overweight/obesity"
    hypertension_women = "Hypertension"
    diabetes_women = "Diabetes"
    hb_f_anemia = "Anemia (non-pregnant)"
    preg_anemia = "Anemia (pregnant)"

    # Place indicator labels at Place
    wo_indicator_x = 10
    wo_indicator_y = 165
    wo_cell_width = 50
    wo_lollipop_gap = wo_indicator_x + 53

    # Put the grid lines
    draw_gridlines(pdf, wo_lollipop_gap, 165, 250)

    # Put the list of indicators
    pdf.set_font('Roboto-Regular', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(wo_indicator_x, wo_indicator_y)
    pdf.cell(wo_cell_width, 10, bmi_f_lowbmiout, align='R')
    pdf.set_xy(wo_indicator_x, wo_indicator_y+15)
    pdf.cell(wo_cell_width, 10, bmi_f_highbmi, align='R')
    pdf.set_xy(wo_indicator_x, wo_indicator_y+30)
    pdf.cell(wo_cell_width, 10, hypertension_women, align='R')
    pdf.set_xy(wo_indicator_x, wo_indicator_y+45)
    pdf.cell(wo_cell_width, 10, diabetes_women, align='R')
    pdf.set_xy(wo_indicator_x, wo_indicator_y+60)
    pdf.cell(wo_cell_width, 10, hb_f_anemia, align='R')
    pdf.set_xy(wo_indicator_x, wo_indicator_y+75)
    pdf.cell(wo_cell_width, 10, preg_anemia, align='R')

    # Put the lollipops
    # bmi_f_lowbmiout = "Underweight (BMI <18.5 kg/m²)"
    draw_green_lollipop(pdf, wo_lollipop_gap, 168, district[30], state[15])
    draw_orange_lollipop(pdf, wo_lollipop_gap, 172, district[31], state[16])
    # bmi_f_highbmi = "Overweight/obesity"
    draw_green_lollipop(pdf, wo_lollipop_gap, 183, district[33], state[17])
    draw_orange_lollipop(pdf, wo_lollipop_gap, 187, district[34], state[18])
    # hypertension_women = "Hypertension"
    draw_green_lollipop(pdf, wo_lollipop_gap, 198, '', '')
    draw_orange_lollipop(pdf, wo_lollipop_gap, 202, district[36], state[19])
    # diabetes_women = "Diabetes"
    draw_green_lollipop(pdf, wo_lollipop_gap, 213, '', '')
    draw_orange_lollipop(pdf, wo_lollipop_gap, 217, district[38], state[20])
    # hb_f_anemia = "Anemia (non-pregnant)"
    draw_green_lollipop(pdf, wo_lollipop_gap, 228, district[40], state[21])
    draw_orange_lollipop(pdf, wo_lollipop_gap, 232, district[41], state[22])
    # preg_anemia = "Anemia (pregnant)"
    draw_green_lollipop(pdf, wo_lollipop_gap, 243, district[43], state[23])
    draw_orange_lollipop(pdf, wo_lollipop_gap, 247, district[44], state[24])

    # Note for NA description
    pdf.set_font('Roboto-Bold', 'B', 7)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(125, 265)
    pdf.cell(5, 10, NA_desc_text[0:5], align='L')
    pdf.set_font('Roboto-Regular', '', 7)
    pdf.cell(72.5, 10, NA_desc_text[5:], align='R')

    # Bottom Points of discussion grey bar
    pdf.set_draw_color(183, 179, 160)
    pdf.set_fill_color(183, 179, 160)
    pdf.rect(x=7, y=273, w=WIDTH-14, h=15, style='F')
    # Bottom Points of discussion: text
    pdf.set_font('Roboto-Bold', 'B', 9)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(10, 274)
    pdf.cell(50, 5, "Points of discussion:", align='L')
    wo_pd1_text2 = "• What are the trends in underweight and anemia among women (15-49 yrs) in the district?"
    wo_pd2_text2 = "• What are the trends in overweight/obesity and other nutrition-related non-communicable diseases in the district?"
    pdf.set_font('Roboto-Regular', '', 9)
    pdf.set_xy(12, 278)
    pdf.cell(170, 5, wo_pd1_text2, align='L')
    pdf.set_xy(12, 282)
    pdf.cell(170, 5, wo_pd2_text2, align='L')

    #Page number-2
    #Left horizontal line
    pdf.set_draw_color(109, 111, 113)
    pdf.set_line_width(0.75)
    pdf.line(0, 292, WIDTH/2-5, 292)
    # Number 2
    pdf.set_font('Roboto-Bold', 'B', 10)
    pdf.set_xy(WIDTH/2-1.5, 290)
    pdf.cell(3, 5, "2", align='C')
    #Right horizontal line
    pdf.set_draw_color(109, 111, 113)
    pdf.set_line_width(0.75)
    pdf.line(WIDTH/2+5, 292, WIDTH, 292)

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
    pdf.cell(100, 10, top_Bar3_text, align='L')
    pdf.set_font('Roboto-Bold', 'B', 12)
    pdf.cell(90, 10, district[3], align='R')

    # Put Top legends
    put_legends(pdf, district[1], 1, 20)

    # Top section - indicator labels
    take100_IFA_preg = "Consumed IFA 100+ days (pregnant women)"
    ifa_180 = "Consumed IFA 180+ days (pregnant women)"
    iycf_earlybf35 = "Early initiation of breastfeeding (children < 3 yr)"
    iycf_exclbf0 = "Exclusive breastfeeding"
    brestfeed12 = "Continued breastfeeding at 2 years"
    n_iycf_introfood = "Timely introduction of complementary foods"
    n_iycf_minaccdiet0 = "Adequate diet (children)"
    ch_dietary = "Dietary diversity (children)"
    ch_meal_freq = "Minimum meal frequency (children)"
    food_623 = "Eggs and/or flesh foods consumption, 6-23 m"
    bev_623 = "Sweet beverage consumption, 6-23 m"
    botfeed_623 = "Bottle feeding of infants, 6-23 m"

    # Place indicator labels at Place
    im_indicator_x = 15
    im_indicator_y = 15
    im_cell_width = 70
    im_lollipop_gap = im_indicator_x + 73

    # Put the grid lines
    draw_gridlines(pdf, im_lollipop_gap, 17, 135)

    # Put the indicators
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Roboto-Regular', '', 10)
    pdf.set_xy(im_indicator_x, im_indicator_y)
    pdf.cell(im_cell_width, 10, take100_IFA_preg, align='R')
    pdf.set_xy(im_indicator_x, im_indicator_y+10)
    pdf.cell(im_cell_width, 10, ifa_180, align='R')
    pdf.set_xy(im_indicator_x, im_indicator_y+20)
    pdf.cell(im_cell_width, 10, iycf_earlybf35, align='R')
    pdf.set_xy(im_indicator_x, im_indicator_y+30)
    pdf.cell(im_cell_width, 10, iycf_exclbf0, align='R')
    pdf.set_xy(im_indicator_x, im_indicator_y+40)
    pdf.cell(im_cell_width, 10, brestfeed12, align='R')
    pdf.set_xy(im_indicator_x, im_indicator_y+50)
    pdf.cell(im_cell_width, 10, n_iycf_introfood, align='R')
    pdf.set_xy(im_indicator_x, im_indicator_y+60)
    pdf.cell(im_cell_width, 10, n_iycf_minaccdiet0, align='R')
    pdf.set_xy(im_indicator_x, im_indicator_y+70)
    pdf.cell(im_cell_width, 10, ch_dietary, align='R')
    pdf.set_xy(im_indicator_x, im_indicator_y+80)
    pdf.cell(im_cell_width, 10, ch_meal_freq, align='R')
    pdf.set_xy(im_indicator_x, im_indicator_y+90)
    pdf.cell(im_cell_width, 10, food_623, align='R')
    pdf.set_xy(im_indicator_x, im_indicator_y+100)
    pdf.cell(im_cell_width, 10, bev_623, align='R')
    pdf.set_xy(im_indicator_x, im_indicator_y+110)
    pdf.cell(im_cell_width, 10, botfeed_623, align='R')
    # Put the lollipops
    # take100_IFA_preg = "Consumed IFA 100+ days (pregnant women)"
    draw_green_lollipop(pdf, im_lollipop_gap, 18, district[48], state[25])
    draw_orange_lollipop(pdf, im_lollipop_gap, 22, district[49], state[26])
    # ifa_180 = "Consumed IFA 180+ days (pregnant women)"
    draw_green_lollipop(pdf, im_lollipop_gap, 28, district[50], state[27])
    draw_orange_lollipop(pdf, im_lollipop_gap, 32, district[51], state[28])
    # iycf_earlybf35 = "Early initiation of breastfeeding (children < 3 yr)"
    draw_green_lollipop(pdf, im_lollipop_gap, 38, district[52], state[29])
    draw_orange_lollipop(pdf, im_lollipop_gap, 42, district[53], state[30])
    # iycf_exclbf0 = "Exclusive breastfeeding"
    draw_green_lollipop(pdf, im_lollipop_gap, 48, district[54], state[31])
    draw_orange_lollipop(pdf, im_lollipop_gap, 52, district[55], state[32])
    # brestfeed12 = "Continued breastfeeding at 2 years"
    draw_green_lollipop(pdf, im_lollipop_gap, 58, '', '')
    draw_orange_lollipop(pdf, im_lollipop_gap, 62, '', '')
    # n_iycf_introfood = "Timely introduction of complementary foods"
    draw_green_lollipop(pdf, im_lollipop_gap, 68, district[56], state[33])
    draw_orange_lollipop(pdf, im_lollipop_gap, 72, district[57], state[34])
    # n_iycf_minaccdiet0 = "Adequate diet (children)"
    draw_green_lollipop(pdf, im_lollipop_gap, 78, district[58], state[35])
    draw_orange_lollipop(pdf, im_lollipop_gap, 82, district[59], state[36])
    # ch_dietary = "Dietary diversity (children)"
    draw_green_lollipop(pdf, im_lollipop_gap, 88, '', '')
    draw_orange_lollipop(pdf, im_lollipop_gap, 92, '', '')
    # ch_meal_freq = "Minimum meal frequency (children)"
    draw_green_lollipop(pdf, im_lollipop_gap, 98, '', '')
    draw_orange_lollipop(pdf, im_lollipop_gap, 102, '', '')
    # food_623 = "Eggs and/or flesh foods consumption, 6-23 m"
    draw_green_lollipop(pdf, im_lollipop_gap, 108, '', '')
    draw_orange_lollipop(pdf, im_lollipop_gap, 112, '', '')
    # bev_623 = "Sweet beverage consumption, 6-23 m"
    draw_green_lollipop(pdf, im_lollipop_gap, 118, '', '')
    draw_orange_lollipop(pdf, im_lollipop_gap, 122, '', '')
    # botfeed_623 = "Bottle feeding of infants, 6-23 m"
    draw_green_lollipop(pdf, im_lollipop_gap, 128, '', '')
    draw_orange_lollipop(pdf, im_lollipop_gap, 132, '', '')

    # Note for NA description
    pdf.set_font('Roboto-Bold', 'B', 7)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(125, 137)
    pdf.cell(5, 10, NA_desc_text[0:5], align='L')
    pdf.set_font('Roboto-Regular', '', 7)
    pdf.cell(72.5, 10, NA_desc_text[5:], align='R')

    # Top Points of discussion grey bar
    pdf.set_draw_color(183, 179, 160)
    pdf.set_fill_color(183, 179, 160)
    pdf.rect(x=7, y=144, w=WIDTH-14, h=21, style='F')
    # Top Points of discussion: text
    pdf.set_font('Roboto-Bold', 'B', 9)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(10, 144)
    pdf.cell(50, 5, "Points of discussion:", align='L')
    im_pd1_text3 = "• What are the trends in infant and young child feeding (timely initiation of breastfeeding, exclusive breastfeeding, timely initiation of complementary feeding, and adequate diet)? What can be done to improve infant and young child feeding?"
    im_pd2_text3 = "• What are the trends in IFA consumption among pregnant women in the district? How can the consumption be improved?"
    im_pd3_text3 = "• What additional data are needed to understand diets and/or other determinants?"
    pdf.set_font('Roboto-Regular', '', 9)
    pdf.set_xy(12, 148)
    pdf.cell(165, 5, im_pd1_text3[0:140], align='L')
    pdf.set_xy(14, 152)
    pdf.cell(165, 5, im_pd1_text3[140:], align='L')
    pdf.set_xy(12, 156)
    pdf.cell(165, 5, im_pd2_text3, align='L')
    pdf.set_xy(12, 160)
    pdf.cell(165, 5, im_pd3_text3, align='L')

    # Add bottom bar
    pdf.set_draw_color(152, 56, 87)
    pdf.set_fill_color(152, 56, 87)
    pdf.rect(x=7, y=166, w=WIDTH-14, h=10, style='F')
    # Add text into the bottom bar
    bottom_Bar3_text = "Underlying determinants"
    pdf.set_font('Roboto-Bold', 'B', 13)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(10, 166)
    pdf.cell(100, 10, bottom_Bar3_text, align='L')
    pdf.set_font('Roboto-Bold', 'B', 12)
    pdf.cell(90, 10, district[3], align='R')

    # Put Bottom legends
    put_legends(pdf, district[1], 1, 181)

    # Bottom section - indicator labels
    school10yr_women = "Women with ≥10 years of education"
    wo2024_mar18 = "Women 20-24 years married before the age of 18"
    wom_pregmothers_1519 = "Women 15-19 years with child or pregnant"
    imp_latrine = "HHs with improved sanitation facility"
    imp_drinkw = "HHs with improved drinking water source"
    dispfeces = "Safe disposal of feces"
    hh_bpl = "HHs with below poverty line (BPL) card"
    hh_healthins = "HHs with health insurance"

    # Place indicator labels at Place
    un_indicator_x = 15
    un_indicator_y = 175
    un_cell_width = 70
    un_lollipop_gap = un_indicator_x + 73
    # Put the grid lines
    draw_gridlines(pdf, un_lollipop_gap, 177, 254)

    # Put the indicators
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Roboto-Regular', '', 10)
    pdf.set_xy(un_indicator_x, un_indicator_y)
    pdf.cell(un_cell_width, 10, school10yr_women, align='R')
    pdf.set_xy(un_indicator_x, un_indicator_y+10)
    pdf.cell(un_cell_width, 10, wo2024_mar18, align='R')
    pdf.set_xy(un_indicator_x, un_indicator_y+20)
    pdf.cell(un_cell_width, 10, wom_pregmothers_1519, align='R')
    pdf.set_xy(un_indicator_x, un_indicator_y+30)
    pdf.cell(un_cell_width, 10, imp_latrine, align='R')
    pdf.set_xy(un_indicator_x, un_indicator_y+40)
    pdf.cell(un_cell_width, 10, imp_drinkw, align='R')
    pdf.set_xy(un_indicator_x, un_indicator_y+50)
    pdf.cell(un_cell_width, 10, dispfeces, align='R')
    pdf.set_xy(un_indicator_x, un_indicator_y+60)
    pdf.cell(un_cell_width, 10, hh_bpl, align='R')
    pdf.set_xy(un_indicator_x, un_indicator_y+70)
    pdf.cell(un_cell_width, 10, hh_healthins, align='R')
    # Put the lollipops
    # school10yr_women = "Women with ≥10 years of education"
    draw_green_lollipop(pdf, im_lollipop_gap, 178, district[60], state[37])
    draw_orange_lollipop(pdf, im_lollipop_gap, 182, district[61], state[38])
    # wo2024_mar18 = "Women 20-24 years married before the age of 18"
    draw_green_lollipop(pdf, im_lollipop_gap, 188, district[62], state[39])
    draw_orange_lollipop(pdf, im_lollipop_gap, 192, district[63], state[40])
    # wom_pregmothers_1519 = "Women 15-19 years with child or pregnant"
    draw_green_lollipop(pdf, im_lollipop_gap, 198, district[64], state[41])
    draw_orange_lollipop(pdf, im_lollipop_gap, 202, district[65], state[42])
    # imp_latrine = "HHs with improved sanitation facility"
    draw_green_lollipop(pdf, im_lollipop_gap, 208, district[66], state[43])
    draw_orange_lollipop(pdf, im_lollipop_gap, 212, district[67], state[44])
    # imp_drinkw = "HHs with improved drinking water source"
    draw_green_lollipop(pdf, im_lollipop_gap, 218, district[68], state[45])
    draw_orange_lollipop(pdf, im_lollipop_gap, 222, district[69], state[46])
    # dispfeces = "Safe disposal of feces"
    draw_green_lollipop(pdf, im_lollipop_gap, 228, '', '')
    draw_orange_lollipop(pdf, im_lollipop_gap, 232, '', '')
    # hh_bpl = "HHs with below poverty line (BPL) card"
    draw_green_lollipop(pdf, im_lollipop_gap, 238, '', '')
    draw_orange_lollipop(pdf, im_lollipop_gap, 242, '', '')
    # hh_healthins = "HHs with health insurance"
    draw_green_lollipop(pdf, im_lollipop_gap, 248, district[70], state[47])
    draw_orange_lollipop(pdf, im_lollipop_gap, 252, district[71], state[48])

    # Note for NA description
    pdf.set_font('Roboto-Bold', 'B', 7)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(125, 255.5)
    pdf.cell(5, 10, NA_desc_text[0:5], align='L')
    pdf.set_font('Roboto-Regular', '', 7)
    pdf.cell(72.5, 10, NA_desc_text[5:], align='R')

    # Bottom Points of discussion grey bar
    pdf.set_draw_color(183, 179, 160)
    pdf.set_fill_color(183, 179, 160)
    pdf.rect(x=7, y=262, w=WIDTH-14, h=26, style='F')
    # Bottom Points of discussion: text
    pdf.set_font('Roboto-Bold', 'B', 9)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(10, 263)
    pdf.cell(50, 5, "Points of discussion:", align='L')
    un_pd1_text3 = "• How can the district increase women’s literacy, and reduce early marriage, if needed?"
    un_pd2_text3 = "• How does the district perform on providing drinking water and sanitation to its residents? Since sanitation and hygiene play an important role in improving nutrition outcomes, how can all aspects of sanitation be improved?"
    un_pd3_text3 = "• How can programs that address underlying and basic determinants (education, poverty, gender) be strengthened?"
    un_pd4_text3 = "• What additional data are needed on food systems, poverty or other underlying determinants?"
    pdf.set_font('Roboto-Regular', '', 9)
    pdf.set_xy(12, 267)
    pdf.cell(170, 5, un_pd1_text3, align='L')
    pdf.set_xy(12, 271)
    pdf.cell(165, 5, un_pd2_text3[0:130], align='L')
    pdf.set_xy(14, 275)
    pdf.cell(165, 5, un_pd2_text3[130:], align='L')
    pdf.set_xy(12, 279)
    pdf.cell(170, 5, un_pd3_text3, align='L')
    pdf.set_xy(12, 283)
    pdf.cell(170, 5, un_pd4_text3, align='L')

    #Page number-3
    #Left horizontal line
    pdf.set_draw_color(109, 111, 113)
    pdf.set_line_width(0.75)
    pdf.line(0, 292, WIDTH/2-5, 292)
    # Number 2
    pdf.set_font('Roboto-Bold', 'B', 10)
    pdf.set_xy(WIDTH/2-1.5, 290)
    pdf.cell(3, 5, "3", align='C')
    #Right horizontal line
    pdf.set_draw_color(109, 111, 113)
    pdf.set_line_width(0.75)
    pdf.line(WIDTH/2+5, 292, WIDTH, 292)

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
    pdf.cell(100, 10, top_Bar4_text, align='L')
    pdf.set_font('Roboto-Bold', 'B', 12)
    pdf.cell(90, 10, district[3], align='R')

    # Add vertical top bar
    pdf.set_draw_color(91, 83, 134)
    pdf.set_fill_color(91, 83, 134)
    pdf.rect(x=7, y=25, w=8, h=84, style='F')
    pdf.image("./resources/vert_bar_first4.png", x=9, y=43, w=4.5)

    # Add vertical middle bar
    pdf.set_draw_color(91, 83, 134)
    pdf.set_fill_color(91, 83, 134)
    pdf.rect(x=7, y=113, w=8, h=54, style='F')
    pdf.image("./resources/vert_bar_second4.png", x=9, y=119, w=4.5)

    # Add vertical bottom bar
    pdf.set_draw_color(91, 83, 134)
    pdf.set_fill_color(91, 83, 134)
    pdf.rect(x=7, y=171, w=8, h=83, style='F')
    pdf.image("./resources/vert_bar_third4.png", x=9, y=197, w=4.5)

    # Put Top legends
    put_legends(pdf, district[1], 0, 15)

    # Top section - indicator labels
    preg_fp_satisfy = "Demand for FP satisfied"
    iod_salt = "Iodized salt"
    mcp_rec = "Pregnancy registered (MPC card)"
    anc_firsttri = "ANC first trimester"
    anc4 = "> 4 ANC visits"
    preg_weighing = "Weighing"
    preg_birth_prep = "Birth preparedness counselling"
    preg_breast_prep = "Breastfeeding counselling"
    protect_tetanus = "Tetanus injection"
    IFA_rec = "Received IFA tab/syrup"
    deworm_preg = "Deworming"
    preg_food = "Food supplementation"

    # Middle section - indicator labels
    inst_birth = "Institutional birth"
    jsy_rec1 = "Financial assistance (JSY)"
    ba_healthpro = "Skilled birth attendant"
    mopostnat_2day_hp = "Postnatal care for mothers"
    chpostnat_2day_hp = "Postnatal care for babies"
    post_food = "Food supplementation"
    post_edu = "Health & nutrition education"
    post_icds = "Health checkup (ICDS)"

    # Bottom section - indicator labels
    full_immun1 = "Full immunization"
    chvitA_6m1 = "Vitamin A"
    child_ifa = "Pediatric IFA"
    child_deworm = "Deworming"
    child_food = "Food supplementation (6-35 months)"
    child_weighing = "Weighing"
    child_growth = "Counselling on child growth"
    ch_ors = "ORS during diarrhea"
    ch_zinc = "Zinc during diarrhea"
    ari_treat = "Careseeking for ARI"
    child_preschool = "Preschool at AWC"
    child_chekcup = "Health checkup from AWC"

    # Place indicator labels at Place
    co_indicator_x = 25
    co_indicator_y = 22
    co_cell_width = 70
    co_lollipop_gap = co_indicator_x + 85
    vert_gap = 7.25
    # Put the grid lines
    # Top grid line x-axis
    x = co_lollipop_gap
    y = co_indicator_y
    pdf.set_draw_color(109, 111, 113)
    pdf.set_line_width(0.5)
    pdf.line(x, y, x+50, y)
    #
    pdf.set_draw_color(109, 111, 113)
    pdf.line(x, y, x, y-1)
    pdf.line(x+10, y, x+10, y-1)
    pdf.line(x+20, y, x+20, y-1)
    pdf.line(x+30, y, x+30, y-1)
    pdf.line(x+40, y, x+40, y-1)
    pdf.line(x+50, y, x+50, y-1)
    #
    pdf.set_font('Roboto-Regular', '', 8)
    pdf.set_text_color(109, 111, 113)
    pdf.set_xy(x-3, y-5)
    pdf.cell(4, 3, "0%", align="L")
    pdf.set_xy(x+10-3, y-5)
    pdf.cell(4, 3, "20%", align="L")
    pdf.set_xy(x+20-3, y-5)
    pdf.cell(4, 3, "40%", align="L")
    pdf.set_xy(x+30-3, y-5)
    pdf.cell(4, 3, "60%", align="L")
    pdf.set_xy(x+40-3, y-5)
    pdf.cell(4, 3, "80%", align="L")
    pdf.set_xy(x+50-3, y-5)
    pdf.cell(4, 3, "100%", align="L")
    # Function call for grid line
    draw_gridlines(pdf, co_lollipop_gap, 23, 256)

    # Put the top indicators
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Roboto-Regular', '', 10)
    pdf.set_xy(co_indicator_x, co_indicator_y)
    pdf.cell(co_cell_width, 10, preg_fp_satisfy, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+1*vert_gap)
    pdf.cell(co_cell_width, 10, iod_salt, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+2*vert_gap)
    pdf.cell(co_cell_width, 10, mcp_rec, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+3*vert_gap)
    pdf.cell(co_cell_width, 10, anc_firsttri, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+4*vert_gap)
    pdf.cell(co_cell_width, 10, anc4, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+5*vert_gap)
    pdf.cell(co_cell_width, 10, preg_weighing, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+6*vert_gap)
    pdf.cell(co_cell_width, 10, preg_birth_prep, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+7*vert_gap)
    pdf.cell(co_cell_width, 10, preg_breast_prep, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+8*vert_gap)
    pdf.cell(co_cell_width, 10, protect_tetanus, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+9*vert_gap)
    pdf.cell(co_cell_width, 10, IFA_rec, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+10*vert_gap)
    pdf.cell(co_cell_width, 10, deworm_preg, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+11*vert_gap)
    pdf.cell(co_cell_width, 10, preg_food, align='R')

    # Put the middle indicators
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Roboto-Regular', '', 10)
    pdf.set_xy(co_indicator_x, co_indicator_y+12*vert_gap)
    pdf.cell(co_cell_width, 10, inst_birth, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+13*vert_gap)
    pdf.cell(co_cell_width, 10, jsy_rec1, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+14*vert_gap)
    pdf.cell(co_cell_width, 10, ba_healthpro, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+15*vert_gap)
    pdf.cell(co_cell_width, 10, mopostnat_2day_hp, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+16*vert_gap)
    pdf.cell(co_cell_width, 10, chpostnat_2day_hp, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+17*vert_gap)
    pdf.cell(co_cell_width, 10, post_food, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+18*vert_gap)
    pdf.cell(co_cell_width, 10, post_edu, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+19*vert_gap)
    pdf.cell(co_cell_width, 10, post_icds, align='R')

    # Put the top indicators
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Roboto-Regular', '', 10)
    pdf.set_xy(co_indicator_x, co_indicator_y+20*vert_gap)
    pdf.cell(co_cell_width, 10, full_immun1, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+21*vert_gap)
    pdf.cell(co_cell_width, 10, chvitA_6m1, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+22*vert_gap)
    pdf.cell(co_cell_width, 10, child_ifa, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+23*vert_gap)
    pdf.cell(co_cell_width, 10, child_deworm, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+24*vert_gap)
    pdf.cell(co_cell_width, 10, child_food, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+25*vert_gap)
    pdf.cell(co_cell_width, 10, child_weighing, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+26*vert_gap)
    pdf.cell(co_cell_width, 10, child_growth, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+27*vert_gap)
    pdf.cell(co_cell_width, 10, ch_ors, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+28*vert_gap)
    pdf.cell(co_cell_width, 10, ch_zinc, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+29*vert_gap)
    pdf.cell(co_cell_width, 10, ari_treat, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+30*vert_gap)
    pdf.cell(co_cell_width, 10, child_preschool, align='R')
    pdf.set_xy(co_indicator_x, co_indicator_y+31*vert_gap)
    pdf.cell(co_cell_width, 10, child_chekcup, align='R')

    # Top section
    #preg_fp_satisfy = "Demand for FP satisfied"
    draw_dual_lollipop(pdf, co_lollipop_gap, 27, '', '')
    # iod_salt = "Iodized salt"
    draw_dual_lollipop(pdf, co_lollipop_gap, 34, district[72], district[73])
    # mcp_rec = "Pregnancy registered (MPC card)"
    draw_dual_lollipop(pdf, co_lollipop_gap, 42, district[74], district[75])
    # anc_firsttri = "ANC first trimester"
    draw_dual_lollipop(pdf, co_lollipop_gap, 49, district[76], district[77])
    # anc4 = "> 4 ANC visits"
    draw_dual_lollipop(pdf, co_lollipop_gap, 56, district[78], district[79])
    # preg_weighing = "Weighing"
    draw_dual_lollipop(pdf, co_lollipop_gap, 63, '', '')
    # preg_birth_prep = "Birth preparedness counselling"
    draw_dual_lollipop(pdf, co_lollipop_gap, 71, '', '')
    # preg_breast_prep = "Breastfeeding counselling"
    draw_dual_lollipop(pdf, co_lollipop_gap, 78, '', '')
    # protect_tetanus = "Tetanus injection"
    draw_dual_lollipop(pdf, co_lollipop_gap, 85, district[80], district[81])
    # # IFA_rec = "Received IFA tab/syrup"
    draw_dual_lollipop(pdf, co_lollipop_gap, 92, '', district[82])
    # # deworm_preg = "Deworming"
    draw_dual_lollipop(pdf, co_lollipop_gap, 99.5, '', district[83])
    # # preg_food = "Food supplementation"
    draw_dual_lollipop(pdf, co_lollipop_gap, 107, '', '')

    # Middle section
    # inst_birth = "Institutional birth"
    draw_dual_lollipop(pdf, co_lollipop_gap, 114, district[84], district[85])
    # jsy_rec1 = "Financial assistance (JSY)"
    draw_dual_lollipop(pdf, co_lollipop_gap, 121, '', district[86])
    # ba_healthpro = "Skilled birth attendant"
    draw_dual_lollipop(pdf, co_lollipop_gap, 128.5, district[87], district[88])
    # mopostnat_2day_hp = "Postnatal care for mothers"
    draw_dual_lollipop(pdf, co_lollipop_gap, 136, district[89], district[90])
    # chpostnat_2day_hp = "Postnatal care for babies"
    draw_dual_lollipop(pdf, co_lollipop_gap, 143, '', district[91])
    # post_food = "Food supplementation"
    draw_dual_lollipop(pdf, co_lollipop_gap, 150.5, '', '')
    # post_edu = "Health & nutrition education"
    draw_dual_lollipop(pdf, co_lollipop_gap, 157, '', '')
    # post_icds = "Health checkup (ICDS)"
    draw_dual_lollipop(pdf, co_lollipop_gap, 165, '', '')

    # Bottom section
    # full_immun1 = "Full immunization"
    draw_dual_lollipop(pdf, co_lollipop_gap, 172, district[92], district[93])
    # chvitA_6m1 = "Vitamin A"
    draw_dual_lollipop(pdf, co_lollipop_gap, 179, district[94], district[95])
    # child_ifa = "Pediatric IFA"
    draw_dual_lollipop(pdf, co_lollipop_gap, 187, '', '')
    # child_deworm = "Deworming"
    draw_dual_lollipop(pdf, co_lollipop_gap, 194, '', '')
    # child_food = "Food supplementation (6-35 months)"
    draw_dual_lollipop(pdf, co_lollipop_gap, 201, '', '')
    # child_weighing = "Weighing"
    draw_dual_lollipop(pdf, co_lollipop_gap, 208, '', '')
    # child_growth = "Counselling on child growth"
    draw_dual_lollipop(pdf, co_lollipop_gap, 215.5, '', '')
    # ch_ors = "ORS during diarrhea"
    draw_dual_lollipop(pdf, co_lollipop_gap, 223, district[96], district[97])
    # ch_zinc = "Zinc during diarrhea"
    draw_dual_lollipop(pdf, co_lollipop_gap, 230.5, district[98], district[99])
    # ari_treat = "Careseeking for ARI"
    draw_dual_lollipop(pdf, co_lollipop_gap, 237, district[100], district[101])
    # child_preschool = "Preschool at AWC"
    draw_dual_lollipop(pdf, co_lollipop_gap, 245, '', '')
    # child_chekcup = "Health checkup from AWC"
    draw_dual_lollipop(pdf, co_lollipop_gap, 252, '', '')

    # Note for NA description
    pdf.set_font('Roboto-Bold', 'B', 7)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(125, 259)
    pdf.cell(5, 10, NA_desc_text[0:5], align='L')
    pdf.set_font('Roboto-Regular', '', 7)
    pdf.cell(72.5, 10, NA_desc_text[5:], align='R')

    # Bottom Points of discussion grey bar
    pdf.set_draw_color(183, 179, 160)
    pdf.set_fill_color(183, 179, 160)
    pdf.rect(x=7, y=266, w=WIDTH-14, h=22, style='F')
    # Bottom Points of discussion: text
    pdf.set_font('Roboto-Bold', 'B', 9)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(10, 267)
    pdf.cell(50, 5, "Points of discussion:", align='L')
    co_pd1_text4 = "• How does the district perform on health and nutrition interventions along the continuum of care? Does it adequately provide both prenatal and postnatal services to women of reproductive age, pregnant women, new mothers and newborns?"
    co_pd2_text4 = "• How has access to health and ICDS services changed over time (food supplementation, health and nutrition education and health checkups)?"
    pdf.set_font('Roboto-Regular', '', 9)
    pdf.set_xy(12, 271)
    pdf.cell(165, 5, co_pd1_text4[0:130], align='L')
    pdf.set_xy(13, 275)
    pdf.cell(165, 5, co_pd1_text4[130:], align='L')
    pdf.set_xy(12, 279)
    pdf.cell(165, 5, co_pd2_text4[0:127], align='L')
    pdf.set_xy(13, 283)
    pdf.cell(165, 5, co_pd2_text4[127:], align='L')

    #Page number-4
    #Left horizontal line
    pdf.set_draw_color(109, 111, 113)
    pdf.set_line_width(0.75)
    pdf.line(0, 292, WIDTH/2-5, 292)
    # Number 2
    pdf.set_font('Roboto-Bold', 'B', 10)
    pdf.set_xy(WIDTH/2-1.5, 290)
    pdf.cell(3, 5, "4", align='C')
    #Right horizontal line
    pdf.set_draw_color(109, 111, 113)
    pdf.set_line_width(0.75)
    pdf.line(WIDTH/2+5, 292, WIDTH, 292)

def create_report(filename):
    pdf = FPDF('P', 'mm', 'A4')

    # Setting auto page break to false (to make bottom margin 0)
    pdf.set_auto_page_break(auto=False)

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
    # pdf.add_page()
    # create_second_page(pdf)

    # Third Page
    # pdf.add_page()
    # create_third_page(pdf)

    # Fourth Page
    # pdf.add_page()
    # create_fourth_page(pdf)

    #create a sub-folder
    path = 'generated_dnp/non_comparable_dnp_english'
    dirName = path + '/{}'.format(district[1])
    if not os.path.exists(dirName):
        os.mkdir(dirName)
    pdf.output(dirName+'/'+filename, "F")

    # Success message
    print(district[3] + " of " + district[1] + " generated.")

#Read CSV file
with open("./data/csv/comparable_district_data_temp.csv", 'r') as infile:
    district_reader = csv.reader(infile, delimiter=",")
    district_header = next(district_reader)
    for district in district_reader:
        # Read State level data
        with open("./data/csv/comparable_state_data_temp.csv", 'r') as infile:
            state_reader = csv.reader(infile, delimiter=",")
            state_header = next(state_reader)
            for state in state_reader:
                if district[2] == state[2]:
                    #Generated DNP file name
                    filename="{}-{}.pdf".format(district[3], district[1])
                    create_report(filename)
