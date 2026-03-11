from tempfile import SpooledTemporaryFile

from pypdf import PdfReader, PdfWriter, Transformation
from PIL import Image


def create_image_page(
    image_path: str, width: float, height: float
) -> tuple[PdfReader, SpooledTemporaryFile]:
    img = Image.open(image_path)
    img = img.resize((int(width), int(height)), Image.LANCZOS)
    f = SpooledTemporaryFile()
    img.save(f, "PDF")
    f.seek(0)
    return PdfReader(f), f


manager = "Manager_Night_Checklist.pdf"
monke_path = "a3eacab5-e3ca-428f-9157-44e7d694a6d5/MonkeDAO_DAOJones.png"

manager_reader = PdfReader(manager)
manager_page = manager_reader.pages[0]
page_width = manager_page.mediabox.width
page_height = manager_page.mediabox.height

monke_width = 60
monke_height = 60
margin = 30

monke_pdf, monke_file = create_image_page(monke_path, monke_width, monke_height)
monke_page = monke_pdf.pages[0]

x_pos = page_width - monke_width - margin
y_pos = page_height - monke_height - margin

trans = Transformation().translate(x_pos, y_pos)
manager_page.merge_transformed_page(monke_page, trans)

merger = PdfWriter()

mic_guide = "4256d4c8-59ea-4659-a490-d63f6fabeae5_MIC_Guide___2024_Final.pdf"
boh = "BOH_Night_Checklist.pdf"
foh = "FOH_Night_Checklist.pdf"

with open(mic_guide, "rb") as f:
    mic_pdf = PdfReader(f)
    mic_page = mic_pdf.pages[-1]
    mic_page.rotate(90)
    merger.add_page(mic_page)

merger.add_page(manager_page)

for pdf in [boh, foh]:
    with open(pdf, "rb") as f:
        reader = PdfReader(f)
        for page in reader.pages:
            merger.add_page(page)

merger.write("MASTER_CHECKLIST.PDF")
merger.close()
monke_file.close()
