from fpdf import FPDF

def download_pdf(sections, filename="can_trace_analysis.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for section in sections:
        title = section.get("title", "").strip()
        if title:
            pdf.set_font("Arial", "B", size=14)
            pdf.cell(0, 10, txt=title, ln=True)

        content = section.get("content", "").strip()
        if content:
            pdf.set_font("Arial", size=10)
            for line in content.splitlines():
                pdf.multi_cell(0, 5, line)
            pdf.ln(5)

    pdf.output(filename)
