# -*- coding: utf-8 -*-
"""Part 1: HTML Head, Stylesheet, Top Navigation, and Hero Banner."""

STYLES_HEAD_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Parallel and Intersecting Lines - Class 7 Mathematics Chapter 5 Master Study Notes (Ganita Prakash | NEP gegp105) | Sujit Classes</title>
  <meta name="description" content="Exhaustive, zero-omission master study note for Class 7 Mathematics Chapter 5: Parallel and Intersecting Lines (NCERT Ganita Prakash gegp105). Complete proofs of vertically opposite angles, linear pairs, transversals, F-shape corresponding angles, Z-shape alternate interior angles, co-interior angles, paper-folding geometry, 100% solved exercises, and 25+ exam question bank.">
  <!-- Google Fonts: Space Grotesk, Plus Jakarta Sans, JetBrains Mono, Noto Sans Oriya -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700&family=Noto+Sans+Oriya:wght@400;600;700&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Space+Grotesk:wght@500;600;700;800&display=swap" rel="stylesheet">
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
      --accent: #d97706;
      --accent-dark: #b45309;
      --accent-light: #fef3c7;
      --purple: #7c3aed;
      --purple-dark: #6d28d9;
      --purple-light: #ede9fe;
      --danger: #dc2626;
      --danger-dark: #b91c1c;
      --danger-light: #fee2e2;
      --success: #16a34a;
      --success-dark: #15803d;
      --success-light: #dcfce7;
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
      line-height: 1.75;
      font-size: 1rem;
      -webkit-font-smoothing: antialiased;
    }

    /* READING PROGRESS BAR */
    #progressBarContainer {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 4px;
      background: transparent;
      z-index: 9999;
    }
    #progressBar {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #0284c7, #0d9488, #7c3aed, #d97706);
      transition: width 0.1s ease-out;
    }

    /* STICKY TOP NAVBAR */
    .top-nav {
      position: sticky;
      top: 0;
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--border);
      padding: 0.75rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 1000;
    }
    .nav-brand {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      font-size: 1.25rem;
      color: var(--dark);
      text-decoration: none;
    }
    .nav-brand i {
      color: var(--primary);
    }
    .nav-links {
      display: flex;
      gap: 1.25rem;
      align-items: center;
    }
    .nav-link {
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 600;
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
      border: 1px solid #bae6fd;
      padding: 0.45rem 1rem;
      border-radius: var(--radius-md);
      font-size: 0.85rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
    }
    .btn-audio:hover {
      background: var(--primary);
      color: #fff;
    }

    /* CONTAINER */
    .container {
      max-width: 1100px;
      margin: 0 auto;
      padding: 2rem 1.5rem 5rem 1.5rem;
    }

    /* HERO SECTION */
    .hero {
      background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0369a1 100%);
      color: #ffffff;
      border-radius: var(--radius-xl);
      padding: 3.5rem 2.5rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow-xl);
      position: relative;
      overflow: hidden;
    }
    .hero::after {
      content: '';
      position: absolute;
      top: -50%;
      right: -20%;
      width: 450px;
      height: 450px;
      background: radial-gradient(circle, rgba(14, 165, 233, 0.25) 0%, transparent 70%);
      border-radius: 50%;
      pointer-events: none;
    }
    .hero-meta {
      display: flex;
      gap: 0.75rem;
      flex-wrap: wrap;
      margin-bottom: 1.25rem;
    }
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.35rem 0.85rem;
      border-radius: 9999px;
      font-size: 0.8rem;
      font-weight: 700;
      letter-spacing: 0.03em;
      text-transform: uppercase;
    }
    .badge-white {
      background: rgba(255, 255, 255, 0.15);
      color: #f8fafc;
      border: 1px solid rgba(255, 255, 255, 0.25);
    }
    .badge-gold {
      background: #fbbf24;
      color: #78350f;
    }
    .badge-teal {
      background: #2dd4bf;
      color: #134e4a;
    }
    .badge-purple {
      background: #c084fc;
      color: #581c87;
    }
    .hero-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 2.75rem;
      font-weight: 800;
      line-height: 1.2;
      margin-bottom: 1rem;
      letter-spacing: -0.02em;
    }
    .hero-subtitle {
      font-size: 1.2rem;
      color: #cbd5e1;
      max-width: 820px;
      line-height: 1.65;
      margin-bottom: 2rem;
    }
    .hero-stats {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 1.25rem;
      border-top: 1px solid rgba(255, 255, 255, 0.15);
      padding-top: 1.75rem;
    }
    .stat-card {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: var(--radius-md);
      padding: 1rem 1.25rem;
      backdrop-filter: blur(5px);
    }
    .stat-val {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.65rem;
      font-weight: 700;
      color: #38bdf8;
      display: block;
    }
    .stat-label {
      font-size: 0.85rem;
      color: #94a3b8;
      font-weight: 500;
    }

    /* BREADCRUMB */
    .breadcrumb {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.9rem;
      color: var(--text-muted);
      margin-bottom: 2rem;
    }
    .breadcrumb a {
      color: var(--primary);
      text-decoration: none;
      font-weight: 600;
    }
    .breadcrumb a:hover {
      text-decoration: underline;
    }

    /* SECTION CARD STYLES */
    .section-card {
      background: var(--surface);
      border-radius: var(--radius-xl);
      border: 1px solid var(--border);
      padding: 2.75rem 2.25rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow-sm);
    }
    .section-header {
      display: flex;
      align-items: flex-start;
      gap: 1.25rem;
      margin-bottom: 2.25rem;
      border-bottom: 2px solid var(--primary-light);
      padding-bottom: 1.25rem;
    }
    .section-icon-box {
      width: 52px;
      height: 52px;
      border-radius: var(--radius-md);
      background: var(--primary-light);
      color: var(--primary);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
      flex-shrink: 0;
    }
    .section-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.85rem;
      font-weight: 700;
      color: var(--dark);
      letter-spacing: -0.01em;
    }
    .section-tagline {
      font-size: 0.95rem;
      color: var(--text-muted);
      margin-top: 0.25rem;
    }

    /* SUB-HEADINGS */
    h3.subheading {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.35rem;
      font-weight: 700;
      color: var(--dark);
      margin: 2.25rem 0 1rem 0;
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }
    h3.subheading i {
      color: var(--primary);
      font-size: 1.15rem;
    }
    h4.topic-head {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin: 1.75rem 0 0.75rem 0;
    }

    p {
      margin-bottom: 1.25rem;
      color: #334155;
    }

    /* PASTEL CALLOUT BOXES */
    .callout {
      border-radius: var(--radius-md);
      padding: 1.25rem 1.5rem;
      margin: 1.5rem 0;
      position: relative;
      border-left: 5px solid;
    }
    .callout-title {
      font-weight: 700;
      font-size: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      margin-bottom: 0.5rem;
      font-family: 'Space Grotesk', sans-serif;
    }
    .callout-def {
      background-color: var(--primary-ultra-light);
      border-left-color: var(--primary);
      color: #0369a1;
    }
    .callout-act {
      background-color: var(--secondary-ultra-light);
      border-left-color: var(--secondary);
      color: #0f766e;
    }
    .callout-pyq {
      background-color: #fdf4ff;
      border-left-color: #c084fc;
      color: #7e22ce;
    }
    .callout-hack {
      background-color: #fffbeb;
      border-left-color: var(--accent);
      color: #b45309;
    }
    .callout-warn {
      background-color: #fef2f2;
      border-left-color: var(--danger);
      color: #b91c1c;
    }

    /* RESPONSIVE TABLES */
    .table-responsive {
      overflow-x: auto;
      margin: 1.75rem 0;
      border-radius: var(--radius-md);
      border: 1px solid var(--border);
      box-shadow: var(--shadow-sm);
    }
    table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.95rem;
    }
    thead {
      background-color: #f1f5f9;
      color: var(--dark);
      font-weight: 700;
    }
    th, td {
      padding: 0.85rem 1.15rem;
      border-bottom: 1px solid var(--border);
    }
    tr:last-child td {
      border-bottom: none;
    }
    tr:nth-child(even) {
      background-color: #f8fafc;
    }
    td.odia-script {
      font-family: 'Noto Sans Oriya', sans-serif;
      font-size: 1rem;
      color: #0f766e;
      font-weight: 600;
    }

    /* MATH DISPLAY & INLINE */
    .math-inline {
      font-family: 'JetBrains Mono', monospace;
      font-weight: 600;
      background: #f1f5f9;
      padding: 0.15rem 0.4rem;
      border-radius: 4px;
      color: #0f172a;
      font-size: 0.95em;
    }
    .math-display {
      font-family: 'JetBrains Mono', monospace;
      font-weight: 600;
      background: #f8fafc;
      border: 1px solid var(--border);
      border-left: 4px solid var(--primary);
      padding: 1rem 1.25rem;
      border-radius: var(--radius-md);
      margin: 1.25rem 0;
      overflow-x: auto;
      font-size: 1.05rem;
      color: #0f172a;
      line-height: 1.9;
    }

    /* COLLAPSIBLE ACCORDION (.ans-box) */
    details.ans-box {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      margin-bottom: 1.5rem;
      box-shadow: var(--shadow-sm);
      transition: all 0.25s ease;
      overflow: hidden;
    }
    details.ans-box[open] {
      border-color: #bae6fd;
      box-shadow: var(--shadow-md);
    }
    summary.ans-header {
      padding: 1.25rem 1.5rem;
      font-weight: 700;
      font-size: 1.05rem;
      color: var(--dark);
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #fcfdfe;
      user-select: none;
      transition: background 0.2s;
    }
    summary.ans-header:hover {
      background: var(--primary-ultra-light);
      color: var(--primary);
    }
    summary.ans-header::-webkit-details-marker {
      display: none;
    }
    .summary-left {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }
    .summary-icon {
      color: var(--primary);
      font-size: 1.1rem;
      transition: transform 0.2s;
    }
    details.ans-box[open] .summary-icon {
      transform: rotate(90deg);
    }
    .question-badge {
      font-size: 0.75rem;
      font-weight: 800;
      padding: 0.25rem 0.6rem;
      border-radius: 9999px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .badge-intext {
      background: #e0f2fe;
      color: #0369a1;
    }
    .badge-try {
      background: #fef3c7;
      color: #b45309;
    }
    .badge-exercise {
      background: #ede9fe;
      color: #6d28d9;
    }
    .ans-content {
      padding: 1.75rem 1.5rem 1.5rem 1.5rem;
      border-top: 1px solid var(--border);
      background: #ffffff;
    }

    /* 5-STEP PRESENTATION FRAMEWORK */
    .step-box {
      margin-bottom: 1.25rem;
      padding: 1rem 1.25rem;
      border-radius: var(--radius-md);
      background: #f8fafc;
      border: 1px solid var(--border);
    }
    .step-header {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-weight: 700;
      font-size: 0.95rem;
      margin-bottom: 0.5rem;
      color: var(--dark);
    }
    .step-1 { border-left: 4px solid #0284c7; }
    .step-2 { border-left: 4px solid #0d9488; }
    .step-3 { border-left: 4px solid #7c3aed; }
    .step-4 { border-left: 4px solid #d97706; }
    .step-5 { border-left: 4px solid #16a34a; background: #f0fdf4; }

    /* SVG DIAGRAM WRAPPERS */
    .diagram-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      margin: 2rem 0;
      box-shadow: var(--shadow-sm);
      text-align: center;
    }
    .diagram-caption {
      margin-top: 1rem;
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--text-muted);
    }
    .svg-node {
      transition: transform 0.25s ease, filter 0.25s ease;
      cursor: pointer;
    }
    .svg-node:hover {
      filter: drop-shadow(0 6px 12px rgba(2, 132, 199, 0.35));
    }

    /* INTERACTIVE QUIZ ENGINE */
    .quiz-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      margin-bottom: 1.5rem;
      box-shadow: var(--shadow-sm);
    }
    .quiz-question {
      font-weight: 700;
      font-size: 1.05rem;
      color: var(--dark);
      margin-bottom: 1rem;
    }
    .quiz-options {
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.75rem;
      margin-bottom: 1rem;
    }
    .option-btn {
      background: #ffffff;
      border: 1.5px solid var(--border);
      border-radius: var(--radius-md);
      padding: 0.85rem 1.15rem;
      text-align: left;
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--text);
      cursor: pointer;
      transition: all 0.2s;
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }
    .option-btn:hover:not(:disabled) {
      border-color: var(--primary);
      background-color: var(--primary-ultra-light);
    }
    .option-btn.correct {
      background-color: #dcfce7 !important;
      border-color: #16a34a !important;
      color: #14532d !important;
    }
    .option-btn.wrong {
      background-color: #fee2e2 !important;
      border-color: #dc2626 !important;
      color: #7f1d1d !important;
    }
    .quiz-feedback {
      padding: 1rem;
      border-radius: var(--radius-md);
      font-size: 0.92rem;
      line-height: 1.6;
      display: none;
    }
    .quiz-feedback.show {
      display: block;
    }
    .quiz-feedback.success {
      background-color: #ecfdf5;
      border: 1px solid #6ee7b7;
      color: #065f46;
    }
    .quiz-feedback.error {
      background-color: #fff1f2;
      border: 1px solid #fecdd3;
      color: #9f1239;
    }

    /* MARKING SCHEME PILL */
    .mark-scheme {
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 0.85rem 1.15rem;
      margin: 1rem 0;
    }
    .mark-scheme-title {
      font-weight: 700;
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: var(--text-muted);
      margin-bottom: 0.5rem;
    }
    .mark-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.9rem;
      padding: 0.3rem 0;
      border-bottom: 1px dashed var(--border);
    }
    .mark-item:last-child {
      border-bottom: none;
    }
    .mark-val {
      font-weight: 700;
      color: var(--primary-dark);
    }

    /* TRAPS COMPARISON */
    .trap-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      margin-bottom: 1.5rem;
      box-shadow: var(--shadow-sm);
    }
    .trap-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--danger-dark);
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .trap-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.25rem;
      margin-top: 1rem;
    }
    @media (max-width: 768px) {
      .trap-grid {
        grid-template-columns: 1fr;
      }
    }
    .wrong-box {
      background: #fef2f2;
      border: 1px solid #fecaca;
      border-radius: var(--radius-md);
      padding: 1rem;
      color: #991b1b;
      font-size: 0.92rem;
    }
    .right-box {
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      border-radius: var(--radius-md);
      padding: 1rem;
      color: #166534;
      font-size: 0.92rem;
    }
    .box-label {
      font-weight: 800;
      text-transform: uppercase;
      font-size: 0.78rem;
      letter-spacing: 0.05em;
      margin-bottom: 0.4rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    /* FOOTER */
    footer {
      background: #0f172a;
      color: #94a3b8;
      padding: 3.5rem 1.5rem;
      text-align: center;
      border-top: 1px solid #1e293b;
    }
    footer a {
      color: #38bdf8;
      text-decoration: none;
    }
    footer a:hover {
      text-decoration: underline;
    }

    /* QUICK NAVIGATION PILLS */
    .quick-nav {
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem;
      margin-bottom: 2.5rem;
      padding: 1rem;
      background: #ffffff;
      border-radius: var(--radius-lg);
      border: 1px solid var(--border);
    }
    .quick-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.5rem 1rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text);
      text-decoration: none;
      background: var(--light);
      border: 1px solid var(--border);
      transition: all 0.2s ease;
    }
    .quick-pill:hover {
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
      transform: translateY(-2px);
    }
  </style>
</head>
<body>

  <!-- Top Scroll Progress Bar -->
  <div id="progressBarContainer">
    <div id="progressBar"></div>
  </div>

  <!-- Sticky Top Navigation -->
  <header class="top-nav">
    <a href="../../index.html" class="nav-brand">
      <i class="fa-solid fa-graduation-cap"></i>
      <span>Sujit Classes</span>
    </a>
    <nav class="nav-links">
      <a href="#blueprint" class="nav-link">Mind Map</a>
      <a href="#concepts" class="nav-link">Concepts</a>
      <a href="#factbank" class="nav-link">Formula Bank</a>
      <a href="#ncert-solutions" class="nav-link">NCERT Solutions</a>
      <a href="#exam-bank" class="nav-link">Exam Bank</a>
      <a href="#traps-revision" class="nav-link">Traps & Revision</a>
      <button id="audioBtn" class="btn-audio" onclick="toggleAudioReader()">
        <i class="fa-solid fa-volume-high"></i>
        <span id="navBtnText">Listen Note</span>
      </button>
    </nav>
  </header>

  <div class="container">

    <!-- Breadcrumb Navigation -->
    <nav class="breadcrumb" aria-label="breadcrumb">
      <a href="../../index.html"><i class="fa-solid fa-house"></i> Home</a>
      <i class="fa-solid fa-chevron-right"></i>
      <a href="../../index.html?class=7">Class 7</a>
      <i class="fa-solid fa-chevron-right"></i>
      <span>Mathematics: Chapter 5 - Parallel and Intersecting Lines</span>
    </nav>

    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-meta">
        <span class="badge badge-gold"><i class="fa-solid fa-award"></i> NCERT NEP 2026-27</span>
        <span class="badge badge-white"><i class="fa-solid fa-book-open"></i> Ganita Prakash gegp105</span>
        <span class="badge badge-teal"><i class="fa-solid fa-circle-check"></i> 100% Solved (Zero Omission)</span>
        <span class="badge badge-purple"><i class="fa-solid fa-language"></i> English + Odia Vocabulary</span>
      </div>
      <h1 class="hero-title">Parallel and Intersecting Lines</h1>
      <p class="hero-subtitle">
        An exhaustive, master-level pedagogical guide covering intersecting lines, linear pairs, vertically opposite angles, orthogonal perpendiculars, transversals, F-shape corresponding angles, Z-shape alternate interior angles, co-interior supplementary rules, folding theorems, and optical illusions.
      </p>
      <div class="hero-stats">
        <div class="stat-card">
          <span class="stat-val">34 Pages</span>
          <span class="stat-label">NCERT gegp105 Textbook Covered</span>
        </div>
        <div class="stat-card">
          <span class="stat-val">100%</span>
          <span class="stat-label">In-Text & Back Exercises Solved</span>
        </div>
        <div class="stat-card">
          <span class="stat-val">30 Terms</span>
          <span class="stat-label">Bilingual English-Odia Glossary</span>
        </div>
        <div class="stat-card">
          <span class="stat-val">25+ Questions</span>
          <span class="stat-label">Exhaustive Exam Question Bank</span>
        </div>
      </div>
    </section>

    <!-- Quick Navigation Pills -->
    <div class="quick-nav">
      <a href="#blueprint" class="quick-pill"><i class="fa-solid fa-sitemap"></i> Section 1: Visual Blueprint</a>
      <a href="#concepts" class="quick-pill"><i class="fa-solid fa-book-reader"></i> Section 2: Concepts & Odia Glossary</a>
      <a href="#factbank" class="quick-pill"><i class="fa-solid fa-table"></i> Section 3: Rapid Revision Bank</a>
      <a href="#ncert-solutions" class="quick-pill"><i class="fa-solid fa-pencil"></i> Section 4: 100% Solved NCERT</a>
      <a href="#exam-bank" class="quick-pill"><i class="fa-solid fa-file-pen"></i> Section 5: Exam Question Bank</a>
      <a href="#traps-revision" class="quick-pill"><i class="fa-solid fa-triangle-exclamation"></i> Section 6: Traps & 15 Revision Points</a>
    </div>
"""
