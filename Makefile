.PHONY: all clean help master

MARKDOWNS = BOH_Night_Checklist.md FOH_Night_Checklist.md Manager_Night_Checklist.md
PDFS = $(MARKDOWNS:.md=.pdf)

help:
	@echo "Available targets:"
	@echo "  all          - Build all PDFs (BOH, FOH, Manager)"
	@echo "  master       - Build combined MASTER_CHECKLIST.PDF"
	@echo "  clean        - Remove generated PDFs"
	@echo ""
	@echo "Usage: make [target]"

all: $(PDFS)

master: MASTER_CHECKLIST.PDF

Manager_Night_Checklist.pdf: Manager_Night_Checklist.md
	pandoc -V geometry:margin=0.25in -V fontsize=9pt -o $@ $<

BOH_Night_Checklist.pdf: BOH_Night_Checklist.md
	pandoc -V geometry:margin=0.6in -V fontsize=10pt -o $@ $<

FOH_Night_Checklist.pdf: FOH_Night_Checklist.md
	pandoc -o $@ $<

clean:
	rm -f $(PDFS)

MASTER_CHECKLIST.PDF: combine_pdfs.py 4256d4c8-59ea-4659-a490-d63f6fabeae5_MIC_Guide___2024_Final.pdf Manager_Night_Checklist.pdf BOH_Night_Checklist.pdf FOH_Night_Checklist.pdf
	.venv/bin/python combine_pdfs.py
