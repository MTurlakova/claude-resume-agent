# Claude Resume Tailor

A no-extra-cost alternative to AI resume tools — no API key, no additional subscription. If you already have Claude Code, tailoring happens conversationally through a single command, and a Python script handles the formatted `.docx` export.

## How it works

You run a single command (`/resume-tailor`) in Claude Code. Claude analyzes the job description, identifies gaps, asks targeted clarifying questions, and iterates on a draft with you. When you're satisfied, it writes the content to `resume_data.py` and generates a formatted `.docx` — no copy-pasting commands required.

The workflow:
1. Run `/resume-tailor` in Claude Code
2. Provide a job posting (paste text or give a URL) and pick a source resume
3. Answer 3–5 targeted questions about gaps between your resume and the role
4. Review and iterate on the draft
5. Claude generates the `.docx` automatically

## What makes it useful

- **No extra costs** — tailoring runs entirely through the Claude Code conversation, no API key needed
- **Gap-focused questions** — not a generic checklist, but questions specific to this role
- **No fabrication** — Claude only reframes what's actually in your resume
- **Resume library** — save base resume variants and previously tailored versions; no re-pasting each session
- **Clean `.docx` output** — Garamond 11pt, 0.75" margins, formatted for 2 pages

## Setup

**Prerequisites:** [Claude Code](https://claude.ai/code) (requires a paid Claude plan)

```bash
git clone https://github.com/yourusername/claude-resume-agent.git
cd claude-resume-agent
python -m venv venv
source venv/Scripts/activate   # Windows
# source venv/bin/activate     # Mac/Linux
pip install -r requirements.txt
```

**Configure your output folder and contact info:**

```bash
cp resume_data_template.py resume_data.py
```

Open `resume_data.py` and set `OUTPUT_FOLDER` to wherever you want `.docx` files saved, and fill in your contact info.

**Add your resume(s):**

Add plain text versions of your resume(s) to the `resumes/` folder (e.g. `resumes/analytics.txt`, `resumes/general.txt`). See `resumes/example.txt` for the expected format.

## Usage

Open the project in Claude Code and run:

```
/resume-tailor
```

Claude will list your available resumes, ask for the job posting, and guide you through the rest.

## Files

```
resume_data_template.py        # Copy to resume_data.py and fill in your details
generate_resume.py             # Reads resume_data.py, outputs formatted .docx
.claude/commands/resume-tailor.md  # The /resume-tailor command definition
resumes/                       # Your resume variants (gitignored except example.txt)
  example.txt                  # Format reference
  tailored/                    # Auto-saved after each session
```

`resume_data.py` and `resumes/` are gitignored — your personal information stays local.

## Output format

- Font: Garamond 11pt
- Margins: 0.75 inches
- Target length: 2 pages
- File name: `{First Last} Resume - {Company} {Role}.docx`
