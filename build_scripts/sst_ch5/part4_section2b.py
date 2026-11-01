# -*- coding: utf-8 -*-
"""
Part 4: Section 2B - Deep Conceptual Analysis (Concepts 6 to 11),
Four Responsive Inline SVGs (SVGs 3, 4, 5, 6), and
Exhaustive 30-Term English-Odia Bilingual Glossary Table.
"""

PART4_CONTENT = '''
      <!-- CONCEPT 6 -->
      <h3 class="subsection-title" id="concept-6">
        <i class="fa-solid fa-building-flag" style="color: #1e3a8a;"></i>
        6. The Election Commission of India (ECI): Structure, Autonomy, and Duties
      </h3>

      <p>
        Conducting an election for nearly a billion people across millions of square kilometers is one of the most complex organizational feats on planet Earth. To ensure that the government of the day cannot rig or manipulate elections, our Constitution created an <strong>independent constitutional powerhouse</strong>: the <strong>Election Commission of India (ECI)</strong>.
      </p>

      <div class="callout-box callout-def">
        <div class="callout-title">
          <i class="fa-solid fa-scale-balanced"></i> Article 324: The Constitutional Shield of ECI
        </div>
        <p>
          Under <strong>Article 324</strong> of the Constitution of India, the superintendence, direction, and control of the preparation of electoral rolls and the conduct of all elections to Parliament, State Legislatures, and the offices of the President and Vice-President are vested entirely in the <strong>Election Commission of India</strong>.
        </p>
        <p>
          The ECI does <em>not</em> report to the Prime Minister, the Home Ministry, or any political party. Its autonomy is safeguarded just like the Supreme Court of India!
        </p>
      </div>

      <h4 class="topic-title">National Headquarters & Core Leadership:</h4>
      <p>
        The ECI operates from its majestic headquarters named <strong>Nirvachan Sadan</strong> on Ashoka Road, New Delhi. It is headed by the <strong>Chief Election Commissioner (CEC)</strong> along with <strong>two Election Commissioners</strong>. Decisions are taken collaboratively, and the commissioners enjoy high constitutional protection to ensure they remain completely impartial and fearless.
      </p>

      <!-- SVG Diagram 3: ECI Hierarchical Pyramid Structure -->
      <div class="svg-diagram-card">
        <div class="svg-header">
          <div class="svg-caption">
            <i class="fa-solid fa-network-wired" style="color: #1e3a8a;"></i>
            <span>Figure 5.C: Hierarchical Chain of Election Administration in India</span>
          </div>
          <span class="svg-tag">Administrative Chain</span>
        </div>
        <div class="svg-container">
          <svg viewBox="0 0 950 500" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background: #ffffff; font-family: 'Plus Jakarta Sans', sans-serif;">
            <defs>
              <linearGradient id="pyr1" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#1e3a8a"/>
                <stop offset="100%" stop-color="#2563eb"/>
              </linearGradient>
              <linearGradient id="pyr2" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#047857"/>
                <stop offset="100%" stop-color="#10b981"/>
              </linearGradient>
              <linearGradient id="pyr3" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#b45309"/>
                <stop offset="100%" stop-color="#f59e0b"/>
              </linearGradient>
              <linearGradient id="pyr4" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#6d28d9"/>
                <stop offset="100%" stop-color="#8b5cf6"/>
              </linearGradient>
              <linearGradient id="pyr5" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#be123c"/>
                <stop offset="100%" stop-color="#f43f5e"/>
              </linearGradient>
            </defs>

            <!-- Tier 1: National Level -->
            <g transform="translate(175, 20)">
              <rect width="600" height="70" rx="12" fill="url(#pyr1)"/>
              <text x="300" y="32" text-anchor="middle" fill="#fbbf24" font-size="12" font-weight="800" letter-spacing="1">NATIONAL LEVEL • NIRVACHAN SADAN, NEW DELHI</text>
              <text x="300" y="55" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="800">Chief Election Commissioner (CEC) + 2 Election Commissioners</text>
            </g>
            <line x1="475" y1="90" x2="475" y2="115" stroke="#94a3b8" stroke-width="3" stroke-dasharray="4,4"/>

            <!-- Tier 2: State / UT Level -->
            <g transform="translate(135, 115)">
              <rect width="680" height="70" rx="12" fill="url(#pyr2)"/>
              <text x="340" y="32" text-anchor="middle" fill="#d1fae5" font-size="12" font-weight="800" letter-spacing="1">STATE & UNION TERRITORY LEVEL</text>
              <text x="340" y="55" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="800">Chief Electoral Officer (CEO) — High Senior IAS Officer</text>
            </g>
            <line x1="475" y1="185" x2="475" y2="210" stroke="#94a3b8" stroke-width="3" stroke-dasharray="4,4"/>

            <!-- Tier 3: District Level -->
            <g transform="translate(95, 210)">
              <rect width="760" height="70" rx="12" fill="url(#pyr3)"/>
              <text x="380" y="32" text-anchor="middle" fill="#fef3c7" font-size="12" font-weight="800" letter-spacing="1">DISTRICT LEVEL</text>
              <text x="380" y="55" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="800">District Election Officer (DEO) — District Magistrate / Collector</text>
            </g>
            <line x1="475" y1="280" x2="475" y2="305" stroke="#94a3b8" stroke-width="3" stroke-dasharray="4,4"/>

            <!-- Tier 4: Constituency Level -->
            <g transform="translate(55, 305)">
              <rect width="840" height="70" rx="12" fill="url(#pyr4)"/>
              <text x="420" y="32" text-anchor="middle" fill="#ede9fe" font-size="12" font-weight="800" letter-spacing="1">CONSTITUENCY LEVEL (543 PARLIAMENTARY / 4000+ ASSEMBLY)</text>
              <text x="420" y="55" text-anchor="middle" fill="#ffffff" font-size="15" font-weight="800">Returning Officer (RO — Conducts Polls) & Electoral Registration Officer (ERO — Voter List)</text>
            </g>
            <line x1="475" y1="375" x2="475" y2="400" stroke="#94a3b8" stroke-width="3" stroke-dasharray="4,4"/>

            <!-- Tier 5: Polling Station / Booth Level -->
            <g transform="translate(15, 400)">
              <rect width="920" height="75" rx="12" fill="url(#pyr5)"/>
              <text x="460" y="30" text-anchor="middle" fill="#ffe4e6" font-size="12" font-weight="800" letter-spacing="1">POLLING BOOTH LEVEL (OVER 1,000,000 POLLING STATIONS NATIONWIDE)</text>
              <text x="460" y="54" text-anchor="middle" fill="#ffffff" font-size="14.5" font-weight="800">Presiding Officer • 1st, 2nd, 3rd Polling Officers • Booth Level Officers (BLOs)</text>
              <text x="460" y="68" text-anchor="middle" fill="#ffe4e6" font-size="11" font-weight="600">School Teachers, Bank Staff & Govt Employees temporarily deputed under ECI command</text>
            </g>
          </svg>
        </div>
      </div>

      <div class="callout-box callout-warn">
        <div class="callout-title">
          <i class="fa-solid fa-triangle-exclamation"></i> Big Exam Distinction: ECI vs State Election Commissions (SECs)
        </div>
        <p>
          Students frequently get confused between the <strong>Election Commission of India (ECI)</strong> and <strong>State Election Commissions (SECs)</strong>. Remember this vital distinction:
        </p>
        <ul>
          <li><strong>ECI (Article 324):</strong> Organizes and conducts elections for the <strong>Lok Sabha, Rajya Sabha, State Legislative Assemblies (Vidhan Sabha), State Legislative Councils (Vidhan Parishad), President, and Vice-President</strong>.</li>
          <li><strong>State Election Commissions (Articles 243K & 243ZA):</strong> Completely independent constitutional bodies that conduct local grassroots elections for <strong>Gram Panchayats, Panchayat Samitis, Zilla Parishads, Municipalities, and Municipal Corporations</strong>. The ECI does not directly conduct village panchayat polls!</li>
        </ul>
      </div>

      <!-- CONCEPT 7 -->
      <h3 class="subsection-title" id="concept-7">
        <i class="fa-solid fa-fingerprint" style="color: #047857;"></i>
        7. Inside the Polling Station: The 4-Step Polling Journey & Technology
      </h3>

      <p>
        On voting day, a school classroom, community center, or village hall is converted into a fortified, fair <strong>Polling Station</strong>. Every station is manned by an impartial team of government servants and school teachers.
      </p>

      <!-- SVG Diagram 4: 4-Step Polling Station Workflow -->
      <div class="svg-diagram-card">
        <div class="svg-header">
          <div class="svg-caption">
            <i class="fa-solid fa-person-booth" style="color: #047857;"></i>
            <span>Figure 5.D: Inside the Polling Station: The 4-Step Journey of an Indian Voter</span>
          </div>
          <span class="svg-tag">Polling Procedure</span>
        </div>
        <div class="svg-container">
          <svg viewBox="0 0 950 420" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background: #ffffff; font-family: 'Plus Jakarta Sans', sans-serif;">
            <defs>
              <linearGradient id="stepGrad1" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#eff6ff"/>
                <stop offset="100%" stop-color="#dbeafe"/>
              </linearGradient>
              <linearGradient id="stepGrad2" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#fef3c7"/>
                <stop offset="100%" stop-color="#fde68a"/>
              </linearGradient>
              <linearGradient id="stepGrad3" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#f0fdf4"/>
                <stop offset="100%" stop-color="#dcfce7"/>
              </linearGradient>
              <linearGradient id="stepGrad4" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#fdf2f8"/>
                <stop offset="100%" stop-color="#fce7f3"/>
              </linearGradient>
            </defs>

            <!-- Flow Connecting Arrow Lines -->
            <path d="M 230 190 L 260 190" stroke="#94a3b8" stroke-width="3" marker-end="url(#arrow)"/>
            <path d="M 470 190 L 500 190" stroke="#94a3b8" stroke-width="3"/>
            <path d="M 710 190 L 740 190" stroke="#94a3b8" stroke-width="3"/>

            <!-- STEP 1 -->
            <g transform="translate(20, 40)">
              <rect width="210" height="320" rx="14" fill="url(#stepGrad1)" stroke="#3b82f6" stroke-width="1.5"/>
              <rect x="15" y="15" width="180" height="36" rx="8" fill="#1e3a8a"/>
              <text x="105" y="38" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="800">1ST POLLING OFFICER</text>
              <circle cx="105" cy="95" r="30" fill="#ffffff" stroke="#3b82f6" stroke-width="2"/>
              <text x="105" y="103" text-anchor="middle" fill="#1d4ed8" font-size="22" font-weight="900">1</text>
              <text x="105" y="155" text-anchor="middle" fill="#1e3a8a" font-size="13.5" font-weight="800">Identity Verification</text>
              <text x="105" y="185" text-anchor="middle" fill="#334155" font-size="11.5" font-weight="600">Checks voter\'s name</text>
              <text x="105" y="205" text-anchor="middle" fill="#334155" font-size="11.5" font-weight="600">against official electoral</text>
              <text x="105" y="225" text-anchor="middle" fill="#334155" font-size="11.5" font-weight="600">roll and verifies EPIC card</text>
              <text x="105" y="245" text-anchor="middle" fill="#334155" font-size="11.5" font-weight="600">or approved photo ID.</text>
              <rect x="25" y="270" width="160" height="30" rx="6" fill="#ffffff"/>
              <text x="105" y="290" text-anchor="middle" fill="#1d4ed8" font-size="11" font-weight="700">Calls name aloud</text>
            </g>

            <!-- STEP 2 -->
            <g transform="translate(260, 40)">
              <rect width="210" height="320" rx="14" fill="url(#stepGrad2)" stroke="#f59e0b" stroke-width="1.5"/>
              <rect x="15" y="15" width="180" height="36" rx="8" fill="#b45309"/>
              <text x="105" y="38" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="800">2ND POLLING OFFICER</text>
              <circle cx="105" cy="95" r="30" fill="#ffffff" stroke="#f59e0b" stroke-width="2"/>
              <text x="105" y="103" text-anchor="middle" fill="#b45309" font-size="22" font-weight="900">2</text>
              <text x="105" y="155" text-anchor="middle" fill="#78350f" font-size="13.5" font-weight="800">Ink & Register</text>
              <text x="105" y="185" text-anchor="middle" fill="#334155" font-size="11.5" font-weight="600">Applies indelible ink</text>
              <text x="105" y="205" text-anchor="middle" fill="#334155" font-size="11.5" font-weight="600">on left index fingernail.</text>
              <text x="105" y="225" text-anchor="middle" fill="#334155" font-size="11.5" font-weight="600">Records signature in</text>
              <text x="105" y="245" text-anchor="middle" fill="#334155" font-size="11.5" font-weight="600">Form 17A register & issues slip.</text>
              <rect x="25" y="270" width="160" height="30" rx="6" fill="#ffffff"/>
              <text x="105" y="290" text-anchor="middle" fill="#b45309" font-size="11" font-weight="700">Silver Nitrate Ink</text>
            </g>

            <!-- STEP 3 -->
            <g transform="translate(500, 40)">
              <rect width="210" height="320" rx="14" fill="url(#stepGrad3)" stroke="#10b981" stroke-width="1.5"/>
              <rect x="15" y="15" width="180" height="36" rx="8" fill="#047857"/>
              <text x="105" y="38" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="800">3RD POLLING OFFICER</text>
              <circle cx="105" cy="95" r="30" fill="#ffffff" stroke="#10b981" stroke-width="2"/>
              <text x="105" y="103" text-anchor="middle" fill="#047857" font-size="22" font-weight="900">3</text>
              <text x="105" y="155" text-anchor="middle" fill="#064e3b" font-size="13.5" font-weight="800">Control & Activation</text>
              <text x="105" y="185" text-anchor="middle" fill="#334155" font-size="11.5" font-weight="600">Collects the voter slip,</text>
              <text x="105" y="205" text-anchor="middle" fill="#334155" font-size="11.5" font-weight="600">inspects finger ink mark,</text>
              <text x="105" y="225" text-anchor="middle" fill="#334155" font-size="11.5" font-weight="600">and presses \'Ballot\' button</text>
              <text x="105" y="245" text-anchor="middle" fill="#334155" font-size="11.5" font-weight="600">on the EVM Control Unit.</text>
              <rect x="25" y="270" width="160" height="30" rx="6" fill="#ffffff"/>
              <text x="105" y="290" text-anchor="middle" fill="#047857" font-size="11" font-weight="700">Activates EVM</text>
            </g>

            <!-- STEP 4 -->
            <g transform="translate(740, 40)">
              <rect width="190" height="320" rx="14" fill="url(#stepGrad4)" stroke="#f43f5e" stroke-width="1.5"/>
              <rect x="10" y="15" width="170" height="36" rx="8" fill="#be123c"/>
              <text x="95" y="38" text-anchor="middle" fill="#ffffff" font-size="12.5" font-weight="800">VOTING BOOTH</text>
              <circle cx="95" cy="95" r="30" fill="#ffffff" stroke="#f43f5e" stroke-width="2"/>
              <text x="95" y="103" text-anchor="middle" fill="#be123c" font-size="22" font-weight="900">4</text>
              <text x="95" y="155" text-anchor="middle" fill="#881337" font-size="13.5" font-weight="800">Vote & VVPAT Audit</text>
              <text x="95" y="185" text-anchor="middle" fill="#334155" font-size="11" font-weight="600">Voter presses blue button</text>
              <text x="95" y="205" text-anchor="middle" fill="#334155" font-size="11" font-weight="600">on Ballot Unit. Red LED</text>
              <text x="95" y="225" text-anchor="middle" fill="#334155" font-size="11" font-weight="600">glows, loud beep sounds,</text>
              <text x="95" y="245" text-anchor="middle" fill="#334155" font-size="11" font-weight="600">and VVPAT slip cuts in 7s!</text>
              <rect x="15" y="270" width="160" height="30" rx="6" fill="#ffffff"/>
              <text x="95" y="290" text-anchor="middle" fill="#be123c" font-size="11" font-weight="700">Beep + 7s Paper Slip</text>
            </g>
          </svg>
        </div>
      </div>

      <div class="callout-box callout-hack">
        <div class="callout-title">
          <i class="fa-solid fa-flask"></i> Science Fact: The Secret of Indelible Ink
        </div>
        <p>
          Have you ever wondered why the purple mark on your finger does not wash off even with soap, lemon juice, or sanitizers?
        </p>
        <p>
          The ink contains <strong>Silver Nitrate (AgNO₃)</strong>, manufactured exclusively by <strong>Mysore Paints and Varnish Ltd</strong> (a Karnataka government enterprise). When applied to the skin, silver nitrate reacts with moisture and protein (keratin) on the nail and oxidizes under ambient light to form a permanent dark stain that only disappears naturally when new nail cells grow out! This prevents unscrupulous persons from voting twice.
        </p>
      </div>

      <div class="callout-box callout-pyq">
        <div class="callout-title">
          <i class="fa-solid fa-person-walking"></i> The Legend of India\'s First Voter: Shyam Saran Negi
        </div>
        <p>
          India\'s very first general elections were scheduled for early 1952. However, in the high snowbound mountains of Kinnaur, Himachal Pradesh, elections were conducted early on <strong>25 October 1951</strong> before heavy winter blizzards blocked the Himalayan passes.
        </p>
        <p>
          A patriotic primary school teacher named <strong>Shyam Saran Negi</strong> (1917–2022) arrived at the Kalpa polling booth at 7:00 AM and became <strong>independent India\'s very first voter</strong>! Negi cast his vote in every single Lok Sabha, Vidhan Sabha, and local election for 71 years—voting a staggering 34 times until he passed away at age 105 in 2022, inspiring generations of young Indians to cherish their voting duty!
        </p>
      </div>

      <!-- SVG Diagram 6: EVM + VVPAT Architecture -->
      <div class="svg-diagram-card">
        <div class="svg-header">
          <div class="svg-caption">
            <i class="fa-solid fa-microchip" style="color: #1e3a8a;"></i>
            <span>Figure 5.E: Architecture of India\'s Electronic Voting Ecosystem: EVM & VVPAT</span>
          </div>
          <span class="svg-tag">Technological Security</span>
        </div>
        <div class="svg-container">
          <svg viewBox="0 0 950 420" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background: #ffffff; font-family: 'Plus Jakarta Sans', sans-serif;">
            <defs>
              <linearGradient id="cuGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#1e293b"/>
                <stop offset="100%" stop-color="#0f172a"/>
              </linearGradient>
              <linearGradient id="buGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#f8fafc"/>
                <stop offset="100%" stop-color="#e2e8f0"/>
              </linearGradient>
              <linearGradient id="vvGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#f1f5f9"/>
                <stop offset="100%" stop-color="#cbd5e1"/>
              </linearGradient>
            </defs>

            <!-- CONTROL UNIT (With Polling Officer) -->
            <g transform="translate(30, 40)">
              <rect width="260" height="340" rx="14" fill="url(#cuGrad)" stroke="#334155" stroke-width="2"/>
              <rect x="20" y="20" width="220" height="36" rx="6" fill="#1e3a8a"/>
              <text x="130" y="43" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="800">CONTROL UNIT (CU)</text>
              <rect x="25" y="75" width="210" height="50" rx="6" fill="#047857"/>
              <text x="130" y="98" text-anchor="middle" fill="#a7f3d0" font-size="11" font-weight="700">SEVEN-SEGMENT DISPLAY</text>
              <text x="130" y="118" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="900" font-family="monospace">TOTAL VOTES: 842</text>
              
              <circle cx="80" cy="180" r="28" fill="#dc2626"/>
              <text x="80" y="185" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="800">BUSY</text>
              <circle cx="180" cy="180" r="28" fill="#16a34a"/>
              <text x="180" y="185" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="800">READY</text>

              <rect x="40" y="240" width="180" height="48" rx="8" fill="#3b82f6"/>
              <text x="130" y="268" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="800">"BALLOT" BUTTON</text>
              <text x="130" y="320" text-anchor="middle" fill="#94a3b8" font-size="11" font-weight="600">Presiding / 3rd Officer Table</text>
            </g>

            <!-- CABLE 1 -->
            <path d="M 290 210 L 360 210" stroke="#047857" stroke-width="4" stroke-dasharray="6,4"/>
            <text x="325" y="200" text-anchor="middle" fill="#047857" font-size="11" font-weight="700">Cable</text>

            <!-- VVPAT UNIT (In Booth) -->
            <g transform="translate(360, 40)">
              <rect width="250" height="340" rx="14" fill="url(#vvGrad)" stroke="#94a3b8" stroke-width="2"/>
              <rect x="20" y="20" width="210" height="36" rx="6" fill="#047857"/>
              <text x="125" y="43" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="800">VVPAT PRINTER</text>
              
              <!-- Paper Slip Window -->
              <rect x="35" y="80" width="180" height="120" rx="8" fill="#ffffff" stroke="#475569" stroke-width="2"/>
              <rect x="50" y="95" width="150" height="85" fill="#fef3c7" stroke="#cbd5e1"/>
              <text x="125" y="115" text-anchor="middle" fill="#78350f" font-size="10" font-weight="800">SLIP VISIBLE FOR 7 SECONDS</text>
              <text x="125" y="135" text-anchor="middle" fill="#1e293b" font-size="11" font-weight="700">Serial No • Name • Symbol</text>
              <text x="125" y="158" text-anchor="middle" fill="#dc2626" font-size="10" font-weight="700">Cuts & Drops into Sealed Box</text>

              <rect x="35" y="225" width="180" height="70" rx="6" fill="#334155"/>
              <text x="125" y="255" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="700">Sealed Ballot Paper Box</text>
              <text x="125" y="275" text-anchor="middle" fill="#cbd5e1" font-size="10" font-weight="500">Retained for physical recount</text>
              <text x="125" y="325" text-anchor="middle" fill="#475569" font-size="11" font-weight="600">Inside Voting Compartment</text>
            </g>

            <!-- CABLE 2 -->
            <path d="M 610 210 L 670 210" stroke="#047857" stroke-width="4" stroke-dasharray="6,4"/>
            <text x="640" y="200" text-anchor="middle" fill="#047857" font-size="11" font-weight="700">Cable</text>

            <!-- BALLOT UNIT (EVM) -->
            <g transform="translate(670, 40)">
              <rect width="250" height="340" rx="14" fill="url(#buGrad)" stroke="#94a3b8" stroke-width="2"/>
              <rect x="20" y="20" width="210" height="36" rx="6" fill="#b45309"/>
              <text x="125" y="43" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="800">BALLOT UNIT (BU)</text>

              <!-- Candidate Buttons Row 1 -->
              <rect x="25" y="75" width="200" height="38" rx="6" fill="#ffffff" stroke="#cbd5e1"/>
              <text x="35" y="98" fill="#1e293b" font-size="11" font-weight="700">1. Candidate A</text>
              <circle cx="170" cy="94" r="5" fill="#22c55e"/>
              <rect x="185" y="83" width="30" height="22" rx="4" fill="#3b82f6"/>

              <!-- Candidate Buttons Row 2 -->
              <rect x="25" y="125" width="200" height="38" rx="6" fill="#ffffff" stroke="#cbd5e1"/>
              <text x="35" y="148" fill="#1e293b" font-size="11" font-weight="700">2. Candidate B</text>
              <circle cx="170" cy="144" r="5" fill="#94a3b8"/>
              <rect x="185" y="133" width="30" height="22" rx="4" fill="#3b82f6"/>

              <!-- Candidate Buttons Row 3 -->
              <rect x="25" y="175" width="200" height="38" rx="6" fill="#ffffff" stroke="#cbd5e1"/>
              <text x="35" y="198" fill="#1e293b" font-size="11" font-weight="700">3. Candidate C</text>
              <circle cx="170" cy="194" r="5" fill="#94a3b8"/>
              <rect x="185" y="183" width="30" height="22" rx="4" fill="#3b82f6"/>

              <!-- NOTA Button Row -->
              <rect x="25" y="225" width="200" height="38" rx="6" fill="#fee2e2" stroke="#fca5a5"/>
              <text x="35" y="248" fill="#991b1b" font-size="11" font-weight="800">16. NOTA</text>
              <circle cx="170" cy="244" r="5" fill="#94a3b8"/>
              <rect x="185" y="233" width="30" height="22" rx="4" fill="#ef4444"/>

              <!-- Embossed Braille Marker -->
              <rect x="25" y="280" width="200" height="35" rx="6" fill="#eff6ff"/>
              <text x="125" y="302" text-anchor="middle" fill="#1d4ed8" font-size="10.5" font-weight="700">Embossed Braille for Blind Voters</text>
            </g>
          </svg>
        </div>
      </div>

      <!-- CONCEPT 8 -->
      <h3 class="subsection-title" id="concept-8">
        <i class="fa-solid fa-gavel" style="color: #b45309;"></i>
        8. The Model Code of Conduct (MCC) & The Legacy of T.N. Seshan
      </h3>

      <p>
        In sports like cricket or football, referees enforce strict rules so that neither team cheats. In Indian elections, the <strong>Model Code of Conduct (MCC)</strong> serves as the moral and ethical rulebook that all political parties and candidates must follow.
      </p>

      <div class="callout-box callout-def">
        <div class="callout-title">
          <i class="fa-solid fa-shield-halved"></i> What is the Model Code of Conduct (MCC)?
        </div>
        <p>
          The <strong>Model Code of Conduct (MCC)</strong> is a comprehensive set of guidelines issued by the Election Commission of India to regulate the conduct of political parties and candidates during election campaigns. It comes into operational effect the exact moment the ECI announces the election schedule at a press conference, and stays in force until counting ends.
        </p>
      </div>

      <h4 class="topic-title">Historical Origin: Kerala 1960</h4>
      <p>
        The MCC was not imposed by force. It originated in the state of <strong>Kerala in 1960</strong> during state assembly elections, where political parties voluntarily gathered and formulated a mutual code of self-discipline. Recognizing its immense success, the ECI circulated it to all states in 1968, refining it into a nationwide code of electoral ethics.
      </p>

      <h4 class="topic-title">Key Prohibitions Under the MCC:</h4>
      <ul>
        <li><strong>No Misuse of Government Power:</strong> Ruling parties cannot use official government aircraft, vehicles, or state-funded advertising campaigns to promote their own election prospects.</li>
        <li><strong>No Policy Bribery (No Last-Minute Scheme Announcements):</strong> Once elections are announced, ministers and governments cannot announce new welfare grants, lay foundation stones, or sanction financial projects to entice voters.</li>
        <li><strong>No Caste or Communal Hate Appeals:</strong> Candidates cannot invoke religion, mosques, temples, churches, or caste animosity to seek votes.</li>
        <li><strong>Zero Bribes or Freebies:</strong> Distributing cash (bundles of currency notes), sarees, pressure cookers, televisions, alcohol, or feast parties to induce voters is strictly prohibited and treated as a criminal offense!</li>
        <li><strong>The 48-Hour Silence Period:</strong> All public campaigning, rallies, loudspeaker use, and TV campaign broadcasts must halt completely <strong>48 hours</strong> prior to the conclusion of polling.</li>
      </ul>

      <div class="callout-box callout-pyq">
        <div class="callout-title">
          <i class="fa-solid fa-user-shield"></i> T.N. Seshan: The Fearless Reformer of Indian Elections
        </div>
        <p>
          Before 1990, Indian elections were frequently plagued by "muscle power", intimidation of poor voters, illegal wall graffiti, unchecked cash donations, and booth-capturing.
        </p>
        <p>
          In December 1990, <strong>T.N. Seshan</strong> became the <strong>10th Chief Election Commissioner of India (1990–1996)</strong>. He transformed the ECI into a powerhouse:
        </p>
        <ul>
          <li>He strictly enforced the Model Code of Conduct, famously declaring: <em>"Nobody is above the Constitution!"</em></li>
          <li>He introduced <strong>Voter Photo Identity Cards (EPIC)</strong> to stamp out proxy voting once and for all.</li>
          <li>He deployed Central Armed Police Forces (CAPF) to protect polling booths in sensitive areas, ending booth capturing.</li>
          <li>He set strict financial expenditure limits for candidates and disqualified those who filed fraudulent accounts.</li>
        </ul>
        <p>
          T.N. Seshan made Indian democracy respected across the globe for fearless, fair, and transparent voting.
        </p>
      </div>

      <!-- CONCEPT 9 -->
      <h3 class="subsection-title" id="concept-9">
        <i class="fa-solid fa-arrows-split-up-and-left" style="color: #6d28d9;"></i>
        9. Direct vs Indirect Elections: How Our Parliaments and Presidents Are Chosen
      </h3>

      <p>
        In India, democracy functions through two primary mechanisms: <strong>Direct Elections</strong> and <strong>Indirect Elections</strong>.
      </p>

      <h4 class="topic-title">Direct Elections (First-Past-The-Post System):</h4>
      <p>
        In a <strong>Direct Election</strong>, every eligible citizen walks directly to the polling booth and casts a personal vote for the candidate of their choice:
      </p>
      <ul>
        <li><strong>Lok Sabha (House of the People):</strong> The country is demarcated into <strong>543 Parliamentary Constituencies</strong>. The candidate who gets the most votes in each constituency wins a seat as a <strong>Member of Parliament (MP)</strong>.</li>
        <li><strong>State Legislative Assembly (Vidhan Sabha):</strong> Each state is divided into assembly constituencies. Voters elect <strong>Members of Legislative Assembly (MLAs)</strong> who focus on state governance (health, schools, state roads, agriculture).</li>
        <li><strong>Local Bodies:</strong> Ward members in Gram Panchayats and Municipal Corporations are directly elected by village and city residents.</li>
      </ul>

      <div class="callout-box callout-def">
        <div class="callout-title">
          <i class="fa-solid fa-id-card-clip"></i> What is the Difference Between an MP and an MLA?
        </div>
        <ul>
          <li><strong>MP (Member of Parliament):</strong> Represents an entire parliamentary constituency in the national Parliament at New Delhi. MPs debate national defense, foreign relations, railways, and national laws.</li>
          <li><strong>MLA (Member of Legislative Assembly):</strong> Represents a state assembly constituency in the state capital. MLAs debate state policies, local policing, irrigation, state roadways, and primary education.</li>
          <li><em>Fun Fact:</em> One Lok Sabha parliamentary constituency is typically composed of <strong>several (5 to 9) Assembly constituencies</strong>! Therefore, every citizen has both an MP and an MLA representing their area.</li>
        </ul>
      </div>

      <!-- SVG Diagram 5: 543 Seats Breakdown & Direct vs Indirect Flow -->
      <div class="svg-diagram-card">
        <div class="svg-header">
          <div class="svg-caption">
            <i class="fa-solid fa-chart-pie" style="color: #b45309;"></i>
            <span>Figure 5.F: Lok Sabha Seat Distribution & Direct vs Indirect Representation Pathways</span>
          </div>
          <span class="svg-tag">Electoral Geometry</span>
        </div>
        <div class="svg-container">
          <svg viewBox="0 0 950 460" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background: #ffffff; font-family: 'Plus Jakarta Sans', sans-serif;">
            <defs>
              <linearGradient id="genGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#1e3a8a"/>
                <stop offset="100%" stop-color="#3b82f6"/>
              </linearGradient>
              <linearGradient id="scGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#b45309"/>
                <stop offset="100%" stop-color="#f59e0b"/>
              </linearGradient>
              <linearGradient id="stGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#047857"/>
                <stop offset="100%" stop-color="#10b981"/>
              </linearGradient>
            </defs>

            <!-- LOK SABHA 543 SEATS PROPORTIONAL BAR -->
            <g transform="translate(40, 30)">
              <text x="0" y="20" fill="#0f172a" font-size="16" font-weight="800">LOK SABHA: 543 DIRECTLY ELECTED CONSTITUENCIES</text>
              
              <!-- 412 General Seats (75.9%) -->
              <rect x="0" y="35" width="660" height="45" rx="6" fill="url(#genGrad)"/>
              <text x="330" y="63" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="800">412 GENERAL SEATS (75.9%)</text>
              
              <!-- 84 SC Reserved Seats (15.5%) -->
              <rect x="665" y="35" width="135" height="45" rx="6" fill="url(#scGrad)"/>
              <text x="732" y="63" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="800">84 SC (15.5%)</text>
              
              <!-- 47 ST Reserved Seats (8.6%) -->
              <rect x="805" y="35" width="65" height="45" rx="6" fill="url(#stGrad)"/>
              <text x="837" y="63" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="800">47 ST</text>
            </g>

            <!-- DIRECT VS INDIRECT PATHWAYS -->
            <!-- Direct Box -->
            <g transform="translate(40, 130)">
              <rect width="415" height="300" rx="14" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.5"/>
              <rect x="20" y="15" width="375" height="38" rx="8" fill="#1e3a8a"/>
              <text x="207" y="40" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="800">DIRECT ELECTIONS (CITIZENS VOTE)</text>

              <rect x="25" y="70" width="365" height="65" rx="8" fill="#ffffff" stroke="#93c5fd"/>
              <text x="40" y="93" fill="#1e3a8a" font-size="13" font-weight="800">Lok Sabha (House of the People)</text>
              <text x="40" y="113" fill="#475569" font-size="11.5" font-weight="500">968 Million voters elect 543 MPs via FPTP system.</text>
              <text x="40" y="128" fill="#1d4ed8" font-size="11" font-weight="700">Majority Party Leader becomes Prime Minister.</text>

              <rect x="25" y="145" width="365" height="65" rx="8" fill="#ffffff" stroke="#93c5fd"/>
              <text x="40" y="168" fill="#1e3a8a" font-size="13" font-weight="800">State Legislative Assembly (Vidhan Sabha)</text>
              <text x="40" y="188" fill="#475569" font-size="11.5" font-weight="500">State voters elect MLAs in single-member seats.</text>
              <text x="40" y="203" fill="#1d4ed8" font-size="11" font-weight="700">Majority Leader becomes Chief Minister.</text>

              <rect x="25" y="220" width="365" height="65" rx="8" fill="#ffffff" stroke="#93c5fd"/>
              <text x="40" y="243" fill="#1e3a8a" font-size="13" font-weight="800">Grassroots Local Bodies (PRIs & ULBs)</text>
              <text x="40" y="263" fill="#475569" font-size="11.5" font-weight="500">Ward members & Sarpanches elected directly by villagers.</text>
              <text x="40" y="278" fill="#1d4ed8" font-size="11" font-weight="700">Conducted independently by State Election Commissions.</text>
            </g>

            <!-- Indirect Box -->
            <g transform="translate(495, 130)">
              <rect width="415" height="300" rx="14" fill="#fef3c7" stroke="#fde68a" stroke-width="1.5"/>
              <rect x="20" y="15" width="375" height="38" rx="8" fill="#b45309"/>
              <text x="207" y="40" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="800">INDIRECT ELECTIONS (REPRESENTATIVES VOTE)</text>

              <rect x="25" y="70" width="365" height="65" rx="8" fill="#ffffff" stroke="#fcd34d"/>
              <text x="40" y="93" fill="#78350f" font-size="13" font-weight="800">Rajya Sabha (Council of States)</text>
              <text x="40" y="113" fill="#475569" font-size="11.5" font-weight="500">233 Members elected by elected MLAs via Single</text>
              <text x="40" y="128" fill="#92400e" font-size="11" font-weight="700">Transferable Vote; 12 nominated by President.</text>

              <rect x="25" y="145" width="365" height="65" rx="8" fill="#ffffff" stroke="#fcd34d"/>
              <text x="40" y="168" fill="#78350f" font-size="13" font-weight="800">President of India</text>
              <text x="40" y="188" fill="#475569" font-size="11.5" font-weight="500">Electoral College of elected MPs (LS + RS) and</text>
              <text x="40" y="203" fill="#92400e" font-size="11" font-weight="700">elected MLAs of all States + Delhi & Puducherry.</text>

              <rect x="25" y="220" width="365" height="65" rx="8" fill="#ffffff" stroke="#fcd34d"/>
              <text x="40" y="243" fill="#78350f" font-size="13" font-weight="800">Vice-President of India</text>
              <text x="40" y="263" fill="#475569" font-size="11.5" font-weight="500">Elected by all MPs (elected + nominated) of both</text>
              <text x="40" y="278" fill="#92400e" font-size="11" font-weight="700">Lok Sabha and Rajya Sabha; Ex-officio RS Chairman.</text>
            </g>
          </svg>
        </div>
      </div>

      <h4 class="topic-title">Indirect Elections: Rajya Sabha & The President of India</h4>
      <p>
        In an <strong>Indirect Election</strong>, citizens do not vote directly. Instead, citizens elect intermediaries (such as MLAs or MPs), who then vote to elect the higher authority:
      </p>

      <h5>1. Election to the Rajya Sabha (Council of States):</h5>
      <ul>
        <li>The Rajya Sabha has a total sanctioned strength of <strong>245 members</strong>.</li>
        <li><strong>233 members</strong> represent the States and Union Territories. They are elected by the <strong>elected members of the State Legislative Assemblies (MLAs)</strong> using the <strong>Single Transferable Vote (STV)</strong> proportional system.</li>
        <li><strong>12 members</strong> are nominated by the President of India for distinguished contributions to literature, science, art, and social service.</li>
        <li><strong>Permanent Chamber:</strong> Rajya Sabha is never dissolved! One-third (1/3) of its members retire every two years, giving every member a full 6-year tenure and ensuring legislative continuity.</li>
      </ul>

      <h5>2. Election of the President of India:</h5>
      <p>
        The President of India is the ceremonial Head of State representing the unity of the entire Republic. Therefore, the President is elected by a specialized <strong>Electoral College</strong> consisting of:
      </p>
      <ol>
        <li>Elected Members of Parliament (MPs) of both Houses (Lok Sabha & Rajya Sabha).</li>
        <li>Elected Members of Legislative Assemblies (MLAs) of all States and the Union Territories of Delhi and Puducherry.</li>
      </ol>
      <p>
        <strong>Who is EXCLUDED from electing the President?</strong>
      </p>
      <ul>
        <li>The 12 Nominated members of Rajya Sabha.</li>
        <li>Nominated members of State Assemblies.</li>
        <li>Members of State Legislative Councils (MLCs in bicameral states like UP, Bihar, Maharashtra, Karnataka, Andhra Pradesh, and Telangana).</li>
      </ul>
      <p>
        <em>Why are nominated members excluded?</em> Because nominated members were chosen by the sitting government/President; allowing them to vote would violate democratic legitimacy and create unfair bias!
      </p>

      <!-- CONCEPT 10 -->
      <h3 class="subsection-title" id="concept-10">
        <i class="fa-solid fa-handshake-angle" style="color: #047857;"></i>
        10. Affirmative Action: Reserved Constituencies for SC and ST
      </h3>

      <p>
        In a purely majoritarian electoral system without safeguards, historically marginalized and oppressed communities might never win an election because they lack wealth, land, and social dominance.
      </p>
      <p>
        To prevent this injustice, our Constitution makers established <strong>Reserved Constituencies</strong> in the Lok Sabha and State Legislative Assemblies:
      </p>
      <ul>
        <li><strong>84 Seats</strong> in the Lok Sabha are reserved exclusively for persons from the <strong>Scheduled Castes (SC)</strong>.</li>
        <li><strong>47 Seats</strong> are reserved exclusively for persons from the <strong>Scheduled Tribes (ST)</strong>.</li>
      </ul>

      <div class="callout-box callout-warn">
        <div class="callout-title">
          <i class="fa-solid fa-circle-question"></i> Frequent Student Confusion: How Does a Reserved Constituency Work?
        </div>
        <p>
          Students often ask: <em>"In an SC-reserved constituency, do only SC citizens vote?"</em><br>
          <strong>NO! That is a major misconception!</strong> In a reserved constituency, <strong>every registered citizen (general, OBC, SC, ST) votes equally</strong>! The only restriction is that the <strong>candidates who stand for election must belong to the Scheduled Caste or Scheduled Tribe community</strong>. This ensures that the elected lawmaker genuinely represents the historic voice of marginalized communities while remaining answerable to all constituents!
        </p>
      </div>

      <!-- CONCEPT 11 -->
      <h3 class="subsection-title" id="concept-11">
        <i class="fa-solid fa-triangle-exclamation" style="color: #be123c;"></i>
        11. Contemporary Challenges and The Road Ahead
      </h3>

      <p>
        While India\'s electoral system is celebrated globally, our democracy faces significant modern challenges that demand active, alert citizenship:
      </p>

      <ol>
        <li>
          <strong>The Growing Influence of Money Power:</strong> Wealthy candidates and corporate financiers often attempt to "buy" votes through cash distribution, free liquor, consumer gadgets, and expensive advertisement blitzes.
        </li>
        <li>
          <strong>Criminalization of Politics:</strong> A troubling percentage of election contestants face pending criminal charges. ECI now mandates that candidates publish full criminal affidavits in newspapers and on the <strong>KYC (Know Your Candidate) mobile app</strong>.
        </li>
        <li>
          <strong>Urban Voter Apathy:</strong> In the 2024 Lok Sabha elections, approximately <strong>34 per cent</strong> of eligible voters did not cast their vote! Shockingly, voting turnout was lowest in affluent, highly educated urban areas (like Bengaluru, Mumbai, and Delhi) where voters treated polling day merely as an extended holiday weekend.
        </li>
        <li>
          <strong>Misinformation & Social Media Manipulation:</strong> Deepfakes, manipulated video reels, hateful WhatsApp forwards, and algorithmic bias can distort facts and polarize voters before elections.
        </li>
      </ol>

      <div class="callout-box callout-hack">
        <div class="callout-title">
          <i class="fa-solid fa-mobile-screen"></i> Citizen Empowerment: The C-VIGIL Smartphone App
        </div>
        <p>
          To empower young citizens, the ECI launched the <strong>c-VIGIL mobile app</strong>. Any citizen who witnesses an MCC violation (like cash distribution, hate speech, or liquor distribution) can snap a photo or record a 2-minute video. The app automatically tags the exact GPS location, transmits it to the nearest flying squad, and election officers are mandated to arrive and investigate within <strong>100 minutes</strong>!
        </p>
      </div>

      <!-- BILINGUAL VOCABULARY & GLOSSARY TABLE -->
      <h3 class="subsection-title" id="glossary">
        <i class="fa-solid fa-language" style="color: #1e3a8a;"></i>
        Exhaustive Bilingual Vocabulary & Key Terms Bank (English-Odia)
      </h3>
      <p>
        Mastering these 30 foundational concepts in both English and standard Odia (ଓଡ଼ିଆ ଭାଷା) will give you total mastery in school classroom tests, BSE Odisha boards, and CBSE examinations.
      </p>

      <div class="table-responsive">
        <table class="study-table">
          <thead>
            <tr>
              <th>#</th>
              <th>Term / Concept</th>
              <th>Part of Speech</th>
              <th>English Meaning & Curricular Context</th>
              <th>ଓଡ଼ିଆ ଅର୍ଥ (Odia Meaning & Script)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1</td>
              <td><strong>Universal Adult Franchise</strong></td>
              <td>Noun Phrase</td>
              <td>The constitutional right of every adult citizen aged 18+ to vote without discrimination.</td>
              <td><span class="badge-odia">ସାର୍ବଜନୀନ ବାଳକ/ପ୍ରାପ୍ତବୟସ୍କ ମତାଧିକାର</span></td>
            </tr>
            <tr>
              <td>2</td>
              <td><strong>Suffrage</strong></td>
              <td>Noun</td>
              <td>The legal and political right to vote in public elections (synonym of franchise).</td>
              <td><span class="badge-odia">ମତାଧିକାର</span></td>
            </tr>
            <tr>
              <td>3</td>
              <td><strong>Constituency</strong></td>
              <td>Noun</td>
              <td>A demarcated geographic area whose registered voters elect a representative.</td>
              <td><span class="badge-odia">ନିର୍ବାଚନ ମଣ୍ଡଳୀ</span></td>
            </tr>
            <tr>
              <td>4</td>
              <td><strong>Secret Ballot</strong></td>
              <td>Noun Phrase</td>
              <td>A voting method where a voter\'s choice is completely confidential to prevent coercion.</td>
              <td><span class="badge-odia">ଗୁପ୍ତ ମତଦାନ / ଗୋପନୀୟ ବାଲାଟ</span></td>
            </tr>
            <tr>
              <td>5</td>
              <td><strong>Election Commission of India (ECI)</strong></td>
              <td>Proper Noun</td>
              <td>Autonomous constitutional body under Article 324 conducting Indian elections.</td>
              <td><span class="badge-odia">ଭାରତର ନିର୍ବାଚନ ଆୟୋଗ</span></td>
            </tr>
            <tr>
              <td>6</td>
              <td><strong>Chief Election Commissioner (CEC)</strong></td>
              <td>Noun</td>
              <td>The constitutional head of the Election Commission of India.</td>
              <td><span class="badge-odia">ମୁଖ୍ୟ ନିର୍ବାଚନ କମିଶନର</span></td>
            </tr>
            <tr>
              <td>7</td>
              <td><strong>Chief Electoral Officer (CEO)</strong></td>
              <td>Noun</td>
              <td>Senior IAS officer supervising elections at the State or Union Territory level.</td>
              <td><span class="badge-odia">ମୁଖ୍ୟ ନିର୍ବାଚନ ଅଧିକାରୀ (ରାଜ୍ୟ ସ୍ତର)</span></td>
            </tr>
            <tr>
              <td>8</td>
              <td><strong>District Election Officer (DEO)</strong></td>
              <td>Noun</td>
              <td>District Magistrate or Collector managing all election machinery in a district.</td>
              <td><span class="badge-odia">ଜିଲ୍ଲା ନିର୍ବାଚନ ଅଧିକାରୀ</span></td>
            </tr>
            <tr>
              <td>9</td>
              <td><strong>Returning Officer (RO)</strong></td>
              <td>Noun</td>
              <td>Officer responsible for conducting elections and declaring results in a constituency.</td>
              <td><span class="badge-odia">ରିଟର୍ଣ୍ଣିଂ ଅଫିସର / ନିର୍ବାଚନ ପରିଚାଳକ</span></td>
            </tr>
            <tr>
              <td>10</td>
              <td><strong>Presiding Officer</strong></td>
              <td>Noun</td>
              <td>Official in charge of conducting polling smoothly at a specific polling station.</td>
              <td><span class="badge-odia">ପ୍ରିଜାଇଡିଂ ଅଫିସର / ବୁଥ୍ ଅଧ୍ୟକ୍ଷ</span></td>
            </tr>
            <tr>
              <td>11</td>
              <td><strong>Booth Level Officer (BLO)</strong></td>
              <td>Noun</td>
              <td>Grassroots local officer maintaining and updating voter lists for a specific booth.</td>
              <td><span class="badge-odia">ବୁଥ୍ ସ୍ତରୀୟ ଅଧିକାରୀ</span></td>
            </tr>
            <tr>
              <td>12</td>
              <td><strong>Electronic Voting Machine (EVM)</strong></td>
              <td>Noun Phrase</td>
              <td>Electronic device used to record votes securely without paper ballot stuffing.</td>
              <td><span class="badge-odia">ଇଲେକ୍ଟ୍ରୋନିକ୍ ଭୋଟିଂ ମେସିନ୍</span></td>
            </tr>
            <tr>
              <td>13</td>
              <td><strong>Voter Verifiable Paper Audit Trail (VVPAT)</strong></td>
              <td>Noun Phrase</td>
              <td>Printer device that shows a 7-second paper slip to verify an EVM vote.</td>
              <td><span class="badge-odia">ଭିଭିପାଟ୍ (କାଗଜ ଅଡିଟ୍ ସ୍ଲିପ୍ ପ୍ରଣାଳୀ)</span></td>
            </tr>
            <tr>
              <td>14</td>
              <td><strong>None Of The Above (NOTA)</strong></td>
              <td>Noun Phrase</td>
              <td>A ballot option enabling voters to formally reject all contesting candidates.</td>
              <td><span class="badge-odia">ଉପରୋକ୍ତ କେହି ନୁହଁନ୍ତି (ନୋଟା)</span></td>
            </tr>
            <tr>
              <td>15</td>
              <td><strong>Model Code of Conduct (MCC)</strong></td>
              <td>Noun Phrase</td>
              <td>Guidelines regulating campaign behavior of political parties and candidates.</td>
              <td><span class="badge-odia">ଆଦର୍ଶ ଆଚରଣ ବିଧି</span></td>
            </tr>
            <tr>
              <td>16</td>
              <td><strong>First-Past-The-Post (FPTP)</strong></td>
              <td>Noun Phrase</td>
              <td>Electoral rule where the candidate winning the highest number of votes wins.</td>
              <td><span class="badge-odia">ସର୍ବାଧିକ ମତ ପ୍ରାପ୍ତ ବିଜୟୀ ପ୍ରଣାଳୀ</span></td>
            </tr>
            <tr>
              <td>17</td>
              <td><strong>Direct Election</strong></td>
              <td>Noun Phrase</td>
              <td>Elections where citizens cast votes directly to choose their representative.</td>
              <td><span class="badge-odia">ପ୍ରତ୍ୟକ୍ଷ ନିର୍ବାଚନ</span></td>
            </tr>
            <tr>
              <td>18</td>
              <td><strong>Indirect Election</strong></td>
              <td>Noun Phrase</td>
              <td>Elections where voters elect intermediaries who then vote for leaders.</td>
              <td><span class="badge-odia">ପରୋକ୍ଷ ନିର୍ବାଚନ</span></td>
            </tr>
            <tr>
              <td>19</td>
              <td><strong>Electoral College</strong></td>
              <td>Noun Phrase</td>
              <td>A specialized body of elected representatives assembled to elect a high official.</td>
              <td><span class="badge-odia">ନିର୍ବାଚକ ମଣ୍ଡଳୀ</span></td>
            </tr>
            <tr>
              <td>20</td>
              <td><strong>Single Transferable Vote (STV)</strong></td>
              <td>Noun Phrase</td>
              <td>Proportional voting system where voters rank candidates by preference order.</td>
              <td><span class="badge-odia">ଏକକ ହସ୍ତାନ୍ତରଣୀୟ ମତ ପ୍ରଣାଳୀ</span></td>
            </tr>
            <tr>
              <td>21</td>
              <td><strong>Member of Parliament (MP)</strong></td>
              <td>Noun Phrase</td>
              <td>An elected or nominated member representing citizens in the national Parliament.</td>
              <td><span class="badge-odia">ସାଂସଦ (ଲୋକସଭା/ରାଜ୍ୟସଭା ସଦସ୍ୟ)</span></td>
            </tr>
            <tr>
              <td>22</td>
              <td><strong>Member of Legislative Assembly (MLA)</strong></td>
              <td>Noun Phrase</td>
              <td>A representative elected by state voters to sit in the State Vidhan Sabha.</td>
              <td><span class="badge-odia">ବିଧାୟକ (ବିଧାନସଭା ସଦସ୍ୟ)</span></td>
            </tr>
            <tr>
              <td>23</td>
              <td><strong>Reserved Constituency</strong></td>
              <td>Noun Phrase</td>
              <td>A seat where only candidates from designated SC or ST groups can contest.</td>
              <td><span class="badge-odia">ସଂରକ୍ଷିତ ନିର୍ବାଚନ ମଣ୍ଡଳୀ</span></td>
            </tr>
            <tr>
              <td>24</td>
              <td><strong>Voter Apathy</strong></td>
              <td>Noun Phrase</td>
              <td>Lack of interest, indifference, or unwillingness of citizens to cast their vote.</td>
              <td><span class="badge-odia">ଭୋଟର ଉଦାସୀନତା</span></td>
            </tr>
            <tr>
              <td>25</td>
              <td><strong>Indelible Ink</strong></td>
              <td>Noun Phrase</td>
              <td>Silver-nitrate stain applied to fingernails to prevent multiple voting.</td>
              <td><span class="badge-odia">ଅଲିଭା କାଳି</span></td>
            </tr>
            <tr>
              <td>26</td>
              <td><strong>Bicameral Legislature</strong></td>
              <td>Noun Phrase</td>
              <td>A legislative parliament divided into two separate houses (e.g. Lok Sabha & Rajya Sabha).</td>
              <td><span class="badge-odia">ଦ୍ୱି-ସଦନ ବିଶିଷ୍ଟ ବ୍ୟବସ୍ଥାପିକା</span></td>
            </tr>
            <tr>
              <td>27</td>
              <td><strong>Coalition Government</strong></td>
              <td>Noun Phrase</td>
              <td>A government formed jointly by two or more political parties when none has a solo majority.</td>
              <td><span class="badge-odia">ମିଳିତ ସରକାର</span></td>
            </tr>
            <tr>
              <td>28</td>
              <td><strong>Kudavolai System</strong></td>
              <td>Noun Phrase</td>
              <td>10th-century Chola pot ticket system using palm leaves drawn by a child.</td>
              <td><span class="badge-odia">କୁଡାଭୋଲାଇ ପ୍ରଣାଳୀ (ମାଠିଆ ତାଳପତ୍ର ଚୟନ)</span></td>
            </tr>
            <tr>
              <td>29</td>
              <td><strong>Electorate</strong></td>
              <td>Noun</td>
              <td>The entire body of citizens registered and eligible to vote in an election.</td>
              <td><span class="badge-odia">ଭୋଟର ସମୂହ / ନିର୍ବାଚକ ମଣ୍ଡଳ</span></td>
            </tr>
            <tr>
              <td>30</td>
              <td><strong>Delimitation</strong></td>
              <td>Noun</td>
              <td>The official process of redrawing electoral constituency boundaries based on census data.</td>
              <td><span class="badge-odia">ନିର୍ବାଚନ ମଣ୍ଡଳୀ ସୀମା ପୁନଃନିର୍ଦ୍ଧାରଣ</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
'''
