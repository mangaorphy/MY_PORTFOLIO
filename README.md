# MY_PORTFOLIO

Portfolio site and CV sources for Orpheus Mhizha Manga.

**Live site:** https://mangaorphy.github.io/MY_PORTFOLIO/

| Folder | What's in it |
| --- | --- |
| `portfolio/` | The website (single static `index.html`). Only this folder is published, by `.github/workflows/pages.yml`. |
| `master_cv/` | `master_cv.py`, the source of truth for CV content, and the generated PDF. |
| `resumes/` | Targeted résumé variants. |

## Updating the CV on the site

```bash
cd master_cv && python master_cv.py
cp Orpheus_Manga_Mhizha__CV.pdf ../portfolio/Orpheus_Manga_Mhizha_Resume.pdf
```

Then update `portfolio/index.html` to match, commit and push to `main`. The site redeploys automatically.
