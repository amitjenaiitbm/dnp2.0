import csv
import os
#@AC import math
import math

#Python libraries
from fpdf import FPDF

WIDTH = 210
HEIGHT = 297

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
            #@AC function for decimals
            whole_value = math.floor(float(district_2016))
            dec_value = float(district_2016) - whole_value
            if dec_value == 0.5 :
                pdf.cell(4, 3, str(math.ceil(float(district_2016)))+"%", align="R")
            else:
                pdf.cell(4, 3, str(round(float(district_2016)))+"%", align="R")
        elif float(district_2016) > float(district_2019):
            percent_text_pos = x2 + 2
            pdf.set_xy(percent_text_pos, y1-1.5)
            #@AC function for decimals
            whole_value = math.floor(float(district_2016))
            dec_value = float(district_2016) - whole_value
            if dec_value == 0.5 :
                pdf.cell(4, 3, str(math.ceil(float(district_2016)))+"%", align="L")
            else:
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
            #@AC function for decimals
            whole_value = math.floor(float(district_2019))
            dec_value = float(district_2019) - whole_value
            if dec_value == 0.5 :
                pdf.cell(4, 3, str(math.ceil(float(district_2019)))+"%", align="L")
            else:
                pdf.cell(4, 3, str(round(float(district_2019)))+"%", align="L")
        elif float(district_2019) < float(district_2016):
            percent_text_pos = x2 - 5
            pdf.set_xy(percent_text_pos, y1-1.5)
            #@AC function for decimals
            whole_value = math.floor(float(district_2019))
            dec_value = float(district_2019) - whole_value
            if dec_value == 0.5 :
                pdf.cell(4, 3, str(math.ceil(float(district_2019)))+"%", align="R")
            else:
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
            #@AC change here for arrow direction
            #pdf.line(p, y1, p-k, y1-k)
            #pdf.line(p, y1, p-k, y1+k)
            pdf.line(q, y1, q+k, y1-k)
            pdf.line(q, y1, q+k, y1+k)

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
        if (float(state_2016) - float(district_2016) >= 0) and (float(state_2016) - float(district_2016) <= 14):
            percent_text_pos = x3 + 2
        else:
            percent_text_pos = x2 + 3
        pdf.set_xy(percent_text_pos, y1-1.5)
        #@AC function for decimals
        whole_value = math.floor(float(district_2016))
        dec_value = float(district_2016)  - whole_value
        if dec_value == 0.5 :
            pdf.cell(4, 3, str(math.ceil(float(district_2016)))+"%", align="L")
        else:
            pdf.cell(4, 3, str(round(float(district_2016)))+"%", align="L")
    else:
        # Print NA
        pdf.set_font('Roboto-Regular', '', 8)
        pdf.set_text_color(136, 180, 64)
        pdf.set_xy(x1, y1-1)
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
        if (float(state_2019) - float(district_2019) >= 0) and (float(state_2019) - float(district_2019) <= 14):
            percent_text_pos = x3 + 2
        else:
            percent_text_pos = x2 + 3
        pdf.set_xy(percent_text_pos, y1-1.5)
        #@AC function for decimals
        whole_value = math.floor(float(district_2019))
        dec_value = float(district_2019) - whole_value
        if dec_value == 0.5 :
            pdf.cell(4, 3, str(math.ceil(float(district_2019)))+"%", align="L")
        else:
            pdf.cell(4, 3, str(round(float(district_2019)))+"%", align="L")
    else:
        # Print NA
        pdf.set_font('Roboto-Regular', '', 8)
        pdf.set_text_color(231, 121, 37)
        pdf.set_xy(x1, y1-1)
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
    # Write 2020
    pdf.image("./resources/orange_circle.png", x=WIDTH-18, y=y+15, w=8)
    pdf.set_font('Roboto-Bold', 'B', 8)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(WIDTH-16, y+17)
    pdf.cell(4, 4, "2020", align="C")

def create_first_page(pdf):
    #Top banner
    pdf.image("./resources/topBanner-1.png", x=0, y=0, w=WIDTH)

    # Add "District Nutrition Profile" text
    pdf.image("./resources/hindi/hn_1_01.png", x=105, y=8, w=90)

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
    pdf.image("./resources/hindi/hn_1_02.png", x=7, y=54, w=102)

    # Add district map
    map_path = './data/maps/comparable_maps/{}.jpg'.format(district[4])
    pdf.image(map_path, x=120, y=51, w=75, h=40)
    # map caption
    # Line-1
    pdf.image("./resources/hindi/hn_1_03_1.png", x=130, y=91, h=3.5)
    citation_district = "{}".format(district[1])
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Roboto-Regular', '', 7)
    pdf.set_xy(155, 91.25)
    pdf.cell(len(district[1]), 3, citation_district, align='L')
    # Line-2
    pdf.image("./resources/hindi/hn_1_03_2.png", x=130, y=94, h=3)
    citation_state = "{}".format(district[3])
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Roboto-Regular', '', 7)
    pdf.set_xy(139, 94.25)
    pdf.cell(len(district[3]), 3, citation_state, align='L')
    pdf.image("./resources/hindi/hn_1_03_3.png", x=140.5+1.25*len(district[3]), y=94.25, h=3)

    # Add framework as image
    pdf.image("./resources/hindi/framework.png", x=8, y=105, w=90)
    # Add framework caption
    pdf.image("./resources/hindi/hn_1_04.png", x=8, y=172, w=40)

    # Factors for child undernutrition: Title
    pdf.image("./resources/hindi/hn_1_05.png", x=102, y=100, w=100)

    # Add grey rectangle
    pdf.set_draw_color(109, 111, 113)
    pdf.set_fill_color(109, 111, 113)
    pdf.rect(x=7, y=183, w=WIDTH-14, h=10, style='F')
    # Add text into the grey bar
    pdf.image("./resources/hindi/hn_1_06.png", x=10, y=184.5, h=6)
    greyBar_year = "2019"
    pdf.set_font('Roboto-Bold', 'B', 13)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(68, 183)
    pdf.cell(7, 10, greyBar_year, align='L')
    pdf.set_font('Roboto-Bold', 'B', 12)
    pdf.cell(125, 10, district[3], align='R')

    # State nutrition profiles
    pdf.image("./resources/hindi/hn_1_007.png", x=7, y=194, w=WIDTH-14)
    # Sex ratio number
    pdf.set_font('Roboto-Bold', 'B', 27)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(19, 193)
    if district[5] != '':
        pdf.cell(40, 20, str("{:,}".format(round(float(district[5]))))+"/1,000", align='L')
    else:
        pdf.cell(40, 20, "NA", 0, 0, 'L')

    # Reproductive age number
    pdf.set_font('Roboto-Bold', 'B', 27)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(84, 193)
    if district[6] != '':
        pdf.cell(40, 20, str("{:,}".format(round(float(district[6])))), align='L')
    else:
        pdf.cell(40, 20, "NA", 0, 0, 'L')

    # Pregnant women number
    pdf.set_font('Roboto-Bold', 'B', 27)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(151, 193)
    if district[7] != '':
        pdf.cell(40, 20, str("{:,}".format(round(float(district[7])))), align='L')
    else:
        pdf.cell(40, 20, "NA", 0, 0, 'L')

    # Live birth number
    pdf.set_font('Roboto-Bold', 'B', 27)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(19, 220)
    if district[8] != '':
        pdf.cell(40, 20, str("{:,}".format(round(float(district[8])))), align='L')
    else:
        pdf.cell(40, 20, "NA", 0, 0, 'L')

    # Total children number
    pdf.set_font('Roboto-Bold', 'B', 27)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(85, 220)
    if district[10] != '':
        pdf.cell(40, 20, str("{:,}".format(round(float(district[10])))), align='L')
    else:
        pdf.cell(40, 20, "NA", 0, 0, 'L')

    # Births registered number
    pdf.set_font('Roboto-Bold', 'B', 27)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(151, 220)
    if district[9] != '':
        pdf.cell(40, 20, str("{:,}".format(round(float(district[9])))), align='L')
    else:
        pdf.cell(40, 20, "NA", 0, 0, 'L')

    # source
    # pdf.image("./resources/hindi/hn_1_source_1.png", x=10, y=247.5, h=3)
    pdf.image("./resources/hindi/hn_1_source_2.png", x=10.5, y=247.5, h=13.5)
    # Horizontal line
    pdf.set_draw_color(109, 111, 113)
    pdf.set_line_width(0.75)
    pdf.line(0,261, WIDTH, 261)

    # citation line-1
    pdf.image("./resources/hindi/hn_1_citation_1.png", x=10, y=262, h=4)
    citation_district = "{},".format(district[3])
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Roboto-Regular', '', 7)
    pdf.set_xy(169, 262.5)
    pdf.cell(len(district[3]), 3, citation_district, align='L')
    # citation line-2
    citation_state = "{}".format(district[1])
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Roboto-Regular', '', 7)
    pdf.set_xy(9.5, 265.75)
    pdf.cell(len(district[1]), 3, citation_state, align='L')
    # The State name (in English) is NOT a monospaced font. Hence, for each state name, it takes different horizontal size.
    # So, for each state, the offset value has to be adjusted as given below.
    state_code = int(district[2])
    if state_code == 42:
        offset = 9
    if state_code == 9:
        offset = 9.5
    elif state_code == 35 or state_code == 12 or state_code == 10 or state_code == 22 or state_code == 24 or state_code == 32 or state_code == 16:
        offset = 10
    elif state_code == 8 or state_code == 11 or state_code == 5 or state_code == 29:
        offset = 10.5
    elif state_code == 18 or state_code == 30 or state_code == 1 or state_code == 31 or state_code == 23 or state_code == 17 or state_code == 15:
        offset = 12
    else:
        offset = 11

    # print("State - " + district[2] + " & Offset - " + str(offset)) # Error check code
    pdf.image("./resources/hindi/hn_1_citation_2.png", x=offset+1.25*len(district[1]), y=265.5, h=3.5)

    # Acknowledgement
    pdf.image("./resources/hindi/hn_1_ack.png", x=10, y=269, h=7.25)
    acknowledgement_text = "Acknowledgement:"

    # Logos
    img_width = 120
    pdf.image("./resources/logos.png", x=(WIDTH-img_width)/2+1, y=277, w=img_width)

def create_second_page(pdf):
    # Add top bar
    pdf.set_draw_color(41, 119, 115)
    pdf.set_fill_color(41, 119, 115)
    pdf.rect(x=7, y=5, w=WIDTH-14, h=10, style='F')
    # Add text into the top bar
    pdf.image("./resources/hindi/hn_2_01.png", x=10, y=6.5, h=7)
    pdf.set_font('Roboto-Bold', 'B', 12)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(110, 5);
    pdf.cell(90, 10, district[3], align='R')

    # Put Top legends
    put_legends(pdf, district[1], 1, 20)

    # Put the burden details
    # Background box image
    pdf.image("./resources/hindi/hn_2_03.png", x=WIDTH-85, y=60, w=77)
    # Burden text: Table rows
    pdf.set_font('Roboto-Regular', '', 8)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(165, 70)
    if district[13] != '':
        pdf.cell(40, 10, round_str(district[13]), align='L')
    else:
        pdf.cell(40, 10, "NA", align='L')
    pdf.set_xy(165, 76)
    pdf.cell(40, 10, round_str(district[16]), align='L')
    pdf.set_xy(165, 81)
    pdf.cell(40, 10, round_str(district[19]), align='L')
    pdf.set_xy(165, 87)
    pdf.cell(40, 10, round_str(district[22]), align='L')
    pdf.set_xy(165, 92.5)
    pdf.cell(40, 10, round_str(district[25]), align='L')
    pdf.set_xy(165, 98.5)
    pdf.cell(40, 10, round_str(district[28]), align='L')
    pdf.set_xy(165, 104.5)
    pdf.cell(40, 10, round_str(district[31]), align='L')
    pdf.set_xy(165, 110)
    pdf.set_font('Roboto-Bold', 'B', 8)
    pdf.cell(40, 10, round_str(district[32]), align='L')

    # Top section - indicator labels
    ch_lbw = "Low-birth weight"
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
    pdf.image("./resources/hindi/hn_2_02.png", x=17, y=19, h=97)

    # Put the lollipops
    # ch_lbw = "Low-birth weight"
    draw_green_lollipop(pdf, ch_lollipop_gap, 20, district[11], state[3])
    draw_orange_lollipop(pdf, ch_lollipop_gap, 24, district[12], state[4])
    # ch_stunt = "Stunted"
    draw_green_lollipop(pdf, ch_lollipop_gap, 36, district[14], state[5])
    draw_orange_lollipop(pdf, ch_lollipop_gap, 40, district[15], state[6])
    # ch_waste = "Wasted"
    draw_green_lollipop(pdf, ch_lollipop_gap, 50, district[17], state[7])
    draw_orange_lollipop(pdf, ch_lollipop_gap, 54, district[18], state[8])
    # ch_wastesev = "Severely wasted"
    draw_green_lollipop(pdf, ch_lollipop_gap, 66, district[20], state[9])
    draw_orange_lollipop(pdf, ch_lollipop_gap, 70, district[21], state[10])
    # ch_uweight = "Underweight"
    draw_green_lollipop(pdf, ch_lollipop_gap, 81, district[23], state[11])
    draw_orange_lollipop(pdf, ch_lollipop_gap, 85, district[24], state[12])
    # ch_over = "Overweight/obesity"
    draw_green_lollipop(pdf, ch_lollipop_gap, 96, district[26], state[13])
    draw_orange_lollipop(pdf, ch_lollipop_gap, 100, district[27], state[14])
    # ch_anemic = "Anemia"
    draw_green_lollipop(pdf, ch_lollipop_gap, 111, district[29], state[15])
    draw_orange_lollipop(pdf, ch_lollipop_gap, 115, district[30], state[16])

    # Note for NA description
    pdf.image("./resources/hindi/hn_NA.png", x=93, y=129, h=3.5)

    # Top Points of discussion grey bar
    pdf.image("./resources/hindi/hn_2_05.png", x=7, y=133, h=15)

    #

    # Add bottom bar
    pdf.set_draw_color(41, 119, 115)
    pdf.set_fill_color(41, 119, 115)
    pdf.rect(x=7, y=150, w=WIDTH-14, h=10, style='F')
    # Add text into the bottom bar
    pdf.image("./resources/hindi/hn_2_06.png", x=10, y=151, h=7)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(110, 150)
    pdf.set_font('Roboto-Bold', 'B', 12)
    pdf.cell(90, 10, district[3], align='R')

    # Put Bottom legends
    put_legends(pdf, district[1], 1, 165)

    # Put the burden details
    # Background box image
    pdf.image("./resources/hindi/hn_2_08.png", x=WIDTH-85, y=192.75, w=77)

    # Burden text: Table rows
    pdf.set_font('Roboto-Regular', '', 8)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(166, 201.5)
    pdf.cell(40, 10, round_str(district[35]), align='L')
    pdf.set_xy(166, 207)
    pdf.cell(40, 10, round_str(district[38]), align='L')
    pdf.set_xy(166, 213)
    pdf.cell(40, 10, round_str(district[41]), align='L')
    pdf.set_xy(166, 218)
    pdf.cell(40, 10, round_str(district[44]), align='L')
    pdf.set_xy(166, 224)
    pdf.cell(40, 10, round_str(district[47]), align='L')
    pdf.set_xy(166, 230)
    pdf.cell(40, 10, round_str(district[50]), align='L')
    pdf.set_font('Roboto-Bold', 'B', 8)
    pdf.set_xy(166, 236)
    pdf.cell(40, 10, round_str(district[51]), align='L')
    pdf.set_xy(166, 241.5)
    pdf.cell(40, 10, round_str(district[52]), align='L')

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
    pdf.image("./resources/hindi/hn_2_07.png", x=18, y=165.5, h=82)

    # Put the lollipops
    # bmi_f_lowbmiout = "Underweight (BMI <18.5 kg/m²)"
    draw_green_lollipop(pdf, wo_lollipop_gap, 168, district[33], state[17])
    draw_orange_lollipop(pdf, wo_lollipop_gap, 172, district[34], state[18])
    # bmi_f_highbmi = "Overweight/obesity"
    draw_green_lollipop(pdf, wo_lollipop_gap, 183, district[36], state[19])
    draw_orange_lollipop(pdf, wo_lollipop_gap, 187, district[37], state[20])
    # hypertension_women = "Hypertension"
    draw_green_lollipop(pdf, wo_lollipop_gap, 198, district[39], state[21])
    draw_orange_lollipop(pdf, wo_lollipop_gap, 202, district[40], state[22])
    # diabetes_women = "Diabetes"
    draw_green_lollipop(pdf, wo_lollipop_gap, 213, district[42], state[23])
    draw_orange_lollipop(pdf, wo_lollipop_gap, 217, district[43], state[24])
    # hb_f_anemia = "Anemia (non-pregnant)"
    draw_green_lollipop(pdf, wo_lollipop_gap, 228, district[45], state[25])
    draw_orange_lollipop(pdf, wo_lollipop_gap, 232, district[46], state[26])
    # preg_anemia = "Anemia (pregnant)"
    draw_green_lollipop(pdf, wo_lollipop_gap, 243, district[48], state[27])
    draw_orange_lollipop(pdf, wo_lollipop_gap, 247, district[49], state[28])

    # Note for NA description
    pdf.image("./resources/hindi/hn_NA.png", x=93, y=269, h=3.5)

    # Bottom Points of discussion grey bar
    pdf.image("./resources/hindi/hn_2_09.png", x=7, y=273, h=15)

    #Page number-2
    #Left horizontal line
    pdf.set_draw_color(109, 111, 113)
    pdf.set_line_width(0.75)
    pdf.line(0, 292, WIDTH/2-5, 292)
    # Number 2
    pdf.set_font('Roboto-Bold', 'B', 10)
    pdf.set_xy(WIDTH/2-1.5, 290)
    pdf.set_text_color(0, 0, 0)
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
    pdf.image("./resources/hindi/hn_3_01.png", x=10, y=6.5, h=6)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(110, 5)
    pdf.set_font('Roboto-Bold', 'B', 12)
    pdf.cell(90, 10, district[3], align='R')

    # Put Top legends
    put_legends(pdf, district[1], 1, 20)

    # Top section - indicator labels
    take100_IFA_preg = "Consumed IFA 100+ days (pregnant women)"
    ifa_180 = "Consumed IFA 180+ days (pregnant women)"
    iycf_earlybf35 = "Early initiation of breastfeeding (children <3 yrs)"
    iycf_exclbf0 = "Exclusive breastfeeding"
    n_iycf_cbf = "Continued breastfeeding at 2 years"
    n_iycf_introfood = "Timely introduction of complementary foods"
    n_iycf_minaccdiet0 = "Adequate diet (children)"
    n_iycf_mindd = "Dietary diversity (children)"
    n_iycf_minfreq = "Minimum meal frequency (children)"
    n_iycf_eff = "Eggs and/or flesh foods consumption, 6-23 m"
    n_iycf_swbvg = "Sweet beverage consumption, 6-23 m"
    bottle = "Bottle feeding of infants, 6-23 m"

    # Place indicator labels at Place
    im_indicator_x = 15
    im_indicator_y = 15
    im_cell_width = 70
    im_lollipop_gap = im_indicator_x + 73

    # Put the grid lines
    draw_gridlines(pdf, im_lollipop_gap, 17, 135)

    # Put the indicators
    pdf.image("./resources/hindi/hn_3_02.png", x=23, y=18, h=115)

    # Put the lollipops
    # take100_IFA_preg = "Consumed IFA 100+ days (pregnant women)"
    draw_green_lollipop(pdf, im_lollipop_gap, 18, district[53], state[29])
    draw_orange_lollipop(pdf, im_lollipop_gap, 22, district[54], state[30])
    # ifa_180 = "Consumed IFA 180+ days (pregnant women)"
    draw_green_lollipop(pdf, im_lollipop_gap, 28, district[55], state[31])
    draw_orange_lollipop(pdf, im_lollipop_gap, 32, district[56], state[32])
    # iycf_earlybf35 = "Early initiation of breastfeeding (children < 3 yr)"
    draw_green_lollipop(pdf, im_lollipop_gap, 38, district[57], state[33])
    draw_orange_lollipop(pdf, im_lollipop_gap, 42, district[58], state[34])
    # iycf_exclbf0 = "Exclusive breastfeeding"
    draw_green_lollipop(pdf, im_lollipop_gap, 48, district[59], state[35])
    draw_orange_lollipop(pdf, im_lollipop_gap, 52, district[60], state[36])
    # n_iycf_cbf = "Continued breastfeeding at 2 years"
    draw_green_lollipop(pdf, im_lollipop_gap, 58, district[61], state[37])
    draw_orange_lollipop(pdf, im_lollipop_gap, 62, district[62], state[38])
    # n_iycf_introfood = "Timely introduction of complementary foods"
    draw_green_lollipop(pdf, im_lollipop_gap, 68, district[63], state[39])
    draw_orange_lollipop(pdf, im_lollipop_gap, 72, district[64], state[40])
    # n_iycf_minaccdiet0 = "Adequate diet (children)"
    draw_green_lollipop(pdf, im_lollipop_gap, 78, district[65], state[41])
    draw_orange_lollipop(pdf, im_lollipop_gap, 82, district[66], state[42])
    # n_iycf_mindd = "Dietary diversity (children)"
    draw_green_lollipop(pdf, im_lollipop_gap, 88, district[67], state[43])
    draw_orange_lollipop(pdf, im_lollipop_gap, 92, district[68], state[44])
    # n_iycf_minfreq = "Minimum meal frequency (children)"
    draw_green_lollipop(pdf, im_lollipop_gap, 98, district[69], state[45])
    draw_orange_lollipop(pdf, im_lollipop_gap, 102, district[70], state[46])
    # n_iycf_eff = "Eggs and/or flesh foods consumption, 6-23 m"
    draw_green_lollipop(pdf, im_lollipop_gap, 108, district[71], state[47])
    draw_orange_lollipop(pdf, im_lollipop_gap, 112, district[72], state[48])
    # n_iycf_swbvg = "Sweet beverage consumption, 6-23 m"
    draw_green_lollipop(pdf, im_lollipop_gap, 118, district[73], state[49])
    draw_orange_lollipop(pdf, im_lollipop_gap, 122, district[74], state[50])
    # bottle = "Bottle feeding of infants, 6-23 m"
    draw_green_lollipop(pdf, im_lollipop_gap, 128, district[75], state[51])
    draw_orange_lollipop(pdf, im_lollipop_gap, 132, district[76], state[52])

    # Note for NA description
    pdf.image("./resources/hindi/hn_NA.png", x=93, y=140.5, h=3.5)

    # Top Points of discussion grey bar
    pdf.image("./resources/hindi/hn_3_03.png", x=7, y=144, h=21)

    # Add bottom bar
    pdf.set_draw_color(152, 56, 87)
    pdf.set_fill_color(152, 56, 87)
    pdf.rect(x=7, y=166, w=WIDTH-14, h=10, style='F')
    # Add text into the bottom bar
    pdf.image("./resources/hindi/hn_3_04.png", x=10, y=167.5, h=6.5)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(110, 166)
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
    safe_disp = "Safe disposal of feces"
    bpl_card = "HHs with below poverty line (BPL) card"
    hh_healthins = "HHs with health insurance"

    # Place indicator labels at Place
    un_indicator_x = 15
    un_indicator_y = 175
    un_cell_width = 70
    un_lollipop_gap = un_indicator_x + 73
    # Put the grid lines
    draw_gridlines(pdf, un_lollipop_gap, 177, 254)

    # Put the indicators
    pdf.image("./resources/hindi/hn_3_05.png", x=9, y=177.25, h=75)

    # Put the lollipops
    # school10yr_women = "Women with ≥10 years of education"
    draw_green_lollipop(pdf, im_lollipop_gap, 178, district[77], state[53])
    draw_orange_lollipop(pdf, im_lollipop_gap, 182, district[78], state[54])
    # wo2024_mar18 = "Women 20-24 years married before the age of 18"
    draw_green_lollipop(pdf, im_lollipop_gap, 188, district[79], state[55])
    draw_orange_lollipop(pdf, im_lollipop_gap, 192, district[80], state[56])
    # wom_pregmothers_1519 = "Women 15-19 years with child or pregnant"
    draw_green_lollipop(pdf, im_lollipop_gap, 198, district[81], state[57])
    draw_orange_lollipop(pdf, im_lollipop_gap, 202, district[82], state[58])
    # imp_latrine = "HHs with improved sanitation facility"
    draw_green_lollipop(pdf, im_lollipop_gap, 208, district[83], state[59])
    draw_orange_lollipop(pdf, im_lollipop_gap, 212, district[84], state[60])
    # imp_drinkw = "HHs with improved drinking water source"
    draw_green_lollipop(pdf, im_lollipop_gap, 218, district[85], state[61])
    draw_orange_lollipop(pdf, im_lollipop_gap, 222, district[86], state[62])
    # safe_disp = "Safe disposal of feces"
    draw_green_lollipop(pdf, im_lollipop_gap, 228, district[87], state[63])
    draw_orange_lollipop(pdf, im_lollipop_gap, 232, district[88], state[64])
    # bpl_card = "HHs with below poverty line (BPL) card"
    draw_green_lollipop(pdf, im_lollipop_gap, 238, district[89], state[65])
    draw_orange_lollipop(pdf, im_lollipop_gap, 242, district[90], state[66])
    # hh_healthins = "HHs with health insurance"
    draw_green_lollipop(pdf, im_lollipop_gap, 248, district[91], state[67])
    draw_orange_lollipop(pdf, im_lollipop_gap, 252, district[92], state[68])

    # Note for NA description
    pdf.image("./resources/hindi/hn_NA.png", x=93, y=259, h=3.5)

    # Bottom Points of discussion grey bar
    pdf.image("./resources/hindi/hn_3_06.png", x=7, y=262.5, h=26)

    #Page number-3
    #Left horizontal line
    pdf.set_draw_color(109, 111, 113)
    pdf.set_line_width(0.75)
    pdf.line(0, 292, WIDTH/2-5, 292)
    # Number 2
    pdf.set_font('Roboto-Bold', 'B', 10)
    pdf.set_xy(WIDTH/2-1.5, 290)
    pdf.set_text_color(0, 0, 0)
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
    pdf.image("./resources/hindi/hn_4_01.png", x=10, y=6.5, h=6)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(110, 5)
    pdf.set_font('Roboto-Bold', 'B', 12)
    pdf.cell(90, 10, district[3], align='R')

    # Add vertical top bar
    pdf.image("./resources/hindi/hn_4_02.png", x=7, y=25, h=229)

    # Put Top legends
    put_legends(pdf, district[1], 0, 15)

    # Top section - indicator labels
    fp_sat = "Demand for FP satisfied"
    iod_salt = "Iodized salt"
    mcp_rec = "Pregnancy registered (MPC card)"
    anc_firsttri = "ANC first trimester"
    anc4 = "> 4 ANC visits"
    anc_weigh = "Weighing"
    counsel_birth_prepare = "Birth preparedness counselling"
    flw_breastcouns = "Breastfeeding counselling"
    protect_tetanus = "Tetanus injection"
    IFA_rec = "Received IFA tab/syrup"
    deworm_preg = "Deworming"
    icds_thr_preg = "Food supplementation"

    # Middle section - indicator labels
    inst_birth = "Institutional birth"
    jsy_rec1 = "Financial assistance (JSY)"
    ba_healthpro = "Skilled birth attendant"
    mopostnat_2day_hp = "Postnatal care for mothers"
    chpostnat_2day_hp = "Postnatal care for babies"
    icds_thr_lact = "Food supplementation"
    icds_hlthnut_lact = "Health & nutrition education"
    icds_hlthcheck_lact = "Health checkup (ICDS)"

    # Bottom section - indicator labels
    full_immun1 = "Full immunization"
    chvitA_6m1 = "Vitamin A"
    ch_ironsupp1 = "Pediatric IFA"
    ch_deworm1 = "Deworming"
    icds_thr6_35_child = "Food supplementation (6-35 months)"
    icds_weight_child = "Weighing"
    icds_weightcounse_child = "Counselling on child growth"
    ch_ors = "ORS during diarrhea"
    ch_zinc = "Zinc during diarrhea"
    ari_treat = "Careseeking for ARI"
    icds_preschool_child = "Preschool at AWC"
    icds_hlthcheck_child = "Health checkup from AWC"

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

    #Put the indicators
    pdf.image("./resources/hindi/hn_4_03.png", x=45, y=25, h=228.5)

    # Top section
    # fp_sat = "Demand for FP satisfied"
    draw_dual_lollipop(pdf, co_lollipop_gap, 27, district[93], district[94])
    # iod_salt = "Iodized salt"
    draw_dual_lollipop(pdf, co_lollipop_gap, 34, district[95], district[96])
    # mcp_rec = "Pregnancy registered (MPC card)"
    draw_dual_lollipop(pdf, co_lollipop_gap, 42, district[97], district[98])
    # anc_firsttri = "ANC first trimester"
    draw_dual_lollipop(pdf, co_lollipop_gap, 49, district[99], district[100])
    # anc4 = "> 4 ANC visits"
    draw_dual_lollipop(pdf, co_lollipop_gap, 56, district[101], district[102])
    # anc_weigh = "Weighing"
    draw_dual_lollipop(pdf, co_lollipop_gap, 63, district[103], district[104])
    # counsel_birth_prepare = "Birth preparedness counselling"
    draw_dual_lollipop(pdf, co_lollipop_gap, 71, district[105], district[106])
    # flw_breastcouns = "Breastfeeding counselling"
    draw_dual_lollipop(pdf, co_lollipop_gap, 78, district[107], district[108])
    # protect_tetanus = "Tetanus injection"
    draw_dual_lollipop(pdf, co_lollipop_gap, 85, district[109], district[110])
    # IFA_rec = "Received IFA tab/syrup"
    draw_dual_lollipop(pdf, co_lollipop_gap, 92, district[111], district[112])
    # deworm_preg = "Deworming"
    draw_dual_lollipop(pdf, co_lollipop_gap, 99.5, district[113], district[114])
    # icds_thr_preg = "Food supplementation"
    draw_dual_lollipop(pdf, co_lollipop_gap, 107, district[115], district[116])

    # Middle section
    # inst_birth = "Institutional birth"
    draw_dual_lollipop(pdf, co_lollipop_gap, 114, district[117], district[118])
    # jsy_rec1 = "Financial assistance (JSY)"
    draw_dual_lollipop(pdf, co_lollipop_gap, 121, district[119], district[120])
    # ba_healthpro = "Skilled birth attendant"
    draw_dual_lollipop(pdf, co_lollipop_gap, 128.5, district[121], district[122])
    # mopostnat_2day_hp = "Postnatal care for mothers"
    draw_dual_lollipop(pdf, co_lollipop_gap, 136, district[123], district[124])
    # chpostnat_2day_hp = "Postnatal care for babies"
    draw_dual_lollipop(pdf, co_lollipop_gap, 143, district[125], district[126])
    # icds_thr_lact = "Food supplementation"
    draw_dual_lollipop(pdf, co_lollipop_gap, 150.5, district[127], district[128])
    # icds_hlthnut_lact = "Health & nutrition education"
    draw_dual_lollipop(pdf, co_lollipop_gap, 157, district[129], district[130])
    # icds_hlthcheck_lact = "Health checkup (ICDS)"
    draw_dual_lollipop(pdf, co_lollipop_gap, 165, district[131], district[132])

    # Bottom section
    # full_immun1 = "Full immunization"
    draw_dual_lollipop(pdf, co_lollipop_gap, 172, district[133], district[134])
    # chvitA_6m1 = "Vitamin A"
    draw_dual_lollipop(pdf, co_lollipop_gap, 179, district[135], district[136])
    # ch_ironsupp1 = "Pediatric IFA"
    draw_dual_lollipop(pdf, co_lollipop_gap, 187, district[137], district[138])
    # ch_deworm1 = "Deworming"
    draw_dual_lollipop(pdf, co_lollipop_gap, 194, district[139], district[140])
    # icds_thr6_35_child = "Food supplementation (6-35 months)"
    draw_dual_lollipop(pdf, co_lollipop_gap, 201, district[141], district[142])
    # icds_weight_child = "Weighing"
    draw_dual_lollipop(pdf, co_lollipop_gap, 208, district[143], district[144])
    # icds_weightcounse_child = "Counselling on child growth"
    draw_dual_lollipop(pdf, co_lollipop_gap, 215.5, district[145], district[146])
    # ch_ors = "ORS during diarrhea"
    draw_dual_lollipop(pdf, co_lollipop_gap, 223, district[147], district[148])
    # ch_zinc = "Zinc during diarrhea"
    draw_dual_lollipop(pdf, co_lollipop_gap, 230.5, district[149], district[150])
    # ari_treat = "Careseeking for ARI"
    draw_dual_lollipop(pdf, co_lollipop_gap, 237, district[151], district[152])
    # icds_preschool_child = "Preschool at AWC"
    draw_dual_lollipop(pdf, co_lollipop_gap, 245, district[153], district[154])
    # icds_hlthcheck_child = "Health checkup from AWC"
    draw_dual_lollipop(pdf, co_lollipop_gap, 252, district[155], district[156])

    # Note for NA description
    pdf.image("./resources/hindi/hn_NA.png", x=93, y=262, h=3.5)

    # Bottom Points of discussion grey bar
    pdf.image("./resources/hindi/hn_4_04.png", x=7, y=266, h=22)

    #Page number-4
    #Left horizontal line
    pdf.set_draw_color(109, 111, 113)
    pdf.set_line_width(0.75)
    pdf.line(0, 292, WIDTH/2-5, 292)
    # Number 4
    pdf.set_font('Roboto-Bold', 'B', 10)
    pdf.set_xy(WIDTH/2-1.5, 290)
    pdf.set_text_color(0, 0, 0)
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
    path = 'generated_dnp/comparable_dnp_hindi'
    dirName = path + '/{}'.format(district[1])
    if not os.path.exists(dirName):
        os.mkdir(dirName)
    pdf.output(dirName+'/'+filename, "F")

    # Success message
    print(district[0] + "." + district[3] + " of " + district[1] + " generated.")

#Read CSV file
# comparable_district_data_temp.csv --> Temporary file with 6 rows for testing
# comparable_district_data.csv --> Actual file 575 rows
with open("./data/csv/comparable_district_data.csv", 'r') as infile:
    district_reader = csv.reader(infile, delimiter=",")
    district_header = next(district_reader)
    for district in district_reader:
        # Read State level data
        with open("./data/csv/comparable_state_data.csv", 'r') as infile:
            state_reader = csv.reader(infile, delimiter=",")
            state_header = next(state_reader)
            for state in state_reader:
                if district[2] == state[2]:
                    #Generated DNP file name
                    filename="{}-{}-HINDI.pdf".format(district[3], district[1])
                    create_report(filename)
