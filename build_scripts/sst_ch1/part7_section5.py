# -*- coding: utf-8 -*-
"""Part 7: Section 5 - Complete Examination Question Bank (27 Questions)."""

PART7_CONTENT = """
    <!-- ======================================================== -->
    <!-- SECTION 5: COMPLETE EXAMINATION QUESTION BANK (27 Qs)   -->
    <!-- ======================================================== -->
    <section id="sec5" class="section-card">
      <div class="section-header">
        <span class="section-num"><i class="fa-solid fa-clipboard-question"></i> Section 5</span>
        <h2>Complete High-Yield Examination Question Bank</h2>
        <p class="section-sub">
          A 27-question master question bank featuring an interactive quiz engine with trap analysis, assertion-reasoning logic, short and long answers with CBSE marking schemes, real-world case studies, and probable exam questions.
        </p>
      </div>

      <!-- ========================================== -->
      <!-- SUBSECTION 5.1: CONCEPTUAL MCQS (QUIZ)    -->
      <!-- ========================================== -->
      <h3 class="topic-title"><i class="fa-solid fa-circle-check"></i> 5.1: Five Conceptual MCQs with Interactive Quiz Engine &amp; Trap Analysis</h3>
      <p>
        Click your chosen option to test your mastery. The quiz engine instantly evaluates your response, updates your score, and reveals the teacher's trap explanation!
      </p>

      <!-- Quiz Scoreboard Banner -->
      <div class="quiz-score-banner">
        <div class="quiz-score-badge">
          <i class="fa-solid fa-trophy"></i>
          <span>Your Score: <span id="quizScoreCount">0</span> / 5</span>
        </div>
        <div id="quizTeacherMsg" class="quiz-teacher-msg">
          Click an option below to test your understanding!
        </div>
      </div>

      <!-- MCQ 1 -->
      <div id="qcard1" class="quiz-card">
        <div class="quiz-question-text">
          <strong>Question 1:</strong> An immense reserve of crude petroleum is discovered 7,000 metres beneath a polar ice shelf. However, the current drilling costs exceed the international market price of oil, and environmental treaties forbid drilling in that sanctuary. According to the foundational criteria of a natural resource, this petroleum reserve is:
        </div>
        <div class="quiz-options">
          <button class="quiz-opt-btn" onclick="checkMCQ(this, 1, 'c')">
            <span>(a) A renewable natural resource because oil naturally regenerates over time.</span>
            <span class="quiz-opt-indicator"></span>
          </button>
          <button class="quiz-opt-btn" onclick="checkMCQ(this, 1, 'c')">
            <span>(b) An active economic resource ready for commercial stock exchange trading.</span>
            <span class="quiz-opt-indicator"></span>
          </button>
          <button class="quiz-opt-btn" onclick="checkMCQ(this, 1, 'c')">
            <span>(c) An element of Nature, but NOT an active resource because it fails economic and cultural feasibility.</span>
            <span class="quiz-opt-indicator"></span>
          </button>
          <button class="quiz-opt-btn" onclick="checkMCQ(this, 1, 'c')">
            <span>(d) An ubiquitous resource because hydrocarbons exist everywhere in the Earth's crust.</span>
            <span class="quiz-opt-indicator"></span>
          </button>
        </div>
        <details class="ans-box" style="display: none; margin-top: 1rem;">
          <summary><span><i class="fa-solid fa-magnifying-glass"></i> Teacher's Trap Analysis &amp; Explanation (Q1)</span></summary>
          <div class="ans-content">
            <p><strong>Correct Answer:</strong> <strong>(c) An element of Nature, but NOT an active resource because it fails economic and cultural feasibility.</strong></p>
            <p><strong>The Trap Explained:</strong> Students frequently confuse <em>Nature</em> with a <em>Resource</em>. An entity occurring in Nature only becomes a resource when it simultaneously satisfies all three filters: (1) Technologically accessible, (2) Economically feasible, and (3) Culturally/legally acceptable. Because extraction costs exceed market value and international treaties ban drilling, it remains neutral environmental stuff. Petroleum is also non-renewable (ruling out option a) and localized rather than ubiquitous (ruling out option d).</p>
          </div>
        </details>
      </div>

      <!-- MCQ 2 -->
      <div id="qcard2" class="quiz-card">
        <div class="quiz-question-text">
          <strong>Question 2:</strong> Which of the following pairs correctly illustrates the precise scientific difference between an <em>Ecosystem Function</em> and an <em>Ecosystem Service</em>?
        </div>
        <div class="quiz-options">
          <button class="quiz-opt-btn" onclick="checkMCQ(this, 2, 'b')">
            <span>(a) Function: A farmer harvesting honey from an artificial wooden beehive; Service: Bees collecting nectar from flowers.</span>
            <span class="quiz-opt-indicator"></span>
          </button>
          <button class="quiz-opt-btn" onclick="checkMCQ(this, 2, 'b')">
            <span>(b) Function: Wetlands filtering suspended sediments and decaying organic matter; Service: Humans obtaining clean drinking water.</span>
            <span class="quiz-opt-indicator"></span>
          </button>
          <button class="quiz-opt-btn" onclick="checkMCQ(this, 2, 'b')">
            <span>(c) Function: Humans constructing a high-capacity concrete dam; Service: Electricity flowing to urban factories.</span>
            <span class="quiz-opt-indicator"></span>
          </button>
          <button class="quiz-opt-btn" onclick="checkMCQ(this, 2, 'b')">
            <span>(d) Function: Burning coal in a thermal power plant; Service: Emitting sulfur dioxide into the atmosphere.</span>
            <span class="quiz-opt-indicator"></span>
          </button>
        </div>
        <details class="ans-box" style="display: none; margin-top: 1rem;">
          <summary><span><i class="fa-solid fa-magnifying-glass"></i> Teacher's Trap Analysis &amp; Explanation (Q2)</span></summary>
          <div class="ans-content">
            <p><strong>Correct Answer:</strong> <strong>(b) Function: Wetlands filtering suspended sediments and decaying organic matter; Service: Humans obtaining clean drinking water.</strong></p>
            <p><strong>The Trap Explained:</strong> An <em>ecosystem function</em> is an inherent biological or physical process that occurs naturally within an ecosystem (wetland filtration). An <em>ecosystem service</em> is the human benefit derived from that natural process (clean drinking water). Options (a) and (c) describe human engineering actions, not ecosystem functions, while option (d) describes pollution.</p>
          </div>
        </details>
      </div>

      <!-- MCQ 3 -->
      <div id="qcard3" class="quiz-card">
        <div class="quiz-question-text">
          <strong>Question 3:</strong> What is the core mechanism underlying the economic phenomenon known as the <em>"Natural Resource Curse"</em> or <em>"Paradox of Plenty"</em>?
        </div>
        <div class="quiz-options">
          <button class="quiz-opt-btn" onclick="checkMCQ(this, 3, 'd')">
            <span>(a) Having natural resources automatically poisons agricultural topsoil through geothermal radiation.</span>
            <span class="quiz-opt-indicator"></span>
          </button>
          <button class="quiz-opt-btn" onclick="checkMCQ(this, 3, 'd')">
            <span>(b) Nations with minerals are legally barred from participating in international trade by the United Nations.</span>
            <span class="quiz-opt-indicator"></span>
          </button>
          <button class="quiz-opt-btn" onclick="checkMCQ(this, 3, 'd')">
            <span>(c) Renewable resources like solar radiation can never generate profitable electricity.</span>
            <span class="quiz-opt-indicator"></span>
          </button>
          <button class="quiz-opt-btn" onclick="checkMCQ(this, 3, 'd')">
            <span>(d) Economies over-relying on raw mineral exports often fail to develop domestic manufacturing, technical skills, and diversified industries.</span>
            <span class="quiz-opt-indicator"></span>
          </button>
        </div>
        <details class="ans-box" style="display: none; margin-top: 1rem;">
          <summary><span><i class="fa-solid fa-magnifying-glass"></i> Teacher's Trap Analysis &amp; Explanation (Q3)</span></summary>
          <div class="ans-content">
            <p><strong>Correct Answer:</strong> <strong>(d) Economies over-relying on raw mineral exports often fail to develop domestic manufacturing, technical skills, and diversified industries.</strong></p>
            <p><strong>The Trap Explained:</strong> The Resource Curse is an economic institutional failure, not a supernatural curse or geographic radiation! Resource-rich countries that simply export unrefined ores or oil become lazy in building schools, technical universities, and manufacturing plants. India avoided this curse by investing heavily in steel mills, refineries, and skilled human engineering.</p>
          </div>
        </details>
      </div>

      <!-- MCQ 4 -->
      <div id="qcard4" class="quiz-card">
        <div class="quiz-question-text">
          <strong>Question 4:</strong> In Punjab, almost 80% of administrative blocks have been classified as "over-exploited" with respect to groundwater. What was the primary agronomic and policy driver of this crisis?
        </div>
        <div class="quiz-options">
          <button class="quiz-opt-btn" onclick="checkMCQ(this, 4, 'a')">
            <span>(a) Widespread cultivation of water-intensive transplanted wetland paddy supported by free, unmetered agricultural electricity.</span>
            <span class="quiz-opt-indicator"></span>
          </button>
          <button class="quiz-opt-btn" onclick="checkMCQ(this, 4, 'a')">
            <span>(b) Construction of too many rainwater harvesting check-dams along the Sutlej and Beas rivers.</span>
            <span class="quiz-opt-indicator"></span>
          </button>
          <button class="quiz-opt-btn" onclick="checkMCQ(this, 4, 'a')">
            <span>(c) Farmers adopting Surapala's *Vrikshayurveda* organic farming techniques across all districts.</span>
            <span class="quiz-opt-indicator"></span>
          </button>
          <button class="quiz-opt-btn" onclick="checkMCQ(this, 4, 'a')">
            <span>(d) Total failure of the southwest monsoon rainfall across northern India for fifty continuous years.</span>
            <span class="quiz-opt-indicator"></span>
          </button>
        </div>
        <details class="ans-box" style="display: none; margin-top: 1rem;">
          <summary><span><i class="fa-solid fa-magnifying-glass"></i> Teacher's Trap Analysis &amp; Explanation (Q4)</span></summary>
          <div class="ans-content">
            <p><strong>Correct Answer:</strong> <strong>(a) Widespread cultivation of water-intensive transplanted wetland paddy supported by free, unmetered agricultural electricity.</strong></p>
            <p><strong>The Trap Explained:</strong> Punjab's climate is semi-arid, yet farmers shifted to wetland paddy (which consumes 3,000–5,000 L of water per kg). The provision of free agricultural electricity caused millions of deep submersible tubewells to run 24/7 without financial cost, drawing water far faster than monsoon recharge.</p>
          </div>
        </details>
      </div>

      <!-- MCQ 5 -->
      <div id="qcard5" class="quiz-card">
        <div class="quiz-question-text">
          <strong>Question 5:</strong> Which ancient Indian scientific text formalized arboriculture and plant pathology in the 10th century CE, recommending seed treatment (*Beeja-samskara*), biological pest repellents, and minimal tillage?
        </div>
        <div class="quiz-options">
          <button class="quiz-opt-btn" onclick="checkMCQ(this, 5, 'c')">
            <span>(a) Kautilya's *Arthashastra*</span>
            <span class="quiz-opt-indicator"></span>
          </button>
          <button class="quiz-opt-btn" onclick="checkMCQ(this, 5, 'c')">
            <span>(b) Charaka's *Charaka Samhita*</span>
            <span class="quiz-opt-indicator"></span>
          </button>
          <button class="quiz-opt-btn" onclick="checkMCQ(this, 5, 'c')">
            <span>(c) Surapala's *Vrikshayurveda*</span>
            <span class="quiz-opt-indicator"></span>
          </button>
          <button class="quiz-opt-btn" onclick="checkMCQ(this, 5, 'c')">
            <span>(d) Aryabhata's *Aryabhatiya*</span>
            <span class="quiz-opt-indicator"></span>
          </button>
        </div>
        <details class="ans-box" style="display: none; margin-top: 1rem;">
          <summary><span><i class="fa-solid fa-magnifying-glass"></i> Teacher's Trap Analysis &amp; Explanation (Q5)</span></summary>
          <div class="ans-content">
            <p><strong>Correct Answer:</strong> <strong>(c) Surapala's *Vrikshayurveda*</strong></p>
            <p><strong>The Trap Explained:</strong> *Arthashastra* is a treatise on statecraft and economics; *Charaka Samhita* deals with human medicine; *Aryabhatiya* deals with astronomy and mathematics. It is Surapala's *Vrikshayurveda* (literally "Ayurveda of Trees") that deals specifically with plant science, organic soil enrichment, and seed preservation.</p>
          </div>
        </details>
      </div>

      <!-- ========================================== -->
      <!-- SUBSECTION 5.2: ASSERTION & REASONING      -->
      <!-- ========================================== -->
      <h3 class="topic-title"><i class="fa-solid fa-scale-balanced"></i> 5.2: Five Assertion &amp; Reasoning Questions</h3>
      <p style="font-size: 0.92rem; color: var(--text-muted); margin-bottom: 1.5rem;">
        <strong>Direction for Questions 6 to 10:</strong> Each item consists of two statements: <strong>Assertion (A)</strong> and <strong>Reason (R)</strong>. Choose the correct code:<br>
        • <strong>(a)</strong> Both (A) and (R) are true, and (R) is the correct explanation of (A).<br>
        • <strong>(b)</strong> Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).<br>
        • <strong>(c)</strong> (A) is true, but (R) is false.<br>
        • <strong>(d)</strong> (A) is false, but (R) is true.
      </p>

      <!-- A&R 1 -->
      <details class="ans-box">
        <summary>
          <span><strong>Question 6:</strong> Assertion: Renewable resources can become non-renewable if overexploited. Reason: Nature's replenishment occurs at finite speeds.</span>
          <span class="badge badge-purple">A&amp;R 1</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> Renewable resources such as groundwater and forest timber can become permanently degraded or functionally non-renewable over time.</p>
          <p><strong>Reason (R):</strong> Nature functions through restorative and regenerative cycles that require time, and extracting resources at a rate exceeding the natural replenishment speed breaks the cycle.</p>
          <div class="step-box">
            <div class="step-title"><i class="fa-solid fa-check"></i> Correct Evaluation: Code (a)</div>
            <p><strong>Analysis:</strong> Both statements are scientifically true, and (R) correctly explains (A). A renewable resource remains renewable only on the condition that $R_Rate_harvest ≤ Rate_replenish. When extraction exceeds replenishment (as seen in Punjab groundwater), the standing resource stock collapses, turning renewable assets into depleted non-renewable assets.</p>
          </div>
        </div>
      </details>

      <!-- A&R 2 -->
      <details class="ans-box">
        <summary>
          <span><strong>Question 7:</strong> Assertion: Having abundant natural resources does not guarantee a region will enjoy economic wealth. Reason: Raw mineral export always generates the highest profit margins.</span>
          <span class="badge badge-purple">A&amp;R 2</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> Regions and nations possessing vast underground endowments of crude oil, diamonds, and iron ore frequently suffer from poverty and sluggish human development.</p>
          <p><strong>Reason (R):</strong> Exporting unprocessed raw minerals generates far higher financial profit margins than domestic industrial manufacturing.</p>
          <div class="step-box">
            <div class="step-title"><i class="fa-solid fa-check"></i> Correct Evaluation: Code (c)</div>
            <p><strong>Analysis:</strong> Assertion (A) is completely true (describing the classic "Paradox of Plenty"). However, Reason (R) is completely false! Raw mineral extraction yields low profit margins and exposes economies to global price volatility; it is high-skill value-adding manufacturing (such as converting raw iron ore into specialized steel or aerospace components) that generates high profit margins and enduring wealth.</p>
          </div>
        </div>
      </details>

      <!-- A&R 3 -->
      <details class="ans-box">
        <summary>
          <span><strong>Question 8:</strong> Assertion: In 2016, Sikkim became the world's first 100% certified organic state. Reason: Farmer incomes rose by 20% on average after the organic transition.</span>
          <span class="badge badge-purple">A&amp;R 3</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> In 2016, the Indian Himalayan state of Sikkim achieved the milestone of becoming the world's first 100% certified organic state across all its farmland.</p>
          <p><strong>Reason (R):</strong> The transition to organic agriculture in Sikkim eventually increased average farmer household incomes by approximately 20% due to premium pricing and zero chemical debt.</p>
          <div class="step-box">
            <div class="step-title"><i class="fa-solid fa-check"></i> Correct Evaluation: Code (b)</div>
            <p><strong>Analysis:</strong> Both statements are factually true based on the textbook caselet. However, Reason (R) is an <em>economic outcome</em> of the transition, not the causal explanation of <em>why</em> the state achieved certification. Certification was achieved through a comprehensive 2003 state government policy that strictly banned chemical imports and subsidized organic compost infrastructure.</p>
          </div>
        </div>
      </details>

      <!-- A&R 4 -->
      <details class="ans-box">
        <summary>
          <span><strong>Question 9:</strong> Assertion: The production of Portland cement is classified as one of the world's most polluting industries. Reason: Cement production releases calcination carbon dioxide and toxic particulate dust.</span>
          <span class="badge badge-purple">A&amp;R 4</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> The manufacture of Portland cement is globally classified among the most environmentally damaging industrial sectors.</p>
          <p><strong>Reason (R):</strong> Cement manufacturing involves heating kilns to 1450°C which burns fossil fuels, chemically calcines limestone releasing vast amounts of CO₂, and generates fine alkaline dust (PM2.5/PM10) that harms lungs and plant foliage.</p>
          <div class="step-box">
            <div class="step-title"><i class="fa-solid fa-check"></i> Correct Evaluation: Code (a)</div>
            <p><strong>Analysis:</strong> Both statements are true, and (R) provides the exact chemical, thermodynamic, and physical explanation of why cement manufacturing carries such a severe environmental footprint.</p>
          </div>
        </div>
      </details>

      <!-- A&R 5 -->
      <details class="ans-box">
        <summary>
          <span><strong>Question 10:</strong> Assertion: Rivers frequently become focal points of intense political disputes across state and national borders. Reason: Nature's hydrological river basins do not align with human political boundaries.</span>
          <span class="badge badge-purple">A&amp;R 5</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> Rivers like the Kaveri in southern India frequently trigger severe political and legal disputes among riparian states.</p>
          <p><strong>Reason (R):</strong> Natural river drainage basins function as unified ecological systems that cut across man-made administrative and political borders.</p>
          <div class="step-box">
            <div class="step-title"><i class="fa-solid fa-check"></i> Correct Evaluation: Code (a)</div>
            <p><strong>Analysis:</strong> Both statements are true, and (R) directly explains (A). Because rivers ignore political boundaries, upstream users (e.g., Karnataka) can alter river flows to downstream recipients (e.g., Tamil Nadu), making shared resource governance a major source of interstate tension.</p>
          </div>
        </div>
      </details>

      <!-- ========================================== -->
      <!-- SUBSECTION 5.3: SHORT ANSWER QUESTIONS     -->
      <!-- ========================================== -->
      <h3 class="topic-title"><i class="fa-solid fa-pencil"></i> 5.3: Six Short Answer Questions (2 Marks &amp; 3 Marks)</h3>

      <!-- SAQ 1 -->
      <details class="ans-box">
        <summary>
          <span><strong>Question 11 (2 Marks):</strong> State the three mandatory criteria an element of Nature must satisfy to be classified as a natural resource.</span>
          <span class="badge badge-blue">2 Marks</span>
        </summary>
        <div class="ans-content">
          <p>To qualify as a natural resource, an element of Nature must satisfy:</p>
          <ol>
            <li><strong>Technologically Accessible:</strong> Humans must possess the engineering tools and scientific knowledge to locate and extract it.</li>
            <li><strong>Economically Feasible:</strong> The market value derived from the substance must exceed the capital cost of extraction and refinement.</li>
            <li><strong>Culturally Acceptable:</strong> Its extraction must conform to social ethics, community rights, and traditional reverence (e.g., preserving sacred groves).</li>
          </ol>
        </div>
      </details>

      <!-- SAQ 2 -->
      <details class="ans-box">
        <summary>
          <span><strong>Question 12 (2 Marks):</strong> Differentiate between Nature's 'Restoration' and 'Regeneration' with one simple example of each.</span>
          <span class="badge badge-blue">2 Marks</span>
        </summary>
        <div class="ans-content">
          <ul>
            <li><strong>Restoration:</strong> The process of returning an ecosystem back to its original healthy baseline state after experiencing damage. <em>Example:</em> Planting native saplings to re-establish a forest patch cleared for temporary construction, or a human skin cut healing naturally.</li>
            <li><strong>Regeneration:</strong> The proactive capacity of living ecosystems to create new life, cycle nutrients, build topsoil, and evolve thriving conditions. <em>Example:</em> A dead tree falling in an old forest, decomposing via fungi into rich humus that nourishes thousands of new tree seedlings and insects without any human waste.</li>
          </ul>
        </div>
      </details>

      <!-- SAQ 3 -->
      <details class="ans-box">
        <summary>
          <span><strong>Question 13 (3 Marks):</strong> Why is the Bhadla Solar Park in Rajasthan considered a symbol of India's green energy transition? State three key facts.</span>
          <span class="badge badge-blue">3 Marks</span>
        </summary>
        <div class="ans-content">
          <p>The Bhadla Solar Park exemplifies India's clean energy leadership because:</p>
          <ol>
            <li><strong>Massive Gigawatt Scale:</strong> Spanning over 14,000 acres in the arid Thar Desert (Phalodi district), it is one of the world's largest solar installations with an installed capacity exceeding <strong>2,245 Megawatts (MW)</strong>.</li>
            <li><strong>Substantial Power Contribution:</strong> It generates enough clean electricity to fulfill approximately <strong>15% of Rajasthan's total electrical power demand</strong>, substituting millions of tonnes of coal combustion.</li>
            <li><strong>Historic Cost Reductions:</strong> It demonstrated that large-scale utility solar can produce electricity at tariffs lower than coal-fired thermal power (under ₹2.50 per kWh), proving clean energy is economically superior.</li>
          </ol>
        </div>
      </details>

      <!-- SAQ 4 -->
      <details class="ans-box">
        <summary>
          <span><strong>Question 14 (3 Marks):</strong> What is ancient Indian Wootz steel, and how does it demonstrate value-addition over raw mineral export?</span>
          <span class="badge badge-blue">3 Marks</span>
        </summary>
        <div class="ans-content">
          <ol>
            <li><strong>Definition &amp; Metallurgy:</strong> Wootz steel (*Ukku*) was a legendary crucible steel developed in ancient South India over 2,000 years ago, renowned across the ancient world (as Damascus steel) for its razor sharpness, wavy water patterns, and extraordinary toughness.</li>
            <li><strong>Crucible Technology:</strong> Indian metallurgists did not merely export raw iron ore; they packed high-grade ore with carbonaceous plant chips and glass inside sealed clay crucibles, firing them at extreme furnace temperatures to create carbon nanotube microstructures.</li>
            <li><strong>Value Addition Proof:</strong> Converting cheap, abundant iron rocks into highly valued swords, armor, and surgical scalpels traded across Rome and Asia allowed ancient Indian kingdoms to accumulate immense wealth and avoid the raw resource export trap.</li>
          </ol>
        </div>
      </details>

      <!-- SAQ 5 -->
      <details class="ans-box">
        <summary>
          <span><strong>Question 15 (3 Marks):</strong> Explain how the International Solar Alliance (ISA) fosters global cooperation in renewable energy.</span>
          <span class="badge badge-blue">3 Marks</span>
        </summary>
        <div class="ans-content">
          <ol>
            <li><strong>Origin &amp; Headquarters:</strong> Launched jointly by India and France at the COP21 Paris Climate Summit in 2015, the ISA is headquartered in <strong>Gurugram, Haryana, India</strong>.</li>
            <li><strong>Targeting "Suryaputra" Nations:</strong> It focuses on sunshine-rich developing nations situated between the Tropics of Cancer and Capricorn, helping them leapfrog fossil fuels directly to solar power.</li>
            <li><strong>Financial Mobilization &amp; OSOWOG Grid:</strong> The alliance aims to mobilize over $1 trillion in affordable solar financing by 2030 and coordinates the visionary <strong>"One Sun One World One Grid" (OSOWOG)</strong> project to interconnect regional solar grids across continents.</li>
          </ol>
        </div>
      </details>

      <!-- SAQ 6 -->
      <details class="ans-box">
        <summary>
          <span><strong>Question 16 (2 Marks):</strong> What does the philosophical concept of *Lokasangraha* mean in the context of natural resource management?</span>
          <span class="badge badge-blue">2 Marks</span>
        </summary>
        <div class="ans-content">
          <ul>
            <li><strong>Philosophical Meaning:</strong> Derived from the <em>Bhagavad Gita</em>, *Lokasangraha* signifies <strong>selfless action undertaken for the universal maintenance, protection, and collective wellbeing of all creation</strong>.</li>
            <li><strong>Environmental Stewardship:</strong> It instructs humans to reject selfish, short-sighted consumer greed and act as responsible guardians (stewards) of the Earth, safeguarding clean air, living soils, and pure water for current vulnerable communities and future generations.</li>
          </ul>
        </div>
      </details>

      <!-- ========================================== -->
      <!-- SUBSECTION 5.4: LONG ANSWER QUESTIONS      -->
      <!-- ========================================== -->
      <h3 class="topic-title"><i class="fa-solid fa-file-lines"></i> 5.4: Four Long Answer Questions (5 Marks Each) with CBSE Marking Schemes</h3>

      <!-- LAQ 1 -->
      <details class="ans-box">
        <summary>
          <span><strong>Question 17 (5 Marks):</strong> Describe the Punjab groundwater crisis in detail: analyze its historical origin, hydrogeological consequences, and four sustainable remedies.</span>
          <span class="badge badge-amber">5 Marks</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-title"><i class="fa-solid fa-clipboard-check"></i> Official CBSE Marking Scheme (5 Marks Breakdown)</div>
            <p>• Historical origin: Green revolution &amp; policy drivers (1 Mark)<br>
            • Hydrogeological reality: Agronomic water mismatch (1 Mark)<br>
            • Quantitative crisis metrics: Water table drop &amp; overexploited blocks (1 Mark)<br>
            • Four concrete sustainable remedial actions (2 Marks)</p>
          </div>
          <div class="step-box">
            <div class="step-title"><i class="fa-solid fa-file-pen"></i> Model Answer</div>
            <p><strong>1. Historical Origin &amp; Policy Drivers:</strong> In the 1960s, Punjab spearheaded India's Green Revolution, adopting High-Yielding Varieties (HYV) of Mexican dwarf wheat and dwarf paddy. To ensure maximum grain production, the government provided free, unmetered agricultural electricity, encouraging farmers to install millions of high-capacity electric submersible tubewells.</p>
            <p><strong>2. Agronomic &amp; Hydrogeological Mismatch:</strong> Punjab is climatically a semi-arid region. Transplanted wetland paddy requires 3,000 to 5,000 litres of water to produce just 1 kilogram of grain. Pumping out deep groundwater 24/7 far exceeded the annual monsoon recharge rate, resulting in severe hydrogeological overdraft.</p>
            <p><strong>3. Current Crisis Metrics:</strong> Today, <strong>almost 80% of Punjab's administrative blocks are classified as 'over-exploited'</strong>. The water table has plummeted from a comfortable 5m below ground level in the 1970s to alarming depths exceeding 40m bgl. Deep pumping has dried out shallow village wells and drawn up toxic subterranean minerals (arsenic, fluorides, and heavy salts).</p>
            <p><strong>4. Four Sustainable Remedial Solutions:</strong></p>
            <ol>
              <li><em>Crop Diversification:</em> Transitioning agricultural acreage away from wetland paddy into indigenous low-water crops (millets, maize, cotton, and pulses) backed by guaranteed Minimum Support Prices (MSP).</li>
              <li><em>Power Tariff Reform:</em> Replacing unmetered free electricity with Direct Benefit Transfer (DBT) and cash incentives for water conservation.</li>
              <li><em>Laser Land Leveling &amp; Direct Seeded Rice (DSR):</em> Eliminating continuous flood ponding and adopting DSR techniques to save up to 25% of irrigation water.</li>
              <li><em>Mandatory Aquifer Recharge:</em> Large-scale construction of percolation shafts, check-dams, and village pond renovation to inject monsoon runoff directly back into depleted subterranean aquifers.</li>
            </ol>
          </div>
        </div>
      </details>

      <!-- LAQ 2 -->
      <details class="ans-box">
        <summary>
          <span><strong>Question 18 (5 Marks):</strong> Explain the "Paradox of Plenty" (Resource Curse). Why does it occur, and how did India overcome it? Contrast with a historical case.</span>
          <span class="badge badge-amber">5 Marks</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-title"><i class="fa-solid fa-clipboard-check"></i> Official CBSE Marking Scheme (5 Marks Breakdown)</div>
            <p>• Precise definition of the Paradox of Plenty / Resource Curse (1 Mark)<br>
            • Economic mechanisms causing the curse (1.5 Marks)<br>
            • Strategy adopted by India to escape the curse (1.5 Marks)<br>
            • Historical illustration: Ancient Indian Wootz steel (1 Mark)</p>
          </div>
          <div class="step-box">
            <div class="step-title"><i class="fa-solid fa-file-pen"></i> Model Answer</div>
            <p><strong>1. Definition:</strong> The <em>Paradox of Plenty</em> (or the <em>Natural Resource Curse</em>) is the economic phenomenon where nations and regions endowed with abundant non-renewable natural resources (like minerals and crude oil) often experience slower economic growth, greater inequality, and worse human development outcomes than resource-poor nations.</p>
            <p><strong>2. Why the Curse Occurs:</strong></p>
            <ul>
              <li><em>Raw Commodity Export Dependency:</em> Economies depend entirely on digging up raw dirt or crude oil and shipping it abroad without domestic processing.</li>
              <li><em>Neglect of Human Capital:</em> Governments neglect investments in public schools, research universities, and diversified manufacturing because easy mineral revenues flow into state coffers.</li>
              <li><em>Price Volatility &amp; Corruption:</em> When global commodity prices crash, national budgets collapse into severe debt and social unrest.</li>
            </ul>
            <p><strong>3. How India Overcame the Curse:</strong> India avoided this trap by pursuing a deliberate national policy of <strong>domestic value addition</strong>:</p>
            <ul>
              <li>Constructing integrated steel plants (Rourkela, Bhilai, Durgapur, Bokaro) to process raw iron ore into structural steel domestically.</li>
              <li>Establishing premier higher education institutions (IITs, NITs, CSIR labs) to train world-class engineers, scientists, and technicians.</li>
              <li>Developing complex manufacturing (automobiles, aerospace, pharmaceuticals, railways), turning raw materials into finished consumer goods.</li>
            </ul>
            <p><strong>4. Historical Precedent (Wootz Steel):</strong> Over 2,000 years ago, ancient Indian metallurgists demonstrated this principle by smelting iron ore in clay crucibles to create Wootz steel (*Ukku*). By adding human skill, carbonaceous wood, and thermodynamic expertise, they transformed ordinary iron ore into world-renowned sword steel, amassing wealth through advanced metallurgical craftsmanship.</p>
          </div>
        </div>
      </details>

      <!-- LAQ 3 -->
      <details class="ans-box">
        <summary>
          <span><strong>Question 19 (5 Marks):</strong> Examine the environmental challenges of the cement manufacturing industry and evaluate three sustainable alternative building materials.</span>
          <span class="badge badge-amber">5 Marks</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-title"><i class="fa-solid fa-clipboard-check"></i> Official CBSE Marking Scheme (5 Marks Breakdown)</div>
            <p>• Industrial indispensability of cement vs. environmental impact (1 Mark)<br>
            • Detailed analysis of emissions (CO₂ and PM2.5/PM10) (1.5 Marks)<br>
            • Three sustainable eco-friendly alternatives with examples (2 Marks)<br>
            • Concluding policy synthesis (0.5 Mark)</p>
          </div>
          <div class="step-box">
            <div class="step-title"><i class="fa-solid fa-file-pen"></i> Model Answer</div>
            <p><strong>1. The Modern Cement Dilemma:</strong> Portland cement is the literal foundation of modern urban development (used in high-rises, bridges, airports, and roads). However, cement manufacturing is classified among the world's most polluting industrial sectors.</p>
            <p><strong>2. Detailed Environmental Impact:</strong></p>
            <ul>
              <li><em>Heavy Greenhouse Gas Emissions:</em> Cement production is responsible for roughly 7% to 8% of total global carbon dioxide emissions. The chemical calcination of limestone (CaCO₃ &rarr; CaO + CO₂) and the combustion of fossil fuels to heat rotary kilns to 1450°C release ~0.85 tonnes of CO₂ for every single tonne of cement manufactured.</li>
              <li><em>Toxic Particulate Dust (PM2.5 &amp; PM10):</em> Grinding clinker and quarrying limestone releases clouds of fine alkaline dust. Inhaled dust induces silicosis and chronic bronchitis in humans and animals, while settling on nearby crop leaves to block stomata and reduce agricultural yields.</li>
            </ul>
            <p><strong>3. Three Sustainable Eco-Alternatives:</strong></p>
            <ol>
              <li><em>Compressed Stabilised Earth Blocks (CSEB) - Auroville Model:</em> The Auroville Earth Institute (UNESCO Chair for Earthen Architecture) manufactures CSEBs using locally excavated subsoil compressed with a tiny fraction of stabilizer. CSEBs possess high compressive strength, require zero kiln firing, and consume 80% less embodied energy than cement bricks.</li>
              <li><em>Traditional Mud &amp; Sandstone Architecture - Jaisalmer Fort:</em> The 12th-century Jaisalmer Fort in Rajasthan stands as living architectural proof that mud and local sandstone structures can endure for over 800 years in extreme desert climates while naturally regulating indoor temperatures.</li>
              <li><em>Blended &amp; Industrial By-Product Cements:</em> Replacing Portland clinker with industrial waste by-products, such as pulverized fuel ash (fly-ash from thermal power plants) and granulated blast furnace slag (GGBS from steel mills), significantly lowers clinker ratios and cuts process emissions.</li>
            </ol>
            <p><strong>Conclusion:</strong> Modern construction must transition from clinker-heavy concrete to bio-composite, earthen, and recycled circular materials to decouple infrastructure growth from environmental destruction.</p>
          </div>
        </div>
      </details>

      <!-- LAQ 4 -->
      <details class="ans-box">
        <summary>
          <span><strong>Question 20 (5 Marks):</strong> Analyze the agro-ecological transition in Sikkim. Detail the problems of chemical farming, the 5-year transition curve, and the tripartite benefits achieved.</span>
          <span class="badge badge-amber">5 Marks</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-title"><i class="fa-solid fa-clipboard-check"></i> Official CBSE Marking Scheme (5 Marks Breakdown)</div>
            <p>• Initial crisis of chemical agriculture &amp; debt cycle (1 Mark)<br>
            • The 2003 state policy and 5-year detoxification dip (1.5 Marks)<br>
            • Ecological restoration mechanisms used (1 Mark)<br>
            • Tripartite outcomes: Economic (+20% income), Ecological, and Tourism (1.5 Marks)</p>
          </div>
          <div class="step-box">
            <div class="step-title"><i class="fa-solid fa-file-pen"></i> Model Answer</div>
            <p><strong>1. The Chemical Agriculture Trap:</strong> By the early 2000s, farmers in Sikkim (like Pema's family) faced mounting debt and declining harvests. Decades of heavy synthetic chemical fertilizers and pesticides had killed the natural soil microbiome, requiring higher fertilizer doses each year while profit margins shrank.</p>
            <p><strong>2. The Bold Policy Decision &amp; The 5-Year Detoxification Dip:</strong> In 2003, the Government of Sikkim took the historic decision to phase out all chemical fertilizers and pesticides. The transition was arduous: during the first 3 to 5 years, crop yields experienced a noticeable dip as exhausted soils detoxified from residual chemicals and beneficial subterranean microbes rebuilt their populations.</p>
            <p><strong>3. Ecological Practices Implemented:</strong> Farmers revived principles mirroring Surapala's *Vrikshayurveda*:</p>
            <ul>
              <li>Replaced synthetic urea with farm-made vermicompost, cattle manure, and green cover crops.</li>
              <li>Formulated natural bio-pesticides using extracts of neem, garlic, cow urine, and local medicinal plants.</li>
              <li>Practiced multi-cropping and crop rotation with nitrogen-fixing pulses to restore soil fertility naturally.</li>
            </ul>
            <p><strong>4. Tripartite Outcomes Achieved (2016 Full Certification):</strong></p>
            <ul>
              <li><em>Economic Prosperity:</em> In 2016, Sikkim became the world's first 100% certified organic state. Farmers commanded high premium prices for organic ginger, turmeric, and large cardamom, resulting in an <strong>average household income increase of 20%</strong> and the complete elimination of chemical input debt.</li>
              <li><em>Ecological Revival:</em> Toxic chemical runoff into Himalayan streams dropped to zero; wild pollinator populations (bees, butterflies) flourished; and mountain soil biological health was fully restored.</li>
              <li><em>Eco-Tourism Boom:</em> Sikkim became a world-renowned destination for eco-conscious travelers seeking pristine mountain landscapes and organic farm-to-table cuisine, generating valuable rural employment.</li>
            </ul>
          </div>
        </div>
      </details>

      <!-- ========================================== -->
      <!-- SUBSECTION 5.5: COMPETENCY CASE STUDIES    -->
      <!-- ========================================== -->
      <h3 class="topic-title"><i class="fa-solid fa-microscope"></i> 5.5: Two Competency-Based Real-World Case Studies</h3>

      <!-- CASE STUDY 1 -->
      <details class="ans-box">
        <summary>
          <span><strong>Case Study 1:</strong> Hydrogeological Overdraft &amp; Aquifer Depletion in Punjab</span>
          <span class="badge badge-rose">Case Study 1</span>
        </summary>
        <div class="ans-content">
          <div style="background: #f8fafc; border-left: 4px solid var(--rose); padding: 1.2rem; border-radius: 8px; margin-bottom: 1.25rem;">
            <p style="font-size: 0.94rem; line-height: 1.7; margin-bottom: 0;">
              <strong>Read the Source Passage Carefully:</strong><br>
              <em>"A crisis has unfolded in the fertile plains of Punjab where groundwater resources have been severely depleted. Punjab was home to the Green Revolution that fed a large proportion of our population and contributed to India becoming self-sufficient in food. Today the same state faces issues of sustainability&mdash;Nature has been exploited beyond regeneration... Almost 80% of the area of Punjab has been classified as 'over-exploited'; in other words, we have drawn water at a rate much greater than at which restoration and rejuvenation of groundwater is possible. We can see that food security was ensured for the short term, but the long-term consequences will take time and effort to heal." (NCERT Class 8, Chapter 1, Pages 13&ndash;14)</em>
            </p>
          </div>

          <p><strong>Competency-Based Questions &amp; Detailed Model Answers:</strong></p>
          <div class="step-box">
            <div class="step-title"><i class="fa-solid fa-circle-question"></i> Sub-Question 1: What does an "over-exploited" administrative block mean in hydrogeology? (1 Mark)</div>
            <p><strong>Answer:</strong> An administrative block is classified as "over-exploited" when the annual net extraction of groundwater exceeds the annual net recharge received from rainfall and surface water, resulting in a persistent, long-term lowering of the groundwater table.</p>
          </div>

          <div class="step-box">
            <div class="step-title"><i class="fa-solid fa-circle-question"></i> Sub-Question 2: Explain how food security in the short term created environmental insecurity in the long term. (2 Marks)</div>
            <p><strong>Answer:</strong> In the short term (1960s–1980s), shifting to High-Yielding Varieties of wheat and transplanted paddy eliminated famine and created national food self-sufficiency. However, because transplanted rice in a semi-arid zone consumes 4,000 litres of water per kilogram, continuous deep pumping over four decades depleted aquifers past 40m bgl, dried out shallow wells, salinized soils, and created a grave long-term water crisis for agriculture.</p>
          </div>

          <div class="step-box">
            <div class="step-title"><i class="fa-solid fa-circle-question"></i> Sub-Question 3: Suggest two technological or policy interventions that can reverse this crisis. (2 Marks)</div>
            <p><strong>Answer:</strong> (1) <em>Agronomic Diversification:</em> Incentivizing farmers to replace summer wetland paddy with drought-tolerant millets, maize, and pulses backed by Minimum Support Prices; (2) <em>Direct Seeded Rice (DSR) &amp; Artificial Aquifer Recharge:</em> Mandating laser leveling, drip irrigation, and constructing deep recharge shafts to channel monsoon runoff directly into depleted aquifers.</p>
          </div>
        </div>
      </details>

      <!-- CASE STUDY 2 -->
      <details class="ans-box">
        <summary>
          <span><strong>Case Study 2:</strong> Surapala's *Vrikshayurveda* &amp; The Regenerative Architecture of Modern Organic Farming</span>
          <span class="badge badge-green">Case Study 2</span>
        </summary>
        <div class="ans-content">
          <div style="background: #f8fafc; border-left: 4px solid var(--primary); padding: 1.2rem; border-radius: 8px; margin-bottom: 1.25rem;">
            <p style="font-size: 0.94rem; line-height: 1.7; margin-bottom: 0;">
              <strong>Read the Source Passage Carefully:</strong><br>
              <em>"Vrikshayurveda is an ancient Indian botanical science that focuses on the study and care of plants and trees. The term comes from Sanskrit, with vriksha meaning tree and ayurveda meaning the science of life or health. This traditional knowledge system dates back several millennia and was formalised in texts such as Surapala’s Vrikshayurveda around the 10th century CE. It has elaborate recommendations on the specific plants to be grown on different soil types, and provides intricate methods for seed collection, preservation, and pre-planting treatments... It specifies pest management strategies through natural repellents and plants that should be grown together. This form of sustainable agriculture promotes practices like crop rotation and mixed cropping to maintain soil health." (NCERT Class 8, Chapter 1, Page 16)</em>
            </p>
          </div>

          <p><strong>Competency-Based Questions &amp; Detailed Model Answers:</strong></p>
          <div class="step-box">
            <div class="step-title"><i class="fa-solid fa-circle-question"></i> Sub-Question 1: What is the linguistic etymology and historical date of Surapala's *Vrikshayurveda*? (1 Mark)</div>
            <p><strong>Answer:</strong> The term originates from two Sanskrit roots: <em>Vriksha</em> (meaning tree or plant) and <em>Ayurveda</em> (meaning the science or knowledge of life). The formal treatise was authored by the scholar-physician Surapala around the <strong>10th century CE</strong>.</p>
          </div>

          <div class="step-box">
            <div class="step-title"><i class="fa-solid fa-circle-question"></i> Sub-Question 2: How did *Vrikshayurveda* manage pests without synthetic chemical pesticides? (2 Marks)</div>
            <p><strong>Answer:</strong> Surapala formulated botanical pest repellents prepared from natural ingredients with antiparasitic properties&mdash;including decoctions of <strong>neem (*Azadirachta indica*), garlic (*Allium sativum*), and turmeric</strong>&mdash;combined with <strong>companion planting</strong> (growing specific aromatic crops together so natural scents confuse and deter harmful insects while protecting beneficial bees).</p>
          </div>

          <div class="step-box">
            <div class="step-title"><i class="fa-solid fa-circle-question"></i> Sub-Question 3: Why does *Vrikshayurveda* advocate gentle shallow ploughing instead of deep mechanical pulverization? (2 Marks)</div>
            <p><strong>Answer:</strong> Gentle shallow tillage causes minimal disruption to the delicate subterranean ecosystem. It preserves subterranean moisture, prevents destructive soil erosion, and protects living soil organisms&mdash;such as earthworms (*Kanchuvata*), nitrogen-fixing bacteria, and symbiotic mycorrhizal fungi&mdash;which maintain natural soil fertility.</p>
          </div>
        </div>
      </details>

      <!-- ========================================== -->
      <!-- SUBSECTION 5.6: PYQS & MOST PROBABLE EXAM  -->
      <!-- ========================================== -->
      <h3 class="topic-title"><i class="fa-solid fa-fire"></i> 5.6: Five Previous Years Questions (PYQs) &amp; Most Probable Exam Questions</h3>

      <!-- PYQ 1 -->
      <details class="ans-box">
        <summary>
          <span><strong>Question 23 (PYQ):</strong> "Natural resources are a free gift of Nature." Critically examine this statement in light of human knowledge and technological development. (3 Marks)</span>
          <span class="badge badge-amber">PYQ • 3 Marks</span>
        </summary>
        <div class="ans-content">
          <p><strong>Model Answer:</strong></p>
          <ol>
            <li><strong>Initial Validity:</strong> The statement is true in the sense that the raw physical elements of Nature&mdash;such as sunshine, rainfall, atmospheric air, and tectonic mineral veins&mdash;were created by cosmic and Earth processes without any human labour.</li>
            <li><strong>Critical Geographic Rebuttal:</strong> However, modern geography rejects the simplistic idea that resources are mere "free gifts." An element of Nature does not become a functioning resource until human beings apply <strong>scientific technology, financial capital, and skilled labour</strong> to locate, extract, refine, and transform it.</li>
            <li><strong>Example:</strong> Petroleum trapped beneath the seabed was completely useless to prehistoric humans; it became an invaluable energy resource only after modern engineering developed offshore drilling platforms and petrochemical refineries. As economist Erich Zimmermann stated: <em>"Resources are not; they become."</em></li>
          </ol>
        </div>
      </details>

      <!-- PYQ 2 -->
      <details class="ans-box">
        <summary>
          <span><strong>Question 24 (PYQ):</strong> Explain the uneven distribution of mineral resources in India with three geographic examples from different geological zones. (3 Marks)</span>
          <span class="badge badge-amber">PYQ • 3 Marks</span>
        </summary>
        <div class="ans-content">
          <p><strong>Model Answer:</strong> Minerals in India are heavily concentrated in specific geological rock formations:</p>
          <ol>
            <li><strong>The Chota Nagpur &amp; Eastern Peninsular Plateau (Jharkhand, Odisha, Chhattisgarh):</strong> Composed of ancient Gondwana sedimentary rifts and Archean crystalline shields, this region holds the vast majority of India's coking coal (Jharia, Bokaro) and high-grade hematite iron ore (Keonjhar, Mayurbhanj).</li>
            <li><strong>The Coastal Sedimentary Basins (Mumbai High &amp; Assam):</strong> Thick marine and deltaic tertiary sedimentary strata trap hydrocarbons, making offshore Mumbai High and upper Assam (Digboi, Naharkatia) India's primary domestic petroleum zones.</li>
            <li><strong>The Arid Western Shield (Rajasthan):</strong> Ancient Aravalli metamorphic formations contain major deposits of non-ferrous minerals like copper (Khetri), lead, zinc, and building stones (limestone and marble).</li>
          </ol>
        </div>
      </details>

      <!-- PYQ 3 -->
      <details class="ans-box">
        <summary>
          <span><strong>Question 25 (Most Probable):</strong> Distinguish between 'Environmental Exploitation' and 'Environmental Stewardship'. Why is stewardship the need of the hour? (3 Marks)</span>
          <span class="badge badge-amber">Probable • 3 Marks</span>
        </summary>
        <div class="ans-content">
          <p><strong>Model Answer:</strong></p>
          <table class="data-table">
            <thead>
              <tr>
                <th>Basis</th>
                <th>Environmental Exploitation</th>
                <th>Environmental Stewardship</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Core Mindset</strong></td>
                <td>Humans as masters entitled to extract Nature without limits for short-term commercial gain.</td>
                <td>Humans as caretakers and guardians (*Lokasangraha*) holding the living Earth in trust for future generations.</td>
              </tr>
              <tr>
                <td><strong>Harvesting Rate</strong></td>
                <td>Exceeds carrying capacity (Rate of Harvest &gt; Rate of Replenishment), causing resource collapse.</td>
                <td>Maintained strictly within natural restorative and regenerative speeds ($R_Rate_harvest ≤ Rate_replenish).</td>
              </tr>
              <tr>
                <td><strong>Waste Philosophy</strong></td>
                <td>Linear economy: "Take, Make, Dispose" creating toxic dumps and river dead zones.</td>
                <td>Circular economy: Zero-waste design mimicking nature where every by-product becomes biological food.</td>
              </tr>
            </tbody>
          </table>
          <p><strong>Why Stewardship is Essential:</strong> With runaway climate change, Himalayan glacier retreat, and 80% over-exploited aquifers in key agricultural states, only stewardship can prevent catastrophic civilizational collapse.</p>
        </div>
      </details>

      <!-- PYQ 4 -->
      <details class="ans-box">
        <summary>
          <span><strong>Question 26 (Most Probable):</strong> What is 'Environmental Justice'? How is resource degradation fundamentally unfair to the weaker sections of society? (3 Marks)</span>
          <span class="badge badge-amber">Probable • 3 Marks</span>
        </summary>
        <div class="ans-content">
          <p><strong>Model Answer:</strong></p>
          <ol>
            <li><strong>Definition of Environmental Justice:</strong> The principle that all citizens&mdash;regardless of income, caste, gender, or social background&mdash;are entitled to equal protection from environmental pollution and equal access to clean natural resources (pure air and potable water).</li>
            <li><strong>Disproportionate Burden on the Poor:</strong> In urban areas, factories and waste treatment facilities are frequently located adjacent to low-income settlements and slums. Marginalized communities breathe noxious industrial particulates (PM2.5) and drink contaminated groundwater.</li>
            <li><strong>Inequality in Adaptation:</strong> Affluent urban households insulate themselves using reverse osmosis (RO) water purifiers, air-conditioned indoor enclosures, and bottled spring water. The daily-wage earner cannot afford these technological shields, bearing the full brunt of pollution through chronic illness, hospital debt, and lost work days.</li>
          </ol>
        </div>
      </details>

      <!-- PYQ 5 -->
      <details class="ans-box">
        <summary>
          <span><strong>Question 27 (Most Probable):</strong> "Nature does not pay attention to political boundaries." Elucidate with reference to interstate river water disputes in India. (3 Marks)</span>
          <span class="badge badge-amber">Probable • 3 Marks</span>
        </summary>
        <div class="ans-content">
          <p><strong>Model Answer:</strong></p>
          <ol>
            <li><strong>Hydrological Unity vs. Political Borders:</strong> Natural river catchments and drainage basins were carved by geology long before human governments drew state boundaries. A river like the Kaveri forms a single continuous hydrological system from the Western Ghats to the Bay of Bengal.</li>
            <li><strong>The Riparian Conflict:</strong> The Kaveri river flows through Karnataka, Tamil Nadu, Kerala, and Puducherry. During monsoon deficit years, Karnataka requires water for irrigation in the Mandya basin and drinking water for Bengaluru, while Tamil Nadu farmers in the fertile Thanjavur delta depend on timely releases for their primary paddy crop (*Kuruvai*).</li>
            <li><strong>The Solution:</strong> Because nature ignores state borders, solutions cannot be unilateral. They require federal water dispute tribunals, scientific distress-sharing formulas, and collaborative basin-wide ecological management.</li>
          </ol>
        </div>
      </details>
    </section>
"""
