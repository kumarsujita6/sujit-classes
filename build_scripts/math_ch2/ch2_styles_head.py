# -*- coding: utf-8 -*-
"""
Module: ch2_styles_head.py
Contains HTML head, CSS styles, top navbar, reading progress bar, hero banner, and quick nav pills.
"""

def get_head_and_hero():
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Power Play - Class 8 Mathematics Chapter 2 Master Study Notes (Ganita Prakash) | Sujit Classes</title>
  <meta name="description" content="Exhaustive, zero-omission teacher notes for Class 8 Mathematics Chapter 2: Power Play (NCERT Ganita Prakash NEP 2020 code: hegp102). Features paper folding paradox, laws of exponents, zero & negative powers, scientific standard form, and fully solved questions.">
  <!-- Google Fonts: Space Grotesk, Plus Jakarta Sans, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Space+Grotesk:wght@500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <!-- Font Awesome 6.4.0 -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <style>
    :root {
      --primary: #0284c7;
      --primary-dark: #0369a1;
      --primary-light: #e0f2fe;
      --primary-ultra-light: #f0f9ff;
      --secondary: #0d9488;
      --secondary-dark: #0f766e;
      --secondary-light: #ccfbf1;
      --secondary-ultra-light: #f0fdfa;
      --accent: #f59e0b;
      --accent-dark: #d97706;
      --accent-light: #fef3c7;
      --purple: #7c3aed;
      --purple-dark: #6d28d9;
      --purple-light: #ede9fe;
      --danger: #dc2626;
      --danger-dark: #b91c1c;
      --danger-light: #fee2e2;
      --dark: #0f172a;
      --light: #f8fafc;
      --surface: #ffffff;
      --text: #334155;
      --text-muted: #64748b;
      --border: #e2e8f0;
      --border-dark: #cbd5e1;
      --shadow-sm: 0 1px 3px 0 rgb(0 0 0 / 0.07);
      --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
      --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      --radius-xl: 24px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      background-color: var(--light);
      color: var(--text);
      line-height: 1.7;
      font-size: 1.025rem;
      overflow-x: hidden;
      padding-top: 65px;
    }

    /* READING PROGRESS BAR */
    #progressBarContainer {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 4px;
      background: rgba(226, 232, 240, 0.6);
      z-index: 1001;
    }
    #progressBar {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #0284c7, #0d9488, #7c3aed, #f59e0b);
      transition: width 0.1s ease-out;
    }

    /* STICKY TOP NAVBAR */
    .top-nav {
      position: fixed;
      top: 4px;
      left: 0;
      width: 100%;
      height: 60px;
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 2rem;
      z-index: 1000;
      box-shadow: var(--shadow-sm);
    }
    .nav-brand {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
      color: var(--dark);
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      font-size: 1.25rem;
    }
    .nav-brand i {
      color: var(--primary);
      font-size: 1.35rem;
    }
    .nav-links {
      display: flex;
      align-items: center;
      gap: 1.25rem;
    }
    .nav-link {
      text-decoration: none;
      color: var(--text-muted);
      font-weight: 600;
      font-size: 0.9rem;
      transition: color 0.2s;
    }
    .nav-link:hover {
      color: var(--primary);
    }
    .btn-audio {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: var(--primary-light);
      color: var(--primary-dark);
      border: 1px solid var(--primary);
      padding: 0.4rem 0.9rem;
      border-radius: var(--radius-sm);
      font-weight: 600;
      font-size: 0.85rem;
      cursor: pointer;
      transition: all 0.2s;
    }
    .btn-audio:hover {
      background: var(--primary);
      color: white;
    }

    /* CONTAINER */
    .main-container {
      max-width: 1140px;
      margin: 0 auto;
      padding: 2.5rem 1.5rem 5rem;
    }

    /* HERO BANNER */
    .hero-banner {
      background: linear-gradient(135deg, #0c4a6e 0%, #0284c7 50%, #0f766e 100%);
      color: white;
      border-radius: var(--radius-xl);
      padding: 3.5rem 2.5rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow-xl);
      position: relative;
      overflow: hidden;
    }
    .hero-banner::before {
      content: '';
      position: absolute;
      top: -30%;
      right: -10%;
      width: 440px;
      height: 440px;
      background: radial-gradient(circle, rgba(255,255,255,0.18) 0%, transparent 70%);
      border-radius: 50%;
      pointer-events: none;
    }
    .hero-badges {
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem;
      margin-bottom: 1.25rem;
    }
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.35rem 0.85rem;
      border-radius: 50px;
      font-size: 0.8rem;
      font-weight: 700;
      letter-spacing: 0.03em;
      text-transform: uppercase;
    }
    .badge-nep {
      background: rgba(255, 255, 255, 0.22);
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.4);
    }
    .badge-code {
      background: #f59e0b;
      color: #0f172a;
    }
    .badge-class {
      background: #10b981;
      color: #ffffff;
    }
    .badge-depth {
      background: #8b5cf6;
      color: #ffffff;
    }
    .hero-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 2.6rem;
      font-weight: 800;
      line-height: 1.2;
      margin-bottom: 1rem;
      color: #ffffff;
    }
    .hero-subtitle {
      font-size: 1.15rem;
      max-width: 860px;
      color: rgba(255, 255, 255, 0.94);
      margin-bottom: 1.75rem;
      line-height: 1.6;
    }
    .hero-meta-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 1.25rem;
      border-top: 1px solid rgba(255, 255, 255, 0.2);
      padding-top: 1.5rem;
    }
    .hero-meta-item {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }
    .hero-meta-item i {
      font-size: 1.4rem;
      color: #fde047;
    }
    .meta-label {
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: rgba(255, 255, 255, 0.75);
    }
    .meta-value {
      font-weight: 700;
      font-size: 0.95rem;
    }

    /* AUDIO CONTROLLER BAR */
    .audio-player-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.25rem 1.75rem;
      margin-bottom: 2.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 1rem;
      box-shadow: var(--shadow-sm);
    }
    .audio-info {
      display: flex;
      align-items: center;
      gap: 1rem;
    }
    .audio-icon-pulse {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: var(--primary-light);
      color: var(--primary);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.2rem;
    }
    .audio-title {
      font-weight: 700;
      color: var(--dark);
      font-size: 1rem;
    }
    .audio-desc {
      font-size: 0.85rem;
      color: var(--text-muted);
    }
    .audio-controls {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }
    .btn-tts {
      background: var(--primary);
      color: white;
      border: none;
      padding: 0.55rem 1.25rem;
      border-radius: var(--radius-md);
      font-weight: 700;
      font-size: 0.9rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: background 0.2s, transform 0.1s;
    }
    .btn-tts:hover {
      background: var(--primary-dark);
      transform: translateY(-1px);
    }
    .btn-tts-stop {
      background: var(--danger);
    }
    .btn-tts-stop:hover {
      background: var(--danger-dark);
    }

    /* QUICK NAVIGATION PILLS */
    .quick-nav {
      background: var(--surface);
      border-radius: var(--radius-lg);
      padding: 1.25rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow-sm);
      margin-bottom: 3rem;
    }
    .quick-nav-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 0.9rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .nav-pill-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
      gap: 0.6rem;
    }
    .nav-pill {
      text-decoration: none;
      background: var(--light);
      border: 1px solid var(--border);
      padding: 0.6rem 0.85rem;
      border-radius: var(--radius-sm);
      color: var(--text);
      font-weight: 600;
      font-size: 0.825rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.2s;
    }
    .nav-pill:hover {
      background: var(--primary-light);
      color: var(--primary-dark);
      border-color: var(--primary);
      transform: translateY(-1px);
    }
    .nav-pill i {
      color: var(--primary);
    }

    /* SECTION STYLING */
    .study-section {
      background: var(--surface);
      border-radius: var(--radius-xl);
      border: 1px solid var(--border);
      padding: 3rem 2.25rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow-sm);
      position: relative;
    }
    .section-header {
      border-bottom: 2px solid var(--border);
      padding-bottom: 1.5rem;
      margin-bottom: 2.25rem;
    }
    .section-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.8rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      padding: 0.35rem 0.85rem;
      border-radius: 50px;
      margin-bottom: 0.75rem;
    }
    .section-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 2rem;
      font-weight: 800;
      color: var(--dark);
      line-height: 1.25;
      margin-bottom: 0.5rem;
    }
    .section-subtitle {
      color: var(--text-muted);
      font-size: 1.05rem;
      line-height: 1.6;
    }

    /* SUBHEADINGS */
    .topic-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.45rem;
      font-weight: 700;
      color: var(--dark);
      margin: 2.5rem 0 1rem;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      border-left: 4px solid var(--primary);
      padding-left: 0.75rem;
    }
    .subtopic-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.2rem;
      font-weight: 700;
      color: #1e293b;
      margin: 1.75rem 0 0.75rem;
    }

    /* PARAGRAPHS & LISTS */
    p {
      margin-bottom: 1.25rem;
      color: var(--text);
    }
    ul, ol {
      margin: 0 0 1.5rem 1.5rem;
    }
    li {
      margin-bottom: 0.5rem;
    }

    /* CALLOUT BOXES */
    .callout {
      border-radius: var(--radius-md);
      padding: 1.25rem 1.5rem;
      margin: 1.75rem 0;
      border-left: 5px solid;
      position: relative;
    }
    .callout-title {
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      font-size: 1.05rem;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .callout-def {
      background-color: #f0f9ff;
      border-left-color: #0284c7;
      color: #0369a1;
    }
    .callout-def .callout-title {
      color: #0284c7;
    }
    .callout-act {
      background-color: #f0fdfa;
      border-left-color: #0d9488;
      color: #134e4a;
    }
    .callout-act .callout-title {
      color: #0f766e;
    }
    .callout-pyq {
      background-color: #f5f3ff;
      border-left-color: #7c3aed;
      color: #4c1d95;
    }
    .callout-pyq .callout-title {
      color: #6d28d9;
    }
    .callout-hack {
      background-color: #fffbeb;
      border-left-color: #f59e0b;
      color: #78350f;
    }
    .callout-hack .callout-title {
      color: #b45309;
    }
    .callout-warn {
      background-color: #fef2f2;
      border-left-color: #dc2626;
      color: #7f1d1d;
    }
    .callout-warn .callout-title {
      color: #b91c1c;
    }

    /* CONCEPT CARDS */
    .card-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.25rem;
      margin: 1.75rem 0;
    }
    .concept-card {
      background: var(--light);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 1.5rem;
      transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
    }
    .concept-card:hover {
      transform: translateY(-3px);
      box-shadow: var(--shadow-md);
      border-color: var(--primary-light);
    }
    .card-icon {
      width: 44px;
      height: 44px;
      border-radius: 10px;
      background: var(--primary-light);
      color: var(--primary);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.25rem;
      margin-bottom: 1rem;
    }
    .card-title {
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      font-size: 1.1rem;
      color: var(--dark);
      margin-bottom: 0.5rem;
    }
    .card-text {
      font-size: 0.925rem;
      color: var(--text);
      line-height: 1.6;
    }

    /* TABLES */
    .table-container {
      overflow-x: auto;
      margin: 1.75rem 0;
      border-radius: var(--radius-md);
      border: 1px solid var(--border);
      background: var(--surface);
      box-shadow: var(--shadow-sm);
    }
    table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.95rem;
    }
    thead {
      background: #f1f5f9;
      color: var(--dark);
    }
    th {
      padding: 0.9rem 1rem;
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      border-bottom: 2px solid var(--border);
    }
    td {
      padding: 0.85rem 1rem;
      border-bottom: 1px solid var(--border);
      color: var(--text);
    }
    tr:last-child td {
      border-bottom: none;
    }
    tr:nth-child(even) td {
      background-color: #f8fafc;
    }
    tr:hover td {
      background-color: #f0f9ff;
    }
    .math-font {
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      color: var(--primary-dark);
    }

    /* COLLAPSIBLE ANSWER BOXES (<details>) */
    details.ans-box {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      margin: 1.25rem 0;
      overflow: hidden;
      transition: all 0.2s ease;
      box-shadow: var(--shadow-sm);
    }
    details.ans-box[open] {
      border-color: var(--primary);
      box-shadow: 0 4px 12px rgba(2, 132, 199, 0.12);
    }
    details.ans-box summary {
      padding: 1rem 1.25rem;
      background: #f8fafc;
      font-weight: 700;
      color: var(--dark);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      user-select: none;
      font-family: 'Space Grotesk', sans-serif;
      transition: background 0.2s;
    }
    details.ans-box summary:hover {
      background: #f1f5f9;
      color: var(--primary);
    }
    details.ans-box summary::-webkit-details-marker {
      display: none;
    }
    .ans-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      font-size: 0.75rem;
      padding: 0.25rem 0.6rem;
      background: var(--primary-light);
      color: var(--primary-dark);
      border-radius: 4px;
      font-family: 'Plus Jakarta Sans', sans-serif;
    }
    .ans-content {
      padding: 1.5rem;
      border-top: 1px solid var(--border);
      background: #ffffff;
    }

    /* 5-STEP SOLUTION PRESENTATION */
    .step-box {
      margin: 0.75rem 0;
      padding: 0.85rem 1.1rem;
      border-radius: var(--radius-sm);
      background: #f8fafc;
      border-left: 3px solid var(--primary);
      font-size: 0.95rem;
    }
    .step-label {
      font-weight: 700;
      color: var(--primary-dark);
      text-transform: uppercase;
      font-size: 0.75rem;
      letter-spacing: 0.05em;
      margin-bottom: 0.25rem;
      display: flex;
      align-items: center;
      gap: 0.35rem;
    }

    /* DIAGRAM & SVG STYLING */
    .diagram-wrapper {
      margin: 2.25rem 0;
      padding: 1.75rem;
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-sm);
      text-align: center;
    }
    .diagram-caption {
      margin-top: 1rem;
      font-size: 0.9rem;
      color: var(--text-muted);
      font-weight: 600;
    }
    svg.responsive-svg {
      max-width: 100%;
      height: auto;
      display: block;
      margin: 0 auto;
      transition: all 0.3s ease;
    }

    /* INTERACTIVE QUIZ ENGINE */
    .quiz-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      margin: 1.5rem 0;
      box-shadow: var(--shadow-sm);
    }
    .quiz-question {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--dark);
      margin-bottom: 1rem;
    }
    .quiz-options {
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
      margin-bottom: 1rem;
    }
    .option-btn {
      text-align: left;
      padding: 0.85rem 1.15rem;
      border-radius: var(--radius-md);
      border: 1px solid var(--border);
      background: var(--light);
      color: var(--text);
      font-size: 0.95rem;
      cursor: pointer;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-weight: 500;
      transition: all 0.2s;
    }
    .option-btn:hover {
      background: #f1f5f9;
      border-color: #cbd5e1;
    }
    .option-btn.correct {
      background: #dcfce7 !important;
      border-color: #22c55e !important;
      color: #15803d !important;
      font-weight: 700;
    }
    .option-btn.wrong {
      background: #fee2e2 !important;
      border-color: #ef4444 !important;
      color: #b91c1c !important;
      font-weight: 700;
    }
    .quiz-feedback {
      display: none;
      padding: 0.85rem 1.15rem;
      border-radius: var(--radius-sm);
      font-size: 0.9rem;
      line-height: 1.5;
      margin-top: 0.75rem;
    }

    /* SCORE COUNTER */
    .quiz-scoreboard {
      background: linear-gradient(135deg, #0f172a, #1e293b);
      color: white;
      border-radius: var(--radius-lg);
      padding: 1.25rem 1.75rem;
      margin: 1.75rem 0;
      display: flex;
      align-items: center;
      justify-content: space-between;
      box-shadow: var(--shadow-md);
    }
    .scoreboard-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.1rem;
      font-weight: 700;
    }
    .score-badge {
      font-family: 'JetBrains Mono', monospace;
      font-size: 1.3rem;
      font-weight: 700;
      background: rgba(255, 255, 255, 0.15);
      padding: 0.35rem 0.85rem;
      border-radius: var(--radius-sm);
      color: #38bdf8;
    }

    /* FOOTER */
    .portal-footer {
      background: var(--dark);
      color: white;
      padding: 4rem 1.5rem 2.5rem;
      margin-top: 4rem;
    }
    .footer-inner {
      max-width: 1140px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 2.5rem;
      margin-bottom: 2.5rem;
    }
    .footer-brand {
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      font-size: 1.35rem;
      margin-bottom: 0.75rem;
      color: white;
    }
    .footer-text {
      color: #94a3b8;
      font-size: 0.9rem;
      line-height: 1.6;
    }
    .footer-heading {
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      font-size: 1rem;
      margin-bottom: 1rem;
      color: #f8fafc;
    }
    .footer-links {
      list-style: none;
      margin: 0;
      padding: 0;
    }
    .footer-links li {
      margin-bottom: 0.5rem;
    }
    .footer-links a {
      color: #94a3b8;
      text-decoration: none;
      font-size: 0.875rem;
      transition: color 0.2s;
    }
    .footer-links a:hover {
      color: white;
    }
    .footer-bottom {
      max-width: 1140px;
      margin: 0 auto;
      border-top: 1px solid #334155;
      padding-top: 1.5rem;
      text-align: center;
      color: #64748b;
      font-size: 0.85rem;
    }

    /* BACK TO TOP */
    #backToTopBtn {
      position: fixed;
      bottom: 25px;
      right: 25px;
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: var(--primary);
      color: white;
      border: none;
      box-shadow: var(--shadow-lg);
      cursor: pointer;
      display: none;
      align-items: center;
      justify-content: center;
      font-size: 1.2rem;
      z-index: 999;
      transition: background 0.2s, transform 0.2s;
    }
    #backToTopBtn:hover {
      background: var(--primary-dark);
      transform: translateY(-2px);
    }

    @media (max-width: 768px) {
      .hero-banner { padding: 2rem 1.5rem; }
      .hero-title { font-size: 2rem; }
      .study-section { padding: 2rem 1.25rem; }
      .top-nav { padding: 0 1rem; }
      .nav-links { display: none; }
    }
  </style>
</head>
<body>

  <!-- Top Fixed Reading Progress Bar -->
  <div id="progressBarContainer">
    <div id="progressBar"></div>
  </div>

  <!-- Sticky Top Navbar -->
  <header class="top-nav">
    <a href="../../index.html" class="nav-brand">
      <i class="fa-solid fa-graduation-cap"></i> Sujit Classes
    </a>
    <nav class="nav-links">
      <a href="#section-1" class="nav-link">Mind Map</a>
      <a href="#section-2" class="nav-link">Concepts</a>
      <a href="#section-3" class="nav-link">Law Bank</a>
      <a href="#section-4" class="nav-link">NCERT Solutions</a>
      <a href="#section-5" class="nav-link">Exam Bank</a>
      <a href="#section-6" class="nav-link">Trap Alerts</a>
    </nav>
    <button class="btn-audio" id="topAudioBtn" onclick="toggleAudioReader()">
      <i class="fa-solid fa-volume-high"></i> Listen to Notes
    </button>
  </header>

  <main class="main-container">

    <!-- Hero Banner -->
    <section class="hero-banner">
      <div class="hero-badges">
        <span class="badge badge-nep"><i class="fa-solid fa-book-open"></i> NCERT NEP 2020</span>
        <span class="badge badge-code"><i class="fa-solid fa-hashtag"></i> Code: hegp102</span>
        <span class="badge badge-class"><i class="fa-solid fa-school"></i> Class 8 Mathematics</span>
        <span class="badge badge-depth"><i class="fa-solid fa-award"></i> Master Study Note</span>
      </div>
      <h1 class="hero-title">Chapter 2: Power Play (Exponents & Powers)</h1>
      <p class="hero-subtitle">
        Discover the astonishing universe of exponential growth! Journey from folding a humble sheet of paper that reaches beyond the Moon in 46 folds, to the 7 unbreakable Laws of Exponents, negative powers, powers of 10, combinatorics of secure locks, and standard scientific notation measuring both subatomic particles and the grandest galaxies.
      </p>
      <div class="hero-meta-grid">
        <div class="hero-meta-item">
          <i class="fa-solid fa-layer-group"></i>
          <div>
            <div class="meta-label">Curriculum Edition</div>
            <div class="meta-value">Ganita Prakash (NCERT)</div>
          </div>
        </div>
        <div class="hero-meta-item">
          <i class="fa-solid fa-bolt"></i>
          <div>
            <div class="meta-label">Core Mathematical Theme</div>
            <div class="meta-value">Multiplicative Power vs Linear Additive Growth</div>
          </div>
        </div>
        <div class="hero-meta-item">
          <i class="fa-solid fa-diagram-project"></i>
          <div>
            <div class="meta-label">Visual Architecture</div>
            <div class="meta-value">6 Responsive Vector Diagrams</div>
          </div>
        </div>
        <div class="hero-meta-item">
          <i class="fa-solid fa-clipboard-check"></i>
          <div>
            <div class="meta-label">Pedagogical Coverage</div>
            <div class="meta-value">100% In-Text & Exercises + 27 Exam Models</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Audio Player Card -->
    <div class="audio-player-card">
      <div class="audio-info">
        <div class="audio-icon-pulse">
          <i class="fa-solid fa-headphones-simple"></i>
        </div>
        <div>
          <div class="audio-title">Interactive Audio Voice Reader</div>
          <div class="audio-desc">Listen to chapter summaries, law recitations, and expert teacher tips on demand.</div>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-tts" id="playAudioBtn" onclick="toggleAudioReader()">
          <i class="fa-solid fa-play"></i> Listen to Summary
        </button>
        <button class="btn-tts btn-tts-stop" id="stopAudioBtn" onclick="stopAudioReader()" style="display:none;">
          <i class="fa-solid fa-square"></i> Stop
        </button>
      </div>
    </div>

    <!-- Quick Navigation Pills -->
    <nav class="quick-nav">
      <div class="quick-nav-title">
        <i class="fa-solid fa-compass"></i> Chapter Quick Navigation
      </div>
      <div class="nav-pill-grid">
        <a href="#section-1" class="nav-pill"><i class="fa-solid fa-sitemap"></i> 1. Visual Blueprint</a>
        <a href="#section-2" class="nav-pill"><i class="fa-solid fa-brain"></i> 2. Concept Explanations</a>
        <a href="#glossary" class="nav-pill"><i class="fa-solid fa-language"></i> Bilingual Glossary</a>
        <a href="#section-3" class="nav-pill"><i class="fa-solid fa-table-list"></i> 3. Law & Formula Bank</a>
        <a href="#section-4" class="nav-pill"><i class="fa-solid fa-pen-to-square"></i> 4. Solved NCERT</a>
        <a href="#section-5" class="nav-pill"><i class="fa-solid fa-file-signature"></i> 5. Exam Bank (27 Qs)</a>
        <a href="#section-6" class="nav-pill"><i class="fa-solid fa-triangle-exclamation"></i> 6. Trap Alerts</a>
      </div>
    </nav>
"""
