# -*- coding: utf-8 -*-
"""Part 1: HTML Head, Meta, CSS, Navigation Bar, and Hero Banner for Class 8 Science Ch 11."""

PART1_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Keeping Time with the Skies - Class 8 Science Chapter 11 Master Study Notes | Sujit Classes</title>
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
      --accent: #d97706;
      --accent-dark: #b45309;
      --accent-light: #fef3c7;
      --purple: #6366f1;
      --purple-dark: #4f46e5;
      --purple-light: #e0e7ff;
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
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: var(--light);
      color: var(--text);
      line-height: 1.75;
      padding-top: 64px;
      font-size: 16px;
      -webkit-font-smoothing: antialiased;
    }

    /* Reading Progress Bar (Top-Fixed) */
    #reading-progress-bar {
      position: fixed;
      top: 0;
      left: 0;
      height: 4px;
      width: 0%;
      background: linear-gradient(90deg, #0284c7, #6366f1, #f59e0b, #0d9488);
      z-index: 10002;
      transition: width 0.1s ease;
    }

    /* Fixed Top Navigation Bar */
    .top-nav {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      height: 64px;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 1.5rem;
      z-index: 10000;
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

    .nav-brand-badge {
      background: linear-gradient(135deg, var(--primary), var(--purple));
      color: white;
      padding: 0.3rem 0.65rem;
      border-radius: var(--radius-sm);
      font-size: 0.8rem;
      font-weight: 800;
      letter-spacing: 0.5px;
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .btn-nav {
      background: var(--light);
      border: 1px solid var(--border);
      color: var(--text);
      padding: 0.45rem 0.9rem;
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      transition: all 0.2s ease;
      text-decoration: none;
    }

    .btn-nav:hover {
      background: var(--primary-light);
      color: var(--primary-dark);
      border-color: var(--primary);
    }

    .btn-nav-primary {
      background: var(--primary);
      color: white;
      border-color: var(--primary-dark);
    }

    .btn-nav-primary:hover {
      background: var(--primary-dark);
      color: white;
    }

    /* Quick Chapter Navigation Pills */
    .quick-nav {
      display: flex;
      gap: 0.5rem;
      overflow-x: auto;
      padding: 0.75rem 0;
      margin-bottom: 2rem;
      scrollbar-width: thin;
    }

    .quick-nav a {
      white-space: nowrap;
      padding: 0.4rem 0.85rem;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 999px;
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--text);
      text-decoration: none;
      transition: all 0.2s ease;
    }

    .quick-nav a:hover {
      background: var(--primary-light);
      color: var(--primary-dark);
      border-color: var(--primary);
    }

    /* Main Container */
    .main-container {
      max-width: 1080px;
      margin: 0 auto;
      padding: 2rem 1.25rem 5rem;
    }

    /* Hero Section */
    .hero-banner {
      background: linear-gradient(135deg, #091e3a 0%, #172554 40%, #1e1b4b 100%);
      color: white;
      border-radius: var(--radius-xl);
      padding: 3rem 2.25rem;
      margin-bottom: 2rem;
      position: relative;
      overflow: hidden;
      box-shadow: var(--shadow-xl);
    }

    .hero-banner::before {
      content: '';
      position: absolute;
      top: -60px;
      right: -60px;
      width: 280px;
      height: 280px;
      background: radial-gradient(circle, rgba(99, 102, 241, 0.35) 0%, rgba(0,0,0,0) 70%);
      border-radius: 50%;
    }

    .hero-banner::after {
      content: '';
      position: absolute;
      bottom: -80px;
      left: 10%;
      width: 320px;
      height: 320px;
      background: radial-gradient(circle, rgba(2, 132, 199, 0.3) 0%, rgba(0,0,0,0) 70%);
      border-radius: 50%;
    }

    .hero-tag {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.25);
      padding: 0.35rem 0.85rem;
      border-radius: 999px;
      font-size: 0.82rem;
      font-weight: 700;
      letter-spacing: 0.5px;
      margin-bottom: 1rem;
      text-transform: uppercase;
      backdrop-filter: blur(4px);
    }

    .hero-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 2.5rem;
      line-height: 1.22;
      font-weight: 800;
      margin-bottom: 1rem;
    }

    .hero-subtitle {
      font-size: 1.1rem;
      color: #e2e8f0;
      max-width: 840px;
      line-height: 1.6;
      margin-bottom: 1.75rem;
    }

    .hero-meta-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 1rem;
      position: relative;
      z-index: 2;
    }

    .hero-meta-card {
      background: rgba(255, 255, 255, 0.1);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: var(--radius-md);
      padding: 0.85rem 1rem;
    }

    .hero-meta-label {
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: #94a3b8;
      margin-bottom: 0.2rem;
    }

    .hero-meta-value {
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      font-size: 1rem;
      color: #ffffff;
    }

    /* Content Section Headings & Layout */
    .study-section {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 2.25rem 2rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow-sm);
    }

    .section-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: var(--primary-light);
      color: var(--primary-dark);
      padding: 0.35rem 0.8rem;
      border-radius: 999px;
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 0.75rem;
    }

    .section-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.85rem;
      color: var(--dark);
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.75rem;
      font-weight: 800;
    }

    .section-description {
      font-size: 1.05rem;
      color: var(--text-muted);
      margin-bottom: 1.75rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid var(--border);
    }

    h3.sub-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.35rem;
      color: var(--dark);
      margin: 1.75rem 0 1rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    h4.nested-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.15rem;
      color: var(--primary-dark);
      margin: 1.25rem 0 0.65rem;
      font-weight: 700;
    }

    p {
      margin-bottom: 1.1rem;
      color: var(--text);
    }

    /* Pastel Callout Boxes */
    .callout {
      border-radius: var(--radius-md);
      padding: 1.25rem 1.35rem;
      margin: 1.5rem 0;
      border-left: 5px solid;
    }

    .callout-def {
      background-color: var(--primary-ultra-light);
      border-color: var(--primary);
    }

    .callout-act {
      background-color: var(--secondary-ultra-light);
      border-color: var(--secondary);
    }

    .callout-pyq {
      background-color: var(--purple-light);
      border-color: var(--purple);
    }

    .callout-hack {
      background-color: var(--accent-light);
      border-color: var(--accent);
    }

    .callout-warn {
      background-color: var(--danger-light);
      border-color: var(--danger);
    }

    .callout-heritage {
      background-color: #fff7ed;
      border-color: #ea580c;
    }

    .callout-header {
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      font-size: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      margin-bottom: 0.5rem;
    }

    .callout-def .callout-header { color: var(--primary-dark); }
    .callout-act .callout-header { color: var(--secondary-dark); }
    .callout-pyq .callout-header { color: var(--purple-dark); }
    .callout-hack .callout-header { color: var(--accent-dark); }
    .callout-warn .callout-header { color: var(--danger-dark); }
    .callout-heritage .callout-header { color: #c2410c; }

    /* Tables */
    .table-container {
      overflow-x: auto;
      margin: 1.5rem 0;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      background: var(--surface);
      box-shadow: var(--shadow-sm);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.95rem;
    }

    thead th {
      background-color: #f1f5f9;
      color: var(--dark);
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      padding: 0.9rem 1.1rem;
      border-bottom: 2px solid var(--border-dark);
      white-space: nowrap;
    }

    tbody td {
      padding: 0.85rem 1.1rem;
      border-bottom: 1px solid var(--border);
      color: var(--text);
      vertical-align: top;
    }

    tbody tr:last-child td {
      border-bottom: none;
    }

    tbody tr:nth-child(even) {
      background-color: #f8fafc;
    }

    tbody tr:hover {
      background-color: var(--primary-ultra-light);
    }

    /* SVG Diagram Containers */
    .svg-container {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 1.5rem 1rem;
      margin: 1.75rem 0;
      text-align: center;
      box-shadow: var(--shadow-sm);
      position: relative;
    }

    .svg-container svg {
      max-width: 100%;
      height: auto;
      display: block;
      margin: 0 auto;
    }

    .svg-caption {
      margin-top: 0.75rem;
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--text-muted);
      font-family: 'Space Grotesk', sans-serif;
    }

    /* SVG Micro-Animations */
    .svg-pulse {
      animation: pulseAnim 2.5s infinite ease-in-out;
    }
    @keyframes pulseAnim {
      0%, 100% { opacity: 0.8; transform: scale(1); }
      50% { opacity: 1; transform: scale(1.03); }
    }

    .svg-glow {
      filter: drop-shadow(0 0 4px rgba(245, 158, 11, 0.7));
      transition: all 0.3s ease;
    }
    .svg-glow:hover {
      filter: drop-shadow(0 0 10px rgba(245, 158, 11, 1));
    }

    /* Interactive Details / Collapsible Box */
    details.ans-box {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      margin: 1.1rem 0;
      overflow: hidden;
      transition: all 0.25s ease;
      box-shadow: var(--shadow-sm);
    }

    details.ans-box[open] {
      border-color: var(--primary);
      box-shadow: var(--shadow-md);
    }

    summary.ans-header {
      padding: 1.1rem 1.25rem;
      background: #f8fafc;
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      font-size: 1.02rem;
      color: var(--dark);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      user-select: none;
      transition: background-color 0.2s ease;
    }

    summary.ans-header:hover {
      background-color: var(--primary-light);
      color: var(--primary-dark);
    }

    summary.ans-header::-webkit-details-marker {
      display: none;
    }

    .summary-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      background: var(--primary);
      color: white;
      font-size: 0.75rem;
      padding: 0.2rem 0.55rem;
      border-radius: var(--radius-sm);
      margin-right: 0.6rem;
    }

    .summary-badge-act {
      background: var(--secondary);
    }

    .summary-badge-pyq {
      background: var(--purple);
    }

    .ans-content {
      padding: 1.25rem 1.35rem;
      background: #ffffff;
      border-top: 1px solid var(--border);
      font-size: 0.98rem;
    }

    /* 5-step badge presentation */
    .step-box {
      margin-bottom: 0.9rem;
      padding-left: 0.5rem;
      border-left: 3px solid var(--primary-light);
    }

    .step-label {
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      font-size: 0.88rem;
      color: var(--primary-dark);
      margin-bottom: 0.2rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    /* MCQ Interactive Quiz Engine */
    .mcq-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 1.5rem;
      margin: 1.5rem 0;
      box-shadow: var(--shadow-sm);
    }

    .mcq-question {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--dark);
      margin-bottom: 1rem;
    }

    .mcq-options {
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
      margin-bottom: 1rem;
    }

    .mcq-btn {
      background: #f8fafc;
      border: 1.5px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 0.75rem 1rem;
      text-align: left;
      font-size: 0.94rem;
      font-family: 'Plus Jakarta Sans', sans-serif;
      color: var(--text);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.75rem;
      transition: all 0.2s ease;
      width: 100%;
    }

    .mcq-btn:hover:not(:disabled) {
      background: var(--primary-light);
      border-color: var(--primary);
      color: var(--primary-dark);
    }

    .mcq-btn.correct {
      background: #dcfce7 !important;
      border-color: #16a34a !important;
      color: #15803d !important;
      font-weight: 700;
    }

    .mcq-btn.wrong {
      background: #fee2e2 !important;
      border-color: #dc2626 !important;
      color: #b91c1c !important;
    }

    .mcq-feedback {
      display: none;
      padding: 0.9rem 1.1rem;
      border-radius: var(--radius-sm);
      font-size: 0.9rem;
      margin-top: 0.75rem;
      border-left: 4px solid;
    }

    .mcq-feedback.show-correct {
      display: block;
      background: #f0fdf4;
      border-color: #16a34a;
      color: #166534;
    }

    .mcq-feedback.show-wrong {
      display: block;
      background: #fef2f2;
      border-color: #dc2626;
      color: #991b1b;
    }

    /* Score counter banner */
    .quiz-score-banner {
      background: linear-gradient(135deg, #0284c7, #6366f1);
      color: white;
      border-radius: var(--radius-md);
      padding: 1rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1.5rem;
    }

    /* Marking scheme box */
    .marking-scheme {
      background: #f1f5f9;
      border: 1px dashed var(--border-dark);
      border-radius: var(--radius-sm);
      padding: 0.75rem 1rem;
      margin-top: 0.75rem;
      font-size: 0.88rem;
      color: var(--text-muted);
    }

    .marking-scheme strong {
      color: var(--dark);
    }

    /* Audio reader pill */
    #audio-status {
      display: none;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--primary);
      background: var(--primary-light);
      padding: 0.25rem 0.65rem;
      border-radius: 999px;
    }

    /* Floating Back-to-Top Button */
    #back-to-top {
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      background: var(--primary);
      color: white;
      width: 46px;
      height: 46px;
      border-radius: 50%;
      border: none;
      box-shadow: var(--shadow-lg);
      cursor: pointer;
      display: none;
      align-items: center;
      justify-content: center;
      font-size: 1.1rem;
      z-index: 9999;
      transition: all 0.2s ease;
    }

    #back-to-top:hover {
      background: var(--primary-dark);
      transform: translateY(-3px);
    }

    /* Concept Mind Map Tree */
    .mindmap-container {
      background: #f8fafc;
      border: 1.5px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.75rem;
      margin: 1.5rem 0;
    }

    .mindmap-root {
      background: linear-gradient(135deg, #0284c7, #6366f1);
      color: white;
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 800;
      font-size: 1.25rem;
      padding: 1rem 1.5rem;
      border-radius: var(--radius-md);
      text-align: center;
      margin-bottom: 2rem;
      box-shadow: var(--shadow-md);
    }

    .mindmap-branches {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.5rem;
    }

    .mindmap-branch-card {
      background: white;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 1.25rem;
      box-shadow: var(--shadow-sm);
      border-top: 4px solid var(--primary);
    }

    .branch-title {
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      font-size: 1.05rem;
      color: var(--dark);
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .branch-list {
      list-style: none;
      padding-left: 0;
    }

    .branch-list li {
      font-size: 0.88rem;
      margin-bottom: 0.5rem;
      padding-left: 1.2rem;
      position: relative;
      color: var(--text);
    }

    .branch-list li::before {
      content: '▸';
      position: absolute;
      left: 0;
      color: var(--primary);
      font-weight: bold;
    }

    /* Responsive Queries */
    @media (max-width: 768px) {
      body { padding-top: 56px; }
      .top-nav { height: 56px; padding: 0 1rem; }
      .hero-title { font-size: 1.85rem; }
      .hero-banner { padding: 2rem 1.25rem; }
      .study-section { padding: 1.5rem 1.15rem; }
      .hero-meta-grid { grid-template-columns: 1fr 1fr; }
      #back-to-top { bottom: 1.25rem; right: 1.25rem; }
      .mindmap-branches { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

  <!-- Top-Fixed Reading Progress Bar -->
  <div id="reading-progress-bar"></div>

  <!-- Fixed Top Navigation Bar -->
  <nav class="top-nav">
    <a href="../../index.html" class="nav-brand">
      <span class="nav-brand-badge">CBSE / NEP</span>
      <span>Sujit Classes</span>
    </a>
    <div class="nav-actions">
      <span id="audio-status"><i class="fa-solid fa-volume-high"></i> Reading aloud...</span>
      <button id="btn-audio-read" class="btn-nav" title="Listen to chapter summary audio">
        <i class="fa-solid fa-headphones"></i>
        <span>Listen</span>
      </button>
      <a href="../../index.html" class="btn-nav">
        <i class="fa-solid fa-arrow-left"></i>
        <span>Portal Home</span>
      </a>
      <button onclick="window.print()" class="btn-nav btn-nav-primary">
        <i class="fa-solid fa-print"></i>
        <span>Print Notes</span>
      </button>
    </div>
  </nav>

  <div class="main-container">

    <!-- Quick Navigation Pills -->
    <div class="quick-nav">
      <a href="#section-1"><i class="fa-solid fa-diagram-project"></i> 1. Visual Mind Map</a>
      <a href="#section-2"><i class="fa-solid fa-book-open"></i> 2. Complete Theory & Odia Vocabulary</a>
      <a href="#section-3"><i class="fa-solid fa-table"></i> 3. Rapid Formula & Fact Bank</a>
      <a href="#section-4"><i class="fa-solid fa-list-check"></i> 4. 100% Solved NCERT (Activities & Exercises)</a>
      <a href="#section-5"><i class="fa-solid fa-graduation-cap"></i> 5. Exam Question Bank (MCQs, A&R, LAQ)</a>
      <a href="#section-6"><i class="fa-solid fa-triangle-exclamation"></i> 6. Exam Traps & 15 Revision Points</a>
    </div>

    <!-- Hero Banner -->
    <header class="hero-banner">
      <div class="hero-tag">
        <i class="fa-solid fa-moon"></i> Class 8 Science • Chapter 11 • NCERT Curiosity (NEP-2020)
      </div>
      <h1 class="hero-title">Keeping Time with the Skies</h1>
      <p class="hero-subtitle">
        An exhaustive, zero-omission conceptual master study note exploring celestial timekeeping, the geometry of Moon phases, solar, lunar and luni-solar calendars, the intercalary month (Adhika Maasa), the Indian National Calendar, and modern artificial satellites launched by ISRO.
      </p>
      <div class="hero-meta-grid">
        <div class="hero-meta-card">
          <div class="hero-meta-label">Curricular Code</div>
          <div class="hero-meta-value">NCERT hecu111</div>
        </div>
        <div class="hero-meta-card">
          <div class="hero-meta-label">Coverage Floor</div>
          <div class="hero-meta-value">100% Zero-Omission</div>
        </div>
        <div class="hero-meta-card">
          <div class="hero-meta-label">Interactive Visuals</div>
          <div class="hero-meta-value">6 Responsive SVGs</div>
        </div>
        <div class="hero-meta-card">
          <div class="hero-meta-label">Exam Questions</div>
          <div class="hero-meta-value">27 CBE & PYQ Models</div>
        </div>
      </div>
    </header>
"""
