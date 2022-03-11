from fpdf import FPDF

# create FPDF object
# Layout ('P', 'L')
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', (100,150) --> custom)
pdf = FPDF('P', 'mm', 'A4')

# Set auto page break
pdf.set_auto_page_break(auto=True, margin = 15)

# Add a page
pdf.add_page()

# specify font
# default fonts available ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
# 'B' (bold), 'U' (underline), 'I' (italics), ' (regular)', combination (i.e., ('BU'))
pdf.set_font('helvetica', 'BIU', 16)

pdf.set_font('times', '', 12)

for i in range(1, 41):
    pdf.cell(0, 10, f'This is line {i} :D', ln=True)

pdf.output('pdf_2.pdf')
