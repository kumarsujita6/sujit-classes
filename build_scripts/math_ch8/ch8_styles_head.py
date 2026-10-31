# -*- coding: utf-8 -*-
"""
Module: ch8_styles_head.py
Contains HTML head, metadata, typography, complete CSS stylesheet, top navbar,
reading progress bar, hero banner, audio player component, and quick navigation pills
for Class 8 Mathematics Chapter 8: Fractions in Disguise (Ganita Prakash / NCERT NEP code: hegp108 / hegp201).
"""

def get_head_and_hero():
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fractions in Disguise - Class 8 Mathematics Chapter 8 Master Study Notes (Ganita Prakash) | Sujit Classes</title>
  <meta name="description" content="Exhaustive, zero-omission teacher master notes for Class 8 Mathematics Chapter 8: Fractions in Disguise (NCERT Ganita Prakash NEP 2020 code: hegp108 / hegp201). Features percentages as fractions with denominator 100, FDP trio conversions, mental benchmarks, commercial mathematics (profit, loss, discount, GST), simple vs compound interest, depreciation, successive discounts, and 100% solved textbook inquiries.">
  <!-- Google Fonts: Space Grotesk, Plus Jakarta Sans, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
  <!-- Font Awesome 6.5.0 Free CDN -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

  <style>
    /* ==========================================================
       CSS VARIABLES & THEME DEFINITIONS
       ========================================================== */
    :root {
      --primary: #4338ca;         /* Deep Indigo */
      --primary-light: #6366f1;   /* Indigo 500 */
      --primary-dark: #312e81;    /* Indigo 900 */
      --secondary: #0d9488;       /* Teal 600 */
      --secondary-light: #14b8a6; /* Teal 500 */
      --accent: #f59e0b;          /* Amber 500 */
      --accent-hover: #d97706;    /* Amber 600 */
      --accent-purple: #8b5cf6;   /* Purple 500 */
      --success: #10b981;         /* Emerald 500 */
      --danger: #ef4444;          /* Red 500 */
      --info: #0284c7;            /* Sky 600 */
      
      --bg-page: #f8fafc;         /* Slate 50 */
      --bg-surface: #ffffff;      /* Pure White */
      --bg-card: #f1f5f9;         /* Slate 100 */
      --bg-tint: #e0e7ff;         /* Indigo 100 */
      
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
      line-height: 1.7;
      -webkit-font-smoothing: antialiased;
      position: relative;
    }

    h1, h2, h3, h4, h5, h6 {
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      line-height: 1.25;
      color: var(--text-main);
    }

    p {
      margin-bottom: 1rem;
      font-size: 1.025rem;
      color: #1e293b;
    }

    code, kbd, samp, pre {
      font-family: 'JetBrains Mono', monospace;
    }

    a {
      color: var(--primary);
      text-decoration: none;
      transition: color 0.2s ease;
    }

    a:hover {
      color: var(--primary-light);
    }

    /* ==========================================================
       PROGRESS BAR (TOP-FIXED 4px)
       ========================================================== */
    #progressBarContainer {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 4px;
      background: transparent;
      z-index: 1000;
    }

    #progressBar {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #4338ca, #6366f1, #0d9488, #f59e0b);
      transition: width 0.1s ease-out;
      box-shadow: 0 0 8px rgba(99, 102, 241, 0.6);
    }

    /* ==========================================================
       TOP NAVIGATION BAR
       ========================================================== */
    .top-nav {
      position: sticky;
      top: 0;
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      z-index: 900;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.75rem 2rem;
      box-shadow: var(--shadow-sm);
    }

    .nav-brand {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      font-size: 1.2rem;
      color: var(--primary-dark);
    }

    .nav-brand i {
      color: var(--primary-light);
      font-size: 1.4rem;
    }

    .nav-links {
      display: flex;
      align-items: center;
      gap: 1.25rem;
      font-size: 0.9rem;
      font-weight: 600;
    }

    .nav-links a {
      color: var(--text-muted);
      padding: 0.4rem 0.75rem;
      border-radius: var(--radius-sm);
      transition: all 0.2s ease;
    }

    .nav-links a:hover {
      background: var(--bg-card);
      color: var(--primary);
    }

    .nav-badge {
      background: #eef2ff;
      color: var(--primary);
      padding: 0.25rem 0.6rem;
      border-radius: var(--radius-full);
      font-size: 0.8rem;
      font-weight: 700;
      border: 1px solid #c7d2fe;
    }

    /* ==========================================================
       CONTAINER & SECTION LAYOUT
       ========================================================== */
    .container {
      max-width: 1120px;
      margin: 0 auto;
      padding: 2rem 1.5rem 4rem 1.5rem;
    }

    section {
      margin-bottom: 4rem;
      scroll-margin-top: 5rem;
    }

    .section-header {
      margin-bottom: 2rem;
      position: relative;
    }

    .section-tag {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: var(--bg-tint);
      color: var(--primary);
      font-size: 0.825rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 0.35rem 0.85rem;
      border-radius: var(--radius-full);
      margin-bottom: 0.75rem;
      border: 1px solid #c7d2fe;
    }

    .section-title {
      font-size: 2.1rem;
      color: var(--primary-dark);
      letter-spacing: -0.02em;
      margin-bottom: 0.5rem;
    }

    .section-desc {
      font-size: 1.05rem;
      color: var(--text-muted);
      max-width: 800px;
      line-height: 1.6;
    }

    .subheading {
      font-size: 1.45rem;
      color: #1e1b4b;
      margin: 2.25rem 0 1rem 0;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      border-bottom: 2px solid #e0e7ff;
      padding-bottom: 0.5rem;
    }

    .subheading i {
      color: var(--primary-light);
    }

    .sub-subheading {
      font-size: 1.2rem;
      color: #334155;
      margin: 1.5rem 0 0.75rem 0;
      font-weight: 700;
    }

    /* ==========================================================
       HERO BANNER
       ========================================================== */
    .hero-banner {
      background: linear-gradient(135deg, #1e1b4b 0%, #312e81 40%, #3730a3 75%, #4338ca 100%);
      color: #ffffff;
      padding: 3rem 2.5rem;
      border-radius: var(--radius-xl);
      box-shadow: var(--shadow-xl);
      margin-bottom: 2.5rem;
      position: relative;
      overflow: hidden;
    }

    .hero-banner::before {
      content: '';
      position: absolute;
      top: -60px;
      right: -60px;
      width: 260px;
      height: 260px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(245, 158, 11, 0.25) 0%, rgba(245, 158, 11, 0) 70%);
      pointer-events: none;
    }

    .hero-badge-group {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
      margin-bottom: 1.25rem;
    }

    .hero-pill {
      background: rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(8px);
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.35rem 0.85rem;
      border-radius: var(--radius-full);
      border: 1px solid rgba(255, 255, 255, 0.25);
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
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
      font-size: 2.75rem;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: -0.03em;
      margin-bottom: 0.75rem;
      text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }

    .hero-subtitle {
      font-size: 1.15rem;
      color: #e0e7ff;
      max-width: 880px;
      line-height: 1.7;
      margin-bottom: 2rem;
    }

    .hero-stats {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 1rem;
      margin-bottom: 1.75rem;
    }

    .stat-card {
      background: rgba(255, 255, 255, 0.1);
      backdrop-filter: blur(6px);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: var(--radius-md);
      padding: 1rem 1.25rem;
      text-align: center;
    }

    .stat-value {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.6rem;
      font-weight: 700;
      color: #fbbf24;
      margin-bottom: 0.25rem;
    }

    .stat-label {
      font-size: 0.8rem;
      font-weight: 600;
      color: #c7d2fe;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    /* AUDIO READER COMPONENT */
    .audio-player-card {
      background: rgba(15, 23, 42, 0.6);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: var(--radius-lg);
      padding: 1rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem;
      flex-wrap: wrap;
    }

    .audio-info {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .audio-icon-btn {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: var(--accent);
      color: #1e1b4b;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.1rem;
      cursor: pointer;
      border: none;
      box-shadow: 0 4px 10px rgba(245, 158, 11, 0.4);
      transition: all 0.2s ease;
    }

    .audio-icon-btn:hover {
      transform: scale(1.08);
      background: #fcd34d;
    }

    .audio-text h4 {
      color: #ffffff;
      font-size: 0.95rem;
      margin-bottom: 0.15rem;
    }

    .audio-text p {
      color: #cbd5e1;
      font-size: 0.8rem;
      margin: 0;
    }

    .audio-controls-right {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .tts-select {
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.3);
      color: #ffffff;
      padding: 0.35rem 0.65rem;
      border-radius: var(--radius-sm);
      font-size: 0.825rem;
      font-family: inherit;
      outline: none;
    }

    .tts-select option {
      background: #1e1b4b;
      color: #ffffff;
    }

    /* QUICK NAVIGATION PILLS */
    .quick-nav {
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem;
      margin-bottom: 3rem;
      background: var(--bg-surface);
      padding: 1rem 1.25rem;
      border-radius: var(--radius-lg);
      border: 1px solid var(--border);
      box-shadow: var(--shadow-sm);
    }

    .quick-nav-title {
      width: 100%;
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--text-light);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.25rem;
    }

    .quick-pill {
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-muted);
      background: var(--bg-card);
      padding: 0.4rem 0.85rem;
      border-radius: var(--radius-full);
      border: 1px solid var(--border);
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s ease;
    }

    .quick-pill:hover {
      background: #eef2ff;
      color: var(--primary);
      border-color: #c7d2fe;
      transform: translateY(-1px);
    }

    /* ==========================================================
       SVG VISUAL CONTAINERS & MICRO-ANIMATIONS
       ========================================================== */
    .svg-container {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      margin: 1.75rem 0;
      box-shadow: var(--shadow-md);
      overflow-x: auto;
      text-align: center;
    }

    .svg-container svg {
      max-width: 100%;
      height: auto;
      display: block;
      margin: 0 auto;
    }

    .svg-caption {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-top: 0.75rem;
      font-style: italic;
    }

    /* Interactive SVG Micro-Animations */
    .svg-glow-circle {
      animation: pulseGlow 2.5s infinite ease-in-out;
    }

    @keyframes pulseGlow {
      0%, 100% {
        transform: scale(1);
        filter: drop-shadow(0 0 3px rgba(99, 102, 241, 0.4));
      }
      50% {
        transform: scale(1.04);
        filter: drop-shadow(0 0 10px rgba(99, 102, 241, 0.8));
      }
    }

    .svg-hover-card {
      transition: all 0.3s ease;
      cursor: pointer;
    }

    .svg-hover-card:hover {
      transform: translateY(-3px);
      filter: drop-shadow(0 6px 12px rgba(0, 0, 0, 0.15));
    }

    /* ==========================================================
       PASTEL CALLOUT BOXES
       ========================================================== */
    .callout {
      border-radius: var(--radius-md);
      padding: 1.25rem 1.5rem;
      margin: 1.5rem 0;
      border-left: 5px solid;
      position: relative;
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

    .callout-def {
      background: #eff6ff;
      border-color: #3b82f6;
      color: #1e3a8a;
    }
    .callout-def .callout-title { color: #1d4ed8; }

    .callout-act {
      background: #f0fdf4;
      border-color: #10b981;
      color: #064e3b;
    }
    .callout-act .callout-title { color: #047857; }

    .callout-pyq {
      background: #faf5ff;
      border-color: #a855f7;
      color: #581c87;
    }
    .callout-pyq .callout-title { color: #7e22ce; }

    .callout-hack {
      background: #fffbeb;
      border-color: #f59e0b;
      color: #78350f;
    }
    .callout-hack .callout-title { color: #b45309; }

    .callout-warn {
      background: #fef2f2;
      border-color: #ef4444;
      color: #7f1d1d;
    }
    .callout-warn .callout-title { color: #b91c1c; }

    /* ==========================================================
       DATA TABLES & VOCABULARY TABLES
       ========================================================== */
    .table-container {
      width: 100%;
      overflow-x: auto;
      margin: 1.75rem 0;
      border-radius: var(--radius-md);
      border: 1px solid var(--border);
      box-shadow: var(--shadow-sm);
    }

    .data-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.95rem;
      background: var(--bg-surface);
    }

    .data-table th {
      background: #1e1b4b;
      color: #ffffff;
      padding: 0.9rem 1.1rem;
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 600;
      letter-spacing: 0.02em;
      border-bottom: 2px solid #312e81;
    }

    .data-table td {
      padding: 0.85rem 1.1rem;
      border-bottom: 1px solid var(--border);
      color: #334155;
    }

    .data-table tbody tr:nth-child(even) {
      background: #f8fafc;
    }

    .data-table tbody tr:hover {
      background: #eef2ff;
    }

    .pos-badge {
      display: inline-block;
      padding: 0.2rem 0.5rem;
      border-radius: var(--radius-sm);
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      background: #e0e7ff;
      color: #3730a3;
    }

    .odia-text {
      font-family: 'Segoe UI', 'Kalinga', 'Nirmala UI', sans-serif;
      font-size: 1.05rem;
      font-weight: 600;
      color: #1e1b4b;
    }

    /* ==========================================================
       COLLAPSIBLE 5-STEP QUESTION & ANSWER BOXES
       ========================================================== */
    details.ans-box {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      margin-bottom: 1.25rem;
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s ease;
    }

    details.ans-box:hover {
      border-color: #c7d2fe;
      box-shadow: var(--shadow-md);
    }

    details.ans-box[open] {
      border-color: #818cf8;
      box-shadow: var(--shadow-md);
    }

    summary {
      padding: 1.1rem 1.35rem;
      font-weight: 700;
      font-size: 1.05rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      color: var(--primary-dark);
      background: #f8fafc;
      user-select: none;
      transition: background 0.2s ease;
    }

    summary:hover {
      background: #f1f5f9;
      color: var(--primary);
    }

    details.ans-box[open] summary {
      background: #eef2ff;
      border-bottom: 1px solid #c7d2fe;
      color: var(--primary-dark);
    }

    summary::after {
      content: '\f078';
      font-family: 'Font Awesome 6 Free';
      font-weight: 900;
      font-size: 0.85rem;
      color: var(--primary-light);
      transition: transform 0.25s ease;
    }

    details.ans-box[open] summary::after {
      transform: rotate(180deg);
    }

    .ans-content {
      padding: 1.5rem;
      background: var(--bg-surface);
    }

    /* 5-STEP PEDAGOGICAL CONTAINER */
    .step-container {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .step-box {
      border-radius: var(--radius-sm);
      padding: 0.9rem 1.15rem;
      position: relative;
      border-left: 4px solid;
    }

    .step-badge {
      display: inline-block;
      font-size: 0.75rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 0.2rem 0.55rem;
      border-radius: var(--radius-sm);
      margin-bottom: 0.45rem;
    }

    .step-box p, .step-box ul {
      margin-bottom: 0.35rem;
      font-size: 0.95rem;
      color: #334155;
    }

    .step-box p:last-child {
      margin-bottom: 0;
    }

    .step-1 { background: #f8fafc; border-color: #64748b; }
    .step-1 .step-badge { background: #e2e8f0; color: #334155; }

    .step-2 { background: #eff6ff; border-color: #3b82f6; }
    .step-2 .step-badge { background: #dbeafe; color: #1d4ed8; }

    .step-3 { background: #faf5ff; border-color: #8b5cf6; }
    .step-3 .step-badge { background: #ede9fe; color: #6d28d9; }

    .step-4 { background: #fffbeb; border-color: #f59e0b; }
    .step-4 .step-badge { background: #fef3c7; color: #b45309; }

    .step-5 { background: #f0fdf4; border-color: #10b981; }
    .step-5 .step-badge { background: #d1fae5; color: #047857; }

    /* ==========================================================
       INTERACTIVE MCQ QUIZ ENGINE
       ========================================================== */
    .mcq-card {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      margin-bottom: 1.5rem;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s ease;
    }

    .mcq-question {
      font-size: 1.05rem;
      font-weight: 600;
      color: var(--text-main);
      margin-bottom: 1rem;
    }

    .mcq-options {
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.6rem;
      margin-bottom: 1rem;
    }

    .option-btn {
      background: #f8fafc;
      border: 1.5px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 0.75rem 1rem;
      font-size: 0.95rem;
      font-family: inherit;
      text-align: left;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.75rem;
      transition: all 0.2s ease;
      color: #334155;
    }

    .option-btn:hover:not([disabled]) {
      background: #eef2ff;
      border-color: #818cf8;
      color: var(--primary);
    }

    .option-btn.selected-correct {
      background: #d1fae5 !important;
      border-color: #10b981 !important;
      color: #064e3b !important;
      font-weight: 700;
    }

    .option-btn.selected-wrong {
      background: #fee2e2 !important;
      border-color: #ef4444 !important;
      color: #7f1d1d !important;
      font-weight: 700;
    }

    .trap-feedback {
      display: none;
      padding: 0.9rem 1.15rem;
      border-radius: var(--radius-sm);
      font-size: 0.9rem;
      line-height: 1.5;
      margin-top: 0.75rem;
    }

    .trap-feedback.show {
      display: block;
    }

    .trap-feedback.correct-feedback {
      background: #f0fdf4;
      border-left: 4px solid #10b981;
      color: #064e3b;
    }

    .trap-feedback.wrong-feedback {
      background: #fef2f2;
      border-left: 4px solid #ef4444;
      color: #991b1b;
    }

    /* ==========================================================
       BLUNDER ALERT CARDS (SECTION 6)
       ========================================================== */
    .blunder-card {
      background: var(--bg-surface);
      border: 1px solid #fecaca;
      border-radius: var(--radius-md);
      padding: 1.25rem 1.5rem;
      margin-bottom: 1.25rem;
      box-shadow: var(--shadow-sm);
    }

    .blunder-header {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      color: #dc2626;
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      font-size: 1.1rem;
      margin-bottom: 0.75rem;
    }

    .blunder-body {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin-top: 0.75rem;
    }

    @media (max-width: 768px) {
      .blunder-body {
        grid-template-columns: 1fr;
      }
    }

    .blunder-bad {
      background: #fef2f2;
      border-radius: var(--radius-sm);
      padding: 0.85rem 1rem;
      border: 1px dashed #ef4444;
      font-size: 0.9rem;
      color: #991b1b;
    }

    .blunder-good {
      background: #f0fdf4;
      border-radius: var(--radius-sm);
      padding: 0.85rem 1rem;
      border: 1px dashed #10b981;
      font-size: 0.9rem;
      color: #064e3b;
    }

    .blunder-label {
      font-weight: 800;
      text-transform: uppercase;
      font-size: 0.75rem;
      display: block;
      margin-bottom: 0.25rem;
    }

    /* ==========================================================
       REVISION POINTS & SUMMARY
       ========================================================== */
    .points-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 1rem;
      margin: 1.5rem 0;
    }

    .point-card {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 1rem 1.25rem;
      display: flex;
      gap: 0.85rem;
      align-items: flex-start;
      box-shadow: var(--shadow-sm);
    }

    .point-num {
      background: #e0e7ff;
      color: var(--primary);
      width: 28px;
      height: 28px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: 'Space Grotesk', sans-serif;
      font-weight: 700;
      font-size: 0.85rem;
      flex-shrink: 0;
      margin-top: 0.15rem;
    }

    .point-card p {
      margin: 0;
      font-size: 0.925rem;
      color: #334155;
    }

    /* ==========================================================
       FOOTER
       ========================================================== */
    footer {
      background: #0f172a;
      color: #94a3b8;
      padding: 3rem 1.5rem 2rem 1.5rem;
      margin-top: 5rem;
      border-top: 1px solid #1e293b;
    }

    .footer-container {
      max-width: 1120px;
      margin: 0 auto;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      gap: 2rem;
      align-items: center;
    }

    .footer-brand {
      color: #ffffff;
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.25rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }

    .footer-links {
      display: flex;
      gap: 1.5rem;
      font-size: 0.9rem;
    }

    .footer-links a {
      color: #cbd5e1;
    }

    .footer-links a:hover {
      color: #ffffff;
    }

    .footer-copy {
      width: 100%;
      text-align: center;
      margin-top: 2rem;
      padding-top: 1.5rem;
      border-top: 1px solid #1e293b;
      font-size: 0.85rem;
    }

    /* PRINT STYLES */
    @media print {
      .top-nav, #progressBarContainer, .audio-player-card, .quick-nav, footer {
        display: none !important;
      }
      details.ans-box {
        break-inside: avoid;
      }
      details.ans-box[open] summary::after {
        display: none;
      }
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
        <span class="hero-pill gold"><i class="fa-solid fa-code"></i> Code: hegp108 / hegp201</span>
        <span class="hero-pill emerald"><i class="fa-solid fa-language"></i> English + ଓଡ଼ିଆ Vocabulary</span>
        <span class="hero-pill"><i class="fa-solid fa-chart-pie"></i> Commercial &amp; Financial Arithmetic</span>
      </div>
      <h1 class="hero-title">Chapter 8: Fractions in Disguise</h1>
      <p class="hero-subtitle">
        An exhaustive, zero-omission teacher master note unveiling percentages as fractions with denominator 100, the FDP conversion trinity, free-hand mental benchmarks, commutative multiplication, commercial trading (profit, loss, trade discount, GST), exponential capital growth in simple versus compound interest, depreciation decay, and 100% solved textbook inquiries.
      </p>

      <div class="hero-stats">
        <div class="stat-card">
          <div class="stat-value"><i class="fa-solid fa-book-open"></i> 13</div>
          <div class="stat-label">In-Text Examples Solved</div>
        </div>
        <div class="stat-card">
          <div class="stat-value"><i class="fa-solid fa-list-check"></i> 55+</div>
          <div class="stat-label">Inquiry &amp; Figure it Out Tasks</div>
        </div>
        <div class="stat-card">
          <div class="stat-value"><i class="fa-solid fa-diagram-project"></i> 6</div>
          <div class="stat-label">Intricate SVG Diagrams</div>
        </div>
        <div class="stat-card">
          <div class="stat-value"><i class="fa-solid fa-trophy"></i> 27</div>
          <div class="stat-label">Exam Bank Questions</div>
        </div>
      </div>

      <!-- AUDIO READER COMPONENT -->
      <div class="audio-player-card">
        <div class="audio-info">
          <button class="audio-icon-btn" id="ttsPlayBtn" onclick="toggleAudioReader()" title="Play Audio Summary">
            <i class="fa-solid fa-play" id="ttsIcon"></i>
          </button>
          <div class="audio-text">
            <h4><i class="fa-solid fa-headphones"></i> Listen to Audio Teacher Summary</h4>
            <p id="ttsStatus">Click play to listen to spoken narration of key concepts &amp; formulas.</p>
          </div>
        </div>
        <div class="audio-controls-right">
          <label for="ttsRate" style="color: #cbd5e1; font-size: 0.8rem; font-weight: 600;">Speed:</label>
          <select id="ttsRate" class="tts-select" onchange="updateSpeechRate()">
            <option value="0.8">0.8×</option>
            <option value="1.0" selected>1.0×</option>
            <option value="1.2">1.2×</option>
            <option value="1.5">1.5×</option>
          </select>
        </div>
      </div>
    </header>

    <!-- QUICK NAVIGATION PILLS -->
    <nav class="quick-nav">
      <div class="quick-nav-title"><i class="fa-solid fa-compass"></i> Quick Chapter Jump Navigation:</div>
      <a href="#section1" class="quick-pill"><i class="fa-solid fa-sitemap"></i> Sec 1: Mind Map &amp; SVGs</a>
      <a href="#section2" class="quick-pill"><i class="fa-solid fa-lightbulb"></i> Sec 2: Concepts &amp; Glossary</a>
      <a href="#section3" class="quick-pill"><i class="fa-solid fa-table"></i> Sec 3: Rapid Revision Bank</a>
      <a href="#section4" class="quick-pill"><i class="fa-solid fa-pen-ruler"></i> Sec 4: 100% Solved NCERT</a>
      <a href="#section5" class="quick-pill"><i class="fa-solid fa-trophy"></i> Sec 5: Exam Question Bank</a>
      <a href="#section6" class="quick-pill"><i class="fa-solid fa-triangle-exclamation"></i> Sec 6: Trap Alerts &amp; Points</a>
    </nav>
"""
