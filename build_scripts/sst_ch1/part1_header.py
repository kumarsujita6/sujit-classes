# -*- coding: utf-8 -*-
"""Part 1: Header, Meta, Full CSS Styling, Top Navigation, and Hero Banner."""

PART1_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sujit Classes Notes: Ch 1 - Natural Resources and Their Use (Class 8 Social Science NEP)</title>
  <!-- Google Fonts: Space Grotesk, Plus Jakarta Sans, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Space+Grotesk:wght@500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <!-- Font Awesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <style>
    :root {
      --primary: #059669;
      --primary-dark: #047857;
      --primary-light: #d1fae5;
      --primary-ultra-light: #f0fdf4;
      --secondary: #0284c7;
      --secondary-dark: #0369a1;
      --secondary-light: #e0f2fe;
      --accent: #d97706;
      --accent-dark: #b45309;
      --accent-light: #fef3c7;
      --purple: #7c3aed;
      --purple-dark: #6d28d9;
      --purple-light: #ede9fe;
      --rose: #e11d48;
      --rose-light: #ffe4e6;
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
    }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--light);
      color: var(--text);
      line-height: 1.75;
      font-size: 15.5px;
      padding-top: 60px;
    }

    /* Top-Fixed 4px Linear Gradient Reading Progress Bar */
    #reading-progress-bar {
      position: fixed;
      top: 0;
      left: 0;
      height: 4px;
      width: 0%;
      background: linear-gradient(90deg, #10b981 0%, #0284c7 45%, #f59e0b 80%, #7c3aed 100%);
      z-index: 10002;
      transition: width 0.1s ease-out;
      box-shadow: 0 0 10px rgba(16, 185, 129, 0.6);
    }

    /* Sticky Navigation Header */
    .top-nav {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      height: 60px;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      z-index: 10001;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 1.5rem;
    }

    .nav-brand {
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      color: var(--primary-dark);
      text-decoration: none;
      font-size: 1.15rem;
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }

    .nav-brand i {
      color: var(--primary);
      font-size: 1.3rem;
    }

    .nav-links {
      display: flex;
      align-items: center;
      gap: 0.4rem;
      overflow-x: auto;
      padding: 0.35rem 0;
    }

    .nav-link {
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.83rem;
      font-weight: 600;
      padding: 0.4rem 0.8rem;
      border-radius: 9999px;
      transition: all 0.2s ease;
      white-space: nowrap;
    }

    .nav-link:hover {
      background: var(--primary-light);
      color: var(--primary-dark);
    }

    .nav-controls {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .control-btn {
      background: #f1f5f9;
      border: 1px solid var(--border);
      color: var(--text);
      font-size: 0.78rem;
      font-weight: 600;
      padding: 0.35rem 0.75rem;
      border-radius: 9999px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s ease;
    }

    .control-btn:hover {
      background: var(--secondary-light);
      color: var(--secondary-dark);
      border-color: #bae6fd;
    }

    /* Hero Banner */
    .hero-banner {
      background: linear-gradient(135deg, #064e3b 0%, #047857 30%, #0284c7 75%, #4338ca 100%);
      color: white;
      padding: 4.25rem 1.5rem 3.75rem;
      text-align: center;
      position: relative;
      overflow: hidden;
      box-shadow: 0 10px 30px -10px rgba(6, 78, 59, 0.45);
    }

    .hero-banner::before {
      content: '';
      position: absolute;
      top: -50%;
      left: -20%;
      width: 140%;
      height: 200%;
      background: radial-gradient(circle, rgba(255,255,255,0.09) 10%, transparent 60%);
      pointer-events: none;
    }

    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: rgba(255, 255, 255, 0.18);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.35);
      padding: 0.45rem 1.2rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 700;
      margin-bottom: 1.25rem;
      letter-spacing: 0.6px;
      text-transform: uppercase;
      box-shadow: 0 2px 8px rgba(0,0,0,0.15);
    }

    .hero-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 2.75rem;
      font-weight: 800;
      line-height: 1.22;
      margin-bottom: 1.15rem;
      max-width: 980px;
      margin-left: auto;
      margin-right: auto;
      letter-spacing: -0.5px;
    }

    .hero-sub {
      font-size: 1.18rem;
      opacity: 0.96;
      max-width: 880px;
      margin: 0 auto 1.6rem;
      font-weight: 400;
      line-height: 1.65;
    }

    .hero-meta {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 1.6rem;
      font-size: 0.92rem;
      opacity: 0.95;
      margin-bottom: 1.8rem;
    }

    .hero-meta span {
      display: flex;
      align-items: center;
      gap: 0.45rem;
      background: rgba(0, 0, 0, 0.18);
      padding: 0.35rem 0.85rem;
      border-radius: 9999px;
      border: 1px solid rgba(255, 255, 255, 0.15);
    }

    .hero-actions {
      display: flex;
      justify-content: center;
      gap: 1rem;
      flex-wrap: wrap;
    }

    .audio-btn {
      background: #ffffff;
      color: #065f46;
      border: none;
      padding: 0.8rem 1.75rem;
      border-radius: 9999px;
      font-weight: 700;
      font-size: 0.95rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.18);
      transition: all 0.25s ease;
    }

    .audio-btn:hover {
      background: #f0fdf4;
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
    }

    .hero-secondary-btn {
      background: rgba(255, 255, 255, 0.16);
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.4);
      padding: 0.8rem 1.5rem;
      border-radius: 9999px;
      font-weight: 600;
      font-size: 0.95rem;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.2s ease;
    }

    .hero-secondary-btn:hover {
      background: rgba(255, 255, 255, 0.25);
      transform: translateY(-2px);
    }

    /* Main Container */
    .main-container {
      max-width: 1120px;
      margin: 2.75rem auto;
      padding: 0 1.5rem;
    }

    /* Section Card */
    .section-card {
      background: var(--surface);
      border-radius: var(--radius-xl);
      border: 1px solid var(--border);
      padding: 2.85rem;
      margin-bottom: 3.25rem;
      box-shadow: var(--shadow-sm);
      transition: box-shadow 0.3s ease;
    }

    .section-card:hover {
      box-shadow: var(--shadow-md);
    }

    .section-header {
      margin-bottom: 2.25rem;
      border-bottom: 2px solid var(--primary-light);
      padding-bottom: 1.35rem;
      position: relative;
    }

    .section-header::after {
      content: '';
      position: absolute;
      bottom: -2px;
      left: 0;
      width: 85px;
      height: 2.5px;
      background: var(--primary);
    }

    .section-num {
      display: inline-block;
      color: var(--primary-dark);
      background: var(--primary-light);
      font-weight: 800;
      text-transform: uppercase;
      font-size: 0.82rem;
      letter-spacing: 1px;
      padding: 0.35rem 0.85rem;
      border-radius: 9999px;
      margin-bottom: 0.5rem;
    }

    .section-card h2 {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 2rem;
      color: var(--dark);
      margin-top: 0.4rem;
      font-weight: 800;
      letter-spacing: -0.3px;
    }

    .section-sub {
      color: var(--text-muted);
      font-size: 1.02rem;
      margin-top: 0.5rem;
      line-height: 1.65;
    }

    h3.topic-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.48rem;
      color: var(--primary-dark);
      margin: 2.6rem 0 1.15rem;
      display: flex;
      align-items: center;
      gap: 0.75rem;
      border-left: 5px solid var(--primary);
      padding-left: 0.85rem;
    }

    h4.sub-topic {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.2rem;
      color: var(--dark);
      margin: 1.85rem 0 0.8rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    p {
      margin-bottom: 1.25rem;
      line-height: 1.8;
      color: var(--text);
    }

    /* Callout Boxes */
    .callout-box {
      border-radius: var(--radius-md);
      padding: 1.4rem 1.65rem;
      margin: 1.85rem 0;
      display: flex;
      gap: 1.15rem;
      align-items: flex-start;
      border-left: 5px solid;
      box-shadow: 0 2px 10px rgba(0,0,0,0.02);
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .callout-box:hover {
      transform: translateY(-2px);
      box-shadow: var(--shadow-sm);
    }

    .callout-box i {
      font-size: 1.45rem;
      margin-top: 0.25rem;
      flex-shrink: 0;
    }

    .callout-box .callout-text {
      flex: 1;
      font-size: 0.97rem;
      line-height: 1.72;
    }

    .callout-box .callout-text strong.callout-heading {
      display: block;
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.06rem;
      font-weight: 700;
      margin-bottom: 0.35rem;
    }

    .callout-def {
      background: var(--primary-ultra-light);
      border-color: #10b981;
      color: #064e3b;
    }
    .callout-def i { color: #059669; }

    .callout-act {
      background: #eff6ff;
      border-color: #3b82f6;
      color: #1e3a8a;
    }
    .callout-act i { color: #2563eb; }

    .callout-pyq {
      background: #fffbeb;
      border-color: #f59e0b;
      color: #78350f;
    }
    .callout-pyq i { color: #d97706; }

    .callout-hack {
      background: #faf5ff;
      border-color: #a855f7;
      color: #581c87;
    }
    .callout-hack i { color: #9333ea; }

    .callout-warn {
      background: #fef2f2;
      border-color: #ef4444;
      color: #7f1d1d;
    }
    .callout-warn i { color: #dc2626; }

    /* Tables */
    .table-container {
      overflow-x: auto;
      margin: 1.85rem 0;
      border-radius: var(--radius-md);
      border: 1px solid var(--border);
      box-shadow: 0 1px 4px rgba(0,0,0,0.03);
    }

    .data-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.95rem;
    }

    .data-table th {
      background: #f1f5f9;
      color: var(--dark);
      padding: 1.05rem 1.2rem;
      font-weight: 700;
      font-family: 'Space Grotesk', sans-serif;
      border-bottom: 2px solid var(--border-dark);
      white-space: nowrap;
    }

    .data-table td {
      padding: 1rem 1.2rem;
      border-bottom: 1px solid var(--border);
      vertical-align: top;
      line-height: 1.68;
    }

    .data-table tr:nth-child(even) { background: #f8fafc; }
    .data-table tr:hover { background: #f0fdf4; }

    /* Collapsible Details Answers (Ans Box) */
    details.ans-box {
      border: 1.5px solid #cbd5e1;
      border-radius: var(--radius-md);
      margin: 1.4rem 0;
      background: #ffffff;
      overflow: hidden;
      transition: all 0.25s ease;
    }

    details.ans-box[open] {
      border-color: var(--primary);
      box-shadow: 0 4px 14px rgba(5, 150, 105, 0.09);
    }

    details.ans-box summary {
      padding: 1.1rem 1.45rem;
      background: #f8fafc;
      font-weight: 700;
      font-size: 0.98rem;
      color: #1e293b;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      user-select: none;
      transition: background 0.2s ease, color 0.2s ease;
    }

    details.ans-box summary:hover {
      background: #f1f5f9;
      color: var(--primary-dark);
    }

    details.ans-box[open] summary {
      background: var(--primary-light);
      color: var(--primary-dark);
      border-bottom: 1px solid #a7f3d0;
    }

    .ans-content {
      padding: 1.45rem 1.65rem;
      background: #ffffff;
      font-size: 0.96rem;
      line-height: 1.76;
    }

    .step-box {
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 0.9rem 1.15rem;
      margin: 0.75rem 0;
    }

    .step-title {
      font-weight: 800;
      color: var(--primary-dark);
      font-size: 0.88rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 0.35rem;
      display: flex;
      align-items: center;
      gap: 0.45rem;
    }

    /* Badges */
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.3rem 0.75rem;
      border-radius: 9999px;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.6px;
    }

    .badge-green { background: #dcfce7; color: #15803d; border: 1px solid #bbf7d0; }
    .badge-blue { background: #dbeafe; color: #1e40af; border: 1px solid #bfdbfe; }
    .badge-amber { background: #fef3c7; color: #b45309; border: 1px solid #fde68a; }
    .badge-purple { background: #f3e8ff; color: #7e22ce; border: 1px solid #e9d5ff; }
    .badge-rose { background: #ffe4e6; color: #be123c; border: 1px solid #fecdd3; }

    /* Diagram Wrapper */
    .diagram-wrapper {
      margin: 2.35rem 0;
      text-align: center;
      background: #ffffff;
      padding: 1.85rem 1.35rem;
      border-radius: var(--radius-lg);
      border: 1px solid var(--border);
      box-shadow: var(--shadow-sm);
    }

    .diagram-caption {
      font-size: 0.92rem;
      color: var(--text-muted);
      margin-top: 1.1rem;
      font-weight: 500;
      line-height: 1.55;
    }

    /* Card Grids */
    .card-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(290px, 1fr));
      gap: 1.5rem;
      margin: 1.6rem 0;
    }

    .card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 1.45rem 1.55rem;
      box-shadow: 0 2px 5px rgba(0,0,0,0.02);
      transition: all 0.25s ease;
    }

    .card:hover {
      box-shadow: var(--shadow-md);
      transform: translateY(-2px);
    }

    /* Quiz Engine */
    .quiz-score-banner {
      background: linear-gradient(135deg, #065f46 0%, #0284c7 100%);
      color: #ffffff;
      border-radius: var(--radius-md);
      padding: 1.45rem 1.85rem;
      margin: 1.85rem 0 2.35rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
      box-shadow: 0 4px 15px rgba(6, 95, 70, 0.25);
    }

    .quiz-score-badge {
      font-size: 1.3rem;
      font-weight: 800;
      font-family: 'Space Grotesk', sans-serif;
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }

    .quiz-teacher-msg {
      font-size: 0.98rem;
      font-weight: 500;
      opacity: 0.95;
    }

    .quiz-card {
      background: #f8fafc;
      border: 1.5px solid var(--border);
      border-radius: var(--radius-md);
      padding: 1.65rem;
      margin: 1.45rem 0;
      transition: border-color 0.2s ease;
    }

    .quiz-question-text {
      font-weight: 700;
      font-size: 1.05rem;
      color: var(--dark);
      margin-bottom: 1.15rem;
      line-height: 1.6;
    }

    .quiz-options {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      margin-bottom: 1.15rem;
    }

    .quiz-opt-btn {
      background: #ffffff;
      border: 1.5px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 0.85rem 1.15rem;
      text-align: left;
      font-size: 0.95rem;
      font-weight: 500;
      color: var(--text);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      transition: all 0.2s ease;
    }

    .quiz-opt-btn:hover:not(.evaluated) {
      border-color: var(--secondary);
      background: #f0f9ff;
      transform: translateX(4px);
    }

    .quiz-opt-btn.correct-opt {
      background: #dcfce7 !important;
      border-color: #10b981 !important;
      color: #065f46 !important;
      font-weight: 700;
    }

    .quiz-opt-btn.wrong-opt {
      background: #ffe4e6 !important;
      border-color: #f43f5e !important;
      color: #881337 !important;
      font-weight: 700;
    }

    /* Back To Top Floating Button */
    #backToTopBtn {
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      background: var(--primary);
      color: white;
      border: none;
      width: 48px;
      height: 48px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
      opacity: 0;
      visibility: hidden;
      transition: all 0.3s ease;
      z-index: 9999;
    }

    #backToTopBtn.visible {
      opacity: 1;
      visibility: visible;
    }

    #backToTopBtn:hover {
      background: var(--primary-dark);
      transform: translateY(-3px);
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
    }

    /* Responsive Adjustments */
    @media (max-width: 768px) {
      .hero-title { font-size: 2.1rem; }
      .hero-sub { font-size: 1.02rem; }
      .section-card { padding: 1.75rem 1.25rem; }
      .nav-links { display: none; }
      .top-nav { padding: 0 1rem; }
    }
  </style>
</head>
<body>

  <!-- Top-Fixed Reading Progress Bar -->
  <div id="reading-progress-bar"></div>

  <!-- Sticky Top Navigation -->
  <header class="top-nav">
    <a href="../../index.html" class="nav-brand">
      <i class="fa-solid fa-graduation-cap"></i>
      <span>Sujit Classes</span>
    </a>
    <nav class="nav-links">
      <a href="#sec1" class="nav-link"><i class="fa-solid fa-sitemap"></i> Blueprint</a>
      <a href="#sec2" class="nav-link"><i class="fa-solid fa-book-open"></i> Core Concepts</a>
      <a href="#sec3" class="nav-link"><i class="fa-solid fa-table-list"></i> Fact Bank</a>
      <a href="#sec4" class="nav-link"><i class="fa-solid fa-circle-check"></i> Solved NCERT</a>
      <a href="#sec5" class="nav-link"><i class="fa-solid fa-clipboard-question"></i> Exam Bank</a>
      <a href="#sec6" class="nav-link"><i class="fa-solid fa-triangle-exclamation"></i> Traps &amp; Revision</a>
    </nav>
    <div class="nav-controls">
      <button class="control-btn" onclick="toggleAllAnswers(true)" title="Expand all answer boxes">
        <i class="fa-solid fa-angles-down"></i> Expand All
      </button>
      <button class="control-btn" onclick="toggleAllAnswers(false)" title="Collapse all answer boxes">
        <i class="fa-solid fa-angles-up"></i> Collapse
      </button>
    </div>
  </header>

  <!-- Hero Banner -->
  <section class="hero-banner">
    <div class="hero-badge">
      <i class="fa-solid fa-seedling"></i> NCERT NEP 2020 • Grade 8 Social Science • Code: hess101
    </div>
    <h1 class="hero-title">Natural Resources and Their Use: Stewardship, Cycles &amp; Sustainable Futures</h1>
    <p class="hero-sub">
      A zero-omission, exhaustive master study note exploring when Nature becomes a resource, the regenerative rhythms of the Earth, the Paradox of Plenty, real-world crises in Punjab and cement manufacturing, ancient ecological wisdom (*Vrikshayurveda*), Sikkim's organic triumph, and India's global solar leadership through the International Solar Alliance.
    </p>
    <div class="hero-meta">
      <span><i class="fa-solid fa-book"></i> Textbook: Exploring Society: India &amp; Beyond</span>
      <span><i class="fa-solid fa-layer-group"></i> Unit: Land and the People</span>
      <span><i class="fa-solid fa-language"></i> Medium: English (with Odia Vocabulary)</span>
      <span><i class="fa-solid fa-star"></i> Benchmark: 100% NCERT Solutions &amp; CBSE Exam Bank</span>
    </div>
    <div class="hero-actions">
      <button id="teacherAudioBtn" class="audio-btn" onclick="toggleTeacherAudio()">
        <i class="fa-solid fa-volume-high"></i>
        <span>Listen to Teacher's Master Summary</span>
      </button>
      <a href="#sec4" class="hero-secondary-btn">
        <i class="fa-solid fa-list-check"></i> View Solved Textbook Exercises
      </a>
      <a href="#sec5" class="hero-secondary-btn">
        <i class="fa-solid fa-circle-question"></i> Practice Interactive Quiz
      </a>
    </div>
  </section>

  <!-- Main Content Container -->
  <main class="main-container">
"""
