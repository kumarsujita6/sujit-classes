\# Sujit Classes Study Portal - AI Guidelines



\## 1. Project Overview \& Hosting

\- \*\*Repository:\*\* Study portal for Classes 6 to 10 (English Medium CBSE \& Odia Medium BSE).

\- \*\*Paths:\*\*

&#x20; - English Medium: `english/classX/`

&#x20; - Odia Medium: `odia/classX/`

\- \*\*Main Portal File:\*\* `index.html`



\## 2. File Naming Rules

Always lowercase with hyphens. No spaces or Odia script in filenames.

\- Pattern: `{medium}/class{num}/{prefix}-ch{num}-{slug}.html`

\- Common Prefixes: `sci-`, `math-`, `sst-`, `phy-`, `chem-`, `bio-`, `eng-`, `flo-`



\## 3. HTML Note Quality Rules

\- Standalone, self-contained HTML (all CSS/JS embedded, clean responsive design).

\- Never use raw LaTeX math dollar signs (`$`). Use standard text/symbols: `0°`, `90°N`, `75.8°E`, `1 cm = 500 m`, `×`, `÷`.

\- Never include raw citation tags (like ``).

\- Use pastel callout boxes (`callout-def`, `callout-act`, `callout-pyq`, `callout-hack`, `callout-warn`).



\## 4. Automation Steps for agy

1\. Read the source PDF from `pdfs/`.

2\. Generate the comprehensive study note following the standard structure.

3\. Save the HTML file in the proper class directory (e.g., `english/class6/`).

4\. Update the `studyMaterials` array in `index.html` with the new chapter metadata and set `isLive: true`.

5\. Run git commit and push changes.

