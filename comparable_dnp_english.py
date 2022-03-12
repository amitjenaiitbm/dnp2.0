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

    # Top section - indicator labels
    ch_lowbirth = "Low-birth weight"
    ch_stunt = "Stunted"
    ch_waste = "Wasted"
    ch_wastesev = "Severely wasted"
    ch_uweight = "Underweight"
    ch_over = "Overweight/obesity"
    ch_anemic = "Anemia"

    # Place indicator labels at Place
    pdf.set_font('Roboto-Regular', '', 10)
    pdf.set_text_color(0, 0, 0)
    ch_indicator_x = 10
    ch_indicator_y = 15
    ch_cell_width = 50
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

    # Top Points of discussion grey bar
    pdf.set_draw_color(183, 179, 160)
    pdf.set_fill_color(183, 179, 160)
    pdf.rect(x=7, y=121, w=WIDTH-14, h=15, style='F')
    # Bottom Points of discussion: text
    pdf.set_font('Roboto-Bold', 'B', 9)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(10, 122)
    pdf.cell(50, 5, "Points of discussion:", align='L')
    ch_pd1_text2 = "• What are the trends in undernutrition among children under five years of age (stunting, wasting, underweight, and anemia)?"
    ch_pd2_text2 = "• What are the trends in overweight/obesity among children under five years of age in the district?"
    pdf.set_font('Roboto-Regular', '', 9)
    pdf.set_xy(12, 126)
    pdf.cell(180, 5, ch_pd1_text2, align='L')
    pdf.set_xy(12, 130)
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

    # Bottom section - indicator labels
    bmi_f_lowbmiout = "Underweight (BMI <18.5 kg/m²)"
    bmi_f_highbmi = "Overweight/obesity"
    hypertension_women = "Hypertension"
    diabetes_women = "Diabetes"
    hb_f_anemia = "Anemia (non-pregnant)"
    preg_anemia = "Anemia (pregnant)"

    # Place indicator labels at Place
    pdf.set_font('Roboto-Regular', '', 10)
    pdf.set_text_color(0, 0, 0)
    wo_indicator_x = 10
    wo_indicator_y = 155
    wo_cell_width = 50
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
    pdf.set_font('Roboto-Regular', '', 10)
    pdf.set_text_color(0, 0, 0)
    im_indicator_x = 15
    im_indicator_y = 15
    im_cell_width = 70
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

    # Top Points of discussion grey bar
    pdf.set_draw_color(183, 179, 160)
    pdf.set_fill_color(183, 179, 160)
    pdf.rect(x=7, y=141, w=WIDTH-14, h=21, style='F')
    # Top Points of discussion: text
    pdf.set_font('Roboto-Bold', 'B', 9)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(10, 141)
    pdf.cell(50, 5, "Points of discussion:", align='L')
    im_pd1_text3 = "• What are the trends in infant and young child feeding (timely initiation of breastfeeding, exclusive breastfeeding, timely initiation of complementary feeding, and adequate diet)? What can be done to improve infant and young child feeding?"
    im_pd2_text3 = "• What are the trends in IFA consumption among pregnant women in the district? How can the consumption be improved?"
    im_pd3_text3 = "• What additional data are needed to understand diets and/or other determinants?"
    pdf.set_font('Roboto-Regular', '', 9)
    pdf.set_xy(12, 145)
    pdf.cell(165, 5, im_pd1_text3[0:140], align='L')
    pdf.set_xy(14, 149)
    pdf.cell(165, 5, im_pd1_text3[140:], align='L')
    pdf.set_xy(12, 153)
    pdf.cell(165, 5, im_pd2_text3, align='L')
    pdf.set_xy(12, 157)
    pdf.cell(165, 5, im_pd3_text3, align='L')

    # Add bottom bar
    pdf.set_draw_color(152, 56, 87)
    pdf.set_fill_color(152, 56, 87)
    pdf.rect(x=7, y=170, w=WIDTH-14, h=10, style='F')
    # Add text into the bottom bar
    bottom_Bar3_text = "Underlying determinants"
    pdf.set_font('Roboto-Bold', 'B', 13)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(10, 170)
    pdf.cell(100, 10, bottom_Bar3_text, align='L')
    pdf.set_font('Roboto-Bold', 'B', 12)
    pdf.cell(90, 10, district[3], align='R')

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
    pdf.set_font('Roboto-Regular', '', 10)
    pdf.set_text_color(0, 0, 0)
    un_indicator_x = 15
    un_indicator_y = 180
    un_cell_width = 70
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

    # Success message
    print(district[3] + " of " + district[1] + " generated.")

#Read CSV file
with open("./data/csv/comparable_district_data_temp.csv", 'r') as infile:
    reader = csv.reader(infile, delimiter=",")
    header = next(reader)
    for district in reader:
        #Generated DNP file name
        filename="{}-{}.pdf".format(district[3], district[1])
        create_report(filename)
