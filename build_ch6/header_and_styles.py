# -*- coding: utf-8 -*-
"""
Header and Styles for Class 8 Science Chapter 6:
Pressure, Winds, Storms, and Cyclones (NCERT NEP code: hecu106)
"""

def get_header_and_styles():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Exhaustive Master Study Notes for Class 8 Science Chapter 6: Pressure, Winds, Storms, and Cyclones (NCERT NEP hecu106). Zero-omission theory, bilingual glossary, hydrostatic depth laws, 100% solved activities & exercises, exam bank, and interactive diagrams.">
  <title>Pressure, Winds, Storms, and Cyclones - Class 8 Science Chapter 6 Master Study Notes | Sujit Classes</title>

  <!-- Google Fonts: Space Grotesk, Plus Jakarta Sans, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Space+Grotesk:wght@500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">

  <!-- Font Awesome Icons -->
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
      --accent-storm: #d97706;
      --accent-storm-dark: #b45309;
      --accent-storm-light: #fef3c7;
      --accent-lightning: #7c3aed;
      --accent-lightning-dark: #6d28d9;
      --accent-lightning-light: #ede9fe;
      --accent-danger: #dc2626;
      --accent-danger-light: #fee2e2;
      --accent-success: #16a34a;
      --accent-success-light: #dcfce7;
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
      --ease-spring: cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
      font-size: 16px;
    }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: #f1f5f9;
      color: var(--text);
      line-height: 1.7;
      -webkit-font-smoothing: antialiased;
    }

    /* Fixed Top Reading Progress Bar */
    .reading-progress-bar {
      position: fixed;
      top: 0;
      left: 0;
      width: 0%;
      height: 4px;
      background: linear-gradient(90deg, #0284c7, #0d9488, #7c3aed, #d97706);
      z-index: 1000;
      transition: width 0.1s ease-out;
      box-shadow: 0 0 8px rgba(2, 132, 199, 0.5);
    }

    /* Top Navigation Bar */
    .top-nav {
      position: sticky;
      top: 0;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      z-index: 990;
      padding: 0.75rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
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
      font-size: 1.15rem;
    }

    .nav-brand i {
      color: var(--primary);
      font-size: 1.35rem;
    }

    .nav-links {
      display: flex;
      gap: 0.5rem;
      align-items: center;
      flex-wrap: wrap;
    }

    .nav-link {
      text-decoration: none;
      color: var(--text-muted);
      font-size: 0.85rem;
      font-weight: 600;
      padding: 0.4rem 0.75rem;
      border-radius: var(--radius-sm);
      transition: all 0.2s ease;
    }

    .nav-link:hover {
      color: var(--primary);
      background: var(--primary-ultra-light);
    }

    .nav-controls {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .control-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: var(--light);
      border: 1px solid var(--border);
      padding: 0.4rem 0.85rem;
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--dark);
      cursor: pointer;
      transition: all 0.2s ease;
      text-decoration: none;
    }

    .control-btn:hover {
      background: var(--primary-light);
      color: var(--primary-dark);
      border-color: var(--primary);
    }

    /* Hero Banner */
    .hero-banner {
      background: linear-gradient(135deg, #0f172a 0%, #0369a1 50%, #0d9488 100%);
      color: #ffffff;
      padding: 4rem 1.5rem 3.5rem;
      text-align: center;
      position: relative;
      overflow: hidden;
    }

    .hero-banner::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: radial-gradient(circle at 20% 30%, rgba(255, 255, 255, 0.15) 0%, transparent 40%),
                  radial-gradient(circle at 80% 70%, rgba(124, 58, 237, 0.2) 0%, transparent 50%);
      pointer-events: none;
    }

    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.25);
      padding: 0.4rem 1.25rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      margin-bottom: 1.25rem;
      backdrop-filter: blur(8px);
    }

    .hero-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 2.75rem;
      font-weight: 800;
      line-height: 1.2;
      margin-bottom: 1rem;
      max-width: 950px;
      margin-left: auto;
      margin-right: auto;
      text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
    }

    .hero-sub {
      font-size: 1.15rem;
      max-width: 800px;
      margin: 0 auto 2rem;
      opacity: 0.95;
      line-height: 1.6;
      font-weight: 400;
    }

    .hero-meta {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 1.5rem;
      font-size: 0.9rem;
      font-weight: 600;
      margin-bottom: 2rem;
    }

    .hero-meta span {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: rgba(15, 23, 42, 0.4);
      padding: 0.4rem 0.9rem;
      border-radius: var(--radius-sm);
      border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .hero-actions {
      display: flex;
      justify-content: center;
      gap: 1rem;
      flex-wrap: wrap;
    }

    .audio-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
      background: #ffffff;
      color: #0369a1;
      border: none;
      padding: 0.75rem 1.5rem;
      border-radius: var(--radius-md);
      font-size: 0.95rem;
      font-weight: 700;
      cursor: pointer;
      box-shadow: var(--shadow-md);
      transition: all 0.25s var(--ease-spring);
    }

    .audio-btn:hover {
      transform: translateY(-2px);
      box-shadow: var(--shadow-lg);
      background: #f0f9ff;
    }

    .hero-secondary-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.3);
      color: #ffffff;
      padding: 0.75rem 1.4rem;
      border-radius: var(--radius-md);
      font-size: 0.95rem;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.25s ease;
      backdrop-filter: blur(8px);
    }

    .hero-secondary-btn:hover {
      background: rgba(255, 255, 255, 0.25);
      transform: translateY(-2px);
    }

    /* Main Container */
    .main-container {
      max-width: 1100px;
      margin: 2.5rem auto;
      padding: 0 1.5rem;
    }

    /* Section Architecture */
    .study-section {
      background: var(--surface);
      border-radius: var(--radius-lg);
      padding: 2.5rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border);
    }

    .section-header {
      border-bottom: 2px solid var(--border);
      padding-bottom: 1.25rem;
      margin-bottom: 2rem;
    }

    .section-tag {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--primary);
      margin-bottom: 0.4rem;
      display: inline-block;
    }

    .section-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.85rem;
      font-weight: 800;
      color: var(--dark);
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .section-title i {
      color: var(--primary);
    }

    .section-desc {
      color: var(--text-muted);
      font-size: 1.05rem;
      margin-top: 0.5rem;
    }

    /* Typography & Content */
    h3.subheading {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--dark);
      margin: 2rem 0 1rem;
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }

    h4.topic-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.15rem;
      font-weight: 700;
      color: #1e293b;
      margin: 1.5rem 0 0.75rem;
    }

    p {
      margin-bottom: 1.15rem;
      color: var(--text);
    }

    ul, ol {
      margin: 0 0 1.25rem 1.5rem;
      color: var(--text);
    }

    li {
      margin-bottom: 0.5rem;
    }

    strong {
      color: var(--dark);
    }

    /* Callout Boxes (Pastel) */
    .callout {
      border-radius: var(--radius-md);
      padding: 1.25rem 1.5rem;
      margin: 1.5rem 0;
      border-left: 5px solid;
    }

    .callout-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.05rem;
      font-weight: 700;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    /* Definition */
    .callout-def {
      background-color: var(--primary-ultra-light);
      border-color: var(--primary);
    }
    .callout-def .callout-title {
      color: var(--primary-dark);
    }

    /* Activity */
    .callout-act {
      background-color: var(--secondary-ultra-light);
      border-color: var(--secondary);
    }
    .callout-act .callout-title {
      color: var(--secondary-dark);
    }

    /* PYQ */
    .callout-pyq {
      background-color: var(--accent-storm-light);
      border-color: var(--accent-storm);
    }
    .callout-pyq .callout-title {
      color: var(--accent-storm-dark);
    }

    /* Hack / Memory Trick */
    .callout-hack {
      background-color: var(--accent-lightning-light);
      border-color: var(--accent-lightning);
    }
    .callout-hack .callout-title {
      color: var(--accent-lightning-dark);
    }

    /* Warning / Exam Mistake */
    .callout-warn {
      background-color: var(--accent-danger-light);
      border-color: var(--accent-danger);
    }
    .callout-warn .callout-title {
      color: #991b1b;
    }

    /* Concept Card Grid */
    .concept-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.5rem;
      margin: 1.5rem 0;
    }

    .concept-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 1.5rem;
      transition: all 0.25s ease;
      box-shadow: var(--shadow-sm);
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
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.25rem;
      margin-bottom: 1rem;
    }

    .card-icon.blue { background: var(--primary-light); color: var(--primary); }
    .card-icon.teal { background: var(--secondary-light); color: var(--secondary); }
    .card-icon.amber { background: var(--accent-storm-light); color: var(--accent-storm); }
    .card-icon.purple { background: var(--accent-lightning-light); color: var(--accent-lightning); }
    .card-icon.red { background: var(--accent-danger-light); color: var(--accent-danger); }

    .card-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--dark);
      margin-bottom: 0.5rem;
    }

    /* Responsive SVG Container */
    .svg-container {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 1.5rem;
      margin: 2rem 0;
      box-shadow: var(--shadow-sm);
      text-align: center;
      overflow-x: auto;
    }

    .svg-container svg {
      max-width: 100%;
      height: auto;
      display: block;
      margin: 0 auto;
    }

    .svg-caption {
      font-size: 0.9rem;
      color: var(--text-muted);
      font-weight: 600;
      margin-top: 1rem;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.4rem;
    }

    /* Modern Tables */
    .table-wrapper {
      overflow-x: auto;
      margin: 1.5rem 0;
      border-radius: var(--radius-md);
      border: 1px solid var(--border);
      box-shadow: var(--shadow-sm);
    }

    table.data-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.95rem;
      background: #ffffff;
      text-align: left;
    }

    table.data-table th {
      background: #f8fafc;
      color: var(--dark);
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      padding: 0.85rem 1rem;
      border-bottom: 2px solid var(--border);
      font-size: 0.9rem;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    table.data-table td {
      padding: 0.85rem 1rem;
      border-bottom: 1px solid var(--border);
      color: var(--text);
      vertical-align: top;
    }

    table.data-table tr:last-child td {
      border-bottom: none;
    }

    table.data-table tr:hover td {
      background: #f8fafc;
    }

    .odia-term {
      font-family: 'Segoe UI', 'Kalinga', sans-serif;
      font-weight: 700;
      color: var(--secondary-dark);
      font-size: 1.05rem;
    }

    /* Collapsible Answer Boxes (5-Step Pedagogical Presentation) */
    details.ans-box {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      margin: 1rem 0 1.5rem;
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s ease;
    }

    details.ans-box[open] {
      border-color: var(--primary);
      box-shadow: var(--shadow-md);
    }

    details.ans-box summary {
      padding: 1.15rem 1.4rem;
      background: #f8fafc;
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      font-size: 1.05rem;
      color: var(--dark);
      cursor: pointer;
      list-style: none;
      display: flex;
      justify-content: space-between;
      align-items: center;
      user-select: none;
      transition: background 0.2s ease;
    }

    details.ans-box summary::-webkit-details-marker {
      display: none;
    }

    details.ans-box summary:hover {
      background: var(--primary-ultra-light);
      color: var(--primary-dark);
    }

    details.ans-box summary::after {
      content: '\\f078';
      font-family: 'Font Awesome 6 Free';
      font-weight: 900;
      font-size: 0.85rem;
      color: var(--text-muted);
      transition: transform 0.25s ease;
    }

    details.ans-box[open] summary::after {
      transform: rotate(180deg);
      color: var(--primary);
    }

    .ans-content {
      padding: 1.5rem;
      border-top: 1px solid var(--border);
      background: #ffffff;
    }

    /* 5-Step Structure Inside Answer Boxes */
    .step-box {
      margin-bottom: 1.25rem;
      padding-left: 1.25rem;
      border-left: 3px solid var(--border-dark);
    }

    .step-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 0.95rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 0.35rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .step-box.core { border-color: var(--primary); }
    .step-box.core .step-title { color: var(--primary-dark); }

    .step-box.step { border-color: var(--secondary); }
    .step-box.step .step-title { color: var(--secondary-dark); }

    .step-box.analogy { border-color: var(--accent-storm); }
    .step-box.analogy .step-title { color: var(--accent-storm-dark); }

    .step-box.formula { border-color: var(--accent-lightning); }
    .step-box.formula .step-title { color: var(--accent-lightning-dark); }

    .step-box.pitfall { border-color: var(--accent-danger); }
    .step-box.pitfall .step-title { color: #b91c1c; }

    /* Interactive Quiz Engine (Section 5) */
    .quiz-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 1.5rem;
      margin-bottom: 1.5rem;
      box-shadow: var(--shadow-sm);
    }

    .quiz-q {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--dark);
      margin-bottom: 1rem;
    }

    .quiz-options {
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.75rem;
      margin-bottom: 1rem;
    }

    .quiz-opt {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      padding: 0.85rem 1.15rem;
      border: 1.5px solid var(--border);
      border-radius: var(--radius-sm);
      background: #f8fafc;
      font-size: 0.95rem;
      font-weight: 500;
      color: var(--text);
      cursor: pointer;
      text-align: left;
      transition: all 0.2s ease;
      width: 100%;
    }

    .quiz-opt:hover {
      background: #f1f5f9;
      border-color: var(--border-dark);
    }

    .quiz-opt.correct {
      background: var(--accent-success-light) !important;
      border-color: var(--accent-success) !important;
      color: #14532d !important;
      font-weight: 700;
    }

    .quiz-opt.wrong {
      background: var(--accent-danger-light) !important;
      border-color: var(--accent-danger) !important;
      color: #7f1d1d !important;
      font-weight: 700;
    }

    .quiz-opt:disabled {
      cursor: not-allowed;
    }

    .quiz-feedback {
      display: none;
      padding: 1rem 1.25rem;
      border-radius: var(--radius-sm);
      margin-top: 1rem;
      font-size: 0.92rem;
      line-height: 1.6;
    }

    .quiz-feedback.show {
      display: block;
    }

    .quiz-feedback.success {
      background: var(--accent-success-light);
      border-left: 4px solid var(--accent-success);
      color: #14532d;
    }

    .quiz-feedback.danger {
      background: var(--accent-danger-light);
      border-left: 4px solid var(--accent-danger);
      color: #7f1d1d;
    }

    .quiz-scoreboard {
      background: linear-gradient(135deg, #0284c7, #0d9488);
      color: #ffffff;
      padding: 1.25rem 1.5rem;
      border-radius: var(--radius-md);
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 2rem;
      box-shadow: var(--shadow-md);
    }

    .score-title {
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      font-size: 1.1rem;
    }

    .score-badge {
      font-family: 'JetBrains Mono', monospace;
      font-size: 1.35rem;
      font-weight: 800;
      background: rgba(255, 255, 255, 0.2);
      padding: 0.35rem 1rem;
      border-radius: var(--radius-sm);
    }

    /* Math entity display */
    .math-entity {
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      background: #f1f5f9;
      padding: 0.15rem 0.45rem;
      border-radius: 4px;
      color: var(--primary-dark);
      font-size: 0.92em;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
      .hero-title { font-size: 2rem; }
      .study-section { padding: 1.5rem; }
      .top-nav { flex-direction: column; align-items: stretch; }
      .nav-links { overflow-x: auto; padding-bottom: 0.5rem; }
      .concept-grid { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

  <!-- Fixed Top Reading Progress Bar -->
  <div class="reading-progress-bar" id="readingProgressBar"></div>

  <!-- Top Navigation Bar -->
  <nav class="top-nav">
    <a href="../../index.html" class="nav-brand">
      <i class="fa-solid fa-graduation-cap"></i>
      <span>Sujit Classes</span>
    </a>
    <div class="nav-links">
      <a href="#sec1" class="nav-link">1. Blueprint</a>
      <a href="#sec2" class="nav-link">2. Deep Theory</a>
      <a href="#sec3" class="nav-link">3. Facts &amp; Laws</a>
      <a href="#sec4" class="nav-link">4. NCERT Solved</a>
      <a href="#sec5" class="nav-link">5. Exam Vault</a>
      <a href="#sec6" class="nav-link">6. Traps &amp; Revision</a>
    </div>
    <div class="nav-controls">
      <button class="control-btn" id="navAudioBtn" onclick="toggleAudioReader()">
        <i class="fa-solid fa-volume-high"></i>
        <span>Listen</span>
      </button>
      <a href="../../index.html" class="control-btn">
        <i class="fa-solid fa-house"></i>
        <span>Home</span>
      </a>
    </div>
  </nav>

  <!-- Hero Banner -->
  <header class="hero-banner">
    <div class="hero-badge">
      <i class="fa-solid fa-wind"></i>
      <span>NCERT Grade 8 Science • Chapter 6 • NEP Code: hecu106</span>
    </div>
    <h1 class="hero-title">Pressure, Winds, Storms, and Cyclones</h1>
    <p class="hero-sub">The Complete Zero-Omission Master Study Note: Hydrostatic Depth Dynamics, 101.3 kPa Atmospheric Pressure, Convective Sea &amp; Land Breezes, Bernoulli Roof Lift, Thunderstorm Cloud Electrification, and Tropical Cyclone Mechanics.</p>
    <div class="hero-meta">
      <span><i class="fa-solid fa-book-open"></i> 100% NEP Textbook Coverage</span>
      <span><i class="fa-solid fa-language"></i> 30+ Bilingual Odia Terms</span>
      <span><i class="fa-solid fa-clipboard-check"></i> All In-Text &amp; Back Exercises</span>
      <span><i class="fa-solid fa-list-check"></i> 27+ Exam Vault Questions</span>
      <span><i class="fa-solid fa-layer-group"></i> 6 Intricate Vector Diagrams</span>
    </div>
    <div class="hero-actions">
      <button class="audio-btn" id="heroAudioBtn" onclick="toggleAudioReader()">
        <i class="fa-solid fa-headphones"></i>
        <span>🔊 Listen to Chapter Summary</span>
      </button>
      <a href="#sec4" class="hero-secondary-btn">
        <i class="fa-solid fa-circle-question"></i>
        <span>Jump to NCERT Solutions</span>
      </a>
      <a href="#sec5" class="hero-secondary-btn">
        <i class="fa-solid fa-trophy"></i>
        <span>Interactive Quiz Engine</span>
      </a>
    </div>
  </header>

  <main class="main-container">
'''
