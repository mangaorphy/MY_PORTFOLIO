"""AmaliTech Apprenticeship Programme (September Cohort) — Python Backend + AI
App Development track.

Reuses the ALU Resume Template layout from space_for_giants_cv.py: centered
header block, single column, ruled section headings in navy small-caps,
right-aligned dates.
"""

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable, KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table,
    TableStyle,
)

file_name = "Orpheus_Manga_Mhizha_Resume_AmaliTech.pdf"

MARGIN  = 0.5 * inch
FULL_W  = letter[0] - 2 * MARGIN

doc = SimpleDocTemplate(
    file_name,
    pagesize=letter,
    rightMargin=MARGIN, leftMargin=MARGIN,
    topMargin=0.5 * inch, bottomMargin=0.5 * inch,
    title="Orpheus Mhizha Manga - Resume",
    author="Orpheus Mhizha Manga",
    subject="AmaliTech Apprenticeship - Python Backend + AI App Development",
)

navy  = colors.HexColor("#1f3864")
text  = colors.HexColor("#1a1a1a")
muted = colors.HexColor("#444444")
link  = "#1f3864"

styles = getSampleStyleSheet()


def S(name, **kw):
    styles.add(ParagraphStyle(name=name, **kw))


S("HName",   fontSize=15,   leading=17,   fontName="Helvetica-Bold",
             alignment=TA_CENTER, textColor=navy, spaceAfter=2)
S("HLine",   fontSize=10,   leading=12,   fontName="Helvetica",
             alignment=TA_CENTER, textColor=text)
S("Sec",     fontSize=10.5, leading=12,   fontName="Helvetica-Bold",
             textColor=navy, spaceBefore=6, spaceAfter=1)
S("Body",    fontSize=10,   leading=11.8, fontName="Helvetica",
             alignment=TA_JUSTIFY, textColor=text, spaceAfter=1)
S("RoleL",   fontSize=10,   leading=12,   fontName="Helvetica-Bold",
             alignment=TA_LEFT, textColor=text)
S("RoleR",   fontSize=10,   leading=12,   fontName="Helvetica-Bold",
             alignment=TA_RIGHT, textColor=text)
S("Org",     fontSize=10,   leading=12,   fontName="Helvetica", textColor=text)
S("Course",  fontSize=10,   leading=12,   fontName="Helvetica-Oblique",
             alignment=TA_JUSTIFY, textColor=muted)
S("Bul",     fontSize=10,   leading=12,   fontName="Helvetica",
             alignment=TA_JUSTIFY, textColor=text,
             leftIndent=13, bulletIndent=4, spaceAfter=1.5,
             bulletFontName="Helvetica", bulletFontSize=6.5)
S("Grid",    fontSize=10,   leading=12,   fontName="Helvetica", textColor=text)

story = []


def rule():
    story.append(HRFlowable(width="100%", thickness=0.7, color=navy,
                            spaceBefore=1, spaceAfter=3))


def sec(title):
    story.append(Paragraph(title.upper(), styles["Sec"]))
    rule()


def header_row(left, right, gap=3):
    """Bold role on the left, right-aligned date on the same line."""
    story.append(Spacer(1, gap))
    t = Table([[Paragraph(left, styles["RoleL"]),
                Paragraph(right, styles["RoleR"])]],
              colWidths=[FULL_W * 0.66, FULL_W * 0.34])
    t.setStyle(TableStyle([
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING",   (0, 0), (-1, -1), 0),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 0),
        ("TOPPADDING",    (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(t)


def bullets(items):
    for b in items:
        story.append(Paragraph(b, styles["Bul"], bulletText="●"))


# ── Header ────────────────────────────────────────────────────────────────
story.append(Paragraph("ORPHEUS MHIZHA MANGA", styles["HName"]))
story.append(Paragraph(
    "Python Backend &amp; AI Application Developer", styles["HLine"]))
story.append(Paragraph(
    "Kigali, Rwanda | +250 792 957 530", styles["HLine"]))
story.append(Paragraph(
    f"<link href='mailto:o.manga@alustudent.com' color='{link}'>o.manga@alustudent.com</link> | "
    f"<link href='https://www.linkedin.com/in/orpheus-manga-13ab76290/' color='{link}'>LinkedIn</link> | "
    f"<link href='https://github.com/mangaorphy' color='{link}'>GitHub</link> | "
    f"<link href='https://mangaorphy.github.io/MY_PORTFOLIO/' color='{link}'>Portfolio</link>",
    styles["HLine"]))
story.append(Spacer(1, 4))

# ── Summary ───────────────────────────────────────────────────────────────
sec("Summary")
story.append(Paragraph(
    "B.Sc. Software Engineering (Machine Learning) graduand at African Leadership University in "
    "Kigali, Rwanda, having completed and successfully defended my capstone project before the "
    "university examination panel. I have over two years of practical Python programming "
    "experience across internships, research work, and personal projects. I build and deploy "
    "backend services with Python, FastAPI, and Flask, integrating machine learning and large "
    "language models into working applications. I am comfortable with REST APIs, relational "
    "databases, Git version control, and Docker, work independently with minimal supervision, "
    "learn new tools quickly, and am fully available for the entire six-month full-time "
    "programme.",
    styles["Body"]))

# ── Education ─────────────────────────────────────────────────────────────
sec("Education")
header_row("African Leadership University – Kigali, Rwanda",
           "September 2023 – August 2026")
story.append(Paragraph(
    "B.Sc. Software Engineering, Machine Learning Specialization. CGPA 4.41 / 5.0. Capstone "
    "project completed and successfully defended; pending graduation.",
    styles["Org"]))
story.append(Paragraph(
    "<i>Relevant Coursework:</i> Object-Oriented Programming; Databases &amp; Data Management; "
    "Web Development; Data Science &amp; Analytics; Machine Learning; Computer Vision; "
    "Statistics &amp; Probability.", styles["Course"]))

# ── Projects ──────────────────────────────────────────────────────────────
sec("Software Projects")

header_row("LexRwanda: Legal Question-Answering Assistant", "2025 – 2026")
story.append(Paragraph(
    "Python · NLP / LLM · REST API · <link href='https://github.com/mangaorphy/LexRwanda' "
    f"color='{link}'>github.com/mangaorphy/LexRwanda</link>", styles["Org"]))
bullets([
    "Built an AI-powered legal assistant that answers questions about Rwandan law in plain "
    "language, making legal information more accessible to non-specialists.",

    "Implemented a retrieval-augmented generation (RAG) pipeline in Python covering document "
    "ingestion, text chunking, embedding, and semantic search, so answers are grounded in source "
    "legal texts rather than model guesswork.",

    "Exposed the system through a Python REST API so the assistant can be consumed by web and "
    "mobile clients, and structured the codebase into reusable modules with version control on "
    "Git and GitHub.",
])

header_row("PlantGuardAI: Crop Disease Detection App", "2025")
story.append(Paragraph(
    "Python · Computer Vision · Flask/FastAPI · <link href='https://github.com/mangaorphy/PlantGuardAI' "
    f"color='{link}'>github.com/mangaorphy/PlantGuardAI</link>", styles["Org"]))
bullets([
    "Developed an AI application that identifies crop diseases from leaf photographs, helping "
    "smallholder farmers diagnose problems early without expert assistance.",

    "Trained and evaluated a convolutional neural network image classifier in TensorFlow and "
    "PyTorch, handling dataset preparation, augmentation, and per-class evaluation to confirm the "
    "model worked across all disease categories.",

    "Wrapped the trained model in a Python web backend with an image-upload endpoint that returns "
    "predictions as JSON, taking the project from notebook experiment to a deployable "
    "application.",
])

header_row("AlertReck: Edge AI Ranger Alert System (Capstone)", "2025 – 2026")
story.append(Paragraph(
    "Python · Edge AI · Raspberry Pi · <link href='https://github.com/mangaorphy/alertreck' "
    f"color='{link}'>github.com/mangaorphy/alertreck</link>", styles["Org"]))
bullets([
    "Designed and built an offline acoustic monitoring system that detects potential poaching "
    "sounds on a Raspberry Pi and automatically sends GPS-tagged SMS alerts to rangers in areas "
    "with no internet connectivity.",

    "Curated and labelled a dataset of 11,333 acoustic recordings across seven threat classes, "
    "then trained and evaluated the classification model that powers detection.",

    "Debugged the evaluation pipeline to find a train/test split defect that had inflated reported "
    "accuracy by 10 points, and successfully defended the completed system before the university "
    "examination panel.",
])

# ── Experience ────────────────────────────────────────────────────────────
sec("Experience")

header_row("AI Developer Intern", "August 2025 – December 2025")
story.append(Paragraph("ThinkGreen Africa – Remote", styles["Org"]))
bullets([
    "Fine-tuned a LLaMA/Mistral language model using LoRA (PEFT) to 92% accuracy on the target "
    "task, preparing and validating the training data end to end.",

    "Deployed the model as a FastAPI inference service serving predictions at under 200ms "
    "latency, improving throughput threefold over the previous setup.",

    "Worked remotely with minimal supervision, managing my own tasks and delivering against "
    "agreed milestones.",
])

header_row("Research Assistant", "January 2026 – Present")
story.append(Paragraph(
    "Rizivo Research Lab, African Leadership University – Kigali, Rwanda",
    styles["Org"]))
bullets([
    "Review literature and datasets to identify research problems and gaps, and contribute to "
    "drafting, revising, and submitting research papers for publication.",

    "Process and annotate research data in Python, documenting decisions so results remain "
    "reproducible across review cycles.",
])

header_row("Data Research Intern", "February 2025 – May 2025")
story.append(Paragraph("Shangani Holistic – Shangani, Zimbabwe", styles["Org"]))
bullets([
    "Collected, cleaned, and validated ecological field datasets using Python, R, and QGIS, "
    "resolving missing records and inconsistent entries before analysis and reporting.",
])

# ── Extracurricular ───────────────────────────────────────────────────────
sec("Extracurricular Activities")

header_row("Robotics &amp; IoT Instructor", "2026 – Present")
story.append(Paragraph("CodeFactory – Kigali, Rwanda", styles["Org"]))
bullets([
    "Teach robotics and Internet of Things (IoT) to students across several schools in Kigali, "
    "taking learners from no prior experience through to writing their own programs for IoT "
    "devices on the Arduino UNO.",

    "Break down programming and electronics concepts for beginners of varying ability, adapting "
    "explanations until each student can build and debug a working device independently.",
])

header_row("3rd Place, CodeXtreme National Hackathon (Team TerraFoma)", "2026")
story.append(Paragraph(
    "Built and pitched a working AI solution under a 24-hour deadline, placing third nationally "
    "among competing university teams.", styles["Body"]))

# ── Skills ────────────────────────────────────────────────────────────────
skills_block = [
    Paragraph("TECHNICAL SKILLS", styles["Sec"]),
    HRFlowable(width="100%", thickness=0.7, color=navy, spaceBefore=1, spaceAfter=3),
]

for cat, items in [
    ("Programming",
     "Python (OOP, functions, modules) · SQL · JavaScript · R · Bash"),

    ("Backend &amp; APIs",
     "FastAPI · Flask · REST API design · JSON · Authentication basics · PostgreSQL · MySQL"),

    ("AI &amp; Machine Learning",
     "PyTorch · TensorFlow · scikit-learn · Hugging Face · LoRA/PEFT · RAG · CNNs · Transformers"),

    ("Data",
     "Pandas · NumPy · Data cleaning &amp; validation · Dataset curation"),

    ("Tools &amp; Practices",
     "Git &amp; GitHub · Docker · CI/CD · Linux · Google Cloud Platform (GCP) · Agile teamwork"),

    ("Embedded &amp; IoT",
     "Arduino UNO · Raspberry Pi · Sensors &amp; microcontrollers"),

    ("Languages",
     "English (fluent, spoken and written) · Shona (native)"),
]:
    skills_block.append(Paragraph(f"<b>{cat}:</b> {items}", styles["Body"]))

story.append(KeepTogether(skills_block))

# ── Certifications ────────────────────────────────────────────────────────
sec("Certifications")
cert_link = ("https://docs.google.com/document/d/"
             "1XNwPcwZGOOx0-MODADeU-OQYLDkjSc-jpYnrXSEOOZM/edit?usp=sharing")
story.append(Paragraph(
    " · ".join(
        f"<link href='{cert_link}' color='{link}'>{c}</link>" for c in [
            "Meta Backend Developer Professional Certificate",
            "Neural Networks &amp; Deep Learning (DeepLearning.AI)",
            "Linear Algebra for ML (DeepLearning.AI)",
        ]),
    styles["Body"]))

# ── Availability ──────────────────────────────────────────────────────────
sec("Availability")
story.append(Paragraph(
    "Currently based in Kigali, Rwanda. Fully available to commit full-time, Monday to Friday, for "
    "the entire six-month programme starting with the September cohort.",
    styles["Body"]))

doc.build(story)
print(f"PDF generated: {file_name}")
