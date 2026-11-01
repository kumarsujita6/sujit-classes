# -*- coding: utf-8 -*-
"""
Part 2: Section 1 - Visual Blueprint & Detailed Mind Map
Includes intricate inline responsive SVG mind map (SVG 1), chapter orientation,
the three Big Questions from NCERT NEP 2020, and the holistic Earth philosophy.
"""

PART2_CONTENT = '''
    <!-- ========================================== -->
    <!-- SECTION 1: VISUAL BLUEPRINT & DETAILED MIND MAP -->
    <!-- ========================================== -->
    <section id="sec1">
      <div class="section-header">
        <div class="section-icon"><i class="fa-solid fa-sitemap"></i></div>
        <div class="section-header-text">
          <span class="section-tag">Section 1 &bull; Pedagogical Architecture</span>
          <h2>Visual Blueprint &amp; Detailed Mind Map</h2>
        </div>
      </div>

      <p>
        Welcome to the master exploration of <strong>World Geography: Some Glimpses</strong> (Theme A: India and the World &mdash; Land and the People). In this chapter, we step beyond national borders to discover how our planet functions as an astonishing, unified living system. As ancient Indian wisdom observed in the phrase <em>"Vasudhaiva Kutumbakam"</em> (the whole Earth is one single family) and indigenous traditions worldwide have celebrated Mother Earth (<em>Bh&#363;dev&#299;</em> or <em>Pachamama</em>), natural phenomena thousands of kilometres away directly shape our daily lives in India. For instance, the winds across the distant Southern Indian Ocean steer our monsoon rains, and mineral dust from the Saharan Desert crosses the Atlantic Ocean to fertilize the Amazon Rainforest!
      </p>

      <!-- The Big Questions Box from NCERT -->
      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-circle-question"></i> The Three Big Questions of NCERT Chapter 8</div>
        <p>Before diving into details, keep these three guiding inquiries in mind as outlined by the NCERT textbook:</p>
        <ol>
          <li><strong>What are the unique physical features of the continents?</strong> How do mountains, plateaus, plains, and deserts differ across Asia, Europe, Africa, the Americas, and Australia?</li>
          <li><strong>Why do we need to understand world geography?</strong> How do ocean currents, global winds, and continental landforms regulate life, agriculture, weather, and trade?</li>
          <li><strong>How do human actions trigger severe environmental issues?</strong> In what ways do deforestation, global warming, and pollution disrupt planetary balance &mdash; from coral bleaching in the Pacific to melting glaciers in the Tibetan Plateau?</li>
        </ol>
      </div>

      <!-- MASTER INLINE SVG DIAGRAM 1: CHAPTER VISUAL MIND MAP -->
      <div class="svg-wrapper">
        <svg viewBox="0 0 920 560" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; border-radius:14px;">
          <!-- Defs for gradients, dropshadows, and markers -->
          <defs>
            <linearGradient id="centerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#0284c7" />
              <stop offset="100%" stop-color="#0369a1" />
            </linearGradient>
            <linearGradient id="mapGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#38bdf8" />
              <stop offset="100%" stop-color="#0284c7" />
            </linearGradient>
            <linearGradient id="oceanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#2dd4bf" />
              <stop offset="100%" stop-color="#0f766e" />
            </linearGradient>
            <linearGradient id="asiaGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#c084fc" />
              <stop offset="100%" stop-color="#7e22ce" />
            </linearGradient>
            <linearGradient id="africaGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#fbbf24" />
              <stop offset="100%" stop-color="#b45309" />
            </linearGradient>
            <linearGradient id="americaGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#4ade80" />
              <stop offset="100%" stop-color="#15803d" />
            </linearGradient>
            <linearGradient id="polarGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#f472b6" />
              <stop offset="100%" stop-color="#be123c" />
            </linearGradient>
            <filter id="nodeShadow" x="-20%" y="-20%" width="140%" height="140%">
              <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#0f172a" flood-opacity="0.12" />
            </filter>
            <filter id="centerShadow" x="-25%" y="-25%" width="150%" height="150%">
              <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#0284c7" flood-opacity="0.35" />
            </filter>
          </defs>

          <!-- Outer Decorative Subtle Ring -->
          <circle cx="460" cy="280" r="230" fill="none" stroke="#e2e8f0" stroke-width="1.5" stroke-dasharray="6 6" />

          <!-- Connecting Curved Splines -->
          <!-- To Node 1: Map Projections (Top Center-Left) -->
          <path d="M 460 280 C 420 180, 280 140, 220 100" fill="none" stroke="#0284c7" stroke-width="2.5" stroke-dasharray="4 2" />
          <!-- To Node 2: Oceans & Reefs (Top Center-Right) -->
          <path d="M 460 280 C 500 180, 640 140, 700 100" fill="none" stroke="#0d9488" stroke-width="2.5" stroke-dasharray="4 2" />
          <!-- To Node 3: Asia & Eurasia (Mid-Left) -->
          <path d="M 460 280 C 340 260, 240 260, 140 250" fill="none" stroke="#7e22ce" stroke-width="2.5" />
          <!-- To Node 4: Africa & Nile (Mid-Right) -->
          <path d="M 460 280 C 580 260, 680 260, 780 250" fill="none" stroke="#b45309" stroke-width="2.5" />
          <!-- To Node 5: The Americas (Bottom-Left) -->
          <path d="M 460 280 C 380 380, 280 430, 200 460" fill="none" stroke="#15803d" stroke-width="2.5" stroke-dasharray="4 2" />
          <!-- To Node 6: Australia & Polar (Bottom-Right) -->
          <path d="M 460 280 C 540 380, 640 430, 720 460" fill="none" stroke="#be123c" stroke-width="2.5" stroke-dasharray="4 2" />

          <!-- CENTER NODE: THE LIVING EARTH -->
          <g transform="translate(460, 280)" filter="url(#centerShadow)">
            <circle cx="0" cy="0" r="76" fill="url(#centerGrad)" stroke="#ffffff" stroke-width="3" />
            <circle cx="0" cy="0" r="82" fill="none" stroke="#0284c7" stroke-width="1.5" stroke-dasharray="4 3" opacity="0.6">
              <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="30s" repeatCount="indefinite" />
            </circle>
            <text x="0" y="-16" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="800" text-anchor="middle" letter-spacing="0.05em">OUR LIVING</text>
            <text x="0" y="6" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="800" text-anchor="middle" letter-spacing="0.05em">PLANET EARTH</text>
            <text x="0" y="24" fill="#bae6fd" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="700" text-anchor="middle">Theme A &bull; Ch 8 Glimpses</text>
            <text x="0" y="38" fill="#e0f2fe" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" text-anchor="middle">Bh&#363;dev&#299; &bull; Vasudh&#257;</text>
          </g>

          <!-- NODE 1: MAP PROJECTIONS & DISTORTION (Top Left) -->
          <g transform="translate(220, 100)" filter="url(#nodeShadow)">
            <rect x="-110" y="-45" width="220" height="90" rx="14" fill="#ffffff" stroke="#0284c7" stroke-width="2" />
            <rect x="-110" y="-45" width="220" height="24" rx="14" fill="url(#mapGrad)" />
            <text x="0" y="-29" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">1. MAP PROJECTIONS</text>
            <text x="0" y="-4" fill="#0369a1" font-family="'Plus Jakarta Sans', sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Oblate Spheroid (3D) to Flat (2D)</text>
            <text x="0" y="12" fill="#475569" font-family="'Plus Jakarta Sans', sans-serif" font-size="9.5" text-anchor="middle">&bull; Mercator: Preserves Shape &amp; Angles</text>
            <text x="0" y="26" fill="#475569" font-family="'Plus Jakarta Sans', sans-serif" font-size="9.5" text-anchor="middle">&bull; Polar Flaw: Greenland = Africa myth!</text>
            <text x="0" y="38" fill="#64748b" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" text-anchor="middle">&bull; Robinson &amp; Equal-Area Balances</text>
          </g>

          <!-- NODE 2: OCEANS, CURRENTS & REEFS (Top Right) -->
          <g transform="translate(700, 100)" filter="url(#nodeShadow)">
            <rect x="-110" y="-45" width="220" height="90" rx="14" fill="#ffffff" stroke="#0d9488" stroke-width="2" />
            <rect x="-110" y="-45" width="220" height="24" rx="14" fill="url(#oceanGrad)" />
            <text x="0" y="-29" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">2. OCEANS &amp; CORAL REEFS</text>
            <text x="0" y="-4" fill="#0f766e" font-family="'Plus Jakarta Sans', sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">71% Earth Surface &bull; Heat Sponge</text>
            <text x="0" y="12" fill="#475569" font-family="'Plus Jakarta Sans', sans-serif" font-size="9.5" text-anchor="middle">&bull; Phytoplankton make 50% Planet O&#178;</text>
            <text x="0" y="26" fill="#475569" font-family="'Plus Jakarta Sans', sans-serif" font-size="9.5" text-anchor="middle">&bull; Gulf Stream &amp; Ocean Conveyor Belt</text>
            <text x="0" y="38" fill="#64748b" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" text-anchor="middle">&bull; Great Barrier Reef: Bleaching Crisis</text>
          </g>

          <!-- NODE 3: ASIA & EURASIA (Mid Left) -->
          <g transform="translate(140, 250)" filter="url(#nodeShadow)">
            <rect x="-105" y="-45" width="210" height="90" rx="14" fill="#ffffff" stroke="#7e22ce" stroke-width="2" />
            <rect x="-105" y="-45" width="210" height="24" rx="14" fill="url(#asiaGrad)" />
            <text x="0" y="-29" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">3. ASIA &amp; EURASIA</text>
            <text x="0" y="-4" fill="#6b21a8" font-family="'Plus Jakarta Sans', sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Roof of the World &amp; Steppes</text>
            <text x="0" y="12" fill="#475569" font-family="'Plus Jakarta Sans', sans-serif" font-size="9.5" text-anchor="middle">&bull; Tibetan Plateau: 'Third Pole' Water Tower</text>
            <text x="0" y="26" fill="#475569" font-family="'Plus Jakarta Sans', sans-serif" font-size="9.5" text-anchor="middle">&bull; Gobi Desert: Blue Sky &amp; -30&#176;C winter</text>
            <text x="0" y="38" fill="#64748b" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" text-anchor="middle">&bull; Steppes Grassland Sink &bull; Urals Border</text>
          </g>

          <!-- NODE 4: AFRICA & EUROPE (Mid Right) -->
          <g transform="translate(780, 250)" filter="url(#nodeShadow)">
            <rect x="-105" y="-45" width="210" height="90" rx="14" fill="#ffffff" stroke="#b45309" stroke-width="2" />
            <rect x="-105" y="-45" width="210" height="24" rx="14" fill="url(#africaGrad)" />
            <text x="0" y="-29" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">4. AFRICA &amp; EUROPE</text>
            <text x="0" y="-4" fill="#92400e" font-family="'Plus Jakarta Sans', sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Deserts, Savannahs &amp; Plains</text>
            <text x="0" y="12" fill="#475569" font-family="'Plus Jakarta Sans', sans-serif" font-size="9.5" text-anchor="middle">&bull; Sahara: Ergs, Oases &amp; Fennec Fox</text>
            <text x="0" y="26" fill="#475569" font-family="'Plus Jakarta Sans', sans-serif" font-size="9.5" text-anchor="middle">&bull; Savannah: 1.5M Wildebeest Migration</text>
            <text x="0" y="38" fill="#64748b" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" text-anchor="middle">&bull; River Nile (6,650 km) &bull; European Plain</text>
          </g>

          <!-- NODE 5: THE AMERICAS (Bottom Left) -->
          <g transform="translate(200, 460)" filter="url(#nodeShadow)">
            <rect x="-105" y="-45" width="210" height="90" rx="14" fill="#ffffff" stroke="#15803d" stroke-width="2" />
            <rect x="-105" y="-45" width="210" height="24" rx="14" fill="url(#americaGrad)" />
            <text x="0" y="-29" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">5. THE AMERICAS</text>
            <text x="0" y="-4" fill="#166534" font-family="'Plus Jakarta Sans', sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Rainforests, Canyons &amp; Lakes</text>
            <text x="0" y="12" fill="#475569" font-family="'Plus Jakarta Sans', sans-serif" font-size="9.5" text-anchor="middle">&bull; Amazon: 'Lungs of Earth' &amp; Flying Rivers</text>
            <text x="0" y="26" fill="#475569" font-family="'Plus Jakarta Sans', sans-serif" font-size="9.5" text-anchor="middle">&bull; Atacama: Driest desert &bull; NASA rover tests</text>
            <text x="0" y="38" fill="#64748b" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" text-anchor="middle">&bull; Colorado Grand Canyon (1.8 km deep)</text>
          </g>

          <!-- NODE 6: AUSTRALIA & ANTARCTICA (Bottom Right) -->
          <g transform="translate(720, 460)" filter="url(#nodeShadow)">
            <rect x="-105" y="-45" width="210" height="90" rx="14" fill="#ffffff" stroke="#be123c" stroke-width="2" />
            <rect x="-105" y="-45" width="210" height="24" rx="14" fill="url(#polarGrad)" />
            <text x="0" y="-29" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-size="11.5" font-weight="800" text-anchor="middle">6. AUSTRALIA &amp; POLAR</text>
            <text x="0" y="-4" fill="#9f1239" font-family="'Plus Jakarta Sans', sans-serif" font-size="10.5" font-weight="700" text-anchor="middle">Arid Outback &amp; Polar Deserts</text>
            <text x="0" y="12" fill="#475569" font-family="'Plus Jakarta Sans', sans-serif" font-size="9.5" text-anchor="middle">&bull; Great Australian Desert: Marsupials</text>
            <text x="0" y="26" fill="#475569" font-family="'Plus Jakarta Sans', sans-serif" font-size="9.5" text-anchor="middle">&bull; Spinifex Indigenous: 25,000 yr wisdom</text>
            <text x="0" y="38" fill="#64748b" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" text-anchor="middle">&bull; Antarctica: Earth's Largest &amp; Coldest Desert</text>
          </g>
        </svg>
        <div class="svg-caption">
          <i class="fa-solid fa-bezier-curve"></i>
          <span><strong>Fig 8.1 Master Pedagogical Blueprint:</strong> Conceptual interconnectedness of map projection mathematics, oceanic climate engines, continental physical landforms, and global ecological stewardship.</span>
        </div>
      </div>

      <p>
        Notice how these six domains are not isolated facts to be memorised for an examination; they are interconnected gears of a single planetary clockwork. The heat captured by equatorial oceans powers the atmospheric circulation that creates the arid Sahara and Atacama deserts. In turn, high winds scoop up phosphorus-rich mineral dust from ancient dried lake beds in the Sahara (the Bod&#233;l&#233; Depression), carrying it 5,000 kilometres across the Atlantic to fertilize the nutrient-starved soils of the Amazon Rainforest. Truly, an injury to one part of our Earth is an injury to all!
      </p>
    </section>
'''
