# Sujit Classes Study Portal - AI Assistant Guidelines

## 1. Project Overview & Hosting
- **Target Audience:** Young school students (Classes 6 to 10) in Odisha, studying in English Medium (CBSE) and Odia Medium (BSE).
- **Core Goal:** Make learning effortless, crystal-clear, and enjoyable.
- **Repository Paths:**
  - English Medium: `english/classX/`
  - Odia Medium: `odia/classX/`
- **Main Portal File:** `index.html`

---

## 2. STRICT Student-Friendly Language & Explanation Rules
1. **Simple, Everyday English (Grade 6-7 Level):**
   - Strictly avoid difficult, heavy, or decorative words (e.g., do not use words like *melancholic, ornate, benevolent, profound, somber, intricate, encompass*).
   - Use simple, friendly words that a 11-12 year old child uses every day (e.g., use *sad, kind, deep, detailed, include, clear, easy*).
2. **Explain Like a Caring Teacher:**
   - Never just state a fact; explain **WHY** and **HOW** it happens in 1-2 simple, conversational lines.
   - Use short sentences and clean bullet points instead of long paragraphs.
3. **Question & Answer Style (CBSE Topper + Child Friendly):**
   - Answers must be direct, point-wise, and simple to memorise.
   - Highlight the main keyword in **bold**, followed by an easy explanation.
   - For 1-mark and 2-mark questions: 1 to 2 crisp, clear points.
   - For 3-mark and 5-mark questions: Bulleted points with short sub-headings.

---

## 3. Mandatory File & Folder Naming Rules
Always lowercase with hyphens (`-`). Never use spaces or native Odia script in filenames.
- Pattern: `{medium}/class{num}/{prefix}-ch{num}-{slug}.html`
- Common Prefixes: `sci-`, `math-`, `sst-`, `phy-`, `chem-`, `bio-`, `eng-`, `flo-`

---

## 4. Technical Formatting Rules
1. **No LaTeX Math Code:** Never use `$0^\circ$` or `$...$`. Use clean characters: `0°`, `90°N`, `75.8°E`, `1 cm = 500 m`, `×`, `÷`, `⇒`.
2. **No Raw Citation Tags:** Never include `` or internal markers in the visible HTML.
3. **Pastel Callout Boxes:** Use clean pastel boxes for definitions (`callout-def`), activities (`callout-act`), PYQs (`callout-pyq`), memory tricks (`callout-hack`), and mistake warnings (`callout-warn`).
4. **Interactive Features:** Keep `<details class="ans-box">` for collapsible question-answers so students can test themselves.

---

## 5. Automated Workflow for agy
1. Read the source PDF from `pdfs/` (or download it directly from NCERT).
2. Write the complete, comprehensive, but **very simply worded** Master Study Note HTML file.
3. Save the file inside the correct folder (e.g., `english/class6/`, NOT the root folder).
4. Update the `studyMaterials` array in `index.html` with the new entry and set `isLive: true`.
5. Run git commit and push to `origin/main`.



## 6. Depth, Graphics, and Anti-Summarization Guardrails
- **Zero-Omission Rule:** Never condense, cut, or summarize topics, activities, or question banks. The file must serve as a complete, comprehensive classroom teaching replacement for the NCERT textbook.
- **No File Size Ceiling:** There is **NO upper limit on file size**. Prioritize completeness, thorough step-by-step explanations, and rich interactive visuals over keeping file sizes low. Never trim content to meet an arbitrary kilobyte target.
- **Embedded Visuals:** Include full, rich inline responsive `<svg>` diagrams for core geographic, cultural, and historical concepts.
- **Accessible Diction:** Explain all concepts in simple, everyday language that an 11-to-12-year-old student can easily understand on the first read.
- **Full NCERT & CBE Coverage:** Every single in-text prompt, box, activity, and end-of-chapter exercise must be thoroughly solved in simple, point-wise language.


## 7. Interactive UI & Fluid Animation Standards for HTML Notes
Every generated chapter HTML note must incorporate:
1. **Reading Progress Bar (Top-Fixed):**
   - A thin 4px linear gradient progress bar at the very top of the window that fills from 0% to 100% as the reader scrolls.
2. **Interactive Quiz Engine (Section 5):**
   - Render MCQs with clickable button options.
   - Clicking an option must immediately evaluate:
     - Correct option: Turns **Green** with an affirmative icon.
     - Wrong option: Turns **Red** and highlights the correct choice.
   - Displays real-time score counters for students.
3. **Audio Reader (Text-to-Speech):**
   - Add a "🔊 Listen to Summary" button utilizing `window.speechSynthesis` so young students can listen to pronunciation and explanations.
4. **Interactive SVG Micro-Animations:**
   - Include gentle CSS hover effects, glowing lines, or rotating indicator needles inside diagrams.


## 8. 3D Interactive Flipbook Engine Standards
Every chapter study note must include a dual-reading mode toggle: **📖 Flipbook Mode** and **📄 Continuous Scroll Mode**.

### 1. Structure of 3D Flipbook Mode:
- **3D Perspective Container:** Use CSS `perspective: 2500px` and `transform-style: preserve-3d`.
- **Two-Page Book Spread:** 
  - On desktop/tablets (screen width >= 768px): Render an open two-page spread (Left Page + Right Page) on a study desk background.
  - Center crease with realistic ambient binding shadow.
  - Page edges with simulated stacked-paper thickness.
  - On mobile devices (< 768px): Automatically adapt to a single responsive page flip view.
- **Realistic Page Turn Mechanics:**
  - Flipping a page triggers `transform: rotateY(-180deg)` with `transform-origin: left center` on the right page (or `rotateY(180deg)` with `transform-origin: right center` on the left page).
  - Include dynamic moving lighting gradients during the flip animation to simulate the natural curve of heavy book paper.
- **Navigation Controls:**
  - Left ($\leftarrow$) and Right ($\rightarrow$) floating buttons on the screen edges.
  - Keyboard arrow key listeners (`ArrowRight` for next page, `ArrowLeft` for previous page).
  - Touch swipe listener on mobile and tablets.
  - Subtle audio page-turn sound generated natively via the Web Audio API (synthesized paper rustle; zero external audio files needed).
- **Default View:** Allow students to switch back to normal vertical scroll mode anytime via a sticky top toggle button (`📄 Scroll View`).