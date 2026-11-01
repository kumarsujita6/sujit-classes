# -*- coding: utf-8 -*-
"""
SVG Diagrams Generator for Class 7 Mathematics Ch 2: Arithmetic Expressions
"""

def get_svg_mindmap():
    return '''<div class="svg-diagram-card">
  <svg viewBox="0 0 1000 660" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Visual Blueprint & Mind Map of Chapter 2 Arithmetic Expressions">
    <defs>
      <linearGradient id="gradCenter" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0284c7" />
        <stop offset="100%" stop-color="#0f172a" />
      </linearGradient>
      <linearGradient id="gradB1" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0284c7" />
        <stop offset="100%" stop-color="#0369a1" />
      </linearGradient>
      <linearGradient id="gradB2" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0d9488" />
        <stop offset="100%" stop-color="#0f766e" />
      </linearGradient>
      <linearGradient id="gradB3" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#7c3aed" />
        <stop offset="100%" stop-color="#6d28d9" />
      </linearGradient>
      <linearGradient id="gradB4" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#ea580c" />
        <stop offset="100%" stop-color="#c2410c" />
      </linearGradient>
      <linearGradient id="gradB5" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#16a34a" />
        <stop offset="100%" stop-color="#15803d" />
      </linearGradient>
      <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
        <feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.12" />
      </filter>
    </defs>

    <!-- Background -->
    <rect width="1000" height="660" rx="16" fill="#f8fafc" />

    <!-- Connecting curved paths -->
    <!-- Center to Top-Left: Branch 1 -->
    <path d="M 500 330 C 350 330, 260 160, 180 150" stroke="#0284c7" stroke-width="3" stroke-dasharray="6,4" fill="none" opacity="0.6"/>
    <!-- Center to Top-Right: Branch 2 -->
    <path d="M 500 330 C 650 330, 740 160, 820 150" stroke="#0d9488" stroke-width="3" stroke-dasharray="6,4" fill="none" opacity="0.6"/>
    <!-- Center to Middle-Left: Branch 3 -->
    <path d="M 500 330 C 340 330, 260 330, 180 330" stroke="#7c3aed" stroke-width="3" stroke-dasharray="6,4" fill="none" opacity="0.6"/>
    <!-- Center to Middle-Right: Branch 4 -->
    <path d="M 500 330 C 660 330, 740 330, 820 330" stroke="#ea580c" stroke-width="3" stroke-dasharray="6,4" fill="none" opacity="0.6"/>
    <!-- Center to Bottom-Left: Branch 5 -->
    <path d="M 500 330 C 350 330, 260 510, 180 510" stroke="#16a34a" stroke-width="3" stroke-dasharray="6,4" fill="none" opacity="0.6"/>
    <!-- Center to Bottom-Right: Branch 6 -->
    <path d="M 500 330 C 650 330, 740 510, 820 510" stroke="#0369a1" stroke-width="3" stroke-dasharray="6,4" fill="none" opacity="0.6"/>

    <!-- Central Core Node -->
    <g filter="url(#shadow)">
      <rect x="360" y="275" width="280" height="110" rx="20" fill="url(#gradCenter)" stroke="#38bdf8" stroke-width="3" />
      <text x="500" y="315" fill="#f8fafc" font-size="19" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">ARITHMETIC EXPRESSIONS</text>
      <text x="500" y="342" fill="#38bdf8" font-size="13" font-family="'Space Grotesk', sans-serif" font-weight="600" text-anchor="middle">NCERT Grade 7 • Ganita Prakash (gegp102)</text>
      <text x="500" y="365" fill="#94a3b8" font-size="11" font-family="'Plus Jakarta Sans', sans-serif" text-anchor="middle">Structure • Properties • Brackets • Applications</text>
    </g>

    <!-- Branch 1: Top-Left (Simple Expressions & Values) -->
    <g filter="url(#shadow)">
      <rect x="40" y="90" width="280" height="115" rx="14" fill="#ffffff" stroke="#0284c7" stroke-width="2" />
      <rect x="40" y="90" width="280" height="32" rx="14" fill="url(#gradB1)" />
      <text x="180" y="112" fill="#ffffff" font-size="13" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">1. SIMPLE EXPRESSIONS &amp; VALUES</text>
      <text x="55" y="140" fill="#334155" font-size="11" font-family="'Plus Jakarta Sans', sans-serif">• Numerical phrases: 13 + 2, 20 − 4, 12 × 5</text>
      <text x="55" y="160" fill="#334155" font-size="11" font-family="'Plus Jakarta Sans', sans-serif">• Unique Value: Number it evaluates to (=)</text>
      <text x="55" y="180" fill="#334155" font-size="11" font-family="'Plus Jakarta Sans', sans-serif">• Reasoning comparisons: 1023+125 vs 1022+128</text>
    </g>

    <!-- Branch 2: Top-Right (The Concept of Terms) -->
    <g filter="url(#shadow)">
      <rect x="680" y="90" width="280" height="115" rx="14" fill="#ffffff" stroke="#0d9488" stroke-width="2" />
      <rect x="680" y="90" width="280" height="32" rx="14" fill="url(#gradB2)" />
      <text x="820" y="112" fill="#ffffff" font-size="13" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">2. THE NOTION OF TERMS (ପଦ)</text>
      <text x="695" y="140" fill="#334155" font-size="11" font-family="'Plus Jakarta Sans', sans-serif">• Parts separated STRICTLY by '+' signs</text>
      <text x="695" y="160" fill="#334155" font-size="11" font-family="'Plus Jakarta Sans', sans-serif">• Subtraction as Additive Inverse: a − b = a + (−b)</text>
      <text x="695" y="180" fill="#334155" font-size="11" font-family="'Plus Jakarta Sans', sans-serif">• Inside each term: × &amp; ÷ take precedence</text>
    </g>

    <!-- Branch 3: Middle-Left (Fundamental Laws of Addition) -->
    <g filter="url(#shadow)">
      <rect x="40" y="270" width="280" height="120" rx="14" fill="#ffffff" stroke="#7c3aed" stroke-width="2" />
      <rect x="40" y="270" width="280" height="32" rx="14" fill="url(#gradB3)" />
      <text x="180" y="292" fill="#ffffff" font-size="13" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">3. COMMUTATIVE &amp; ASSOCIATIVE LAWS</text>
      <text x="55" y="320" fill="#334155" font-size="11" font-family="'Plus Jakarta Sans', sans-serif">• Commutative: Term 1 + Term 2 = Term 2 + Term 1</text>
      <text x="55" y="340" fill="#334155" font-size="11" font-family="'Plus Jakarta Sans', sans-serif">• Associative: Grouping does not change sum</text>
      <text x="55" y="360" fill="#334155" font-size="11" font-family="'Plus Jakarta Sans', sans-serif">• Token Model Proof: Zero pairs cancel out</text>
      <text x="55" y="378" fill="#334155" font-size="11" font-family="'Plus Jakarta Sans', sans-serif">• Real-life: Shoes &amp; Hat vs Shoes &amp; Socks</text>
    </g>

    <!-- Branch 4: Middle-Right (Removing Brackets - Part I) -->
    <g filter="url(#shadow)">
      <rect x="680" y="270" width="280" height="120" rx="14" fill="#ffffff" stroke="#ea580c" stroke-width="2" />
      <rect x="680" y="270" width="280" height="32" rx="14" fill="url(#gradB4)" />
      <text x="820" y="292" fill="#ffffff" font-size="13" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">4. REMOVING BRACKETS (I)</text>
      <text x="695" y="320" fill="#334155" font-size="11" font-family="'Plus Jakarta Sans', sans-serif">• Preceded by '+': Signs REMAIN UNCHANGED</text>
      <text x="695" y="340" fill="#334155" font-size="11" font-family="'Plus Jakarta Sans', sans-serif">• Preceded by '−': ALL signs inside FLIP</text>
      <text x="695" y="360" fill="#334155" font-size="11" font-family="'Plus Jakarta Sans', sans-serif">• a − (b + c) = a − b − c (Irfan shopping bill)</text>
      <text x="695" y="378" fill="#334155" font-size="11" font-family="'Plus Jakarta Sans', sans-serif">• a − (b − c) = a − b + c (Excess deduction fix)</text>
    </g>

    <!-- Branch 5: Bottom-Left (The Distributive Property) -->
    <g filter="url(#shadow)">
      <rect x="40" y="450" width="280" height="120" rx="14" fill="#ffffff" stroke="#16a34a" stroke-width="2" />
      <rect x="40" y="450" width="280" height="32" rx="14" fill="url(#gradB5)" />
      <text x="180" y="472" fill="#ffffff" font-size="13" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">5. DISTRIBUTIVE PROPERTY (II)</text>
      <text x="55" y="500" fill="#334155" font-size="11" font-family="'Plus Jakarta Sans', sans-serif">• Over addition: a × (b + c) = a×b + a×c</text>
      <text x="55" y="520" fill="#334155" font-size="11" font-family="'Plus Jakarta Sans', sans-serif">• Over subtraction: a × (b − c) = a×b − a×c</text>
      <text x="55" y="540" fill="#334155" font-size="11" font-family="'Plus Jakarta Sans', sans-serif">• Mental Math: 97 × 25 = (100 − 3) × 25</text>
      <text x="55" y="558" fill="#334155" font-size="11" font-family="'Plus Jakarta Sans', sans-serif">• Area Model &amp; Parade Row Verification</text>
    </g>

    <!-- Branch 6: Bottom-Right (Order of Operations & Applications) -->
    <g filter="url(#shadow)">
      <rect x="680" y="450" width="280" height="120" rx="14" fill="#ffffff" stroke="#0369a1" stroke-width="2" />
      <rect x="680" y="450" width="280" height="32" rx="14" fill="url(#gradB1)" />
      <text x="820" y="472" fill="#ffffff" font-size="13" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">6. ORDER &amp; REAL-WORLD MODELS</text>
      <text x="695" y="500" fill="#334155" font-size="11" font-family="'Plus Jakarta Sans', sans-serif">• Syntax Trees: Leaf to root evaluation</text>
      <text x="695" y="520" fill="#334155" font-size="11" font-family="'Plus Jakarta Sans', sans-serif">• Problem Solving: Begur market, Metro fares</text>
      <text x="695" y="540" fill="#334155" font-size="11" font-family="'Plus Jakarta Sans', sans-serif">• Snail Post Dilemma (3cm up, 2cm slip)</text>
      <text x="695" y="558" fill="#334155" font-size="11" font-family="'Plus Jakarta Sans', sans-serif">• Expression Engineer: 4 fours puzzle</text>
    </g>

    <!-- Bottom Legend Banner -->
    <rect x="180" y="615" width="640" height="32" rx="8" fill="#e2e8f0" />
    <text x="500" y="636" fill="#475569" font-size="12" font-family="'Space Grotesk', sans-serif" font-weight="600" text-anchor="middle">CBSE Grade 7 • BSE Odisha (ଗଣିତ ପ୍ରକାଶ) • Competency-Based Educational Blueprint</text>
  </svg>
  <div class="diagram-caption"><i class="fa-solid fa-diagram-project"></i> Diagram 1: Complete Concept Architecture &amp; Mind Map for Chapter 2 (Arithmetic Expressions)</div>
</div>'''

def get_svg_terms():
    return '''<div class="svg-diagram-card">
  <svg viewBox="0 0 920 380" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Anatomy of an Arithmetic Expression and Decomposition into Terms">
    <defs>
      <linearGradient id="tGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0284c7" />
        <stop offset="100%" stop-color="#0369a1" />
      </linearGradient>
      <linearGradient id="tGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#ef4444" />
        <stop offset="100%" stop-color="#b91c1c" />
      </linearGradient>
      <linearGradient id="tGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#10b981" />
        <stop offset="100%" stop-color="#047857" />
      </linearGradient>
      <filter id="boxShadow" x="-5%" y="-5%" width="110%" height="110%">
        <feDropShadow dx="0" dy="3" stdDeviation="4" flood-opacity="0.1" />
      </filter>
    </defs>

    <rect width="920" height="380" rx="16" fill="#f8fafc" />

    <!-- Original Expression Title -->
    <text x="460" y="40" fill="#0f172a" font-size="17" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">ANATOMY OF AN ARITHMETIC EXPRESSION &amp; THE NOTION OF TERMS</text>
    <text x="460" y="65" fill="#64748b" font-size="13" font-family="'Plus Jakarta Sans', sans-serif" text-anchor="middle">Every arithmetic expression is converted into a sum of distinct terms separated by '+' signs</text>

    <!-- Raw Expression Display -->
    <rect x="220" y="85" width="480" height="50" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="2" />
    <text x="460" y="118" fill="#1e293b" font-size="22" font-family="'JetBrains Mono', monospace" font-weight="700" text-anchor="middle">28 − 2 × 6 + 16 ÷ 2</text>

    <!-- Step Arrow -->
    <path d="M 460 145 L 460 175" stroke="#64748b" stroke-width="3" stroke-linecap="round" />
    <polygon points="454,175 460,185 466,175" fill="#64748b" />
    <text x="585" y="165" fill="#475569" font-size="12" font-family="'Space Grotesk', sans-serif" font-weight="600">Rewrite subtraction as addition of inverse: a − b = a + (−b)</text>

    <!-- 3 Terms Display as Sum -->
    <!-- Term 1 -->
    <g filter="url(#boxShadow)">
      <rect x="120" y="200" width="180" height="85" rx="12" fill="#ffffff" stroke="#0284c7" stroke-width="2" />
      <rect x="120" y="200" width="180" height="26" rx="12" fill="url(#tGrad1)" />
      <text x="210" y="218" fill="#ffffff" font-size="12" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">TERM 1</text>
      <text x="210" y="252" fill="#0369a1" font-size="20" font-family="'JetBrains Mono', monospace" font-weight="700" text-anchor="middle">28</text>
      <text x="210" y="275" fill="#64748b" font-size="11" font-family="'Plus Jakarta Sans', sans-serif" text-anchor="middle">Single positive integer</text>
    </g>

    <!-- Plus Sign 1 -->
    <circle cx="350" cy="242" r="20" fill="#e2e8f0" />
    <text x="350" y="250" fill="#0f172a" font-size="24" font-family="'Space Grotesk', sans-serif" font-weight="800" text-anchor="middle">+</text>

    <!-- Term 2 -->
    <g filter="url(#boxShadow)">
      <rect x="390" y="200" width="200" height="85" rx="12" fill="#ffffff" stroke="#ef4444" stroke-width="2" />
      <rect x="390" y="200" width="200" height="26" rx="12" fill="url(#tGrad2)" />
      <text x="490" y="218" fill="#ffffff" font-size="12" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">TERM 2</text>
      <text x="490" y="252" fill="#b91c1c" font-size="20" font-family="'JetBrains Mono', monospace" font-weight="700" text-anchor="middle">−(2 × 6)</text>
      <text x="490" y="275" fill="#64748b" font-size="11" font-family="'Plus Jakarta Sans', sans-serif" text-anchor="middle">Evaluates first to −12</text>
    </g>

    <!-- Plus Sign 2 -->
    <circle cx="635" cy="242" r="20" fill="#e2e8f0" />
    <text x="635" y="250" fill="#0f172a" font-size="24" font-family="'Space Grotesk', sans-serif" font-weight="800" text-anchor="middle">+</text>

    <!-- Term 3 -->
    <g filter="url(#boxShadow)">
      <rect x="675" y="200" width="180" height="85" rx="12" fill="#ffffff" stroke="#10b981" stroke-width="2" />
      <rect x="675" y="200" width="180" height="26" rx="12" fill="url(#tGrad3)" />
      <text x="765" y="218" fill="#ffffff" font-size="12" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">TERM 3</text>
      <text x="765" y="252" fill="#047857" font-size="20" font-family="'JetBrains Mono', monospace" font-weight="700" text-anchor="middle">16 ÷ 2</text>
      <text x="765" y="275" fill="#64748b" font-size="11" font-family="'Plus Jakarta Sans', sans-serif" text-anchor="middle">Evaluates first to +8</text>
    </g>

    <!-- Final Evaluation Banner -->
    <rect x="180" y="315" width="560" height="45" rx="10" fill="#0f172a" />
    <text x="460" y="343" fill="#38bdf8" font-size="15" font-family="'JetBrains Mono', monospace" font-weight="700" text-anchor="middle">Sum of Terms: 28 + (−12) + 8 = 16 + 8 = 24</text>
  </svg>
  <div class="diagram-caption"><i class="fa-solid fa-cubes-stacked"></i> Diagram 2: Deconstructing an Arithmetic Expression into Distinct Terms Separated by Addition</div>
</div>'''

def get_svg_tokens():
    return '''<div class="svg-diagram-card">
  <svg viewBox="0 0 920 420" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Token Model of Integers and Commutative Associative Laws">
    <defs>
      <radialGradient id="posChip" cx="35%" cy="35%" r="65%">
        <stop offset="0%" stop-color="#60a5fa" />
        <stop offset="100%" stop-color="#1d4ed8" />
      </radialGradient>
      <radialGradient id="negChip" cx="35%" cy="35%" r="65%">
        <stop offset="0%" stop-color="#f87171" />
        <stop offset="100%" stop-color="#b91c1c" />
      </radialGradient>
    </defs>

    <rect width="920" height="420" rx="16" fill="#f8fafc" />

    <text x="460" y="35" fill="#0f172a" font-size="17" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">THE TOKEN MODEL: WHY SWAPPING &amp; GROUPING TERMS ALWAYS WORKS</text>
    <text x="460" y="58" fill="#64748b" font-size="13" font-family="'Plus Jakarta Sans', sans-serif" text-anchor="middle">Positive tokens (+1) and Negative tokens (−1) form zero-pairs and cancel out naturally</text>

    <!-- Left Box: Commutative Property -->
    <rect x="40" y="75" width="400" height="260" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
    <rect x="40" y="75" width="400" height="32" rx="12" fill="#0284c7" />
    <text x="240" y="97" fill="#ffffff" font-size="13" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">COMMUTATIVE LAW: 6 + (−4) = (−4) + 6</text>

    <!-- Order A -->
    <text x="65" y="135" fill="#0369a1" font-size="13" font-family="'Space Grotesk', sans-serif" font-weight="700">Order A: 6 positive tokens first, then 4 negative tokens</text>
    <!-- 6 Positives -->
    <g transform="translate(65, 145)">
      <circle cx="15" cy="15" r="12" fill="url(#posChip)" /><text x="15" y="20" fill="#fff" font-size="14" font-weight="700" text-anchor="middle">+</text>
      <circle cx="45" cy="15" r="12" fill="url(#posChip)" /><text x="45" y="20" fill="#fff" font-size="14" font-weight="700" text-anchor="middle">+</text>
      <circle cx="75" cy="15" r="12" fill="url(#posChip)" /><text x="75" y="20" fill="#fff" font-size="14" font-weight="700" text-anchor="middle">+</text>
      <circle cx="105" cy="15" r="12" fill="url(#posChip)" /><text x="105" y="20" fill="#fff" font-size="14" font-weight="700" text-anchor="middle">+</text>
      <circle cx="135" cy="15" r="12" fill="url(#posChip)" /><text x="135" y="20" fill="#fff" font-size="14" font-weight="700" text-anchor="middle">+</text>
      <circle cx="165" cy="15" r="12" fill="url(#posChip)" /><text x="165" y="20" fill="#fff" font-size="14" font-weight="700" text-anchor="middle">+</text>
      <!-- 4 Negatives below cancelling -->
      <circle cx="15" cy="45" r="12" fill="url(#negChip)" /><text x="15" y="50" fill="#fff" font-size="16" font-weight="700" text-anchor="middle">−</text>
      <circle cx="45" cy="45" r="12" fill="url(#negChip)" /><text x="45" y="50" fill="#fff" font-size="16" font-weight="700" text-anchor="middle">−</text>
      <circle cx="75" cy="45" r="12" fill="url(#negChip)" /><text x="75" y="50" fill="#fff" font-size="16" font-weight="700" text-anchor="middle">−</text>
      <circle cx="105" cy="45" r="12" fill="url(#negChip)" /><text x="105" y="50" fill="#fff" font-size="16" font-weight="700" text-anchor="middle">−</text>
      <!-- Cancellation rect -->
      <rect x="0" y="0" width="120" height="60" rx="8" fill="none" stroke="#ef4444" stroke-dasharray="4,3" stroke-width="1.5" />
      <text x="60" y="75" fill="#ef4444" font-size="11" font-weight="600" text-anchor="middle">4 Zero-Pairs (0)</text>
      <!-- Remaining -->
      <rect x="122" y="0" width="58" height="30" rx="6" fill="#dbeafe" stroke="#0284c7" stroke-width="1.5" />
      <text x="230" y="25" fill="#15803d" font-size="14" font-family="'JetBrains Mono', monospace" font-weight="700">Remainder = +2</text>
    </g>

    <!-- Order B Note -->
    <path d="M 60 250 L 420 250" stroke="#e2e8f0" stroke-width="1" />
    <text x="65" y="275" fill="#0369a1" font-size="13" font-family="'Space Grotesk', sans-serif" font-weight="700">Order B: 4 negative tokens first, then 6 positive tokens</text>
    <text x="65" y="300" fill="#475569" font-size="12" font-family="'Plus Jakarta Sans', sans-serif">The physical tokens in the bag are identical. Cancellation yields exactly the same net remainder of +2.</text>
    <text x="65" y="320" fill="#15803d" font-size="12" font-family="'JetBrains Mono', monospace" font-weight="700">⇒ Swapping terms preserves exact value!</text>

    <!-- Right Box: Associative Property -->
    <rect x="480" y="75" width="400" height="260" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
    <rect x="480" y="75" width="400" height="32" rx="12" fill="#7c3aed" />
    <text x="680" y="97" fill="#ffffff" font-size="13" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">ASSOCIATIVE LAW: (−7) + 10 + (−11)</text>

    <text x="505" y="135" fill="#6d28d9" font-size="13" font-family="'Space Grotesk', sans-serif" font-weight="700">Grouping Way 1: [ (−7) + 10 ] + (−11)</text>
    <text x="505" y="158" fill="#334155" font-size="12" font-family="'JetBrains Mono', monospace">• Step 1: −7 and +10 leave +3</text>
    <text x="505" y="178" fill="#334155" font-size="12" font-family="'JetBrains Mono', monospace">• Step 2: +3 and −11 leave −8</text>

    <path d="M 500 195 L 860 195" stroke="#e2e8f0" stroke-width="1" />

    <text x="505" y="225" fill="#6d28d9" font-size="13" font-family="'Space Grotesk', sans-serif" font-weight="700">Grouping Way 2: (−7) + [ 10 + (−11) ]</text>
    <text x="505" y="248" fill="#334155" font-size="12" font-family="'JetBrains Mono', monospace">• Step 1: +10 and −11 leave −1</text>
    <text x="505" y="268" fill="#334155" font-size="12" font-family="'JetBrains Mono', monospace">• Step 2: −7 and −1 leave −8</text>

    <rect x="505" y="290" width="350" height="34" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.5" />
    <text x="680" y="312" fill="#6d28d9" font-size="13" font-family="'JetBrains Mono', monospace" font-weight="700" text-anchor="middle">Both groupings evaluate to −8</text>

    <!-- Bottom Takeaway -->
    <rect x="40" y="355" width="840" height="45" rx="10" fill="#0f172a" />
    <text x="460" y="382" fill="#fde047" font-size="14" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">Core Principle: Terms can be rearranged and grouped in ANY order without altering the sum!</text>
  </svg>
  <div class="diagram-caption"><i class="fa-solid fa-circle-nodes"></i> Diagram 3: Concrete Physical Demonstration of Commutativity and Associativity via Token Models</div>
</div>'''

def get_svg_distributive():
    return '''<div class="svg-diagram-card">
  <svg viewBox="0 0 920 420" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Geometric Grid and Area Model of Distributive Property">
    <defs>
      <linearGradient id="scoutGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#38bdf8" />
        <stop offset="100%" stop-color="#0284c7" />
      </linearGradient>
      <linearGradient id="guideGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#4ade80" />
        <stop offset="100%" stop-color="#16a34a" />
      </linearGradient>
    </defs>

    <rect width="920" height="420" rx="16" fill="#f8fafc" />

    <text x="460" y="35" fill="#0f172a" font-size="17" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">GEOMETRIC PROOF: DISTRIBUTIVE PROPERTY OF MULTIPLICATION OVER ADDITION</text>
    <text x="460" y="58" fill="#64748b" font-size="13" font-family="'Plus Jakarta Sans', sans-serif" text-anchor="middle">Republic Day Parade Model: 5 rows with 4 Boy Scouts + 3 Girl Guides in each row</text>

    <!-- Outer Frame for Grid Area -->
    <!-- Scout Section: 5 rows x 4 cols -->
    <g transform="translate(100, 90)">
      <rect x="0" y="0" width="240" height="200" rx="8" fill="#e0f2fe" stroke="#0284c7" stroke-width="2" />
      <!-- Grid rows & cols -->
      <line x1="60" y1="0" x2="60" y2="200" stroke="#bae6fd" stroke-width="1.5" />
      <line x1="120" y1="0" x2="120" y2="200" stroke="#bae6fd" stroke-width="1.5" />
      <line x1="180" y1="0" x2="180" y2="200" stroke="#bae6fd" stroke-width="1.5" />
      <line x1="0" y1="40" x2="240" y2="40" stroke="#bae6fd" stroke-width="1.5" />
      <line x1="0" y1="80" x2="240" y2="80" stroke="#bae6fd" stroke-width="1.5" />
      <line x1="0" y1="120" x2="240" y2="120" stroke="#bae6fd" stroke-width="1.5" />
      <line x1="0" y1="160" x2="240" y2="160" stroke="#bae6fd" stroke-width="1.5" />
      <text x="120" y="105" fill="#0369a1" font-size="18" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">Boy Scouts</text>
      <text x="120" y="130" fill="#0284c7" font-size="14" font-family="'JetBrains Mono', monospace" font-weight="700" text-anchor="middle">4 × 5 = 20</text>
      <!-- Column width label -->
      <text x="120" y="-12" fill="#0369a1" font-size="14" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">4 columns</text>
    </g>

    <!-- Guide Section: 5 rows x 3 cols -->
    <g transform="translate(340, 90)">
      <rect x="0" y="0" width="180" height="200" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2" />
      <!-- Grid lines -->
      <line x1="60" y1="0" x2="60" y2="200" stroke="#bbf7d0" stroke-width="1.5" />
      <line x1="120" y1="0" x2="120" y2="200" stroke="#bbf7d0" stroke-width="1.5" />
      <line x1="0" y1="40" x2="180" y2="40" stroke="#bbf7d0" stroke-width="1.5" />
      <line x1="0" y1="80" x2="180" y2="80" stroke="#bbf7d0" stroke-width="1.5" />
      <line x1="0" y1="120" x2="180" y2="120" stroke="#bbf7d0" stroke-width="1.5" />
      <line x1="0" y1="160" x2="180" y2="160" stroke="#bbf7d0" stroke-width="1.5" />
      <text x="90" y="105" fill="#15803d" font-size="18" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">Girl Guides</text>
      <text x="90" y="130" fill="#16a34a" font-size="14" font-family="'JetBrains Mono', monospace" font-weight="700" text-anchor="middle">3 × 5 = 15</text>
      <!-- Column width label -->
      <text x="90" y="-12" fill="#15803d" font-size="14" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">3 columns</text>
    </g>

    <!-- Row Height Bracket / Label on Left -->
    <text x="65" y="195" fill="#0f172a" font-size="16" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">5 rows</text>
    <path d="M 85 90 L 85 290" stroke="#0f172a" stroke-width="2" />

    <!-- Total Width Bracket on Top -->
    <path d="M 100 68 L 520 68" stroke="#0f172a" stroke-width="2" />
    <text x="310" y="60" fill="#0f172a" font-size="14" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">Total Width = 4 + 3 = 7 columns</text>

    <!-- Right Side Mathematical Equivalences -->
    <g transform="translate(560, 95)">
      <rect x="0" y="0" width="320" height="195" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
      <text x="160" y="32" fill="#0f172a" font-size="14" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">TWO VIEWPOINTS, ONE TRUTH</text>
      
      <!-- Method 1 -->
      <rect x="15" y="48" width="290" height="52" rx="8" fill="#f0f9ff" stroke="#bae6fd" />
      <text x="25" y="68" fill="#0369a1" font-size="11" font-family="'Space Grotesk', sans-serif" font-weight="700">METHOD 1: Total Columns × Rows</text>
      <text x="25" y="88" fill="#0f172a" font-size="14" font-family="'JetBrains Mono', monospace" font-weight="700">(4 + 3) × 5 = 7 × 5 = 35</text>

      <!-- Method 2 -->
      <rect x="15" y="112" width="290" height="52" rx="8" fill="#f0fdf4" stroke="#bbf7d0" />
      <text x="25" y="132" fill="#15803d" font-size="11" font-family="'Space Grotesk', sans-serif" font-weight="700">METHOD 2: Scouts + Guides Separately</text>
      <text x="25" y="152" fill="#0f172a" font-size="14" font-family="'JetBrains Mono', monospace" font-weight="700">4 × 5 + 3 × 5 = 20 + 15 = 35</text>

      <text x="160" y="182" fill="#7c3aed" font-size="12" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">Therefore: (4 + 3) × 5 = 4 × 5 + 3 × 5</text>
    </g>

    <!-- Bottom Algebraic Law Box -->
    <rect x="60" y="320" width="800" height="75" rx="12" fill="#0f172a" />
    <text x="460" y="348" fill="#38bdf8" font-size="15" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">THE GENERAL DISTRIBUTIVE LAW (ବଣ୍ଟନ ନିୟମ)</text>
    <text x="460" y="375" fill="#f8fafc" font-size="16" font-family="'JetBrains Mono', monospace" font-weight="700" text-anchor="middle">a × (b + c) = a × b + a × c   AND   a × (b − c) = a × b − a × c</text>
  </svg>
  <div class="diagram-caption"><i class="fa-solid fa-shapes"></i> Diagram 4: Area Model Geometric Proof of the Distributive Law of Multiplication over Addition</div>
</div>'''

def get_svg_brackets():
    return '''<div class="svg-diagram-card">
  <svg viewBox="0 0 920 400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The Bracket Unpacking Machine and Sign Inversion Gate">
    <defs>
      <linearGradient id="gatePlus" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#10b981" />
        <stop offset="100%" stop-color="#047857" />
      </linearGradient>
      <linearGradient id="gateMinus" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#ef4444" />
        <stop offset="100%" stop-color="#b91c1c" />
      </linearGradient>
    </defs>

    <rect width="920" height="400" rx="16" fill="#f8fafc" />

    <text x="460" y="35" fill="#0f172a" font-size="17" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">THE BRACKET UNPACKING MACHINE: SIGN INVERSION RULES</text>
    <text x="460" y="58" fill="#64748b" font-size="13" font-family="'Plus Jakarta Sans', sans-serif" text-anchor="middle">How the preceding operator gate governs the signs of terms emerging from parentheses</text>

    <!-- CASE 1: Preceded by PLUS -->
    <g transform="translate(60, 85)">
      <rect x="0" y="0" width="380" height="235" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
      <!-- Header -->
      <rect x="0" y="0" width="380" height="32" rx="12" fill="url(#gatePlus)" />
      <text x="190" y="22" fill="#ffffff" font-size="13" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">CASE 1: PRECEEDED BY '+' (IDENTITY GATE)</text>

      <!-- Input Expression -->
      <text x="25" y="65" fill="#475569" font-size="12" font-family="'Space Grotesk', sans-serif" font-weight="600">Expression with Brackets:</text>
      <rect x="25" y="75" width="330" height="38" rx="8" fill="#f1f5f9" />
      <text x="190" y="100" fill="#0f172a" font-size="16" font-family="'JetBrains Mono', monospace" font-weight="700" text-anchor="middle">28 + (35 − 10)</text>

      <!-- Machine Gate -->
      <path d="M 190 115 L 190 140" stroke="#10b981" stroke-width="3" />
      <polygon points="184,140 190,148 196,140" fill="#10b981" />
      <text x="190" y="135" fill="#047857" font-size="10" font-weight="700" text-anchor="middle">GATE: NO CHANGE</text>

      <!-- Output Expression -->
      <text x="25" y="165" fill="#475569" font-size="12" font-family="'Space Grotesk', sans-serif" font-weight="600">Unpacked Form (Preserves Signs):</text>
      <rect x="25" y="175" width="330" height="38" rx="8" fill="#dcfce7" stroke="#86efac" />
      <text x="190" y="200" fill="#15803d" font-size="16" font-family="'JetBrains Mono', monospace" font-weight="700" text-anchor="middle">28 + 35 − 10 = 53</text>
    </g>

    <!-- CASE 2: Preceded by MINUS -->
    <g transform="translate(480, 85)">
      <rect x="0" y="0" width="380" height="235" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
      <!-- Header -->
      <rect x="0" y="0" width="380" height="32" rx="12" fill="url(#gateMinus)" />
      <text x="190" y="22" fill="#ffffff" font-size="13" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">CASE 2: PRECEEDED BY '−' (INVERTER GATE)</text>

      <!-- Input Expression -->
      <text x="25" y="65" fill="#475569" font-size="12" font-family="'Space Grotesk', sans-serif" font-weight="600">Subtracted Sum &amp; Difference:</text>
      <rect x="25" y="75" width="330" height="38" rx="8" fill="#f1f5f9" />
      <text x="190" y="100" fill="#0f172a" font-size="14" font-family="'JetBrains Mono', monospace" font-weight="700" text-anchor="middle">100 − (15 + 56)  &amp;  500 − (250 − 100)</text>

      <!-- Machine Gate -->
      <path d="M 190 115 L 190 140" stroke="#ef4444" stroke-width="3" />
      <polygon points="184,140 190,148 196,140" fill="#ef4444" />
      <text x="190" y="135" fill="#b91c1c" font-size="10" font-weight="700" text-anchor="middle">GATE: INVERTS ALL INTERNAL SIGNS</text>

      <!-- Output Expression -->
      <text x="25" y="165" fill="#475569" font-size="12" font-family="'Space Grotesk', sans-serif" font-weight="600">Unpacked Form (All Signs Flipped):</text>
      <rect x="25" y="175" width="330" height="42" rx="8" fill="#fee2e2" stroke="#fca5a5" />
      <text x="190" y="193" fill="#b91c1c" font-size="13" font-family="'JetBrains Mono', monospace" font-weight="700" text-anchor="middle">100 − 15 − 56 = 29</text>
      <text x="190" y="210" fill="#b91c1c" font-size="13" font-family="'JetBrains Mono', monospace" font-weight="700" text-anchor="middle">500 − 250 + 100 = 350</text>
    </g>

    <!-- Bottom Golden Rule -->
    <rect x="60" y="335" width="800" height="50" rx="10" fill="#0f172a" />
    <text x="460" y="365" fill="#fde047" font-size="14" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">Golden Law: When removing brackets preceded by '−', '+' becomes '−' and '−' becomes '+'!</text>
  </svg>
  <div class="diagram-caption"><i class="fa-solid fa-arrows-split-up-and-left"></i> Diagram 5: Algorithmic Logic of the Bracket Unpacking and Sign Inversion Mechanism</div>
</div>'''

def get_svg_tree():
    return '''<div class="svg-diagram-card">
  <svg viewBox="0 0 920 440" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Hierarchical Expression Tree and Order of Operations">
    <defs>
      <linearGradient id="rootGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0f172a" />
        <stop offset="100%" stop-color="#334155" />
      </linearGradient>
      <linearGradient id="nodeAdd" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0284c7" />
        <stop offset="100%" stop-color="#0369a1" />
      </linearGradient>
      <linearGradient id="nodeMul" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#7c3aed" />
        <stop offset="100%" stop-color="#6d28d9" />
      </linearGradient>
      <linearGradient id="nodeBracket" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#ea580c" />
        <stop offset="100%" stop-color="#c2410c" />
      </linearGradient>
      <linearGradient id="leafGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#ffffff" />
        <stop offset="100%" stop-color="#f1f5f9" />
      </linearGradient>
    </defs>

    <rect width="920" height="440" rx="16" fill="#f8fafc" />

    <text x="460" y="30" fill="#0f172a" font-size="17" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">HIERARCHICAL EXPRESSION TREE: ORDER OF OPERATIONS SYNTAX MODEL</text>
    <text x="460" y="52" fill="#64748b" font-size="13" font-family="'Plus Jakarta Sans', sans-serif" text-anchor="middle">Evaluating: 5 × (3 + 2) + 7 × 8 + 3 from bottom leaves up to the root</text>

    <!-- Branch Lines -->
    <!-- Root to Add1 and Term 3 -->
    <line x1="460" y1="80" x2="310" y2="150" stroke="#94a3b8" stroke-width="2.5" />
    <line x1="460" y1="80" x2="710" y2="150" stroke="#94a3b8" stroke-width="2.5" />

    <!-- Add1 to Mul1 and Mul2 -->
    <line x1="310" y1="150" x2="180" y2="230" stroke="#94a3b8" stroke-width="2.5" />
    <line x1="310" y1="150" x2="440" y2="230" stroke="#94a3b8" stroke-width="2.5" />

    <!-- Mul1 to 5 and (3+2) -->
    <line x1="180" y1="230" x2="110" y2="310" stroke="#94a3b8" stroke-width="2.5" />
    <line x1="180" y1="230" x2="250" y2="310" stroke="#94a3b8" stroke-width="2.5" />

    <!-- (3+2) to leaves 3 and 2 -->
    <line x1="250" y1="310" x2="210" y2="385" stroke="#94a3b8" stroke-width="2.5" />
    <line x1="250" y1="310" x2="290" y2="385" stroke="#94a3b8" stroke-width="2.5" />

    <!-- Mul2 to leaves 7 and 8 -->
    <line x1="440" y1="230" x2="390" y2="310" stroke="#94a3b8" stroke-width="2.5" />
    <line x1="440" y1="230" x2="490" y2="310" stroke="#94a3b8" stroke-width="2.5" />

    <!-- ROOT NODE (Final Addition) -->
    <circle cx="460" cy="80" r="32" fill="url(#rootGrad)" stroke="#38bdf8" stroke-width="2" />
    <text x="460" y="85" fill="#f8fafc" font-size="18" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">+</text>
    <text x="525" y="85" fill="#0f172a" font-size="13" font-family="'JetBrains Mono', monospace" font-weight="700">Val = 84</text>

    <!-- Intermediate ADD Node: (Term 1 + Term 2) -->
    <circle cx="310" cy="150" r="28" fill="url(#nodeAdd)" />
    <text x="310" y="156" fill="#fff" font-size="16" font-weight="700" text-anchor="middle">+</text>
    <text x="245" y="155" fill="#0369a1" font-size="12" font-family="'JetBrains Mono', monospace" font-weight="700">25+56=81</text>

    <!-- Term 3 Leaf: 3 -->
    <circle cx="710" cy="150" r="28" fill="url(#leafGrad)" stroke="#0284c7" stroke-width="2" />
    <text x="710" y="157" fill="#0f172a" font-size="16" font-family="'JetBrains Mono', monospace" font-weight="700" text-anchor="middle">3</text>
    <text x="710" y="195" fill="#64748b" font-size="11" font-weight="600" text-anchor="middle">Term 3 (+3)</text>

    <!-- MULTIPLY NODE 1: 5 × (3+2) -->
    <circle cx="180" cy="230" r="28" fill="url(#nodeMul)" />
    <text x="180" y="236" fill="#fff" font-size="16" font-weight="700" text-anchor="middle">×</text>
    <text x="120" y="235" fill="#6d28d9" font-size="12" font-family="'JetBrains Mono', monospace" font-weight="700">5×5=25</text>

    <!-- MULTIPLY NODE 2: 7 × 8 -->
    <circle cx="440" cy="230" r="28" fill="url(#nodeMul)" />
    <text x="440" y="236" fill="#fff" font-size="16" font-weight="700" text-anchor="middle">×</text>
    <text x="440" y="275" fill="#6d28d9" font-size="12" font-family="'JetBrains Mono', monospace" font-weight="700" text-anchor="middle">7×8 = 56</text>

    <!-- LEAF: 5 -->
    <circle cx="110" cy="310" r="24" fill="url(#leafGrad)" stroke="#7c3aed" stroke-width="2" />
    <text x="110" y="316" fill="#0f172a" font-size="15" font-family="'JetBrains Mono', monospace" font-weight="700" text-anchor="middle">5</text>

    <!-- INNER BRACKET NODE: (3 + 2) -->
    <circle cx="250" cy="310" r="26" fill="url(#nodeBracket)" />
    <text x="250" y="316" fill="#fff" font-size="16" font-weight="700" text-anchor="middle">+</text>
    <text x="305" y="315" fill="#ea580c" font-size="12" font-family="'JetBrains Mono', monospace" font-weight="700">3+2=5</text>

    <!-- LEAVES: 7 and 8 -->
    <circle cx="390" cy="310" r="24" fill="url(#leafGrad)" stroke="#7c3aed" stroke-width="2" />
    <text x="390" y="316" fill="#0f172a" font-size="15" font-family="'JetBrains Mono', monospace" font-weight="700" text-anchor="middle">7</text>

    <circle cx="490" cy="310" r="24" fill="url(#leafGrad)" stroke="#7c3aed" stroke-width="2" />
    <text x="490" y="316" fill="#0f172a" font-size="15" font-family="'JetBrains Mono', monospace" font-weight="700" text-anchor="middle">8</text>

    <!-- LEAVES OF BRACKET: 3 and 2 -->
    <circle cx="210" cy="385" r="22" fill="url(#leafGrad)" stroke="#ea580c" stroke-width="2" />
    <text x="210" y="391" fill="#0f172a" font-size="14" font-family="'JetBrains Mono', monospace" font-weight="700" text-anchor="middle">3</text>

    <circle cx="290" cy="385" r="22" fill="url(#leafGrad)" stroke="#ea580c" stroke-width="2" />
    <text x="290" y="391" fill="#0f172a" font-size="14" font-family="'JetBrains Mono', monospace" font-weight="700" text-anchor="middle">2</text>

    <!-- Step Evaluation Sequence on Right -->
    <g transform="translate(580, 240)">
      <rect x="0" y="0" width="310" height="175" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
      <text x="155" y="24" fill="#0f172a" font-size="13" font-family="'Space Grotesk', sans-serif" font-weight="700" text-anchor="middle">EVALUATION FLOW (BOTTOM-UP)</text>
      <text x="15" y="52" fill="#ea580c" font-size="12" font-family="'JetBrains Mono', monospace" font-weight="700">1. Parentheses: (3 + 2) = 5</text>
      <text x="15" y="80" fill="#6d28d9" font-size="12" font-family="'JetBrains Mono', monospace" font-weight="700">2. Term 1: 5 × 5 = 25</text>
      <text x="15" y="108" fill="#6d28d9" font-size="12" font-family="'JetBrains Mono', monospace" font-weight="700">3. Term 2: 7 × 8 = 56</text>
      <text x="15" y="136" fill="#0284c7" font-size="12" font-family="'JetBrains Mono', monospace" font-weight="700">4. Term 3: +3</text>
      <text x="15" y="162" fill="#15803d" font-size="12" font-family="'JetBrains Mono', monospace" font-weight="700">5. Sum: 25 + 56 + 3 = 84</text>
    </g>
  </svg>
  <div class="diagram-caption"><i class="fa-solid fa-network-wired"></i> Diagram 6: Syntax Tree Visualizing the Execution Priority from Inner Brackets to Term Multiplications to Root Addition</div>
</div>'''
