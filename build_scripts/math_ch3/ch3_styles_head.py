# -*- coding: utf-8 -*-
"""
Module: ch3_styles_head.py
Contains HTML head, metadata, typography, complete CSS stylesheet, top navbar,
reading progress bar, hero banner, and quick navigation pills.
"""

def get_head_and_hero():
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>A Story of Numbers - Class 8 Mathematics Chapter 3 Master Study Notes (Ganita Prakash) | Sujit Classes</title>
  <meta name="description" content="Exhaustive, zero-omission teacher notes for Class 8 Mathematics Chapter 3: A Story of Numbers (NCERT Ganita Prakash NEP 2020 code: hegp103). Features counting mechanisms, Egyptian hieroglyphs, Babylonian sexagesimal, Mayan vigesimal, Roman abacus, Chinese rod numerals, and Indian invention of Zero.">
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
      background: linear-gradient(135deg, #0f172a 0%, #1e293b 60%, #0369a1 100%);
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
      background: radial-gradient(circle, rgba(14, 165, 233, 0.2) 0%, rgba(0, 0, 0, 0) 70%);
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
      background: radial-gradient(circle, rgba(13, 148, 136, 0.15) 0%, rgba(0, 0, 0, 0) 70%);
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
      background: rgba(13, 148, 136, 0.25);
      color: #ccfbf1;
      border-color: rgba(13, 148, 136, 0.4);
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
      font-size: 1.15rem;
      color: #cbd5e1;
      max-width: 860px;
      line-height: 1.6;
      margin-bottom: 2rem;
    }
    .hero-stats {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 1.25rem;
      border-top: 1px solid rgba(255, 255, 255, 0.15);
      padding-top: 2rem;
    }
    .stat-card {
      background: rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(6px);
      border-radius: var(--radius-md);
      padding: 1rem 1.25rem;
      border: 1px solid rgba(255, 255, 255, 0.12);
    }
    .stat-value {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.75rem;
      font-weight: 800;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .stat-label {
      font-size: 0.825rem;
      color: #94a3b8;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-top: 0.2rem;
    }

    /* QUICK NAVIGATION PILLS */
    .quick-nav-bar {
      display: flex;
      gap: 0.75rem;
      overflow-x: auto;
      padding: 0.5rem 0.25rem 1.5rem 0.25rem;
      margin-bottom: 2.5rem;
      scrollbar-width: thin;
    }
    .quick-nav-bar::-webkit-scrollbar {
      height: 6px;
    }
    .quick-nav-bar::-webkit-scrollbar-thumb {
      background: var(--border-dark);
      border-radius: 9999px;
    }
    .quick-nav-pill {
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text);
      padding: 0.65rem 1.25rem;
      border-radius: 9999px;
      font-weight: 700;
      font-size: 0.875rem;
      text-decoration: none;
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s ease;
    }
    .quick-nav-pill:hover {
      background: var(--primary-light);
      color: var(--primary-dark);
      border-color: var(--primary);
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
    }
    .quick-nav-pill i {
      color: var(--primary);
    }

    /* SECTION STYLES */
    section {
      background: var(--surface);
      border-radius: var(--radius-xl);
      padding: 3rem;
      margin-bottom: 3.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow-md);
      position: relative;
    }
    .section-header {
      margin-bottom: 2.5rem;
      padding-bottom: 1.5rem;
      border-bottom: 2px solid var(--border);
    }
    .section-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.8rem;
      font-weight: 800;
      padding: 0.35rem 0.85rem;
      border-radius: 9999px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.75rem;
    }
    .section-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 2.15rem;
      font-weight: 800;
      color: var(--dark);
      letter-spacing: -0.02em;
    }
    .section-desc {
      font-size: 1.05rem;
      color: var(--text-muted);
      margin-top: 0.4rem;
    }

    /* HEADINGS */
    h3 {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.5rem;
      font-weight: 700;
      color: var(--dark);
      margin: 2.5rem 0 1.25rem 0;
      display: flex;
      align-items: center;
      gap: 0.65rem;
    }
    h4 {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--dark);
      margin: 1.75rem 0 0.85rem 0;
    }
    p {
      margin-bottom: 1.2rem;
      color: var(--text);
    }

    /* CALLOUT BOXES */
    .callout {
      border-radius: var(--radius-md);
      padding: 1.5rem 1.75rem;
      margin: 1.75rem 0;
      border-left: 5px solid;
      position: relative;
    }
    .callout-title {
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      font-size: 1.075rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      margin-bottom: 0.65rem;
    }
    .callout-def {
      background: var(--primary-ultra-light);
      border-color: var(--primary);
      color: #0c4a6e;
    }
    .callout-def .callout-title {
      color: var(--primary-dark);
    }
    .callout-act {
      background: var(--secondary-ultra-light);
      border-color: var(--secondary);
      color: #134e4a;
    }
    .callout-act .callout-title {
      color: var(--secondary-dark);
    }
    .callout-pyq {
      background: #fdf4ff;
      border-color: #c026d3;
      color: #701a75;
    }
    .callout-pyq .callout-title {
      color: #a21caf;
    }
    .callout-hack {
      background: #fffbeb;
      border-color: var(--accent);
      color: #78350f;
    }
    .callout-hack .callout-title {
      color: var(--accent-dark);
    }
    .callout-warn {
      background: var(--danger-light);
      border-color: var(--danger);
      color: #7f1d1d;
    }
    .callout-warn .callout-title {
      color: var(--danger-dark);
    }

    /* COLLAPSIBLE ACCORDIONS (<details class="ans-box">) */
    details.ans-box {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      margin: 1.25rem 0;
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s ease;
    }
    details.ans-box:hover {
      border-color: var(--border-dark);
    }
    details.ans-box[open] {
      border-color: var(--primary);
      box-shadow: var(--shadow-md);
    }
    details.ans-box summary {
      padding: 1.2rem 1.5rem;
      font-weight: 700;
      font-size: 1.05rem;
      color: var(--dark);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      user-select: none;
      background: var(--light);
      transition: background 0.2s ease;
    }
    details.ans-box summary:hover {
      background: var(--primary-ultra-light);
      color: var(--primary-dark);
    }
    details.ans-box summary::-webkit-details-marker {
      display: none;
    }
    details.ans-box summary::after {
      content: '\\f078';
      font-family: 'Font Awesome 6 Free';
      font-weight: 900;
      font-size: 0.9rem;
      color: var(--text-muted);
      transition: transform 0.25s ease;
    }
    details.ans-box[open] summary::after {
      transform: rotate(180deg);
      color: var(--primary);
    }
    .ans-content {
      padding: 1.75rem 1.75rem 2rem 1.75rem;
      border-top: 1px solid var(--border);
      background: var(--surface);
    }

    /* 5-STEP PRESENTATION ENGINE */
    .step-container {
      display: flex;
      flex-direction: column;
      gap: 1.15rem;
      margin-top: 0.75rem;
    }
    .step-box {
      background: var(--light);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 1.1rem 1.25rem;
      position: relative;
      border-left: 4px solid var(--primary);
    }
    .step-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-size: 0.775rem;
      font-weight: 800;
      padding: 0.25rem 0.65rem;
      border-radius: 9999px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.5rem;
    }
    .step-1 .step-badge { background: #e0f2fe; color: #0369a1; }
    .step-2 .step-badge { background: #ccfbf1; color: #0f766e; }
    .step-3 .step-badge { background: #ede9fe; color: #6d28d9; }
    .step-4 .step-badge { background: #fef3c7; color: #b45309; }
    .step-5 .step-badge { background: #dcfce7; color: #15803d; }
    .step-1 { border-left-color: #0284c7; }
    .step-2 { border-left-color: #0d9488; }
    .step-3 { border-left-color: #7c3aed; }
    .step-4 { border-left-color: #f59e0b; }
    .step-5 { border-left-color: #16a34a; }

    /* TABLES */
    .table-wrapper {
      width: 100%;
      overflow-x: auto;
      margin: 1.75rem 0;
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border);
    }
    table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.95rem;
      background: var(--surface);
    }
    th {
      background: #f1f5f9;
      color: var(--dark);
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      padding: 1rem 1.25rem;
      border-bottom: 2px solid var(--border-dark);
      white-space: nowrap;
    }
    td {
      padding: 0.9rem 1.25rem;
      border-bottom: 1px solid var(--border);
      color: var(--text);
      vertical-align: top;
    }
    tr:last-child td {
      border-bottom: none;
    }
    tr:hover td {
      background: var(--primary-ultra-light);
    }

    /* CODE & MATH */
    code, .math-code {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.925rem;
      background: #f1f5f9;
      color: #0f172a;
      padding: 0.2rem 0.45rem;
      border-radius: 4px;
      border: 1px solid #e2e8f0;
    }
    .math-block {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: var(--radius-sm);
      padding: 1rem 1.5rem;
      font-family: 'JetBrains Mono', monospace;
      font-size: 1.05rem;
      margin: 1.25rem 0;
      overflow-x: auto;
      color: #0369a1;
      font-weight: 600;
    }

    /* SVG DIAGRAM CONTAINERS */
    .svg-container {
      background: white;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.75rem;
      margin: 2rem 0;
      box-shadow: var(--shadow-md);
      text-align: center;
      overflow: hidden;
      transition: all 0.3s ease;
    }
    .svg-container:hover {
      box-shadow: var(--shadow-lg);
      border-color: var(--primary-light);
    }
    .svg-container svg {
      max-width: 100%;
      height: auto;
      display: block;
      margin: 0 auto;
    }
    .svg-caption {
      font-size: 0.875rem;
      color: var(--text-muted);
      font-weight: 600;
      margin-top: 1rem;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.4rem;
    }

    /* INTERACTIVE QUIZ ENGINE */
    .quiz-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.75rem 2rem;
      margin: 1.75rem 0;
      box-shadow: var(--shadow-md);
      transition: all 0.2s ease;
    }
    .quiz-q-num {
      font-size: 0.8rem;
      font-weight: 800;
      color: var(--primary);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.4rem;
    }
    .quiz-question {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--dark);
      margin-bottom: 1.25rem;
    }
    .quiz-options {
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.75rem;
      margin-bottom: 1.25rem;
    }
    .option-btn {
      background: var(--light);
      border: 1.5px solid var(--border);
      border-radius: var(--radius-md);
      padding: 0.9rem 1.25rem;
      text-align: left;
      font-size: 1rem;
      font-weight: 600;
      color: var(--text);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.75rem;
      transition: all 0.2s ease;
    }
    .option-btn:hover:not(:disabled) {
      background: var(--primary-light);
      border-color: var(--primary);
      color: var(--primary-dark);
      transform: translateX(4px);
    }
    .option-btn.correct {
      background: #dcfce7 !important;
      border-color: #16a34a !important;
      color: #14532d !important;
      font-weight: 700;
    }
    .option-btn.wrong {
      background: #fee2e2 !important;
      border-color: #dc2626 !important;
      color: #7f1d1d !important;
    }
    .quiz-feedback {
      padding: 1rem 1.25rem;
      border-radius: var(--radius-sm);
      font-size: 0.95rem;
      line-height: 1.6;
      display: none;
      margin-top: 1rem;
    }
    .quiz-feedback.show {
      display: block;
    }
    .quiz-feedback.correct-feedback {
      background: #f0fdf4;
      border: 1px solid #86efac;
      color: #166534;
    }
    .quiz-feedback.wrong-feedback {
      background: #fef2f2;
      border: 1px solid #fca5a5;
      color: #991b1b;
    }
    .score-badge-container {
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: #f1f5f9;
      border-radius: var(--radius-md);
      padding: 1rem 1.5rem;
      margin-bottom: 2rem;
      border: 1px solid var(--border);
    }
    .score-text {
      font-weight: 700;
      color: var(--dark);
      font-size: 1.1rem;
    }
    .score-number {
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 800;
      font-size: 1.4rem;
      color: var(--primary);
    }

    /* AUDIO READER CONTROL */
    .audio-player-card {
      background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
      border: 1px solid #bae6fd;
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
      gap: 0.85rem;
    }
    .audio-icon-btn {
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: var(--primary);
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.25rem;
      cursor: pointer;
      border: none;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s ease;
    }
    .audio-icon-btn:hover {
      background: var(--primary-dark);
      transform: scale(1.05);
    }
    .audio-text h5 {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.2rem;
    }
    .audio-text p {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 0;
    }
    .audio-controls-right {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    /* FOOTER */
    footer {
      background: var(--dark);
      color: white;
      padding: 4rem 1.5rem 2.5rem 1.5rem;
      margin-top: 5rem;
      border-top: 1px solid #1e293b;
    }
    .footer-content {
      max-width: 1200px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 2.5rem;
      margin-bottom: 3rem;
    }
    .footer-brand h4 {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.4rem;
      font-weight: 800;
      color: white;
      margin-bottom: 0.85rem;
    }
    .footer-brand p {
      color: #94a3b8;
      font-size: 0.925rem;
    }
    .footer-links h5 {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1rem;
      font-weight: 700;
      color: #38bdf8;
      margin-bottom: 1rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .footer-links ul {
      list-style: none;
    }
    .footer-links li {
      margin-bottom: 0.5rem;
    }
    .footer-links a {
      color: #cbd5e1;
      text-decoration: none;
      font-size: 0.925rem;
      transition: color 0.2s ease;
    }
    .footer-links a:hover {
      color: white;
    }
    .footer-bottom {
      max-width: 1200px;
      margin: 0 auto;
      border-top: 1px solid #1e293b;
      padding-top: 2rem;
      text-align: center;
      color: #64748b;
      font-size: 0.875rem;
    }

    /* BACK TO TOP BUTTON */
    #backToTopBtn {
      position: fixed;
      bottom: 25px;
      right: 25px;
      width: 46px;
      height: 46px;
      background: var(--primary);
      color: white;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.15rem;
      cursor: pointer;
      border: none;
      box-shadow: var(--shadow-lg);
      opacity: 0;
      visibility: hidden;
      transition: all 0.3s ease;
      z-index: 999;
    }
    #backToTopBtn.visible {
      opacity: 1;
      visibility: visible;
    }
    #backToTopBtn:hover {
      background: var(--primary-dark);
      transform: translateY(-4px);
    }

    /* RESPONSIVE DESIGN */
    @media (max-width: 768px) {
      .top-nav { padding: 0 1rem; }
      .nav-links a span { display: none; }
      .hero-banner { padding: 2.25rem 1.5rem; }
      .hero-title { font-size: 2rem; }
      .hero-subtitle { font-size: 1rem; }
      section { padding: 1.75rem 1.25rem; }
      .section-title { font-size: 1.65rem; }
      .hero-stats { grid-template-columns: 1fr 1fr; }
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
      <i class="fa-solid fa-graduation-cap"></i>
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
        <span class="hero-pill emerald"><i class="fa-solid fa-square-root-variable"></i> Mathematics (Ganita Prakash)</span>
        <span class="hero-pill gold"><i class="fa-solid fa-dna"></i> NEP Code: hegp103</span>
        <span class="hero-pill"><i class="fa-solid fa-award"></i> NCERT Aligned</span>
      </div>
      <h1 class="hero-title">Chapter 3: A Story of Numbers</h1>
      <p class="hero-subtitle">
        Embark on a magnificent 45,000-year historical and mathematical odyssey! Discover how human counting evolved from Stone Age notches on baboon bones to Egyptian hieroglyphs, Babylonian sexagesimal base-60, Mayan seashell zeros, Chinese rod numerals, and the crown jewel of mathematical civilization: the Indian Decimal Place-Value System with Zero.
      </p>

      <div class="hero-stats">
        <div class="stat-card">
          <div class="stat-value"><i class="fa-solid fa-hourglass-start"></i> 45,000+</div>
          <div class="stat-label">Years of History</div>
        </div>
        <div class="stat-card">
          <div class="stat-value"><i class="fa-solid fa-landmark"></i> 6</div>
          <div class="stat-label">Great Civilizations</div>
        </div>
        <div class="stat-card">
          <div class="stat-value"><i class="fa-solid fa-calculator"></i> 5</div>
          <div class="stat-label">Evolutionary Stages</div>
        </div>
        <div class="stat-card">
          <div class="stat-value"><i class="fa-solid fa-check-double"></i> 100%</div>
          <div class="stat-label">NCERT & CBE Solved</div>
        </div>
      </div>
    </header>

    <!-- QUICK NAVIGATION PILLS -->
    <div class="quick-nav-bar">
      <a href="#section-1" class="quick-nav-pill"><i class="fa-solid fa-sitemap"></i> Sec 1: Visual Blueprint & Mind Map</a>
      <a href="#section-2" class="quick-nav-pill"><i class="fa-solid fa-book-bookmark"></i> Sec 2: Concepts & Bilingual Glossary</a>
      <a href="#section-3" class="quick-nav-pill"><i class="fa-solid fa-vault"></i> Sec 3: Rapid Revision Bank</a>
      <a href="#section-4" class="quick-nav-pill"><i class="fa-solid fa-file-signature"></i> Sec 4: 100% Solved NCERT (32 Prompts)</a>
      <a href="#section-5" class="quick-nav-pill"><i class="fa-solid fa-trophy"></i> Sec 5: Complete Exam Bank (27 CBE)</a>
      <a href="#section-6" class="quick-nav-pill"><i class="fa-solid fa-shield-halved"></i> Sec 6: Trap Alerts & Revision Takeaways</a>
    </div>
"""
