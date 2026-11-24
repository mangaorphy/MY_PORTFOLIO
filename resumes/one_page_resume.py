from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

file_name = "Orpheus_Manga_Mhizha_Resume_Econet.pdf"

MARGIN    = 0.45 * inch
MAIN_W    = 5.05 * inch
SIDEBAR_W = 1.75 * inch

doc = SimpleDocTemplate(
    file_name,
    pagesize=letter,
    rightMargin=MARGIN, leftMargin=MARGIN,
    topMargin=MARGIN,   bottomMargin=MARGIN,
)

name_color    = colors.HexColor("#15397a")   # Econet navy
section_color = colors.HexColor("#15397a")
text_color    = colors.HexColor("#1e1e1e")
muted_color   = colors.HexColor("#5a5a5a")
link_color    = colors.HexColor("#15397a")

styles = getSampleStyleSheet()

def S(name, **kw):
    styles.add(ParagraphStyle(name=name, **kw))

S("CVName",    fontSize=19,   leading=21,   spaceAfter=1,
               fontName="Times-Bold", alignment=TA_LEFT, textColor=name_color)
S("CVTitle",   fontSize=10.5, leading=12,   spaceAfter=5,
               fontName="Times-Bold", alignment=TA_LEFT, textColor=text_color)
S("CVSec",     fontSize=10.8, leading=12,   spaceAfter=3, spaceBefore=8,
               fontName="Times-Bold", textColor=section_color)
S("CVRole",    fontSize=10,   leading=11.5, spaceAfter=1,
               fontName="Times-Bold", textColor=text_color)
S("CVMeta",    fontSize=8.8,  leading=10,   spaceAfter=2,
               fontName="Times-Italic", textColor=muted_color)
S("CVBody",    fontSize=9.5,  leading=12.5, spaceAfter=3,
               fontName="Times-Roman", alignment=TA_JUSTIFY, textColor=text_color)
S("CVBullet",  fontSize=9.5,  leading=12.5, spaceAfter=2.5, leftIndent=8,
               fontName="Times-Roman", alignment=TA_JUSTIFY, textColor=text_color)
S("SideLabel", fontSize=9.5,  leading=10.5, spaceAfter=2,  spaceBefore=9,
               fontName="Times-Bold", textColor=section_color)
S("SideText",  fontSize=8.8,  leading=10.8, spaceAfter=2.5,
               fontName="Times-Roman", textColor=text_color)
S("SideCat",   fontSize=8.3,  leading=9.5,  spaceAfter=0.5, spaceBefore=5,
               fontName="Times-Bold", textColor=muted_color)

def sec(t):
    return Paragraph(t, styles["CVSec"])

def role(col, title, meta, bullets):
    col.append(Paragraph(title, styles["CVRole"]))
    col.append(Paragraph(meta,  styles["CVMeta"]))
    for b in bullets:
        col.append(Paragraph(f"• {b}", styles["CVBullet"]))
    col.append(Spacer(1, 0.05 * inch))

# ══════════════════════════════════════════════════════════════════════════
# MAIN COLUMN
# ══════════════════════════════════════════════════════════════════════════
main = []

main.append(Paragraph("ORPHEUS MHIZHA MANGA", styles["CVName"]))
main.append(Paragraph(
    "AI/ML Engineer  |  Deep Learning · NLP · LLMs · Edge AI · Production Deployment",
    styles["CVTitle"],
))

# ── Summary ───────────────────────────────────────────────────────────────
main.append(sec("Summary"))
main.append(Paragraph(
    "AI/ML Engineer who designs, builds, and <b>deploys AI solutions that drive real impact</b>, "
    "from fine-tuning large language models to shipping deep-learning systems on edge hardware. "
    "Hands-on with <b>Python, PyTorch, TensorFlow</b>, RAG/LLM pipelines, and scalable APIs, "
    "with a proven track record taking models from research to production.",
    styles["CVBody"],
))

# ── Experience ────────────────────────────────────────────────────────────
main.append(sec("Experience"))

role(main,
    "AI/ML Engineer | Alertreck: Edge-AI Anti-Poaching System  ·  github.com/mangaorphy/alertreck",
    "2025 – 2026  ·  Lead Engineer (Capstone Project)",
    [
        "Designed, trained, and <b>deployed a custom CNN (92.64% accuracy)</b> for real-time "
        "acoustic threat detection (gunshots, chainsaws, vehicles, human voices), running fully "
        "offline on <b>Raspberry Pi 4</b> via <b>ONNX Runtime</b> CPU inference.",
        "Ran a <b>comparative study of 5 models across 4 ML paradigms</b> (CNN, ProtoNet few-shot, "
        "Wav2Vec2 transfer learning, Conv-AE, One-Class SVM) on 7,900+ labelled audio files, "
        "achieving F1 ≥ 0.997 on gunshot detection.",
        "Built end-to-end edge pipeline: onset-triggered inference, EBU R128 audio normalization, "
        "GPS-tagged <b>SMS alerting via SIM808 GSM module</b>, and a Flask <b>Grad-CAM "
        "explainability dashboard</b>.",
    ],
)
role(main,
    "Research Assistant | Rizivo Research Lab, African Leadership University",
    "Jan 2026 – Present  ·  Kigali, Rwanda",
    [
        "Engineered a <b>transformer-based NER pipeline</b> to detect and redact 18 PHI categories "
        "from clinical records; designing an LLM-driven synthetic data generator targeting "
        "a peer-reviewed publication in 2026.",
    ],
)
role(main,
    "AI Developer Intern | ThinkGreen Africa",
    "Aug – Dec 2025  ·  Remote",
    [
        "Fine-tuned a <b>LLaMA/Mistral model with LoRA (PEFT)</b> to <b>92% accuracy</b> and "
        "deployed a <b>FastAPI inference service</b> at &lt;200ms latency, improving throughput 3×.",
    ],
)
role(main,
    "Data Research Intern | Shangani Holistic (OGRC)",
    "2025  ·  Shangani, Zimbabwe",
    [
        "Analyzed wildlife population and ecological data using <b>R and QGIS</b> to support "
        "anti-poaching strategies and conservation planning, with field data collection at the "
        "human-wildlife-environment interface.",
    ],
)

# ── Projects ──────────────────────────────────────────────────────────────
main.append(sec("Projects"))

role(main,
    "LexRwanda: AI Legal Assistant (RAG)  ·  github.com/mangaorphy/LexRwanda",
    "Python · FastAPI · ChromaDB · Claude · Next.js · Vercel/Render  |  LLMs · RAG · Deployed",
    [
        "Built a production <b>Retrieval-Augmented Generation</b> system giving Rwandan citizens "
        "plain-language answers about their legal rights, grounded in 200+ indexed constitutional "
        "articles via semantic search (bge embeddings) and <b>Claude</b>; deployed full-stack with "
        "streaming responses, source citations, and confidence scoring.",
    ],
)
role(main,
    "Legal Case Summarization  ·  LoRA Fine-tuned Gemma-2B",
    "Python · Hugging Face · PEFT/LoRA · BitsAndBytes · Gradio  |  LLM Fine-Tuning",
    [
        "Fine-tuned <b>Google Gemma-2B</b> on 4,000 legal judgments using LoRA (4-bit NF4); "
        "achieved <b>BERTScore F1 = 0.79</b> and deployed a live demo on HuggingFace Spaces.",
    ],
)
# ── Education ─────────────────────────────────────────────────────────────
main.append(sec("Education"))
main.append(Paragraph(
    "African Leadership University | B.Sc. Software Engineering, ML Specialization",
    styles["CVRole"],
))
main.append(Paragraph(
    "Kigali, Rwanda  ·  Expected Aug 2026  ·  CGPA: <b>4.41 / 5.0</b>",
    styles["CVMeta"],
))

# ══════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════════════════
side = []

side.append(Paragraph("Contact", styles["SideLabel"]))
side.append(Paragraph("Kigali, Rwanda", styles["SideText"]))
side.append(Paragraph("+250 792 957 530", styles["SideText"]))
side.append(Paragraph(
    "<link href='mailto:o.manga@alustudent.com' color='#15397a'>o.manga@alustudent.com</link>",
    styles["SideText"],
))

side.append(Paragraph("Links", styles["SideLabel"]))
side.append(Paragraph(
    "<link href='https://mangaorphy.github.io/MY_PORTFOLIO/' color='#15397a'>Portfolio</link>",
    styles["SideText"],
))
side.append(Paragraph(
    "<link href='https://www.linkedin.com/in/orpheus-manga-13ab76290/' color='#15397a'>LinkedIn</link>",
    styles["SideText"],
))
side.append(Paragraph(
    "<link href='https://github.com/mangaorphy' color='#15397a'>GitHub</link>",
    styles["SideText"],
))

side.append(Paragraph("Skills", styles["SideLabel"]))
for cat, items in [
    ("Languages",       "Python · SQL · Bash · R"),
    ("Deep Learning",   "PyTorch · TensorFlow\nONNX · scikit-learn\nCNNs · Transformers"),
    ("NLP / LLMs",      "LLM Fine-Tuning · LoRA/PEFT\nRAG · NER · Hugging Face\nChromaDB · Claude API"),
    ("Edge / RL",       "Raspberry Pi · ONNX\nStable Baselines3\nDQN · PPO · librosa"),
    ("MLOps / Deploy",  "FastAPI · Docker · GCP\nGit · CI/CD · Flask"),
    ("Data / Analysis", "Pandas · NumPy · spaCy\nStatistical Modeling"),
]:
    side.append(Paragraph(cat,   styles["SideCat"]))
    side.append(Paragraph(items, styles["SideText"]))

side.append(Paragraph("Achievements", styles["SideLabel"]))
side.append(Paragraph(
    "<b>3rd Place, CodeXtreme 2026</b> (Team TerraFoma): AI solution under 24-hour constraints.",
    styles["SideText"],
))

side.append(Paragraph("Certifications", styles["SideLabel"]))
cert_link = "https://docs.google.com/document/d/1XNwPcwZGOOx0-MODADeU-OQYLDkjSc-jpYnrXSEOOZM/edit?usp=sharing"
for c in [
    "Neural Networks & Deep Learning (DeepLearning.AI)",
    "Linear Algebra for ML (DeepLearning.AI)",
    "Meta Backend Professional Certificate",
]:
    side.append(Paragraph(
        f"<link href='{cert_link}' color='#15397a'>{c}</link>",
        styles["SideText"],
    ))

# ══════════════════════════════════════════════════════════════════════════
# BUILD
# ══════════════════════════════════════════════════════════════════════════
layout = Table(
    [[main, side]],
    colWidths=[MAIN_W, SIDEBAR_W],
)
layout.setStyle(TableStyle([
    ("VALIGN",        (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING",   (0, 0), (-1, -1), 0),
    ("RIGHTPADDING",  (0, 0), (-1, -1), 0),
    ("TOPPADDING",    (0, 0), (-1, -1), 0),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ("LEFTPADDING",   (1, 0), (1, 0),   10),
]))

doc.build([layout])
print(f"PDF generated: {file_name}")
