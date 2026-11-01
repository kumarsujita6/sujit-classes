# -*- coding: utf-8 -*-
"""
Part 1: HTML Head, Typography, Custom Responsive CSS, Fixed Top Navigation,
Hero Section, and Interactive Audio Reader Bar for Class 8 SST Chapter 9.
Chapter: India's Long Road to Independence (NCERT NEP Code: hess109 / hees202)
"""

PART1_CONTENT = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>India's Long Road to Independence - Class 8 Social Science NEP Master Study Note | Sujit Classes</title>
  <!-- Google Fonts: Space Grotesk, Plus Jakarta Sans, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Space+Grotesk:wght@500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <!-- Font Awesome 6 -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
  :root {
    --primary: #c2410c;           /* Tiranga Saffron / Terracotta Amber */
    --primary-dark: #9a3412;      /* Deep Rust Mahogany */
    --primary-light: #ffedd5;     /* Warm Saffron Glow */
    --primary-ultra-light: #fff7ed;
    --secondary: #0f766e;         /* Deep Forest Teal / Tiranga Green */
    --secondary-dark: #115e59;
    --secondary-light: #ccfbf1;
    --accent: #1d4ed8;            /* Ashoka Chakra Navy Blue */
    --accent-dark: #1e40af;
    --accent-light: #dbeafe;
    --earth-green: #15803d;       /* Emerald Independence Green */
    --earth-light: #dcfce7;
    --maroon: #991b1b;            /* Martyr Red / Historical Crimson */
    --maroon-light: #fee2e2;
    --dark: #0f172a;              /* Midnight Slate */
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
    line-height: 1.78;
    font-size: 15.5px;
    padding-top: 60px;
  }

  /* Top Reading Progress Bar */
  #reading-progress-bar {
    position: fixed;
    top: 0;
    left: 0;
    width: 0%;
    height: 4px;
    background: linear-gradient(90deg, #ea580c 0%, #1d4ed8 50%, #15803d 100%);
    z-index: 9999;
    transition: width 0.12s ease-out;
  }

  /* Fixed Top Navigation */
  .top-nav {
    position: fixed;
    top: 4px;
    left: 0;
    right: 0;
    height: 56px;
    background: rgba(255, 255, 255, 0.96);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 1.5rem;
    z-index: 1000;
    box-shadow: var(--shadow-sm);
  }

  .nav-brand {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    text-decoration: none;
    color: var(--dark);
    font-weight: 700;
    font-size: 1.05rem;
    font-family: 'Space Grotesk', sans-serif;
  }

  .brand-badge {
    background: linear-gradient(135deg, #c2410c, #ea580c);
    color: white;
    padding: 0.25rem 0.6rem;
    border-radius: var(--radius-sm);
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }

  .nav-actions {
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }

  .btn-audio-listen {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: var(--primary-light);
    color: var(--primary-dark);
    border: 1px solid rgba(194, 65, 12, 0.25);
    padding: 0.4rem 0.85rem;
    border-radius: 9999px;
    font-size: 0.82rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
  }

  .btn-audio-listen:hover {
    background: #fed7aa;
    transform: translateY(-1px);
  }

  .btn-portal-back {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: #f1f5f9;
    color: var(--dark);
    border: 1px solid var(--border);
    padding: 0.4rem 0.85rem;
    border-radius: var(--radius-sm);
    font-size: 0.82rem;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.2s ease;
  }

  .btn-portal-back:hover {
    background: #e2e8f0;
  }

  /* Quick Navigation Bar */
  .quick-nav-bar {
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    padding: 0.6rem 1rem;
    display: flex;
    gap: 0.5rem;
    overflow-x: auto;
    white-space: nowrap;
    position: sticky;
    top: 60px;
    z-index: 900;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02);
  }

  .quick-nav-pill {
    padding: 0.35rem 0.75rem;
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--text-muted);
    text-decoration: none;
    border-radius: 9999px;
    background: #f1f5f9;
    transition: all 0.2s ease;
  }

  .quick-nav-pill:hover, .quick-nav-pill.active {
    background: var(--primary);
    color: white;
  }

  /* Main Container */
  .container {
    max-width: 1040px;
    margin: 0 auto;
    padding: 2rem 1.25rem 4rem;
  }

  /* Hero Section */
  .hero-card {
    background: linear-gradient(135deg, #fff7ed 0%, #ffffff 50%, #f0fdf4 100%);
    border: 1px solid rgba(194, 65, 12, 0.2);
    border-radius: var(--radius-xl);
    padding: 2.5rem 2rem;
    margin-bottom: 2.5rem;
    box-shadow: var(--shadow-md);
    position: relative;
    overflow: hidden;
  }

  .hero-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 5px;
    background: linear-gradient(90deg, #ea580c 0%, #1d4ed8 50%, #15803d 100%);
  }

  .hero-badge-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1.25rem;
  }

  .hero-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    padding: 0.25rem 0.7rem;
    border-radius: 9999px;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.4px;
    text-transform: uppercase;
  }

  .hero-pill-primary {
    background: #ffedd5;
    color: #9a3412;
    border: 1px solid #fed7aa;
  }

  .hero-pill-secondary {
    background: #dcfce7;
    color: #14532d;
    border: 1px solid #bbf7d0;
  }

  .hero-pill-blue {
    background: #dbeafe;
    color: #1e40af;
    border: 1px solid #bfdbfe;
  }

  .hero-pill-accent {
    background: #fef3c7;
    color: #92400e;
    border: 1px solid #fde68a;
  }

  .hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.4rem;
    font-weight: 800;
    color: var(--dark);
    line-height: 1.25;
    margin-bottom: 0.75rem;
    letter-spacing: -0.5px;
  }

  .hero-subtitle {
    font-size: 1.15rem;
    color: var(--text-muted);
    margin-bottom: 1.5rem;
    font-weight: 500;
    max-width: 860px;
    line-height: 1.6;
  }

  .hero-meta-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
    gap: 1rem;
    padding-top: 1.25rem;
    border-top: 1px solid var(--border);
  }

  .hero-meta-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }

  .hero-meta-icon {
    width: 38px;
    height: 38px;
    border-radius: var(--radius-sm);
    background: var(--surface);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--primary);
    box-shadow: var(--shadow-sm);
    font-size: 1rem;
  }

  .hero-meta-text {
    font-size: 0.8rem;
    line-height: 1.35;
  }

  .hero-meta-label {
    color: var(--text-muted);
    font-size: 0.72rem;
    text-transform: uppercase;
    font-weight: 600;
  }

  .hero-meta-val {
    color: var(--dark);
    font-weight: 700;
  }

  /* Audio Reader Bar Card */
  .audio-bar-card {
    background: #ffffff;
    border: 1px solid #fed7aa;
    border-radius: var(--radius-md);
    padding: 1rem 1.25rem;
    margin-top: 1.5rem;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    box-shadow: var(--shadow-sm);
  }

  .audio-bar-info {
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }

  .audio-bar-icon {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: #ffedd5;
    color: #c2410c;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.95rem;
  }

  .audio-bar-title {
    font-weight: 700;
    font-size: 0.9rem;
    color: var(--dark);
  }

  .audio-bar-desc {
    font-size: 0.78rem;
    color: var(--text-muted);
  }

  .audio-bar-controls {
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .audio-btn {
    padding: 0.35rem 0.75rem;
    border-radius: var(--radius-sm);
    font-size: 0.78rem;
    font-weight: 600;
    border: none;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    transition: all 0.2s ease;
  }

  .audio-btn-primary {
    background: var(--primary);
    color: white;
  }

  .audio-btn-primary:hover {
    background: var(--primary-dark);
  }

  .audio-btn-secondary {
    background: #f1f5f9;
    color: var(--text);
    border: 1px solid var(--border);
  }

  .audio-btn-secondary:hover {
    background: #e2e8f0;
  }

  /* Section Styling */
  .section-wrapper {
    margin-bottom: 3.5rem;
  }

  .section-header {
    margin-bottom: 2rem;
    padding-bottom: 1rem;
    border-bottom: 2px solid var(--border);
  }

  .section-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: #ffedd5;
    color: #9a3412;
    padding: 0.25rem 0.7rem;
    border-radius: 9999px;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 0.5rem;
  }

  .section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.85rem;
    font-weight: 700;
    color: var(--dark);
    line-height: 1.3;
  }

  .section-desc {
    font-size: 0.98rem;
    color: var(--text-muted);
    margin-top: 0.4rem;
  }

  /* Concept Cards */
  .concept-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 1.75rem;
    margin-bottom: 1.75rem;
    box-shadow: var(--shadow-sm);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }

  .concept-card:hover {
    box-shadow: var(--shadow-md);
  }

  .concept-card-header {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    margin-bottom: 1.25rem;
  }

  .concept-card-icon {
    width: 44px;
    height: 44px;
    border-radius: var(--radius-md);
    background: #ffedd5;
    color: #c2410c;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    flex-shrink: 0;
  }

  .concept-card-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.35rem;
    font-weight: 700;
    color: var(--dark);
    line-height: 1.35;
  }

  .concept-card-subtitle {
    font-size: 0.85rem;
    color: var(--text-muted);
    margin-top: 0.2rem;
  }

  .concept-card-body p {
    margin-bottom: 1rem;
  }

  .concept-card-body ul, .concept-card-body ol {
    margin-left: 1.5rem;
    margin-bottom: 1rem;
  }

  .concept-card-body li {
    margin-bottom: 0.45rem;
  }

  /* Pastel Callout Boxes */
  .callout-box {
    border-radius: var(--radius-md);
    padding: 1.25rem 1.5rem;
    margin: 1.35rem 0;
    border-left: 4px solid transparent;
  }

  .callout-title {
    font-weight: 700;
    font-size: 0.95rem;
    margin-bottom: 0.45rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-family: 'Space Grotesk', sans-serif;
  }

  .callout-def {
    background: #eff6ff;
    border-left-color: #2563eb;
    color: #1e3a8a;
  }
  .callout-def .callout-title { color: #1e40af; }

  .callout-act {
    background: #f0fdf4;
    border-left-color: #16a34a;
    color: #14532d;
  }
  .callout-act .callout-title { color: #15803d; }

  .callout-pyq {
    background: #fff7ed;
    border-left-color: #ea580c;
    color: #7c2d12;
  }
  .callout-pyq .callout-title { color: #c2410c; }

  .callout-hack {
    background: #faf5ff;
    border-left-color: #9333ea;
    color: #581c87;
  }
  .callout-hack .callout-title { color: #7e22ce; }

  .callout-warn {
    background: #fef2f2;
    border-left-color: #dc2626;
    color: #7f1d1d;
  }
  .callout-warn .callout-title { color: #b91c1c; }

  /* Responsive Tables */
  .table-responsive {
    overflow-x: auto;
    margin: 1.5rem 0;
    border-radius: var(--radius-md);
    border: 1px solid var(--border);
    background: var(--surface);
    box-shadow: var(--shadow-sm);
  }

  .data-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9rem;
    text-align: left;
  }

  .data-table th {
    background: #fff7ed;
    color: #9a3412;
    font-weight: 700;
    padding: 0.85rem 1rem;
    border-bottom: 2px solid #fed7aa;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  .data-table td {
    padding: 0.8rem 1rem;
    border-bottom: 1px solid var(--border);
    vertical-align: top;
  }

  .data-table tr:last-child td {
    border-bottom: none;
  }

  .data-table tr:hover td {
    background: #fffaf0;
  }

  .data-table .badge {
    display: inline-block;
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 700;
  }

  /* Collapsible Details Answer Box */
  .ans-box {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    margin-bottom: 1.25rem;
    overflow: hidden;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
  }

  .ans-box[open] {
    border-color: #fed7aa;
    box-shadow: var(--shadow-sm);
  }

  .ans-summary {
    padding: 1rem 1.25rem;
    font-weight: 700;
    color: var(--dark);
    cursor: pointer;
    background: #ffffff;
    display: flex;
    align-items: center;
    justify-content: space-between;
    list-style: none;
    user-select: none;
    font-size: 0.98rem;
  }

  .ans-summary::-webkit-details-marker {
    display: none;
  }

  .ans-summary::after {
    content: '\\f078';
    font-family: 'Font Awesome 6 Free';
    font-weight: 900;
    font-size: 0.85rem;
    color: var(--primary);
    transition: transform 0.25s ease;
  }

  .ans-box[open] .ans-summary::after {
    transform: rotate(180deg);
  }

  .ans-summary:hover {
    background: #fffaf0;
  }

  .ans-content {
    padding: 1.25rem;
    border-top: 1px solid var(--border);
    background: #fafafa;
    font-size: 0.95rem;
  }

  /* 5-Step Presentation Inside Answers */
  .step-card {
    background: #ffffff;
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    padding: 0.85rem 1.1rem;
    margin-bottom: 0.75rem;
    position: relative;
    border-left: 3px solid var(--primary);
  }

  .step-label {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    font-size: 0.72rem;
    font-weight: 800;
    text-transform: uppercase;
    color: var(--primary);
    letter-spacing: 0.5px;
    margin-bottom: 0.3rem;
  }

  .step-text {
    font-size: 0.92rem;
    color: var(--text);
    line-height: 1.6;
  }

  /* Quiz Interactive Engine */
  .quiz-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    box-shadow: var(--shadow-sm);
  }

  .quiz-q-title {
    font-weight: 700;
    font-size: 1.05rem;
    color: var(--dark);
    margin-bottom: 1rem;
  }

  .quiz-options-list {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    margin-bottom: 1rem;
  }

  .quiz-opt-btn {
    text-align: left;
    padding: 0.75rem 1rem;
    background: #f8fafc;
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    font-size: 0.92rem;
    cursor: pointer;
    font-family: inherit;
    color: var(--text);
    display: flex;
    align-items: center;
    transition: all 0.2s ease;
  }

  .quiz-opt-btn:hover:not(:disabled) {
    background: #f1f5f9;
    border-color: #cbd5e1;
    transform: translateX(4px);
  }

  .quiz-opt-btn.correct {
    background: #dcfce7 !important;
    border-color: #22c55e !important;
    color: #14532d !important;
    font-weight: 700;
  }

  .quiz-opt-btn.incorrect {
    background: #fee2e2 !important;
    border-color: #ef4444 !important;
    color: #7f1d1d !important;
  }

  .quiz-feedback {
    display: none;
    padding: 0.85rem 1rem;
    border-radius: var(--radius-sm);
    font-size: 0.88rem;
    line-height: 1.5;
  }

  .quiz-feedback.show {
    display: block;
    margin-top: 0.75rem;
    animation: fadeIn 0.3s ease;
  }

  .quiz-feedback.correct-feedback {
    background: #dcfce7;
    border: 1px solid #86efac;
    color: #14532d;
  }

  .quiz-feedback.incorrect-feedback {
    background: #fef2f2;
    border: 1px solid #fca5a5;
    color: #991b1b;
  }

  /* Blunder Traps & Corrections */
  .blunder-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.25rem;
    margin-top: 1.25rem;
  }

  .blunder-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    padding: 1.25rem;
    box-shadow: var(--shadow-sm);
  }

  .blunder-trap {
    background: #fef2f2;
    border-left: 3px solid #dc2626;
    padding: 0.6rem 0.85rem;
    border-radius: 4px;
    font-size: 0.88rem;
    color: #7f1d1d;
    margin-bottom: 0.75rem;
  }

  .blunder-fix {
    background: #f0fdf4;
    border-left: 3px solid #16a34a;
    padding: 0.6rem 0.85rem;
    border-radius: 4px;
    font-size: 0.88rem;
    color: #14532d;
  }

  /* Diagram Container & Micro Animations */
  .diagram-container {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 1.5rem;
    margin: 2rem 0;
    box-shadow: var(--shadow-sm);
    text-align: center;
  }

  .diagram-title {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 1.1rem;
    color: var(--dark);
    margin-bottom: 0.5rem;
  }

  .diagram-caption {
    font-size: 0.85rem;
    color: var(--text-muted);
    margin-top: 0.75rem;
  }

  svg {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 0 auto;
  }

  /* SVG Micro-animations */
  .svg-glow-hover {
    transition: filter 0.3s ease, transform 0.3s ease;
    cursor: pointer;
  }

  .svg-glow-hover:hover {
    filter: drop-shadow(0 0 8px rgba(234, 88, 12, 0.45));
    transform: scale(1.015);
  }

  .svg-pulse-path {
    stroke-dasharray: 8;
    animation: dashPulse 25s linear infinite;
  }

  @keyframes dashPulse {
    from { stroke-dashoffset: 200; }
    to { stroke-dashoffset: 0; }
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(-4px); }
    to { opacity: 1; transform: translateY(0); }
  }

  /* Media Queries */
  @media (max-width: 768px) {
    .hero-title { font-size: 1.85rem; }
    .hero-card { padding: 1.75rem 1.25rem; }
    .quick-nav-bar { top: 56px; }
    .top-nav { padding: 0 1rem; }
  }
  </style>
</head>
<body>

  <!-- 1. Top Reading Progress Bar -->
  <div id="reading-progress-bar"></div>

  <!-- 2. Fixed Top Navigation -->
  <header class="top-nav">
    <a href="../../index.html" class="nav-brand">
      <i class="fa-solid fa-graduation-cap" style="color: #c2410c;"></i>
      <span>Sujit Classes</span>
      <span class="brand-badge">Class 8 SST</span>
    </a>
    <div class="nav-actions">
      <button class="btn-audio-listen" id="btn-quick-listen" onclick="toggleAudioReader()">
        <i class="fa-solid fa-volume-high"></i>
        <span>Listen to Summary</span>
      </button>
      <a href="../../index.html" class="btn-portal-back">
        <i class="fa-solid fa-arrow-left"></i>
        <span>Portal</span>
      </a>
    </div>
  </header>

  <!-- 3. Sticky Quick Navigation Bar -->
  <nav class="quick-nav-bar">
    <a href="#section-1" class="quick-nav-pill active"><i class="fa-solid fa-diagram-project"></i> 1. Visual Blueprint</a>
    <a href="#section-2" class="quick-nav-pill"><i class="fa-solid fa-book-open"></i> 2. Deep Concepts</a>
    <a href="#glossary" class="quick-nav-pill"><i class="fa-solid fa-language"></i> Bilingual Glossary</a>
    <a href="#section-3" class="quick-nav-pill"><i class="fa-solid fa-bolt"></i> 3. Rapid Revision</a>
    <a href="#section-4" class="quick-nav-pill"><i class="fa-solid fa-clipboard-check"></i> 4. 100% Solved NCERT</a>
    <a href="#section-5" class="quick-nav-pill"><i class="fa-solid fa-graduation-cap"></i> 5. Exam Question Bank</a>
    <a href="#section-6" class="quick-nav-pill"><i class="fa-solid fa-triangle-exclamation"></i> 6. Traps & Blunders</a>
  </nav>

  <!-- Main Container -->
  <main class="container">

    <!-- Hero Card -->
    <section class="hero-card">
      <div class="hero-badge-row">
        <span class="hero-pill hero-pill-primary"><i class="fa-solid fa-landmark"></i> CBSE Class 8 History</span>
        <span class="hero-pill hero-pill-blue"><i class="fa-solid fa-book"></i> NCERT NEP hess109</span>
        <span class="hero-pill hero-pill-secondary"><i class="fa-solid fa-certificate"></i> Zero-Omission Master Note</span>
        <span class="hero-pill hero-pill-accent"><i class="fa-solid fa-fire"></i> 90-Year Freedom Saga</span>
      </div>

      <h1 class="hero-title">India's Long Road to Independence</h1>
      <p class="hero-subtitle">
        An exhaustive, classroom-level master study note chronicling India's ninety-year odyssey from the 1857 Great Rebellion to the midnight dawn of 15 August 1947. Discover how a subcontinent of diverse languages, religions, and regions united through socio-religious awakening, constitutional struggle, armed revolutionary heroism, and unprecedented mass nonviolent satyagraha to overthrow the world's mightiest colonial empire.
      </p>

      <div class="hero-meta-grid">
        <div class="hero-meta-item">
          <div class="hero-meta-icon"><i class="fa-regular fa-clock"></i></div>
          <div class="hero-meta-text">
            <div class="hero-meta-label">Study Duration</div>
            <div class="hero-meta-val">55 – 65 Mins</div>
          </div>
        </div>
        <div class="hero-meta-item">
          <div class="hero-meta-icon"><i class="fa-solid fa-scroll"></i></div>
          <div class="hero-meta-text">
            <div class="hero-meta-label">Curricular Code</div>
            <div class="hero-meta-val">Part 2 Ch 2 (hess109)</div>
          </div>
        </div>
        <div class="hero-meta-item">
          <div class="hero-meta-icon"><i class="fa-solid fa-layer-group"></i></div>
          <div class="hero-meta-text">
            <div class="hero-meta-label">Pedagogical Breadth</div>
            <div class="hero-meta-val">6 Core Sections</div>
          </div>
        </div>
        <div class="hero-meta-item">
          <div class="hero-meta-icon"><i class="fa-solid fa-award"></i></div>
          <div class="hero-meta-text">
            <div class="hero-meta-label">Board Alignment</div>
            <div class="hero-meta-val">CBSE + BSE Odisha</div>
          </div>
        </div>
      </div>

      <!-- Audio Reader Bar Card -->
      <div class="audio-bar-card" id="audio-companion">
        <div class="audio-bar-info">
          <div class="audio-bar-icon"><i class="fa-solid fa-headphones-simple"></i></div>
          <div>
            <div class="audio-bar-title">Interactive Audio Reader Companion</div>
            <div class="audio-bar-desc">Listen to an engaging teacher-voiced narrative of this chapter using browser speech synthesis.</div>
          </div>
        </div>
        <div class="audio-bar-controls">
          <button class="audio-btn audio-btn-primary" id="btn-audio-play" onclick="toggleAudioReader()">
            <i class="fa-solid fa-play"></i>
            <span id="audio-btn-label">Play Narration</span>
          </button>
          <button class="audio-btn audio-btn-secondary" onclick="stopAudioReader()">
            <i class="fa-solid fa-stop"></i>
            <span>Stop</span>
          </button>
        </div>
      </div>
    </section>
'''
