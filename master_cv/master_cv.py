"""Orpheus Mhizha Manga — master CV.

General-purpose ML/software engineering CV. Same visual system as the
targeted variants (centered header, ruled navy section headings, single
column, right-aligned dates) but with role-neutral wording, a stronger
summary, and Experience broadened to include robotics mentoring and
teaching, plus a separate Volunteering section.

Tailored variants live in the *_resume.py / *_cv.py scripts; this one is
the source of truth for shared content.
"""

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle,
)

file_name = "Orpheus_Manga_Mhizha__CV.pdf"

MARGIN  = 0.5 * inch
FULL_W  = letter[0] - 2 * MARGIN

doc = SimpleDocTemplate(
    file_name,
    pagesize=letter,
    rightMargin=MARGIN, leftMargin=MARGIN,
    topMargin=0.5 * inch, bottomMargin=0.5 * inch,
    title="Orpheus Mhizha Manga - CV",
    author="Orpheus Mhizha Manga",
    subject="Software Engineer, Machine Learning",
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
             bulletFontName="Helvetica", bulletFontSize=4.5)

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
story.append(Paragraph("Software Engineer, Machine Learning", styles["HLine"]))
story.append(Paragraph("Kigali, Rwanda | +250 792 957 530", styles["HLine"]))
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
    "Machine Learning Engineer and B.Sc. Software Engineering graduand with hands-on experience "
    "building, evaluating, and deploying scalable machine learning systems. Experienced across "
    "the ML lifecycle, from dataset curation and quality assurance to model training, "
    "optimisation, and deployment on both cloud and resource-constrained environments. Skilled "
    "in Python, PyTorch, TensorFlow, FastAPI, and backend development, with experience building "
    "APIs and integrating machine learning models into production-oriented applications, and "
    "co-author of a paper accepted at Africa at NeurIPS 2026. Strong "
    "interest in opportunities where I can apply my existing skills, learn from experienced "
    "teams, and continue developing as a machine learning and backend engineer.",
    styles["Body"]))

# ── Experience ────────────────────────────────────────────────────────────
sec("Experience")

header_row("Data &amp; GIS Intern", "October 2026 – December 2026")
story.append(Paragraph("Space for Giants, Conservation Science Team – Kenya (In person)", styles["Org"]))
bullets([
    "Work with the wildlife research team in Kenya, supporting conservation decision-making "
    "with spatial and non-spatial data.",

    "Applied computer vision to build a model that identifies <b>collared elephants</b> in "
    "camera-trap imagery, enabling quick evaluation of elephant camera-trap images.",

    "Developed a <b>RAG-based tool</b> that extracts data from EarthRanger, visualises it as "
    "graphs, and generates monthly reports.",
])

header_row("Wildlife Economy Research Intern", "2026 – December 2026")
story.append(Paragraph(
    "School of Wildlife Conservation, African Leadership University – Remote",
    styles["Org"]))
bullets([
    "Research the wildlife economy across African countries, running structured literature "
    "reviews to establish what the evidence shows, where it is thin, and how key terms are "
    "defined across sources.",

    "Source, compile, and construct the datasets behind an African wildlife economy index, "
    "documenting data origins and cleaning decisions so the index can be reproduced and audited.",

    "Interpret index results for non-technical readers, stating data limitations and the "
    "comparability of figures across countries.",
])

header_row("Research Assistant", "January 2026 – Present")
story.append(Paragraph(
    "Rizivo Research Lab, African Leadership University – Kigali, Rwanda",
    styles["Org"]))
bullets([
    "Process and analyse research datasets in Python, documenting annotation and preprocessing "
    "decisions so results stay reproducible across research cycles.",

    "Co-authored, with the lab team, <i>Vector-Free Salience versus Local Dense Retrieval for "
    "Grounded Longitudinal Clinical Summarisation</i>, <b>accepted at Africa at NeurIPS 2026</b>; "
    "contributed to the literature review, experiments, and manuscript.",
])

header_row("Robotics Mentor", "January 2026 – September 2026")
story.append(Paragraph("TheCodeFactoryAfrica – Kigali, Rwanda", styles["Org"]))
bullets([
    "Coordinated robotics and IoT bootcamps, taking student teams from ideation through to a "
    "fully working Arduino-based prototype within each cohort.",

    "Taught embedded programming, sensor integration, and circuit prototyping on Arduino and "
    "LEGO platforms, translating hardware concepts for students with no prior electronics "
    "background.",

    "Hosted online sessions alongside in-person classes, tracked attendance, and used "
    "participant feedback to adjust pacing and content for later cohorts.",
])

header_row("AI Developer Intern", "August 2025 – December 2025")
story.append(Paragraph("ThinkGreen Africa – Remote", styles["Org"]))
bullets([
    "Fine-tuned a LLaMA/Mistral model with LoRA (PEFT), owning the full pipeline from data "
    "preparation and validation through training, and reaching <b>92% accuracy</b> on the "
    "target task.",

    "Deployed the model as a FastAPI inference service with <b>sub-200 ms latency</b>, tripling "
    "throughput over the previous setup.",
])

header_row("Data Research Intern", "February 2025 – May 2025")
story.append(Paragraph("Shangani Holistic – Shangani, Zimbabwe", styles["Org"]))
bullets([
    "Collected, cleaned, and validated ecological field datasets using Python, R, and QGIS, "
    "resolving missing records and inconsistent entries ahead of analysis.",
])

# ── Projects ──────────────────────────────────────────────────────────────
sec("Projects")

header_row("AlertReck: Edge AI Ranger Alert System — Final Year Capstone",
           "2025 – 2026")
story.append(Paragraph(
    "Python · PyTorch · ONNX · Edge AI · Raspberry Pi · "
    "<link href='https://github.com/mangaorphy/alertreck' "
    f"color='{link}'>GitHub</link>", styles["Org"]))
bullets([
    "Built an offline edge-AI acoustic monitoring system on Raspberry Pi that detects "
    "poaching-related sounds and sends GPS-tagged SMS alerts to rangers with no internet "
    "connectivity required.",

    "Curated and annotated <b>11,333 acoustic recordings across seven classes</b>, building the "
    "preprocessing, segmentation, and metadata workflows behind the training set.",

    "Benchmarked five models across four learning paradigms and selected a lightweight CNN "
    "reaching <b>82.6% test accuracy, 0.807 macro-F1, and 0.976 macro-AUC</b> in a 4.6 MB "
    "deployment artifact.",

    "Traced and fixed a train/test data-leakage defect that had <b>inflated reported accuracy by "
    "roughly 10 percentage points</b>, restoring a trustworthy evaluation of the final system.",
])

header_row("Savanna Acoustic Threat Detection — Reinforcement Learning", "2025")
story.append(Paragraph(
    "Python · Stable-Baselines3 · Gymnasium · PyTorch · "
    "<link href='https://github.com/mangaorphy/orpheus_reinforcement_learning_summative' "
    f"color='{link}'>GitHub</link>", styles["Org"]))
bullets([
    "Designed a custom Gymnasium environment simulating a ranger drone navigating a 20×20 "
    "savanna grid, with an 847-dimensional observation space and a shaped reward function.",

    "Trained and compared four RL algorithms (DQN, PPO, A2C, REINFORCE) across <b>40 "
    "hyperparameter-swept runs</b>, with DQN reaching the best mean reward of 50.5.",
])

header_row("UNSW Predators: Wildlife Camera-Trap Dataset Study", "2025")
story.append(Paragraph(
    "Python · Computer Vision · Data Curation · "
    "<link href='https://github.com/mangaorphy/UNSW-Predators' "
    f"color='{link}'>GitHub</link>", styles["Org"]))
bullets([
    "Curated and validated a <b>131,802-image</b> camera-trap dataset across five classes, "
    "auditing category assignments and building a stratified sample for quality assessment.",

    "Quantified severe class imbalance and documented its distorting effect on per-class "
    "evaluation metrics.",
])

# ── Publications & Presentations ─────────────────────────────────────────
sec("Publications &amp; Presentations")
header_row("<i>Vector-Free Salience versus Local Dense Retrieval for Grounded Longitudinal "
           "Clinical Summarisation</i>", "2026")
story.append(Paragraph(
    "<b>Africa at NeurIPS 2026</b> — Accepted · Co-author, Rizivo Research Lab, ALU",
    styles["Org"]))
header_row("AlertReck: Offline Edge-AI Acoustic Monitoring for Anti-Poaching Ranger Alerting",
           "2026")
story.append(Paragraph(
    "<b>ICAAD 2026</b>, International Conference on AI Across Disciplines (Selçuk University) — "
    "Presented; publication pending · "
    "<link href='https://drive.google.com/file/d/12fzP3FC_-jBf58P1yescFaop47kHfQfI/view?usp=sharing' "
    f"color='{link}'>Certificate</link>",
    styles["Org"]))

# ── Education ─────────────────────────────────────────────────────────────
sec("Education")
header_row("African Leadership University – Kigali, Rwanda",
           "September 2023 – August 2026")
story.append(Paragraph(
    "B.Sc. Software Engineering, Machine Learning Specialization. CGPA 4.41 / 5.0. Final-year "
    "requirements completed; capstone defended; graduation pending.",
    styles["Org"]))
story.append(Paragraph(
    "<i>Relevant Coursework:</i> Machine Learning; Deep Learning; Reinforcement Learning; "
    "Computer Vision; Data Science &amp; Analytics; Statistics &amp; Probability; "
    "Linear Algebra &amp; Calculus for Machine Learning.",
    styles["Course"]))
story.append(Paragraph(
    "<i>Capstone Thesis:</i> AlertReck — Offline Edge-AI Acoustic Monitoring for Anti-Poaching "
    "Ranger Alerting. Presented at <b>ICAAD 2026</b>.",
    styles["Course"]))

# ── Skills ────────────────────────────────────────────────────────────────
sec("Technical Skills")
for cat, items in [
    ("Languages",
     "Python · SQL · R · C/C++ (Arduino) · JavaScript"),

    ("Machine Learning",
     "PyTorch · TensorFlow · scikit-learn · Hugging Face Transformers · LoRA / PEFT · "
     "RAG · Stable-Baselines3 · Gymnasium · CNNs · Reinforcement Learning (DQN/PPO/A2C)"),

    ("Geospatial",
     "ArcGIS Online · QGIS · EarthRanger · GeoPandas · Spatial analysis · "
     "Animal movement analysis · Feature digitisation · Cartography &amp; dashboards"),

    ("Data &amp; Analysis",
     "Pandas · NumPy · OpenCV · librosa · Dataset curation · Annotation guidelines · "
     "Label auditing · Leakage detection · Reproducible pipelines"),

    ("Backend &amp; Deployment",
     "FastAPI · Django · Flask · REST APIs · ONNX · Docker · Git/GitHub · Raspberry Pi · "
     "Arduino · Edge deployment"),

    ("Spoken Languages",
     "English (fluent) · Shona (native)"),
]:
    story.append(Paragraph(f"<b>{cat}:</b> {items}", styles["Body"]))

# ── Volunteering ──────────────────────────────────────────────────────────
sec("Volunteering")

header_row("Robotics Mentor &amp; National Competition Judge", "January 2024 – December 2025")
story.append(Paragraph(
    "Rwanda Basic Education Board (FIRST LEGO League) – Nyagatare District, Rwanda",
    styles["Org"]))
bullets([
    "Trained <b>30+ students</b> from two schools in LEGO Mindstorms programming and innovation "
    "project research over two seasons, most of them first-time coders in a low-resource setting.",

    "Coached one school to <b>1st place in its province, 5th place nationally, and a national "
    "award</b>, using a rotating-role model so every student built, programmed, researched, and "
    "presented.",

    "Invited to <b>judge at the FIRST LEGO League national competition</b>, assessing robot "
    "performance, innovation projects, and presentations.",
])

header_row("Volunteer Data Collector &amp; Event Organiser", "2024")
story.append(Paragraph("Africa Food Systems Forum – Kigali, Rwanda", styles["Org"]))
bullets([
    "Collected and checked participant data for the organisers' reporting, and supported "
    "logistics and attendance tracking at a large international forum.",
])

# ── Certifications & Achievements ────────────────────────────────────────
sec("Certifications &amp; Achievements")
cert_link = ("https://docs.google.com/document/d/"
             "1XNwPcwZGOOx0-MODADeU-OQYLDkjSc-jpYnrXSEOOZM/edit?usp=sharing")
story.append(Paragraph(
    "<b>3rd Place — CodeXtreme 2026 National Hackathon</b> (Team TerraFoma).",
    styles["Body"]))
for c, url in [
    ("Mathematics for Machine Learning &amp; Data Science Specialization — DeepLearning.AI "
     "(Linear Algebra, Calculus, Probability &amp; Statistics)",
     "https://coursera.org/share/49a89e1c8ca847ce4ad324cb789abb65"),
    ("Neural Networks &amp; Deep Learning — DeepLearning.AI", cert_link),
    ("Meta Back-End Developer Professional Certificate",
     "https://coursera.org/share/51ddb4cc8987d48eddd9339a53120bf2"),
]:
    story.append(Paragraph(
        f"<link href='{url}' color='{link}'>{c}</link>", styles["Body"]))

doc.build(story)
print(f"PDF generated: {file_name}")
