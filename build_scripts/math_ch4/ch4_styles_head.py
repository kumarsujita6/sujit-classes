# -*- coding: utf-8 -*-
"""
Module: ch4_styles_head.py
Contains HTML head, metadata, typography, complete CSS stylesheet, top navbar,
reading progress bar, hero banner, audio player component, and quick navigation pills.
"""

def get_head_and_hero():
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quadrilaterals - Class 8 Mathematics Chapter 4 Master Study Notes (Ganita Prakash) | Sujit Classes</title>
  <meta name="description" content="Exhaustive, zero-omission teacher notes for Class 8 Mathematics Chapter 4: Quadrilaterals (NCERT Ganita Prakash NEP 2020 code: hegp104). Features complete angle sum proofs, the Carpenter's Problem, 10 deductions, Euler-Venn taxonomy, parallelograms, rhombuses, rectangles, squares, trapeziums, kites, and 100% solved exercises.">
  <!-- Google Fonts: Space Grotesk, Plus Jakarta Sans, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Space+Grotesk:wght@500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <!-- Font Awesome 6.4.0 -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <style>
    :root {
      --primary: #2563eb;
      --primary-dark: #1d4ed8;
      --primary-light: #dbeafe;
      --primary-ultra-light: #eff6ff;
      --secondary: #059669;
      --secondary-dark: #047857;
      --secondary-light: #d1fae5;
      --secondary-ultra-light: #ecfdf5;
      --accent: #d97706;
      --accent-dark: #b45309;
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
      line-height: 1.75;
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
      background: linear-gradient(90deg, #2563eb, #059669, #7c3aed, #d97706);
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
    .nav-links a {
      text-decoration: none;
      color: var(--text-muted);
      font-weight: 600;
      font-size: 0.925rem;
      transition: color 0.2s ease;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }
    .nav-links a:hover {
      color: var(--primary);
    }
    .nav-badge {
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.25rem 0.65rem;
      border-radius: 9999px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    /* CONTAINER & LAYOUT */
    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 2.5rem 1.5rem 5rem 1.5rem;
    }

    /* HERO BANNER */
    .hero-banner {
      background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #1e3a8a 100%);
      color: white;
      border-radius: var(--radius-xl);
      padding: 3.5rem 3rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow-xl);
      position: relative;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .hero-banner::before {
      content: '';
      position: absolute;
      top: -50%;
      right: -20%;
      width: 500px;
      height: 500px;
      background: radial-gradient(circle, rgba(37, 99, 235, 0.25) 0%, rgba(0, 0, 0, 0) 70%);
      border-radius: 50%;
      pointer-events: none;
    }
    .hero-banner::after {
      content: '';
      position: absolute;
      bottom: -30%;
      left: 10%;
      width: 400px;
      height: 400px;
      background: radial-gradient(circle, rgba(124, 58, 237, 0.2) 0%, rgba(0, 0, 0, 0) 70%);
      border-radius: 50%;
      pointer-events: none;
    }
    .hero-badge-group {
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem;
      margin-bottom: 1.25rem;
    }
    .hero-pill {
      background: rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(8px);
      color: #e0f2fe;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.35rem 0.9rem;
      border-radius: 9999px;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      border: 1px solid rgba(255, 255, 255, 0.2);
    }
    .hero-pill.gold {
      background: rgba(245, 158, 11, 0.25);
      color: #fef3c7;
      border-color: rgba(245, 158, 11, 0.4);
    }
    .hero-pill.emerald {
      background: rgba(16, 185, 129, 0.25);
      color: #d1fae5;
      border-color: rgba(16, 185, 129, 0.4);
    }
    .hero-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 2.85rem;
      font-weight: 800;
      line-height: 1.2;
      margin-bottom: 1rem;
      letter-spacing: -0.02em;
    }
    .hero-subtitle {
      font-size: 1.15rem;
      color: #cbd5e1;
      max-width: 880px;
      line-height: 1.65;
      margin-bottom: 2rem;
    }
    .hero-stats {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 1.25rem;
      margin-top: 2rem;
      border-top: 1px solid rgba(255, 255, 255, 0.15);
      padding-top: 1.75rem;
    }
    .stat-card {
      background: rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-md);
      padding: 1rem 1.25rem;
      border: 1px solid rgba(255, 255, 255, 0.12);
    }
    .stat-value {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.6rem;
      font-weight: 700;
      color: #60a5fa;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .stat-label {
      font-size: 0.85rem;
      color: #94a3b8;
      font-weight: 500;
      margin-top: 0.25rem;
    }

    /* AUDIO PLAYER CARD */
    .audio-player-card {
      background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
      color: white;
      border-radius: var(--radius-lg);
      padding: 1.5rem 2rem;
      margin-bottom: 2.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem;
      box-shadow: var(--shadow-lg);
      border: 1px solid rgba(255, 255, 255, 0.1);
      flex-wrap: wrap;
    }
    .audio-info {
      display: flex;
      align-items: center;
      gap: 1.25rem;
    }
    .audio-icon-btn {
      width: 52px;
      height: 52px;
      border-radius: 50%;
      background: linear-gradient(135deg, #2563eb, #7c3aed);
      border: none;
      color: white;
      font-size: 1.25rem;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.4);
      transition: transform 0.2s ease, box-shadow 0.2s ease;
      flex-shrink: 0;
    }
    .audio-icon-btn:hover {
      transform: scale(1.06);
      box-shadow: 0 6px 16px rgba(37, 99, 235, 0.6);
    }
    .audio-text h4 {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.1rem;
      font-weight: 700;
      color: #f8fafc;
    }
    .audio-text p {
      font-size: 0.875rem;
      color: #94a3b8;
      margin-top: 0.2rem;
    }
    .audio-controls-right {
      display: flex;
      align-items: center;
      gap: 1rem;
    }
    .speech-rate-select {
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: white;
      padding: 0.4rem 0.8rem;
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      outline: none;
      cursor: pointer;
    }
    .speech-rate-select option {
      background: #0f172a;
      color: white;
    }

    /* QUICK NAVIGATION PILLS */
    .quick-nav-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
      margin-bottom: 3rem;
      background: var(--surface);
      padding: 1.25rem;
      border-radius: var(--radius-lg);
      border: 1px solid var(--border);
      box-shadow: var(--shadow-sm);
    }
    .quick-pill {
      text-decoration: none;
      background: var(--light);
      color: var(--text);
      font-size: 0.9rem;
      font-weight: 600;
      padding: 0.5rem 1rem;
      border-radius: var(--radius-md);
      border: 1px solid var(--border);
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.2s ease;
    }
    .quick-pill:hover {
      background: var(--primary-light);
      color: var(--primary-dark);
      border-color: var(--primary);
      transform: translateY(-2px);
    }
    .quick-pill i {
      color: var(--primary);
    }

    /* SECTION STYLING */
    section {
      background: var(--surface);
      border-radius: var(--radius-xl);
      padding: 3rem 2.5rem;
      margin-bottom: 3rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow-sm);
    }
    .section-header {
      margin-bottom: 2.25rem;
      border-bottom: 2px solid var(--border);
      padding-bottom: 1.25rem;
    }
    .section-tag {
      font-family: 'Space Grotesk', sans-serif;
      text-transform: uppercase;
      font-size: 0.8rem;
      font-weight: 800;
      color: var(--primary);
      letter-spacing: 0.1em;
      margin-bottom: 0.35rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .section-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 2.15rem;
      font-weight: 800;
      color: var(--dark);
      line-height: 1.25;
      letter-spacing: -0.015em;
    }
    .section-desc {
      font-size: 1.05rem;
      color: var(--text-muted);
      margin-top: 0.5rem;
      max-width: 950px;
    }

    /* SUBHEADINGS */
    h3.subheading {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.5rem;
      font-weight: 700;
      color: var(--dark);
      margin: 2.5rem 0 1.25rem 0;
      display: flex;
      align-items: center;
      gap: 0.65rem;
    }
    h3.subheading i {
      color: var(--primary);
      font-size: 1.3rem;
    }
    h4.subheading-sm {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.2rem;
      font-weight: 700;
      color: #1e293b;
      margin: 1.75rem 0 0.85rem 0;
    }

    /* PARAGRAPHS & LISTS */
    p {
      margin-bottom: 1.15rem;
      color: var(--text);
    }
    ul, ol {
      margin-bottom: 1.25rem;
      padding-left: 1.5rem;
    }
    li {
      margin-bottom: 0.45rem;
    }

    /* PASTEL CALLOUT BOXES */
    .callout {
      border-radius: var(--radius-md);
      padding: 1.4rem 1.6rem;
      margin: 1.75rem 0;
      border-left: 5px solid;
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
    .callout p:last-child, .callout ul:last-child {
      margin-bottom: 0;
    }
    .callout-def {
      background-color: var(--primary-ultra-light);
      border-left-color: var(--primary);
      color: #1e3a8a;
    }
    .callout-def .callout-title {
      color: var(--primary-dark);
    }
    .callout-act {
      background-color: var(--secondary-ultra-light);
      border-left-color: var(--secondary);
      color: #064e3b;
    }
    .callout-act .callout-title {
      color: var(--secondary-dark);
    }
    .callout-pyq {
      background-color: #fbf5ff;
      border-left-color: var(--purple);
      color: #4c1d95;
    }
    .callout-pyq .callout-title {
      color: var(--purple-dark);
    }
    .callout-hack {
      background-color: #fffbeb;
      border-left-color: var(--accent);
      color: #78350f;
    }
    .callout-hack .callout-title {
      color: var(--accent-dark);
    }
    .callout-warn {
      background-color: #fff1f2;
      border-left-color: var(--danger);
      color: #881337;
    }
    .callout-warn .callout-title {
      color: var(--danger-dark);
    }

    /* STEP-BY-STEP PROBLEM CONTAINERS */
    .step-container {
      margin-top: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 0.9rem;
    }
    .step-box {
      border-radius: var(--radius-sm);
      padding: 1rem 1.25rem;
      border: 1px solid var(--border);
      background: #fafafa;
    }
    .step-badge {
      display: inline-block;
      font-size: 0.775rem;
      font-weight: 800;
      padding: 0.2rem 0.55rem;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.5rem;
    }
    .step-1 { border-left: 4px solid #3b82f6; }
    .step-1 .step-badge { background: #dbeafe; color: #1e40af; }
    .step-2 { border-left: 4px solid #10b981; }
    .step-2 .step-badge { background: #d1fae5; color: #065f46; }
    .step-3 { border-left: 4px solid #f59e0b; }
    .step-3 .step-badge { background: #fef3c7; color: #92400e; }
    .step-4 { border-left: 4px solid #8b5cf6; }
    .step-4 .step-badge { background: #ede9fe; color: #5b21b6; }
    .step-5 { border-left: 4px solid #ec4899; }
    .step-5 .step-badge { background: #fce7f3; color: #9d174d; }

    /* COLLAPSIBLE DETAILS ANS-BOX */
    details.ans-box {
      background: var(--light);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      margin: 1.4rem 0;
      overflow: hidden;
      transition: all 0.2s ease;
    }
    details.ans-box[open] {
      box-shadow: var(--shadow-md);
      border-color: #cbd5e1;
    }
    details.ans-box summary {
      padding: 1.1rem 1.5rem;
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      font-size: 1.05rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      user-select: none;
      background: #ffffff;
      transition: background-color 0.2s ease;
    }
    details.ans-box summary:hover {
      background-color: var(--primary-ultra-light);
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
      line-height: 1.75;
    }

    /* DATA TABLES */
    .table-container {
      overflow-x: auto;
      margin: 1.75rem 0;
      border-radius: var(--radius-md);
      border: 1px solid var(--border);
      box-shadow: var(--shadow-sm);
    }
    table.data-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.95rem;
      background: white;
    }
    table.data-table th {
      background: #f1f5f9;
      color: var(--dark);
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      padding: 0.9rem 1.1rem;
      border-bottom: 2px solid var(--border-dark);
      white-space: nowrap;
    }
    table.data-table td {
      padding: 0.85rem 1.1rem;
      border-bottom: 1px solid var(--border);
      color: var(--text);
    }
    table.data-table tr:last-child td {
      border-bottom: none;
    }
    table.data-table tr:hover {
      background-color: #f8fafc;
    }
    table.data-table td strong {
      color: var(--dark);
    }

    /* SVG DIAGRAM CARDS */
    .diagram-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.75rem;
      margin: 2rem 0;
      box-shadow: var(--shadow-sm);
      text-align: center;
    }
    .diagram-card .caption {
      font-size: 0.9rem;
      color: var(--text-muted);
      margin-top: 0.85rem;
      font-weight: 500;
    }
    .svg-container {
      width: 100%;
      max-width: 900px;
      margin: 0 auto;
      display: flex;
      justify-content: center;
    }
    .svg-container svg {
      width: 100%;
      height: auto;
      display: block;
    }

    /* INTERACTIVE QUIZ MCQ CARDS */
    .quiz-score-header {
      background: linear-gradient(135deg, #2563eb, #1d4ed8);
      color: white;
      padding: 1.25rem 1.75rem;
      border-radius: var(--radius-md);
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 2rem;
    }
    .quiz-score-header h3 {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.3rem;
      margin: 0;
    }
    .score-badge {
      background: rgba(255, 255, 255, 0.2);
      font-size: 1.15rem;
      font-weight: 800;
      padding: 0.35rem 0.85rem;
      border-radius: 9999px;
      font-family: 'JetBrains Mono', monospace;
    }
    .mcq-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.75rem;
      margin-bottom: 1.5rem;
      box-shadow: var(--shadow-sm);
    }
    .mcq-question {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--dark);
      margin-bottom: 1.2rem;
    }
    .mcq-options-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.75rem;
      margin-bottom: 1rem;
    }
    @media (min-width: 640px) {
      .mcq-options-grid {
        grid-template-columns: 1fr 1fr;
      }
    }
    .option-btn {
      text-align: left;
      padding: 0.85rem 1.1rem;
      border-radius: var(--radius-sm);
      border: 1.5px solid var(--border);
      background: #f8fafc;
      color: var(--dark);
      font-size: 0.95rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .option-btn:hover:not(:disabled) {
      border-color: var(--primary);
      background: var(--primary-light);
      color: var(--primary-dark);
    }
    .option-btn.correct {
      background: #d1fae5 !important;
      border-color: #059669 !important;
      color: #065f46 !important;
    }
    .option-btn.wrong {
      background: #fee2e2 !important;
      border-color: #dc2626 !important;
      color: #991b1b !important;
    }
    .feedback-box {
      display: none;
      padding: 1rem 1.25rem;
      border-radius: var(--radius-sm);
      font-size: 0.925rem;
      margin-top: 0.75rem;
      line-height: 1.6;
    }
    .feedback-box.show {
      display: block;
    }
    .correct-feedback {
      background: #ecfdf5;
      border-left: 4px solid #10b981;
      color: #064e3b;
    }
    .wrong-feedback {
      background: #fef2f2;
      border-left: 4px solid #ef4444;
      color: #7f1d1d;
    }

    /* EXAM HALL BLUNDERS */
    .blunder-card {
      background: #ffffff;
      border-radius: var(--radius-md);
      border: 1px solid var(--border);
      padding: 1.5rem;
      margin-bottom: 1.25rem;
      box-shadow: var(--shadow-sm);
      border-left: 5px solid var(--danger);
    }
    .blunder-header {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--danger-dark);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .blunder-comparison {
      display: grid;
      grid-template-columns: 1fr;
      gap: 1rem;
      margin-top: 0.75rem;
    }
    @media (min-width: 640px) {
      .blunder-comparison {
        grid-template-columns: 1fr 1fr;
      }
    }
    .bad-box {
      background: #fef2f2;
      padding: 0.9rem;
      border-radius: var(--radius-sm);
      border: 1px solid #fecaca;
      font-size: 0.9rem;
    }
    .bad-box strong { color: #991b1b; }
    .good-box {
      background: #ecfdf5;
      padding: 0.9rem;
      border-radius: var(--radius-sm);
      border: 1px solid #a7f3d0;
      font-size: 0.9rem;
    }
    .good-box strong { color: #065f46; }

    /* REVISION POINTS LIST */
    .revision-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 1rem;
      margin-top: 1.5rem;
    }
    .revision-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 1.2rem;
      display: flex;
      gap: 0.85rem;
      align-items: flex-start;
      box-shadow: var(--shadow-sm);
    }
    .rev-num {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 800;
      font-size: 0.85rem;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      font-family: 'Space Grotesk', sans-serif;
    }
    .rev-text {
      font-size: 0.925rem;
      line-height: 1.6;
      color: var(--dark);
    }

    /* FOOTER */
    footer {
      background: var(--dark);
      color: #94a3b8;
      padding: 3rem 1.5rem;
      border-radius: var(--radius-xl);
      text-align: center;
      font-size: 0.925rem;
      margin-top: 4rem;
    }
    footer a {
      color: #60a5fa;
      text-decoration: none;
    }
    footer a:hover {
      text-decoration: underline;
    }

    /* BACK TO TOP BUTTON */
    #backToTopBtn {
      position: fixed;
      bottom: 30px;
      right: 30px;
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: var(--primary);
      color: white;
      border: none;
      cursor: pointer;
      display: none;
      align-items: center;
      justify-content: center;
      font-size: 1.2rem;
      box-shadow: var(--shadow-lg);
      z-index: 999;
      transition: transform 0.2s ease, background-color 0.2s ease;
    }
    #backToTopBtn:hover {
      background-color: var(--primary-dark);
      transform: translateY(-3px);
    }
    #backToTopBtn.visible {
      display: flex;
    }

    @media (max-width: 768px) {
      .top-nav {
        padding: 0 1rem;
      }
      .nav-links {
        display: none;
      }
      .hero-title {
        font-size: 2.15rem;
      }
      .hero-banner {
        padding: 2.5rem 1.5rem;
      }
      section {
        padding: 2rem 1.25rem;
      }
    }
  </style>
</head>
<body>

  <!-- READING PROGRESS BAR -->
  <div id="progressBarContainer">
    <div id="progressBar"></div>
  </div>

  <!-- TOP STICKY NAVBAR -->
  <nav class="top-nav">
    <a href="../../index.html" class="nav-brand">
      <i class="fa-solid fa-shapes"></i>
      <span>Sujit Classes</span>
    </a>
    <div class="nav-links">
      <a href="#section-1"><i class="fa-solid fa-compass"></i> <span>Blueprint</span></a>
      <a href="#section-2"><i class="fa-solid fa-book-open"></i> <span>Concepts</span></a>
      <a href="#section-3"><i class="fa-solid fa-table-list"></i> <span>Formulas</span></a>
      <a href="#section-4"><i class="fa-solid fa-pen-ruler"></i> <span>NCERT Solved</span></a>
      <a href="#section-5"><i class="fa-solid fa-clipboard-question"></i> <span>Exam Bank</span></a>
      <a href="#section-6"><i class="fa-solid fa-triangle-exclamation"></i> <span>Traps</span></a>
      <span class="nav-badge">NEP Class 8</span>
    </div>
  </nav>

  <div class="container">

    <!-- HERO BANNER -->
    <header class="hero-banner">
      <div class="hero-badge-group">
        <span class="hero-pill"><i class="fa-solid fa-school"></i> Class 8 CBSE / BSE Odisha</span>
        <span class="hero-pill emerald"><i class="fa-solid fa-shapes"></i> Mathematics (Ganita Prakash)</span>
        <span class="hero-pill gold"><i class="fa-solid fa-dna"></i> NEP Code: hegp104</span>
        <span class="hero-pill"><i class="fa-solid fa-award"></i> NCERT Aligned</span>
      </div>
      <h1 class="hero-title">Chapter 4: Quadrilaterals</h1>
      <p class="hero-subtitle">
        Master the geometric science of four-sided figures! Journey through the famous Carpenter's Problem, discover the 10 landmark geometric deductions, explore the universal 360° angle sum law, and unveil the complete hierarchical family tree uniting parallelograms, rhombuses, rectangles, squares, trapeziums, and kites.
      </p>

      <div class="hero-stats">
        <div class="stat-card">
          <div class="stat-value"><i class="fa-solid fa-draw-polygon"></i> 4</div>
          <div class="stat-label">Sides & Angles</div>
        </div>
        <div class="stat-card">
          <div class="stat-value"><i class="fa-solid fa-sitemap"></i> 6</div>
          <div class="stat-label">Special Quad Families</div>
        </div>
        <div class="stat-card">
          <div class="stat-value"><i class="fa-solid fa-lightbulb"></i> 10</div>
          <div class="stat-label">Landmark Deductions</div>
        </div>
        <div class="stat-card">
          <div class="stat-value"><i class="fa-solid fa-circle-notch"></i> 360°</div>
          <div class="stat-label">Universal Angle Sum</div>
        </div>
      </div>
    </header>

    <!-- AUDIO PLAYER CARD -->
    <div class="audio-player-card">
      <div class="audio-info">
        <button class="audio-icon-btn" id="audioToggleBtn" onclick="toggleChapterAudio()" title="Play audio overview">
          <i class="fa-solid fa-volume-high" id="audioIcon"></i>
        </button>
        <div class="audio-text">
          <h4>Audio Master Summary: Quadrilaterals</h4>
          <p id="audioStatusText">Click play to listen to a 2-minute spoken overview of chapter concepts.</p>
        </div>
      </div>
      <div class="audio-controls-right">
        <label for="speechRate" style="font-size: 0.85rem; color: #94a3b8;"><i class="fa-solid fa-gauge-high"></i> Speed:</label>
        <select id="speechRate" class="speech-rate-select" onchange="updateSpeechRate()">
          <option value="0.85">0.85x</option>
          <option value="1.0" selected>1.0x</option>
          <option value="1.15">1.15x</option>
          <option value="1.25">1.25x</option>
        </select>
      </div>
    </div>

    <!-- QUICK NAVIGATION PILLS -->
    <div class="quick-nav-pills">
      <a href="#section-1" class="quick-pill"><i class="fa-solid fa-sitemap"></i> Sec 1: Visual Blueprint & Mind Map</a>
      <a href="#section-2" class="quick-pill"><i class="fa-solid fa-book-open-reader"></i> Sec 2: Concepts & Bilingual Glossary</a>
      <a href="#section-3" class="quick-pill"><i class="fa-solid fa-table"></i> Sec 3: Rapid Revision Formula Bank</a>
      <a href="#section-4" class="quick-pill"><i class="fa-solid fa-square-check"></i> Sec 4: 100% Solved NCERT Questions</a>
      <a href="#section-5" class="quick-pill"><i class="fa-solid fa-pen-to-square"></i> Sec 5: Exam Question Bank (27 CBE)</a>
      <a href="#section-6" class="quick-pill"><i class="fa-solid fa-triangle-exclamation"></i> Sec 6: Traps & 15 Revision Points</a>
    </div>
"""
