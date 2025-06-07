# This script generates a PDF quiz for "The Story of Village Palampur".
# It uses minimal PDF syntax without external libraries.

def create_quiz_pdf(filename):
    title = "Quiz: Economics Chapter 1 - The Story of Village Palampur"
    questions = [
        ("1. What is the main occupation of most people in Palampur?",
         "a) Farming  (b) Weaving  (c) Trade  (d) Factory work"),
        ("2. Which facility helped expand irrigation in Palampur?",
         "a) Persian wheels  (b) Tube wells  (c) Canals  (d) Tanks"),
        ("3. Which crop is typically grown in the rabi season in Palampur?",
         "a) Jowar  (b) Bajra  (c) Wheat  (d) Maize"),
        ("4. What does the term 'multiple cropping' mean?",
         "a) Growing a single crop  (b) Growing two or more crops on the same field in a year  (c) Using more chemical fertilisers  (d) Growing crops using only machines"),
        ("5. Which factor of production includes tools and machinery?",
         "a) Land  (b) Labour  (c) Physical capital  (d) Human capital"),
        ("6. Why do small farmers often borrow money from large farmers or traders?",
         "a) To buy mobile phones  (b) To buy seeds and fertilisers  (c) To go on vacations  (d) To pay school fees"),
        ("7. Which of the following is a non-farm activity found in Palampur?",
         "a) Dairy  (b) Wheat farming  (c) Sugarcane cultivation  (d) Paddy farming"),
        ("8. About what proportion of Palampur's land is irrigated?",
         "a) Less than 10%  (b) Around half  (c) More than 75%  (d) Almost none"),
        ("9. Large farmers in Palampur generally employ which kind of workers?",
         "a) Government officials  (b) Hired labourers  (c) Doctors  (d) Carpenters"),
        ("10. Palampur is best described as a:",
         "a) Real historical village  (b) Hypothetical example  (c) Large industrial city  (d) Seaside resort")
    ]

    pdf = bytearray()
    offsets = []

    def write(text):
        pdf.extend(text.encode('latin-1'))

    def add_object(num, data):
        offsets.append(len(pdf))
        write(f"{num} 0 obj\n{data}\nendobj\n")

    write("%PDF-1.4\n")
    add_object(1, "<< /Type /Catalog /Pages 2 0 R >>")
    add_object(2, "<< /Type /Pages /Kids [3 0 R] /Count 1 >>")
    add_object(3, "<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>")

    content_lines = []
    content_lines.append("/F1 18 Tf")
    content_lines.append("70 770 Td")
    content_lines.append(f"({title}) Tj")
    content_lines.append("/F1 12 Tf")
    y = 740
    content_lines.append(f"70 {y} Td")
    content_lines.append("() Tj")
    y -= 20
    for q, opts in questions:
        content_lines.append(f"70 {y} Td")
        content_lines.append(f"({q}) Tj")
        y -= 20
        content_lines.append(f"70 {y} Td")
        content_lines.append(f"(({opts})) Tj")
        y -= 20
        content_lines.append(f"70 {y} Td")
        content_lines.append("() Tj")
        y -= 20
    content = "\n".join(content_lines) + "\n"

    add_object(4, f"<< /Length {len(content)} >>\nstream\n{content}endstream")
    add_object(5, "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")

    xref_pos = len(pdf)
    write("xref\n0 6\n")
    write("0000000000 65535 f \n")
    for off in offsets:
        write(f"{off:010d} 00000 n \n")
    write("trailer\n<< /Root 1 0 R /Size 6 >>\nstartxref\n")
    write(str(xref_pos))
    write("\n%%EOF")

    with open(filename, 'wb') as f:
        f.write(pdf)

if __name__ == "__main__":
    create_quiz_pdf("class9-socialscience/quizzes/economics-ch1-village-palampur-10q.pdf")
