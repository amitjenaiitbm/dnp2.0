from fpdf import FPDF

# create FPDF object
# Layout ('P', 'L')
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', (100,150) --> custom)
pdf = FPDF('P', 'mm', 'A4')

# Add a page
pdf.add_page()

# specify font
# default fonts available ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
# 'B' (bold), 'U' (underline), 'I' (italics), ' (regular)', combination (i.e., ('BU'))
pdf.set_font('helvetica', 'B', 16)

# Add text (using cell)
# w = width
# h = height
# txt = your text
# ln (0 False; 1 True - move cursor down to the next line)
pdf.cell(120, 100, 'Hello World!', ln=True, border=True) #40 & 10 are in the units that we specified earlier i.e. mm
pdf.cell(80, 10, 'Good Bye World!')

pdf.output('pdf_1.pdf')
