# -*- coding: utf-8 -*-
"""
Styles and Head Module for Class 8 Mathematics Chapter 11
Exploring Some Geometric Themes (NCERT NEP code: hegp111)
"""

def get_head_and_styles():
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Exploring Some Geometric Themes - Class 8 Mathematics Chapter 11 Master Study Notes (Ganita Prakash) | Sujit Classes</title>
  <meta name="description" content="Exhaustive, zero-omission master study notes for Class 8 Mathematics Chapter 11: Exploring Some Geometric Themes (NCERT Ganita Prakash Grade 8 Part-II NEP code: hegp111). Complete coverage of fractals, self-similarity, Sierpinski Carpet, Sierpinski Gasket, Koch Snowflake, temple architecture fractals, polyhedra, 11 cube nets, Platonic solids, Euler's formula, surface geodesics (Ant & Laddu shortest paths), orthographic projections (front, top, side views), isometric grid drafting, optical illusions, and 100% solved textbook exercises.">
  <!-- Google Fonts: Space Grotesk, Plus Jakarta Sans, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Space+Grotesk:wght@500;600;700;800&display=swap" rel="stylesheet">
  <!-- Font Awesome 6.5.0 Free CDN -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

  <style>
    /* ==========================================================
       CSS VARIABLES & THEME DEFINITIONS
       ========================================================== */
    :root {
      --primary: #4f46e5;         /* Indigo 600 - Geometric Theme Core */
      --primary-light: #6366f1;   /* Indigo 500 */
      --primary-dark: #3730a3;    /* Indigo 800 */
      --primary-tint: #eef2ff;    /* Indigo 50 */
      --secondary: #0891b2;       /* Cyan 600 */
      --secondary-light: #06b6d4; /* Cyan 500 */
      --secondary-tint: #ecfeff;  /* Cyan 50 */
      --accent: #f59e0b;          /* Amber 500 */
      --accent-warm: #d97706;     /* Amber 600 */
      --accent-tint: #fefce8;     /* Amber 50 */
      --purple: #9333ea;          /* Purple 600 */
      --purple-light: #a855f7;    /* Purple 500 */
      --purple-tint: #faf5ff;     /* Purple 50 */
      --emerald: #059669;         /* Emerald 600 */
      --emerald-tint: #ecfdf5;    /* Emerald 50 */
      --danger: #dc2626;          /* Red 600 */
      --danger-tint: #fef2f2;     /* Red 50 */
      --info: #2563eb;            /* Blue 600 */
      
      --bg-page: #f8fafc;         /* Slate 50 */
      --bg-surface: #ffffff;      /* Pure White */
      --bg-card: #f1f5f9;         /* Slate 100 */
      --bg-card-alt: #ffffff;     /* White Card */
      
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
      line-height: 1.75;
      -webkit-font-smoothing: antialiased;
      position: relative;
    }

    /* Top-Fixed Reading Progress Bar */
    #progressBarContainer {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 4px;
      background: rgba(226, 232, 240, 0.6);
      z-index: 9999;
    }

    #progressBar {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #4f46e5, #0891b2, #9333ea, #f59e0b);
      transition: width 0.1s ease-out;
    }

    /* Header & Navigation */
    .top-nav {
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 0.75rem 1.5rem;
      position: sticky;
      top: 4px;
      z-index: 1000;
      box-shadow: var(--shadow-sm);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
    }

    .brand-group {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
    }

    .brand-logo {
      width: 38px;
      height: 38px;
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-weight: 800;
      font-size: 1.2rem;
    }

    .brand-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-main);
    }

    .brand-subtitle {
      font-size: 0.75rem;
      color: var(--text-muted);
      display: block;
    }

    .breadcrumb {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.85rem;
      color: var(--text-muted);
    }

    .breadcrumb a {
      color: var(--text-muted);
      text-decoration: none;
    }

    .breadcrumb a:hover {
      color: var(--primary);
    }

    .nav-pills {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
    }

    .nav-pill {
      font-size: 0.75rem;
      font-weight: 600;
      padding: 0.35rem 0.75rem;
      border-radius: var(--radius-full);
      background: var(--bg-card);
      color: var(--text-muted);
      text-decoration: none;
      border: 1px solid var(--border);
      transition: all 0.2s ease;
    }

    .nav-pill:hover {
      background: var(--primary-tint);
      color: var(--primary);
      border-color: var(--primary-light);
      text-decoration: none;
    }

    /* Container */
    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 2rem 1.5rem;
    }

    /* Hero Banner */
    .hero-banner {
      background: linear-gradient(135deg, #312e81 0%, #4f46e5 50%, #0891b2 100%);
      color: #ffffff;
      padding: 3rem 2.5rem;
      border-radius: var(--radius-xl);
      box-shadow: var(--shadow-lg);
      margin-bottom: 2.5rem;
      position: relative;
      overflow: hidden;
    }

    .hero-banner::after {
      content: "";
      position: absolute;
      top: -40px;
      right: -40px;
      width: 280px;
      height: 280px;
      background: radial-gradient(circle, rgba(255,255,255,0.18) 0%, rgba(255,255,255,0) 70%);
      border-radius: 50%;
      pointer-events: none;
    }

    .hero-badges {
      display: flex;
      gap: 0.6rem;
      flex-wrap: wrap;
      margin-bottom: 1.25rem;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.35rem 0.85rem;
      border-radius: var(--radius-full);
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.03em;
      text-transform: uppercase;
    }

    .badge-primary {
      background: rgba(255, 255, 255, 0.2);
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.35);
      backdrop-filter: blur(4px);
    }

    .badge-gold {
      background: #fef08a;
      color: #854d0e;
      border: 1px solid #fde047;
    }

    .badge-emerald {
      background: #a7f3d0;
      color: #065f46;
      border: 1px solid #6ee7b7;
    }

    .hero-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: clamp(2rem, 4vw, 2.9rem);
      font-weight: 800;
      line-height: 1.15;
      margin-bottom: 1rem;
      color: #ffffff;
    }

    .hero-subtitle {
      font-size: 1.1rem;
      color: #e0e7ff;
      max-width: 900px;
      margin-bottom: 1.75rem;
      line-height: 1.6;
    }

    .hero-stats {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 1rem;
      background: rgba(0, 0, 0, 0.18);
      padding: 1.25rem;
      border-radius: var(--radius-lg);
      border: 1px solid rgba(255, 255, 255, 0.15);
    }

    .stat-item {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .stat-icon {
      font-size: 1.6rem;
      color: #a5b4fc;
    }

    .stat-text h4 {
      font-size: 1.1rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 0.15rem;
    }

    .stat-text p {
      font-size: 0.75rem;
      color: #c7d2fe;
      margin-bottom: 0;
    }

    /* TTS Audio Reader Bar */
    .tts-container {
      background: #ffffff;
      border: 1px solid #c7d2fe;
      border-left: 5px solid var(--primary);
      border-radius: var(--radius-lg);
      padding: 1.25rem 1.75rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow-sm);
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 1.25rem;
    }

    .tts-info {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .tts-icon-box {
      width: 48px;
      height: 48px;
      border-radius: var(--radius-full);
      background: var(--primary-tint);
      color: var(--primary);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.35rem;
    }

    .tts-details h4 {
      font-size: 1rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 0.2rem;
    }

    .tts-details p {
      font-size: 0.825rem;
      color: var(--text-muted);
      margin-bottom: 0;
    }

    .tts-controls {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      flex-wrap: wrap;
    }

    .tts-btn {
      background: var(--primary);
      color: #ffffff;
      border: none;
      padding: 0.6rem 1.25rem;
      border-radius: var(--radius-md);
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.2s ease;
      box-shadow: var(--shadow-sm);
    }

    .tts-btn:hover {
      background: var(--primary-dark);
      transform: translateY(-1px);
    }

    .tts-select {
      background: var(--bg-card);
      border: 1px solid var(--border);
      padding: 0.55rem 0.85rem;
      border-radius: var(--radius-md);
      font-size: 0.85rem;
      color: var(--text-main);
      outline: none;
      cursor: pointer;
    }

    /* Section Headers */
    .section-box {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-xl);
      padding: 2.5rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow-sm);
    }

    .section-header {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      margin-bottom: 2rem;
      padding-bottom: 1.25rem;
      border-bottom: 2px solid var(--border);
      flex-wrap: wrap;
      gap: 1rem;
    }

    .section-header-left {
      max-width: 850px;
    }

    .section-tag {
      font-size: 0.75rem;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--primary);
      margin-bottom: 0.4rem;
      display: inline-block;
    }

    .section-title {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 1.85rem;
      font-weight: 700;
      color: var(--text-main);
      line-height: 1.25;
    }

    .section-desc {
      font-size: 0.95rem;
      color: var(--text-muted);
      margin-top: 0.4rem;
      margin-bottom: 0;
    }

    /* Pastel Callout Boxes */
    .callout {
      border-radius: var(--radius-lg);
      padding: 1.35rem 1.6rem;
      margin: 1.5rem 0;
      position: relative;
      border-left: 5px solid;
    }

    .callout p:last-child {
      margin-bottom: 0;
    }

    .callout-title {
      font-weight: 700;
      font-size: 0.95rem;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .callout-def {
      background-color: var(--primary-tint);
      border-left-color: var(--primary);
      color: #312e81;
    }
    .callout-def .callout-title { color: var(--primary-dark); }

    .callout-act {
      background-color: var(--secondary-tint);
      border-left-color: var(--secondary);
      color: #155e75;
    }
    .callout-act .callout-title { color: var(--secondary); }

    .callout-pyq {
      background-color: var(--purple-tint);
      border-left-color: var(--purple);
      color: #581c87;
    }
    .callout-pyq .callout-title { color: var(--purple); }

    .callout-hack {
      background-color: var(--accent-tint);
      border-left-color: var(--accent-warm);
      color: #78350f;
    }
    .callout-hack .callout-title { color: var(--accent-warm); }

    .callout-warn {
      background-color: var(--danger-tint);
      border-left-color: var(--danger);
      color: #7f1d1d;
    }
    .callout-warn .callout-title { color: var(--danger); }

    /* Concept Cards */
    .concept-card {
      background: var(--bg-card-alt);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.75rem;
      margin-bottom: 2rem;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s ease;
    }

    .concept-card:hover {
      box-shadow: var(--shadow-md);
      border-color: #cbd5e1;
    }

    .concept-card-title {
      font-size: 1.35rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.65rem;
    }

    .concept-card-title i {
      color: var(--primary);
    }

    /* Math Formula Blocks */
    .math-block {
      background: #f8fafc;
      border: 1px dashed var(--border-dark);
      border-radius: var(--radius-md);
      padding: 1rem 1.5rem;
      margin: 1.25rem 0;
      font-family: 'JetBrains Mono', monospace;
      font-size: 1.05rem;
      color: #1e293b;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      line-height: 1.8;
      overflow-x: auto;
    }

    .math-inline {
      font-family: 'JetBrains Mono', monospace;
      background: #eef2ff;
      color: #3730a3;
      padding: 0.15em 0.4em;
      border-radius: 4px;
      font-size: 0.95em;
      border: 1px solid #c7d2fe;
    }

    /* Tables */
    .data-table-wrapper {
      width: 100%;
      overflow-x: auto;
      margin: 1.5rem 0;
      border-radius: var(--radius-lg);
      border: 1px solid var(--border);
      box-shadow: var(--shadow-sm);
    }

    .data-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.925rem;
      text-align: left;
      background: #ffffff;
    }

    .data-table th {
      background: #f1f5f9;
      color: var(--text-main);
      font-weight: 700;
      padding: 0.85rem 1.25rem;
      border-bottom: 2px solid var(--border-dark);
    }

    .data-table td {
      padding: 0.85rem 1.25rem;
      border-bottom: 1px solid var(--border);
      color: var(--text-main);
      vertical-align: top;
    }

    .data-table tr:last-child td {
      border-bottom: none;
    }

    .data-table tr:hover td {
      background-color: #f8fafc;
    }

    .vocab-table td:nth-child(4) {
      font-family: 'Plus Jakarta Sans', 'Segoe UI', 'Kalinga', sans-serif;
      font-weight: 600;
      color: #4f46e5;
      font-size: 1rem;
    }

    /* Step Pill */
    .step-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.2rem 0.65rem;
      border-radius: var(--radius-full);
      background: #e0e7ff;
      color: #4338ca;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 0.4rem;
    }

    /* Collapsible Question / Answer Box */
    details.ans-box {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      margin-bottom: 1.25rem;
      box-shadow: var(--shadow-sm);
      overflow: hidden;
      transition: all 0.25s ease;
    }

    details.ans-box:hover {
      border-color: #cbd5e1;
    }

    details.ans-box[open] {
      border-color: #a5b4fc;
      box-shadow: var(--shadow-md);
    }

    details.ans-box summary {
      padding: 1.15rem 1.5rem;
      font-weight: 700;
      font-size: 1rem;
      cursor: pointer;
      list-style: none;
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: #f8fafc;
      color: var(--text-main);
      user-select: none;
      transition: background-color 0.2s ease;
    }

    details.ans-box summary::-webkit-details-marker {
      display: none;
    }

    details.ans-box summary:hover {
      background: #eef2ff;
    }

    details.ans-box summary::after {
      content: "\\f078";
      font-family: 'Font Awesome 6 Free';
      font-weight: 900;
      font-size: 0.85rem;
      color: var(--primary);
      transition: transform 0.25s ease;
    }

    details.ans-box[open] summary::after {
      transform: rotate(180deg);
    }

    .ans-content {
      padding: 1.5rem;
      background: #ffffff;
      border-top: 1px solid var(--border);
    }

    .ans-step {
      margin-bottom: 1rem;
      padding-left: 1rem;
      border-left: 3px solid #e2e8f0;
    }

    .ans-step-title {
      font-weight: 700;
      font-size: 0.85rem;
      color: var(--primary-dark);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 0.25rem;
    }

    /* MCQs & Quiz Engine */
    .mcq-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.75rem;
      margin-bottom: 1.5rem;
      box-shadow: var(--shadow-sm);
    }

    .mcq-question {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 1.25rem;
      line-height: 1.5;
    }

    .options-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.75rem;
      margin-bottom: 1rem;
    }

    @media (min-width: 640px) {
      .options-grid {
        grid-template-columns: 1fr 1fr;
      }
    }

    .option-btn {
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 0.85rem 1.15rem;
      text-align: left;
      font-size: 0.925rem;
      font-weight: 500;
      color: var(--text-main);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.75rem;
      transition: all 0.2s ease;
      width: 100%;
    }

    .option-btn:hover:not(:disabled) {
      background: #eef2ff;
      border-color: var(--primary-light);
    }

    .pos-badge {
      width: 26px;
      height: 26px;
      border-radius: 50%;
      background: #e2e8f0;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.75rem;
      font-weight: 700;
      flex-shrink: 0;
    }

    .option-btn.selected-correct {
      background: #ecfdf5 !important;
      border-color: #10b981 !important;
      color: #065f46 !important;
    }

    .option-btn.selected-correct .pos-badge {
      background: #10b981 !important;
      color: #ffffff !important;
    }

    .option-btn.selected-wrong {
      background: #fef2f2 !important;
      border-color: #ef4444 !important;
      color: #991b1b !important;
    }

    .option-btn.selected-wrong .pos-badge {
      background: #ef4444 !important;
      color: #ffffff !important;
    }

    .trap-feedback {
      display: none;
      padding: 1rem 1.25rem;
      border-radius: var(--radius-md);
      font-size: 0.9rem;
      line-height: 1.6;
      margin-top: 1rem;
    }

    .trap-feedback.show {
      display: block;
      animation: fadeIn 0.3s ease;
    }

    .correct-feedback {
      background: #ecfdf5;
      border-left: 4px solid #10b981;
      color: #065f46;
    }

    .wrong-feedback {
      background: #fef2f2;
      border-left: 4px solid #ef4444;
      color: #991b1b;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(-4px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .score-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: #e0e7ff;
      color: #3730a3;
      padding: 0.5rem 1rem;
      border-radius: var(--radius-full);
      font-weight: 700;
      font-size: 0.9rem;
    }

    /* SVG Graphics Container */
    .svg-graphic-box {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      margin: 2rem 0;
      text-align: center;
      box-shadow: var(--shadow-sm);
      overflow-x: auto;
    }

    .svg-graphic-box svg {
      max-width: 100%;
      height: auto;
      display: inline-block;
    }

    .svg-caption {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-top: 0.75rem;
      font-weight: 500;
    }

    /* Footer */
    .page-footer {
      background: #0f172a;
      color: #94a3b8;
      padding: 3.5rem 1.5rem 2.5rem;
      margin-top: 4rem;
      border-top: 1px solid #1e293b;
    }

    .footer-content {
      max-width: 1200px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 2rem;
      margin-bottom: 2.5rem;
    }

    .footer-col h4 {
      color: #ffffff;
      font-size: 1.1rem;
      font-weight: 700;
      margin-bottom: 1rem;
      font-family: 'Space Grotesk', sans-serif;
    }

    .footer-col p {
      font-size: 0.875rem;
      line-height: 1.6;
      color: #94a3b8;
    }

    .footer-links {
      list-style: none;
      margin: 0;
    }

    .footer-links li {
      margin-bottom: 0.5rem;
    }

    .footer-links a {
      color: #94a3b8;
      text-decoration: none;
      font-size: 0.875rem;
      transition: color 0.2s ease;
    }

    .footer-links a:hover {
      color: #818cf8;
    }

    .footer-bottom {
      max-width: 1200px;
      margin: 0 auto;
      padding-top: 1.75rem;
      border-top: 1px solid #334155;
      text-align: center;
      font-size: 0.8rem;
      color: #64748b;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
      .section-box {
        padding: 1.5rem;
      }
      .hero-banner {
        padding: 2rem 1.5rem;
      }
      .hero-stats {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>
  <!-- Reading Progress Bar -->
  <div id="progressBarContainer">
    <div id="progressBar"></div>
  </div>

  <!-- Top Sticky Navbar -->
  <nav class="top-nav">
    <a href="../../index.html" class="brand-group">
      <div class="brand-logo"><i class="fa-solid fa-shapes"></i></div>
      <div>
        <span class="brand-title">Sujit Classes</span>
        <span class="brand-subtitle">Master Study Notes Portal</span>
      </div>
    </a>
    
    <div class="breadcrumb">
      <a href="../../index.html"><i class="fa-solid fa-house"></i> Home</a>
      <span>/</span>
      <span>Class 8</span>
      <span>/</span>
      <span>Mathematics</span>
      <span>/</span>
      <span style="color: var(--primary); font-weight: 600;">Chapter 11</span>
    </div>

    <div class="nav-pills">
      <a href="#section1" class="nav-pill">§ 1. Blueprint</a>
      <a href="#section2" class="nav-pill">§ 2. Concepts & Vocab</a>
      <a href="#section3" class="nav-pill">§ 3. Formula Bank</a>
      <a href="#section4" class="nav-pill">§ 4. Solved NCERT</a>
      <a href="#section5" class="nav-pill">§ 5. Exam Bank</a>
      <a href="#section6" class="nav-pill">§ 6. Trap Alerts</a>
    </div>
  </nav>

  <div class="container">
"""
