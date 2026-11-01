# -*- coding: utf-8 -*-
"""Part 2: Section 1 - Visual Blueprint, Detailed Mind Map, and Master SVG Architecture Diagrams."""

PART2_CONTENT = """
    <!-- ========================================== -->
    <!-- SECTION 1: VISUAL BLUEPRINT & MIND MAP     -->
    <!-- ========================================== -->
    <section id="sec1" class="section-card">
      <div class="section-header">
        <span class="section-num"><i class="fa-solid fa-sitemap"></i> Section 1</span>
        <h2>Visual Blueprint &amp; Detailed Mind Map</h2>
        <p class="section-sub">
          A high-level architectural overview of NCERT Chapter 1: understanding when Nature becomes a resource, the dual classification systems, the delicate ecological balance between restoration and regeneration, and the roadmap toward ethical planetary stewardship (*Lokasangraha*).
        </p>
      </div>

      <!-- Pedagogical Overview Callout -->
      <div class="callout-box callout-def">
        <i class="fa-solid fa-compass"></i>
        <div class="callout-text">
          <strong class="callout-heading">The Core Chapter Philosophy: From Exploitation to Regeneration</strong>
          In Grade 8 Social Science, we take a giant leap forward from simply listing rivers, rocks, and trees. We investigate <strong>how human society interacts with the living Earth</strong>. As social scientists Christiana Figueres and Tom Rivett-Carnac emphasize, our civilization must transition from a predatory extractive economy to a <strong>regenerative economy</strong>&mdash;an economic model that mimics Nature's own zero-waste cycles, restores damaged biomes, and acts with foresight.
        </div>
      </div>

      <!-- DIAGRAM 1: Tripartite Resource Filter & Classification Matrix -->
      <div class="diagram-wrapper">
        <svg viewBox="0 0 960 560" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="font-family: 'Plus Jakarta Sans', sans-serif;">
          <defs>
            <linearGradient id="bgGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#f8fafc"/>
              <stop offset="100%" stop-color="#f1f5f9"/>
            </linearGradient>
            <linearGradient id="primGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#059669"/>
              <stop offset="100%" stop-color="#047857"/>
            </linearGradient>
            <linearGradient id="secGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#0284c7"/>
              <stop offset="100%" stop-color="#0369a1"/>
            </linearGradient>
            <linearGradient id="warnGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#d97706"/>
              <stop offset="100%" stop-color="#b45309"/>
            </linearGradient>
            <linearGradient id="purpGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#7c3aed"/>
              <stop offset="100%" stop-color="#6d28d9"/>
            </linearGradient>
            <filter id="shadowBox" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
              <feDropShadow dx="2" dy="4" stdDeviation="4" flood-opacity="0.12"/>
            </filter>
          </defs>

          <!-- Outer Background -->
          <rect width="960" height="560" rx="16" fill="url(#bgGrad1)" stroke="#cbd5e1" stroke-width="1.5"/>

          <!-- Title Bar -->
          <rect x="20" y="18" width="920" height="50" rx="10" fill="url(#primGrad)" filter="url(#shadowBox)"/>
          <text x="480" y="50" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-size="20" font-weight="700" text-anchor="middle" letter-spacing="0.5">
            THE ANATOMY OF A NATURAL RESOURCE: FILTERS &amp; CLASSIFICATION ARCHITECTURE
          </text>

          <!-- Left Block: Nature (The Totality of Non-Human Creation) -->
          <g transform="translate(40, 95)">
            <rect width="210" height="200" rx="12" fill="#ffffff" stroke="#10b981" stroke-width="2" filter="url(#shadowBox)"/>
            <rect width="210" height="40" rx="12" fill="#d1fae5"/>
            <text x="105" y="26" fill="#065f46" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="15" text-anchor="middle">
              1. RAW NATURE
            </text>
            <text x="105" y="65" fill="#334155" font-size="12" text-anchor="middle" font-weight="600">Totality of Life &amp; Non-Life</text>
            <text x="105" y="85" fill="#64748b" font-size="11" text-anchor="middle">Exists independently of humans</text>
            <line x1="20" y1="98" x2="190" y2="98" stroke="#e2e8f0" stroke-width="1"/>
            <text x="25" y="120" fill="#1e293b" font-size="11.5">• Deep Ocean Petroleum</text>
            <text x="25" y="140" fill="#1e293b" font-size="11.5">• Wild Forest Timber</text>
            <text x="25" y="160" fill="#1e293b" font-size="11.5">• Underground Aquifers</text>
            <text x="25" y="180" fill="#1e293b" font-size="11.5">• Wind &amp; Solar Radiation</text>
            <text x="105" y="215" fill="#047857" font-size="11" font-weight="700" text-anchor="middle">Neutral Biogeochemical Stuff</text>
          </g>

          <!-- Middle Filter: The Tripartite Human Qualification Filter -->
          <g transform="translate(290, 85)">
            <rect width="260" height="230" rx="12" fill="#ffffff" stroke="#f59e0b" stroke-width="2" filter="url(#shadowBox)"/>
            <rect width="260" height="40" rx="12" fill="#fef3c7"/>
            <text x="130" y="26" fill="#92400e" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="14.5" text-anchor="middle">
              2. THE 3-PARTITE FILTER
            </text>
            
            <!-- Criterion 1 -->
            <rect x="15" y="52" width="230" height="48" rx="8" fill="#fffbeb" stroke="#fde68a" stroke-width="1"/>
            <text x="25" y="70" fill="#b45309" font-size="11.5" font-weight="700">⚙️ Technologically Accessible</text>
            <text x="25" y="88" fill="#64748b" font-size="10.5">Must have tools &amp; engineering to reach</text>

            <!-- Criterion 2 -->
            <rect x="15" y="108" width="230" height="48" rx="8" fill="#fffbeb" stroke="#fde68a" stroke-width="1"/>
            <text x="25" y="126" fill="#b45309" font-size="11.5" font-weight="700">💰 Economically Feasible</text>
            <text x="25" y="144" fill="#64748b" font-size="10.5">Extraction cost &lt; Value generated</text>

            <!-- Criterion 3 -->
            <rect x="15" y="164" width="230" height="48" rx="8" fill="#fffbeb" stroke="#fde68a" stroke-width="1"/>
            <text x="25" y="182" fill="#b45309" font-size="11.5" font-weight="700">🕊️ Culturally Acceptable</text>
            <text x="25" y="200" fill="#64748b" font-size="10.5">Honours sacred groves, traditions &amp; ethics</text>
          </g>

          <!-- Connective Arrow 1 -->
          <path d="M 250 195 L 285 195" stroke="#059669" stroke-width="3" marker-end="url(#arrow)" fill="none"/>
          <polygon points="288,195 278,190 278,200" fill="#059669"/>

          <!-- Connective Arrow 2 -->
          <path d="M 550 195 L 585 195" stroke="#0284c7" stroke-width="3" fill="none"/>
          <polygon points="588,195 578,190 578,200" fill="#0284c7"/>

          <!-- Right Block: Natural Resource Realized -->
          <g transform="translate(590, 95)">
            <rect width="330" height="200" rx="12" fill="#ffffff" stroke="#0284c7" stroke-width="2" filter="url(#shadowBox)"/>
            <rect width="330" height="40" rx="12" fill="#e0f2fe"/>
            <text x="165" y="26" fill="#0369a1" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="15" text-anchor="middle">
              3. NATURAL RESOURCE
            </text>
            <text x="165" y="65" fill="#334155" font-size="12" text-anchor="middle" font-weight="600">Material / Substance with Human Utility</text>
            <line x1="20" y1="78" x2="310" y2="78" stroke="#e2e8f0" stroke-width="1"/>
            <text x="30" y="100" fill="#0369a1" font-weight="700" font-size="12">Dual Classification Branches:</text>
            <rect x="25" y="112" width="135" height="70" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1"/>
            <text x="92" y="130" fill="#15803d" font-weight="700" font-size="11" text-anchor="middle">A. BY UTILITY</text>
            <text x="32" y="148" fill="#334155" font-size="10">• Life Essentials</text>
            <text x="32" y="162" fill="#334155" font-size="10">• Raw Materials</text>
            <text x="32" y="176" fill="#334155" font-size="10">• Energy Sources</text>

            <rect x="170" y="112" width="135" height="70" rx="6" fill="#ede9fe" stroke="#c4b5fd" stroke-width="1"/>
            <text x="237" y="130" fill="#6d28d9" font-weight="700" font-size="11" text-anchor="middle">B. BY NATURE</text>
            <text x="177" y="148" fill="#334155" font-size="10">• Renewable</text>
            <text x="177" y="162" fill="#334155" font-size="10">• Non-Renewable</text>
            <text x="177" y="176" fill="#334155" font-size="10">• Biotic / Abiotic</text>
          </g>

          <!-- Bottom Branch: 4 Key Curricular Themes -->
          <g transform="translate(40, 335)">
            <!-- Box 1: Restoration vs Regeneration -->
            <rect x="0" y="0" width="205" height="195" rx="10" fill="#ffffff" stroke="#10b981" stroke-width="1.5" filter="url(#shadowBox)"/>
            <rect x="0" y="0" width="205" height="32" rx="10" fill="#d1fae5"/>
            <text x="102" y="21" fill="#065f46" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="12.5" text-anchor="middle">ECOLOGICAL DYNAMICS</text>
            <text x="12" y="52" fill="#047857" font-weight="700" font-size="11.5">Restoration:</text>
            <text x="12" y="68" fill="#475569" font-size="10.5">Healing damage back to original baseline state.</text>
            <text x="12" y="92" fill="#047857" font-weight="700" font-size="11.5">Regeneration:</text>
            <text x="12" y="108" fill="#475569" font-size="10.5">Creating new life &amp; self-propagating vitality.</text>
            <text x="12" y="135" fill="#b91c1c" font-weight="700" font-size="11">The Golden Rule:</text>
            <text x="12" y="152" fill="#1e293b" font-size="10.5">Harvest Rate &le; Replenish Rate</text>
            <text x="12" y="172" fill="#64748b" font-size="10">Overshoot = Depletion</text>
          </g>

          <g transform="translate(265, 335)">
            <!-- Box 2: Spatial Distribution & Paradox of Plenty -->
            <rect x="0" y="0" width="205" height="195" rx="10" fill="#ffffff" stroke="#0284c7" stroke-width="1.5" filter="url(#shadowBox)"/>
            <rect x="0" y="0" width="205" height="32" rx="10" fill="#e0f2fe"/>
            <text x="102" y="21" fill="#0369a1" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="12.5" text-anchor="middle">PARADOX OF PLENTY</text>
            <text x="12" y="52" fill="#0369a1" font-weight="700" font-size="11.5">Resource Curse:</text>
            <text x="12" y="68" fill="#475569" font-size="10.5">Mineral wealth &ne; Automatic prosperity.</text>
            <text x="12" y="92" fill="#0369a1" font-weight="700" font-size="11.5">The Solution:</text>
            <text x="12" y="108" fill="#475569" font-size="10.5">Invest in human skills &amp; value-adding industries.</text>
            <text x="12" y="135" fill="#0284c7" font-weight="700" font-size="11">Historical Proof:</text>
            <text x="12" y="152" fill="#1e293b" font-size="10.5">Wootz Steel Crucible Tech</text>
            <text x="12" y="172" fill="#64748b" font-size="10">Iron ore + carbon nanotubes</text>
          </g>

          <g transform="translate(490, 335)">
            <!-- Box 3: Real Crises & Caselets -->
            <rect x="0" y="0" width="205" height="195" rx="10" fill="#ffffff" stroke="#e11d48" stroke-width="1.5" filter="url(#shadowBox)"/>
            <rect x="0" y="0" width="205" height="32" rx="10" fill="#ffe4e6"/>
            <text x="102" y="21" fill="#be123c" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="12.5" text-anchor="middle">EXPLOITATION CRISES</text>
            <text x="12" y="52" fill="#be123c" font-weight="700" font-size="11.5">Punjab Water Crisis:</text>
            <text x="12" y="68" fill="#475569" font-size="10.5">HYV paddy + free power &rarr; 80% overexploited aquifers.</text>
            <text x="12" y="100" fill="#be123c" font-weight="700" font-size="11.5">Cement Industry:</text>
            <text x="12" y="116" fill="#475569" font-size="10.5">Limestone mining, heavy CO₂ &amp; toxic fine dust (PM2.5).</text>
            <text x="12" y="148" fill="#991b1b" font-weight="700" font-size="11">Transboundary Tensions:</text>
            <text x="12" y="165" fill="#1e293b" font-size="10.5">Kaveri river interstate dispute</text>
          </g>

          <g transform="translate(715, 335)">
            <!-- Box 4: Sustainable Future & Leadership -->
            <rect x="0" y="0" width="205" height="195" rx="10" fill="#ffffff" stroke="#7c3aed" stroke-width="1.5" filter="url(#shadowBox)"/>
            <rect x="0" y="0" width="205" height="32" rx="10" fill="#ede9fe"/>
            <text x="102" y="21" fill="#6d28d9" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="12.5" text-anchor="middle">REGENERATIVE PATH</text>
            <text x="12" y="52" fill="#6d28d9" font-weight="700" font-size="11.5">Ancient Agro-Botany:</text>
            <text x="12" y="68" fill="#475569" font-size="10.5">Vrikshayurveda of Surapala: seed care &amp; soil moisture.</text>
            <text x="12" y="100" fill="#6d28d9" font-weight="700" font-size="11.5">Sikkim 100% Organic:</text>
            <text x="12" y="116" fill="#475569" font-size="10.5">+20% income, biodiversity surge.</text>
            <text x="12" y="145" fill="#6d28d9" font-weight="700" font-size="11">Global Solar Champion:</text>
            <text x="12" y="162" fill="#1e293b" font-size="10.5">Bhadla Solar Park &amp; ISA</text>
            <text x="12" y="179" fill="#5b21b6" font-size="10">Ethic of Lokasangraha</text>
          </g>
        </svg>
        <p class="diagram-caption">
          <strong>Figure 1.1:</strong> Conceptual Flowchart of Natural Resources &mdash; illustrating the transition from raw environmental matter to functional resources via the Tripartite Filter, followed by the four pillars of ecological dynamics, socioeconomic distribution, industrial crises, and regenerative stewardship.
        </p>
      </div>

      <!-- Mind Map Structured Cards -->
      <h3 class="topic-title"><i class="fa-solid fa-brain"></i> Chapter Architectural Mind Map</h3>
      <p>
        To master this chapter for CBSE Class 8 examinations and competitive foundations, follow this structured, five-dimensional cognitive breakdown:
      </p>

      <div class="card-grid">
        <!-- Card 1 -->
        <div class="card" style="border-top: 4px solid var(--primary);">
          <h4 class="sub-topic"><i class="fa-solid fa-leaf" style="color: var(--primary);"></i> 1. The Nature-Resource Continuum</h4>
          <p style="font-size: 0.93rem; color: var(--text);">
            • <strong>Nature:</strong> The totality of biotic (living) and abiotic (non-living) entities created without human intervention.<br>
            • <strong>Resource Transformation:</strong> Elements become resources only when humans possess the <strong>technology</strong> to extract them, the <strong>capital</strong> to make it profitable, and the <strong>cultural consent</strong> to use them ethically.<br>
            • <strong>Indigenous Reverence:</strong> Traditional worldviews view Nature as an affectionate mother and nourisher (*Mata Prithvi*), celebrating sacred groves (*Devrais*) and performing daily rituals like *Tulasi Puja* and *Arghyam to Surya*.
          </p>
        </div>

        <!-- Card 2 -->
        <div class="card" style="border-top: 4px solid var(--secondary);">
          <h4 class="sub-topic"><i class="fa-solid fa-arrows-spin" style="color: var(--secondary);"></i> 2. Restoration vs Regeneration</h4>
          <p style="font-size: 0.93rem; color: var(--text);">
            • <strong>Restoration:</strong> Healing back to an original baseline state after damage (e.g., skin wound healing, natural river re-aeration, re-planting cleared forest patches).<br>
            • <strong>Regeneration:</strong> The proactive capacity of living ecosystems to create new life, build deep topsoil, and evolve thriving conditions for biological communities.<br>
            • <strong>The Renewable Condition:</strong> A resource remains renewable <em>only if</em> the human rate of harvest remains strictly below or equal to Nature's speed of replenishment.
          </p>
        </div>

        <!-- Card 3 -->
        <div class="card" style="border-top: 4px solid var(--accent);">
          <h4 class="sub-topic"><i class="fa-solid fa-scale-unbalanced" style="color: var(--accent);"></i> 3. Spatial Distribution &amp; Paradox of Plenty</h4>
          <p style="font-size: 0.93rem; color: var(--text);">
            • <strong>Uneven Geography:</strong> Minerals and fuels are clustered due to geological history (e.g., coal in Jharkhand/Odisha, crude oil in Assam &amp; Mumbai High, iron in Bastar &amp; Keonjhar).<br>
            • <strong>Transboundary Tensions:</strong> Rivers ignore political state lines, leading to intense interstate disputes (e.g., Kaveri river among Karnataka, Tamil Nadu, Kerala, and Puducherry).<br>
            • <strong>Paradox of Plenty:</strong> Regions blessed with abundant natural treasures often suffer from poverty if they merely export raw rocks without developing local manufacturing, technical skills, and schools.
          </p>
        </div>

        <!-- Card 4 -->
        <div class="card" style="border-top: 4px solid var(--rose);">
          <h4 class="sub-topic"><i class="fa-solid fa-triangle-exclamation" style="color: var(--rose);"></i> 4. Two Real-World Crises</h4>
          <p style="font-size: 0.93rem; color: var(--text);">
            • <strong>Punjab Groundwater Depletion:</strong> Post-1960 Green Revolution monoculture of water-guzzling paddy supported by free electric power pushed deep tubewells past 40 meters below ground level (m bgl), leaving nearly 80% of blocks severely over-exploited.<br>
            • <strong>The Cement Dilemma:</strong> Indispensable for modern urban housing and bridges, but ranks among the most polluting industries due to intense calcination CO₂ emissions, heavy quarrying, and toxic PM2.5/PM10 fine dust choking lungs and foliage.
          </p>
        </div>

        <!-- Card 5 -->
        <div class="card" style="border-top: 4px solid var(--purple);">
          <h4 class="sub-topic"><i class="fa-solid fa-sun" style="color: var(--purple);"></i> 5. The Regenerative Renaissance</h4>
          <p style="font-size: 0.93rem; color: var(--text);">
            • <strong>Vrikshayurveda of Surapala:</strong> 10th-century CE botanical science advocating zero-chemical farming, soil moisture preservation, microbial nourishment, and natural pest repellents (neem, garlic).<br>
            • <strong>Sikkim 100% Organic State:</strong> Certified fully organic in 2016, proving ecological detox boosts farmer incomes (+20%) and revives pollinator populations.<br>
            • <strong>Solar Leadership:</strong> Rajasthan's Bhadla Solar Park (2,245+ MW) and the India-France International Solar Alliance (ISA) leading 120+ nations under the universal ethic of *Lokasangraha*.
          </p>
        </div>
      </div>

      <!-- DIAGRAM 2: The Restoration vs Regeneration Dynamics & Human Disruption Loop -->
      <div class="diagram-wrapper">
        <svg viewBox="0 0 960 480" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="font-family: 'Plus Jakarta Sans', sans-serif;">
          <defs>
            <linearGradient id="restGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#10b981"/>
              <stop offset="100%" stop-color="#047857"/>
            </linearGradient>
            <linearGradient id="regenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#0284c7"/>
              <stop offset="100%" stop-color="#0369a1"/>
            </linearGradient>
            <linearGradient id="dangerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#ef4444"/>
              <stop offset="100%" stop-color="#b91c1c"/>
            </linearGradient>
          </defs>

          <!-- Outer Container -->
          <rect width="960" height="480" rx="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>

          <rect x="20" y="16" width="920" height="44" rx="8" fill="#1e293b"/>
          <text x="480" y="44" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-size="18" font-weight="700" text-anchor="middle">
            THE REGENERATIVE RHYTHM: NATURE'S BALANCED CYCLE VS. HUMAN OVER-EXTRACTION SPIRAL
          </text>

          <!-- Left Circle: Nature's Balanced Cycles -->
          <g transform="translate(60, 85)">
            <rect width="390" height="360" rx="14" fill="#ffffff" stroke="#10b981" stroke-width="2" filter="url(#shadowBox)"/>
            <rect width="390" height="38" rx="14" fill="#d1fae5"/>
            <text x="195" y="25" fill="#065f46" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="15" text-anchor="middle">
              A. HEALTHY NATURAL EQUILIBRIUM (RATE IN &ge; RATE OUT)
            </text>

            <!-- Circular Cycle Representation -->
            <circle cx="195" cy="180" r="105" fill="none" stroke="#a7f3d0" stroke-width="8" stroke-dasharray="10 6"/>
            
            <!-- Nodes in the Balanced Cycle -->
            <!-- Top: Growth -->
            <rect x="135" y="85" width="120" height="42" rx="8" fill="#ecfdf5" stroke="#10b981" stroke-width="1.5"/>
            <text x="195" y="104" fill="#065f46" font-weight="700" font-size="11.5" text-anchor="middle">1. Plant Growth</text>
            <text x="195" y="119" fill="#047857" font-size="9.5" text-anchor="middle">Photosynthesis &amp; Rain</text>

            <!-- Right: Natural Death / Utilization -->
            <rect x="255" y="160" width="125" height="42" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
            <text x="317" y="179" fill="#1e3a8a" font-weight="700" font-size="11.5" text-anchor="middle">2. Gentle Harvest</text>
            <text x="317" y="194" fill="#1d4ed8" font-size="9.5" text-anchor="middle">Within carrying capacity</text>

            <!-- Bottom: Decomposition -->
            <rect x="135" y="235" width="120" height="42" rx="8" fill="#faf5ff" stroke="#a855f7" stroke-width="1.5"/>
            <text x="195" y="254" fill="#581c87" font-weight="700" font-size="11.5" text-anchor="middle">3. Decomposition</text>
            <text x="195" y="269" fill="#7e22ce" font-size="9.5" text-anchor="middle">Fungi &amp; Microbes</text>

            <!-- Left: Topsoil & Aquifer Recharge -->
            <rect x="10" y="160" width="125" height="42" rx="8" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.5"/>
            <text x="72" y="179" fill="#78350f" font-weight="700" font-size="11.5" text-anchor="middle">4. Soil Rejuvenation</text>
            <text x="72" y="194" fill="#b45309" font-size="9.5" text-anchor="middle">Humus &amp; Clean Water</text>

            <!-- Center Core -->
            <circle cx="195" cy="180" r="32" fill="#047857"/>
            <text x="195" y="177" fill="#ffffff" font-weight="800" font-size="10.5" text-anchor="middle">ZERO</text>
            <text x="195" y="191" fill="#ffffff" font-weight="800" font-size="10.5" text-anchor="middle">WASTE</text>

            <rect x="25" y="305" width="340" height="42" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1"/>
            <text x="195" y="323" fill="#166534" font-size="11" font-weight="700" text-anchor="middle">Result: Sustainable &amp; Eternally Renewable</text>
            <text x="195" y="338" fill="#15803d" font-size="10" text-anchor="middle">Nature heals wounds (Restoration) &amp; flourishes (Regeneration)</text>
          </g>

          <!-- Right Circle: The Over-Extraction Spiral -->
          <g transform="translate(510, 85)">
            <rect width="390" height="360" rx="14" fill="#ffffff" stroke="#ef4444" stroke-width="2" filter="url(#shadowBox)"/>
            <rect width="390" height="38" rx="14" fill="#ffe4e6"/>
            <text x="195" y="25" fill="#9f1239" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="15" text-anchor="middle">
              B. OVERSHOOT SPIRAL (RATE OUT &gt;&gt; RATE IN)
            </text>

            <!-- Broken Cycle Line -->
            <circle cx="195" cy="180" r="105" fill="none" stroke="#fecdd3" stroke-width="8" stroke-dasharray="14 10"/>

            <!-- Broken Nodes -->
            <rect x="135" y="85" width="120" height="42" rx="8" fill="#fff1f2" stroke="#f43f5e" stroke-width="1.5"/>
            <text x="195" y="104" fill="#9f1239" font-weight="700" font-size="11.5" text-anchor="middle">1. Excessive Pumping</text>
            <text x="195" y="119" fill="#be123c" font-size="9.5" text-anchor="middle">Tubewells &gt;40m bgl</text>

            <rect x="255" y="160" width="125" height="42" rx="8" fill="#fff1f2" stroke="#f43f5e" stroke-width="1.5"/>
            <text x="317" y="179" fill="#9f1239" font-weight="700" font-size="11.5" text-anchor="middle">2. Toxic Effluents</text>
            <text x="317" y="194" fill="#be123c" font-size="9.5" text-anchor="middle">Undegradable chemicals</text>

            <rect x="135" y="235" width="120" height="42" rx="8" fill="#fff1f2" stroke="#f43f5e" stroke-width="1.5"/>
            <text x="195" y="254" fill="#9f1239" font-weight="700" font-size="11.5" text-anchor="middle">3. Microbial Death</text>
            <text x="195" y="269" fill="#be123c" font-size="9.5" text-anchor="middle">Soil salinization &amp; poison</text>

            <rect x="10" y="160" width="125" height="42" rx="8" fill="#fff1f2" stroke="#f43f5e" stroke-width="1.5"/>
            <text x="72" y="179" fill="#9f1239" font-weight="700" font-size="11.5" text-anchor="middle">4. Aquifer Collapse</text>
            <text x="72" y="194" fill="#be123c" font-size="9.5" text-anchor="middle">Dry borewells &amp; cracks</text>

            <!-- Center Core Alert -->
            <circle cx="195" cy="180" r="32" fill="#b91c1c"/>
            <text x="195" y="177" fill="#ffffff" font-weight="800" font-size="10" text-anchor="middle">CYCLE</text>
            <text x="195" y="191" fill="#ffffff" font-weight="800" font-size="10" text-anchor="middle">BROKEN</text>

            <rect x="25" y="305" width="340" height="42" rx="6" fill="#fef2f2" stroke="#fca5a5" stroke-width="1"/>
            <text x="195" y="323" fill="#991b1b" font-size="11" font-weight="700" text-anchor="middle">Result: Renewable becomes Non-Renewable!</text>
            <text x="195" y="338" fill="#b91c1c" font-size="10" text-anchor="middle">Aquifer recharge takes centuries; fertile soil turns sterile</text>
          </g>
        </svg>
        <p class="diagram-caption">
          <strong>Figure 1.2:</strong> The Regenerative Rhythm vs. The Human Overshoot Spiral &mdash; demonstrating how natural restorative cycles maintain zero waste, and how extraction rates exceeding natural replenishment transform what is today a renewable resource into an exhausted, non-renewable asset tomorrow.
        </p>
      </div>
    </section>
"""
