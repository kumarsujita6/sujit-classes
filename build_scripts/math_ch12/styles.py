# -*- coding: utf-8 -*-
"""
Styles and Head Module for Class 8 Mathematics Chapter 12
Tales by Dots and Lines (NCERT Ganita Prakash Grade 8 Part-II NEP code: hegp112)
"""

def get_head_and_styles():
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tales by Dots and Lines - Class 8 Mathematics Chapter 12 Master Study Notes (Ganita Prakash) | Sujit Classes</title>
  <meta name="description" content="Exhaustive, zero-omission master study notes for Class 8 Mathematics Chapter 12: Tales by Dots and Lines (NCERT Ganita Prakash Grade 8 Part-II NEP code: hegp112). Complete coverage of the physical fulcrum model of arithmetic mean, algebraic proofs of shifting and scaling invariants, sensitivity analysis of mean and median, cumulative frequency distributions, spreadsheet formulas and functions, 2-step line graph interpretation protocol, slope and rate of change, real-world data stories (Kerala vs Punjab climate, space launches, coastal rainfall, 24-hr activity strips, sleep duration curves across age, astronomical solar/lunar cycles), game of Hex topology, and 100% solved textbook exercises.">
  <!-- Google Fonts: Space Grotesk, Plus Jakarta Sans, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Space+Grotesk:wght@500;600;700;800&display=swap" rel="stylesheet">
  <!-- Font Awesome 6.5.0 Free CDN -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

  <style>
    /* ==========================================================
       CSS VARIABLES & THEME DEFINITIONS
       ========================================================== */
    :root {
      --primary: #0284c7;         /* Sky Blue 600 - Data & Lines Core */
      --primary-light: #38bdf8;   /* Sky 400 */
      --primary-dark: #0369a1;    /* Sky 700 */
      --primary-tint: #f0f9ff;    /* Sky 50 */
      --secondary: #0d9488;       /* Teal 600 - Statistical Balance */
      --secondary-light: #14b8a6; /* Teal 500 */
      --secondary-tint: #ccfbf1;  /* Teal 50 */
      --accent: #f59e0b;          /* Amber 500 - Highlight */
      --accent-warm: #d97706;     /* Amber 600 */
      --accent-tint: #fefce8;     /* Amber 50 */
      --purple: #7c3aed;          /* Violet 600 */
      --purple-light: #a78bfa;    /* Violet 400 */
      --purple-tint: #f5f3ff;     /* Violet 50 */
      --emerald: #059669;         /* Emerald 600 */
      --emerald-tint: #ecfdf5;    /* Emerald 50 */
      --danger: #dc2626;          /* Red 600 */
      --danger-tint: #fef2f2;     /* Red 50 */
      --info: #2563eb;            /* Blue 600 */
      
      --bg-page: #f8fafc;         /* Slate 50 */
      --bg-surface: #ffffff;      /* Pure White */
      --bg-card: #f1f5f9;         /* Slate 100 */
      --bg-card-alt: #ffffff;     /* White Card */
      
      --text-main: #0f172a;       /* Slate 900 */
      --text-muted: #475569;      /* Slate 600 */
      --text-light: #94a3b8;      /* Slate 400 */
      
      --border: #e2e8f0;          /* Slate 200 */
      --border-dark: #cbd5e1;     /* Slate 300 */
      
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
      --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
      --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
      
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      --radius-xl: 24px;
      --radius-full: 9999px;
    }

    /* ==========================================================
       GLOBAL RESETS & TYPOGRAPHY
       ========================================================== */
    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
      font-size: 16px;
    }

    body {
      background-color: var(--bg-page);
      color: var(--text-main);
      font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      line-height: 1.75;
      -webkit-font-smoothing: antialiased;
      position: relative;
    }

    /* Top-Fixed Reading Progress Bar */
    #progressBarContainer {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 4px;
      background: rgba(226, 232, 240, 0.6);
      z-index: 9999;
    }

    #progressBar {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #0284c7, #0d9488, #7c3aed, #f59e0b);
      transition: width 0.1s ease-out;
    }

    /* Header & Navigation */
    .top-nav {
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 0.75rem 1.5rem;
      position: sticky;
      top: 4px;
      z-index: 1000;
      box-shadow: var(--shadow-sm);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
    }

    .brand-group {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
    }

    .brand-logo {
      width: 38px;
      height: 38px;
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-weight: 800;
      font-size: 1.2rem;
    }

    .brand-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-main);
    }

    .nav-links {
      display: flex;
      gap: 1.25rem;
      list-style: none;
    }

    .nav-links a {
      color: var(--text-muted);
      text-decoration: none;
      font-weight: 600;
      font-size: 0.9rem;
      transition: color 0.2s;
    }

    .nav-links a:hover {
      color: var(--primary);
    }

    /* Hero Banner */
    .hero-banner {
      background: linear-gradient(135deg, #0369a1 0%, #0d9488 50%, #1e1b4b 100%);
      color: #ffffff;
      padding: 3.5rem 2rem 3rem;
      text-align: center;
      position: relative;
      overflow: hidden;
    }

    .hero-banner::before {
      content: "";
      position: absolute;
      top: -50%;
      left: -50%;
      width: 200%;
      height: 200%;
      background: radial-gradient(circle, rgba(255,255,255,0.08) 10%, transparent 20%);
      background-size: 24px 24px;
      pointer-events: none;
    }

    .hero-badges {
      display: flex;
      justify-content: center;
      gap: 0.75rem;
      flex-wrap: wrap;
      margin-bottom: 1.25rem;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.35rem 0.85rem;
      border-radius: var(--radius-full);
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .badge-primary { background: rgba(255, 255, 255, 0.2); color: #ffffff; backdrop-filter: blur(4px); }
    .badge-gold { background: #fef3c7; color: #92400e; }
    .badge-emerald { background: #d1fae5; color: #065f46; }

    .hero-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 2.75rem;
      font-weight: 800;
      line-height: 1.2;
      margin-bottom: 1rem;
      letter-spacing: -0.02em;
    }

    .hero-subtitle {
      font-size: 1.15rem;
      max-width: 860px;
      margin: 0 auto 2rem;
      color: #e0f2fe;
      font-weight: 400;
      line-height: 1.6;
    }

    .hero-stats {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1.25rem;
      max-width: 960px;
      margin: 0 auto;
      text-align: left;
    }

    .stat-item {
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: var(--radius-md);
      padding: 1rem 1.25rem;
      backdrop-filter: blur(8px);
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .stat-icon {
      font-size: 1.75rem;
      color: #38bdf8;
    }

    .stat-text h4 {
      font-size: 0.95rem;
      font-weight: 700;
      margin-bottom: 0.15rem;
      color: #ffffff;
    }

    .stat-text p {
      font-size: 0.75rem;
      color: #bae6fd;
      line-height: 1.3;
    }

    /* TTS Audio Reader Bar */
    .tts-container {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1rem 1.5rem;
      margin: 2rem auto;
      max-width: 1200px;
      box-shadow: var(--shadow-md);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1.25rem;
    }

    .tts-info {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .tts-icon-box {
      width: 44px;
      height: 44px;
      border-radius: var(--radius-md);
      background: var(--primary-tint);
      color: var(--primary);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.35rem;
    }

    .tts-details h4 {
      font-size: 1rem;
      font-weight: 700;
      color: var(--text-main);
    }

    .tts-details p {
      font-size: 0.825rem;
      color: var(--text-muted);
    }

    .tts-controls {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .tts-btn {
      background: var(--primary);
      color: white;
      border: none;
      padding: 0.6rem 1.25rem;
      border-radius: var(--radius-md);
      font-weight: 700;
      font-size: 0.875rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      transition: background 0.2s, transform 0.1s;
    }

    .tts-btn:hover {
      background: var(--primary-dark);
      transform: translateY(-1px);
    }

    .tts-select {
      padding: 0.6rem 0.85rem;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-dark);
      font-size: 0.85rem;
      font-weight: 600;
      background: #ffffff;
      color: var(--text-main);
      cursor: pointer;
    }

    /* Main Container & Sections */
    .main-content {
      max-width: 1200px;
      margin: 2rem auto 4rem;
      padding: 0 1.5rem;
    }

    .section-box {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-xl);
      padding: 2.5rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow-sm);
    }

    .section-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 2rem;
      border-bottom: 2px solid var(--border);
      padding-bottom: 1.25rem;
      gap: 1.5rem;
      flex-wrap: wrap;
    }

    .section-header-left {
      max-width: 800px;
    }

    .section-tag {
      font-size: 0.75rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--primary);
      margin-bottom: 0.35rem;
      display: block;
    }

    .section-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.85rem;
      font-weight: 800;
      color: var(--text-main);
      line-height: 1.3;
    }

    .section-desc {
      font-size: 0.95rem;
      color: var(--text-muted);
      margin-top: 0.5rem;
      line-height: 1.6;
    }

    /* Concept Cards */
    .concept-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 2rem;
      margin-bottom: 2rem;
      box-shadow: var(--shadow-sm);
    }

    .concept-card-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.35rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .concept-card-title i {
      color: var(--primary);
    }

    /* Callout Boxes */
    .callout {
      border-radius: var(--radius-md);
      padding: 1.25rem 1.5rem;
      margin: 1.5rem 0;
      position: relative;
    }

    .callout-title {
      font-weight: 700;
      font-size: 0.95rem;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .callout-def {
      background-color: var(--primary-tint);
      border-left: 5px solid var(--primary);
      color: #0c4a6e;
    }
    .callout-def .callout-title { color: var(--primary-dark); }

    .callout-act {
      background-color: var(--accent-tint);
      border-left: 5px solid var(--accent);
      color: #78350f;
    }
    .callout-act .callout-title { color: var(--accent-warm); }

    .callout-pyq {
      background-color: var(--purple-tint);
      border-left: 5px solid var(--purple);
      color: #4c1d95;
    }
    .callout-pyq .callout-title { color: var(--purple); }

    .callout-hack {
      background-color: var(--emerald-tint);
      border-left: 5px solid var(--emerald);
      color: #064e3b;
    }
    .callout-hack .callout-title { color: var(--emerald); }

    .callout-warn {
      background-color: var(--danger-tint);
      border-left: 5px solid var(--danger);
      color: #7f1d1d;
    }
    .callout-warn .callout-title { color: var(--danger); }

    /* Math Notation Blocks */
    .math-block {
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 1rem 1.25rem;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.95rem;
      color: #1e293b;
      margin: 1rem 0;
      overflow-x: auto;
      line-height: 1.7;
    }

    .math-inline {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.9em;
      background: #f1f5f9;
      padding: 0.15rem 0.35rem;
      border-radius: 4px;
      color: #0369a1;
      font-weight: 600;
    }

    /* Tables */
    .table-container {
      overflow-x: auto;
      margin: 1.75rem 0;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-sm);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.925rem;
    }

    thead th {
      background: #f1f5f9;
      color: var(--text-main);
      padding: 0.85rem 1.25rem;
      font-weight: 700;
      border-bottom: 2px solid var(--border);
    }

    tbody td {
      padding: 0.85rem 1.25rem;
      border-bottom: 1px solid var(--border);
      color: var(--text-main);
      vertical-align: top;
    }

    tbody tr:last-child td {
      border-bottom: none;
    }

    tbody tr:nth-child(even) {
      background-color: #f8fafc;
    }

    tbody tr:hover {
      background-color: #f0f9ff;
    }

    /* Solved Questions - Details & Collapsible Cards */
    .solved-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      margin-bottom: 1.5rem;
      box-shadow: var(--shadow-sm);
    }

    .solved-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    details.ans-box {
      margin-top: 1rem;
      border: 1px solid var(--border-dark);
      border-radius: var(--radius-md);
      overflow: hidden;
      background: #ffffff;
    }

    details.ans-box summary {
      background: #f8fafc;
      padding: 0.85rem 1.25rem;
      font-weight: 700;
      font-size: 0.9rem;
      color: var(--primary-dark);
      cursor: pointer;
      user-select: none;
      display: flex;
      justify-content: space-between;
      align-items: center;
      transition: background 0.2s;
    }

    details.ans-box summary:hover {
      background: #f1f5f9;
    }

    details.ans-box summary::after {
      content: "\\f078";
      font-family: "Font Awesome 6 Free";
      font-weight: 900;
      font-size: 0.8rem;
      transition: transform 0.2s;
    }

    details.ans-box[open] summary::after {
      transform: rotate(180deg);
    }

    .ans-content {
      padding: 1.5rem;
      border-top: 1px solid var(--border);
      background: #ffffff;
    }

    .step-box {
      display: flex;
      gap: 1rem;
      margin-bottom: 1.25rem;
    }

    .step-box:last-child {
      margin-bottom: 0;
    }

    .step-num {
      width: 28px;
      height: 28px;
      border-radius: var(--radius-full);
      background: var(--primary);
      color: white;
      font-size: 0.8rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 0.2rem;
    }

    .step-text {
      flex: 1;
      font-size: 0.925rem;
      line-height: 1.6;
    }

    .step-text strong {
      color: var(--text-main);
    }

    /* SVG Containers */
    .svg-graphic-box {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-xl);
      padding: 1.75rem;
      margin: 2rem 0;
      box-shadow: var(--shadow-md);
      text-align: center;
      overflow: hidden;
    }

    .svg-caption {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-top: 0.75rem;
      font-style: italic;
    }

    /* Interactive Quiz Engine Styles */
    .quiz-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      margin-bottom: 1.5rem;
      box-shadow: var(--shadow-sm);
    }

    .quiz-q-num {
      font-size: 0.75rem;
      font-weight: 800;
      text-transform: uppercase;
      color: var(--primary);
      margin-bottom: 0.35rem;
    }

    .quiz-q-text {
      font-size: 1rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 1rem;
    }

    .options-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.75rem;
      margin-bottom: 1rem;
    }

    .opt-btn {
      background: #f8fafc;
      border: 1px solid var(--border-dark);
      border-radius: var(--radius-md);
      padding: 0.85rem 1.25rem;
      text-align: left;
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--text-main);
      cursor: pointer;
      transition: all 0.2s;
      display: flex;
      align-items: center;
      gap: 0.75rem;
      width: 100%;
    }

    .opt-btn:hover:not([disabled]) {
      background: #e0f2fe;
      border-color: var(--primary);
    }

    .opt-btn.correct {
      background: #d1fae5 !important;
      border-color: #059669 !important;
      color: #065f46 !important;
    }

    .opt-btn.wrong {
      background: #fee2e2 !important;
      border-color: #dc2626 !important;
      color: #991b1b !important;
    }

    .eval-box {
      padding: 1rem;
      border-radius: var(--radius-md);
      font-size: 0.875rem;
      line-height: 1.5;
      display: none;
      margin-top: 0.75rem;
    }

    .eval-box.correct {
      background: #ecfdf5;
      border: 1px solid #10b981;
      color: #065f46;
      display: block;
    }

    .eval-box.wrong {
      background: #fef2f2;
      border: 1px solid #ef4444;
      color: #991b1b;
      display: block;
    }

    .score-banner {
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      color: white;
      padding: 1.5rem;
      border-radius: var(--radius-lg);
      text-align: center;
      margin-bottom: 2rem;
    }

    .score-banner h3 {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.5rem;
      margin-bottom: 0.35rem;
    }

    /* Footer */
    .footer {
      background: #0f172a;
      color: #94a3b8;
      padding: 3rem 1.5rem;
      text-align: center;
      font-size: 0.9rem;
    }

    .footer a {
      color: #38bdf8;
      text-decoration: none;
    }

    .footer a:hover {
      text-decoration: underline;
    }

    @media (max-width: 768px) {
      .hero-title { font-size: 2rem; }
      .section-box { padding: 1.5rem; }
      .nav-links { display: none; }
    }
  </style>
</head>
<body>

  <!-- Reading Progress Bar -->
  <div id="progressBarContainer">
    <div id="progressBar"></div>
  </div>

  <!-- Navigation -->
  <nav class="top-nav">
    <a href="../../index.html" class="brand-group">
      <div class="brand-logo"><i class="fa-solid fa-chart-line"></i></div>
      <div class="brand-title">Sujit Classes</div>
    </a>
    <ul class="nav-links">
      <li><a href="#section1">Blueprint</a></li>
      <li><a href="#section2">Concepts & Glossary</a></li>
      <li><a href="#section3">Fact Bank</a></li>
      <li><a href="#section4">NCERT Solutions</a></li>
      <li><a href="#section5">Exam Bank</a></li>
      <li><a href="#section6">Trap Alerts</a></li>
    </ul>
  </nav>
"""
