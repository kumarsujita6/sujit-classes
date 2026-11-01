# -*- coding: utf-8 -*-
"""
Generator script for Class 7 Mathematics Chapter 2: Arithmetic Expressions (gegp102)
Target file: english/class7/math-ch2-arithmetic-expressions.html
Benchmark: 150KB+ minimum size floor, zero-omission depth, 6 sections, 6 inline SVGs, interactive quiz, audio narrator.
"""

import os
import sys

def get_head_and_styles():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Arithmetic Expressions - Class 7 Mathematics Chapter 2 Master Study Notes (Ganita Prakash | NEP gegp102) | Sujit Classes</title>
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
      background: rgba(255, 255, 255, 0.95);
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
      background: linear-gradient(135deg, #0369a1 0%, #0284c7 40%, #0d9488 100%);
      color: white;
      padding: 3.5rem 2.5rem;
      border-radius: var(--radius-xl);
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow-xl);
      position: relative;
      overflow: hidden;
    }
    .hero::after {
      content: '';
      position: absolute;
      top: -50px;
      right: -50px;
      width: 250px;
      height: 250px;
      background: rgba(255, 255, 255, 0.08);
      border-radius: 50%;
      pointer-events: none;
    }
    .hero-badges {
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem;
      margin-bottom: 1.2rem;
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
      background: rgba(255, 255, 255, 0.2);
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.3);
    }
    .badge-gold {
      background: #fef3c7;
      color: #92400e;
    }
    .hero h1 {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 2.6rem;
      line-height: 1.2;
      font-weight: 800;
      margin-bottom: 0.8rem;
    }
    .hero p {
      font-size: 1.15rem;
      color: #e0f2fe;
      max-width: 820px;
      line-height: 1.6;
    }
    .hero-meta {
      margin-top: 1.5rem;
      display: flex;
      flex-wrap: wrap;
      gap: 1.8rem;
      font-size: 0.88rem;
      color: #bae6fd;
      border-top: 1px solid rgba(255, 255, 255, 0.2);
      padding-top: 1.2rem;
    }
    .hero-meta span {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    /* ACTION BAR */
    .action-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      background: #ffffff;
      padding: 1.2rem 1.5rem;
      border-radius: var(--radius-lg);
      border: 1px solid var(--border);
      box-shadow: var(--shadow-sm);
      margin-bottom: 2.5rem;
      align-items: center;
      justify-content: space-between;
    }
    .action-group {
      display: flex;
      flex-wrap: wrap;
      gap: 0.8rem;
      align-items: center;
    }
    .btn-action {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.55rem 1.1rem;
      border-radius: var(--radius-md);
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.2s;
      border: 1px solid transparent;
    }
    .btn-primary-action {
      background: var(--primary);
      color: #ffffff;
    }
    .btn-primary-action:hover {
      background: var(--primary-dark);
    }
    .btn-secondary-action {
      background: var(--secondary-light);
      color: var(--secondary-dark);
      border-color: #99f6e4;
    }
    .btn-secondary-action:hover {
      background: var(--secondary);
      color: #ffffff;
    }

    /* SECTION STYLES */
    .study-section {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-xl);
      padding: 2.5rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow-sm);
    }
    .section-header {
      border-bottom: 2px solid var(--border);
      padding-bottom: 1.2rem;
      margin-bottom: 2rem;
      display: flex;
      align-items: center;
      gap: 1rem;
    }
    .section-icon {
      width: 52px;
      height: 52px;
      border-radius: var(--radius-md);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
      flex-shrink: 0;
    }
    .icon-blue { background: var(--primary-light); color: var(--primary); }
    .icon-teal { background: var(--secondary-light); color: var(--secondary-dark); }
    .icon-purple { background: var(--purple-light); color: var(--purple); }
    .icon-amber { background: var(--accent-light); color: var(--accent-dark); }
    .icon-red { background: var(--danger-light); color: var(--danger-dark); }

    .section-header h2 {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.85rem;
      color: var(--dark);
      font-weight: 700;
      line-height: 1.25;
    }
    .section-header p {
      color: var(--text-muted);
      font-size: 0.95rem;
      margin-top: 0.2rem;
    }

    h3 {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.4rem;
      color: var(--dark);
      margin: 2rem 0 1rem 0;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }
    h4 {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.15rem;
      color: #1e293b;
      margin: 1.5rem 0 0.8rem 0;
      font-weight: 700;
    }
    p {
      margin-bottom: 1.2rem;
    }
    ul, ol {
      margin-left: 1.6rem;
      margin-bottom: 1.5rem;
    }
    li {
      margin-bottom: 0.5rem;
    }

    /* CALLOUT BOXES */
    .callout {
      border-radius: var(--radius-lg);
      padding: 1.4rem 1.6rem;
      margin: 1.8rem 0;
      border-left: 5px solid;
    }
    .callout-title {
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      font-size: 1.05rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      margin-bottom: 0.6rem;
    }
    .callout-def {
      background: var(--primary-ultra-light);
      border-left-color: var(--primary);
      color: #0c4a6e;
    }
    .callout-def .callout-title { color: var(--primary-dark); }
    .callout-act {
      background: var(--secondary-ultra-light);
      border-left-color: var(--secondary);
      color: #134e4a;
    }
    .callout-act .callout-title { color: var(--secondary-dark); }
    .callout-hack {
      background: #fdf4ff;
      border-left-color: var(--purple);
      color: #581c87;
    }
    .callout-hack .callout-title { color: var(--purple-dark); }
    .callout-pyq {
      background: #fffbeb;
      border-left-color: var(--accent);
      color: #78350f;
    }
    .callout-pyq .callout-title { color: var(--accent-dark); }
    .callout-warn {
      background: #fef2f2;
      border-left-color: var(--danger);
      color: #7f1d1d;
    }
    .callout-warn .callout-title { color: var(--danger-dark); }

    /* MATH EXPRESSIONS & CODE */
    .math-display {
      background: #f1f5f9;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 0.9rem 1.4rem;
      margin: 1.2rem 0;
      font-family: 'JetBrains Mono', monospace;
      font-weight: 600;
      font-size: 1.15rem;
      color: #0f172a;
      text-align: center;
      overflow-x: auto;
    }
    .math-inline {
      font-family: 'JetBrains Mono', monospace;
      font-weight: 600;
      color: #0369a1;
      background: #e0f2fe;
      padding: 0.15rem 0.45rem;
      border-radius: 4px;
      font-size: 0.95em;
    }

    /* TABLES */
    .table-container {
      width: 100%;
      overflow-x: auto;
      margin: 1.8rem 0;
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
    th {
      background: #f8fafc;
      color: var(--dark);
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      padding: 0.9rem 1.1rem;
      border-bottom: 2px solid var(--border);
    }
    td {
      padding: 0.85rem 1.1rem;
      border-bottom: 1px solid var(--border);
      color: var(--text);
    }
    tr:nth-child(even) td {
      background: #fcfdfe;
    }
    tr:hover td {
      background: #f0f9ff;
    }
    .odia-text {
      font-family: 'Noto Sans Oriya', 'Plus Jakarta Sans', sans-serif;
      font-weight: 600;
      color: #047857;
    }

    /* COLLAPSIBLE ANS-BOX (5-STEP NCERT SOLUTIONS) */
    .ans-box {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      margin: 1.5rem 0;
      box-shadow: var(--shadow-sm);
      overflow: hidden;
      transition: all 0.2s ease;
    }
    .ans-box[open] {
      border-color: #bae6fd;
      box-shadow: var(--shadow-md);
    }
    .ans-box summary {
      padding: 1.2rem 1.5rem;
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      font-size: 1.05rem;
      color: var(--dark);
      background: #f8fafc;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      user-select: none;
      transition: background 0.2s;
    }
    .ans-box summary:hover {
      background: #f0f9ff;
    }
    .ans-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .ans-content {
      padding: 1.5rem;
      background: #ffffff;
      border-top: 1px solid var(--border);
    }

    /* 5-STEP FORMAT */
    .step-box {
      position: relative;
      background: #f8fafc;
      border-left: 4px solid var(--primary);
      padding: 1.1rem 1.4rem;
      margin-bottom: 1.1rem;
      border-radius: 0 var(--radius-md) var(--radius-md) 0;
    }
    .step-box:nth-child(2) { border-left-color: #0d9488; }
    .step-box:nth-child(3) { border-left-color: #7c3aed; background: #faf5ff; }
    .step-box:nth-child(4) { border-left-color: #d97706; background: #fffbeb; }
    .step-box:nth-child(5) { border-left-color: #16a34a; background: #f0fdf4; }
    .step-label {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 0.85rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #475569;
      display: block;
      margin-bottom: 0.4rem;
    }
    .step-box:nth-child(1) .step-label { color: #0369a1; }
    .step-box:nth-child(2) .step-label { color: #0f766e; }
    .step-box:nth-child(3) .step-label { color: #6d28d9; }
    .step-box:nth-child(4) .step-label { color: #b45309; }
    .step-box:nth-child(5) .step-label { color: #15803d; }

    /* SVG DIAGRAM CARDS */
    .svg-diagram-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      margin: 2rem 0;
      box-shadow: var(--shadow-sm);
      text-align: center;
    }
    .svg-diagram-card svg {
      width: 100%;
      height: auto;
      max-width: 950px;
      display: block;
      margin: 0 auto;
    }
    .diagram-caption {
      margin-top: 1rem;
      font-size: 0.9rem;
      color: var(--text-muted);
      font-weight: 600;
    }

    /* INTERACTIVE QUIZ ENGINE */
    .quiz-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.6rem;
      margin: 1.8rem 0;
      box-shadow: var(--shadow-sm);
    }
    .quiz-question {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--dark);
      margin-bottom: 1.2rem;
    }
    .quiz-options {
      display: flex;
      flex-direction: column;
      gap: 0.7rem;
      margin-bottom: 1rem;
    }
    .option-btn {
      text-align: left;
      padding: 0.9rem 1.25rem;
      border-radius: var(--radius-md);
      border: 1px solid var(--border);
      background: var(--light);
      color: var(--text);
      font-size: 0.98rem;
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
      padding: 1rem 1.25rem;
      border-radius: var(--radius-md);
      margin-top: 1rem;
      font-size: 0.95rem;
      line-height: 1.6;
    }
    .quiz-feedback.show {
      display: block;
    }
    .quiz-feedback.success {
      background: #f0fdf4;
      border: 1px solid #86efac;
      color: #166534;
    }
    .quiz-feedback.error {
      background: #fef2f2;
      border: 1px solid #fca5a5;
      color: #991b1b;
    }
    .quiz-score-banner {
      background: linear-gradient(135deg, #0284c7, #0d9488);
      color: white;
      padding: 1.2rem 1.8rem;
      border-radius: var(--radius-lg);
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 2rem;
      box-shadow: var(--shadow-md);
    }
    .quiz-score-banner h4 {
      margin: 0;
      color: white;
      font-size: 1.2rem;
    }

    /* MARKING SCHEME PILLS */
    .mark-scheme {
      background: #f8fafc;
      border: 1px dashed #cbd5e1;
      padding: 0.8rem 1.2rem;
      border-radius: var(--radius-md);
      margin: 0.8rem 0;
      font-size: 0.9rem;
    }
    .mark-item {
      display: flex;
      justify-content: space-between;
      padding: 0.3rem 0;
      border-bottom: 1px dotted #e2e8f0;
    }
    .mark-item:last-child {
      border-bottom: none;
    }
    .mark-val {
      font-weight: 700;
      color: var(--primary);
    }

    /* TRAP ALERT BOX */
    .trap-card {
      background: #fff;
      border: 1px solid #fecaca;
      border-left: 6px solid var(--danger);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      margin: 1.5rem 0;
      box-shadow: var(--shadow-sm);
    }
    .trap-title {
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      color: var(--danger-dark);
      font-size: 1.15rem;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      margin-bottom: 0.8rem;
    }
    .trap-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin: 1rem 0;
    }
    @media (max-width: 768px) {
      .trap-grid { grid-template-columns: 1fr; }
    }
    .trap-wrong {
      background: #fef2f2;
      border: 1px solid #fca5a5;
      padding: 0.9rem 1.1rem;
      border-radius: var(--radius-md);
      font-size: 0.92rem;
    }
    .trap-wrong strong { color: #b91c1c; }
    .trap-right {
      background: #f0fdf4;
      border: 1px solid #86efac;
      padding: 0.9rem 1.1rem;
      border-radius: var(--radius-md);
      font-size: 0.92rem;
    }
    .trap-right strong { color: #15803d; }

    /* BACK TO TOP */
    #backToTopBtn {
      position: fixed;
      bottom: 2rem;
      right: 2rem;
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
      transition: all 0.2s;
      z-index: 999;
    }
    #backToTopBtn:hover {
      background: var(--primary-dark);
      transform: translateY(-3px);
    }

    /* FOOTER */
    footer {
      background: var(--dark);
      color: #94a3b8;
      padding: 3rem 1.5rem;
      margin-top: 5rem;
      text-align: center;
      border-top: 1px solid #334155;
    }
    footer a {
      color: #38bdf8;
      text-decoration: none;
    }
    footer a:hover {
      text-decoration: underline;
    }
    .footer-links {
      display: flex;
      justify-content: center;
      gap: 1.5rem;
      margin: 1.5rem 0;
      flex-wrap: wrap;
    }

    /* RESPONSIVE */
    @media (max-width: 850px) {
      .top-nav { padding: 0.75rem 1rem; }
      .nav-links { display: none; }
      .hero { padding: 2.2rem 1.5rem; }
      .hero h1 { font-size: 1.9rem; }
      .study-section { padding: 1.5rem; }
      .section-header h2 { font-size: 1.45rem; }
    }
  </style>
</head>
'''
