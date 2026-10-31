# -*- coding: utf-8 -*-
"""
Section 6: Exam Hall Trap Alerts & 15 Revision Points + Footer & Scripts
Class 8 Mathematics Chapter 10: Proportional Reasoning - 2
"""

def get_section_6():
    return """
    <!-- ==========================================================
         SECTION 6: EXAM HALL TRAP ALERTS & 15 REVISION POINTS
         ========================================================== -->
    <section id="section6" class="section-box">
      <div class="section-header">
        <div class="section-header-left">
          <span class="section-tag"><i class="fa-solid fa-triangle-exclamation"></i> Error Prevention &amp; Final Review</span>
          <h2 class="section-title">Section 6: Exam Hall Trap Alerts &amp; 15 Revision Points</h2>
          <p class="section-desc">
            The ultimate exam guardrail. Review the top 5 conceptual traps that cost students marks and commit the 15 golden high-yield revision principles to memory.
          </p>
        </div>
      </div>

      <!-- Top 5 Exam Hall Trap Alerts -->
      <h3 style="font-size: 1.35rem; color: var(--danger); margin: 1.5rem 0 1.25rem;">
        <i class="fa-solid fa-shield-halved"></i> The 5 Most Dangerous Student Blunders &amp; How to Avoid Them
      </h3>

      <!-- Trap 1 -->
      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-triangle-exclamation"></i> Blunder 1: The "Averaging Time" Trap in Combined Work Problems</div>
        <p><strong>The Typical Student Error:</strong><br>
        <em>"If Ram takes 4 hours to paint a room and Shyam takes 6 hours, working together they will take (4 + 6) ÷ 2 = 5 hours!"</em></p>
        <p><strong>Why This Fails Mathematically &amp; Logically:</strong><br>
        Think about this: If Ram can finish the entire room alone in 4 hours, having a friend help him <em>CANNOT make it take longer than 4 hours</em>! Combining workers always reduces completion time to less than the fastest individual worker's time.</p>
        <p><strong>The Correct Mathematical Method:</strong><br>
        You <strong>cannot average times</strong>; you must <strong>sum their reciprocal rates of work</strong>!
        </p>
        <div class="math-block">
          Ram's 1-hour rate = 1/4 &nbsp;|&nbsp; Shyam's 1-hour rate = 1/6<br>
          Combined Rate = 1/4 + 1/6 = 3/12 + 2/12 = 5/12 of the room per hour.<br>
          True Combined Time = 1 ÷ (5/12) = 12/5 = 2.4 hours (2 hours 24 minutes)!
        </div>
      </div>

      <!-- Trap 2 -->
      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-triangle-exclamation"></i> Blunder 2: The Unit Conversion Blindspot in Cartographic Scales (RF)</div>
        <p><strong>The Typical Student Error:</strong><br>
        <em>"On a map with RF 1 : 50,000, 3 cm represents 3 × 50,000 = 1,50,000 km on the ground."</em></p>
        <p><strong>Why This Fails Mathematically:</strong><br>
        A Representative Fraction is a pure, unitless ratio. 1 cm on paper represents 50,000 <strong>centimetres</strong> on the ground, not kilometres! 1,50,000 km would circle the entire globe nearly 4 times!</p>
        <p><strong>The Correct Mathematical Method:</strong><br>
        Always execute the two-tier metric conversion chain:
        </p>
        <div class="math-block">
          1. cm to metres: Divide by 100 &nbsp;⇒&nbsp; 1,50,000 ÷ 100 = 1,500 m<br>
          2. metres to km: Divide by 1,000 &nbsp;⇒&nbsp; 1,500 ÷ 1,000 = 1.5 km!<br>
          Master Rule: Ground km = (Map cm × Scale Denominator) ÷ 1,00,000.
        </div>
      </div>

      <!-- Trap 3 -->
      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-triangle-exclamation"></i> Blunder 3: The Cross-Multiplication Misapplication in Inverse Variation</div>
        <p><strong>The Typical Student Error:</strong><br>
        <em>"If 20 workers take 4 days, then 10 workers take x days: 20/4 = 10/x ⇒ 20x = 40 ⇒ x = 2 days!"</em></p>
        <p><strong>Why This Fails Mathematically:</strong><br>
        The student blindly used direct variation cross-multiplication. But reducing workers from 20 to 10 cannot cause a road to be built in <em>fewer</em> days!</p>
        <p><strong>The Correct Mathematical Method:</strong><br>
        In inverse proportion, the <strong>product</strong> is invariant, not the quotient:
        </p>
        <div class="math-block">
          Workers × Days = Constant Work Volume (w₁ · d₁ = w₂ · d₂)<br>
          20 × 4 = 10 × x &nbsp;⇒&nbsp; 80 = 10x &nbsp;⇒&nbsp; x = 8 days!
        </div>
      </div>

      <!-- Trap 4 -->
      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-triangle-exclamation"></i> Blunder 4: The Percentage-to-Degrees Confusion in Pie Charts</div>
        <p><strong>The Typical Student Error:</strong><br>
        <em>"If 30% of students scored Grade A, the central angle on the pie chart is 30°."</em></p>
        <p><strong>Why This Fails Mathematically:</strong><br>
        A protractor circle measures <strong>360°</strong>, whereas percentages are measured out of <strong>100%</strong>. Treating 1% as 1° leaves <code>360 - 100 = 260°</code> of empty unused circle!</p>
        <p><strong>The Correct Mathematical Method:</strong><br>
        Always multiply the percentage by <strong>3.6°</strong> (since 360° ÷ 100% = 3.6° per percent):
        </p>
        <div class="math-block">
          Central Angle θ = 30 × 3.6° = 108°!<br>
          (Verification: 108° / 360° = 0.30 = 30%).
        </div>
      </div>

      <!-- Trap 5 -->
      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-triangle-exclamation"></i> Blunder 5: The "Ratios Guarantee Congruence" Fallacy in Geometry</div>
        <p><strong>The Typical Student Error:</strong><br>
        <em>"Since both triangles have sides in the ratio 3 : 4 : 5, they are congruent by SSS!"</em></p>
        <p><strong>Why This Fails Mathematically:</strong><br>
        SSS congruence demands that corresponding sides have <strong>identically equal physical lengths</strong>, not merely equal ratios! A triangle with sides (3 cm, 4 cm, 5 cm) has area 6 cm², while one with sides (6 cm, 8 cm, 10 cm) has area 24 cm².</p>
        <p><strong>The Correct Mathematical Method:</strong><br>
        Equal sidelength ratios prove <strong>SIMILARITY (ସାଦୃଶ୍ୟ)</strong>, meaning they have the identical shape and angles. They are <strong>CONGRUENT (ସର୍ବସମ)</strong> if and only if their side lengths are identically equal (scale factor k = 1).
        </p>
      </div>

      <!-- 15 High-Yield Fast Revision Bullet Points -->
      <div class="concept-card" style="margin-top: 2.5rem;">
        <h3 class="concept-card-title"><i class="fa-solid fa-list-ol"></i> 15 High-Yield Revision Points (Morning-of-Exam Master Checklist)</h3>
        
        <ol style="margin-left: 1.5rem; line-height: 1.85; font-size: 0.95rem;">
          <li><strong>Direct Proportion Core Law:</strong> Two quantities <em>x</em> and <em>y</em> vary directly if their quotient is constant (<code class="math-inline">x / y = k</code>). Multiplying <em>x</em> by factor <em>m</em> multiplies <em>y</em> by the identical factor <em>m</em>.</li>
          <li><strong>Inverse Proportion Core Law:</strong> Two quantities <em>x</em> and <em>y</em> vary inversely if their product is constant (<code class="math-inline">x · y = k</code>). Multiplying <em>x</em> by factor <em>n</em> divides <em>y</em> by <em>n</em> (multiplies by reciprocal <code class="math-inline">1/n</code>).</li>
          <li><strong>Cross-Multiplication Test:</strong> Two ratios <code class="math-inline">a : b</code> and <code class="math-inline">c : d</code> form a direct proportion if and only if <code class="math-inline">a · d = b · c</code> (Product of Extremes = Product of Means).</li>
          <li><strong>Cartographic Representative Fraction:</strong> <code class="math-inline">RF = Distance on Map / Ground Distance</code> is a dimensionless ratio. Both map and ground distances must be in the identical metric unit (usually cm) before simplifying.</li>
          <li><strong>The Metric Lakh Bridge:</strong> Exactly <code class="math-inline">1,00,000 cm = 1 km</code>. On a map with RF 1 : 60,00,000, 1 cm represents <code class="math-inline">60,00,000 ÷ 1,00,000 = 60 km</code> of real ground distance.</li>
          <li><strong>Crow-Flight vs. Road Distance:</strong> Map scale measurements calculate direct geographical straight-line distance. Actual highway travel distance is typically 15% to 35% longer due to topographical curvature.</li>
          <li><strong>Classroom Scale 1 : 50:</strong> Under a 1:50 drafting scale, <code class="math-inline">1 cm on paper = 50 cm in the room = 0.5 m</code>. Conversely, <code class="math-inline">2 cm on paper = 1 metre in the room</code>.</li>
          <li><strong>Multi-Term Ratio Compounding:</strong> When <code class="math-inline">a : b : c : d :: p : q : r : s</code>, all corresponding pairs share the identical scale factor: <code class="math-inline">a/p = b/q = c/r = d/s = k</code>.</li>
          <li><strong>Master Partitioning Formula:</strong> When dividing a whole quantity <em>W</em> in the multi-term ratio <code class="math-inline">a : b : c : ...</code>, each part equals <code class="math-inline">W × [term / (a + b + c + ...)]</code>.</li>
          <li><strong>Triangle Sidelength Feasibility:</strong> By the Triangle Inequality Theorem, no triangle can have sidelengths in ratio 1 : 3 : 5 because <code class="math-inline">1x + 3x = 4x &lt; 5x</code> (the two shorter sides cannot meet).</li>
          <li><strong>Pie Chart Complete Angle:</strong> The complete revolution of a circle subtends exactly <code class="math-inline">360°</code>. The central sector angle for any item is <code class="math-inline">θ = (Frequency / Total N) × 360°</code>.</li>
          <li><strong>Percentage to Degrees Conversion:</strong> To convert a percentage <em>P%</em> into pie chart degrees, multiply by 3.6°: <code class="math-inline">θ = P × 3.6°</code> (e.g., 50% = 180°, 25% = 90°, 10% = 36°).</li>
          <li><strong>Pie Chart HCF Mental Shortcut:</strong> Simplify data frequencies by their Highest Common Factor (HCF) before calculating angles. If sum of simplified terms is <em>S</em>, then <code class="math-inline">1 part = 360° ÷ S</code>.</li>
          <li><strong>Speed-Time Invariant:</strong> When transit distance is fixed, <code class="math-inline">Speed₁ × Time₁ = Speed₂ × Time₂</code>. Doubling cruising speed cuts travel time in half.</li>
          <li><strong>Combined Work Reciprocal Theorem:</strong> Working together, completion times cannot be averaged. Work rates add directly: <code class="math-inline">1 / T_total = 1 / t₁ + 1 / t₂</code>, yielding <code class="math-inline">T_total = (t₁ · t₂) / (t₁ + t₂)</code>.</li>
        </ol>
      </div>
    </section>

  </div> <!-- End .container -->

  <!-- Page Footer -->
  <footer class="page-footer">
    <div class="footer-content">
      <div class="footer-col">
        <h4><i class="fa-solid fa-graduation-cap"></i> Sujit Classes</h4>
        <p>
          Empowering Odisha's middle school scholars (Classes 6 to 10) in CBSE English Medium and BSE Odia Medium with exhaustive, mathematically sound, zero-omission master study materials.
        </p>
      </div>
      <div class="footer-col">
        <h4>Chapter Quick Links</h4>
        <ul class="footer-links">
          <li><a href="#section1">§ 1. Visual Blueprint &amp; Mind Map</a></li>
          <li><a href="#section2">§ 2. Complete Theory &amp; Vocabulary</a></li>
          <li><a href="#section3">§ 3. Rapid Formula &amp; Law Bank</a></li>
          <li><a href="#section4">§ 4. 100% Solved NCERT Questions</a></li>
          <li><a href="#section5">§ 5. Complete Exam Question Bank</a></li>
          <li><a href="#section6">§ 6. Exam Hall Trap Alerts</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Class 8 Mathematics Deck</h4>
        <ul class="footer-links">
          <li><a href="math-ch7-proportional-reasoning-1.html">Chapter 7: Proportional Reasoning - 1</a></li>
          <li><a href="math-ch8-fractions-in-disguise.html">Chapter 8: Fractions in Disguise</a></li>
          <li><a href="math-ch9-the-baudhayana-pythagoras-theorem.html">Chapter 9: The Baudhāyana-Pythagoras Theorem</a></li>
          <li><a href="math-ch10-proportional-reasoning-2.html" style="color: #38bdf8; font-weight: 700;">Chapter 10: Proportional Reasoning - 2</a></li>
          <li><a href="math-ch11-exploring-some-geometric-themes.html">Chapter 11: Exploring Some Geometric Themes</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 Sujit Classes Portal. Designed strictly in alignment with NCERT NEP 2020 Ganita Prakash curriculum. Crafted with dedication for young mathematics scholars.</p>
    </div>
  </footer>

  <!-- ==========================================================
       JAVASCRIPT INTERACTIVITY CONTROLLERS
       ========================================================== -->
  <script>
    /* ----------------------------------------------------------
       1. READING PROGRESS BAR CONTROLLER
       ---------------------------------------------------------- */
    window.addEventListener('scroll', function() {
      const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      const bar = document.getElementById('progressBar');
      if (bar) {
        bar.style.width = scrolled + '%';
      }
    });

    /* ----------------------------------------------------------
       2. INTERACTIVE MCQ QUIZ ENGINE
       ---------------------------------------------------------- */
    let quizScore = 0;
    const answeredQuestions = new Set();

    function evaluateMCQ(qNum, selectedOption, isCorrect, feedbackText) {
      const card = document.getElementById('mcqCard' + qNum);
      const feedback = document.getElementById('feedback' + qNum);
      if (!card || !feedback) return;

      // Prevent re-answering
      if (answeredQuestions.has(qNum)) return;
      answeredQuestions.add(qNum);

      const buttons = card.querySelectorAll('.option-btn');
      buttons.forEach(btn => {
        btn.disabled = true;
        btn.style.cursor = 'default';
        const optBadge = btn.querySelector('.pos-badge');
        if (optBadge) {
          const optLetter = optBadge.innerText.trim();
          if (optLetter === selectedOption) {
            if (isCorrect) {
              btn.classList.add('selected-correct');
              btn.innerHTML += ' <i class="fa-solid fa-circle-check" style="margin-left: auto; color: #059669;"></i>';
            } else {
              btn.classList.add('selected-wrong');
              btn.innerHTML += ' <i class="fa-solid fa-circle-xmark" style="margin-left: auto; color: #dc2626;"></i>';
            }
          }
        }
      });

      // Update feedback box
      feedback.className = 'trap-feedback show ' + (isCorrect ? 'correct-feedback' : 'wrong-feedback');
      feedback.innerHTML = '<strong>' + (isCorrect ? '✓ Correct! ' : '✗ Conceptual Trap! ') + '</strong>' + feedbackText;

      // Update score display
      if (isCorrect) {
        quizScore++;
      }
      const scoreDisplay = document.getElementById('quizScoreDisplay');
      if (scoreDisplay) {
        scoreDisplay.innerHTML = '<i class="fa-solid fa-trophy"></i> Score: ' + quizScore + ' / 5';
      }
    }

    /* ----------------------------------------------------------
       3. TEXT-TO-SPEECH (AUDIO TEACHER READER)
       ---------------------------------------------------------- */
    const synth = window.speechSynthesis;
    let currentUtterance = null;
    let isPlayingAudio = false;
    let speechRate = 1.0;

    const chapterSummarySpeechText = 
      "Welcome to Class 8 Mathematics Chapter 10: Proportional Reasoning - 2, based on the NCERT Ganita Prakash curriculum. " +
      "In this chapter, we extend our mastery of ratios and proportions into multi-variable compounding, spatial cartography, circular statistics, and inverse variation. " +
      "We begin with a review of direct proportionality and the idli batter recipe: when quantities scale by the same factor, their quotient remains constant, and cross-multiplication verifies the equality of ratios. " +
      "In cartography, the Representative Fraction, such as 1 to 60 lakhs, means 1 centimeter on the map equals 60 kilometers of straight-line geographical distance on the ground. We distinguish straight-line crow-flight distance from winding road distance and learn how to draft classroom blueprints at a scale of 1 to 50. " +
      "Next, we explore multi-term ratios with three or more terms, such as Viswanath's spice mix of 8 to 4 to 2 to 1 and structural concrete of 1 cement to 1.5 sand to 3 gravel. " +
      "When dividing a whole quantity into a multi-term ratio, we divide the whole by the sum of parts to find the value of one part, and multiply each term by this factor. " +
      "We discover that while triangles with angles in ratio 1 to 3 to 5 yield 20, 60, and 100 degrees, side lengths in ratio 1 to 3 to 5 can never form a triangle because they violate the Triangle Inequality Theorem. " +
      "In Section 3.5, we construct pie charts. Since a circle has 360 degrees, each category occupies a central angle proportional to its frequency or percentage: central angle equals percentage times 3.6 degrees. " +
      "Finally, we enter the reciprocal world of inverse proportions, where product x times y equals a constant k. In travel, speed times time equals constant distance: doubling speed halves travel time. " +
      "In construction, workers times days equals total worker-days. In collaborative work, completion times cannot be averaged; instead, we add reciprocal work rates. " +
      "Review the solved exercises, practice the exam question bank, avoid common exam traps, and achieve excellence with Sujit Classes!";

    function toggleAudioReader() {
      const btn = document.getElementById('ttsPlayBtn');
      const icon = document.getElementById('ttsIcon');
      const status = document.getElementById('ttsStatus');

      if (!synth) {
        if (status) status.innerText = "Speech synthesis is not supported on this browser.";
        return;
      }

      if (isPlayingAudio) {
        synth.cancel();
        isPlayingAudio = false;
        if (icon) icon.className = "fa-solid fa-play";
        if (status) status.innerText = "Audio paused. Click Play to resume teacher narration.";
      } else {
        synth.cancel();
        currentUtterance = new SpeechSynthesisUtterance(chapterSummarySpeechText);
        currentUtterance.rate = speechRate;
        currentUtterance.pitch = 1.0;
        currentUtterance.lang = 'en-US';

        currentUtterance.onend = function() {
          isPlayingAudio = false;
          if (icon) icon.className = "fa-solid fa-play";
          if (status) status.innerText = "Narration completed. Click Play to listen again.";
        };

        currentUtterance.onerror = function() {
          isPlayingAudio = false;
          if (icon) icon.className = "fa-solid fa-play";
          if (status) status.innerText = "Audio playback interrupted.";
        };

        synth.speak(currentUtterance);
        isPlayingAudio = true;
        if (icon) icon.className = "fa-solid fa-pause";
        if (status) status.innerText = "Playing audio narration... Listen attentively to key concepts.";
      }
    }

    function updateSpeechRate() {
      const select = document.getElementById('ttsRate');
      if (select) {
        speechRate = parseFloat(select.value);
        if (isPlayingAudio) {
          toggleAudioReader();
          toggleAudioReader();
        }
      }
    }
  </script>
</body>
</html>
"""
