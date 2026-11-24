"""Zipline Data Labeling Specialist CV.

Reuses the ALU Resume Template layout from amalitech_resume.py: centered
header block, single column, ruled section headings in navy, right-aligned
dates, bulleted achievements. Content retargeted to sensor-data labeling,
dataset review, and dataset quality assurance.
"""

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle,
)

file_name = "Orpheus_Manga_Mhizha_Resume_Zipline.pdf"

MARGIN  = 0.5 * inch
FULL_W  = letter[0] - 2 * MARGIN

doc = SimpleDocTemplate(
    file_name,
    pagesize=letter,
    rightMargin=MARGIN, leftMargin=MARGIN,
    topMargin=0.5 * inch, bottomMargin=0.5 * inch,
    title="Orpheus Mhizha Manga - Resume",
    author="Orpheus Mhizha Manga",
    subject="Data Labeling Specialist - Zipline",
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
             textColor=navy, spaceBefore=8, spaceAfter=2)
S("Body",    fontSize=10,   leading=12.5, fontName="Helvetica",
             alignment=TA_JUSTIFY, textColor=text, spaceAfter=2)
S("RoleL",   fontSize=10,   leading=12,   fontName="Helvetica-Bold",
             alignment=TA_LEFT, textColor=text)
S("RoleR",   fontSize=10,   leading=12,   fontName="Helvetica-Bold",
             alignment=TA_RIGHT, textColor=text)
S("Org",     fontSize=10,   leading=12,   fontName="Helvetica", textColor=text)
S("Course",  fontSize=10,   leading=12,   fontName="Helvetica-Oblique",
             alignment=TA_JUSTIFY, textColor=muted)
S("Bul",     fontSize=10,   leading=12.5, fontName="Helvetica",
             alignment=TA_JUSTIFY, textColor=text,
             leftIndent=13, bulletIndent=4, spaceAfter=2.5,
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
    "Software Engineer, Machine Learning",
    styles["HLine"]))
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
    "B.Sc. Software Engineering (Machine Learning) graduand with hands-on experience annotating, "
    "reviewing, and auditing large-scale audio, image, and sensor datasets. Experienced in "
    "developing annotation guidelines, resolving edge cases, detecting data-quality issues, and "
    "maintaining reproducible records for machine-learning workflows. Detail-oriented and "
    "methodical, with strong Python-based data-processing skills.",
    styles["Body"]))

# ── Experience ────────────────────────────────────────────────────────────
sec("Experience")

header_row("AI Developer Intern", "August 2025 – December 2025")
story.append(Paragraph("ThinkGreen Africa – Remote", styles["Org"]))
bullets([
    "Prepared, cleaned, and validated training data end-to-end for a LLaMA/Mistral model "
    "fine-tuned with LoRA (PEFT), achieving 92% accuracy on the target task.",

    "Deployed the resulting model as a FastAPI inference service with sub-200 ms latency, "
    "improving throughput threefold over the previous setup.",

    "Worked independently in a remote environment, managing tasks and delivering against agreed "
    "milestones.",
])

header_row("Research Assistant", "January 2026 – Present")
story.append(Paragraph(
    "Rizivo Research Lab, African Leadership University – Kigali, Rwanda",
    styles["Org"]))
bullets([
    "Review and process research datasets in Python, documenting annotation and preprocessing "
    "decisions to maintain reproducibility across research cycles.",

    "Contribute to literature reviews, research analysis, manuscript preparation, and submission "
    "for publication.",
])

header_row("Data Research Intern", "February 2025 – May 2025")
story.append(Paragraph("Shangani Holistic – Shangani, Zimbabwe", styles["Org"]))
bullets([
    "Collected, cleaned, and validated ecological datasets using Python, R, and QGIS, resolving "
    "missing records and inconsistent entries before analysis.",

    "Documented data-cleaning decisions and maintained structured datasets for reproducible "
    "reporting.",
])

# ── Projects ──────────────────────────────────────────────────────────────
sec("Projects")

header_row("AlertReck: Edge AI Ranger Alert System — Final Year Capstone",
           "2025 – 2026")
story.append(Paragraph(
    "Python · Machine Learning · Edge AI · Raspberry Pi · PyTorch · ONNX · "
    "<link href='https://github.com/mangaorphy/alertreck' "
    f"color='{link}'>GitHub</link>", styles["Org"]))
bullets([
    "Designed and built an offline edge-AI acoustic monitoring system on Raspberry Pi that "
    "detects potential poaching-related sounds and automatically sends GPS-tagged SMS alerts to "
    "rangers without internet connectivity.",

    "Curated, annotated, and quality-assured <b>11,333 acoustic recordings across seven "
    "classes</b>, developing preprocessing, segmentation, and metadata workflows for "
    "machine-learning training.",

    "Compared five machine-learning models across four learning paradigms, selecting a "
    "lightweight CNN that achieved <b>82.6% test accuracy, 0.807 macro-F1, and 0.976 "
    "macro-AUC</b> with a 4.6 MB deployment model.",

    "Identified and corrected a train/test data-leakage defect that had <b>inflated reported "
    "model performance by approximately 10 percentage points</b>, ensuring reliable evaluation "
    "of the final system.",
])

header_row("UNSW Predators: Wildlife Camera-Trap Dataset Study", "2025")
story.append(Paragraph(
    "Python · Computer Vision · Data Curation · "
    "<link href='https://github.com/mangaorphy/UNSW-Predators' "
    f"color='{link}'>GitHub</link>", styles["Org"]))
bullets([
    "Curated and validated a <b>131,802-image</b> wildlife camera-trap dataset across five "
    "classes, reviewing category assignments and constructing a stratified sample for quality "
    "assessment.",

    "Identified and quantified severe class imbalance and documented its impact on per-class "
    "evaluation metrics.",
])

header_row("Savanna Acoustic Threat Detection — Reinforcement Learning", "2025")
story.append(Paragraph(
    "Python · Stable-Baselines3 · Gymnasium · PyTorch · "
    "<link href='https://github.com/mangaorphy/orpheus_reinforcement_learning_summative' "
    f"color='{link}'>GitHub</link>", styles["Org"]))
bullets([
    "Designed a custom Gymnasium environment simulating a ranger drone that navigates a 20×20 "
    "savanna grid to detect acoustic threats, with an 847-dimensional observation space and a "
    "structured reward function.",

    "Trained and compared four reinforcement-learning algorithms (DQN, PPO, A2C, REINFORCE) "
    "across 40 hyperparameter-swept runs, with DQN reaching the best mean reward of "
    "<b>50.5</b> and documented training metrics for each configuration.",
])

# ── Education ─────────────────────────────────────────────────────────────
sec("Education")
header_row("African Leadership University – Kigali, Rwanda",
           "September 2023 – August 2026")
story.append(Paragraph(
    "B.Sc. Software Engineering, Machine Learning Specialization. CGPA 4.41 / 5.0. Final-year "
    "requirements completed; capstone defended; graduation pending.",
    styles["Org"]))
story.append(Paragraph(
    "<i>Relevant Coursework:</i> Machine Learning; Computer Vision; Data Science &amp; Analytics; "
    "Statistics &amp; Probability.", styles["Course"]))

# ── Skills ────────────────────────────────────────────────────────────────
sec("Technical Skills")
for cat, items in [
    ("Data Annotation &amp; Quality",
     "Audio annotation · Image annotation · Multi-class labeling · Annotation guidelines · "
     "Edge-case resolution · Dataset review · Label auditing · Metadata management · "
     "Quality assurance · Data validation · Data integrity · Leakage detection"),

    ("Data &amp; Sensor Processing",
     "Acoustic/audio data · Camera-trap imagery · Clinical sensor data · MEMS microphones · "
     "GPS metadata"),

    ("Programming &amp; Tools",
     "Python · Pandas · NumPy · SQL · OpenCV · librosa · R · QGIS · Git/GitHub"),

    ("Machine Learning",
     "PyTorch · TensorFlow · Stable-Baselines3 · Gymnasium · Reinforcement Learning "
     "(DQN/PPO/A2C)"),

    ("Languages",
     "English (fluent, spoken and written) · Shona (native)"),
]:
    story.append(Paragraph(f"<b>{cat}:</b> {items}", styles["Body"]))

# ── Certifications ────────────────────────────────────────────────────────
sec("Certifications")
cert_link = ("https://docs.google.com/document/d/"
             "1XNwPcwZGOOx0-MODADeU-OQYLDkjSc-jpYnrXSEOOZM/edit?usp=sharing")
for c in [
    "Neural Networks &amp; Deep Learning — DeepLearning.AI",
    "Linear Algebra for Machine Learning — DeepLearning.AI",
    "Meta Back-End Developer Professional Certificate",
]:
    story.append(Paragraph(
        f"<link href='{cert_link}' color='{link}'>{c}</link>", styles["Body"]))

# ── Achievements ──────────────────────────────────────────────────────────
sec("Achievements")
story.append(Paragraph(
    "<b>3rd Place — CodeXtreme 2026 National Hackathon</b> (Team TerraFoma).",
    styles["Body"]))

# ── Availability ──────────────────────────────────────────────────────────
sec("Availability")
story.append(Paragraph(
    "Based in Kigali, Rwanda, with legal authorization to work in Rwanda. Available full-time, "
    "40+ hours per week, including rotating shifts, weekends, and public holidays.",
    styles["Body"]))

doc.build(story)
print(f"PDF generated: {file_name}")
