from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


file_name = "Orpheus_Manga_Mhizha_Resume.pdf"
doc = SimpleDocTemplate(
    file_name,
    pagesize=letter,
    rightMargin=0.5 * inch,
    leftMargin=0.5 * inch,
    topMargin=0.5 * inch,
    bottomMargin=0.5 * inch,
)

styles = getSampleStyleSheet()
name_color = colors.HexColor("#1f5fbf")
section_color = colors.HexColor("#1f5fbf")
text_color = colors.HexColor("#4a4a4a")
muted_color = colors.HexColor("#7a7a7a")

styles.add(
    ParagraphStyle(
        name="Name",
        fontSize=19,
        leading=21,
        spaceAfter=2,
        fontName="Helvetica-Bold",
        alignment=TA_LEFT,
        textColor=name_color,
    )
)

styles.add(
    ParagraphStyle(
        name="ResumeTitle",
        fontSize=10.5,
        leading=12,
        spaceAfter=8,
        alignment=TA_LEFT,
        fontName="Helvetica-Bold",
        textColor=text_color,
    )
)

styles.add(
    ParagraphStyle(
        name="SidebarLabel",
        fontSize=9.3,
        leading=10.3,
        spaceAfter=1,
        spaceBefore=6,
        alignment=TA_LEFT,
        fontName="Helvetica-Bold",
        textColor=section_color,
    )
)

styles.add(
    ParagraphStyle(
        name="SidebarText",
        fontSize=8.8,
        leading=10,
        spaceAfter=2,
        alignment=TA_LEFT,
        fontName="Helvetica",
        textColor=text_color,
    )
)

styles.add(
    ParagraphStyle(
        name="SidebarCategory",
        fontSize=8.3,
        leading=9.5,
        spaceAfter=0,
        spaceBefore=4,
        alignment=TA_LEFT,
        fontName="Helvetica-Bold",
        textColor=muted_color,
    )
)

styles.add(
    ParagraphStyle(
        name="SectionHeader",
        fontSize=11.5,
        leading=12,
        spaceAfter=2,
        spaceBefore=4,
        fontName="Helvetica-Bold",
        textColor=section_color,
    )
)

styles.add(
    ParagraphStyle(
        name="RoleTitle",
        fontSize=10,
        leading=11,
        spaceAfter=0,
        fontName="Helvetica-Bold",
        textColor=text_color,
    )
)

styles.add(
    ParagraphStyle(
        name="RoleMeta",
        fontSize=8.8,
        leading=10,
        spaceAfter=1.5,
        fontName="Helvetica-Oblique",
        textColor=muted_color,
    )
)

styles.add(
    ParagraphStyle(
        name="Body",
        fontSize=9.5,
        leading=11,
        spaceAfter=2,
        alignment=TA_LEFT,
        fontName="Helvetica",
        textColor=text_color,
    )
)

styles.add(
    ParagraphStyle(
        name="BulletPoint",
        fontSize=9.3,
        leading=10.6,
        spaceAfter=1,
        leftIndent=10,
        fontName="Helvetica",
        textColor=text_color,
    )
)


def add_section(story, title):
    story.append(Paragraph(title, styles["SectionHeader"]))


def add_role(story, title, meta, bullets):
    story.append(Paragraph(title, styles["RoleTitle"]))
    story.append(Paragraph(meta, styles["RoleMeta"]))
    for bullet in bullets:
        story.append(Paragraph(f"• {bullet}", styles["BulletPoint"]))
    story.append(Spacer(1, 0.015 * inch))


main_content = []
sidebar_content = []

# ── Header ──────────────────────────────────────────────────────────────
main_content.append(Paragraph("ORPHEUS MHIZHA MANGA", styles["Name"]))
main_content.append(
    Paragraph(
        "AI/ML Engineer  |  NLP · LLMs · Reinforcement Learning · Computer Vision",
        styles["ResumeTitle"],
    )
)

# ── Summary ──────────────────────────────────────────────────────────────
add_section(main_content, "Summary")
main_content.append(
    Paragraph(
        "Results-driven ML Engineer with production experience deploying NLP and LLM systems across "
        "healthcare, AgriTech, and talent acquisition. Fine-tuned transformer models (LoRA/PEFT) achieving "
        "<b>92% classification accuracy</b>; built FastAPI inference pipelines serving real-time predictions "
        "at sub-200ms latency. Research background in privacy-preserving AI and synthetic data generation "
        "for low-resource African clinical settings.",
        styles["Body"],
    )
)

# ── Experience ───────────────────────────────────────────────────────────
add_section(main_content, "Experience")

roles = [
    {
        "title": "Research Assistant | Rizivo Research Lab, African Leadership University",
        "meta": "Jan 2026 – Present  ·  Kigali, Rwanda",
        "bullets": [
            "Engineered a transformer-based NER pipeline to detect and redact <b>18 PHI categories</b> from "
            "clinical records, targeting HIPAA/GDPR-aligned compliance for African healthcare systems.",
            "Designed an LLM-driven <b>synthetic data generation pipeline</b> for low-resource African clinical "
            "contexts using agent-based de-identification — targeting a <b>peer-reviewed publication in 2026</b>.",
        ],
    },
    {
        "title": "AI Developer Intern | ThinkGreen Africa",
        "meta": "Aug 2025 – Dec 2025  ·  Remote",
        "bullets": [
            "Fine-tuned a <b>LLaMA/Mistral-based resume ranking model using LoRA (PEFT)</b>, achieving "
            "<b>92% accuracy</b> and reducing recruiter screening time by <b>40%</b>.",
            "Deployed a <b>FastAPI inference service</b> for real-time candidate classification in production, "
            "maintaining &lt;200ms latency; built end-to-end ML pipeline improving throughput by <b>3×</b>.",
        ],
    },
    {
        "title": "Backend Developer Intern | Beam Social Hub",
        "meta": "Jan 2025 – Apr 2025  ·  Kenya (Remote)",
        "bullets": [
            "Built a real-time event notification system using Node.js and MongoDB change streams, "
            "increasing user engagement by <b>35%</b> and email open rates by <b>28%</b>.",
        ],
    },
]

for role in roles:
    add_role(main_content, role["title"], role["meta"], role["bullets"])

# ── Projects ─────────────────────────────────────────────────────────────
add_section(main_content, "Projects")

projects = [
    {
        "title": "Savanna Acoustic Threat Detection  ·  RL Summative",
        "meta": "Python · Stable Baselines3 · Gymnasium · PyTorch · OpenGL  |  Reinforcement Learning",
        "bullets": [
            "Built a custom <b>Gymnasium environment</b> (847-dim obs, 7 discrete actions) modelling a "
            "20×20 African savanna grid; trained and compared <b>DQN, PPO, A2C, and REINFORCE</b> across "
            "40 hyperparameter sweeps (100k steps each) on Kaggle GPU.",
            "<b>DQN best_tuned achieved mean reward 50.53</b> (±12.37) — 3% above PPO — driven by experience "
            "replay and soft target updates (τ=0.05); implemented OpenGL 3D renderer for live agent visualization.",
        ],
    },
    {
        "title": "Legal Case Summarization  ·  LoRA Fine-tuned Gemma-2B",
        "meta": "Python · Hugging Face · PEFT/LoRA · BitsAndBytes · Gradio  |  LLMs · Deployed",
        "bullets": [
            "Fine-tuned <b>Google Gemma-2B</b> on 4,000 legal judgments using <b>LoRA (r=16)</b> with "
            "4-bit NF4 quantization; achieved <b>BERTScore F1 = 0.79</b> and <b>+2.98% ROUGE improvement</b> "
            "over zero-shot baseline with only ~20M trainable parameters.",
            "Deployed interactive demo to <b>HuggingFace Spaces</b> (Gradio) with real-time summarization, "
            "input validation, and performance metrics dashboard.",
        ],
    },
    {
        "title": "Acoustic Threat Classification  ·  AudioSet Pipeline",
        "meta": "Python · PyTorch · yt-dlp · ffmpeg · AudioSet  |  Audio ML · Dataset Curation",
        "bullets": [
            "Curated and labelled a <b>6,734-sample audio dataset</b> across 8 threat classes (gunshot, "
            "chainsaw, human voice, dog bark, wildlife, ambient) for conservation-focused audio classification, "
            "sourcing from AudioSet and AWS S3.",
        ],
    },
]

for project in projects:
    add_role(main_content, project["title"], project["meta"], project["bullets"])

# ── Education ─────────────────────────────────────────────────────────────
add_section(main_content, "Education")
main_content.append(
    Paragraph(
        "African Leadership University | B.Sc. Software Engineering, Machine Learning Specialization",
        styles["RoleTitle"],
    )
)
main_content.append(
    Paragraph("Kigali, Rwanda  ·  Expected Aug 2026  ·  CGPA: <b>4.41 / 5.0</b>", styles["RoleMeta"])
)
main_content.append(
    Paragraph(
        "Coursework: Machine Learning Pipelines & Techniques · Mathematics for ML · "
        "Data Structures & Algorithms · Database Systems",
        styles["Body"],
    )
)

# ── Sidebar ───────────────────────────────────────────────────────────────
sidebar_content.append(Paragraph("Contact", styles["SidebarLabel"]))
sidebar_content.append(Paragraph("Kigali, Rwanda", styles["SidebarText"]))
sidebar_content.append(Paragraph("+250 792 957 530", styles["SidebarText"]))
sidebar_content.append(
    Paragraph(
        "<link href='mailto:o.manga@alustudent.com' color='#0b57d0'>o.manga@alustudent.com</link>",
        styles["SidebarText"],
    )
)

sidebar_content.append(Paragraph("Links", styles["SidebarLabel"]))
sidebar_content.append(
    Paragraph(
        "<link href='https://www.linkedin.com/in/orpheus-manga-13ab76290/' color='#0b57d0'>LinkedIn</link>",
        styles["SidebarText"],
    )
)
sidebar_content.append(
    Paragraph(
        "<link href='https://github.com/mangaorphy' color='#0b57d0'>GitHub</link>",
        styles["SidebarText"],
    )
)

sidebar_content.append(Paragraph("Skills", styles["SidebarLabel"]))

skill_groups = [
    ("ML / Deep Learning", "PyTorch · TensorFlow\nscikit-learn · PEFT/LoRA\nHugging Face Transformers"),
    ("NLP / LLMs", "LLM Fine-Tuning · RAG\nText Classification · NER\nRLHF · Prompt Engineering"),
    ("RL / Audio ML", "Stable Baselines3 · PPO\nDQN · A2C · Gymnasium\nOpenCV · PyAudio"),
    ("MLOps", "FastAPI · Docker · GCP\nWeights & Biases · MLflow"),
    ("Data", "Pandas · NumPy · spaCy\nSynthetic Data Generation"),
    ("Backend / DB", "Python · Django · Node.js\nMongoDB · PostgreSQL · Git"),
]

for category, items in skill_groups:
    sidebar_content.append(Paragraph(category, styles["SidebarCategory"]))
    sidebar_content.append(Paragraph(items, styles["SidebarText"]))

sidebar_content.append(Paragraph("Achievements", styles["SidebarLabel"]))
sidebar_content.append(
    Paragraph(
        "<b>3rd Place — CodeXtreme 2026</b> (Team TerraFoma): AI-powered solution built under "
        "24-hour competitive constraints.",
        styles["SidebarText"],
    )
)

sidebar_content.append(Paragraph("Certifications", styles["SidebarLabel"]))
certs = [
    "Neural Networks & Deep Learning — DeepLearning.AI",
    "Linear Algebra for ML — DeepLearning.AI",
    "Meta Backend Professional Certificate",
    "IBM Flutter & Dart Development",
]
for cert in certs:
    sidebar_content.append(Paragraph(cert, styles["SidebarText"]))

# ── Layout ────────────────────────────────────────────────────────────────
layout = Table(
    [[main_content, sidebar_content]],
    colWidths=[4.95 * inch, 1.85 * inch],
)
layout.setStyle(
    TableStyle(
        [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ("LEFTPADDING", (1, 0), (1, 0), 12),
        ]
    )
)

doc.build([layout])
print(f"PDF generated: {file_name}")
