from fpdf import FPDF
from datetime import datetime

class PDFReport(FPDF):


    def header(self):
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 10, "Rapport d'Analyse des CV", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(
            0,
            10,
            f"Page {self.page_no()}",
            align="C"
        )


def generate_pdf_report(results, output_path):

 
    pdf = PDFReport()

    # pdf.add_font(
    #         "DejaVu",
    #         "",
    #         "fonts/DejaVuSans.ttf",
    #         uni=True
    # )

    # pdf.set_font("DejaVu", "", 11)
    pdf.set_font("Helvetica", "", 11)


    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.add_page()

    #pdf.set_font("Helvetica", "", 11)

    pdf.cell(
        0,
        8,
        f"Date de génération : {datetime.now().strftime('%d/%m/%Y %H:%M')}",
        ln=True
    )

    pdf.ln(5)

    for rank, candidate in enumerate(results, start=1):

        pdf.set_font("Helvetica", "B", 13)
        name = str(candidate.get("name", "Candidat Inconnu"))[:80]

        pdf.multi_cell(
            0,
            8,
            f"{rank}. {candidate['name']}"
        )  

        pdf.ln(2)

        pdf.set_x(10)  # Indentation pour le contenu du candidat

        pdf.set_font("Helvetica", "", 11)
        
       
        content = (
            f"Score de pertinence : {candidate['score']}/100\n\n"
            f"Niveau d'etudes : {candidate['education']}\n"
            f"Experience : {candidate['experience']} ans\n\n"
            f"Competences : {', '.join(candidate['skills'])}\n\n"
            f"Langues : {', '.join(candidate['languages'])}\n\n"
            f"Certifications : {', '.join(candidate['certifications'])}\n\n"
            f"Points forts : {', '.join(candidate['strengths'])}\n\n"
            f"Points de vigilance : {', '.join(candidate['warnings'])}"
        )
        pdf.set_x(10)  # Réinitialiser l'indentation pour le contenu du candidat

        pdf.multi_cell(180, 7, content)


        pdf.ln(5)

    pdf.output(output_path)