import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Class 8 Social Science: India's Long Road to Independence (Master Comprehensive Notes)</title>
  <style>
    :root {
      --primary: #c2410c; /* Deep rust/saffron historic tone */
      --primary-dark: #9a3412;
      --primary-light: #fff7ed;
      --secondary: #0f766e; /* Teal */
      --accent: #b45309; /* Warm amber */
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text: #1e293b;
      --text-muted: #64748b;
      --border: #e2e8f0;
      --success: #15803d;
      --danger: #b91c1c;
      --warning: #b45309;
      --info: #0369a1;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04);
      --radius: 12px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.7;
      color: var(--text);
      background-color: var(--bg);
      padding-bottom: 80px;
    }

    #reading-progress-bar {
      position: fixed;
      top: 0;
      left: 0;
      height: 4px;
      width: 0%;
      background: linear-gradient(90deg, #ea580c, #0d9488, #16a34a);
      z-index: 1000;
      transition: width 0.1s ease;
    }

    header {
      background: linear-gradient(135deg, #7c2d12 0%, #9a3412 50%, #c2410c 100%);
      color: white;
      padding: 40px 20px 30px;
      position: relative;
    }

    .container {
      max-width: 1000px;
      margin: 0 auto;
      padding: 0 20px;
    }

    .breadcrumbs {
      display: flex;
      gap: 8px;
      font-size: 0.85rem;
      color: #ffedd5;
      margin-bottom: 15px;
      flex-wrap: wrap;
    }

    .breadcrumbs a {
      color: #fed7aa;
      text-decoration: none;
    }

    .breadcrumbs a:hover {
      text-decoration: underline;
    }

    header h1 {
      font-size: 2.3rem;
      line-height: 1.25;
      margin-bottom: 12px;
      font-weight: 800;
    }

    header p.subtitle {
      font-size: 1.1rem;
      color: #ffedd5;
      max-width: 800px;
      margin-bottom: 20px;
    }

    .meta-badges {
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
    }

    .badge {
      background: rgba(255, 255, 255, 0.18);
      backdrop-filter: blur(4px);
      padding: 5px 14px;
      border-radius: 20px;
      font-size: 0.82rem;
      font-weight: 600;
      letter-spacing: 0.3px;
    }

    /* TTS Audio Bar */
    .audio-bar {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-top: 20px;
      background: rgba(0, 0, 0, 0.2);
      padding: 10px 16px;
      border-radius: 30px;
      width: fit-content;
    }

    .audio-btn {
      background: white;
      color: var(--primary-dark);
      border: none;
      padding: 6px 14px;
      border-radius: 20px;
      font-weight: 700;
      font-size: 0.85rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }

    .audio-btn:hover {
      background: #fed7aa;
      transform: translateY(-1px);
    }

    /* Quick Nav */
    .nav-bar {
      position: sticky;
      top: 4px;
      background: white;
      z-index: 99;
      box-shadow: var(--shadow);
      border-bottom: 1px solid var(--border);
    }

    .nav-tabs {
      display: flex;
      gap: 15px;
      padding: 12px 20px;
      max-width: 1000px;
      margin: 0 auto;
      overflow-x: auto;
      white-space: nowrap;
      scrollbar-width: thin;
    }

    .nav-link {
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 600;
      padding: 6px 14px;
      border-radius: 20px;
      transition: all 0.2s;
    }

    .nav-link:hover, .nav-link.active {
      background: var(--primary-light);
      color: var(--primary);
    }

    main {
      padding: 30px 0;
    }

    section {
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 35px;
      margin-bottom: 30px;
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
    }

    h2 {
      font-size: 1.7rem;
      color: var(--primary-dark);
      margin-bottom: 20px;
      padding-bottom: 10px;
      border-bottom: 2px solid var(--primary-light);
      display: flex;
      align-items: center;
      gap: 10px;
    }

    h3 {
      font-size: 1.25rem;
      color: #334155;
      margin: 25px 0 12px;
    }

    p {
      margin-bottom: 14px;
      color: #334155;
    }

    ul, ol {
      margin-left: 24px;
      margin-bottom: 16px;
      color: #334155;
    }

    li {
      margin-bottom: 6px;
    }

    /* Callout Boxes */
    .callout {
      border-left: 4px solid;
      padding: 16px 20px;
      margin: 20px 0;
      border-radius: 0 var(--radius) var(--radius) 0;
      background: #fafafa;
    }

    .callout-def {
      border-color: #3b82f6;
      background: #eff6ff;
    }

    .callout-act {
      border-color: #10b981;
      background: #f0fdf4;
    }

    .callout-pyq {
      border-color: #8b5cf6;
      background: #f5f3ff;
    }

    .callout-hack {
      border-color: #f59e0b;
      background: #fffbeb;
    }

    .callout-warn {
      border-color: #ef4444;
      background: #fef2f2;
    }

    .callout-title {
      font-weight: 700;
      font-size: 0.95rem;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .callout-def .callout-title { color: #1e40af; }
    .callout-act .callout-title { color: #065f46; }
    .callout-pyq .callout-title { color: #5b21b6; }
    .callout-hack .callout-title { color: #92400e; }
    .callout-warn .callout-title { color: #991b1b; }

    /* SVG Containers */
    .svg-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 20px;
      margin: 25px 0;
      text-align: center;
      box-shadow: 0 2px 4px rgba(0,0,0,0.03);
    }

    .svg-card svg {
      max-width: 100%;
      height: auto;
    }

    .svg-caption {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-top: 10px;
      font-style: italic;
    }

    /* Comparison & Data Tables */
    .table-container {
      overflow-x: auto;
      margin: 20px 0;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.95rem;
    }

    th, td {
      border: 1px solid var(--border);
      padding: 12px 14px;
      text-align: left;
    }

    th {
      background-color: #f8fafc;
      font-weight: 700;
      color: #334155;
    }

    tr:nth-child(even) {
      background-color: #fcfdfe;
    }

    /* Term Bank Grid */
    .term-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 16px;
      margin-top: 20px;
    }

    .term-card {
      background: #ffffff;
      border: 1px solid var(--border);
      padding: 16px;
      border-radius: 10px;
      border-left: 3px solid var(--secondary);
      box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }

    .term-title {
      font-weight: 700;
      color: var(--secondary);
      margin-bottom: 6px;
      font-size: 1rem;
    }

    /* Details Accordion */
    details.ans-box {
      border: 1px solid var(--border);
      border-radius: 8px;
      margin-bottom: 12px;
      background: white;
      overflow: hidden;
      transition: all 0.2s ease;
    }

    details.ans-box[open] {
      border-color: #fdba74;
      box-shadow: 0 2px 5px rgba(234, 88, 12, 0.08);
    }

    summary {
      padding: 14px 18px;
      font-weight: 700;
      color: #1e293b;
      cursor: pointer;
      background: #fafafa;
      user-select: none;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    summary:hover {
      background: #f4f4f5;
    }

    details[open] summary {
      background: var(--primary-light);
      color: var(--primary-dark);
      border-bottom: 1px solid #fed7aa;
    }

    .ans-content {
      padding: 18px;
      background: #ffffff;
      line-height: 1.7;
    }

    /* Quiz Component */
    .quiz-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 20px;
      margin-bottom: 18px;
    }

    .quiz-question {
      font-weight: 700;
      font-size: 1.05rem;
      margin-bottom: 14px;
      color: #0f172a;
    }

    .quiz-options {
      display: flex;
      flex-direction: column;
      gap: 9px;
    }

    .quiz-opt {
      padding: 10px 16px;
      border: 1px solid var(--border);
      border-radius: 8px;
      background: #f8fafc;
      cursor: pointer;
      font-size: 0.95rem;
      text-align: left;
      transition: all 0.2s;
    }

    .quiz-opt:hover {
      background: #f1f5f9;
      border-color: #cbd5e1;
    }

    .quiz-feedback {
      margin-top: 12px;
      padding: 10px 14px;
      border-radius: 6px;
      font-size: 0.9rem;
      display: none;
    }

    .feedback-correct {
      background: #dcfce7;
      color: #14532d;
      border: 1px solid #86efac;
      display: block;
    }

    .feedback-wrong {
      background: #fee2e2;
      color: #7f1d1d;
      border: 1px solid #fca5a5;
      display: block;
    }

    /* Floating Back to Top Button */
    #back-to-top {
      position: fixed;
      bottom: 25px;
      right: 25px;
      background: var(--primary);
      color: white;
      border: none;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      box-shadow: var(--shadow-lg);
      transition: all 0.2s;
      z-index: 999;
    }

    #back-to-top:hover {
      background: var(--primary-dark);
      transform: translateY(-2px);
    }

    @media (max-width: 768px) {
      header { padding: 30px 15px 20px; }
      header h1 { font-size: 1.8rem; }
      section { padding: 20px 15px; }
      .term-grid { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

  <div id="reading-progress-bar"></div>

  <header>
    <div class="container">
      <div class="breadcrumbs">
        <a href="../../index.html">Home</a> &rsaquo;
        <a href="../../index.html#c8_sst">Class 8 Social Science</a> &rsaquo;
        <span>Chapter 9: India's Long Road to Independence</span>
      </div>
      <h1>India's Long Road to Independence</h1>
      <p class="subtitle">From the 1857 Great Rebellion to the midnight dawn of 15 August 1947: A comprehensive study of the constitutional debates, mass satyagrahas, armed revolutionary bravery, Azad Hind Fauj, and the bittersweet triumph of Partition and Swaraj.</p>
      
      <div class="meta-badges">
        <span class="badge">NCERT Code: hees202 (Ch 9 / Part 2 Ch 2)</span>
        <span class="badge">Medium: English Master Notes</span>
        <span class="badge">Grade: 8 Social Science</span>
        <span class="badge">Updated for NEP 2020</span>
      </div>

      <div class="audio-bar">
        <button class="audio-btn" id="tts-play-btn" onclick="toggleAudio()">
          <span id="tts-icon">▶</span> <span id="tts-label">Listen to Chapter Notes</span>
        </button>
        <span style="font-size: 0.8rem; opacity: 0.9;">Voice narration engine for quick revision</span>
      </div>
    </div>
  </header>

  <nav class="nav-bar">
    <div class="nav-tabs">
      <a href="#mindmap" class="nav-link">Mind Map</a>
      <a href="#concepts" class="nav-link">Exhaustive Concepts</a>
      <a href="#terms" class="nav-link">Term Bank</a>
      <a href="#solutions" class="nav-link">NCERT Solutions</a>
      <a href="#quiz" class="nav-link">Interactive Quiz</a>
      <a href="#revision" class="nav-link">Exam Hall Traps & 15 Facts</a>
    </div>
  </nav>

  <main class="container">

    <!-- SECTION 1: MIND MAP -->
    <section id="mindmap">
      <h2>1. Chapter Mind Map & Historical Arc</h2>
      <p>The journey from subjection to sovereignty spanned 90 continuous years (1857&ndash;1947). It was not a single, straight road. Instead, it was an interconnected tapestry of constitutional petitions, grassroots boycotts, fierce armed revolutionary strikes, nationwide mass satyagrahas, and international military diplomacy.</p>

      <div class="svg-card">
        <svg viewBox="0 0 920 340" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="g1" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#ea580c"/>
              <stop offset="50%" stop-color="#f59e0b"/>
              <stop offset="100%" stop-color="#10b981"/>
            </linearGradient>
            <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
              <feDropShadow dx="1" dy="2" stdDeviation="2" flood-opacity="0.15"/>
            </filter>
          </defs>

          <!-- Timeline Axis -->
          <line x1="40" y1="170" x2="880" y2="170" stroke="url(#g1)" stroke-width="6" stroke-linecap="round"/>

          <!-- 1857-1858 Node -->
          <circle cx="70" cy="170" r="14" fill="#ea580c" stroke="#ffffff" stroke-width="3" filter="url(#shadow)"/>
          <rect x="20" y="80" width="105" height="60" rx="8" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5" filter="url(#shadow)"/>
          <text x="72" y="100" font-size="11" font-weight="bold" fill="#9a3412" text-anchor="middle">1857 &ndash; 1858</text>
          <text x="72" y="116" font-size="9" fill="#431407" text-anchor="middle">Great Rebellion &amp;</text>
          <text x="72" y="129" font-size="9" fill="#431407" text-anchor="middle">Crown Takeover</text>

          <!-- 1885 Node -->
          <circle cx="170" cy="170" r="12" fill="#ea580c" stroke="#ffffff" stroke-width="3" filter="url(#shadow)"/>
          <rect x="120" y="200" width="105" height="60" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5" filter="url(#shadow)"/>
          <text x="172" y="220" font-size="11" font-weight="bold" fill="#1e40af" text-anchor="middle">1885: INC Formed</text>
          <text x="172" y="236" font-size="9" fill="#1e3a8a" text-anchor="middle">72 delegates in Bombay</text>
          <text x="172" y="249" font-size="9" fill="#1e3a8a" text-anchor="middle">Moderate Era begins</text>

          <!-- 1905 Node -->
          <circle cx="280" cy="170" r="13" fill="#ea580c" stroke="#ffffff" stroke-width="3" filter="url(#shadow)"/>
          <rect x="230" y="80" width="115" height="65" rx="8" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.5" filter="url(#shadow)"/>
          <text x="287" y="100" font-size="11" font-weight="bold" fill="#b45309" text-anchor="middle">1905: Partition</text>
          <text x="287" y="115" font-size="9" fill="#78350f" text-anchor="middle">Bengal Partitioned</text>
          <text x="287" y="128" font-size="9" fill="#78350f" text-anchor="middle">Swadeshi &amp; Boycott</text>
          <text x="287" y="139" font-size="8.5" fill="#78350f" text-anchor="middle">Tilak: 'Swaraj Birthright'</text>

          <!-- 1919-1922 Node -->
          <circle cx="410" cy="170" r="13" fill="#d97706" stroke="#ffffff" stroke-width="3" filter="url(#shadow)"/>
          <rect x="360" y="200" width="115" height="65" rx="8" fill="#fef2f2" stroke="#ef4444" stroke-width="1.5" filter="url(#shadow)"/>
          <text x="417" y="220" font-size="11" font-weight="bold" fill="#991b1b" text-anchor="middle">1919 &ndash; 1922</text>
          <text x="417" y="235" font-size="9" fill="#7f1d1d" text-anchor="middle">Rowlatt &amp; Jallianwala</text>
          <text x="417" y="248" font-size="9" fill="#7f1d1d" text-anchor="middle">Non-Cooperation &amp;</text>
          <text x="417" y="259" font-size="8.5" fill="#7f1d1d" text-anchor="middle">Khilafat (Chauri Chaura)</text>

          <!-- 1930 Node -->
          <circle cx="540" cy="170" r="13" fill="#d97706" stroke="#ffffff" stroke-width="3" filter="url(#shadow)"/>
          <rect x="490" y="80" width="115" height="65" rx="8" fill="#f0fdf4" stroke="#10b981" stroke-width="1.5" filter="url(#shadow)"/>
          <text x="547" y="100" font-size="11" font-weight="bold" fill="#065f46" text-anchor="middle">1930: Salt March</text>
          <text x="547" y="115" font-size="9" fill="#064e3b" text-anchor="middle">Purna Swaraj (1929)</text>
          <text x="547" y="128" font-size="9" fill="#064e3b" text-anchor="middle">Dandi Salt Yatra</text>
          <text x="547" y="139" font-size="8.5" fill="#064e3b" text-anchor="middle">Civil Disobedience</text>

          <!-- 1942 Node -->
          <circle cx="680" cy="170" r="14" fill="#059669" stroke="#ffffff" stroke-width="3" filter="url(#shadow)"/>
          <rect x="630" y="200" width="115" height="65" rx="8" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5" filter="url(#shadow)"/>
          <text x="687" y="220" font-size="11" font-weight="bold" fill="#9a3412" text-anchor="middle">1942: Quit India</text>
          <text x="687" y="235" font-size="9" fill="#7c2d12" text-anchor="middle">"Do or Die" call</text>
          <text x="687" y="248" font-size="9" fill="#7c2d12" text-anchor="middle">Netaji's INA / Azad Hind</text>
          <text x="687" y="259" font-size="8.5" fill="#7c2d12" text-anchor="middle">"Delhi Chalo!"</text>

          <!-- 1947 Node -->
          <circle cx="820" cy="170" r="16" fill="#10b981" stroke="#ffffff" stroke-width="4" filter="url(#shadow)"/>
          <rect x="765" y="75" width="125" height="70" rx="8" fill="#ecfdf5" stroke="#059669" stroke-width="2" filter="url(#shadow)"/>
          <text x="827" y="96" font-size="11.5" font-weight="bold" fill="#065f46" text-anchor="middle">15 AUGUST 1947</text>
          <text x="827" y="112" font-size="9.5" fill="#047857" text-anchor="middle">Independence &amp; Swaraj</text>
          <text x="827" y="126" font-size="8.5" fill="#b91c1c" text-anchor="middle">Tragedy of Partition</text>
          <text x="827" y="138" font-size="8.5" fill="#064e3b" text-anchor="middle">Radcliffe Line drawn</text>
        </svg>
        <p class="svg-caption">Figure 9.1: The 90-Year Master Timeline of India's Freedom Movement (1857&ndash;1947).</p>
      </div>

      <div class="callout callout-def">
        <div class="callout-title">The Central Historical Question</div>
        <p><em>"How did a land of diverse geographies, multiple languages, and distinct faiths unite to challenge and overthrow nearly two centuries of British imperial rule?"</em> It was achieved through the gradual awakening of national consciousness, economic self-reliance (Swadeshi), non-violent mass defiance (Satyagraha), and the supreme sacrifice of thousands of known and unsung patriots.</p>
      </div>
    </section>

    <!-- SECTION 2: EXHAUSTIVE CONCEPTS -->
    <section id="concepts">
      <h2>2. Exhaustive Conceptual Breakdown</h2>

      <h3>2.1 The Rise of the Indian National Congress (1885)</h3>
      <p>Following the 1857 Revolt, the British Crown took direct control of India under the Government of India Act 1858. However, bureaucratic indifference, high land taxes, press censorship (Vernacular Press Act 1878), and racial arrogance (the Ilbert Bill controversy of 1883) fueled deep resentment among educated Indians.</p>
      <ul>
        <li><strong>Foundation (December 1885):</strong> Formed in Bombay at <em>Gokuldas Tejpal Sanskrit College</em> by 72 educated delegates from across India, facilitated by retired British civil servant <strong>Allan Octavian Hume (A.O. Hume)</strong>.</li>
        <li><strong>First President:</strong> <strong>Womesh Chandra Bonnerjee (W.C. Bonnerjee)</strong>. Prominent pioneers included Dadabhai Naoroji (the "Grand Old Man of India"), Dinshaw Wacha, Pherozeshah Mehta, and Gopal Krishna Gokhale.</li>
        <li><strong>The 'Moderate' Strategy (1885&ndash;1905):</strong> The early Congress believed the British had a sense of justice. They used the <strong>"3 Ps" method: Petitions, Prayers, and Protests</strong>. They demanded Indian representation in the Legislative Councils, holding the Civil Service (ICS) examination simultaneously in India, stopping the "Drain of Wealth", and reducing military expenditures.</li>
      </ul>

      <h3>2.2 The Partition of Bengal &amp; The Swadeshi Movement (1905)</h3>
      <p>In 1905, Viceroy <strong>Lord Curzon</strong> ordered the Partition of Bengal, claiming the province was too large to govern (78 million people). The true motive, however, was political: to weaken Bengal&mdash;the nerve center of Indian nationalism&mdash;by driving a communal wedge between the Muslim-majority East Bengal and Hindu-majority West Bengal.</p>
      
      <div class="callout callout-hack">
        <div class="callout-title">The Three Pillars of the 1905 Agitation</div>
        <ol>
          <li><strong>Swaraj (Self-Rule):</strong> Aiming beyond petty administrative reforms to absolute self-determination. Bal Gangadhar Tilak roared: <em>"Swaraj is my birthright, and I shall have it!"</em></li>
          <li><strong>Swadeshi (Indigenous Goods):</strong> Promoting Indian-made goods&mdash;handloom khadi, indigenous soaps, matchboxes, and indigenous enterprises. J.N. Tata set up the <em>Tata Iron &amp; Steel Company (TISCO)</em> and Swadeshi Mills; Acharya P.C. Ray founded <em>Bengal Chemicals</em>; and V.O. Chidambaram Pillai launched the <em>Swadeshi Steam Navigation Company</em> in Tamil Nadu to challenge British shipping monopolies.</li>
          <li><strong>Boycott:</strong> Refusing to purchase British Manchester cloth, Liverpool salt, foreign cigarettes, and boycotting government schools, titles, and courts. Public bonfires of foreign textiles lit up city squares.</li>
        </ol>
      </div>

      <p>During the anti-partition protests, <strong>Rabindranath Tagore</strong> composed <em>Amar Shonar Bangla</em> and organized the <strong>Raksha Bandhan festival</strong>, where Hindus and Muslims tied yellow threads on each other's wrists as a symbol of unbreakable brotherhood. Bankim Chandra Chattopadhyay's song <strong>Vande Mataram</strong> became the universal anthem of defiance. The immense popular backlash forced the British to <strong>annul the partition in 1911</strong> (shifting the imperial capital from Calcutta to Delhi).</p>

      <h3>2.3 Moderates vs. Nationalists (Surat Split 1907)</h3>
      <p>A deep ideological fracture emerged within the Congress between the <strong>Moderates</strong> (led by G.K. Gokhale and Pherozeshah Mehta, who favored constitutional petitions within the empire) and the <strong>Nationalists / Assertive Extremists</strong> (led by the famous triumvirate <strong>Lal-Bal-Pal</strong>: Lala Lajpat Rai, Bal Gangadhar Tilak, Bipin Chandra Pal, alongside Sri Aurobindo Ghose). The Nationalists argued that freedom could never be won as a gift or "political mendicancy"; it had to be seized through mass agitation and civil resistance.</p>
      <p>At the <strong>Surat Session of 1907</strong>, tensions erupted into a physical confrontation with shoes thrown on the dais, causing the Congress to split. The British seized this opportunity to unleash brutal repression: Tilak was sentenced to six years of hard labor in Mandalay jail (Burma), and Aurobindo Ghose was arrested during the Alipore Bomb Case before later retiring to Pondicherry for spiritual pursuits.</p>

      <div class="svg-card">
        <svg viewBox="0 0 880 280" xmlns="http://www.w3.org/2000/svg">
          <rect x="10" y="10" width="860" height="260" rx="12" fill="#fafafa" stroke="#e2e8f0" stroke-width="2"/>
          <text x="440" y="35" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">Four Complementary Streams of the Indian Freedom Movement</text>

          <!-- Stream 1: Constitutional / Moderates -->
          <rect x="30" y="60" width="190" height="190" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
          <circle cx="125" cy="95" r="22" fill="#dbeafe"/>
          <text x="125" y="102" font-size="20" text-anchor="middle">📜</text>
          <text x="125" y="130" font-size="12" font-weight="bold" fill="#1e40af" text-anchor="middle">Constitutional Reform</text>
          <text x="125" y="150" font-size="9" fill="#1e3a8a" text-anchor="middle">• Moderates (Gokhale, Naoroji)</text>
          <text x="125" y="165" font-size="9" fill="#1e3a8a" text-anchor="middle">• Petitions, legislative debates</text>
          <text x="125" y="180" font-size="9" fill="#1e3a8a" text-anchor="middle">• Exposed British 'Drain of Wealth'</text>
          <text x="125" y="195" font-size="9" fill="#1e3a8a" text-anchor="middle">• Laid administrative groundwork</text>

          <!-- Stream 2: Mass Satyagraha -->
          <rect x="240" y="60" width="190" height="190" rx="10" fill="#f0fdf4" stroke="#10b981" stroke-width="1.5"/>
          <circle cx="335" cy="95" r="22" fill="#d1fae5"/>
          <text x="335" y="102" font-size="20" text-anchor="middle">🕊️</text>
          <text x="335" y="130" font-size="12" font-weight="bold" fill="#065f46" text-anchor="middle">Mass Satyagraha</text>
          <text x="335" y="150" font-size="9" fill="#064e3b" text-anchor="middle">• Mahatma Gandhi, Patel, Nehru</text>
          <text x="335" y="165" font-size="9" fill="#064e3b" text-anchor="middle">• Non-violence (Ahimsa), Truth</text>
          <text x="335" y="180" font-size="9" fill="#064e3b" text-anchor="middle">• Non-Cooperation, Civil Disob.</text>
          <text x="335" y="195" font-size="9" fill="#064e3b" text-anchor="middle">• Millions of peasants &amp; women</text>

          <!-- Stream 3: Armed Revolutionaries -->
          <rect x="450" y="60" width="190" height="190" rx="10" fill="#fff1f2" stroke="#f43f5e" stroke-width="1.5"/>
          <circle cx="545" cy="95" r="22" fill="#ffe4e6"/>
          <text x="545" y="102" font-size="20" text-anchor="middle">⚡</text>
          <text x="545" y="130" font-size="12" font-weight="bold" fill="#9f1239" text-anchor="middle">Revolutionary Patriots</text>
          <text x="545" y="150" font-size="9" fill="#881337" text-anchor="middle">• Bhagat Singh, Azad, Bismil</text>
          <text x="545" y="165" font-size="9" fill="#881337" text-anchor="middle">• Bagha Jatin, Surya Sen, Bose</text>
          <text x="545" y="180" font-size="9" fill="#881337" text-anchor="middle">• HRA/HSRA, Anushilan Samiti</text>
          <text x="545" y="195" font-size="9" fill="#881337" text-anchor="middle">• Fearless sacrifice &amp; defiance</text>

          <!-- Stream 4: Azad Hind Fauj (INA) -->
          <rect x="660" y="60" width="190" height="190" rx="10" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.5"/>
          <circle cx="755" cy="95" r="22" fill="#fef3c7"/>
          <text x="755" y="102" font-size="20" text-anchor="middle">⚔️</text>
          <text x="755" y="130" font-size="12" font-weight="bold" fill="#92400e" text-anchor="middle">Armed Liberation (INA)</text>
          <text x="755" y="150" font-size="9" fill="#78350f" text-anchor="middle">• Netaji Subhas Chandra Bose</text>
          <text x="755" y="165" font-size="9" fill="#78350f" text-anchor="middle">• Rash Behari Bose, Mohan Singh</text>
          <text x="755" y="180" font-size="9" fill="#78350f" text-anchor="middle">• All-women Rani Jhansi Regt.</text>
          <text x="755" y="195" font-size="9" fill="#78350f" text-anchor="middle">• Shook British military loyalty</text>
        </svg>
        <p class="svg-caption">Figure 9.2: The multi-faceted convergence of methods that unseated British colonial rule.</p>
      </div>

      <h3>2.4 Fearless Sacrifices: The Revolutionary Movement</h3>
      <p>Young men and women who believed that constitutional prayers would never dislodge an armed occupying power formed secret societies dedicated to armed insurrection:</p>
      <ul>
        <li><strong>Anushilan Samiti (1902) &amp; Abhinav Bharat (1904):</strong> Pioneered by Pramathanath Mitra, Aurobindo Ghose, Barindra Ghosh, and the Savarkar brothers (Vinayak &amp; Ganesh).</li>
        <li><strong>Khudiram Bose (1908):</strong> At just 18 years of age, Khudiram and Prafulla Chaki attempted to assassinate the oppressive magistrate Kingsford at Muzaffarpur. Khudiram went to the gallows smiling, becoming a legendary folk hero.</li>
        <li><strong>Bagha Jatin (Jatindranath Mukherjee):</strong> Leader of the Yugantar party who earned his moniker after wrestling a royal Bengal tiger barehanded. In September 1915, while awaiting German arms at Balasore (Odisha) to orchestrate an all-India rebellion, he died in an epic gunfight against heavily armed colonial forces at the banks of the Burhi Balam river.</li>
        <li><strong>Rash Behari Bose:</strong> Masterminded the Delhi Bomb attempt on Viceroy Lord Hardinge in 1912. Evading a massive British manhunt, he fled disguised to Japan, where he mobilized international support and later established the Indian Independence League and laid the foundation of the INA.</li>
        <li><strong>Hindustan Socialist Republican Association (HSRA):</strong> Founded by Ram Prasad Bismil, Ashfaqullah Khan, and Chandrashekhar Azad (famous for the 1925 <em>Kakori Train Action</em> to fund weapons). Later revitalized by <strong>Bhagat Singh</strong> and <strong>Sukhdev</strong>, who assassinated British officer Saunders in 1928 to avenge the fatal lathi beating of Lala Lajpat Rai. In April 1929, Bhagat Singh and Batukeshwar Dutt threw smoke bombs and leaflets inside the Central Legislative Assembly in Delhi shouting <em>"Inquilab Zindabad!"</em> to "make the deaf hear." Bhagat Singh, Rajguru, and Sukhdev were hanged on 23 March 1931.</li>
        <li><strong>Surya Sen ("Master Da") &amp; Pritilata Waddedar:</strong> Led the famous 1930 <em>Chittagong Armoury Raid</em> in Bengal. Pritilata led an armed assault on the Pahartali European Club (which had a racist board: "Dogs and Indians not allowed"), sacrificing her life by consuming potassium cyanide to avoid capture.</li>
      </ul>

      <h3>2.5 Mahatma Gandhi and the Mass Movements</h3>
      <p>Returning from South Africa in January 1915, <strong>Mohandas Karamchand Gandhi</strong> transformed Indian politics by introducing <strong>Satyagraha</strong> (insistence on truth through non-violent resistance) and <strong>Ahimsa</strong>. After touring India on the advice of his political guru Gopal Krishna Gokhale, he led three local struggles that tested his techniques:</p>
      <ol>
        <li><strong>Champaran (1917, Bihar):</strong> Against oppressive European planters who forced peasants into the exploitative <em>Tinkathia</em> system (cultivating indigo on 3/20th of their land).</li>
        <li><strong>Kheda (1918, Gujarat):</strong> Demanded revenue remission for farmers hit by severe crop failure and plague, working closely with <strong>Vallabhbhai Patel</strong>.</li>
        <li><strong>Ahmedabad (1918, Gujarat):</strong> Led textile mill workers on strike for a 35% wage hike and undertook his first hunger strike in India.</li>
      </ol>

      <div class="callout callout-warn">
        <div class="callout-title">The Rowlatt Act &amp; Jallianwala Bagh Massacre (1919)</div>
        <p>The draconian <strong>Anarchical and Revolutionary Crimes Act of 1919 (Rowlatt Act)</strong> allowed the British police to arrest any Indian without warrant and detain them for up to two years without trial ("No Dalil, No Vakil, No Appeal"). Gandhi called for a nationwide <em>hartal</em>.</p>
        <p>On <strong>13 April 1919 (Baisakhi Day)</strong>, thousands of peaceful men, women, and children gathered at <strong>Jallianwala Bagh</strong> in Amritsar to protest the arrest of leaders Dr. Saifuddin Kitchlew and Dr. Satyapal. <strong>Brigadier-General Reginald Dyer</strong> blocked the single narrow exit with troops and ordered firing without warning. Over 1,650 rounds were shot; hundreds were massacred in cold blood and thousands wounded. In profound grief and protest, <strong>Rabindranath Tagore renounced his British Knighthood</strong>. Decades later in 1940, revolutionary <strong>Udham Singh</strong> assassinated Michael O'Dwyer (the Lt. Governor of Punjab who approved the massacre) in London.</p>
      </div>

      <h3>2.6 The Non-Cooperation Movement (1920&ndash;1922)</h3>
      <p>Launched at the Nagpur Congress Session (December 1920), Gandhi combined the nationalist demand for Swaraj with the Muslim community's <strong>Khilafat Movement</strong> (led by the Ali brothers, Maulana Mohammad Ali and Shaukat Ali, protesting the harsh British dismemberment of the Ottoman Caliphate). This forged unprecedented Hindu-Muslim unity.</p>
      <ul>
        <li><strong>Tactics:</strong> Surrender of titles and honorary offices, boycott of foreign cloth, boycott of courts by lawyers (like Motilal Nehru, C.R. Das), boycott of government schools and colleges, and spinning khadi on charkhas.</li>
        <li><strong>Sudden Withdrawal (Chauri Chaura, 1922):</strong> On 5 February 1922, an angry mob at Chauri Chaura (Gorakhpur, UP) clashed with police and set the police station on fire, killing 22 policemen inside. Devastated that the movement had degenerated into violence, Gandhi immediately suspended the Non-Cooperation Movement, stating that India was not yet spiritually disciplined for pure non-violence.</li>
      </ul>

      <h3>2.7 The Salt March &amp; Civil Disobedience Movement (1930)</h3>
      <p>At the <strong>Lahore Session of 1929</strong>, presided over by young <strong>Jawaharlal Nehru</strong>, the Congress adopted the historic resolution demanding <strong>Purna Swaraj</strong> (Complete Independence) and hoisted the Tricolour on the banks of the Ravi River. <strong>26 January 1930</strong> was celebrated nationwide as Independence Day.</p>
      <p>To launch Civil Disobedience, Gandhi chose an ingenious weapon: <strong>Salt</strong>. Salt was a basic daily human necessity, yet the British imposed an oppressive monopoly and tax on it, affecting every rich and poor citizen equally.</p>

      <div class="svg-card">
        <svg viewBox="0 0 880 260" xmlns="http://www.w3.org/2000/svg">
          <rect x="10" y="10" width="860" height="240" rx="12" fill="#fffbeb" stroke="#fcd34d" stroke-width="2"/>
          <text x="440" y="38" font-size="16" font-weight="bold" fill="#78350f" text-anchor="middle">The Historic Dandi March (12 March &ndash; 6 April 1930)</text>

          <!-- Sabarmati Ashram -->
          <circle cx="100" cy="130" r="30" fill="#ea580c"/>
          <text x="100" y="136" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Sabarmati</text>
          <text x="100" y="175" font-size="10" font-weight="bold" fill="#7c2d12" text-anchor="middle">Ahmedabad</text>
          <text x="100" y="190" font-size="9" fill="#431407" text-anchor="middle">12 March 1930</text>
          <text x="100" y="202" font-size="8.5" fill="#431407" text-anchor="middle">78 trusted volunteers</text>

          <!-- Path -->
          <path d="M 130 130 Q 300 90, 440 130 T 750 130" fill="none" stroke="#ea580c" stroke-width="4" stroke-dasharray="6,6"/>
          
          <!-- Midpoint Stats -->
          <rect x="360" y="70" width="160" height="45" rx="8" fill="#ffffff" stroke="#f59e0b" stroke-width="1.5"/>
          <text x="440" y="88" font-size="10" font-weight="bold" fill="#92400e" text-anchor="middle">240 Miles (385 km)</text>
          <text x="440" y="103" font-size="9" fill="#78350f" text-anchor="middle">24 Days on Foot across Gujarat</text>

          <!-- Dandi Coast -->
          <circle cx="780" cy="130" r="32" fill="#0d9488"/>
          <text x="780" y="136" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Dandi</text>
          <text x="780" y="175" font-size="10" font-weight="bold" fill="#134e4a" text-anchor="middle">Arabian Sea Coast</text>
          <text x="780" y="190" font-size="9" fill="#042f2e" text-anchor="middle">6 April 1930</text>
          <text x="780" y="203" font-size="8.5" fill="#042f2e" text-anchor="middle">Lifting a lump of natural salt</text>
          <text x="780" y="215" font-size="8.5" fill="#042f2e" text-anchor="middle">British Salt Law Broken!</text>
        </svg>
        <p class="svg-caption">Figure 9.3: The Salt March route that electrified millions and shattered British legal legitimacy.</p>
      </div>

      <p>The defiance spread like wildfire: in the North-West Frontier Province, <strong>Khan Abdul Ghaffar Khan ("Frontier Gandhi")</strong> led his non-violent brigade, the <em>Khudai Khidmatgars ("Red Shirts")</em>; in Tamil Nadu, <strong>C. Rajagopalachari</strong> led the Vedaranyam Salt March; in Odisha, thousands boiled seawater at Inchudi (Balasore); and at Dharasana, <strong>Sarojini Naidu</strong> led thousands of volunteers who absorbed brutal steel-tipped lathi charges without lifting a hand in retaliation.</p>

      <h3>2.8 Dr. B.R. Ambedkar and the Poona Pact (1932)</h3>
      <p>At the Second Round Table Conference in London (1931), <strong>Dr. Bhimrao Ramji Ambedkar</strong> strongly championed the rights of the Depressed Classes (Dalits), demanding separate electorates so they could elect their own representatives free from caste-elite domination. In 1932, the British announced the <strong>Communal Award</strong> granting separate electorates to Dalits.</p>
      <p>Gandhi, imprisoned in Yerwada Jail (Pune), opposed separate electorates, believing it would permanently divide Hindu society and freeze caste divisions forever. He undertook a fast-unto-death. To save Gandhi's life and preserve national unity, Dr. Ambedkar held intense negotiations, resulting in the historic <strong>Poona Pact (September 1932)</strong>: separate electorates were abandoned in favor of <strong>reserved seats</strong> for Dalits within the general electorate, with their representation increased from 71 to 148 seats.</p>

      <h3>2.9 Netaji Subhas Chandra Bose and the Azad Hind Fauj (INA)</h3>
      <p>Elected Congress President in 1938 and 1939, <strong>Subhas Chandra Bose</strong> clashed with Gandhi over strategy, believing that Britain's crisis in World War II should be leveraged through international alliances and armed force. He resigned and formed the <em>Forward Bloc</em>.</p>
      <ul>
        <li><strong>Great Escape (1941):</strong> Placed under house arrest in Calcutta, Bose escaped disguised as an Afghan traveler named Ziauddin, traveling through Peshawar, Kabul, and Moscow to Berlin.</li>
        <li><strong>The INA Campaign:</strong> In 1943, Netaji arrived in Singapore by submarine. He took charge of the <strong>Azad Hind Fauj (Indian National Army)</strong> formed earlier by <strong>General Mohan Singh</strong> and <strong>Rash Behari Bose</strong> from Indian prisoners of war captured by the Japanese.</li>
        <li><strong>Provisional Government of Free India:</strong> Netaji gave electrifying battle cries: <em>"Delhi Chalo!"</em>, <em>"Jai Hind!"</em>, and <em>"Give me blood, and I will give you freedom!"</em> He established the <strong>Rani of Jhansi Regiment</strong>, one of Asia's first all-female combat regiments, commanded by <strong>Captain Lakshmi Sahgal</strong>.</li>
        <li><strong>Military &amp; Political Impact:</strong> Though the INA's advance was halted at Kohima and Imphal due to monsoons and supply collapses, the post-war <strong>Red Fort INA Trials (1945&ndash;1946)</strong> triggered widespread mutinies among Indian soldiers, culminating in the <strong>Royal Indian Navy (RIN) Mutiny of February 1946</strong> in Bombay. This proved to the British that their armed hold on India had completely unraveled.</li>
      </ul>

      <h3>2.10 The Quit India Movement (1942) &amp; The Road to Partition</h3>
      <p>Following the collapse of the <strong>Cripps Mission</strong> (which offered vague dominion status only after the war, famously dubbed by Gandhi as "a post-dated cheque on a crashing bank"), Gandhi launched the <strong>Quit India Movement</strong> on <strong>8 August 1942</strong> at Gowalia Tank Maidan in Bombay with the clarion call: <strong>"Do or Die" (Karo ya Maro)</strong>.</p>
      <p>Within 24 hours, the British arrested Gandhi, Nehru, Patel, and all top leaders. Instead of dying out, the movement became a massive leaderless rebellion: <strong>Aruna Asaf Ali</strong> hoisted the Tricolour at Gowalia Tank; young <strong>Usha Mehta</strong> ran an underground secret radio transmitter; peasants established parallel governments (<em>Prati Sarkar</em> led by Nana Patil in Satara, and Tamluk National Government in Bengal where 73-year-old <strong>Matangini Hazra</strong> was shot dead while holding the flag aloft).</p>

      <h3>2.11 Partition, Turmoil, and the Dawn of Independence</h3>
      <p>As World War II ended, a weakened Britain decided to withdraw. However, the political rift deepened: <strong>Muhammad Ali Jinnah</strong> and the <strong>Muslim League</strong> insisted on the <em>Two-Nation Theory</em>, demanding a separate sovereign state of Pakistan. The tragic <strong>Direct Action Day</strong> (16 August 1946) launched by the League led to horrific communal bloodshed in Calcutta and Noakhali.</p>
      <p>The <strong>Mountbatten Plan</strong> (June 3, 1947) decided to divide British India into two independent dominions: <strong>India and Pakistan</strong>. A British barrister, <strong>Sir Cyril Radcliffe</strong>, who had never visited India before, was given a meager five weeks to draw the international borders (the Radcliffe Line) slicing through Punjab and Bengal. On <strong>15 August 1947</strong>, India won its independence. While Delhi rejoiced to Jawaharlal Nehru's stirring <em>"Tryst with Destiny"</em> speech, millions of refugees crossed burning borders amidst catastrophic violence, and Mahatma Gandhi spent Independence Day in Calcutta fasting to quell communal riots.</p>
    </section>

    <!-- SECTION 3: TERM BANK -->
    <section id="terms">
      <h2>3. Comprehensive Term Bank (20 Essential Concepts)</h2>
      <div class="term-grid">
        <div class="term-card">
          <div class="term-title">1. Swaraj</div>
          <p>Self-rule and absolute autonomy from foreign rule; popularized by Bal Gangadhar Tilak and Sri Aurobindo as an inalienable birthright.</p>
        </div>
        <div class="term-card">
          <div class="term-title">2. Swadeshi</div>
          <p>The practice of using indigenous, locally manufactured goods (like khadi) while systematically rejecting foreign imports to achieve economic self-reliance.</p>
        </div>
        <div class="term-card">
          <div class="term-title">3. Boycott</div>
          <p>Organized collective refusal to purchase British goods, attend British schools, practice in colonial courts, or accept government titles.</p>
        </div>
        <div class="term-card">
          <div class="term-title">4. Satyagraha</div>
          <p>Gandhi's philosophy of non-violent resistance; literally "insistence on truth" (Satya = Truth, Agraha = Firm insistence) through moral force.</p>
        </div>
        <div class="term-card">
          <div class="term-title">5. Ahimsa</div>
          <p>The cardinal principle of complete non-violence in thought, word, and deed, ensuring no harm is caused even to the oppressor.</p>
        </div>
        <div class="term-card">
          <div class="term-title">6. Drain of Wealth</div>
          <p>Dadabhai Naoroji's economic thesis explaining how India's wealth, raw materials, and tax revenues were systematically extracted to enrich Britain without any economic return.</p>
        </div>
        <div class="term-card">
          <div class="term-title">7. Rowlatt Act (1919)</div>
          <p>Imperial law granting arbitrary police powers to arrest and imprison political suspects for two years without trial, legal defense, or appeal.</p>
        </div>
        <div class="term-card">
          <div class="term-title">8. Khilafat Movement</div>
          <p>Pan-Islamic campaign led by the Ali brothers in 1919&ndash;1920 to protect the Caliphate in Ottoman Turkey, linked with Non-Cooperation by Gandhi for communal unity.</p>
        </div>
        <div class="term-card">
          <div class="term-title">9. Purna Swaraj</div>
          <p>Resolution adopted at the 1929 Lahore Congress Session demanding "Complete Independence" and ending any association with the British Empire.</p>
        </div>
        <div class="term-card">
          <div class="term-title">10. Dandi March</div>
          <p>The 240-mile trek led by Gandhi from Sabarmati to Dandi (March&ndash;April 1930) to produce illegal salt and kick off nationwide Civil Disobedience.</p>
        </div>
        <div class="term-card">
          <div class="term-title">11. Khudai Khidmatgars</div>
          <p>"Servants of God" or "Red Shirts"&mdash;a non-violent Pashtun army of freedom fighters raised by Khan Abdul Ghaffar Khan in the NWFP.</p>
        </div>
        <div class="term-card">
          <div class="term-title">12. Poona Pact (1932)</div>
          <p>Agreement between Dr. B.R. Ambedkar and Mahatma Gandhi replacing separate electorates for Dalits with reserved seats in joint electorates.</p>
        </div>
        <div class="term-card">
          <div class="term-title">13. HSRA</div>
          <p>Hindustan Socialist Republican Association; a revolutionary anti-imperialist body led by Chandrashekhar Azad, Bhagat Singh, and Sukhdev.</p>
        </div>
        <div class="term-card">
          <div class="term-title">14. Azad Hind Fauj (INA)</div>
          <p>The Indian National Army revived by Netaji Subhas Chandra Bose in Singapore to liberate India through military confrontation alongside Axis forces.</p>
        </div>
        <div class="term-card">
          <div class="term-title">15. Rani of Jhansi Regiment</div>
          <p>The pioneer all-women armed combat unit of the INA commanded by Captain Lakshmi Sahgal, fighting on the Burma front.</p>
        </div>
        <div class="term-card">
          <div class="term-title">16. Quit India Movement</div>
          <p>The mass August Kranti launched in 1942 where Gandhi delivered the "Do or Die" call demanding immediate British evacuation of India.</p>
        </div>
        <div class="term-card">
          <div class="term-title">17. Radcliffe Line</div>
          <p>The arbitrary boundary line drawn in five weeks by British lawyer Sir Cyril Radcliffe dividing Punjab and Bengal between India and Pakistan.</p>
        </div>
        <div class="term-card">
          <div class="term-title">18. Prati Sarkar</div>
          <p>Parallel independent underground government set up by local freedom fighters in Satara (Maharashtra) led by Krantisinha Nana Patil during Quit India.</p>
        </div>
        <div class="term-card">
          <div class="term-title">19. Royal Indian Navy (RIN) Mutiny</div>
          <p>February 1946 strike by ratings of HMIS Talwar in Bombay that spread to 78 ships, demonstrating that British armed control had collapsed.</p>
        </div>
        <div class="term-card">
          <div class="term-title">20. Tryst with Destiny</div>
          <p>Historic speech delivered by Jawaharlal Nehru on the midnight of 14&ndash;15 August 1947 marking India's rebirth as an independent democratic nation.</p>
        </div>
      </div>
    </section>

    <!-- SECTION 4: NCERT SOLUTIONS -->
    <section id="solutions">
      <h2>4. Complete NCERT Textbook Solutions &amp; Classroom Activities</h2>

      <h3>Part A: True or False (With Complete Historical Explanations)</h3>

      <details class="ans-box">
        <summary>Q1. Right from its inception, the Indian National Congress called for India's independence.</summary>
        <div class="ans-content">
          <p><strong>Answer: False.</strong></p>
          <p><strong>Explanation:</strong> In its initial years (1885&ndash;1905), the Congress was led by Moderates who did not demand complete independence. Instead, they asked for constitutional reforms, greater Indian representation in Legislative Councils, administrative opportunities, and reduction in military taxes while affirming loyalty to the British Crown. The call for absolute independence (<em>Purna Swaraj</em>) was formally adopted much later at the Lahore Session in December 1929.</p>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q2. Bal Gangadhar Tilak turned a Shivaji festival into a popular event.</summary>
        <div class="ans-content">
          <p><strong>Answer: True.</strong></p>
          <p><strong>Explanation:</strong> Tilak transformed the traditional Ganesh Chaturthi and Shivaji Utsav (Shivaji Festival) into grand public celebrations. He used these festivals as public platforms to build national pride, awaken political consciousness, and unite ordinary citizens against colonial rule across caste barriers.</p>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q3. The Ghadar Movement of 1914–15 aimed to start a mutiny within the British Indian Army while British troops were busy with World War I.</summary>
        <div class="ans-content">
          <p><strong>Answer: True.</strong></p>
          <p><strong>Explanation:</strong> Formed in North America by expatriate Indians (including Lala Har Dayal, Sohan Singh Bhakna, and Kartar Singh Sarabha), the Ghadar Party sought to exploit Britain's vulnerability during World War I. Thousands returned to India in 1914&ndash;1915 to organize an armed mutiny within the British Indian Army regiments, though it was betrayed by internal spies and ruthlessly crushed.</p>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q4. Vallabhbhai Patel earned the title 'Sardar' for his leadership during the Satyagraha agitation in Gujarat.</summary>
        <div class="ans-content">
          <p><strong>Answer: True.</strong></p>
          <p><strong>Explanation:</strong> Vallabhbhai Patel earned the beloved title of <strong>'Sardar' (Chief / Leader)</strong> from the women of Bardoli during the heroic <strong>Bardoli Satyagraha of 1928</strong> in Gujarat, where he successfully led peasants in refusing to pay an unjust 22% land tax hike.</p>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q5. The Kakori train robbery of 1925 was carried out to fund the activities of the Hindustan Republican Association.</summary>
        <div class="ans-content">
          <p><strong>Answer: True.</strong></p>
          <p><strong>Explanation:</strong> On 9 August 1925, members of the Hindustan Republican Association (HRA)&mdash;including Ram Prasad Bismil, Ashfaqullah Khan, Chandrashekhar Azad, and Rajendra Lahiri&mdash;halted the 8-Down train near Kakori (Lucknow) and seized government treasury funds to purchase weapons and sustain their underground revolutionary activities.</p>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q6. The 'Do or Die' call was given by Mahatma Gandhi during the Non-Cooperation Movement in 1920.</summary>
        <div class="ans-content">
          <p><strong>Answer: False.</strong></p>
          <p><strong>Explanation:</strong> The famous slogan <strong>'Do or Die' (Karo ya Maro)</strong> was delivered by Mahatma Gandhi during the <strong>Quit India Movement on 8 August 1942</strong> at Gowalia Tank Maidan in Bombay, not during the 1920 Non-Cooperation Movement.</p>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q7. B.R. Ambedkar and Gandhi were in total agreement regarding the issue of 'separate electorates' for Dalits.</summary>
        <div class="ans-content">
          <p><strong>Answer: False.</strong></p>
          <p><strong>Explanation:</strong> They had deep ideological disagreements. Dr. Ambedkar insisted on separate electorates to ensure authentic Dalit political representation free from high-caste dominance. Gandhi vehemently opposed separate electorates, fearing it would permanently fracture Hindu society, and undertook a fast-unto-death in Yerwada Jail. The dispute was finally resolved through compromise in the <strong>Poona Pact (1932)</strong>, which provided reserved seats within joint electorates.</p>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q8. Sir Stafford Cripps was sent to India in 1942 because Winston Churchill supported immediate independence for India.</summary>
        <div class="ans-content">
          <p><strong>Answer: False.</strong></p>
          <p><strong>Explanation:</strong> British Prime Minister Winston Churchill was a staunch imperialist who strongly opposed Indian independence. Cripps was sent in 1942 only under severe military pressure from US President Franklin D. Roosevelt and Chinese leader Chiang Kai-shek, and because Japanese forces had captured Rangoon and were threatening India's borders. Cripps offered only vague dominion status after the war, which Indian leaders rejected.</p>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q9. Subhas Chandra Bose raised an army during his stay in Germany.</summary>
        <div class="ans-content">
          <p><strong>Answer: True.</strong></p>
          <p><strong>Explanation:</strong> In Germany (1941&ndash;1943), Bose established the <em>Free India Centre</em> in Berlin and raised the <strong>Indian Legion (Tiger Legion / Indische Legion)</strong> consisting of approximately 3,000 Indian prisoners of war captured in North Africa, before traveling by submarine to Southeast Asia to take charge of the INA.</p>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q10. The Radcliffe Line, which divided India and Pakistan, was announced a few weeks before Independence Day.</summary>
        <div class="ans-content">
          <p><strong>Answer: False.</strong></p>
          <p><strong>Explanation:</strong> The Radcliffe Line boundary award was deliberately kept secret and only published on <strong>17 August 1947&mdash;two days AFTER Independence Day</strong>. This delay created immense confusion and chaos among millions of citizens who celebrated independence without knowing which country their hometowns fell into.</p>
        </div>
      </details>

      <h3>Part B: "Who Am I?" Historical Identification</h3>

      <details class="ans-box">
        <summary>1. Known as the 'Lion of Punjab', I was severely injured during a brutal lathi charge while protesting against the Simon Commission.</summary>
        <div class="ans-content">
          <p><strong>Answer: Lala Lajpat Rai (Punjab Kesari).</strong></p>
          <p>He famously declared after the assault: <em>"The blows struck at me today will be the last nails in the coffin of British rule in India."</em> He succumbed to his injuries on 17 November 1928.</p>
        </div>
      </details>

      <details class="ans-box">
        <summary>2. I famously declared, 'Swaraj is my birthright, and I shall have it!' I used the Kesari newspaper and festivals like Ganesh Chaturthi to unite people against British rule.</summary>
        <div class="ans-content">
          <p><strong>Answer: Bal Gangadhar Tilak ("Lokmanya" Tilak).</strong></p>
        </div>
      </details>

      <details class="ans-box">
        <summary>3. I was a leader of the Nationalist faction of the Congress. In the daily Bande Mataram, I wrote on the need for India to attain absolute autonomy.</summary>
        <div class="ans-content">
          <p><strong>Answer: Sri Aurobindo Ghose.</strong></p>
        </div>
      </details>

      <details class="ans-box">
        <summary>4. I earned my nickname 'Bagha' after wrestling a tiger with my bare hands. I was a revolutionary leader who died in a gunfight while waiting for a shipment of German arms to start an uprising.</summary>
        <div class="ans-content">
          <p><strong>Answer: Jatindranath Mukherjee (Bagha Jatin).</strong></p>
          <p>He died heroically in September 1915 during the battle of Burhi Balam at Balasore (Odisha).</p>
        </div>
      </details>

      <details class="ans-box">
        <summary>5. I organised the daring attempt to throw a bomb at the Viceroy in 1912. I later escaped to Japan, where I spent years working to organise a movement from there.</summary>
        <div class="ans-content">
          <p><strong>Answer: Rash Behari Bose.</strong></p>
        </div>
      </details>

      <details class="ans-box">
        <summary>6. I was martyred at a young age after an attempt on the life of a British judge.</summary>
        <div class="ans-content">
          <p><strong>Answer: Khudiram Bose.</strong></p>
          <p>Martyred on 11 August 1908 at the age of 18 for the Muzaffarpur bomb incident.</p>
        </div>
      </details>

      <details class="ans-box">
        <summary>7. I was martyred at a young age after throwing non-lethal bombs in Delhi's Central Legislative Assembly.</summary>
        <div class="ans-content">
          <p><strong>Answer: Bhagat Singh.</strong></p>
          <p>Executed on 23 March 1931 alongside Rajguru and Sukhdev in Lahore Central Jail.</p>
        </div>
      </details>

      <details class="ans-box">
        <summary>8. I turned the freedom struggle into a mass movement through the principles of ahimsa and satyagraha, leading campaigns such as the Dandi March.</summary>
        <div class="ans-content">
          <p><strong>Answer: Mahatma Mohandas Karamchand Gandhi.</strong></p>
        </div>
      </details>

      <details class="ans-box">
        <summary>9. I sought help from the Axis powers during World War II to organise the Indian National Army.</summary>
        <div class="ans-content">
          <p><strong>Answer: Netaji Subhas Chandra Bose.</strong></p>
        </div>
      </details>

      <details class="ans-box">
        <summary>10. A British lawyer, I was given just five weeks to draw the boundary line that would partition the Indian subcontinent into two separate nations.</summary>
        <div class="ans-content">
          <p><strong>Answer: Sir Cyril Radcliffe.</strong></p>
        </div>
      </details>

      <h3>Part C: In-Depth Analytical &amp; Classroom Inquiry Questions</h3>

      <details class="ans-box">
        <summary>Q3. What kinds of sacrifices are needed to achieve freedom? What comforts would you give up for a cause you believe in?</summary>
        <div class="ans-content">
          <p><strong>Teacher-Crafted Model Answer:</strong></p>
          <ul>
            <li><strong>Forms of Sacrifice in India's Freedom Movement:</strong>
              <ol>
                <li><strong>Loss of Life and Youth:</strong> Revolutionaries like Bhagat Singh, Khudiram Bose, and Kartar Singh Sarabha mounted the gallows in their teens and twenties, sacrificing their entire future.</li>
                <li><strong>Economic Ruin &amp; Confiscation:</strong> Peasants during the Kheda and Bardoli satyagrahas suffered confiscation of their lands, cattle, and household utensils for refusing to pay colonial taxes.</li>
                <li><strong>Long Prison Sentences &amp; Separation:</strong> Leaders like Tilak, Gandhi, and Nehru spent years behind bars. Tilak wrote <em>Gita Rahasya</em> in dark cells in Mandalay, while Nehru missed watching his daughter grow up.</li>
                <li><strong>Bodily Harm:</strong> Thousands suffered brutal fractures in police lathi charges (such as Sarojini Naidu's volunteers at Dharasana and Lala Lajpat Rai at Lahore).</li>
                <li><strong>Women's Courage:</strong> Women like Kasturba Gandhi, Usha Mehta, and Matangini Hazra faced bullets, police beatings, and jail while keeping families resilient.</li>
              </ol>
            </li>
            <li><strong>Personal Reflection for Students:</strong> Standing up for justice today requires giving up personal convenience, overcoming peer pressure, sacrificing screen time to serve community needs, and standing firmly with vulnerable classmates when unfairness occurs.</li>
          </ul>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q4. What values does Tilak's statement, "Swaraj is my birthright and I shall have it," reflect? Can these values be meaningful for young people today?</summary>
        <div class="ans-content">
          <p><strong>Values Reflected in Tilak's Statement:</strong></p>
          <ol>
            <li><strong>Inherent Human Dignity:</strong> Liberty and self-rule are not benevolent gifts granted by a colonial master, but fundamental natural rights possessed from birth.</li>
            <li><strong>Fearlessness and Determination:</strong> The phrase <em>"I shall have it"</em> displays resolute willpower, rejecting defeatism and submissiveness.</li>
            <li><strong>Self-Reliance:</strong> It urges citizens to stop petitioning for favors and instead organize their own internal strength.</li>
          </ol>
          <p><strong>Relevance for Today's Youth:</strong> For contemporary students, "Swaraj" represents intellectual autonomy&mdash;freeing one's mind from misinformation, prejudice, and digital addictions. It means taking responsibility for one's own education, community environment, and moral choices.</p>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q5. How did peasants, workers, tribals, and students contribute to the national movement differently from political leaders?</summary>
        <div class="ans-content">
          <p>While political leaders debated policies and drafted manifestos, the grassroots backbone of the movement was built by ordinary citizens:</p>
          <table>
            <thead>
              <tr>
                <th>Group</th>
                <th>Distinct Contribution to Freedom Movement</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Peasants</strong></td>
                <td>Refused to pay illegal cesses and land rents (Kheda, Bardoli, Champaran). In Awadh, Baba Ramchandra organized the <em>Kisan Sabha</em>; in Bihar, Swami Sahajanand mobilized millions against landlord exploitation.</td>
              </tr>
              <tr>
                <td><strong>Industrial Workers</strong></td>
                <td>Conducted massive strikes halting British transport and factories: railway strikes, textile strikes in Bombay and Ahmedabad, and postal strikes shutting down imperial logistics.</td>
              </tr>
              <tr>
                <td><strong>Tribal Communities</strong></td>
                <td>Fought guerrilla warfare to reclaim forest rights taken away by British colonial forest laws (e.g., Alluri Sitarama Raju in the Rampa rebellion of Andhra, Birsa Munda in Chhota Nagpur, and Lakshman Nayak in Koraput, Odisha).</td>
              </tr>
              <tr>
                <td><strong>Students</strong></td>
                <td>Walked out of government colleges and British schools; distributed underground nationalist newspapers; picketed liquor and foreign cloth shops; and served as the courier network during the Quit India Movement.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q6. Discuss Nehru's 'Tryst with Destiny' speech: What is meant by "redeem our pledge"? How would you define the 'soul of a nation'?</summary>
        <div class="ans-content">
          <p><strong>1. "Redeem our pledge":</strong></p>
          <p>At the Lahore Congress of 1929, Indians took a sacred pledge on 26 January 1930 that subjection to British rule was a crime against humanity and that they would not rest until complete independence (<em>Purna Swaraj</em>) was achieved. On 15 August 1947, Nehru stated that the nation was now fulfilling ("redeeming") that sacred promise.</p>
          <p><strong>2. The 'Soul of a nation':</strong></p>
          <p>The "soul of a nation" represents the collective spirit, enduring cultural heritage, ethical values (like Vasudhaiva Kutumbakam and Ahimsa), and shared aspirations of its people that survive centuries of foreign subjugation. Foreign rule suppressed this creative voice; independence allowed that latent spirit to finally find free expression.</p>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q7. Classroom Debate: Imagine you are a freedom fighter. Explain your method (Non-violence vs. Armed Resistance) and what debate teaches about unity.</summary>
        <div class="ans-content">
          <p><strong>Perspective A (Satyagraha / Non-Violence):</strong> "Violence only begets greater state repression and brutalizes society. By using truth, boycott, and willingness to suffer without retaliation, we strip the British empire of its moral legitimacy and awaken the conscience of the world."</p>
          <p><strong>Perspective B (Revolutionary / Armed Struggle):</strong> "An empire built on gunpowder and imperial armies will never yield to moral persuasion alone. Fearless strikes, military sabotage, and Netaji's Azad Hind Fauj prove that Indians can shatter the military pillar of the British Raj."</p>
          <p><strong>Lesson on Unity:</strong> Even though Gandhi, Bose, Bhagat Singh, and Ambedkar differed sharply on strategies and philosophical priorities, their love for the motherland and ultimate goal of national liberation remained identical. True national unity does not mean uniform obedience; it means working toward a common noble cause through respectful diversity of approaches.</p>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q8. Write a News Report based on an important event (Sample: The Salt March at Dandi).</summary>
        <div class="ans-content">
          <div style="background: #fdf6e2; padding: 16px; border: 1px dashed #d97706; border-radius: 8px; font-family: Georgia, serif;">
            <h4 style="text-align: center; margin-bottom: 4px; font-size: 1.2rem; color: #78350f;">THE FREE HINDUSTAN CHRONICLE</h4>
            <p style="text-align: center; font-size: 0.8rem; border-bottom: 1px solid #d97706; padding-bottom: 6px;">DANDI, GUJARAT &bull; 6 APRIL 1930 &bull; MORNING EDITION</p>
            <h3 style="margin: 10px 0 6px; font-size: 1.15rem; color: #1e293b;">PINCH OF SALT SHATTERS THE MIGHT OF THE BRITISH EMPIRE!</h3>
            <p style="font-size: 0.9rem;"><strong>DANDI:</strong> At 6:30 AM this morning, after offering dawn prayers on the sea shore, Mahatma Gandhi walked into the waters of the Arabian Sea. Returning to the beach, he bent down and picked up a handful of natural salt encrusted on the mud flats, deliberately breaking the British salt monopoly laws.</p>
            <p style="font-size: 0.9rem;"><strong>Public Reaction:</strong> Eyewitness and local farmer Raman Patel (48) exclaimed with tears in his eyes: <em>"The British government made us pay tax on God's gift of salt from our own seas! By lifting this salt, Bapu has lifted the heavy chains of fear from our hearts!"</em></p>
            <p style="font-size: 0.9rem;"><strong>Historical Significance:</strong> This peaceful act of civil disobedience signals to the entire subcontinent that colonial laws without moral sanction will no longer be obeyed. Nationwide boiling of salt has erupted along India's 6,000 km coastline.</p>
          </div>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q9. Museum Exhibition Design: Three Historical Objects representing the Freedom Struggle.</summary>
        <div class="ans-content">
          <p><strong>Exhibit Title:</strong> <em>"Echoes of Courage: Relics of India's Long Road to Freedom"</em></p>
          <ol>
            <li><strong>Object 1: A Wooden Spinning Wheel (Charkha):</strong>
              <br><em>Meaning:</em> Symbolizes <em>Swadeshi</em>, self-reliance, dignity of manual labor, and economic defiance against the industrial mills of Manchester.
            </li>
            <li><strong>Object 2: Bhagat Singh's Pocket Notebook from Lahore Jail:</strong>
              <br><em>Meaning:</em> Contains his revolutionary writings (including <em>"Why I am an Atheist"</em>) illustrating that revolutionaries were deep thinkers, avid readers, and visionary humanists, not merely men of arms.
            </li>
            <li><strong>Object 3: The Uniform Badge of the Rani of Jhansi Regiment (INA):</strong>
              <br><em>Meaning:</em> Symbolizes the courage of women soldiers who fought on the frontlines under Netaji Subhas Chandra Bose, breaking patriarchal traditions to liberate their motherland.
            </li>
          </ol>
          <p><strong>Visitor Takeaway:</strong> Visitors should understand that freedom is never free; it was earned through tears, intellect, labor, and supreme sacrifice, inspiring students to guard this democracy with vigilance.</p>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q10. Citizen Responsibilities Today: 5 to 10 lines to protect and strengthen India's hard-won freedom.</summary>
        <div class="ans-content">
          <ol>
            <li><strong>Uphold Communal Harmony:</strong> Actively reject hatred, religious bigotry, and caste discrimination, honoring the composite culture of our freedom fighters.</li>
            <li><strong>Exercise the Right to Vote:</strong> Participate conscientiously in elections without succumbing to money, caste, or sectarian appeals.</li>
            <li><strong>Protect Democratic Institutions:</strong> Respect the Constitution, the rule of law, and an independent judiciary.</li>
            <li><strong>Support Self-Reliance (Atmanirbharta):</strong> Promote local innovators, Indian science, sustainable agriculture, and indigenous industries.</li>
            <li><strong>Foster Environmental Stewardship:</strong> Safeguard India's natural resources&mdash;rivers, forests, clean air, and soil&mdash;for future generations.</li>
            <li><strong>Stand for Truth and Justice:</strong> Oppose misinformation, fight corruption, and ensure that the fruits of freedom reach the most marginalized citizen.</li>
          </ol>
        </div>
      </details>
    </section>

    <!-- SECTION 5: INTERACTIVE QUIZ ENGINE -->
    <section id="quiz">
      <h2>5. Interactive Concept Mastery Quiz</h2>
      <p>Test your conceptual understanding with real-time feedback. Click your chosen option to receive immediate explanations.</p>

      <div class="quiz-card" id="qcard1">
        <div class="quiz-question">1. Who was the first President of the Indian National Congress in 1885?</div>
        <div class="quiz-options">
          <button class="quiz-opt" onclick="checkQuiz(this, false, 'f1', 'A.O. Hume was the British facilitator, not the President.')">A. Allan Octavian Hume</button>
          <button class="quiz-opt" onclick="checkQuiz(this, true, 'f1', 'Correct! Womesh Chandra Bonnerjee presided over the 72 delegates in Bombay in December 1885.')">B. Womesh Chandra Bonnerjee</button>
          <button class="quiz-opt" onclick="checkQuiz(this, false, 'f1', 'Dadabhai Naoroji was the second president (Calcutta, 1886).')">C. Dadabhai Naoroji</button>
          <button class="quiz-opt" onclick="checkQuiz(this, false, 'f1', 'Gopal Krishna Gokhale presided later in 1905.')">D. Gopal Krishna Gokhale</button>
        </div>
        <div class="quiz-feedback" id="f1"></div>
      </div>

      <div class="quiz-card" id="qcard2">
        <div class="quiz-question">2. Which Viceroy was responsible for the controversial Partition of Bengal in 1905?</div>
        <div class="quiz-options">
          <button class="quiz-opt" onclick="checkQuiz(this, false, 'f2', 'Lord Dalhousie implemented the Doctrine of Lapse in the 1850s.')">A. Lord Dalhousie</button>
          <button class="quiz-opt" onclick="checkQuiz(this, true, 'f2', 'Spot on! Lord Curzon partitioned Bengal to weaken the national movement along religious lines.')">B. Lord Curzon</button>
          <button class="quiz-opt" onclick="checkQuiz(this, false, 'f2', 'Lord Mountbatten partitioned India in 1947.')">C. Lord Mountbatten</button>
          <button class="quiz-opt" onclick="checkQuiz(this, false, 'f2', 'Lord Irwin signed the Gandhi-Irwin pact in 1931.')">D. Lord Irwin</button>
        </div>
        <div class="quiz-feedback" id="f2"></div>
      </div>

      <div class="quiz-card" id="qcard3">
        <div class="quiz-question">3. Why did Rabindranath Tagore renounce his British Knighthood in 1919?</div>
        <div class="quiz-options">
          <button class="quiz-opt" onclick="checkQuiz(this, false, 'f3', 'Tagore did not renounce it over the Bengal partition in 1905.')">A. In protest against the Partition of Bengal</button>
          <button class="quiz-opt" onclick="checkQuiz(this, true, 'f3', 'Correct! He relinquished his Knighthood in deep anguish and protest over the Jallianwala Bagh massacre.')">B. In protest against the Jallianwala Bagh Massacre</button>
          <button class="quiz-opt" onclick="checkQuiz(this, false, 'f3', 'The Salt March occurred in 1930.')">C. In support of the Salt Satyagraha</button>
          <button class="quiz-opt" onclick="checkQuiz(this, false, 'f3', 'The Simon Commission visited India in 1928.')">D. To protest against the Simon Commission</button>
        </div>
        <div class="quiz-feedback" id="f3"></div>
      </div>

      <div class="quiz-card" id="qcard4">
        <div class="quiz-question">4. Why did Mahatma Gandhi abruptly withdraw the Non-Cooperation Movement in February 1922?</div>
        <div class="quiz-options">
          <button class="quiz-opt" onclick="checkQuiz(this, false, 'f4', 'The British had not agreed to grant Swaraj.')">A. Because the British government granted full Dominion status</button>
          <button class="quiz-opt" onclick="checkQuiz(this, true, 'f4', 'Correct! The violent clash at Chauri Chaura, where 22 policemen were burned alive, violated Gandhi\'s strict principle of Ahimsa.')">B. Due to the violent clash at Chauri Chaura</button>
          <button class="quiz-opt" onclick="checkQuiz(this, false, 'f4', 'Subhas Chandra Bose actually criticized Gandhi for withdrawing the movement.')">C. Because Subhas Chandra Bose advised him to do so</button>
          <button class="quiz-opt" onclick="checkQuiz(this, false, 'f4', 'The movement enjoyed massive popular participation.')">D. Because peasants refused to participate</button>
        </div>
        <div class="quiz-feedback" id="f4"></div>
      </div>

      <div class="quiz-card" id="qcard5">
        <div class="quiz-question">5. The historic resolution demanding 'Purna Swaraj' (Complete Independence) was passed at which Congress Session?</div>
        <div class="quiz-options">
          <button class="quiz-opt" onclick="checkQuiz(this, false, 'f5', 'Nagpur Session of 1920 passed the Non-Cooperation resolution.')">A. Nagpur Session 1920</button>
          <button class="quiz-opt" onclick="checkQuiz(this, false, 'f5', 'Surat Session 1907 witnessed the split between Moderates and Extremists.')">B. Surat Session 1907</button>
          <button class="quiz-opt" onclick="checkQuiz(this, true, 'f5', 'Exact! The Lahore Session of December 1929, presided over by Jawaharlal Nehru, passed the Purna Swaraj resolution.')">C. Lahore Session 1929</button>
          <button class="quiz-opt" onclick="checkQuiz(this, false, 'f5', 'Karachi Session 1931 endorsed the Gandhi-Irwin pact.')">D. Karachi Session 1931</button>
        </div>
        <div class="quiz-feedback" id="f5"></div>
      </div>

      <div class="quiz-card" id="qcard6">
        <div class="quiz-question">6. The Poona Pact of September 1932 was signed between which two leaders?</div>
        <div class="quiz-options">
          <button class="quiz-opt" onclick="checkQuiz(this, false, 'f6', 'Nehru and Jinnah never signed a pact named the Poona Pact.')">A. Jawaharlal Nehru and Muhammad Ali Jinnah</button>
          <button class="quiz-opt" onclick="checkQuiz(this, true, 'f6', 'Correct! Signed between Mahatma Gandhi and Dr. B.R. Ambedkar to provide reserved seats for Depressed Classes within joint electorates.')">B. Mahatma Gandhi and Dr. B.R. Ambedkar</button>
          <button class="quiz-opt" onclick="checkQuiz(this, false, 'f6', 'Lord Irwin signed the Gandhi-Irwin Pact in 1931.')">C. Mahatma Gandhi and Lord Irwin</button>
          <button class="quiz-opt" onclick="checkQuiz(this, false, 'f6', 'Subhas Chandra Bose and Rash Behari Bose operated in East Asia.')">D. Subhas Chandra Bose and Rash Behari Bose</button>
        </div>
        <div class="quiz-feedback" id="f6"></div>
      </div>

      <div class="quiz-card" id="qcard7">
        <div class="quiz-question">7. Who led the famous underground secret radio transmitter during the 1942 Quit India Movement?</div>
        <div class="quiz-options">
          <button class="quiz-opt" onclick="checkQuiz(this, false, 'f7', 'Aruna Asaf Ali hoisted the national flag at Gowalia Tank.')">A. Aruna Asaf Ali</button>
          <button class="quiz-opt" onclick="checkQuiz(this, true, 'f7', 'Spot on! Young Usha Mehta operated the clandestine Congress Radio to broadcast uncensored news.')">B. Usha Mehta</button>
          <button class="quiz-opt" onclick="checkQuiz(this, false, 'f7', 'Captain Lakshmi Sahgal commanded the Rani of Jhansi regiment in the INA.')">C. Captain Lakshmi Sahgal</button>
          <button class="quiz-opt" onclick="checkQuiz(this, false, 'f7', 'Matangini Hazra was martyred holding the flag in Tamluk, Bengal.')">D. Matangini Hazra</button>
        </div>
        <div class="quiz-feedback" id="f7"></div>
      </div>

      <div class="quiz-card" id="qcard8">
        <div class="quiz-question">8. When was the Radcliffe Line boundary award dividing India and Pakistan officially published?</div>
        <div class="quiz-options">
          <button class="quiz-opt" onclick="checkQuiz(this, false, 'f8', 'It was not published before Independence.')">A. 3 June 1947</button>
          <button class="quiz-opt" onclick="checkQuiz(this, false, 'f8', 'India became independent on 15 August, but the borders were announced later.')">B. 15 August 1947</button>
          <button class="quiz-opt" onclick="checkQuiz(this, true, 'f8', 'Correct! It was published on 17 August 1947, two days after Independence Day.')">C. 17 August 1947</button>
          <button class="quiz-opt" onclick="checkQuiz(this, false, 'f8', '26 January 1950 is Republic Day.')">D. 26 January 1950</button>
        </div>
        <div class="quiz-feedback" id="f8"></div>
      </div>
    </section>

    <!-- SECTION 6: REVISION & EXAM TRAPS -->
    <section id="revision">
      <h2>6. Exam Hall Traps &amp; 15 High-Yield Revision Facts</h2>

      <div class="callout callout-warn">
        <div class="callout-title">Top 4 Exam Pitfalls Students Must Avoid</div>
        <ul>
          <li><strong>Trap 1: Confusing Non-Cooperation (1920) with Civil Disobedience (1930).</strong> Non-Cooperation asked citizens to <em>stop cooperating</em> with the administration (boycott titles, courts, schools, and foreign goods). Civil Disobedience went a step further: it asked citizens to <em>actively break unjust colonial laws</em> (such as breaking the salt laws, forest laws, and refusing to pay land tax).</li>
          <li><strong>Trap 2: Origin of INA.</strong> Netaji Subhas Chandra Bose did NOT establish the INA from scratch. General Mohan Singh and Rash Behari Bose originally raised it; Netaji was invited to take supreme leadership in 1943.</li>
          <li><strong>Trap 3: "Do or Die" Movement.</strong> Do not write that Gandhi gave the "Do or Die" slogan in 1920 or 1930. It was exclusively the battle cry of the <strong>1942 Quit India Movement</strong>.</li>
          <li><strong>Trap 4: Separate Electorates vs. Reserved Seats.</strong> Separate electorates meant only Dalit voters could vote for Dalit candidates (a separate political system). Reserved seats meant candidates must be Dalit, but all adults in the constituency (Dalits, Hindus, Muslims, etc.) vote together. The 1932 Poona Pact chose <strong>reserved seats</strong>, not separate electorates.</li>
        </ul>
      </div>

      <h3>15 High-Yield Facts for Quick Revision</h3>
      <ol>
        <li><strong>1885:</strong> First Congress session in Bombay; 72 delegates presided by W.C. Bonnerjee; facilitated by A.O. Hume.</li>
        <li><strong>Drain Theory:</strong> Propounded by Dadabhai Naoroji in his book <em>Poverty and Un-British Rule in India</em>.</li>
        <li><strong>1905:</strong> Partition of Bengal by Lord Curzon sparking the Swadeshi and Boycott Movement; reversed in 1911.</li>
        <li><strong>Swadeshi Enterprises:</strong> Bengal Chemicals (Acharya P.C. Ray), Swadeshi Mills (J.N. Tata), Swadeshi Steam Navigation (V.O. Chidambaram Pillai).</li>
        <li><strong>Lal-Bal-Pal:</strong> Lala Lajpat Rai (Punjab), Bal Gangadhar Tilak (Maharashtra), Bipin Chandra Pal (Bengal).</li>
        <li><strong>1908:</strong> Execution of 18-year-old Khudiram Bose for the Muzaffarpur bomb incident.</li>
        <li><strong>1915:</strong> Return of Mahatma Gandhi from South Africa; Bagha Jatin martyred at Burhi Balam (Balasore, Odisha).</li>
        <li><strong>13 April 1919:</strong> Jallianwala Bagh massacre in Amritsar by General Reginald Dyer; Tagore renounced his Knighthood.</li>
        <li><strong>1920&ndash;1922:</strong> Non-Cooperation Movement launched; suspended after the Chauri Chaura violence in February 1922.</li>
        <li><strong>Kakori Train Action (1925):</strong> Carried out by HRA leaders (Ram Prasad Bismil, Ashfaqullah Khan, Chandrashekhar Azad).</li>
        <li><strong>Lahore Session (1929):</strong> Congress under Jawaharlal Nehru declared <em>Purna Swaraj</em> (Complete Independence).</li>
        <li><strong>Dandi March (1930):</strong> 240-mile trek from Sabarmati to Dandi (12 March to 6 April 1930) by Gandhi and 78 followers to break the salt tax.</li>
        <li><strong>Poona Pact (1932):</strong> Signed between Gandhi and Ambedkar, granting 148 reserved seats for Dalits instead of separate electorates.</li>
        <li><strong>Azad Hind Fauj (1943):</strong> Reorganized by Netaji Subhas Chandra Bose in Singapore; Rani of Jhansi regiment commanded by Captain Lakshmi Sahgal.</li>
        <li><strong>15 August 1947:</strong> India achieved freedom; Cyril Radcliffe divided Bengal and Punjab; Nehru delivered the "Tryst with Destiny" speech.</li>
      </ol>
    </section>

  </main>

  <button id="back-to-top" onclick="scrollToTop()" title="Back to top">↑</button>

  <script>
    // Reading Progress Bar
    window.addEventListener('scroll', () => {
      const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      document.getElementById('reading-progress-bar').style.width = scrolled + '%';

      // Back to top toggle
      const btt = document.getElementById('back-to-top');
      if (winScroll > 300) {
        btt.style.display = 'flex';
      } else {
        btt.style.display = 'none';
      }
    });

    function scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Interactive Quiz Engine
    function checkQuiz(btn, isCorrect, feedbackId, explanation) {
      const parent = btn.parentElement;
      const allButtons = parent.querySelectorAll('.quiz-opt');
      allButtons.forEach(b => b.disabled = true);

      const fb = document.getElementById(feedbackId);
      if (isCorrect) {
        btn.style.backgroundColor = '#86efac';
        btn.style.borderColor = '#16a34a';
        btn.style.color = '#064e3b';
        btn.style.fontWeight = 'bold';
        fb.className = 'quiz-feedback feedback-correct';
        fb.innerHTML = '<strong>✓ Correct!</strong> ' + explanation;
      } else {
        btn.style.backgroundColor = '#fca5a5';
        btn.style.borderColor = '#dc2626';
        btn.style.color = '#7f1d1d';
        btn.style.fontWeight = 'bold';
        fb.className = 'quiz-feedback feedback-wrong';
        fb.innerHTML = '<strong>✗ Incorrect.</strong> ' + explanation;
      }
    }

    // Text to Speech
    let isSpeaking = false;
    let synth = window.speechSynthesis;
    let utterance = null;

    function toggleAudio() {
      if (!synth) {
        alert('Text-to-Speech is not supported in this browser.');
        return;
      }
      if (isSpeaking) {
        synth.cancel();
        isSpeaking = false;
        document.getElementById('tts-icon').innerText = '▶';
        document.getElementById('tts-label').innerText = 'Listen to Chapter Notes';
      } else {
        const text = "Class 8 Social Science. Chapter 9: India's Long Road to Independence. " + 
          document.querySelector('#mindmap p').innerText + " " +
          document.querySelector('#concepts p').innerText;
        utterance = new SpeechSynthesisUtterance(text);
        utterance.rate = 0.95;
        utterance.pitch = 1.0;
        utterance.onend = () => {
          isSpeaking = false;
          document.getElementById('tts-icon').innerText = '▶';
          document.getElementById('tts-label').innerText = 'Listen to Chapter Notes';
        };
        synth.speak(utterance);
        isSpeaking = true;
        document.getElementById('tts-icon').innerText = '⏸';
        document.getElementById('tts-label').innerText = 'Pause Reading';
      }
    }
  </script>
</body>
</html>
'''

target_path = os.path.join('english', 'class8', 'sst-ch9-indias-long-road-to-independence.html')
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully generated {target_path} ({len(html_content.encode('utf-8'))} bytes)")
