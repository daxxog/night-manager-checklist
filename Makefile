.PHONY: all clean help

MARKDOWNS = BOH_Night_Checklist.md FOH_Night_Checklist.md Manager_Night_Checklist.md
PDFS = $(MARKDOWNS:.md=.pdf)

help:
	@echo "Available targets:"
	@echo "  all     - Build all PDFs (BOH, FOH, Manager)"
	@echo "  clean   - Remove generated PDFs"
	@echo ""
	@echo "Usage: make [target]"

all: $(PDFS)

Manager_Night_Checklist.pdf: Manager_Night_Checklist.md
	pandoc -V geometry:margin=0.25in -V fontsize=9pt -o $@ $<

BOH_Night_Checklist.pdf: BOH_Night_Checklist.md
	pandoc -V geometry:margin=0.6in -V fontsize=10pt -o $@ $<

FOH_Night_Checklist.pdf: FOH_Night_Checklist.md
	pandoc -o $@ $<

clean:
	rm -f $(PDFS)
