from pypdf import PdfWriter, PdfReader

merger = PdfWriter()

mic_guide = "4256d4c8-59ea-4659-a490-d63f6fabeae5_MIC_Guide___2024_Final.pdf"
manager = "Manager_Night_Checklist.pdf"
boh = "BOH_Night_Checklist.pdf"
foh = "FOH_Night_Checklist.pdf"

with open(mic_guide, "rb") as f:
    mic_pdf = PdfReader(f)
    mic_page = mic_pdf.pages[-1]
    mic_page.rotate(90)
    merger.add_page(mic_page)

for pdf in [manager, boh, foh]:
    with open(pdf, "rb") as f:
        reader = PdfReader(f)
        for page in reader.pages:
            merger.add_page(page)

merger.write("MASTER_CHECKLIST.PDF")
merger.close()
