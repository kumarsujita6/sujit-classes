# -*- coding: utf-8 -*-
"""
Part 2: Section 1 - Visual Blueprint & Detailed Mind Map.
Includes two responsive inline SVGs:
1. Five Pillars of Universal Adult Franchise
2. Evolution of Voting: 10th-Century Kudavolai to 21st-Century EVM-VVPAT
Plus comprehensive 4-quadrant conceptual mind maps.
"""

PART2_CONTENT = '''
    <!-- ========================================== -->
    <!-- SECTION 1: VISUAL BLUEPRINT & MIND MAP    -->
    <!-- ========================================== -->
    <section class="section-block" id="section-1">
      <div class="section-header">
        <div class="section-title-wrap">
          <span class="section-tag"><i class="fa-solid fa-sitemap"></i> Master Blueprint</span>
          <h2 class="section-title">Section 1: Visual Blueprint & Detailed Mind Map</h2>
          <p class="section-desc">
            Get an instant bird\'s-eye view of India\'s democratic architecture: from the sacred moral power of a single vote to the multi-tiered institutional machinery that powers the world\'s largest elections.
          </p>
        </div>
      </div>

      <!-- SVG Diagram 1: Five Pillars of Universal Adult Franchise -->
      <div class="svg-diagram-card">
        <div class="svg-header">
          <div class="svg-caption">
            <i class="fa-solid fa-hand-holding-heart" style="color: #b45309;"></i>
            <span>Figure 5.A: The Five Fundamental Pillars of Universal Adult Franchise</span>
          </div>
          <span class="svg-tag">Conceptual Architecture</span>
        </div>
        <div class="svg-container">
          <svg viewBox="0 0 950 560" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background: #ffffff; font-family: 'Plus Jakarta Sans', sans-serif;">
            <defs>
              <linearGradient id="centerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#1e3a8a"/>
                <stop offset="100%" stop-color="#0f172a"/>
              </linearGradient>
              <linearGradient id="p1Grad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#fef3c7"/>
                <stop offset="100%" stop-color="#fde68a"/>
              </linearGradient>
              <linearGradient id="p2Grad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#dbeafe"/>
                <stop offset="100%" stop-color="#bfdbfe"/>
              </linearGradient>
              <linearGradient id="p3Grad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#d1fae5"/>
                <stop offset="100%" stop-color="#a7f3d0"/>
              </linearGradient>
              <linearGradient id="p4Grad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#fee2e2"/>
                <stop offset="100%" stop-color="#fecaca"/>
              </linearGradient>
              <linearGradient id="p5Grad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#ede9fe"/>
                <stop offset="100%" stop-color="#ddd6fe"/>
              </linearGradient>
              <filter id="cardShadow" x="-10%" y="-10%" width="120%" height="120%">
                <feDropShadow dx="0" dy="4" stdDeviation="4" flood-opacity="0.1"/>
              </filter>
            </defs>

            <!-- Connecting Background Radial Orbit Lines -->
            <circle cx="475" cy="280" r="195" fill="none" stroke="#e2e8f0" stroke-width="2" stroke-dasharray="6,6"/>

            <!-- Central Core Hub -->
            <circle cx="475" cy="280" r="95" fill="url(#centerGrad)" filter="url(#cardShadow)"/>
            <circle cx="475" cy="280" r="88" fill="none" stroke="#60a5fa" stroke-width="2" stroke-dasharray="4,4"/>
            <text x="475" y="258" text-anchor="middle" fill="#fbbf24" font-size="13" font-weight="800" letter-spacing="1">ARTICLE 326</text>
            <text x="475" y="278" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="800">UNIVERSAL</text>
            <text x="475" y="298" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="800">ADULT FRANCHISE</text>
            <text x="475" y="318" text-anchor="middle" fill="#93c5fd" font-size="11" font-weight="600">One Person • One Vote • One Value</text>

            <!-- Pillar 1: Top (Power to Determine Future) -->
            <path d="M 475 185 L 475 110" stroke="#b45309" stroke-width="3" stroke-linecap="round"/>
            <g transform="translate(325, 20)" filter="url(#cardShadow)">
              <rect width="300" height="88" rx="14" fill="url(#p1Grad)" stroke="#f59e0b" stroke-width="1.5"/>
              <circle cx="35" cy="44" r="22" fill="#b45309"/>
              <text x="35" y="50" text-anchor="middle" fill="#ffffff" font-size="18" font-weight="900">1</text>
              <text x="70" y="36" fill="#78350f" font-size="14" font-weight="800">Power to Determine Future</text>
              <text x="70" y="56" fill="#92400e" font-size="11.5" font-weight="500">Citizens choose policies, laws, and leaders</text>
              <text x="70" y="72" fill="#92400e" font-size="11" font-weight="500">to shape the nation\'s collective tomorrow.</text>
            </g>

            <!-- Pillar 2: Top Right (Absolute Human Equality) -->
            <path d="M 545 225 L 685 170" stroke="#1d4ed8" stroke-width="3" stroke-linecap="round"/>
            <g transform="translate(640, 120)" filter="url(#cardShadow)">
              <rect width="290" height="88" rx="14" fill="url(#p2Grad)" stroke="#3b82f6" stroke-width="1.5"/>
              <circle cx="35" cy="44" r="22" fill="#1d4ed8"/>
              <text x="35" y="50" text-anchor="middle" fill="#ffffff" font-size="18" font-weight="900">2</text>
              <text x="70" y="36" fill="#1e3a8a" font-size="14" font-weight="800">Strict Human Equality</text>
              <text x="70" y="56" fill="#1e40af" font-size="11.5" font-weight="500">Zero discrimination by caste, religion,</text>
              <text x="70" y="72" fill="#1e40af" font-size="11" font-weight="500">gender, education, wealth, or ethnicity.</text>
            </g>

            <!-- Pillar 3: Bottom Right (Every Voice Matters) -->
            <path d="M 545 335 L 685 390" stroke="#047857" stroke-width="3" stroke-linecap="round"/>
            <g transform="translate(640, 350)" filter="url(#cardShadow)">
              <rect width="290" height="88" rx="14" fill="url(#p3Grad)" stroke="#10b981" stroke-width="1.5"/>
              <circle cx="35" cy="44" r="22" fill="#047857"/>
              <text x="35" y="50" text-anchor="middle" fill="#ffffff" font-size="18" font-weight="900">3</text>
              <text x="70" y="36" fill="#064e3b" font-size="14" font-weight="800">Every Voice Counts Equally</text>
              <text x="70" y="56" fill="#065f46" font-size="11.5" font-weight="500">The vote of a daily laborer has the</text>
              <text x="70" y="72" fill="#065f46" font-size="11" font-weight="500">exact same weight as that of a billionaire.</text>
            </g>

            <!-- Pillar 4: Bottom Left (Elected Accountability) -->
            <path d="M 405 335 L 265 390" stroke="#be123c" stroke-width="3" stroke-linecap="round"/>
            <g transform="translate(20, 350)" filter="url(#cardShadow)">
              <rect width="290" height="88" rx="14" fill="url(#p4Grad)" stroke="#f43f5e" stroke-width="1.5"/>
              <circle cx="35" cy="44" r="22" fill="#be123c"/>
              <text x="35" y="50" text-anchor="middle" fill="#ffffff" font-size="18" font-weight="900">4</text>
              <text x="70" y="36" fill="#881337" font-size="14" font-weight="800">Answerable Representatives</text>
              <text x="70" y="56" fill="#9f1239" font-size="11.5" font-weight="500">Leaders must return every 5 years to the</text>
              <text x="70" y="72" fill="#9f1239" font-size="11" font-weight="500">people; non-performers are voted out.</text>
            </g>

            <!-- Pillar 5: Top Left (Active Civic Engagement) -->
            <path d="M 405 225 L 265 170" stroke="#6d28d9" stroke-width="3" stroke-linecap="round"/>
            <g transform="translate(20, 120)" filter="url(#cardShadow)">
              <rect width="290" height="88" rx="14" fill="url(#p5Grad)" stroke="#8b5cf6" stroke-width="1.5"/>
              <circle cx="35" cy="44" r="22" fill="#6d28d9"/>
              <text x="35" y="50" text-anchor="middle" fill="#ffffff" font-size="18" font-weight="900">5</text>
              <text x="70" y="36" fill="#4c1d95" font-size="14" font-weight="800">Fosters Civic Engagement</text>
              <text x="70" y="56" fill="#5b21b6" font-size="11.5" font-weight="500">Encourages communities to solve local</text>
              <text x="70" y="72" fill="#5b21b6" font-size="11" font-weight="500">problems, debate laws, and demand justice.</text>
            </g>

            <!-- Bottom Emblem / Footer Tag -->
            <rect x="330" y="490" width="290" height="40" rx="20" fill="#f1f5f9" stroke="#cbd5e1"/>
            <text x="475" y="515" text-anchor="middle" fill="#475569" font-size="12" font-weight="700">61st Amendment Act, 1988: Voting Age = 18 Years</text>
          </svg>
        </div>
      </div>

      <!-- SVG Diagram 2: Kudavolai vs Modern EVM-VVPAT System -->
      <div class="svg-diagram-card">
        <div class="svg-header">
          <div class="svg-caption">
            <i class="fa-solid fa-code-compare" style="color: #047857;"></i>
            <span>Figure 5.B: Evolution of Voting Systems: 10th-Century Kudavolai to 21st-Century EVM + VVPAT</span>
          </div>
          <span class="svg-tag">Historical Continuity</span>
        </div>
        <div class="svg-container">
          <svg viewBox="0 0 950 480" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background: #ffffff; font-family: 'Plus Jakarta Sans', sans-serif;">
            <defs>
              <linearGradient id="cholaGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#fffbeb"/>
                <stop offset="100%" stop-color="#fef3c7"/>
              </linearGradient>
              <linearGradient id="modernGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#eff6ff"/>
                <stop offset="100%" stop-color="#dbeafe"/>
              </linearGradient>
            </defs>

            <!-- Center Divider Line -->
            <line x1="475" y1="30" x2="475" y2="440" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="6,6"/>
            <circle cx="475" cy="235" r="28" fill="#ffffff" stroke="#94a3b8" stroke-width="2"/>
            <text x="475" y="241" text-anchor="middle" fill="#475569" font-size="13" font-weight="800">VS</text>

            <!-- LEFT SIDE: 10th Century Chola Kudavolai System -->
            <g transform="translate(30, 30)">
              <rect width="415" height="410" rx="16" fill="url(#cholaGrad)" stroke="#fde68a" stroke-width="1.5"/>
              <rect x="20" y="20" width="375" height="42" rx="8" fill="#b45309"/>
              <text x="207" y="47" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="800">10TH CENTURY: UTTARAMERUR (CHOLA)</text>

              <!-- Step 1 Palm Leaf -->
              <rect x="25" y="80" width="365" height="60" rx="8" fill="#ffffff" stroke="#f59e0b"/>
              <circle cx="50" cy="110" r="14" fill="#fef3c7" stroke="#b45309"/>
              <text x="50" y="115" text-anchor="middle" fill="#b45309" font-size="12" font-weight="800">1</text>
              <text x="75" y="103" fill="#78350f" font-size="12.5" font-weight="700">Palm Leaf Slips (Kudavolai)</text>
              <text x="75" y="123" fill="#92400e" font-size="11" font-weight="500">Names of eligible candidates written on dried palm leaves.</text>

              <!-- Step 2 Earthen Pot -->
              <rect x="25" y="155" width="365" height="60" rx="8" fill="#ffffff" stroke="#f59e0b"/>
              <circle cx="50" cy="185" r="14" fill="#fef3c7" stroke="#b45309"/>
              <text x="50" y="190" text-anchor="middle" fill="#b45309" font-size="12" font-weight="800">2</text>
              <text x="75" y="178" fill="#78350f" font-size="12.5" font-weight="700">Sealed Mud Pot (Kuda)</text>
              <text x="75" y="198" fill="#92400e" font-size="11" font-weight="500">All slips mixed inside an earthen pot before village assembly.</text>

              <!-- Step 3 Innocent Child -->
              <rect x="25" y="230" width="365" height="60" rx="8" fill="#ffffff" stroke="#f59e0b"/>
              <circle cx="50" cy="260" r="14" fill="#fef3c7" stroke="#b45309"/>
              <text x="50" y="265" text-anchor="middle" fill="#b45309" font-size="12" font-weight="800">3</text>
              <text x="75" y="253" fill="#78350f" font-size="12.5" font-weight="700">Unbiased Random Draw</text>
              <text x="75" y="273" fill="#92400e" font-size="11" font-weight="500">A young child picks slips one by one without prejudice.</text>

              <!-- Step 4 Public Reading -->
              <rect x="25" y="305" width="365" height="70" rx="8" fill="#ffffff" stroke="#f59e0b"/>
              <circle cx="50" cy="340" r="14" fill="#fef3c7" stroke="#b45309"/>
              <text x="50" y="345" text-anchor="middle" fill="#b45309" font-size="12" font-weight="800">4</text>
              <text x="75" y="328" fill="#78350f" font-size="12.5" font-weight="700">Public Reading with Empty Hands</text>
              <text x="75" y="348" fill="#92400e" font-size="11" font-weight="500">Officer shows open hands to all villagers before reading,</text>
              <text x="75" y="363" fill="#92400e" font-size="11" font-weight="500">guaranteeing 100% public transparency.</text>
            </g>

            <!-- RIGHT SIDE: Modern 21st Century EVM + VVPAT -->
            <g transform="translate(505, 30)">
              <rect width="415" height="410" rx="16" fill="url(#modernGrad)" stroke="#bfdbfe" stroke-width="1.5"/>
              <rect x="20" y="20" width="375" height="42" rx="8" fill="#1e3a8a"/>
              <text x="207" y="47" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="800">21ST CENTURY: MODERN EVM + VVPAT</text>

              <!-- Step 1 Secret Compartment -->
              <rect x="25" y="80" width="365" height="60" rx="8" fill="#ffffff" stroke="#3b82f6"/>
              <circle cx="50" cy="110" r="14" fill="#eff6ff" stroke="#1d4ed8"/>
              <text x="50" y="115" text-anchor="middle" fill="#1d4ed8" font-size="12" font-weight="800">1</text>
              <text x="75" y="103" fill="#1e3a8a" font-size="12.5" font-weight="700">Secret Voting Compartment</text>
              <text x="75" y="123" fill="#1e40af" font-size="11" font-weight="500">Total privacy guarantees complete freedom from fear.</text>

              <!-- Step 2 Press Blue Button -->
              <rect x="25" y="155" width="365" height="60" rx="8" fill="#ffffff" stroke="#3b82f6"/>
              <circle cx="50" cy="185" r="14" fill="#eff6ff" stroke="#1d4ed8"/>
              <text x="50" y="190" text-anchor="middle" fill="#1d4ed8" font-size="12" font-weight="800">2</text>
              <text x="75" y="178" fill="#1e3a8a" font-size="12.5" font-weight="700">Ballot Unit (EVM)</text>
              <text x="75" y="198" fill="#1e40af" font-size="11" font-weight="500">Voter presses blue button next to candidate name/symbol.</text>

              <!-- Step 3 7-Second VVPAT Slip -->
              <rect x="25" y="230" width="365" height="60" rx="8" fill="#ffffff" stroke="#3b82f6"/>
              <circle cx="50" cy="260" r="14" fill="#eff6ff" stroke="#1d4ed8"/>
              <text x="50" y="265" text-anchor="middle" fill="#1d4ed8" font-size="12" font-weight="800">3</text>
              <text x="75" y="253" fill="#1e3a8a" font-size="12.5" font-weight="700">7-Second VVPAT Verification</text>
              <text x="75" y="273" fill="#1e40af" font-size="11" font-weight="500">Screen displays paper slip verifying vote, then drops in box.</text>

              <!-- Step 4 Audio Beep & Zero Tampering -->
              <rect x="25" y="305" width="365" height="70" rx="8" fill="#ffffff" stroke="#3b82f6"/>
              <circle cx="50" cy="340" r="14" fill="#eff6ff" stroke="#1d4ed8"/>
              <text x="50" y="345" text-anchor="middle" fill="#1d4ed8" font-size="12" font-weight="800">4</text>
              <text x="75" y="328" fill="#1e3a8a" font-size="12.5" font-weight="700">Loud Beep & Tamper-Proof Audit</text>
              <text x="75" y="348" fill="#1e40af" font-size="11" font-weight="500">Standalone offline computer chips prevent hacking;</text>
              <text x="75" y="363" fill="#1e40af" font-size="11" font-weight="500">VVPAT paper slips offer 100% recount verification.</text>
            </g>
          </svg>
        </div>
      </div>

      <!-- High-Yield 4-Quadrant Mind Map Breakdown -->
      <h3 class="subsection-title">
        <i class="fa-solid fa-compass" style="color: #1e3a8a;"></i>
        The Four Thematic Quadrants of India\'s Electoral Architecture
      </h3>
      <p>
        To master this chapter effortlessly for CBSE Class 8 examinations and competitive foundations, think of India\'s electoral framework as four interlocking pillars:
      </p>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.25rem; margin: 1.5rem 0;">
        <!-- Quadrant 1 -->
        <div style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-top: 4px solid #1e3a8a; border-radius: 12px; padding: 1.25rem;">
          <h4 style="color: #1e3a8a; font-size: 1.05rem; margin-bottom: 0.5rem; font-family: 'Space Grotesk', sans-serif;">
            <i class="fa-solid fa-scale-balanced"></i> Q1: Constitutional Foundations
          </h4>
          <ul style="font-size: 0.88rem; padding-left: 1.2rem; color: #475569; margin: 0;">
            <li><strong>Article 326:</strong> Universal Adult Franchise granted to all citizens.</li>
            <li><strong>61st Amendment (1988):</strong> Voting age lowered from 21 to 18 years.</li>
            <li><strong>Ambedkar\'s Vision:</strong> "One person, one vote, one value" eliminates feudal hierarchies.</li>
            <li><strong>Global Contrast:</strong> India gave women equal voting in 1950; Switzerland lagged till 1971.</li>
          </ul>
        </div>

        <!-- Quadrant 2 -->
        <div style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-top: 4px solid #b45309; border-radius: 12px; padding: 1.25rem;">
          <h4 style="color: #b45309; font-size: 1.05rem; margin-bottom: 0.5rem; font-family: 'Space Grotesk', sans-serif;">
            <i class="fa-solid fa-landmark"></i> Q2: Institutional Machinery
          </h4>
          <ul style="font-size: 0.88rem; padding-left: 1.2rem; color: #475569; margin: 0;">
            <li><strong>Article 324:</strong> Election Commission of India (ECI) at <em>Nirvachan Sadan</em>.</li>
            <li><strong>Leadership:</strong> Chief Election Commissioner (CEC) + 2 Election Commissioners.</li>
            <li><strong>Field Chain:</strong> CEO (State) → DEO (District) → RO (Constituency) → BLO (Booth).</li>
            <li><strong>State Election Commissions:</strong> Independent bodies managing Gram Panchayats & Municipalities.</li>
          </ul>
        </div>

        <!-- Quadrant 3 -->
        <div style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-top: 4px solid #047857; border-radius: 12px; padding: 1.25rem;">
          <h4 style="color: #047857; font-size: 1.05rem; margin-bottom: 0.5rem; font-family: 'Space Grotesk', sans-serif;">
            <i class="fa-solid fa-users-viewfinder"></i> Q3: Representation Systems
          </h4>
          <ul style="font-size: 0.88rem; padding-left: 1.2rem; color: #475569; margin: 0;">
            <li><strong>Direct Elections:</strong> Lok Sabha (543 MPs) & Vidhan Sabha (MLAs) via First-Past-The-Post.</li>
            <li><strong>Indirect Elections:</strong> Rajya Sabha (233 elected MLAs + 12 nominated) & President of India.</li>
            <li><strong>Affirmative Action:</strong> 84 SC and 47 ST reserved Lok Sabha constituencies.</li>
            <li><strong>Secret Ballot:</strong> Total voter confidentiality prevents coercion and intimidation.</li>
          </ul>
        </div>

        <!-- Quadrant 4 -->
        <div style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-top: 4px solid #be123c; border-radius: 12px; padding: 1.25rem;">
          <h4 style="color: #be123c; font-size: 1.05rem; margin-bottom: 0.5rem; font-family: 'Space Grotesk', sans-serif;">
            <i class="fa-solid fa-shield-virus"></i> Q4: Ethical Integrity & Reforms
          </h4>
          <ul style="font-size: 0.88rem; padding-left: 1.2rem; color: #475569; margin: 0;">
            <li><strong>Model Code of Conduct (MCC):</strong> Voluntary 1960 Kerala model made national standard.</li>
            <li><strong>T.N. Seshan Era:</strong> Enforced EPIC voter IDs, banned muscle power, capped spending.</li>
            <li><strong>EVM + VVPAT:</strong> High-tech electronic voting eliminating invalid votes and paper waste.</li>
            <li><strong>Vigilant Citizenship:</strong> Tackling urban apathy (34% non-voters in 2024), NOTA, and C-VIGIL app.</li>
          </ul>
        </div>
      </div>
    </section>
'''
