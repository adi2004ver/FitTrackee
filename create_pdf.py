from markdown_pdf import Section, MarkdownPdf

def create_pdf(md_path, pdf_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    pdf = MarkdownPdf(toc_level=2)
    pdf.add_section(Section(text, toc=False))
    pdf.save(pdf_path)

if __name__ == "__main__":
    create_pdf('README.md', 'README.pdf')
    create_pdf('fittrackee_presentation_slides.md', 'fittrackee_presentation_slides.pdf')
    print("PDFs created successfully!")
