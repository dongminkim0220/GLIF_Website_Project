# creating the report 

def formsetting(report):
    report.setLineWidth(.3)
    report.setFont('Times-Roman', 12)

    report.drawString(100, 750, "Global News Clipping")
    report.line(120,700,580,700)
    report.drawString(500,800,"GLIF")