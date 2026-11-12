# -*- coding: utf-8 -*-
"""
Section 3: Rapid Revision Fact & Formula/Law Bank
for Class 8 Science Chapter 6: Pressure, Winds, Storms, and Cyclones
"""

def get_section3():
    return '''
    <!-- SECTION 3: RAPID REVISION FACT & FORMULA/LAW BANK -->
    <section class="study-section" id="sec3">
      <div id="section-3"></div>
      <div class="section-header">
        <span class="section-tag">Quick-Reference Knowledge Vault &bull; High-Yield Fact Bank</span>
        <h2 class="section-title">
          <i class="fa-solid fa-table-list"></i>
          Section 3: Rapid Revision Fact &amp; Formula/Law Bank
        </h2>
        <p class="section-desc">
          Structured comparative tables, SI metric conventions, atmospheric pressure constants, and electrodynamic storm mechanics for instant exam recall.
        </p>
      </div>

      <!-- TABLE 1: FORMULAS AND QUANTITIES -->
      <h3 class="subheading"><i class="fa-solid fa-square-root-variable"></i> Table 3.1: Fundamental Formulas, Physical Quantities &amp; SI Units</h3>
      <div class="table-wrapper">
        <table class="data-table">
          <thead>
            <tr>
              <th>Physical Quantity</th>
              <th>Symbol</th>
              <th>Governing Formula</th>
              <th>SI Unit &amp; Symbol</th>
              <th>Standard Equivalents / Reference Values</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Mechanical Pressure</strong></td>
              <td><span class="math-entity">P</span></td>
              <td><span class="math-entity">P = F / A</span> (Thrust &divide; Area)</td>
              <td>Pascal (<span class="math-entity">Pa</span>) or <span class="math-entity">N/m&sup2;</span></td>
              <td><span class="math-entity">1 Pa = 1 N/m&sup2;</span>; named after Blaise Pascal.</td>
            </tr>
            <tr>
              <td><strong>Applied Thrust (Force)</strong></td>
              <td><span class="math-entity">F</span></td>
              <td><span class="math-entity">F = P &times; A</span></td>
              <td>Newton (<span class="math-entity">N</span>)</td>
              <td><span class="math-entity">1 N = 1 kg&middot;m/s&sup2;</span> (force to accelerate 1 kg by 1 m/s&sup2;).</td>
            </tr>
            <tr>
              <td><strong>Contact Surface Area</strong></td>
              <td><span class="math-entity">A</span></td>
              <td><span class="math-entity">A = F / P</span></td>
              <td>Square metre (<span class="math-entity">m&sup2;</span>)</td>
              <td><span class="math-entity">1 m&sup2; = 10,000 cm&sup2; = 1,000,000 mm&sup2;</span>.</td>
            </tr>
            <tr>
              <td><strong>Hydrostatic Depth Pressure</strong></td>
              <td><span class="math-entity">P</span></td>
              <td><span class="math-entity">P = h &times; &rho; &times; g</span></td>
              <td>Pascal (<span class="math-entity">Pa</span>)</td>
              <td><span class="math-entity">h</span> = liquid height (m), <span class="math-entity">&rho;</span> = density (1000 kg/m&sup3; for water), <span class="math-entity">g</span> = 9.8 m/s&sup2;.</td>
            </tr>
            <tr>
              <td><strong>Standard Sea-Level Air Pressure</strong></td>
              <td><span class="math-entity">P<sub>atm</sub></span></td>
              <td><span class="math-entity">P<sub>atm</sub> = &rho;<sub>Hg</sub> &times; g &times; h</span></td>
              <td>Pascal (<span class="math-entity">Pa</span>)</td>
              <td><span class="math-entity">101.325 kPa = 1.013 bar = 760 mm of Hg</span>.</td>
            </tr>
            <tr>
              <td><strong>Atmospheric Force on Palm (15&times;15 cm)</strong></td>
              <td><span class="math-entity">F</span></td>
              <td><span class="math-entity">F = 101,325 &times; 0.0225 m&sup2;</span></td>
              <td>Newton (<span class="math-entity">N</span>)</td>
              <td><strong>~2,250 N</strong> (equivalent to weight of 225 kg mass).</td>
            </tr>
            <tr>
              <td><strong>Lightning Channel Temperature</strong></td>
              <td><span class="math-entity">T</span></td>
              <td>Thermal plasma excitation</td>
              <td>Kelvin (<span class="math-entity">K</span>) or &deg;C</td>
              <td><strong>Up to ~30,000 &deg;C</strong> (~5 times hotter than Sun's surface).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 2: HIGH PRESSURE VS LOW PRESSURE -->
      <h3 class="subheading"><i class="fa-solid fa-gauge-high"></i> Table 3.2: High-Pressure vs Low-Pressure Atmospheric Systems</h3>
      <div class="table-wrapper">
        <table class="data-table">
          <thead>
            <tr>
              <th>Feature / Parameter</th>
              <th>High-Pressure System (Anticyclone)</th>
              <th>Low-Pressure System (Cyclone / Depression)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Vertical Air Motion</strong></td>
              <td>Air gently sinks (subsides) downward toward the surface.</td>
              <td>Air rapidly warms, expands, and surges upward (buoyant updrafts).</td>
            </tr>
            <tr>
              <td><strong>Thermal State</strong></td>
              <td>Cooler, dense, heavier air mass.</td>
              <td>Warmer, moist, lighter air mass.</td>
            </tr>
            <tr>
              <td><strong>Surface Wind Direction</strong></td>
              <td>Winds diverge outward from the centre.</td>
              <td>Winds converge inward toward the central low-pressure core.</td>
            </tr>
            <tr>
              <td><strong>Cloud Formation</strong></td>
              <td>Sinking air compresses and warms; suppresses condensation and clouds.</td>
              <td>Rising moist air expands and cools; rapid condensation creates clouds.</td>
            </tr>
            <tr>
              <td><strong>Associated Weather</strong></td>
              <td>Dry, fair, clear sunny skies with gentle, calm breezes.</td>
              <td>Overcast, stormy, gusty winds, heavy rainfall, or severe cyclonic storms.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 3: SEA BREEZE VS LAND BREEZE -->
      <h3 class="subheading"><i class="fa-solid fa-arrows-left-right"></i> Table 3.3: Sea Breeze vs Land Breeze Comparative Matrix</h3>
      <div class="table-wrapper">
        <table class="data-table">
          <thead>
            <tr>
              <th>Comparison Factor</th>
              <th>Sea Breeze (ସମୁଦ୍ର ବାୟୁ)</th>
              <th>Land Breeze (ସ୍ଥଳ ବାୟୁ)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Time of Occurrence</strong></td>
              <td>Daytime (peaks in late afternoon, 1:00 PM to 4:00 PM).</td>
              <td>Nighttime (develops late at night and continues until sunrise).</td>
            </tr>
            <tr>
              <td><strong>Primary Thermal Driver</strong></td>
              <td>Land absorbs solar radiation and heats up much faster than water.</td>
              <td>Land radiates heat into space and cools down much faster than the sea.</td>
            </tr>
            <tr>
              <td><strong>Low-Pressure Location</strong></td>
              <td>Located over the <strong>Land</strong> (warm air rises over land).</td>
              <td>Located over the <strong>Sea</strong> (warm water warms overlying air).</td>
            </tr>
            <tr>
              <td><strong>High-Pressure Location</strong></td>
              <td>Located over the <strong>Sea</strong> (cooler, denser maritime air).</td>
              <td>Located over the <strong>Land</strong> (cooler, denser terrestrial air).</td>
            </tr>
            <tr>
              <td><strong>Surface Wind Trajectory</strong></td>
              <td><strong>From Sea to Land</strong> (onshore wind).</td>
              <td><strong>From Land to Sea</strong> (offshore wind).</td>
            </tr>
            <tr>
              <td><strong>Ecological &amp; Human Impact</strong></td>
              <td>Brings pleasant relief from scorching summer heat; bends coastal trees inland.</td>
              <td>Allows traditional coastal fishermen to sail their boats out to sea easily before dawn.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 4: THUNDERSTORM VS CYCLONE -->
      <h3 class="subheading"><i class="fa-solid fa-cloud-bolt"></i> Table 3.4: Thunderstorm vs Tropical Cyclone Comparative Taxonomy</h3>
      <div class="table-wrapper">
        <table class="data-table">
          <thead>
            <tr>
              <th>Diagnostic Criterion</th>
              <th>Thunderstorm (ଘଡ଼ଘଡ଼ି ଝଡ଼)</th>
              <th>Tropical Cyclone (ବାତ୍ୟା / ଘୂର୍ଣ୍ଣିଝଡ଼)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Geographical Scale</strong></td>
              <td>Localized phenomenon (typically 5 to 25 km across).</td>
              <td>Colossal synoptic system (typically 300 to 1,000 km across).</td>
            </tr>
            <tr>
              <td><strong>Lifespan &amp; Duration</strong></td>
              <td>Short-lived: typically lasting 30 minutes to 2 hours.</td>
              <td>Long-lived: survives for several days to over two weeks.</td>
            </tr>
            <tr>
              <td><strong>Genesis Location</strong></td>
              <td>Can form over land or water wherever humid updrafts exist.</td>
              <td>Forms <strong>strictly over warm tropical oceans</strong> (sea temperature &ge; 27 &deg;C).</td>
            </tr>
            <tr>
              <td><strong>Primary Energy Source</strong></td>
              <td>Surface solar thermal updrafts and moisture condensation.</td>
              <td>Vast reservoirs of <strong>latent heat of condensation</strong> released by evaporating sea water.</td>
            </tr>
            <tr>
              <td><strong>Rotational Organization</strong></td>
              <td>Lacks large-scale planetary rotation (no organized eye).</td>
              <td>Highly organized vortex spun by Coriolis force; features a calm central <strong>Eye</strong>.</td>
            </tr>
            <tr>
              <td><strong>Peak Wind Speeds</strong></td>
              <td>Gusts typically 50 to 90 km/h.</td>
              <td>Catastrophic sustained winds ranging from 120 km/h to over 270 km/h.</td>
            </tr>
            <tr>
              <td><strong>Primary Lethal Hazards</strong></td>
              <td>Deadly lightning strikes, localized flash floods, and hailstones.</td>
              <td>Massive coastal <strong>Storm Surges (3-12 m)</strong>, widespread regional inundation, roof devastation.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 5: LIGHTNING SAFETY RULES -->
      <h3 class="subheading"><i class="fa-solid fa-shield-halved"></i> Table 3.5: Lightning Safety Protocol: Outdoor vs Indoor Survival Matrix</h3>
      <div class="table-wrapper">
        <table class="data-table">
          <thead>
            <tr>
              <th>Setting / Location</th>
              <th>Strict Life-Saving Action (DO)</th>
              <th>Fatal Mistake to Avoid (DON'T)</th>
              <th>Underlying Scientific Reason</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Open Field / Farmland</strong></td>
              <td>Squat low in a "Lightning Crouch": feet together, head tucked between knees, hands over ears.</td>
              <td><strong>DO NOT lie flat on the ground!</strong> DO NOT stand tall as the highest object!</td>
              <td>Lying flat increases ground surface contact with lethal radial ground currents. Crouching minimizes your height while keeping ground contact to a tiny footprint.</td>
            </tr>
            <tr>
              <td><strong>Near Trees / Forest</strong></td>
              <td>Seek shelter under a dense stand of short, stunted bushes or small trees.</td>
              <td><strong>NEVER stand under an isolated, tall solitary tree!</strong></td>
              <td>Tall solitary trees act as natural lightning arresters. Lightning vaporizes sap inside the trunk, exploding the wood and jumping horizontally (side-flash) into people nearby.</td>
            </tr>
            <tr>
              <td><strong>Rainy Weather Gear</strong></td>
              <td>Wear a synthetic or plastic raincoat without exposed metal snaps.</td>
              <td><strong>DO NOT carry an umbrella with a pointed metal tip!</strong></td>
              <td>The elevated metallic rod of an umbrella acts like a miniature lightning rod directly above your head, attracting the electrical leader.</td>
            </tr>
            <tr>
              <td><strong>Inside a Car or Bus</strong></td>
              <td>Stay completely inside the vehicle with all glass windows rolled up tightly.</td>
              <td>DO NOT step outside into the open; do not touch exposed metal door handles.</td>
              <td>The closed metallic body acts as a <strong>Faraday Cage</strong>. Electrical charges travel harmlessly around the outer metal shell and discharge through tyres into the ground without penetrating the passenger cabin.</td>
            </tr>
            <tr>
              <td><strong>Inside a House / School</strong></td>
              <td>Unplug delicate electronics; stay away from windows; use mobile/cordless phones only.</td>
              <td><strong>DO NOT take a shower, wash dishes, or use corded landline phones!</strong></td>
              <td>Lightning currents can travel long distances along copper plumbing pipes, wired electrical circuits, and telephone landlines.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 6: HISTORICAL CYCLONES IN INDIA & ODISHA -->
      <h3 class="subheading"><i class="fa-solid fa-landmark"></i> Table 3.6: Historic Severe Tropical Cyclones Affecting India &amp; Odisha</h3>
      <div class="table-wrapper">
        <table class="data-table">
          <thead>
            <tr>
              <th>Cyclone Name</th>
              <th>Year</th>
              <th>Peak Wind Speed</th>
              <th>Primary Impact Region</th>
              <th>Key Lessons &amp; Disaster Management Evolution</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>1999 Odisha Super Cyclone</strong></td>
              <td>1999 (Oct)</td>
              <td>260 &ndash; 270 km/h</td>
              <td>Odisha Coast (Jagatsinghpur, Paradip, Kendrapara)</td>
              <td>Category 5 storm surge (>7 m) caused tragic loss of ~10,000 lives. Prompted Odisha to pioneer the <strong>OSDMA</strong> (Odisha State Disaster Management Authority), building hundreds of cyclone shelters.</td>
            </tr>
            <tr>
              <td><strong>Cyclone Phailin</strong></td>
              <td>2013 (Oct)</td>
              <td>215 &ndash; 225 km/h</td>
              <td>Gopalpur, Southern Odisha &amp; North Andhra Pradesh</td>
              <td>Global benchmark in disaster evacuation: over 1 million citizens moved to cyclone shelters in 48 hours; zero casualty mission praised by the United Nations.</td>
            </tr>
            <tr>
              <td><strong>Cyclone Hudhud</strong></td>
              <td>2014 (Oct)</td>
              <td>185 &ndash; 205 km/h</td>
              <td>Visakhapatnam (Andhra) &amp; Southern Odisha</td>
              <td>Heavy urban infrastructure damage; underlined the need for underground electrical cabling and Doppler radar coastal surveillance.</td>
            </tr>
            <tr>
              <td><strong>Cyclone Fani</strong></td>
              <td>2019 (May)</td>
              <td>215 &ndash; 250 km/h</td>
              <td>Puri, Bhubaneswar, Cuttack (Odisha)</td>
              <td>Extremely rare, severe pre-monsoon cyclone. High winds uprooted millions of trees and destroyed the electrical grid; 1.2 million people safely evacuated within 24 hours.</td>
            </tr>
            <tr>
              <td><strong>Cyclone Amphan</strong></td>
              <td>2020 (May)</td>
              <td>260 &ndash; 270 km/h</td>
              <td>West Bengal (Sundarbans, Kolkata) &amp; Coastal Odisha</td>
              <td>Super cyclonic storm with peak wind speeds of 270 km/h cited in NCERT Class 8; massive flooding and storm surges across mangrove estuaries.</td>
            </tr>
            <tr>
              <td><strong>Cyclone Yaas</strong></td>
              <td>2021 (May)</td>
              <td>140 &ndash; 155 km/h</td>
              <td>Balasore, Bhadrak (Odisha) &amp; West Bengal</td>
              <td>Coincided with full-moon astronomical high tide, driving extensive saline seawater inundation into agricultural paddy lands.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- SVG DIAGRAM 5: CLOUD CHARGE SEPARATION & LIGHTNING DISCHARGE -->
      <div class="svg-container">
        <h4 class="subheading" style="justify-content: center; margin-top: 0;">
          <i class="fa-solid fa-cloud-bolt"></i>
          Electrostatic Charge Separation in Cumulonimbus Clouds &amp; Lightning Conductor Grounding
        </h4>
        <svg viewBox="0 0 1000 540" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
          <rect width="1000" height="540" fill="#f8fafc" rx="16" />
          <defs>
            <linearGradient id="gradCloud" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#94a3b8" />
              <stop offset="50%" stop-color="#475569" />
              <stop offset="100%" stop-color="#1e293b" />
            </linearGradient>
            <filter id="lightningGlow" x="-20%" y="-20%" width="140%" height="140%">
              <feGaussianBlur stdDeviation="3" result="blur" />
              <feMerge>
                <feMergeNode in="blur" />
                <feMergeNode in="SourceGraphic" />
              </feMerge>
            </filter>
          </defs>

          <!-- Cumulonimbus Thundercloud Body -->
          <path d="M 120 180 C 120 120 180 80 250 80 C 290 50 380 40 450 60 C 520 30 620 40 680 70 C 760 60 840 100 860 150 C 900 180 900 240 850 270 C 800 300 700 290 600 290 C 500 300 350 290 250 290 C 160 290 120 250 120 180 Z" fill="url(#gradCloud)" stroke="#334155" stroke-width="2" />

          <!-- Upper Cloud Positive Charges (Ice Crystals) -->
          <g fill="#ef4444" font-family="'Space Grotesk', sans-serif" font-weight="800" font-size="20">
            <text x="260" y="100">+</text>
            <text x="320" y="85">+</text>
            <text x="380" y="80">+</text>
            <text x="440" y="75">+</text>
            <text x="500" y="75">+</text>
            <text x="560" y="80">+</text>
            <text x="620" y="90">+</text>
            <text x="680" y="105">+</text>
            <text x="740" y="120">+</text>
          </g>
          <rect x="360" y="105" width="280" height="26" rx="6" fill="rgba(255,255,255,0.9)" />
          <text x="500" y="122" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="11" fill="#b91c1c" text-anchor="middle">UPPER LAYER: Lighter Positively Charged Ice Crystals (+)</text>

          <!-- Mid-Cloud Updraft / Downdraft Collision Zone -->
          <path d="M 300 220 L 300 150" stroke="#f59e0b" stroke-width="3" />
          <polygon points="300,140 294,155 306,155" fill="#f59e0b" />
          <path d="M 650 150 L 650 220" stroke="#38bdf8" stroke-width="3" />
          <polygon points="650,230 644,215 656,215" fill="#38bdf8" />
          <text x="480" y="190" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="700" fill="#f8fafc" text-anchor="middle">&uarr; Updrafts (Ice) rub against Downdrafts (Water) &darr;</text>

          <!-- Lower Cloud Negative Charges (Heavier Water Droplets) -->
          <g fill="#38bdf8" font-family="'Space Grotesk', sans-serif" font-weight="800" font-size="28">
            <text x="220" y="270">&minus;</text>
            <text x="280" y="270">&minus;</text>
            <text x="340" y="270">&minus;</text>
            <text x="400" y="270">&minus;</text>
            <text x="460" y="270">&minus;</text>
            <text x="520" y="270">&minus;</text>
            <text x="580" y="270">&minus;</text>
            <text x="640" y="270">&minus;</text>
            <text x="700" y="270">&minus;</text>
            <text x="760" y="270">&minus;</text>
          </g>
          <rect x="340" y="235" width="310" height="24" rx="6" fill="rgba(15,23,42,0.85)" />
          <text x="495" y="251" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="11" fill="#38bdf8" text-anchor="middle">BASE LAYER: Massive Pool of Negative Charges (&minus;)</text>

          <!-- Ground Level Baseline -->
          <rect x="50" y="470" width="900" height="40" fill="#334155" rx="4" />
          <line x1="50" y1="470" x2="950" y2="470" stroke="#64748b" stroke-width="3" />
          <text x="130" y="495" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="13" fill="#ffffff">EARTH GROUND</text>

          <!-- Induced Positive Charges on Ground Objects -->
          <g fill="#ef4444" font-family="'Space Grotesk', sans-serif" font-weight="800" font-size="18">
            <text x="220" y="460">+</text>
            <text x="260" y="460">+</text>
            <text x="300" y="460">+</text>
            <text x="340" y="460">+</text>
            <text x="480" y="460">+</text>
            <text x="520" y="460">+</text>
          </g>

          <!-- TALL BUILDING WITH LIGHTNING CONDUCTOR -->
          <g transform="translate(680, 310)">
            <!-- Building Masonry -->
            <rect x="0" y="60" width="160" height="100" fill="#cbd5e1" stroke="#475569" stroke-width="2" />
            <!-- Windows -->
            <rect x="20" y="80" width="25" height="30" fill="#0284c7" />
            <rect x="65" y="80" width="25" height="30" fill="#0284c7" />
            <rect x="110" y="80" width="25" height="30" fill="#0284c7" />
            <rect x="20" y="120" width="25" height="30" fill="#0284c7" />
            <rect x="65" y="120" width="25" height="30" fill="#0284c7" />
            <rect x="110" y="120" width="25" height="30" fill="#0284c7" />

            <!-- Lightning Conductor (Pointed Copper Rod) -->
            <line x1="80" y1="10" x2="80" y2="160" stroke="#d97706" stroke-width="4" />
            <!-- Sharp Pointed Tip at Top -->
            <polygon points="80,0 75,15 85,15" fill="#d97706" />
            <line x1="70" y1="12" x2="80" y2="0" stroke="#d97706" stroke-width="2.5" />
            <line x1="90" y1="12" x2="80" y2="0" stroke="#d97706" stroke-width="2.5" />

            <!-- Grounding Wire running down into earth -->
            <line x1="80" y1="160" x2="80" y2="200" stroke="#d97706" stroke-width="4" />
            <line x1="60" y1="200" x2="100" y2="200" stroke="#d97706" stroke-width="5" />
            <line x1="68" y1="206" x2="92" y2="206" stroke="#d97706" stroke-width="3" />
            <line x1="74" y1="212" x2="86" y2="212" stroke="#d97706" stroke-width="2" />

            <!-- Labels -->
            <text x="95" y="15" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="700" fill="#b45309">Pointed Rod</text>
            <text x="80" y="180" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="700" fill="#b45309" text-anchor="middle">Ground Plate</text>
          </g>

          <!-- LIGHTNING BOLT DIRECTED INTO LIGHTNING CONDUCTOR -->
          <polyline points="720,280 735,305 725,320 755,340 760,320" fill="none" stroke="#facc15" stroke-width="4.5" filter="url(#lightningGlow)" />
          <line x1="720" y1="280" x2="760" y2="320" stroke="#ffffff" stroke-width="2" />
          <rect x="790" y="270" width="160" height="34" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5" />
          <text x="870" y="286" font-family="'Space Grotesk', sans-serif" font-weight="800" font-size="11" fill="#b45309" text-anchor="middle">SAFE GROUNDING</text>
          <text x="870" y="299" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" fill="#78350f" text-anchor="middle">Zero Structural Damage</text>

          <!-- CLOUD-TO-GROUND DIRECT STRIKE (UNPROTECTED OPEN FIELD) -->
          <polyline points="380,280 400,320 385,350 420,380 405,410 440,470" fill="none" stroke="#facc15" stroke-width="4" filter="url(#lightningGlow)" />
          <polyline points="380,280 400,320 385,350 420,380 405,410 440,470" fill="none" stroke="#ffffff" stroke-width="1.5" />
          <circle cx="440" cy="470" r="14" fill="#ef4444" opacity="0.3" />
          <text x="440" y="445" font-family="'Space Grotesk', sans-serif" font-weight="800" font-size="11" fill="#b91c1c" text-anchor="middle">Direct Ground Strike</text>
        </svg>
        <div class="svg-caption">
          <i class="fa-solid fa-circle-info"></i>
          Figure 3.1: Physics of Atmospheric Electrification: Updraft friction causes positive charge accumulation at the cloud summit and negative charge accumulation at the cloud base, driving dielectric air breakdown and safe routing via a Benjamin Franklin lightning conductor.
        </div>
      </div>
    </section>
'''
