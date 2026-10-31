# -*- coding: utf-8 -*-
"""
Module: ch7_styles_head.py
Contains HTML head, metadata, typography, complete CSS stylesheet, top navbar,
reading progress bar, hero banner, audio player component, and quick navigation pills
for Class 8 Mathematics Chapter 7: Proportional Reasoning - 1.
"""

def get_head_and_hero():
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Proportional Reasoning - 1 - Class 8 Mathematics Chapter 7 Master Study Notes (Ganita Prakash) | Sujit Classes</title>
  <meta name="description" content="Exhaustive, zero-omission teacher notes for Class 8 Mathematics Chapter 7: Proportional Reasoning - 1 (NCERT Ganita Prakash NEP 2020 code: hegp107). Features aspect ratio scaling, ancient Indian Trairāśika (Rule of Three by Āryabhaṭa), cross-multiplication, group sharing m:n, unit conversions, and 100% solved exercises.">
  <!-- Google Fonts: Space Grotesk, Plus Jakarta Sans, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Space+Grotesk:wght@500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <!-- Font Awesome 6.4.0 -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <style>
    :root {
      --primary: #4f46e5;
      --primary-dark: #3730a3;
      --primary-light: #e0e7ff;
      --primary-ultra-light: #eef2ff;
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
      background: linear-gradient(90deg, #4f46e5, #059669, #7c3aed, #d97706);
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
      background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 45%, #064e3b 100%);
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
      background: radial-gradient(circle, rgba(79, 70, 229, 0.28) 0%, rgba(0, 0, 0, 0) 70%);
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
      background: radial-gradient(circle, rgba(5, 150, 105, 0.22) 0%, rgba(0, 0, 0, 0) 70%);
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
      color: #e0e7ff;
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
      color: #a5b4fc;
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
      background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%);
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
      background: linear-gradient(135deg, #4f46e5, #059669);
      border: none;
      color: white;
      font-size: 1.25rem;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(79, 70, 229, 0.4);
      transition: transform 0.2s ease, box-shadow 0.2s ease;
      flex-shrink: 0;
    }
    .audio-icon-btn:hover {
      transform: scale(1.06);
      box-shadow: 0 6px 16px rgba(79, 70, 229, 0.6);
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
      color: #312e81;
    }
    .callout-def .callout-title {
      color: var(--primary-dark);
    }
    .callout-act {
      background-color: var(--secondary-ultra-light);
      border-left-color: var(--secondary);
      color: #065f46;
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
    .step-1 { border-left: 4px solid #4f46e5; }
    .step-1 .step-badge { background: #e0e7ff; color: #3730a3; }
    .step-2 { border-left: 4px solid #059669; }
    .step-2 .step-badge { background: #d1fae5; color: #047857; }
    .step-3 { border-left: 4px solid #f59e0b; }
    .step-3 .step-badge { background: #fef3c7; color: #b45309; }
    .step-4 { border-left: 4px solid #8b5cf6; }
    .step-4 .step-badge { background: #ede9fe; color: #6d28d9; }
    .step-5 { border-left: 4px solid #ec4899; }
    .step-5 .step-badge { background: #fce7f3; color: #be185d; }

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
    table.data-table th, table.data-table td {
      padding: 0.9rem 1.15rem;
      border: 1px solid var(--border);
    }
    table.data-table th {
      background: #f1f5f9;
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      color: var(--dark);
    }
    table.data-table tr:nth-child(even) {
      background-color: #f8fafc;
    }
    table.data-table tr:hover {
      background-color: #f1f5f9;
    }

    /* INLINE SVG CONTAINERS */
    .svg-container {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.75rem;
      margin: 2rem 0;
      text-align: center;
      box-shadow: var(--shadow-sm);
    }
    .svg-container svg {
      max-width: 100%;
      height: auto;
      display: inline-block;
    }
    .svg-caption {
      margin-top: 1rem;
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--text-muted);
      font-family: 'Space Grotesk', sans-serif;
    }

    /* BLUNDER CARDS */
    .blunder-card {
      background: #ffffff;
      border-radius: var(--radius-md);
      border: 1px solid var(--border);
      overflow: hidden;
      margin: 1.5rem 0;
      box-shadow: var(--shadow-sm);
    }
    .blunder-header {
      background: #fee2e2;
      color: #991b1b;
      padding: 0.85rem 1.25rem;
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      font-size: 1.05rem;
    }
    .blunder-body {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.25rem;
      padding: 1.25rem;
    }
    @media (max-width: 768px) {
      .blunder-body {
        grid-template-columns: 1fr;
      }
    }
    .blunder-bad {
      background: #fff5f5;
      padding: 1rem;
      border-radius: var(--radius-sm);
      border: 1px dashed #fca5a5;
    }
    .blunder-good {
      background: #f0fdf4;
      padding: 1rem;
      border-radius: var(--radius-sm);
      border: 1px solid #86efac;
    }
    .blunder-label {
      font-weight: 800;
      font-size: 0.85rem;
      text-transform: uppercase;
      margin-bottom: 0.4rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }
    .blunder-bad .blunder-label { color: #dc2626; }
    .blunder-good .blunder-label { color: #16a34a; }

    /* MCQ CARDS & INTERACTIVE QUIZ */
    .mcq-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 1.5rem;
      margin: 1.5rem 0;
      box-shadow: var(--shadow-sm);
    }
    .mcq-question {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.08rem;
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
    .option-btn {
      background: #f8fafc;
      border: 1.5px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 0.8rem 1.1rem;
      font-size: 0.95rem;
      font-weight: 500;
      text-align: left;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 0.75rem;
      width: 100%;
      color: var(--text);
    }
    .option-btn:hover:not(:disabled) {
      background: var(--primary-light);
      border-color: var(--primary);
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
    .mcq-feedback {
      display: none;
      padding: 1rem 1.25rem;
      border-radius: var(--radius-sm);
      font-size: 0.925rem;
      line-height: 1.6;
      margin-top: 0.75rem;
    }
    .mcq-feedback.show {
      display: block;
    }
    .correct-feedback {
      background: #f0fdf4;
      border: 1px solid #86efac;
      color: #166534;
    }
    .wrong-feedback {
      background: #fef2f2;
      border: 1px solid #fca5a5;
      color: #991b1b;
    }

    /* FOOTER */
    footer {
      background: var(--dark);
      color: #cbd5e1;
      padding: 3.5rem 2rem;
      border-radius: var(--radius-xl);
      text-align: center;
      margin-top: 3rem;
      border: 1px solid rgba(255, 255, 255, 0.08);
    }
    .footer-brand {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.75rem;
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 800;
      font-size: 1.35rem;
      color: white;
      margin-bottom: 0.75rem;
    }
    .footer-brand i {
      color: var(--primary-light);
    }
    .footer-links {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 1.5rem;
      margin: 1.5rem 0;
    }
    .footer-links a {
      color: #94a3b8;
      text-decoration: none;
      font-weight: 600;
      font-size: 0.9rem;
      transition: color 0.2s ease;
    }
    .footer-links a:hover {
      color: white;
    }

    /* HIGHLIGHT PILLS */
    .highlight-pill {
      background: #ede9fe;
      color: #6d28d9;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.88rem;
      padding: 0.15rem 0.45rem;
      border-radius: 4px;
      font-weight: 600;
    }
  </style>
</head>
<body>

  <!-- READING PROGRESS BAR -->
  <div id="progressBarContainer">
    <div id="progressBar"></div>
  </div>

  <!-- STICKY TOP NAVBAR -->
  <nav class="top-nav">
    <a href="../../index.html" class="nav-brand">
      <i class="fa-solid fa-graduation-cap"></i>
      <span>Sujit Classes</span>
    </a>
    <div class="nav-links">
      <span class="nav-badge"><i class="fa-solid fa-book"></i> Class 8 • Math</span>
      <a href="#section1"><i class="fa-solid fa-sitemap"></i> Mind Map</a>
      <a href="#section2"><i class="fa-solid fa-lightbulb"></i> Concepts</a>
      <a href="#section3"><i class="fa-solid fa-table"></i> Formulas</a>
      <a href="#section4"><i class="fa-solid fa-pen-ruler"></i> NCERT Solved</a>
      <a href="#section5"><i class="fa-solid fa-trophy"></i> Exam Bank</a>
      <a href="#section6"><i class="fa-solid fa-triangle-exclamation"></i> Traps</a>
      <a href="../../index.html"><i class="fa-solid fa-house"></i> Home</a>
    </div>
  </nav>

  <div class="container">
    <!-- HERO BANNER -->
    <header class="hero-banner">
      <div class="hero-badge-group">
        <span class="hero-pill"><i class="fa-solid fa-award"></i> NCERT NEP 2020 Ganita Prakash</span>
        <span class="hero-pill gold"><i class="fa-solid fa-code"></i> Code: hegp107</span>
        <span class="hero-pill emerald"><i class="fa-solid fa-language"></i> English + ଓଡ଼ିଆ Vocabulary</span>
        <span class="hero-pill"><i class="fa-solid fa-brain"></i> Proportional Reasoning Series</span>
      </div>
      <h1 class="hero-title">Chapter 7: Proportional Reasoning - 1</h1>
      <p class="hero-subtitle">
        An exhaustive, zero-omission teacher master note covering visual scaling, aspect ratios, simplest forms, ancient Indian Trairāśika (Rule of Three by Āryabhaṭa), cross-multiplication, sharing in specified ratios, unit conversions, and 100% solved textbook inquiries.
      </p>

      <div class="hero-stats">
        <div class="stat-card">
          <div class="stat-value"><i class="fa-solid fa-book-open"></i> 12</div>
          <div class="stat-label">In-Text Examples Solved</div>
        </div>
        <div class="stat-card">
          <div class="stat-value"><i class="fa-solid fa-list-check"></i> 26</div>
          <div class="stat-label">Figure it Out & Inquiry Tasks</div>
        </div>
        <div class="stat-card">
          <div class="stat-value"><i class="fa-solid fa-diagram-project"></i> 6</div>
          <div class="stat-label">Intricate Inline SVG Visuals</div>
        </div>
        <div class="stat-card">
          <div class="stat-value"><i class="fa-solid fa-trophy"></i> 27</div>
          <div class="stat-label">Exhaustive Exam Bank Questions</div>
        </div>
        <div class="stat-card">
          <div class="stat-value"><i class="fa-solid fa-language"></i> 32</div>
          <div class="stat-label">Bilingual Glossary Terms</div>
        </div>
      </div>
    </header>

    <!-- AUDIO PLAYER CARD -->
    <div class="audio-player-card">
      <div class="audio-info">
        <button id="ttsPlayBtn" class="audio-icon-btn" onclick="toggleAudioReader()" title="Listen to Chapter Summary">
          <i class="fa-solid fa-play" id="ttsIcon"></i>
        </button>
        <div class="audio-text">
          <h4><i class="fa-solid fa-headphones"></i> Audio Reader • Listen to Chapter Master Narrative</h4>
          <p id="ttsStatus">Click Play to listen to teacher explanations, core rules, and memory hacks using Web Speech synthesis.</p>
        </div>
      </div>
      <div class="audio-controls-right">
        <label for="ttsRate" style="font-size: 0.85rem; color: #cbd5e1; font-weight: 600;">Speed:</label>
        <select id="ttsRate" class="speech-rate-select" onchange="updateSpeechRate()">
          <option value="0.8">0.8×</option>
          <option value="1.0" selected>1.0×</option>
          <option value="1.2">1.2×</option>
          <option value="1.4">1.4×</option>
        </select>
      </div>
    </div>

    <!-- QUICK NAVIGATION PILLS -->
    <div class="quick-nav-pills">
      <a href="#section1" class="quick-pill"><i class="fa-solid fa-sitemap"></i> Sec 1: Mind Map & Blueprint</a>
      <a href="#section2" class="quick-pill"><i class="fa-solid fa-book-open"></i> Sec 2: Conceptual Core & Glossary</a>
      <a href="#section3" class="quick-pill"><i class="fa-solid fa-table-list"></i> Sec 3: Formula & Law Bank</a>
      <a href="#section4" class="quick-pill"><i class="fa-solid fa-pen-ruler"></i> Sec 4: 100% Solved NCERT (All 4 Sets)</a>
      <a href="#section5" class="quick-pill"><i class="fa-solid fa-award"></i> Sec 5: Exam Question Bank (27 Qs)</a>
      <a href="#section6" class="quick-pill"><i class="fa-solid fa-triangle-exclamation"></i> Sec 6: Traps & 15 Key Takeaways</a>
    </div>
"""
