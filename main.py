from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation = "portrait", unit = "mm", format = 'A4')
#dont auto break line
pdf.set_auto_page_break(auto=False, margin = 0)

#file must be in the same directory
df = pd.read_csv("topics.csv")

#read through the CSV file row by row and add a pdf page for each row
for index,row in df.iterrows():
    for index in range(row["Pages"]):
        pdf.add_page()

        #Set header
        pdf.set_font(family="Times", size=24)
        pdf.set_text_color(0,0,254)
        #add topic to start of page
        # w is width, h is height, should be same as text size, ln is line spacing, border = box around text
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)

        #set body to have lines all over page
        # coordinates for starting and ending point of the line, A4 is 210
        for i in range(20,270,12):
            pdf.line(10, i, 200, i)

        #set footer
        # 278mm after first line
        pdf.ln(260)
        pdf.set_font(family="Times",style="I",size = 8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0,h=10,txt=row["Topic"], align="R")

pdf.output("output.pdf")


