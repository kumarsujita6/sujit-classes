# -*- coding: utf-8 -*-
"""
Section 5: Complete Exam Question Bank (27 Exhaustive Exam Questions)
for Class 8 Science Chapter 6: Pressure, Winds, Storms, and Cyclones
"""

def get_section5():
    return '''
    <!-- SECTION 5: COMPLETE EXAM QUESTION BANK -->
    <section class="study-section" id="sec5">
      <div id="section-5"></div>
      <div class="section-header">
        <span class="section-tag">Assessment Vault &bull; CBSE / NEP Exam Preparation</span>
        <h2 class="section-title">
          <i class="fa-solid fa-trophy"></i>
          Section 5: Complete Exam Question Bank (27 Questions)
        </h2>
        <p class="section-desc">
          Rigorous assessment suite containing interactive MCQs, Assertion-Reasoning tests, 2M/3M Short Answers, 5M Long Answers with marking schemes, Competency Case Studies, and Previous Years Questions (PYQs).
        </p>
      </div>

      <!-- PART A: CONCEPTUAL MCQS WITH INTERACTIVE QUIZ ENGINE -->
      <h3 class="subheading"><i class="fa-solid fa-circle-question"></i> Part A: Conceptual MCQs (Interactive Quiz Engine)</h3>
      <p>Test your conceptual mastery by clicking your choice. Instant feedback highlights correct answers in green, flags traps in red, and updates your live score counter.</p>

      <div class="quiz-scoreboard">
        <div class="score-title"><i class="fa-solid fa-chart-line"></i> Interactive Quiz Scoreboard</div>
        <div class="score-badge"><span id="quizScoreCount">0</span> / 5 Score</div>
      </div>
      <p id="quizTeacherMsg" style="font-weight: 700; color: var(--primary-dark); margin-bottom: 1.5rem;"></p>

      <!-- MCQ 1 -->
      <div class="quiz-card" id="qcard1">
        <div class="quiz-q">1. A solid rectangular wooden brick of dimensions 20 cm &times; 10 cm &times; 5 cm has a mass of 4 kg. On which face will it exert the MAXIMUM pressure on a tabletop?</div>
        <div class="quiz-options">
          <button class="quiz-opt" onclick="checkQuizAnswer(1, 0, false, 'Trap Alert: The 20 cm &times; 10 cm face has the LARGEST area (200 cm&sup2;), which produces the MINIMUM pressure, not maximum!')">(A) Resting on the face measuring 20 cm &times; 10 cm</button>
          <button class="quiz-opt" onclick="checkQuizAnswer(1, 1, false, 'Incorrect: The 20 cm &times; 5 cm face gives an intermediate area of 100 cm&sup2;.')">(B) Resting on the face measuring 20 cm &times; 5 cm</button>
          <button class="quiz-opt" onclick="checkQuizAnswer(1, 2, true, 'CORRECT! Because P = F / A, the maximum pressure occurs when the contact area is the absolute SMALLEST. Area = 10 cm &times; 5 cm = 50 cm&sup2; (0.005 m&sup2;), generating P = 40 N / 0.005 m&sup2; = 8,000 Pa!')">(C) Resting on the face measuring 10 cm &times; 5 cm</button>
          <button class="quiz-opt" onclick="checkQuizAnswer(1, 3, false, 'Trap Alert: While total gravitational force (weight) is equal on all faces, pressure depends on contact area!')">(D) The pressure is identical on all three faces</button>
        </div>
        <div class="quiz-feedback" id="qfb1"></div>
      </div>

      <!-- MCQ 2 -->
      <div class="quiz-card" id="qcard2">
        <div class="quiz-q">2. Which of the following statements correctly explains why a person standing in a fast-moving river feels a stronger pushing force at their ankles than at their knees?</div>
        <div class="quiz-options">
          <button class="quiz-opt" onclick="checkQuizAnswer(2, 0, true, 'CORRECT! Hydrostatic pressure in liquids increases directly with depth (P = h &times; &rho; &times; g). The ankles are deeper below the water surface than the knees, experiencing higher static fluid pressure.')">(A) Hydrostatic liquid pressure increases directly with depth below the surface</button>
          <button class="quiz-opt" onclick="checkQuizAnswer(2, 1, false, 'Incorrect: Water density is virtually uniform and incompressible throughout shallow river depths.')">(B) Water density is much higher at the bottom of the river</button>
          <button class="quiz-opt" onclick="checkQuizAnswer(2, 2, false, 'Incorrect: Gravitational acceleration (g) is identical at both knee and ankle levels.')">(C) Gravitational pull is significantly stronger on the ankles</button>
          <button class="quiz-opt" onclick="checkQuizAnswer(2, 3, false, 'Incorrect: River surface friction slows surface water; water pressure itself depends strictly on depth.')">(D) River water is stationary at the surface but turbulent at the bottom</button>
        </div>
        <div class="quiz-feedback" id="qfb2"></div>
      </div>

      <!-- MCQ 3 -->
      <div class="quiz-card" id="qcard3">
        <div class="quiz-q">3. During a summer afternoon along the coast of Puri (Odisha), a child notices that kites consistently drift toward the inland city. What causes this atmospheric motion?</div>
        <div class="quiz-options">
          <button class="quiz-opt" onclick="checkQuizAnswer(3, 0, false, 'Trap Alert: Land Breeze occurs at NIGHT, not during summer afternoons!')">(A) Land Breeze blowing from the cooler land toward the warmer sea</button>
          <button class="quiz-opt" onclick="checkQuizAnswer(3, 1, true, 'CORRECT! Intense daytime solar heating causes land to heat up faster than sea water. Warm air rises over land, creating low pressure. Denser, cooler air from the sea blows inland as the Sea Breeze, carrying kites inland!')">(B) Sea Breeze driven by warm buoyant air rising over the sunlit land</button>
          <button class="quiz-opt" onclick="checkQuizAnswer(3, 2, false, 'Incorrect: High pressure forms over the COOL sea, not over the hot land.')">(C) High pressure developing over the hot sandy beaches</button>
          <button class="quiz-opt" onclick="checkQuizAnswer(3, 3, false, 'Incorrect: Evaporation alone does not determine horizontal wind direction.')">(D) Gravitational attraction of moisture evaporating from ocean waves</button>
        </div>
        <div class="quiz-feedback" id="qfb3"></div>
      </div>

      <!-- MCQ 4 -->
      <div class="quiz-card" id="qcard4">
        <div class="quiz-q">4. When a Category 4 tropical cyclone makes landfall, meteorological radar detects a 20 km central core where winds are gentle and skies are clear. What is this meteorological zone called?</div>
        <div class="quiz-options">
          <button class="quiz-opt" onclick="checkQuizAnswer(4, 0, false, 'Trap Alert: The Eye Wall is the MOST violent sector with peak winds and torrential rainfall!')">(A) The Eye Wall of the cyclone</button>
          <button class="quiz-opt" onclick="checkQuizAnswer(4, 1, true, 'CORRECT! The Eye is the calm, cloudless, low-pressure circular hub at the center of a tropical cyclone where air gently subsides.')">(B) The Eye of the cyclone</button>
          <button class="quiz-opt" onclick="checkQuizAnswer(4, 2, false, 'Incorrect: Spiral rainbands bring heavy rain squalls and strong winds.')">(C) Outer Spiral Rainbands</button>
          <button class="quiz-opt" onclick="checkQuizAnswer(4, 3, false, 'Incorrect: The storm surge is an ocean water swell, not a calm atmospheric zone.')">(D) The Coastal Storm Surge Front</button>
        </div>
        <div class="quiz-feedback" id="qfb4"></div>
      </div>

      <!-- MCQ 5 -->
      <div class="quiz-card" id="qcard5">
        <div class="quiz-q">5. If you are caught in an open field during a severe thunderstorm with lightning flashing nearby, which posture provides the SAFEST protection?</div>
        <div class="quiz-options">
          <button class="quiz-opt" onclick="checkQuizAnswer(5, 0, false, 'FATAL TRAP: Lying flat exposes your entire body to lethal radial ground surface currents!')">(A) Lying completely flat on the wet soil with arms and legs outstretched</button>
          <button class="quiz-opt" onclick="checkQuizAnswer(5, 1, false, 'FATAL TRAP: Tall trees act as natural lightning arresters and explode or side-flash!')">(B) Standing under the tallest solitary banyan tree in the field</button>
          <button class="quiz-opt" onclick="checkQuizAnswer(5, 2, true, 'CORRECT! The Lightning Crouch minimizes your height above ground while keeping foot contact area to a tiny footprint, reducing both direct strike risk and ground voltage exposure.')">(C) Crouching low on the balls of your feet with heels touching, head tucked down, and hands over ears</button>
          <button class="quiz-opt" onclick="checkQuizAnswer(5, 3, false, 'FATAL TRAP: An open metal-tipped umbrella acts like an elevated lightning rod above your head!')">(D) Holding an open umbrella with a pointed metal ferrule pointed at the sky</button>
        </div>
        <div class="quiz-feedback" id="qfb5"></div>
      </div>

      <!-- SVG DIAGRAM 6: BERNOULLI ROOF LIFT & AERODYNAMIC FLOW -->
      <div class="svg-container">
        <h4 class="subheading" style="justify-content: center; margin-top: 0;">
          <i class="fa-solid fa-wind"></i>
          Aerodynamic Lift on House Roofs During Severe Cyclones (Bernoulli Effect)
        </h4>
        <svg viewBox="0 0 950 480" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
          <rect width="950" height="480" fill="#f8fafc" rx="16" />
          <defs>
            <linearGradient id="gradHouse" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#cbd5e1" />
              <stop offset="100%" stop-color="#94a3b8" />
            </linearGradient>
            <linearGradient id="gradRoof" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#ea580c" />
              <stop offset="100%" stop-color="#c2410c" />
            </linearGradient>
            <filter id="shadowRoof" x="-10%" y="-10%" width="120%" height="120%">
              <feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#000000" flood-opacity="0.15" />
            </filter>
          </defs>

          <!-- Ground Baseline -->
          <line x1="50" y1="400" x2="900" y2="400" stroke="#475569" stroke-width="4" />

          <!-- House Masonry Body -->
          <g transform="translate(300, 200)">
            <rect x="0" y="50" width="350" height="150" fill="url(#gradHouse)" stroke="#334155" stroke-width="3" />
            <!-- Door -->
            <rect x="140" y="100" width="70" height="100" fill="#475569" stroke="#1e293b" stroke-width="2" />
            <!-- Windows (Closed) -->
            <rect x="40" y="90" width="55" height="55" fill="#e0f2fe" stroke="#334155" stroke-width="2" />
            <line x1="67" y1="90" x2="67" y2="145" stroke="#334155" stroke-width="1.5" />
            <rect x="255" y="90" width="55" height="55" fill="#e0f2fe" stroke="#334155" stroke-width="2" />
            <line x1="282" y1="90" x2="282" y2="145" stroke="#334155" stroke-width="1.5" />

            <!-- Indoor Stagnant Air (High Pressure) -->
            <rect x="20" y="65" width="310" height="25" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5" />
            <text x="175" y="82" font-family="'Space Grotesk', sans-serif" font-weight="800" font-size="12" fill="#b45309" text-anchor="middle">INDOOR STILL AIR: HIGH PRESSURE (101.3 kPa)</text>

            <!-- Massive Upward Force Arrows from Indoors -->
            <line x1="70" y1="45" x2="70" y2="-10" stroke="#ef4444" stroke-width="4" />
            <polygon points="70,-20 62,-5 78,-5" fill="#ef4444" />

            <line x1="175" y1="45" x2="175" y2="-25" stroke="#ef4444" stroke-width="5" />
            <polygon points="175,-35 167,-20 183,-20" fill="#ef4444" />

            <line x1="280" y1="45" x2="280" y2="-10" stroke="#ef4444" stroke-width="4" />
            <polygon points="280,-20 272,-5 288,-5" fill="#ef4444" />

            <text x="175" y="-45" font-family="'Space Grotesk', sans-serif" font-weight="800" font-size="13" fill="#dc2626" text-anchor="middle">UPWARD LIFTING THRUST</text>
          </g>

          <!-- Pitched Tin Roof (Detaching / Flying Off) -->
          <g transform="translate(285, 175)" filter="url(#shadowRoof)">
            <polygon points="0,70 190,0 380,70" fill="url(#gradRoof)" stroke="#7c2d12" stroke-width="3" />
            <text x="190" y="45" font-family="'Space Grotesk', sans-serif" font-weight="800" font-size="13" fill="#ffffff" text-anchor="middle">WEAK TIN / THATCHED ROOF</text>
          </g>

          <!-- High-Speed Streamlines Over Roof (Bernoulli Low Pressure) -->
          <g stroke="#0284c7" stroke-width="3" fill="none">
            <!-- Streamline 1 -->
            <path d="M 80 150 Q 280 130 475 110 Q 670 130 870 150" />
            <polygon points="875,150 860,144 860,156" fill="#0284c7" />

            <!-- Streamline 2 (Constricted over apex -> High Velocity) -->
            <path d="M 80 115 Q 280 90 475 70 Q 670 90 870 115" stroke-width="4" />
            <polygon points="875,115 860,109 860,121" fill="#0284c7" />

            <!-- Streamline 3 -->
            <path d="M 80 80 Q 280 60 475 40 Q 670 60 870 80" />
            <polygon points="875,80 860,74 860,86" fill="#0284c7" />
          </g>

          <!-- Low Pressure Zone Callout Box -->
          <rect x="360" y="20" width="230" height="32" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5" />
          <text x="475" y="41" font-family="'Space Grotesk', sans-serif" font-weight="800" font-size="12" fill="#b91c1c" text-anchor="middle">SEVERE LOW PRESSURE ZONE</text>
          <text x="475" y="140" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="11" fill="#0284c7" text-anchor="middle">High Wind Speed: 150 - 200 km/h &rarr;</text>
        </svg>
        <div class="svg-caption">
          <i class="fa-solid fa-circle-info"></i>
          Figure 5.1: Aerodynamic Bernoulli Mechanism of Storm Damage: High-speed horizontal winds sweeping over roofs cause external pressure to drop; higher indoor atmospheric pressure produces massive upward lift that blows roofs away.
        </div>
      </div>

      <!-- PART B: ASSERTION & REASONING QUESTIONS -->
      <h3 class="subheading"><i class="fa-solid fa-arrows-split-up-and-left"></i> Part B: Assertion &amp; Reasoning Questions</h3>
      <p><em>Directions: Choose (A) if both Assertion and Reason are true and Reason is the correct explanation; (B) if both are true but Reason is NOT the correct explanation; (C) if Assertion is true but Reason is false; (D) if Assertion is false but Reason is true.</em></p>

      <details class="ans-box">
        <summary>Q6: Assertion &amp; Reason &mdash; Sharp Knives vs Blunt Knives for Cutting</summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> It is much easier to cut an apple with the sharp edge of a knife than with its blunt edge.</p>
          <p><strong>Reason (R):</strong> The sharp edge has a smaller surface area, producing higher pressure for the same applied muscular force.</p>
          <div class="step-box core">
            <div class="step-title"><i class="fa-solid fa-check"></i> Correct Answer &amp; Explanation</div>
            <p><strong>(A) Both Assertion and Reason are true, and Reason is the correct explanation of Assertion.</strong></p>
            <p>Pressure is defined as <span class="math-entity">P = F / A</span>. For a fixed muscular force <span class="math-entity">F</span>, reducing contact area <span class="math-entity">A</span> to a microscopic edge concentrates the force, generating high cutting pressure that cleanly slices plant tissues.</p>
          </div>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q7: Assertion &amp; Reason &mdash; Dam Base Width Engineering</summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> The concrete base of a hydroelectric dam is constructed significantly broader than its top crest.</p>
          <p><strong>Reason (R):</strong> The density of reservoir water increases rapidly with depth, becoming extremely dense at the bottom.</p>
          <div class="step-box core">
            <div class="step-title"><i class="fa-solid fa-check"></i> Correct Answer &amp; Explanation</div>
            <p><strong>(C) Assertion (A) is true, but Reason (R) is false.</strong></p>
            <p>Water is an almost incompressible liquid; its density is virtually constant (~1000 kg/m&sup3;) throughout the reservoir. The dam base is broad because <em>hydrostatic lateral pressure</em> increases directly with vertical depth (<span class="math-entity">P = h &times; &rho; &times; g</span>), not because water becomes denser!</p>
          </div>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q8: Assertion &amp; Reason &mdash; Daytime Coastal Sea Breeze</summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> Along coastal regions, the wind blows from the sea towards the land during the daytime.</p>
          <p><strong>Reason (R):</strong> During daytime, land warms up faster than the ocean, causing warm air over land to rise and create a local low-pressure zone.</p>
          <div class="step-box core">
            <div class="step-title"><i class="fa-solid fa-check"></i> Correct Answer &amp; Explanation</div>
            <p><strong>(A) Both Assertion and Reason are true, and Reason is the correct explanation of Assertion.</strong></p>
            <p>Water has a higher specific heat capacity than soil and rock, warming slowly. The rapidly heated land creates buoyant updrafts and low pressure. Dense cool air from over the sea moves inland toward this low pressure as the Sea Breeze.</p>
          </div>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q9: Assertion &amp; Reason &mdash; Rubber Sucker on Rough Wood</summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> A rubber suction cup fails to stick firmly when pressed against an unpolished, rough wooden door.</p>
          <p><strong>Reason (R):</strong> Rough wooden surfaces do not allow an airtight seal, allowing ambient atmospheric air to leak beneath the cup rim.</p>
          <div class="step-box core">
            <div class="step-title"><i class="fa-solid fa-check"></i> Correct Answer &amp; Explanation</div>
            <p><strong>(A) Both Assertion and Reason are true, and Reason is the correct explanation of Assertion.</strong></p>
            <p>Suction depends on creating a pressure deficit beneath the cup. When air leaks past microscopic surface irregularities on rough wood, internal pressure matches external atmospheric pressure (<span class="math-entity">&Delta;P = 0</span>), leaving zero net holding force.</p>
          </div>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q10: Assertion &amp; Reason &mdash; Lightning Strike Safety Inside a Car</summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> If a car is struck by lightning during a thunderstorm, the passengers seated inside remain unharmed.</p>
          <p><strong>Reason (R):</strong> Thick rubber tyres act as perfect electrical insulators, preventing lightning from completing a path into the ground.</p>
          <div class="step-box core">
            <div class="step-title"><i class="fa-solid fa-check"></i> Correct Answer &amp; Explanation</div>
            <p><strong>(C) Assertion (A) is true, but Reason (R) is false.</strong></p>
            <p>Rubber tyres do not insulate a car against millions of volts of lightning (which easily arcs across the wet rubber rim to the ground). Passengers are protected because the closed metallic body acts as a <strong>Faraday cage</strong>, routing current around the outer metal shell.</p>
          </div>
        </div>
      </details>

      <!-- PART C: SHORT ANSWER QUESTIONS (2M / 3M) -->
      <h3 class="subheading"><i class="fa-solid fa-file-pen"></i> Part C: Short Answer Questions (2-Mark &amp; 3-Mark Formats)</h3>

      <details class="ans-box">
        <summary>Q11 (2 Marks): Explain why railway porters (coolies) place a round cloth ring (goundi) on their heads before lifting heavy luggage.</summary>
        <div class="ans-content">
          <div class="step-box core">
            <div class="step-title"><i class="fa-solid fa-atom"></i> 1. Core Physics Principle</div>
            <p>Pressure is inversely proportional to contact surface area (<span class="math-entity">P = F / A</span>). Increasing the contact area dilutes the downward pressure exerted by a fixed load.</p>
          </div>
          <div class="step-box step">
            <div class="step-title"><i class="fa-solid fa-list-ol"></i> 2. Crisp 2-Mark Scoring Points</div>
            <ul>
              <li><strong>Point 1 (1 Mark):</strong> A round roll of cloth (goundi) fills the natural contours of the skull and significantly <strong>increases the contact surface area</strong> between the porter's head and the flat base of the heavy trunk or basket.</li>
              <li><strong>Point 2 (1 Mark):</strong> By increasing contact area (<span class="math-entity">A</span>) for a constant luggage weight (<span class="math-entity">F</span>), the pressure (<span class="math-entity">P = F / A</span>) on the skull is reduced, preventing localized tissue pain and spinal strain.</li>
            </ul>
          </div>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q12 (2 Marks): Why do heavy army battle tanks move on wide continuous steel tracks (caterpillar tracks) instead of wheels?</summary>
        <div class="ans-content">
          <div class="step-box core">
            <div class="step-title"><i class="fa-solid fa-atom"></i> 1. Core Principle</div>
            <p>Minimizing ground contact pressure prevents multi-tonne vehicles from sinking into soft or yielding terrain.</p>
          </div>
          <div class="step-box step">
            <div class="step-title"><i class="fa-solid fa-list-ol"></i> 2. Scoring Points</div>
            <ul>
              <li><strong>Point 1:</strong> An army tank weighs 50 to 60 tonnes (500,000 to 600,000 N). If supported on normal wheels, the small contact area would exert enormous pressure, sinking the tank into mud or sand.</li>
              <li><strong>Point 2:</strong> Continuous caterpillar tracks provide an expansive ground contact area of several square metres. This spreads the massive weight over a large area, lowering ground pressure so the tank can cross swamps and soft desert sands without bogging down.</li>
            </ul>
          </div>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q13 (3 Marks): Explain why high-altitude mountaineers frequently suffer from acute nosebleeds when climbing Mount Everest.</summary>
        <div class="ans-content">
          <div class="step-box core">
            <div class="step-title"><i class="fa-solid fa-atom"></i> 1. Core Principle</div>
            <p>Human circulatory health relies on hydrostatic equilibrium between internal blood pressure and ambient external atmospheric pressure.</p>
          </div>
          <div class="step-box step">
            <div class="step-title"><i class="fa-solid fa-list-ol"></i> 2. Scoring Points</div>
            <ul>
              <li><strong>Atmospheric Pressure Drop (1 Mark):</strong> As altitude increases, the overlying column of air shortens and thins. At high mountain peaks (above 5,000 to 8,000 m), atmospheric pressure drops to roughly one-third of sea-level pressure.</li>
              <li><strong>Internal Blood Pressure (1 Mark):</strong> The blood pressure inside human vascular capillaries remains regulated at near sea-level pressure (~100 to 120 kPa).</li>
              <li><strong>Capillary Rupture (1 Mark):</strong> The internal blood pressure significantly exceeds the reduced external air pressure. This outward pressure difference ruptures delicate, thin-walled capillaries inside nasal membranes, causing nosebleeds.</li>
            </ul>
          </div>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q14 (3 Marks): State three clear differences between a Sea Breeze and a Land Breeze.</summary>
        <div class="ans-content">
          <div class="step-box step">
            <div class="step-title"><i class="fa-solid fa-table"></i> 3-Mark Scoring Matrix</div>
            <div class="table-wrapper">
              <table class="data-table">
                <thead>
                  <tr>
                    <th>Diagnostic Feature</th>
                    <th>Sea Breeze (1.5 Marks)</th>
                    <th>Land Breeze (1.5 Marks)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>Time of Flow</strong></td>
                    <td>Occurs during the <strong>daytime</strong> (peaks late afternoon).</td>
                    <td>Occurs during the <strong>nighttime</strong> (continues till dawn).</td>
                  </tr>
                  <tr>
                    <td><strong>Direction of Wind</strong></td>
                    <td>Blows <strong>from Sea to Land</strong>.</td>
                    <td>Blows <strong>from Land to Sea</strong>.</td>
                  </tr>
                  <tr>
                    <td><strong>Location of Low Pressure</strong></td>
                    <td>Over the <strong>Land</strong> (rapidly heated by daytime sun).</td>
                    <td>Over the <strong>Sea</strong> (ocean retains absorbed heat at night).</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q15 (2 Marks): Why is an open umbrella with a metallic rod dangerous to carry outdoors during a thunderstorm?</summary>
        <div class="ans-content">
          <div class="step-box step">
            <div class="step-title"><i class="fa-solid fa-list-ol"></i> 2. Scoring Points</div>
            <ul>
              <li><strong>Point 1:</strong> Metallic materials (steel, aluminium) are excellent electrical conductors. Holding an umbrella overhead raises a pointed metal ferrule to the highest point in your immediate vicinity.</li>
              <li><strong>Point 2:</strong> Sharp elevated metal points concentrate induced positive charges, attracting stepped lightning leaders. A strike would channel hundreds of thousands of amperes directly through the metal shaft into the person's hand and heart.</li>
            </ul>
          </div>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q16 (3 Marks): Explain why overhead domestic water tanks are always installed on rooftops rather than in ground-floor gardens.</summary>
        <div class="ans-content">
          <div class="step-box step">
            <div class="step-title"><i class="fa-solid fa-list-ol"></i> 2. Scoring Points</div>
            <ul>
              <li><strong>Point 1 (Hydrostatic Formula):</strong> Hydrostatic liquid pressure at any tap is determined by <span class="math-entity">P = h &times; &rho; &times; g</span>, where <span class="math-entity">h</span> is the vertical height difference between the free water level in the tank and the tap.</li>
              <li><strong>Point 2 (Gravity Head):</strong> Installing the tank on the rooftop maximizes vertical height (<span class="math-entity">h</span>) above all household washbasins, showers, and kitchen taps.</li>
              <li><strong>Point 3 (Functional Advantage):</strong> This elevation provides steady water pressure throughout the plumbing system, eliminating the need for electric booster pumps every time a tap is opened.</li>
            </ul>
          </div>
        </div>
      </details>

      <!-- PART D: LONG ANSWER QUESTIONS (5M) WITH MARKING SCHEMES -->
      <h3 class="subheading"><i class="fa-solid fa-award"></i> Part D: Long Answer Questions (5-Mark Master Formats)</h3>

      <details class="ans-box">
        <summary>Q17 (5 Marks): Explain the complete physical mechanism of how a tropical cyclone forms, sustains itself, and eventually weakens. Describe the internal structure of its eye and eye wall.</summary>
        <div class="ans-content">
          <div class="step-box step">
            <div class="step-title"><i class="fa-solid fa-list-check"></i> Step-by-Step 5-Mark Marking Scheme</div>
            <ul>
              <li><strong>1. Genesis over Warm Ocean (1 Mark):</strong> Cyclones form over tropical seas where water surface temperature is at least 26.5 &deg;C to 27 &deg;C. Solar heating causes massive evaporation, creating warm, moist, buoyant air that expands and rises, leaving a deep low-pressure zone at the ocean surface.</li>
              <li><strong>2. Latent Heat Fuel Cycle (1 Mark):</strong> As moist air rises into cooler upper altitudes, water vapour condenses into raindrops. Condensation releases latent heat into the surrounding air. This heat warms the surrounding air, making it rise faster and lowering central pressure further, drawing in more warm, moist air in a self-sustaining cycle.</li>
              <li><strong>3. Coriolis Rotational Deflection (1 Mark):</strong> Cool air rushing inward from surrounding high-pressure regions is deflected by the Earth's rotation (Coriolis force). In the Northern Hemisphere, winds spiral counter-clockwise, organizing the storm into a spinning vortex.</li>
              <li><strong>4. Eye &amp; Eye Wall Structure (1 Mark):</strong>
                <ul>
                  <li><em>The Eye:</em> A calm, cloudless circular hub (10 to 30 km wide) at the centre, with light winds and the lowest barometric pressure on Earth. Air gently subsides here, warming and suppressing clouds.</li>
                  <li><em>The Eye Wall:</em> A ring of towering cumulonimbus clouds immediately encircling the eye, delivering peak sustained winds (150 to 250+ km/h), heavy lightning, and torrential rain.</li>
                </ul>
              </li>
              <li><strong>5. Dissipation over Land (1 Mark):</strong> When the cyclone crosses onto land (landfall), its primary energy source &mdash; warm, moist evaporating sea water &mdash; is cut off. Surface land friction also slows down the winds, causing the cyclone to gradually weaken and dissipate.</li>
            </ul>
          </div>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q18 (5 Marks): Describe with the aid of a labelled schematic the working principle, installation, and operation of a Lightning Conductor on tall structures.</summary>
        <div class="ans-content">
          <div class="step-box step">
            <div class="step-title"><i class="fa-solid fa-list-check"></i> 5-Mark Marking Scheme</div>
            <ul>
              <li><strong>1. Definition &amp; Purpose (1 Mark):</strong> A lightning conductor is a protective safety device installed on tall buildings to provide a low-resistance path that directs lightning current safely into the ground, preventing fires and structural damage.</li>
              <li><strong>2. Structural Components (1.5 Marks):</strong>
                <ul>
                  <li><em>Pointed Metallic Rod:</em> A heavy copper or brass rod with sharp prongs extending several metres above the building's highest rooftop.</li>
                  <li><em>Down Conductor:</em> A thick, heavy-gauge copper strip or cable running down the exterior building wall.</li>
                  <li><em>Grounding Plate:</em> A large copper electrode buried deep underground in moist soil surrounded by charcoal and salt to ensure low earth resistance.</li>
                </ul>
              </li>
              <li><strong>3. Operational Mechanism During a Storm (1.5 Marks):</strong>
                <ul>
                  <li>When a thundercloud approaches with a negatively charged base, it induces a strong positive charge on the pointed conductor rod.</li>
                  <li>The sharp points concentrate this electric field, causing a gentle ion discharge (point action / corona discharge) that helps neutralize part of the cloud's charge.</li>
                  <li>If a lightning strike occurs, the conductor provides a low-resistance pathway, guiding millions of amperes directly into the Earth rather than through the building's masonry or electrical wiring.</li>
                </ul>
              </li>
              <li><strong>4. Diagram Credit (1 Mark):</strong> Fully labelled schematic showing the pointed rod, down conductor, and buried earth plate.</li>
            </ul>
          </div>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q19 (5 Marks): Why do high-speed winds blow off roofs of houses? How can this hazard be minimized architecturally? Support your answer with Bernoulli's Principle.</summary>
        <div class="ans-content">
          <div class="step-box step">
            <div class="step-title"><i class="fa-solid fa-list-check"></i> 5-Mark Marking Scheme</div>
            <ul>
              <li><strong>1. Statement of Principle (1 Mark):</strong> Bernoulli's principle states that an increase in the speed of a fluid occurs simultaneously with a decrease in its static lateral pressure: high velocity corresponds to reduced pressure.</li>
              <li><strong>2. Pressure Differential Formation (1.5 Marks):</strong>
                <ul>
                  <li>When intense gale-force winds (150+ km/h) blow horizontally across the roof of a house, static air pressure above the roof drops sharply (<span class="math-entity">P<sub>top</sub> &darr;</span>).</li>
                  <li>Inside the house, where air is enclosed and stagnant, the pressure remains at standard atmospheric level (<span class="math-entity">P<sub>inside</sub> &asymp; 101.3 kPa</span>).</li>
                </ul>
              </li>
              <li><strong>3. Upward Lifting Force (1.5 Marks):</strong>
                <ul>
                  <li>This large pressure difference (<span class="math-entity">&Delta;P = P<sub>inside</sub> &minus; P<sub>top</sub></span>) acts upward over the entire roof area (<span class="math-entity">A</span>).</li>
                  <li>The net upward thrust (<span class="math-entity">F<sub>lift</sub> = &Delta;P &times; A</span>) easily reaches tens of thousands of Newtons, lifting the roof off its supports.</li>
                </ul>
              </li>
              <li><strong>4. Architectural Mitigation (1 Mark):</strong>
                <ul>
                  <li><em>Equalizing Pressure:</em> Keeping windows and doors slightly open on both sides allows air to circulate, balancing indoor and outdoor pressure (<span class="math-entity">&Delta;P &asymp; 0</span>).</li>
                  <li><em>Structural Anchorage:</em> Bolting roof trusses directly into reinforced concrete wall pillars rather than using simple nails.</li>
                </ul>
              </li>
            </ul>
          </div>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q20 (5 Marks): Derive the mathematical relation between pressure, force, and area. Explain with two practical examples how pressure can be minimized and with two examples how it can be maximized.</summary>
        <div class="ans-content">
          <div class="step-box step">
            <div class="step-title"><i class="fa-solid fa-list-check"></i> 5-Mark Marking Scheme</div>
            <ul>
              <li><strong>1. Definition &amp; Mathematical Formulation (1 Mark):</strong>
                <br>Pressure is defined as thrust applied perpendicularly per unit surface area:
                <br><span class="math-entity">Pressure (P) = Thrust (F) / Area (A)</span>
                <br>SI Unit: Force in Newtons (N), Area in square metres (m&sup2;); Unit = <span class="math-entity">N/m&sup2; = Pascal (Pa)</span>.
              </li>
              <li><strong>2. Two Examples of Minimizing Pressure by Increasing Area (2 Marks):</strong>
                <ul>
                  <li><em>Wide Backpack Straps:</em> Broad straps distribute the bag's weight over a larger shoulder area, lowering pressure and preventing painful shoulder gouging.</li>
                  <li><em>Wide Foundations for Buildings:</em> Skyscraper foundations are constructed with broad concrete footings, spreading the building's weight over a larger ground area to prevent settling or sinking into soil.</li>
                </ul>
              </li>
              <li><strong>3. Two Examples of Maximizing Pressure by Decreasing Area (2 Marks):</strong>
                <ul>
                  <li><em>Pointed Tip of Sewing Needle / Pin:</em> The tiny tip has a microscopic contact area, so light finger pressure generates thousands of Pascals, easily piercing woven fabric.</li>
                  <li><em>Sharp Edge of a Kitchen Axe:</em> Sharpening the axe blade reduces contact area, generating high chopping pressure that splits hardwood logs with ease.</li>
                </ul>
              </li>
            </ul>
          </div>
        </div>
      </details>

      <!-- PART E: COMPETENCY-BASED CASE STUDIES -->
      <h3 class="subheading"><i class="fa-solid fa-microscope"></i> Part E: Competency-Based Case Studies</h3>

      <!-- Case Study 1 -->
      <details class="ans-box">
        <summary>Case Study 1: The 1999 Odisha Super Cyclone and Modern Early Warning Meteorological Networks</summary>
        <div class="ans-content">
          <p><strong>Case Passage:</strong></p>
          <p>
            On 29 October 1999, an unprecedented Category 5 Super Cyclonic Storm struck the coastal district of Jagatsinghpur in Odisha. With sustained winds reaching 260 km/h and an astronomical storm surge exceeding 7 metres, seawater surged more than 20 kilometres inland, resulting in the tragic loss of approximately 10,000 lives. In response to this disaster, the Government of Odisha established the Odisha State Disaster Management Authority (OSDMA), pioneering an early warning network in partnership with the India Meteorological Department (IMD). Today, INSAT-3D satellites and coastal Doppler Weather Radars provide 48-hour Cyclone Watches and 24-hour Cyclone Warnings. In 2013, when Cyclone Phailin struck with winds of 220 km/h, over 1 million people were evacuated to multi-purpose cyclone shelters in 48 hours, earning praise from the United Nations for achieving near-zero casualties.
          </p>
          <div class="step-box step">
            <div class="step-title"><i class="fa-solid fa-clipboard-question"></i> Case Questions &amp; Model Answers</div>
            <ol>
              <li><strong>(a) What is a storm surge, and what causes it during a cyclone? (1 Mark)</strong>
                <br><em>Answer:</em> A storm surge is an abnormal coastal water rise (3 to 12 metres high) caused by strong cyclonic winds pushing ocean water toward the coast, combined with the suction effect of the storm's deep low-pressure central core.
              </li>
              <li><strong>(b) Why does a cyclone begin to dissipate rapidly after crossing the coastline (landfall)? (1 Mark)</strong>
                <br><em>Answer:</em> Moving over land cuts off the cyclone's moisture source &mdash; warm ocean water &mdash; which halts the latent heat of condensation that fuels the storm. In addition, surface friction over land slows down the winds.
              </li>
              <li><strong>(c) Distinguish between a 'Cyclone Watch' and a 'Cyclone Warning' issued by the IMD. (2 Marks)</strong>
                <br><em>Answer:</em>
                <ul>
                  <li><em>Cyclone Watch (or Alert):</em> Issued <strong>48 hours in advance</strong> of expected adverse weather, alerting coastal authorities to prepare contingency plans.</li>
                  <li><em>Cyclone Warning:</em> Issued <strong>24 hours in advance</strong> of anticipated landfall, specifying affected coastal districts and triggering mandatory evacuations.</li>
                </ul>
              </li>
            </ol>
          </div>
        </div>
      </details>

      <!-- Case Study 2 -->
      <details class="ans-box">
        <summary>Case Study 2: Deep-Sea Submersibles, Atmospheric Diving Suits, and Hydrostatic Loads</summary>
        <div class="ans-content">
          <p><strong>Case Passage:</strong></p>
          <p>
            Marine oceanographers exploring the Mariana Trench (depth ~11,000 metres) cannot use conventional scuba gear. Standard scuba diving is limited to roughly 40 metres because ambient hydrostatic pressure increases by approximately 100 kPa (1 atmosphere) for every 10 metres of descent. At ocean depths of 4,000 metres, where the wreck of the Titanic rests, hydrostatic pressure exceeds 40,000 kPa (400 times sea-level atmospheric pressure). To explore these environments, scientists must remain enclosed inside titanium-hulled submersibles or rigid Atmospheric Diving Suits (ADS) engineered to maintain an internal cabin pressure of exactly 1 atmosphere.
          </p>
          <div class="step-box step">
            <div class="step-title"><i class="fa-solid fa-clipboard-question"></i> Case Questions &amp; Model Answers</div>
            <ol>
              <li><strong>(a) State the physical law explaining why hydrostatic pressure increases with ocean depth. (1 Mark)</strong>
                <br><em>Answer:</em> The hydrostatic law: <span class="math-entity">P = h &times; &rho; &times; g</span>. Liquid pressure increases linearly with depth (<span class="math-entity">h</span>) due to the accumulated weight of the overlying water column.
              </li>
              <li><strong>(b) Why would an unprotected human body be crushed at extreme ocean depths? (1 Mark)</strong>
                <br><em>Answer:</em> Human internal blood and cellular fluid pressure is regulated at ~101.3 kPa. At extreme depths, the multi-megapascal external water pressure vastly exceeds internal pressure, causing body cavities and lungs to collapse.
              </li>
              <li><strong>(c) Why are deep-sea submersibles built with spherical or curved cylindrical hulls rather than flat rectangular boxes? (2 Marks)</strong>
                <br><em>Answer:</em> Curved and spherical geometries distribute external compressive hydrostatic forces evenly across their entire surface through uniform hoop stress, eliminating sharp corners and stress concentrations where structural failure could occur under high pressure.
              </li>
            </ol>
          </div>
        </div>
      </details>

      <!-- PART F: PREVIOUS YEARS QUESTIONS (PYQS) & PROBABLE EXAM QUESTIONS -->
      <h3 class="subheading"><i class="fa-solid fa-clock-rotate-left"></i> Part F: Previous Years Questions (PYQs) &amp; Most Probable Questions</h3>

      <details class="ans-box">
        <summary>Q21 [PYQ 2024]: Why does blowing air between two suspended ping-pong balls cause them to move toward each other?</summary>
        <div class="ans-content">
          <div class="step-box core">
            <div class="step-title"><i class="fa-solid fa-atom"></i> 1. Core Principle</div>
            <p>Bernoulli's principle: high-speed airflow produces a reduction in static lateral fluid pressure.</p>
          </div>
          <div class="step-box step">
            <div class="step-title"><i class="fa-solid fa-list-ol"></i> 2. Model Exam Answer</div>
            <ul>
              <li>When air is blown through the narrow gap between two suspended ping-pong balls, the air speed in that gap increases.</li>
              <li>This high air velocity produces a localized drop in static air pressure between the balls.</li>
              <li>The air on the outer sides remains at higher atmospheric pressure.</li>
              <li>This outer high pressure pushes both balls inward toward the central low-pressure zone, causing them to move together.</li>
            </ul>
          </div>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q22 [PYQ 2023]: A girl stands on loose sand with bare feet and then puts on flat snowshoes. Compare the depth of depression in both cases and explain why.</summary>
        <div class="ans-content">
          <div class="step-box step">
            <div class="step-title"><i class="fa-solid fa-list-ol"></i> 2. Model Exam Answer</div>
            <ul>
              <li><strong>Bare Feet:</strong> Contact area is small (only the soles of her feet, ~0.03 m&sup2;). For her constant weight <span class="math-entity">W</span>, the pressure <span class="math-entity">P = W / A</span> is high, causing her feet to sink deep into the sand.</li>
              <li><strong>Flat Snowshoes:</strong> Contact area is much larger (~0.3 m&sup2;). The pressure exerted on the sand is reduced to roughly one-tenth (<span class="math-entity">P &darr;&darr;</span>), so she experiences minimal depression and walks across the sand easily.</li>
            </ul>
          </div>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q23 [PYQ 2022]: Describe an experiment using a tin can with hot water and cold water to demonstrate atmospheric pressure.</summary>
        <div class="ans-content">
          <div class="step-box step">
            <div class="step-title"><i class="fa-solid fa-list-ol"></i> 2. Model Exam Answer (Can-Crushing Experiment)</div>
            <ol>
              <li>Take a clean metallic tin can with an airtight screw cap. Fill it with a small amount of water and heat it over a flame until steam vigorously expels all internal air.</li>
              <li>Tightly seal the screw cap and immediately remove the can from the flame.</li>
              <li>Pour cold tap water over the sealed can.</li>
              <li><strong>Observation:</strong> The tin can instantly collapses inward with a loud crunch, as if crushed by a giant fist.</li>
              <li><strong>Scientific Explanation:</strong> Cold water rapidly condenses the hot steam inside into a few drops of liquid water, creating a near-vacuum (<span class="math-entity">P<sub>inside</sub> &asymp; 0</span>). The surrounding atmospheric pressure (~101.3 kPa) crushes the thin metal walls inward.</li>
            </ol>
          </div>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q24 [Most Probable Exam Question]: Why is lightning rarely observed during light winter rains in Northern India, but frequent during pre-monsoon summer showers?</summary>
        <div class="ans-content">
          <div class="step-box step">
            <div class="step-title"><i class="fa-solid fa-list-ol"></i> 2. Model Exam Answer</div>
            <ul>
              <li>Light winter rains (such as Western Disturbances) feature gentle stratiform cloud layers with mild, stable vertical air movement and minimal ground heating.</li>
              <li>Pre-monsoon summer showers feature intense solar ground heating, producing violent, turbulent convective updrafts exceeding 100 km/h.</li>
              <li>These vigorous updrafts and downdrafts drive frequent collisions between ice crystals and supercooled water droplets, building up the massive static charges required for lightning discharges.</li>
            </ul>
          </div>
        </div>
      </details>

      <details class="ans-box">
        <summary>Q25 [Most Probable Exam Question]: A block weighing 240 N has dimensions 0.4 m &times; 0.3 m &times; 0.2 m. Calculate the minimum and maximum pressure it can exert on a table.</summary>
        <div class="ans-content">
          <div class="step-box step">
            <div class="step-title"><i class="fa-solid fa-list-ol"></i> 2. Numerical Solution</div>
            <ol>
              <li><strong>Given:</strong> Force <span class="math-entity">F = 240 N</span>.
                <ul>
                  <li>Face 1 Area: <span class="math-entity">A<sub>1</sub> = 0.4 m &times; 0.3 m = 0.12 m&sup2;</span> (Largest Area)</li>
                  <li>Face 2 Area: <span class="math-entity">A<sub>2</sub> = 0.4 m &times; 0.2 m = 0.08 m&sup2;</span></li>
                  <li>Face 3 Area: <span class="math-entity">A<sub>3</sub> = 0.3 m &times; 0.2 m = 0.06 m&sup2;</span> (Smallest Area)</li>
                </ul>
              </li>
              <li><strong>Minimum Pressure (<span class="math-entity">P<sub>min</sub></span>):</strong> Occurs on the largest area (<span class="math-entity">A<sub>1</sub></span>):
                <br><span class="math-entity">P<sub>min</sub> = F / A<sub>1</sub> = 240 N / 0.12 m&sup2; = 2,000 N/m&sup2; = 2,000 Pa (2 kPa)</span>.
              </li>
              <li><strong>Maximum Pressure (<span class="math-entity">P<sub>max</sub></span>):</strong> Occurs on the smallest area (<span class="math-entity">A<sub>3</sub></span>):
                <br><span class="math-entity">P<sub>max</sub> = F / A<sub>3</sub> = 240 N / 0.06 m&sup2; = 4,000 N/m&sup2; = 4,000 Pa (4 kPa)</span>.
              </li>
              <li><strong>Final Answer:</strong> Minimum pressure = <strong>2,000 Pa</strong>; Maximum pressure = <strong>4,000 Pa</strong>.</li>
            </ol>
          </div>
        </div>
      </details>
    </section>
'''
