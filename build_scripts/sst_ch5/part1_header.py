# -*- coding: utf-8 -*-
"""
Part 1: HTML Head, Typography, Custom Responsive CSS, Fixed Top Navigation,
Hero Section, and Interactive Audio Reader Bar for Class 8 SST Chapter 5.
"""

PART1_CONTENT = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Universal Franchise and India's Electoral System - Class 8 Social Science NEP Master Study Note | Sujit Classes</title>
  <!-- Google Fonts: Space Grotesk, Plus Jakarta Sans, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Space+Grotesk:wght@500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <!-- Font Awesome 6 -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
  :root {
    --primary: #1e3a8a;           /* Deep Parliamentary Navy */
    --primary-dark: #0f172a;      /* Midnight Blue */
    --primary-light: #dbeafe;     /* Soft Sky Blue */
    --primary-ultra-light: #eff6ff;
    --secondary: #047857;         /* Ashoka Green / Democratic Emerald */
    --secondary-dark: #064e3b;
    --secondary-light: #d1fae5;
    --accent: #b45309;            /* Sovereign Amber / Republic Saffron */
    --accent-dark: #78350f;
    --accent-light: #fef3c7;
    --chakra-blue: #0284c7;       /* Wheel of Dharma Azure */
    --chakra-light: #e0f2fe;
    --rose: #be123c;              /* Vigilance Crimson */
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
    background: linear-gradient(90deg, #b45309 0%, #1e3a8a 50%, #047857 100%);
    z-index: 9999;
    transition: width 0.1s ease;
  }

  /* Fixed Top Navigation */
  .top-nav {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 60px;
    background: rgba(255, 255, 255, 0.96);
    backdrop-filter: blur(10px);
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
    color: var(--primary);
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 1.15rem;
  }

  .nav-brand .brand-badge {
    background: var(--primary-light);
    color: var(--primary);
    font-size: 0.75rem;
    padding: 0.2rem 0.55rem;
    border-radius: 999px;
    font-weight: 700;
    letter-spacing: 0.5px;
  }

  .nav-links {
    display: flex;
    align-items: center;
    gap: 1.25rem;
    list-style: none;
  }

  .nav-links a {
    text-decoration: none;
    color: var(--text-muted);
    font-size: 0.88rem;
    font-weight: 600;
    transition: color 0.2s ease;
  }

  .nav-links a:hover {
    color: var(--primary);
  }

  .nav-actions {
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }

  .btn-audio-listen {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    background: linear-gradient(135deg, var(--primary), var(--primary-dark));
    color: white;
    padding: 0.45rem 0.9rem;
    border-radius: 999px;
    font-size: 0.82rem;
    font-weight: 600;
    cursor: pointer;
    border: none;
    box-shadow: 0 2px 4px rgba(30, 58, 138, 0.25);
    transition: all 0.2s ease;
  }

  .btn-audio-listen:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 8px rgba(30, 58, 138, 0.35);
  }

  .btn-audio-listen.playing {
    background: linear-gradient(135deg, #16a34a, #15803d);
  }

  .btn-portal-back {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: var(--light);
    color: var(--text);
    border: 1px solid var(--border);
    padding: 0.45rem 0.85rem;
    border-radius: 999px;
    font-size: 0.82rem;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.2s ease;
  }

  .btn-portal-back:hover {
    background: var(--surface);
    border-color: var(--text-muted);
  }

  /* Main Container */
  .container {
    max-width: 1120px;
    margin: 0 auto;
    padding: 2rem 1.5rem 5rem;
  }

  /* Hero Section */
  .hero-section {
    background: linear-gradient(135deg, #ffffff 0%, #f0fdf4 50%, #eff6ff 100%);
    border: 1px solid #bfdbfe;
    border-radius: var(--radius-xl);
    padding: 3rem 2.5rem;
    margin-bottom: 2.5rem;
    box-shadow: var(--shadow-md);
    position: relative;
    overflow: hidden;
  }

  .hero-section::before {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    width: 340px;
    height: 340px;
    background: radial-gradient(circle, rgba(30, 58, 138, 0.07) 0%, transparent 70%);
    border-radius: 50%;
    pointer-events: none;
  }

  .hero-badge-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    margin-bottom: 1.25rem;
  }

  .hero-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    font-size: 0.78rem;
    font-weight: 700;
    padding: 0.3rem 0.75rem;
    border-radius: 999px;
    letter-spacing: 0.3px;
    text-transform: uppercase;
  }

  .hero-pill-blue {
    background: #eff6ff;
    color: #1e3a8a;
    border: 1px solid #bfdbfe;
  }

  .hero-pill-saffron {
    background: #fffbeb;
    color: #b45309;
    border: 1px solid #fde68a;
  }

  .hero-pill-green {
    background: #f0fdf4;
    color: #047857;
    border: 1px solid #bbf7d0;
  }

  .hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.6rem;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.2;
    margin-bottom: 0.75rem;
    letter-spacing: -0.5px;
  }

  .hero-subtitle {
    font-size: 1.15rem;
    color: #475569;
    font-weight: 500;
    max-width: 880px;
    margin-bottom: 1.5rem;
  }

  .hero-quote-card {
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(8px);
    border-left: 5px solid var(--accent);
    border-radius: 0 var(--radius-md) var(--radius-md) 0;
    padding: 1.35rem 1.6rem;
    margin-bottom: 1.75rem;
    box-shadow: var(--shadow-sm);
  }

  .hero-quote-text {
    font-style: italic;
    font-size: 1rem;
    color: #1e293b;
    line-height: 1.68;
  }

  .hero-quote-author {
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--accent-dark);
    margin-top: 0.6rem;
    text-align: right;
  }

  /* Big Questions Tri-Card Grid */
  .big-questions-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 1.25rem;
    margin: 1.5rem 0;
  }

  .bq-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 1.25rem 1.5rem;
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    box-shadow: var(--shadow-sm);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }

  .bq-card:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
    border-color: var(--primary-light);
  }

  .bq-icon {
    width: 44px;
    height: 44px;
    border-radius: 12px;
    background: var(--primary-light);
    color: var(--primary);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    flex-shrink: 0;
  }

  .bq-text h5 {
    font-size: 0.76rem;
    text-transform: uppercase;
    color: var(--text-muted);
    letter-spacing: 0.6px;
    margin-bottom: 0.2rem;
  }

  .bq-text p {
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--dark);
    margin: 0;
    line-height: 1.4;
  }

  /* Hero Metadata Grid */
  .hero-meta-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
    gap: 1rem;
    margin-top: 1.5rem;
    padding-top: 1.5rem;
    border-top: 1px solid rgba(226, 232, 240, 0.8);
  }

  .hero-meta-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }

  .hero-meta-icon {
    width: 40px;
    height: 40px;
    border-radius: var(--radius-sm);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.1rem;
  }

  .hero-meta-text h5 {
    font-size: 0.74rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 0.15rem;
  }

  .hero-meta-text p {
    font-size: 0.92rem;
    font-weight: 700;
    color: var(--dark);
    margin: 0;
  }

  /* Audio Bar Widget */
  .audio-bar-card {
    background: linear-gradient(135deg, #0f172a, #1e3a8a);
    color: white;
    border-radius: var(--radius-lg);
    padding: 1.35rem 1.85rem;
    margin-bottom: 2.5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1.25rem;
    box-shadow: var(--shadow-md);
  }

  .audio-bar-info {
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  .audio-bar-icon {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.15);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.3rem;
    color: #fbbf24;
  }

  .audio-bar-text h4 {
    font-size: 1.05rem;
    font-weight: 700;
    margin-bottom: 0.2rem;
    font-family: 'Space Grotesk', sans-serif;
  }

  .audio-bar-text p {
    font-size: 0.85rem;
    color: #cbd5e1;
    margin: 0;
  }

  .audio-bar-controls {
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }

  .audio-btn {
    background: white;
    color: #0f172a;
    border: none;
    border-radius: 999px;
    padding: 0.55rem 1.25rem;
    font-size: 0.85rem;
    font-weight: 700;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    transition: all 0.2s ease;
  }

  .audio-btn:hover {
    background: #f8fafc;
    transform: translateY(-1px);
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.25);
  }

  .audio-btn-secondary {
    background: rgba(255, 255, 255, 0.15);
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.25);
  }

  .audio-btn-secondary:hover {
    background: rgba(255, 255, 255, 0.25);
    color: white;
  }

  /* Section Block */
  .section-block {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-xl);
    padding: 2.75rem 2.25rem;
    margin-bottom: 3rem;
    box-shadow: var(--shadow-sm);
  }

  .section-header {
    border-bottom: 2px solid var(--border);
    padding-bottom: 1.25rem;
    margin-bottom: 2rem;
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1rem;
  }

  .section-title-wrap {
    flex: 1;
  }

  .section-tag {
    display: inline-block;
    font-size: 0.75rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--primary);
    background: var(--primary-light);
    padding: 0.25rem 0.65rem;
    border-radius: 999px;
    margin-bottom: 0.5rem;
  }

  .section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.85rem;
    font-weight: 800;
    color: var(--dark);
    line-height: 1.25;
  }

  .section-desc {
    font-size: 0.95rem;
    color: var(--text-muted);
    margin-top: 0.35rem;
  }

  /* Subheadings */
  h3.subsection-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.35rem;
    font-weight: 700;
    color: var(--dark);
    margin: 2.25rem 0 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid var(--border);
    display: flex;
    align-items: center;
    gap: 0.6rem;
  }

  h4.topic-title {
    font-size: 1.12rem;
    font-weight: 700;
    color: #1e293b;
    margin: 1.5rem 0 0.6rem;
  }

  p {
    margin-bottom: 1rem;
  }

  ul, ol {
    margin-bottom: 1.25rem;
    padding-left: 1.5rem;
  }

  li {
    margin-bottom: 0.45rem;
  }

  /* Callout Boxes */
  .callout-box {
    border-radius: var(--radius-md);
    padding: 1.25rem 1.5rem;
    margin: 1.5rem 0;
    position: relative;
    border-left: 4px solid;
  }

  .callout-title {
    font-weight: 700;
    font-size: 0.95rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.5rem;
  }

  .callout-def {
    background: #eff6ff;
    border-color: #3b82f6;
    color: #1e3a8a;
  }
  .callout-def .callout-title { color: #1d4ed8; }

  .callout-act {
    background: #f0fdf4;
    border-color: #22c55e;
    color: #14532d;
  }
  .callout-act .callout-title { color: #15803d; }

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
    background: #fff1f2;
    border-color: #f43f5e;
    color: #881337;
  }
  .callout-warn .callout-title { color: #be123c; }

  /* Responsive Styled Tables */
  .table-responsive {
    overflow-x: auto;
    margin: 1.75rem 0;
    border-radius: var(--radius-md);
    box-shadow: var(--shadow-sm);
    border: 1px solid var(--border);
  }

  table.study-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.92rem;
    background: var(--surface);
    text-align: left;
  }

  table.study-table th {
    background: #f8fafc;
    color: #1e293b;
    font-weight: 700;
    padding: 0.95rem 1.15rem;
    border-bottom: 2px solid var(--border);
    font-family: 'Space Grotesk', sans-serif;
  }

  table.study-table td {
    padding: 0.85rem 1.15rem;
    border-bottom: 1px solid var(--border);
    color: #334155;
    vertical-align: top;
  }

  table.study-table tr:nth-child(even) td {
    background: #fcfdfe;
  }

  table.study-table tr:hover td {
    background: #f1f5f9;
  }

  .badge-odia {
    display: inline-block;
    background: #fef3c7;
    color: #92400e;
    font-weight: 700;
    padding: 0.15rem 0.45rem;
    border-radius: 4px;
    font-size: 0.88rem;
    font-family: 'Plus Jakarta Sans', sans-serif;
  }

  /* SVG Diagrams Container */
  .svg-diagram-card {
    background: #ffffff;
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 1.5rem;
    margin: 2rem 0;
    box-shadow: var(--shadow-sm);
  }

  .svg-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1rem;
    flex-wrap: wrap;
    gap: 0.5rem;
  }

  .svg-caption {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 1.05rem;
    color: var(--dark);
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .svg-tag {
    font-size: 0.72rem;
    font-weight: 700;
    padding: 0.2rem 0.55rem;
    border-radius: 999px;
    background: var(--primary-light);
    color: var(--primary);
    text-transform: uppercase;
  }

  .svg-container {
    width: 100%;
    overflow-x: auto;
    display: flex;
    justify-content: center;
    align-items: center;
    background: #fafafa;
    border-radius: var(--radius-md);
    padding: 1rem;
    border: 1px dashed var(--border-dark);
  }

  .svg-container svg {
    max-width: 100%;
    height: auto;
    filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.05));
  }

  /* Collapsible Answer Boxes */
  details.ans-box {
    background: var(--light);
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    margin-bottom: 1.25rem;
    overflow: hidden;
    transition: all 0.2s ease;
  }

  details.ans-box[open] {
    background: var(--surface);
    border-color: var(--primary);
    box-shadow: var(--shadow-sm);
  }

  summary.ans-summary {
    padding: 1.1rem 1.35rem;
    font-weight: 700;
    font-size: 1rem;
    color: #1e293b;
    cursor: pointer;
    list-style: none;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    background: #f8fafc;
    border-bottom: 1px solid transparent;
    transition: background 0.2s ease;
  }

  summary.ans-summary::-webkit-details-marker {
    display: none;
  }

  details.ans-box[open] summary.ans-summary {
    background: #eff6ff;
    border-bottom-color: #bfdbfe;
    color: var(--primary);
  }

  summary.ans-summary::after {
    content: '\\f078';
    font-family: 'Font Awesome 6 Free';
    font-weight: 900;
    font-size: 0.85rem;
    color: var(--text-muted);
    transition: transform 0.2s ease;
  }

  details.ans-box[open] summary.ans-summary::after {
    transform: rotate(180deg);
    color: var(--primary);
  }

  .ans-content {
    padding: 1.5rem 1.75rem;
    font-size: 0.95rem;
  }

  /* 5-Step Solution Badges */
  .step-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    font-size: 0.75rem;
    font-weight: 800;
    padding: 0.2rem 0.55rem;
    border-radius: 999px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 0.5rem;
  }

  .step-1 { background: #fee2e2; color: #991b1b; }
  .step-2 { background: #fef3c7; color: #92400e; }
  .step-3 { background: #dbeafe; color: #1e40af; }
  .step-4 { background: #ede9fe; color: #6d28d9; }
  .step-5 { background: #dcfce7; color: #15803d; }

  /* Interactive Quiz Engine */
  .quiz-container {
    margin: 2rem 0;
  }

  .quiz-score-banner {
    background: linear-gradient(135deg, #0f172a, #1e3a8a);
    color: white;
    border-radius: var(--radius-lg);
    padding: 1.25rem 1.75rem;
    margin-bottom: 1.75rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1rem;
  }

  .quiz-score-text h4 {
    font-size: 1.1rem;
    font-weight: 700;
    font-family: 'Space Grotesk', sans-serif;
  }

  .quiz-score-counter {
    font-size: 1.5rem;
    font-weight: 800;
    color: #fbbf24;
    font-family: 'JetBrains Mono', monospace;
  }

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
    color: #1e293b;
    margin-bottom: 1rem;
  }

  .quiz-options {
    display: grid;
    grid-template-columns: 1fr;
    gap: 0.65rem;
    margin-bottom: 1rem;
  }

  .quiz-opt-btn {
    text-align: left;
    background: #f8fafc;
    border: 1.5px solid var(--border);
    border-radius: var(--radius-md);
    padding: 0.85rem 1.15rem;
    font-size: 0.93rem;
    font-weight: 600;
    color: var(--text);
    cursor: pointer;
    transition: all 0.2s ease;
    display: flex;
    align-items: center;
    gap: 0.75rem;
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
  }

  .quiz-opt-btn.incorrect {
    background: #fee2e2 !important;
    border-color: #ef4444 !important;
    color: #991b1b !important;
  }

  .quiz-feedback {
    display: none;
    padding: 1rem 1.25rem;
    border-radius: var(--radius-md);
    font-size: 0.9rem;
    line-height: 1.6;
    margin-top: 0.85rem;
  }

  .quiz-feedback.show {
    display: block;
  }

  .quiz-feedback.correct-feedback {
    background: #f0fdf4;
    border: 1px solid #86efac;
    color: #166534;
  }

  .quiz-feedback.incorrect-feedback {
    background: #fef2f2;
    border: 1px solid #fca5a5;
    color: #991b1b;
  }

  /* Section Toggle Controls */
  .section-toggle-bar {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 1rem;
  }

  .btn-toggle-all {
    background: var(--surface);
    border: 1px solid var(--border);
    color: var(--primary);
    font-weight: 700;
    font-size: 0.82rem;
    padding: 0.4rem 0.85rem;
    border-radius: var(--radius-sm);
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    transition: all 0.2s ease;
  }

  .btn-toggle-all:hover {
    background: var(--primary-light);
    border-color: var(--primary);
  }

  /* Responsive Adjustments */
  @media (max-width: 768px) {
    body { padding-top: 50px; font-size: 14.5px; }
    .top-nav { padding: 0 1rem; height: 50px; }
    .nav-links { display: none; }
    .container { padding: 1.25rem 1rem 3rem; }
    .hero-section { padding: 2rem 1.5rem; }
    .hero-title { font-size: 1.95rem; }
    .section-block { padding: 1.75rem 1.25rem; }
    .section-title { font-size: 1.5rem; }
  }
  </style>
</head>
<body>

  <!-- Top Linear Reading Progress Bar -->
  <div id="reading-progress-bar"></div>

  <!-- Fixed Top Header Navigation -->
  <nav class="top-nav">
    <a href="../../index.html" class="nav-brand">
      <i class="fa-solid fa-landmark-dome" style="color: #b45309;"></i>
      <span>Sujit Classes</span>
      <span class="brand-badge">Class 8 SST</span>
    </a>
    <ul class="nav-links">
      <li><a href="#section-1">Blueprint</a></li>
      <li><a href="#section-2">Concepts</a></li>
      <li><a href="#section-3">Fact Bank</a></li>
      <li><a href="#section-4">NCERT Solutions</a></li>
      <li><a href="#section-5">Exam Bank</a></li>
      <li><a href="#section-6">Trap Alerts</a></li>
    </ul>
    <div class="nav-actions">
      <button class="btn-audio-listen" id="btn-audio-nav" onclick="toggleAudioReader()">
        <i class="fa-solid fa-volume-high"></i>
        <span id="audio-btn-nav-text">Listen Summary</span>
      </button>
      <a href="../../index.html" class="btn-portal-back">
        <i class="fa-solid fa-house"></i>
        <span>Portal</span>
      </a>
    </div>
  </nav>

  <!-- Main Content Container -->
  <main class="container">

    <!-- Hero Section -->
    <header class="hero-section">
      <div class="hero-badge-row">
        <span class="hero-pill hero-pill-blue"><i class="fa-solid fa-graduation-cap"></i> CBSE Class 8 Social Science</span>
        <span class="hero-pill hero-pill-saffron"><i class="fa-solid fa-scroll"></i> NCERT Exploring Society Part 1</span>
        <span class="hero-pill hero-pill-green"><i class="fa-solid fa-check-double"></i> NEP Code: hess105</span>
        <span class="hero-pill hero-pill-blue"><i class="fa-solid fa-scale-balanced"></i> Governance & Democracy Unit</span>
      </div>

      <h1 class="hero-title">Universal Franchise and India's Electoral System</h1>
      <p class="hero-subtitle">
        Explore how 968 million Indian citizens exercise their supreme constitutional power through universal adult franchise, how independent constitutional bodies organize the world's largest democratic festival, and why every single vote holds equal value.
      </p>

      <!-- Alladi Krishnaswami Ayyar Opening Quote -->
      <div class="hero-quote-card">
        <p class="hero-quote-text">
          "[India] adopted the principle of adult franchise with an abundant faith in the common man and the ultimate success of democratic rule—never before in the history of the world has such an experiment been so boldly undertaken."
        </p>
        <p class="hero-quote-author">
          — Alladi Krishnaswami Ayyar, November 1949 (Constituent Assembly of India Debates)
        </p>
      </div>

      <!-- The Big Questions Tri-Card Grid -->
      <div class="big-questions-grid">
        <div class="bq-card">
          <div class="bq-icon"><i class="fa-solid fa-fingerprint"></i></div>
          <div class="bq-text">
            <h5>Big Question 1</h5>
            <p>What is universal adult franchise and why is it the bedrock of our democracy?</p>
          </div>
        </div>
        <div class="bq-card">
          <div class="bq-icon"><i class="fa-solid fa-gears"></i></div>
          <div class="bq-text">
            <h5>Big Question 2</h5>
            <p>What is an electoral system and how do direct vs indirect elections operate?</p>
          </div>
        </div>
        <div class="bq-card">
          <div class="bq-icon"><i class="fa-solid fa-shield-halved"></i></div>
          <div class="bq-text">
            <h5>Big Question 3</h5>
            <p>How does the Election Commission ensure free, fair, accessible, and fearless voting?</p>
          </div>
        </div>
      </div>

      <!-- Hero Metadata Statistics Grid -->
      <div class="hero-meta-grid">
        <div class="hero-meta-item">
          <div class="hero-meta-icon" style="background:#eff6ff; color:#1e3a8a;"><i class="fa-solid fa-users"></i></div>
          <div class="hero-meta-text">
            <h5>Electorate Scale</h5>
            <p>968 Million Registered Voters</p>
          </div>
        </div>
        <div class="hero-meta-item">
          <div class="hero-meta-icon" style="background:#fef3c7; color:#b45309;"><i class="fa-solid fa-building-columns"></i></div>
          <div class="hero-meta-text">
            <h5>Lok Sabha Seats</h5>
            <p>543 Constituencies (412 Gen, 84 SC, 47 ST)</p>
          </div>
        </div>
        <div class="hero-meta-item">
          <div class="hero-meta-icon" style="background:#f0fdf4; color:#047857;"><i class="fa-solid fa-person-shelter"></i></div>
          <div class="hero-meta-text">
            <h5>Polling Infrastructure</h5>
            <p>1,000,000+ Polling Stations</p>
          </div>
        </div>
        <div class="hero-meta-item">
          <div class="hero-meta-icon" style="background:#fdf2f8; color:#be123c;"><i class="fa-solid fa-scale-balanced"></i></div>
          <div class="hero-meta-text">
            <h5>Constitutional Anchors</h5>
            <p>Articles 324 & 326 of the Constitution</p>
          </div>
        </div>
      </div>
    </header>

    <!-- Audio Bar Player Widget -->
    <div class="audio-bar-card">
      <div class="audio-bar-info">
        <div class="audio-bar-icon">
          <i class="fa-solid fa-podcast"></i>
        </div>
        <div class="audio-bar-text">
          <h4>Smart Audio Companion & Explainer</h4>
          <p>Listen to a high-yield 3-minute executive revision of Chapter 5 spoken in crisp, student-friendly English.</p>
        </div>
      </div>
      <div class="audio-bar-controls">
        <button class="audio-btn" id="btn-audio-main" onclick="toggleAudioReader()">
          <i class="fa-solid fa-play"></i>
          <span id="audio-btn-main-text">Play Audio Summary</span>
        </button>
        <button class="audio-btn audio-btn-secondary" onclick="stopAudioReader()">
          <i class="fa-solid fa-stop"></i>
          <span>Stop</span>
        </button>
      </div>
    </div>
'''
