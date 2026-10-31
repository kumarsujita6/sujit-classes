# -*- coding: utf-8 -*-
"""Part 2: Section 1 - Visual Blueprint & Detailed Mind Map for Class 8 Science Ch 11."""

PART2_CONTENT = """
    <!-- ========================================== -->
    <!-- SECTION 1: VISUAL BLUEPRINT & MIND MAP    -->
    <!-- ========================================== -->
    <section id="section-1" class="study-section">
      <div class="section-badge"><i class="fa-solid fa-diagram-project"></i> Section 1</div>
      <h2 class="section-title">Visual Blueprint & Conceptual Mind Map</h2>
      <p class="section-description">
        Before diving into the detailed theory, use this visual roadmap and hierarchical mind map to see how celestial motions create the natural clocks of our universe—from the spinning of the Earth that gives us the day, to the orbiting Moon that carves the month, to the grand journey around the Sun that defines the year and its seasons.
      </p>

      <!-- SVG 1: Grand Master Celestial Architecture Flowchart -->
      <div class="svg-container">
        <svg viewBox="0 0 960 480" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="skyGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#091e3a" />
              <stop offset="50%" stop-color="#1e1b4b" />
              <stop offset="100%" stop-color="#0f172a" />
            </linearGradient>
            <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#f59e0b" />
              <stop offset="100%" stop-color="#d97706" />
            </linearGradient>
            <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#38bdf8" />
              <stop offset="100%" stop-color="#0284c7" />
            </linearGradient>
            <linearGradient id="tealGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#2dd4bf" />
              <stop offset="100%" stop-color="#0d9488" />
            </linearGradient>
            <linearGradient id="purpGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#a855f7" />
              <stop offset="100%" stop-color="#6366f1" />
            </linearGradient>
            <filter id="glowLight" x="-20%" y="-20%" width="140%" height="140%">
              <feGaussianBlur stdDeviation="3" result="blur" />
              <feComposite in="SourceGraphic" in2="blur" operator="over" />
            </filter>
          </defs>

          <!-- Outer Background -->
          <rect width="960" height="480" rx="16" fill="url(#skyGrad)" />

          <!-- Background Subtle Constellation Stars -->
          <g fill="#ffffff" opacity="0.4">
            <circle cx="80" cy="60" r="1.5" />
            <circle cx="150" cy="40" r="2" />
            <circle cx="280" cy="85" r="1" />
            <circle cx="450" cy="30" r="2.5" />
            <circle cx="620" cy="55" r="1.5" />
            <circle cx="780" cy="40" r="2" />
            <circle cx="890" cy="70" r="1.5" />
            <circle cx="920" cy="180" r="2" />
            <circle cx="50" cy="220" r="1" />
            <circle cx="130" cy="390" r="2" />
            <circle cx="850" cy="420" r="1.5" />
          </g>

          <!-- Central Title Banner -->
          <rect x="280" y="22" width="400" height="46" rx="23" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.2)" stroke-width="1.5" />
          <text x="480" y="51" fill="#38bdf8" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="18" text-anchor="middle" letter-spacing="1">
            CELESTIAL TIMEKEEPING &amp; CALENDAR ARCHITECTURE
          </text>

          <!-- Pillar 1: EARTH ROTATION -> SOLAR DAY -->
          <g transform="translate(40, 95)">
            <rect width="260" height="180" rx="12" fill="rgba(2, 132, 199, 0.15)" stroke="#0284c7" stroke-width="2" />
            <circle cx="40" cy="35" r="18" fill="url(#blueGrad)" />
            <text x="40" y="41" fill="#ffffff" font-family="'Font Awesome 6 Free'" font-weight="900" font-size="16" text-anchor="middle">&#xf2f1;</text>
            <text x="70" y="32" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="15">EARTH'S ROTATION</text>
            <text x="70" y="48" fill="#93c5fd" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">Spin on Axis (24 Hours)</text>
            <line x1="20" y1="65" x2="240" y2="65" stroke="rgba(255,255,255,0.15)" stroke-width="1" />
            <text x="25" y="88" fill="#e2e8f0" font-family="'Plus Jakarta Sans', sans-serif" font-size="12">• Natural Unit: <tspan fill="#38bdf8" font-weight="700">Mean Solar Day</tspan></text>
            <text x="25" y="108" fill="#e2e8f0" font-family="'Plus Jakarta Sans', sans-serif" font-size="12">• Solar Noon: Shortest Shadow</text>
            <text x="25" y="128" fill="#e2e8f0" font-family="'Plus Jakarta Sans', sans-serif" font-size="12">• Gnomon / Sundial tracking</text>
            <text x="25" y="148" fill="#e2e8f0" font-family="'Plus Jakarta Sans', sans-serif" font-size="12">• Basis of: Daily Clock (24h)</text>
            <rect x="25" y="155" width="210" height="18" rx="4" fill="rgba(56, 189, 248, 0.2)" />
            <text x="130" y="168" fill="#bae6fd" font-family="'Space Grotesk', sans-serif" font-size="10" font-weight="700" text-anchor="middle">24 Hours / 1 Solar Day</text>
          </g>

          <!-- Pillar 2: MOON REVOLUTION -> LUNAR MONTH -->
          <g transform="translate(350, 95)">
            <rect width="260" height="180" rx="12" fill="rgba(168, 85, 247, 0.15)" stroke="#a855f7" stroke-width="2" />
            <circle cx="40" cy="35" r="18" fill="url(#purpGrad)" />
            <text x="40" y="41" fill="#ffffff" font-family="'Font Awesome 6 Free'" font-weight="900" font-size="16" text-anchor="middle">&#xf186;</text>
            <text x="70" y="32" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="15">MOON'S ORBIT</text>
            <text x="70" y="48" fill="#d8b4fe" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">Revolves Earth (29.5 Days)</text>
            <line x1="20" y1="65" x2="240" y2="65" stroke="rgba(255,255,255,0.15)" stroke-width="1" />
            <text x="25" y="88" fill="#e2e8f0" font-family="'Plus Jakarta Sans', sans-serif" font-size="12">• Natural Unit: <tspan fill="#d8b4fe" font-weight="700">Synodic Month</tspan></text>
            <text x="25" y="108" fill="#e2e8f0" font-family="'Plus Jakarta Sans', sans-serif" font-size="12">• 8 Phases: New to Full Moon</text>
            <text x="25" y="128" fill="#e2e8f0" font-family="'Plus Jakarta Sans', sans-serif" font-size="12">• Rises ~50 mins later daily</text>
            <text x="25" y="148" fill="#e2e8f0" font-family="'Plus Jakarta Sans', sans-serif" font-size="12">• 12 Lunar Months = 354 Days</text>
            <rect x="25" y="155" width="210" height="18" rx="4" fill="rgba(168, 85, 247, 0.25)" />
            <text x="130" y="168" fill="#f3e8ff" font-family="'Space Grotesk', sans-serif" font-size="10" font-weight="700" text-anchor="middle">Pure Lunar: 11 Days Short / Year</text>
          </g>

          <!-- Pillar 3: EARTH REVOLUTION -> SOLAR YEAR -->
          <g transform="translate(660, 95)">
            <rect width="260" height="180" rx="12" fill="rgba(245, 158, 11, 0.15)" stroke="#f59e0b" stroke-width="2" />
            <circle cx="40" cy="35" r="18" fill="url(#goldGrad)" />
            <text x="40" y="41" fill="#ffffff" font-family="'Font Awesome 6 Free'" font-weight="900" font-size="16" text-anchor="middle">&#xf185;</text>
            <text x="70" y="32" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="15">EARTH'S REVOLUTION</text>
            <text x="70" y="48" fill="#fde68a" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">Orbits Sun (365.25 Days)</text>
            <line x1="20" y1="65" x2="240" y2="65" stroke="rgba(255,255,255,0.15)" stroke-width="1" />
            <text x="25" y="88" fill="#e2e8f0" font-family="'Plus Jakarta Sans', sans-serif" font-size="12">• Natural Unit: <tspan fill="#fde68a" font-weight="700">Solar Year / Seasons</tspan></text>
            <text x="25" y="108" fill="#e2e8f0" font-family="'Plus Jakarta Sans', sans-serif" font-size="12">• Equinoxes &amp; Solstices</text>
            <text x="25" y="128" fill="#e2e8f0" font-family="'Plus Jakarta Sans', sans-serif" font-size="12">• Uttarayan &amp; Dakshinayan</text>
            <text x="25" y="148" fill="#e2e8f0" font-family="'Plus Jakarta Sans', sans-serif" font-size="12">• Leap Year (+1 day / 4 yrs)</text>
            <rect x="25" y="155" width="210" height="18" rx="4" fill="rgba(245, 158, 11, 0.25)" />
            <text x="130" y="168" fill="#fef3c7" font-family="'Space Grotesk', sans-serif" font-size="10" font-weight="700" text-anchor="middle">Tropical (365.24d) vs Sidereal (365.26d)</text>
          </g>

          <!-- Connecting Arrows down to Calendar Integration -->
          <path d="M 170 275 L 170 315 L 340 315 L 340 330" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4" />
          <path d="M 480 275 L 480 330" fill="none" stroke="#a855f7" stroke-width="2" stroke-dasharray="4,4" />
          <path d="M 790 275 L 790 315 L 620 315 L 620 330" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4" />

          <!-- Bottom Master Synthesis: THE CALENDAR SYSTEMS & SPACE AGE -->
          <g transform="translate(60, 335)">
            <!-- Box 1: Solar Calendar -->
            <rect x="0" y="0" width="260" height="115" rx="10" fill="rgba(15, 23, 42, 0.85)" stroke="#38bdf8" stroke-width="1.5" />
            <text x="130" y="24" fill="#38bdf8" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="13" text-anchor="middle">SOLAR CALENDARS</text>
            <text x="15" y="46" fill="#cbd5e1" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">• Gregorian Calendar (Standard)</text>
            <text x="15" y="64" fill="#cbd5e1" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">• Indian National (Saka) Calendar</text>
            <text x="15" y="82" fill="#cbd5e1" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">• Synchronized directly to seasons</text>
            <text x="15" y="100" fill="#93c5fd" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="600">Leap rule: 100/400 yr century filter</text>

            <!-- Box 2: Luni-Solar Calendar -->
            <rect x="280" y="0" width="280" height="115" rx="10" fill="rgba(15, 23, 42, 0.85)" stroke="#a855f7" stroke-width="1.5" />
            <text x="420" y="24" fill="#d8b4fe" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="13" text-anchor="middle">LUNI-SOLAR SYSTEMS</text>
            <text x="295" y="46" fill="#cbd5e1" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">• Tracks Moon phases for months</text>
            <text x="295" y="64" fill="#cbd5e1" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">• <tspan fill="#f59e0b" font-weight="700">Adhika Maasa</tspan> added every 2-3 yrs</text>
            <text x="295" y="82" fill="#cbd5e1" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">• Amant (New Moon) &amp; Purnimant</text>
            <text x="295" y="100" fill="#f3e8ff" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="600">Festivals: Diwali, Holi, Buddha Purnima</text>

            <!-- Box 3: Space Exploration & Satellites -->
            <rect x="580" y="0" width="260" height="115" rx="10" fill="rgba(15, 23, 42, 0.85)" stroke="#2dd4bf" stroke-width="1.5" />
            <text x="710" y="24" fill="#2dd4bf" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="13" text-anchor="middle">ARTIFICIAL SATELLITES</text>
            <text x="595" y="46" fill="#cbd5e1" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">• ISRO: Vikram Sarabhai's vision</text>
            <text x="595" y="64" fill="#cbd5e1" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">• Cartosat (Bhuvan mapping)</text>
            <text x="595" y="82" fill="#cbd5e1" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">• AstroSat, Aditya-L1, Chandrayaan</text>
            <text x="595" y="100" fill="#99f6e4" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="600">Space junk monitoring &amp; weather</text>
          </g>
        </svg>
        <p class="svg-caption">Figure 1.1: Master Conceptual Architecture of Chapter 11 — How Nature's Cosmic Cycles Form the Foundations of Timekeeping and Human Space Technology.</p>
      </div>

      <!-- Conceptual Mind Map Grid -->
      <div class="mindmap-container">
        <div class="mindmap-root">
          <i class="fa-solid fa-compass"></i> Chapter 11: Keeping Time with the Skies — Comprehensive Mind Map Tree
        </div>

        <div class="mindmap-branches">
          <!-- Branch 1 -->
          <div class="mindmap-branch-card" style="border-top-color: #0284c7;">
            <div class="branch-title"><i class="fa-solid fa-circle-notch" style="color: #0284c7;"></i> 1. Moon Phases &amp; Geometry</div>
            <ul class="branch-list">
              <li><strong>Reflected Sunlight:</strong> The Moon has no light of its own; exactly 50% of the Moon is always illuminated by the Sun.</li>
              <li><strong>Phases Definition:</strong> Changing visible shapes of the bright portion seen from the Earth as it orbits our planet.</li>
              <li><strong>Cycle Duration:</strong> ~29.5 days (one synodic month / lunation from full Moon to full Moon).</li>
              <li><strong>Shukla Paksha (Waxing):</strong> Growing bright portion (New Moon &rarr; Crescent &rarr; Half &rarr; Gibbous &rarr; Full Moon; ~14-15 days).</li>
              <li><strong>Krishna Paksha (Waning):</strong> Shrinking bright portion (Full Moon &rarr; Gibbous &rarr; Half &rarr; Crescent &rarr; New Moon; ~14-15 days).</li>
              <li><strong>50-Minute Daily Shift:</strong> Earth must rotate ~50 minutes extra each day to face the orbital advancing Moon.</li>
              <li><strong>Tidal Locking:</strong> Moon completes 1 rotation on its axis in the exact time it completes 1 orbit around Earth (~27.3 days). Hence, only ONE hemisphere ever faces Earth!</li>
              <li><strong>Why Eclipses Don't Occur Monthly:</strong> Moon's orbit is tilted at ~5° to the ecliptic (Earth's orbit around Sun).</li>
            </ul>
          </div>

          <!-- Branch 2 -->
          <div class="mindmap-branch-card" style="border-top-color: #6366f1;">
            <div class="branch-title"><i class="fa-solid fa-hourglass-half" style="color: #6366f1;"></i> 2. Natural Astronomical Clocks</div>
            <ul class="branch-list">
              <li><strong>The Day (24 Hours):</strong> Earth's rotation on its axis. Mean Solar Day measured from highest solar altitude (shortest shadow) to next.</li>
              <li><strong>The Gnomon Experiment:</strong> Vertical 1-meter stick on flat ground; shortest shadow marks local solar noon.</li>
              <li><strong>The Month (~29.5 Days):</strong> Revolution of the Moon around Earth; full cycle of 8 lunar phases.</li>
              <li><strong>The Year (~365.25 Days):</strong> Revolution of Earth around the Sun causing cyclic progression of seasons.</li>
              <li><strong>Tropical Year (365.2422 Days):</strong> Vernal equinox to vernal equinox; foundation of Gregorian solar calendar.</li>
              <li><strong>Sidereal Year (365.2564 Days):</strong> Return to same star background at sunset; 20 minutes longer than tropical year due to axial precession.</li>
              <li><strong>Gregorian Leap Year Rules:</strong> Add leap day if divisible by 4; skip if divisible by 100; re-add if divisible by 400.</li>
            </ul>
          </div>

          <!-- Branch 3 -->
          <div class="mindmap-branch-card" style="border-top-color: #d97706;">
            <div class="branch-title"><i class="fa-solid fa-calendar-days" style="color: #d97706;"></i> 3. Calendar Systems &amp; Heritage</div>
            <ul class="branch-list">
              <li><strong>Lunar Calendars:</strong> 12 lunar months &times; 29.5 days = 354 days. Falls 11 days short of solar year annually. Seasons drift through months.</li>
              <li><strong>Luni-Solar Calendars:</strong> Keeps lunar months but adds an intercalary month (<tspan style="color:#d97706; font-weight:700;">Adhika Maasa</tspan>) every 32-33 months to re-synchronize with seasons.</li>
              <li><strong>Amant vs. Purnimant:</strong> Amant months run New Moon to New Moon; Purnimant runs Full Moon to Full Moon.</li>
              <li><strong>Indian National Calendar (Saka Era):</strong> Adopted March 22, 1957; designed by Meghnad Saha Calendar Reform Committee; 1 Chaitra begins March 22 (March 21 in leap year).</li>
              <li><strong>Ancient Observations:</strong> Uttarayan (apparent northward march of sunrise, Dec to June) and Dakshinayan (southward march, June to Dec) documented in Taittiriya Samhita &amp; Surya Siddhanta.</li>
              <li><strong>Festivals &amp; Culture:</strong> Diwali, Holi, Buddha Purnima, Eid-ul-Fitr tied to Moon phases. Solar festivals: Makar Sankranti, Bihu, Pongal, Pana Sankranti. Classical music ragas (Chandrakauns) &amp; dance mudras.</li>
            </ul>
          </div>

          <!-- Branch 4 -->
          <div class="mindmap-branch-card" style="border-top-color: #0d9488;">
            <div class="branch-title"><i class="fa-solid fa-satellite" style="color: #0d9488;"></i> 4. Artificial Satellites &amp; Space Tech</div>
            <ul class="branch-list">
              <li><strong>Human-Made Satellites:</strong> Orbiting spacecraft launched into Low Earth Orbit (LEO) and Geostationary Orbit (GEO).</li>
              <li><strong>Core Functions:</strong> Telecommunication, weather monitoring &amp; cyclone tracking, navigation (NavIC/GPS), scientific research.</li>
              <li><strong>ISRO Remote Sensing:</strong> Cartosat constellation providing high-resolution imagery for city planning and Bhuvan GIS portal.</li>
              <li><strong>Pioneering Astronomy Missions:</strong> AstroSat (multi-wavelength space observatory), Aditya-L1 (solar study at L1 point), Chandrayaan 1, 2, 3 (lunar exploration).</li>
              <li><strong>Father of Indian Space:</strong> Dr. Vikram Ambalal Sarabhai (1919-1971), founder of INCOSPAR / ISRO and VSSC.</li>
              <li><strong>Space Junk / Space Debris:</strong> Spent rocket stages and inactive satellites posing collision hazards; mitigated by international deorbit rules &amp; ISRO NETRA.</li>
              <li><strong>Ocean Tides Link:</strong> Gravitational pull of the Moon drives tidal cycles; high tide arrives ~50 minutes later daily, exactly matching moonrise!</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
"""
