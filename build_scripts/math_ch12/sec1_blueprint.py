# -*- coding: utf-8 -*-
"""
Section 1 Module: Hero Banner, Audio Reader, Visual Blueprint & Mind Map
Class 8 Mathematics Chapter 12: Tales by Dots and Lines (NCERT NEP code: hegp112)
"""

def get_section_1():
    return """
    <!-- Hero Banner -->
    <header class="hero-banner">
      <div class="hero-badges">
        <span class="badge badge-primary"><i class="fa-solid fa-book-open"></i> NCERT Ganita Prakash Class 8 Part-II</span>
        <span class="badge badge-gold"><i class="fa-solid fa-certificate"></i> NEP 2020 Code: hegp112</span>
        <span class="badge badge-emerald"><i class="fa-solid fa-check-double"></i> 100% Zero-Omission Complete Edition</span>
      </div>
      <h1 class="hero-title">Tales by Dots and Lines</h1>
      <p class="hero-subtitle">
        An exhaustive, mathematically rigorous, and child-friendly master guide unlocking the physical fulcrum model of arithmetic mean, algebraic proofs of shifting and scaling invariants, sensitivity analysis of mean versus median, cumulative frequency distributions, spreadsheet formulas, 2-step line graph interpretation protocols, and captivating real-life data stories (climate trends, space launches, 24-hour activity strips, lifetime sleep curves, and the Game of Hex).
      </p>

      <div class="hero-stats">
        <div class="stat-item">
          <i class="fa-solid fa-scale-balanced stat-icon"></i>
          <div class="stat-text">
            <h4>The Balancing Act</h4>
            <p>Physical Fulcrum & Deviation Balance &Sigma;(x - x̄) = 0</p>
          </div>
        </div>
        <div class="stat-item">
          <i class="fa-solid fa-square-root-variable stat-icon"></i>
          <div class="stat-text">
            <h4>Algebraic Invariants</h4>
            <p>Rigid Shifting (x̄ + c) & Scaling (k &times; x̄) Proofs</p>
          </div>
        </div>
        <div class="stat-item">
          <i class="fa-solid fa-table-cells stat-icon"></i>
          <div class="stat-text">
            <h4>Frequencies & Tech</h4>
            <p>Weighted Means & Spreadsheets (=SUM, =AVERAGE)</p>
          </div>
        </div>
        <div class="stat-item">
          <i class="fa-solid fa-chart-line stat-icon"></i>
          <div class="stat-text">
            <h4>Visual Storytelling</h4>
            <p>Line Graphs, Slopes, Activity Strips & Hex Topology</p>
          </div>
        </div>
      </div>
    </header>

    <!-- TTS Audio Reader Bar -->
    <div class="tts-container">
      <div class="tts-info">
        <div class="tts-icon-box">
          <i class="fa-solid fa-headphones"></i>
        </div>
        <div class="tts-details">
          <h4>Audio Teacher Reader (Listen to Chapter Summary)</h4>
          <p id="ttsStatus">Click Play to listen to an engaging audio overview of Chapter 12 concepts.</p>
        </div>
      </div>
      <div class="tts-controls">
        <button class="tts-btn" id="ttsPlayBtn" onclick="toggleAudioReader()">
          <i class="fa-solid fa-play" id="ttsIcon"></i> Listen to Summary
        </button>
        <select class="tts-select" id="ttsRate" onchange="updateSpeechRate()">
          <option value="0.8">0.8x Speed (Slow & Clear)</option>
          <option value="1.0" selected>1.0x Speed (Normal)</option>
          <option value="1.2">1.2x Speed (Brisk Revision)</option>
          <option value="1.4">1.4x Speed (Rapid Recap)</option>
        </select>
      </div>
    </div>

    <!-- MAIN CONTAINER -->
    <main class="main-content">

      <!-- SECTION 1: BLUEPRINT & MIND MAP -->
      <section id="section1" class="section-box">
        <div class="section-header">
          <div class="section-header-left">
            <span class="section-tag">Curriculum Architecture</span>
            <h2 class="section-title">§ 1. Visual Blueprint & Detailed Mind Map</h2>
            <p class="section-desc">
              A comprehensive visual roadmap structuring Chapter 12 into five master pedagogical branches: moving from physical and algebraic models of central tendency (the balancing act) to computational tools (spreadsheets) and dynamic visual analytics (line graphs, time-series slopes, activity strips, and topological board games).
            </p>
          </div>
          <div>
            <span class="badge badge-primary"><i class="fa-solid fa-sitemap"></i> 5 Master Branches</span>
          </div>
        </div>

        <!-- INLINE RESPONSIVE SVG 1: CHAPTER 12 CONCEPT MIND MAP -->
        <div class="svg-graphic-box">
          <svg viewBox="0 0 1000 620" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="bgGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#0f172a" />
                <stop offset="100%" stop-color="#075985" />
              </linearGradient>
              <linearGradient id="centerGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#0284c7" />
                <stop offset="100%" stop-color="#0d9488" />
              </linearGradient>
              <linearGradient id="cardGradA" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#0369a1" />
                <stop offset="100%" stop-color="#0284c7" />
              </linearGradient>
              <linearGradient id="cardGradB" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#0f766e" />
                <stop offset="100%" stop-color="#14b8a6" />
              </linearGradient>
              <linearGradient id="cardGradC" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#6d28d9" />
                <stop offset="100%" stop-color="#8b5cf6" />
              </linearGradient>
              <linearGradient id="cardGradD" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#b45309" />
                <stop offset="100%" stop-color="#f59e0b" />
              </linearGradient>
              <linearGradient id="cardGradE" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#be123c" />
                <stop offset="100%" stop-color="#f43f5e" />
              </linearGradient>
              <filter id="glow1" x="-20%" y="-20%" width="140%" height="140%">
                <feGaussianBlur stdDeviation="6" result="blur" />
                <feComposite in="SourceGraphic" in2="blur" operator="over" />
              </filter>
            </defs>

            <!-- Background Canvas -->
            <rect width="1000" height="620" rx="20" fill="url(#bgGrad1)" />

            <!-- Connecting Curves -->
            <path d="M 500 310 C 350 200, 250 140, 180 110" stroke="#38bdf8" stroke-width="3" fill="none" opacity="0.6" stroke-dasharray="6,6" />
            <path d="M 500 310 C 650 200, 750 140, 820 110" stroke="#2dd4bf" stroke-width="3" fill="none" opacity="0.6" stroke-dasharray="6,6" />
            <path d="M 500 310 C 300 320, 220 370, 180 430" stroke="#c084fc" stroke-width="3" fill="none" opacity="0.6" stroke-dasharray="6,6" />
            <path d="M 500 310 C 700 320, 780 370, 820 430" stroke="#fbbf24" stroke-width="3" fill="none" opacity="0.6" stroke-dasharray="6,6" />
            <path d="M 500 310 C 500 420, 500 480, 500 520" stroke="#fb7185" stroke-width="3" fill="none" opacity="0.6" stroke-dasharray="6,6" />

            <!-- Central Hub -->
            <g transform="translate(500, 310)">
              <circle r="85" fill="url(#centerGrad1)" filter="url(#glow1)" stroke="#ffffff" stroke-width="3" />
              <text text-anchor="middle" y="-22" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-weight="800" font-size="15">TALES BY</text>
              <text text-anchor="middle" y="2" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-weight="800" font-size="16">DOTS &amp; LINES</text>
              <text text-anchor="middle" y="24" fill="#e0f2fe" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600">Class 8 Mathematics</text>
              <text text-anchor="middle" y="40" fill="#bae6fd" font-family="'JetBrains Mono', monospace" font-size="10">hegp112 • NEP 2020</text>
            </g>

            <!-- Node 1: Top Left (The Balancing Act) -->
            <g transform="translate(70, 40)">
              <rect width="230" height="120" rx="14" fill="url(#cardGradA)" stroke="#38bdf8" stroke-width="2" />
              <text x="18" y="28" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="14">1. The Balancing Act</text>
              <text x="18" y="52" fill="#e0f2fe" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">• Mean as Physical Fulcrum</text>
              <text x="18" y="72" fill="#e0f2fe" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">• LHS Distance = RHS Distance</text>
              <text x="18" y="92" fill="#e0f2fe" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">• Uniqueness of Center Point</text>
              <text x="18" y="110" fill="#bae6fd" font-family="'JetBrains Mono', monospace" font-size="10">&Sigma;(x - x̄) = 0</text>
            </g>

            <!-- Node 2: Top Right (Algebraic Invariants) -->
            <g transform="translate(700, 40)">
              <rect width="240" height="120" rx="14" fill="url(#cardGradB)" stroke="#2dd4bf" stroke-width="2" />
              <text x="18" y="28" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="14">2. Algebraic Invariants</text>
              <text x="18" y="52" fill="#ccfbf1" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">• Shifting: x' = x + c &rArr; x̄' = x̄ + c</text>
              <text x="18" y="72" fill="#ccfbf1" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">• Scaling: x' = kx &rArr; x̄' = k &times; x̄</text>
              <text x="18" y="92" fill="#ccfbf1" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">• Median Positional Resilience</text>
              <text x="18" y="110" fill="#a7f3d0" font-family="'Plus Jakarta Sans', sans-serif" font-size="10">• Immunity to Outliers</text>
            </g>

            <!-- Node 3: Bottom Left (Frequencies & Spreadsheets) -->
            <g transform="translate(70, 360)">
              <rect width="230" height="130" rx="14" fill="url(#cardGradC)" stroke="#c084fc" stroke-width="2" />
              <text x="18" y="28" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="14">3. Frequencies &amp; Tech</text>
              <text x="18" y="52" fill="#f5f3ff" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">• Weighted Mean: &Sigma;fx / &Sigma;f</text>
              <text x="18" y="72" fill="#f5f3ff" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">• Cumulative Frequencies</text>
              <text x="18" y="92" fill="#f5f3ff" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">• Locating Median Ranks</text>
              <text x="18" y="112" fill="#e9d5ff" font-family="'JetBrains Mono', monospace" font-size="10">Spreadsheets: =SUM, =AVERAGE</text>
            </g>

            <!-- Node 4: Bottom Right (Line Graphs & Slopes) -->
            <g transform="translate(700, 360)">
              <rect width="240" height="130" rx="14" fill="url(#cardGradD)" stroke="#fbbf24" stroke-width="2" />
              <text x="18" y="28" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="14">4. Line Graphs &amp; Slopes</text>
              <text x="18" y="52" fill="#fefce8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">• Visualising Change Over Time</text>
              <text x="18" y="72" fill="#fefce8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">• 2-Step Protocol: Identify &amp; Infer</text>
              <text x="18" y="92" fill="#fefce8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">• Slope = Instant Rate of Change</text>
              <text x="18" y="112" fill="#fde68a" font-family="'Plus Jakarta Sans', sans-serif" font-size="10">• Kerala vs Punjab Climate Trends</text>
            </g>

            <!-- Node 5: Bottom Center (Data Stories & Hex Topology) -->
            <g transform="translate(360, 480)">
              <rect width="280" height="110" rx="14" fill="url(#cardGradE)" stroke="#fb7185" stroke-width="2" />
              <text x="20" y="28" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="14">5. Real-Life Stories &amp; Hex</text>
              <text x="20" y="52" fill="#ffe4e6" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">• 48-Box Activity Strips (24-Hour Day)</text>
              <text x="20" y="72" fill="#ffe4e6" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">• Sleepy-Deepy Curve (Ages 6 to 75)</text>
              <text x="20" y="92" fill="#fecdd3" font-family="'Plus Jakarta Sans', sans-serif" font-size="10">• Astronomical Cycles &amp; Nash's Game of Hex</text>
            </g>
          </svg>
          <div class="svg-caption">
            Figure 1.1: Master Architectural Mind Map of Class 8 Mathematics Chapter 12 ("Tales by Dots and Lines").
          </div>
        </div>

        <div class="concept-card">
          <h3 class="concept-card-title"><i class="fa-solid fa-compass"></i> Chapter Narrative Walkthrough</h3>
          <p>
            Welcome to one of the most exciting, visually intuitive chapters in modern middle-school mathematics! In Class 6 and 7, you learned about the <strong>arithmetic mean</strong> as a simple "fair-share" operation—imagine pooling candies from everyone in a room and distributing them back equally. In Chapter 12, we elevate this idea to a deeper, more profound physical and geometric truth: <strong>the arithmetic mean is the physical balance point (center of gravity or fulcrum) of a dataset</strong>.
          </p>
          <p>
            When data points are placed on a number line like weights on a seesaw, the mean is the exact fulcrum where the seesaw rests in perfect horizontal equilibrium. The sum of all distances to points lying to the left of the mean exactly equals the sum of all distances to points lying to the right. From this single elegant principle flows a rich tapestry of mathematical proofs:
          </p>
          <ul style="margin-left: 1.5rem; margin-top: 0.5rem; line-height: 1.8;">
            <li><strong>Why the center is unique:</strong> If you nudge the fulcrum even a millimeter to the left or right, the balance of distances is instantly broken.</li>
            <li><strong>How data additions and removals work:</strong> Adding an observation above the mean pulls the balance point upward; adding one below pulls it downward.</li>
            <li><strong>Rigid shifting and scaling:</strong> Adding a fixed amount to everyone's score slides the entire seesaw forward without warping its balance; multiplying scores scales the balance point proportionally.</li>
            <li><strong>Modern data handling:</strong> When dealing with hundreds of observations, we organize data into frequency tables and unleash digital spreadsheets using formulas like <span class="math-inline">=SUM()</span> and <span class="math-inline">=AVERAGE()</span>.</li>
            <li><strong>Visual storytelling with line graphs:</strong> When categories multiply across months and years, bar charts become cluttered forests. Line graphs turn discrete data points into continuous stories where the steepness of a line reveals how fast things change.</li>
          </ul>
        </div>
      </section>
"""
