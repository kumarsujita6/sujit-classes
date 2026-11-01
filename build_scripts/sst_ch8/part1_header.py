# -*- coding: utf-8 -*-
"""
Part 1: HTML Head, Typography, Custom Responsive CSS, Fixed Top Navigation,
Hero Section, and Interactive Audio Reader Bar for Class 8 SST Chapter 8.
Chapter: World Geography: Some Glimpses (NCERT NEP Code: hess108 / hees201)
"""

PART1_CONTENT = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>World Geography: Some Glimpses - Class 8 Social Science NEP Master Study Note | Sujit Classes</title>
  <!-- Google Fonts: Space Grotesk, Plus Jakarta Sans, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Space+Grotesk:wght@500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <!-- Font Awesome 6 -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
  :root {
    --primary: #0284c7;           /* Ocean Azure */
    --primary-dark: #0369a1;      /* Deep Sea Navy */
    --primary-light: #e0f2fe;     /* Glacier Sky */
    --primary-ultra-light: #f0f9ff;
    --secondary: #0d9488;         /* Coral Teal / Emerald Coast */
    --secondary-dark: #0f766e;
    --secondary-light: #ccfbf1;
    --accent: #d97706;            /* Desert Amber / Saharan Gold */
    --accent-dark: #b45309;
    --accent-light: #fef3c7;
    --earth-green: #15803d;       /* Amazon Forest Green */
    --earth-light: #dcfce7;
    --plateau-purple: #7e22ce;    /* Tibetan Peak Purple */
    --plateau-light: #f3e8ff;
    --rose: #e11d48;              /* Coral Bleaching Rose */
    --rose-light: #ffe4e6;
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
    background: linear-gradient(90deg, #0284c7 0%, #0d9488 35%, #d97706 70%, #15803d 100%);
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
    font-weight: 800;
    font-size: 1.15rem;
    font-family: 'Space Grotesk', sans-serif;
    letter-spacing: -0.02em;
  }

  .nav-brand i {
    color: var(--primary);
    font-size: 1.35rem;
  }

  .nav-brand-badge {
    background: var(--primary-light);
    color: var(--primary-dark);
    font-size: 0.72rem;
    font-weight: 700;
    padding: 0.2rem 0.55rem;
    border-radius: 6px;
    letter-spacing: 0.04em;
    text-transform: uppercase;
  }

  .nav-tools {
    display: flex;
    align-items: center;
    gap: 0.65rem;
  }

  .btn-tool {
    background: var(--light);
    border: 1px solid var(--border);
    color: var(--text);
    padding: 0.42rem 0.85rem;
    border-radius: var(--radius-sm);
    font-size: 0.85rem;
    font-weight: 600;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    transition: all 0.2s ease;
    text-decoration: none;
    font-family: inherit;
  }

  .btn-tool:hover {
    background: var(--primary-light);
    color: var(--primary-dark);
    border-color: var(--primary);
    transform: translateY(-1px);
  }

  .btn-tool.active-audio {
    background: var(--rose-light);
    color: var(--rose);
    border-color: var(--rose);
    animation: pulseAudio 1.5s infinite;
  }

  @keyframes pulseAudio {
    0% { box-shadow: 0 0 0 0 rgba(225, 29, 72, 0.4); }
    70% { box-shadow: 0 0 0 8px rgba(225, 29, 72, 0); }
    100% { box-shadow: 0 0 0 0 rgba(225, 29, 72, 0); }
  }

  /* Main Container */
  .container {
    max-width: 960px;
    margin: 0 auto;
    padding: 2.25rem 1.25rem 5rem;
  }

  /* Breadcrumb */
  .breadcrumb {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.85rem;
    color: var(--text-muted);
    margin-bottom: 1.25rem;
    flex-wrap: wrap;
  }

  .breadcrumb a {
    color: var(--primary);
    text-decoration: none;
    font-weight: 600;
  }

  .breadcrumb a:hover {
    text-decoration: underline;
  }

  .breadcrumb i {
    font-size: 0.7rem;
    color: var(--text-muted);
  }

  /* Chapter Hero Card */
  .chapter-hero {
    background: linear-gradient(135deg, #0369a1 0%, #0284c7 45%, #0d9488 100%);
    color: white;
    border-radius: var(--radius-xl);
    padding: 3rem 2.25rem;
    margin-bottom: 2.5rem;
    box-shadow: var(--shadow-xl);
    position: relative;
    overflow: hidden;
  }

  .chapter-hero::before {
    content: "";
    position: absolute;
    top: -60px;
    right: -60px;
    width: 240px;
    height: 240px;
    background: radial-gradient(circle, rgba(255, 255, 255, 0.2) 0%, rgba(255, 255, 255, 0) 70%);
    border-radius: 50%;
    pointer-events: none;
  }

  .hero-pill-box {
    display: flex;
    gap: 0.6rem;
    margin-bottom: 1.25rem;
    flex-wrap: wrap;
  }

  .badge-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: rgba(255, 255, 255, 0.18);
    backdrop-filter: blur(6px);
    border: 1px solid rgba(255, 255, 255, 0.35);
    color: white;
    padding: 0.35rem 0.85rem;
    border-radius: 50px;
    font-size: 0.8rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }

  .badge-pill-gold {
    background: rgba(245, 158, 11, 0.28);
    border-color: rgba(245, 158, 11, 0.55);
    color: #fef08a;
  }

  .chapter-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.5rem;
    font-weight: 800;
    line-height: 1.2;
    margin-bottom: 1rem;
    letter-spacing: -0.03em;
    color: #ffffff;
  }

  .chapter-subtitle {
    font-size: 1.15rem;
    color: rgba(255, 255, 255, 0.92);
    margin-bottom: 1.75rem;
    max-width: 820px;
    line-height: 1.6;
    font-weight: 400;
  }

  .hero-quote-box {
    background: rgba(15, 23, 42, 0.3);
    border-left: 4px solid #fef08a;
    padding: 1rem 1.25rem;
    border-radius: 0 var(--radius-md) var(--radius-md) 0;
    margin-bottom: 2rem;
    font-style: italic;
    font-size: 0.95rem;
    color: #f1f5f9;
  }

  .hero-quote-box cite {
    display: block;
    font-style: normal;
    font-weight: 700;
    margin-top: 0.4rem;
    color: #fde047;
    font-size: 0.85rem;
  }

  .hero-stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 1rem;
    padding-top: 1.5rem;
    border-top: 1px solid rgba(255, 255, 255, 0.22);
  }

  .stat-item {
    display: flex;
    align-items: center;
    gap: 0.65rem;
    font-size: 0.88rem;
    font-weight: 600;
    color: #ffffff;
  }

  .stat-icon {
    width: 34px;
    height: 34px;
    border-radius: 8px;
    background: rgba(255, 255, 255, 0.2);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1rem;
    flex-shrink: 0;
  }

  /* Quick Navigation Bar */
  .quick-nav {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 1.35rem;
    margin-bottom: 2.75rem;
    box-shadow: var(--shadow-sm);
  }

  .quick-nav-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.9rem;
    flex-wrap: wrap;
    gap: 0.5rem;
  }

  .quick-nav-title {
    font-size: 0.85rem;
    font-weight: 800;
    color: var(--dark);
    text-transform: uppercase;
    letter-spacing: 0.06em;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .nav-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 0.55rem;
  }

  .nav-pill {
    padding: 0.45rem 0.95rem;
    background: var(--light);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    font-size: 0.82rem;
    font-weight: 700;
    color: var(--text);
    text-decoration: none;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
  }

  .nav-pill:hover {
    background: var(--primary);
    color: white;
    border-color: var(--primary);
    transform: translateY(-2px);
    box-shadow: 0 4px 10px rgba(2, 132, 199, 0.25);
  }

  /* Audio Bar Widget */
  .audio-bar-widget {
    background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%);
    border: 1px solid #a7f3d0;
    border-radius: var(--radius-md);
    padding: 1rem 1.25rem;
    margin-bottom: 2.5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    box-shadow: var(--shadow-sm);
  }

  .audio-info {
    display: flex;
    align-items: center;
    gap: 0.85rem;
  }

  .audio-icon-bubble {
    width: 42px;
    height: 42px;
    border-radius: 50%;
    background: #059669;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.15rem;
    flex-shrink: 0;
  }

  .audio-text h4 {
    font-size: 0.95rem;
    font-weight: 700;
    color: #065f46;
    margin-bottom: 0.15rem;
  }

  .audio-text p {
    font-size: 0.8rem;
    color: #047857;
    margin-bottom: 0;
  }

  .audio-controls {
    display: flex;
    gap: 0.5rem;
  }

  .btn-audio-action {
    background: #059669;
    color: white;
    border: none;
    padding: 0.45rem 1rem;
    border-radius: var(--radius-sm);
    font-size: 0.85rem;
    font-weight: 700;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    transition: all 0.2s ease;
    font-family: inherit;
  }

  .btn-audio-action:hover {
    background: #047857;
    transform: translateY(-1px);
  }

  .btn-audio-stop {
    background: #e2e8f0;
    color: #475569;
  }

  .btn-audio-stop:hover {
    background: #cbd5e1;
    color: #1e293b;
  }

  /* Section Card Styling */
  section {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-xl);
    padding: 2.75rem 2.25rem;
    margin-bottom: 3rem;
    box-shadow: var(--shadow-sm);
  }

  .section-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 2rem;
    padding-bottom: 1.25rem;
    border-bottom: 2px solid var(--border);
  }

  .section-icon {
    width: 52px;
    height: 52px;
    border-radius: var(--radius-md);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.45rem;
    background: var(--primary-light);
    color: var(--primary);
    flex-shrink: 0;
  }

  .section-header-text h2 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.85rem;
    font-weight: 800;
    color: var(--dark);
    line-height: 1.2;
    letter-spacing: -0.02em;
  }

  .section-tag {
    font-size: 0.78rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--primary-dark);
  }

  /* Subheadings & Typography */
  h3 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.35rem;
    font-weight: 700;
    color: var(--dark);
    margin: 2.25rem 0 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  h3::before {
    content: "";
    display: inline-block;
    width: 6px;
    height: 1.2em;
    background: var(--primary);
    border-radius: 4px;
  }

  h4 {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--primary-dark);
    margin: 1.5rem 0 0.65rem;
  }

  h5 {
    font-size: 0.98rem;
    font-weight: 700;
    color: var(--text);
    margin: 1.2rem 0 0.4rem;
  }

  p {
    margin-bottom: 1.25rem;
    color: var(--text);
  }

  ul, ol {
    margin-bottom: 1.35rem;
    padding-left: 1.6rem;
  }

  li {
    margin-bottom: 0.6rem;
    line-height: 1.7;
  }

  strong {
    color: var(--dark);
    font-weight: 700;
  }

  /* Callout Boxes */
  .callout {
    border-radius: var(--radius-lg);
    padding: 1.4rem 1.6rem;
    margin: 1.75rem 0;
    border-left: 5px solid;
    position: relative;
    box-shadow: var(--shadow-sm);
  }

  .callout-def {
    background: #eff6ff;
    border-color: #3b82f6;
    color: #1e3a8a;
  }

  .callout-act {
    background: #f0fdf4;
    border-color: #10b981;
    color: #064e3b;
  }

  .callout-pyq {
    background: #fffbeb;
    border-color: #f59e0b;
    color: #78350f;
  }

  .callout-hack {
    background: #faf5ff;
    border-color: #a855f7;
    color: #581c87;
  }

  .callout-warn {
    background: #fef2f2;
    border-color: #ef4444;
    color: #7f1d1d;
  }

  .callout-title {
    font-weight: 800;
    font-size: 1rem;
    margin-bottom: 0.6rem;
    display: flex;
    align-items: center;
    gap: 0.55rem;
    font-family: 'Space Grotesk', sans-serif;
  }

  .callout p:last-child,
  .callout ul:last-child,
  .callout ol:last-child {
    margin-bottom: 0;
  }

  /* Interactive Inline SVG Container */
  .svg-wrapper {
    background: #ffffff;
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 1.75rem 1.25rem;
    margin: 2.25rem 0;
    text-align: center;
    box-shadow: var(--shadow-sm);
    overflow-x: auto;
  }

  .svg-wrapper svg {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 0 auto;
  }

  .svg-caption {
    font-size: 0.88rem;
    color: var(--text-muted);
    margin-top: 1rem;
    font-weight: 600;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
  }

  /* Tables */
  .table-container {
    overflow-x: auto;
    margin: 1.75rem 0 2.25rem;
    border-radius: var(--radius-lg);
    border: 1px solid var(--border);
    box-shadow: var(--shadow-sm);
  }

  table.study-table {
    width: 100%;
    border-collapse: collapse;
    text-align: left;
    font-size: 0.94rem;
  }

  table.study-table th {
    background: #f1f5f9;
    padding: 0.95rem 1.15rem;
    font-weight: 800;
    color: var(--dark);
    border-bottom: 2px solid var(--border-dark);
    font-family: 'Space Grotesk', sans-serif;
  }

  table.study-table td {
    padding: 0.95rem 1.15rem;
    border-bottom: 1px solid var(--border);
    vertical-align: top;
    line-height: 1.65;
  }

  table.study-table tr:last-child td {
    border-bottom: none;
  }

  table.study-table tr:nth-child(even) {
    background: #f8fafc;
  }

  table.study-table tr:hover {
    background: #f0f9ff;
  }

  .badge-tag {
    display: inline-block;
    padding: 0.2rem 0.6rem;
    border-radius: 6px;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
  }

  .badge-blue { background: #dbeafe; color: #1e40af; }
  .badge-green { background: #dcfce7; color: #166534; }
  .badge-amber { background: #fef3c7; color: #92400e; }
  .badge-purple { background: #ede9fe; color: #6b21a8; }
  .badge-rose { background: #ffe4e6; color: #9f1239; }

  /* Accordion Answer Boxes (<details class="ans-box">) */
  .accordion-controls {
    display: flex;
    justify-content: flex-end;
    gap: 0.6rem;
    margin-bottom: 1rem;
  }

  .btn-accordion-toggle {
    background: var(--light);
    border: 1px solid var(--border);
    color: var(--text);
    padding: 0.35rem 0.75rem;
    border-radius: var(--radius-sm);
    font-size: 0.8rem;
    font-weight: 600;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    font-family: inherit;
    transition: all 0.2s ease;
  }

  .btn-accordion-toggle:hover {
    background: var(--primary-light);
    color: var(--primary-dark);
    border-color: var(--primary);
  }

  details.ans-box {
    background: var(--light);
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    margin-bottom: 1.15rem;
    overflow: hidden;
    transition: all 0.25s ease;
  }

  details.ans-box[open] {
    background: var(--surface);
    border-color: var(--primary);
    box-shadow: var(--shadow-md);
  }

  details.ans-box summary {
    padding: 1.15rem 1.35rem;
    font-weight: 700;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
    color: var(--dark);
    user-select: none;
    font-size: 1.02rem;
    gap: 1rem;
  }

  details.ans-box summary:hover {
    background: var(--primary-ultra-light);
    color: var(--primary-dark);
  }

  details.ans-box summary .q-title {
    display: flex;
    align-items: center;
    gap: 0.65rem;
    text-align: left;
  }

  details.ans-box summary .q-badge {
    background: var(--primary);
    color: white;
    font-size: 0.75rem;
    padding: 0.2rem 0.6rem;
    border-radius: 6px;
    font-weight: 700;
    flex-shrink: 0;
  }

  details.ans-box summary .chevron-icon {
    transition: transform 0.25s ease;
    color: var(--primary);
    font-size: 0.95rem;
  }

  details.ans-box[open] summary .chevron-icon {
    transform: rotate(180deg);
  }

  details.ans-box .ans-content {
    padding: 1.4rem 1.6rem;
    border-top: 1px solid var(--border);
    font-size: 0.96rem;
    color: var(--text);
    background: #ffffff;
  }

  /* 5-Step Presentation inside Answer Boxes */
  .step-box {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.25rem;
    align-items: flex-start;
  }

  .step-badge {
    background: #e2e8f0;
    color: #334155;
    font-size: 0.75rem;
    font-weight: 800;
    padding: 0.25rem 0.6rem;
    border-radius: 6px;
    white-space: nowrap;
    text-transform: uppercase;
    flex-shrink: 0;
    margin-top: 0.2rem;
  }

  .step-badge-1 { background: #dbeafe; color: #1e40af; }
  .step-badge-2 { background: #e0e7ff; color: #3730a3; }
  .step-badge-3 { background: #dcfce7; color: #166534; }
  .step-badge-4 { background: #fef3c7; color: #92400e; }
  .step-badge-5 { background: #ede9fe; color: #6b21a8; }

  .step-text {
    flex: 1;
  }

  /* Interactive Quiz Engine */
  .quiz-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 1.75rem 1.6rem;
    margin-bottom: 1.6rem;
    box-shadow: var(--shadow-sm);
    transition: border-color 0.2s ease;
  }

  .quiz-card:hover {
    border-color: var(--primary-light);
  }

  .quiz-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1rem;
  }

  .quiz-category-tag {
    font-size: 0.72rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding: 0.2rem 0.55rem;
    border-radius: 6px;
    background: var(--primary-light);
    color: var(--primary-dark);
  }

  .quiz-q {
    font-weight: 700;
    font-size: 1.05rem;
    color: var(--dark);
    margin-bottom: 1.25rem;
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
  }

  .quiz-num {
    background: var(--primary);
    color: white;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 0.9rem;
    font-weight: 800;
    flex-shrink: 0;
  }

  .quiz-options {
    display: grid;
    grid-template-columns: 1fr;
    gap: 0.75rem;
    margin-bottom: 1rem;
  }

  .opt-btn {
    text-align: left;
    padding: 0.85rem 1.15rem;
    background: var(--light);
    border: 1.5px solid var(--border);
    border-radius: var(--radius-md);
    font-size: 0.94rem;
    cursor: pointer;
    transition: all 0.2s ease;
    font-family: inherit;
    color: var(--text);
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }

  .opt-btn:hover:not(:disabled) {
    background: var(--primary-light);
    border-color: var(--primary);
    color: var(--primary-dark);
  }

  .opt-letter {
    font-weight: 800;
    width: 24px;
    height: 24px;
    border-radius: 6px;
    background: #e2e8f0;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 0.8rem;
    flex-shrink: 0;
  }

  .opt-btn.correct {
    background: #dcfce7 !important;
    border-color: #22c55e !important;
    color: #14532d !important;
    font-weight: 700;
  }

  .opt-btn.correct .opt-letter {
    background: #22c55e;
    color: white;
  }

  .opt-btn.wrong {
    background: #fee2e2 !important;
    border-color: #ef4444 !important;
    color: #7f1d1d !important;
  }

  .opt-btn.wrong .opt-letter {
    background: #ef4444;
    color: white;
  }

  .trap-explanation {
    display: none;
    margin-top: 1rem;
    padding: 1.15rem 1.35rem;
    border-radius: var(--radius-md);
    font-size: 0.92rem;
    line-height: 1.65;
    background: #f8fafc;
    border-left: 4px solid var(--primary);
  }

  .score-board {
    background: linear-gradient(135deg, #0284c7 0%, #0d9488 100%);
    color: white;
    border-radius: var(--radius-lg);
    padding: 2rem;
    text-align: center;
    margin-top: 2rem;
    box-shadow: var(--shadow-md);
  }

  .score-text {
    font-size: 1.45rem;
    font-weight: 800;
    margin-bottom: 0.5rem;
    font-family: 'Space Grotesk', sans-serif;
  }

  .score-sub {
    font-size: 0.95rem;
    opacity: 0.95;
  }

  /* Revision List Styling */
  .revision-list {
    list-style: none;
    padding-left: 0;
    display: grid;
    grid-template-columns: 1fr;
    gap: 0.85rem;
  }

  .revision-item {
    background: var(--light);
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    padding: 1rem 1.25rem;
    display: flex;
    align-items: flex-start;
    gap: 0.85rem;
    transition: transform 0.2s ease;
  }

  .revision-item:hover {
    transform: translateX(4px);
    background: #ffffff;
    border-color: var(--primary-light);
  }

  .revision-num {
    background: var(--primary-light);
    color: var(--primary-dark);
    font-weight: 800;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 0.82rem;
    flex-shrink: 0;
    margin-top: 0.15rem;
  }

  /* Floating Back to Top Button */
  #back-to-top {
    position: fixed;
    bottom: 28px;
    right: 28px;
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: var(--primary);
    color: white;
    border: none;
    box-shadow: var(--shadow-xl);
    cursor: pointer;
    display: none;
    align-items: center;
    justify-content: center;
    font-size: 1.25rem;
    z-index: 1000;
    transition: all 0.25s var(--ease-spring);
  }

  #back-to-top:hover {
    background: var(--primary-dark);
    transform: translateY(-4px) scale(1.05);
  }

  /* Footer */
  footer {
    text-align: center;
    padding: 3rem 1.5rem;
    border-top: 1px solid var(--border);
    color: var(--text-muted);
    font-size: 0.9rem;
    background: #ffffff;
    border-radius: var(--radius-xl);
    margin-top: 2rem;
  }

  footer a {
    color: var(--primary);
    text-decoration: none;
    font-weight: 600;
  }

  footer a:hover {
    text-decoration: underline;
  }

  /* Responsive Design */
  @media (max-width: 768px) {
    .chapter-title { font-size: 1.85rem; }
    .chapter-hero { padding: 2rem 1.5rem; }
    section { padding: 1.85rem 1.25rem; }
    .hero-stats { grid-template-columns: 1fr 1fr; }
    .audio-bar-widget { flex-direction: column; align-items: flex-start; }
    .audio-controls { width: 100%; justify-content: space-between; }
  }

  @media (max-width: 480px) {
    .hero-stats { grid-template-columns: 1fr; }
    .nav-brand span { display: none; }
  }
  </style>
</head>
<body>

  <!-- Top Fixed Reading Progress Bar -->
  <div id="reading-progress-bar"></div>

  <!-- Top Sticky Navigation Bar -->
  <nav class="top-nav">
    <a href="../../index.html" class="nav-brand">
      <i class="fa-solid fa-earth-americas"></i>
      <span>Sujit Classes</span>
      <span class="nav-brand-badge">Class 8 SST</span>
    </a>
    <div class="nav-tools">
      <button class="btn-tool" id="speech-btn" onclick="toggleAudioReader()">
        <i class="fa-solid fa-volume-high"></i>
        <span id="speech-btn-text">Listen</span>
      </button>
      <a href="../../index.html" class="btn-tool">
        <i class="fa-solid fa-house"></i>
        <span>Portal</span>
      </a>
    </div>
  </nav>

  <div class="container">

    <!-- Breadcrumb Hierarchy -->
    <div class="breadcrumb">
      <a href="../../index.html"><i class="fa-solid fa-house"></i> Home</a>
      <i class="fa-solid fa-chevron-right"></i>
      <a href="../../index.html">Class 8</a>
      <i class="fa-solid fa-chevron-right"></i>
      <a href="../../index.html">Social Science</a>
      <i class="fa-solid fa-chevron-right"></i>
      <span>Chapter 8: World Geography: Some Glimpses</span>
    </div>

    <!-- Chapter Hero Card -->
    <header class="chapter-hero">
      <div class="hero-pill-box">
        <span class="badge-pill"><i class="fa-solid fa-book-open"></i> NCERT NEP 2020 &bull; Grade 8 Part 2</span>
        <span class="badge-pill badge-pill-gold"><i class="fa-solid fa-star"></i> hess108 &bull; Comprehensive Benchmark</span>
        <span class="badge-pill"><i class="fa-solid fa-globe"></i> Theme A: India and the World</span>
      </div>

      <h1 class="chapter-title">Chapter 8: World Geography: Some Glimpses</h1>
      <p class="chapter-subtitle">
        An exhaustive, zero-omission journey across planet Earth: From map projection geometry and global ocean circulation to the high roof of Tibet, the fiery Sahara, the ancient Amazon, and indigenous environmental reverence.
      </p>

      <div class="hero-quote-box">
        "The modern age has brought the geography of the earth near to us, but made it difficult for us to come into touch with man."
        <cite>&mdash; Rabindranath Tagore (Nobel Laureate, 1913)</cite>
      </div>

      <div class="hero-stats">
        <div class="stat-item">
          <div class="stat-icon"><i class="fa-solid fa-clock"></i></div>
          <div><strong>45 Mins</strong><br><span style="opacity:0.85; font-size:0.78rem;">Exhaustive Read</span></div>
        </div>
        <div class="stat-item">
          <div class="stat-icon"><i class="fa-solid fa-diagram-project"></i></div>
          <div><strong>6 Inline SVGs</strong><br><span style="opacity:0.85; font-size:0.78rem;">High-Precision Visuals</span></div>
        </div>
        <div class="stat-item">
          <div class="stat-icon"><i class="fa-solid fa-check-double"></i></div>
          <div><strong>100% Solved</strong><br><span style="opacity:0.85; font-size:0.78rem;">In-Text &amp; Exercises</span></div>
        </div>
        <div class="stat-item">
          <div class="stat-icon"><i class="fa-solid fa-graduation-cap"></i></div>
          <div><strong>27+ Questions</strong><br><span style="opacity:0.85; font-size:0.78rem;">Complete Question Bank</span></div>
        </div>
      </div>
    </header>

    <!-- Audio Player Notification Bar -->
    <div class="audio-bar-widget">
      <div class="audio-info">
        <div class="audio-icon-bubble"><i class="fa-solid fa-headphones"></i></div>
        <div class="audio-text">
          <h4>Smart Audio Companion (Text-to-Speech)</h4>
          <p>Listen to pronunciation of geographic terms and core conceptual summaries in Indian English.</p>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-audio-action" id="audio-bar-play" onclick="toggleAudioReader()">
          <i class="fa-solid fa-play"></i> Listen Now
        </button>
        <button class="btn-audio-action btn-audio-stop" onclick="stopAudioReader()">
          <i class="fa-solid fa-stop"></i> Stop
        </button>
      </div>
    </div>

    <!-- Quick Navigation Bar -->
    <nav class="quick-nav">
      <div class="quick-nav-header">
        <div class="quick-nav-title"><i class="fa-solid fa-compass"></i> Chapter Sections Roadmap</div>
        <span style="font-size:0.78rem; color:var(--text-muted); font-weight:600;">Click to jump directly to any section</span>
      </div>
      <div class="nav-pills">
        <a href="#sec1" class="nav-pill"><i class="fa-solid fa-sitemap"></i> 1. Visual Blueprint</a>
        <a href="#sec2" class="nav-pill"><i class="fa-solid fa-book-bookmark"></i> 2. Complete Concepts</a>
        <a href="#sec2-vocab" class="nav-pill"><i class="fa-solid fa-language"></i> 2. Bilingual Glossary</a>
        <a href="#sec3" class="nav-pill"><i class="fa-solid fa-table-list"></i> 3. Rapid Revision Bank</a>
        <a href="#sec4" class="nav-pill"><i class="fa-solid fa-pen-to-square"></i> 4. 100% Solved NCERT</a>
        <a href="#sec5" class="nav-pill"><i class="fa-solid fa-brain"></i> 5. Exam Question Bank</a>
        <a href="#sec6" class="nav-pill"><i class="fa-solid fa-shield-halved"></i> 6. Traps &amp; Key Points</a>
      </div>
    </nav>
'''
