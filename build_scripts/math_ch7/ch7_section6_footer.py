# -*- coding: utf-8 -*-
"""
Module: ch7_section6_footer.py
Contains Section 6: Exam Hall Trap Alerts (5 common student blunders with side-by-side bad vs topper way),
15 Rapid Revision Points, footer, and complete interactive JavaScript engine (reading progress, TTS audio reader, MCQ engine).
"""

def get_section6_and_footer():
    return """
    <!-- ========================================== -->
    <!-- SECTION 6: COMMON TRAPS & RAPID REVISION  -->
    <!-- ========================================== -->
    <section id="section6">
      <div class="section-header">
        <div class="section-tag"><i class="fa-solid fa-triangle-exclamation"></i> Exam Hall Survival Shield</div>
        <h2 class="section-title">Section 6: Exam Hall Trap Alerts &amp; 15 Revision Points</h2>
        <p class="section-desc">
          Avoid the five most devastating mathematical pitfalls that cost students marks in CBSE/BSE examinations, followed by 15 high-impact memory anchors for last-minute revision.
        </p>
      </div>

      <!-- 5 COMMON TRAPS -->
      <h3 class="subheading"><i class="fa-solid fa-skull-crossbones"></i> The 5 Most Fatal Student Blunders</h3>

      <!-- Blunder 1 -->
      <div class="blunder-card">
        <div class="blunder-header">
          <i class="fa-solid fa-circle-xmark"></i> Trap 1: Forming Ratios with Inconsistent Measurement Units
        </div>
        <div class="blunder-body">
          <div class="blunder-bad">
            <div class="blunder-label"><i class="fa-solid fa-thumbs-down"></i> The Flawed Student Way</div>
            <p>Writing the ratio of 200 grams of tea to 1 kg of tea as: <em>200 : 1</em>.</p>
            <p style="font-size: 0.85rem; color: #991b1b;">
              <strong>Why it fails:</strong> The student compared grams directly with kilograms, resulting in an error by a factor of 1,000!
            </p>
          </div>
          <div class="blunder-good">
            <div class="blunder-label"><i class="fa-solid fa-thumbs-up"></i> The 100% CBSE Topper Way</div>
            <p>Always convert both quantities to the <strong>same unit first</strong>:
              <br>1 kg = 1,000 g ⇒ Ratio = <em>200 g : 1000 g = <strong>1 : 5</strong></em>.
            </p>
            <p style="font-size: 0.85rem; color: #166534;">
              <strong>Rule:</strong> A ratio must be dimensionless. Units MUST match and cancel out completely.
            </p>
          </div>
        </div>
      </div>

      <!-- Blunder 2 -->
      <div class="blunder-card">
        <div class="blunder-header">
          <i class="fa-solid fa-circle-xmark"></i> Trap 2: Believing Adding a Constant Preserves Proportionality
        </div>
        <div class="blunder-body">
          <div class="blunder-bad">
            <div class="blunder-label"><i class="fa-solid fa-thumbs-down"></i> The Flawed Student Way</div>
            <p>Assuming that if father and son's ages are in ratio 4 : 1, their age ratio after 10 years will still be <em>4 : 1</em> or <em>(4+10) : (1+10) = 14 : 11</em>.</p>
            <p style="font-size: 0.85rem; color: #991b1b;">
              <strong>Why it fails:</strong> The student assumed adding 10 years preserves the ratio or simply added 10 to the ratio terms.
            </p>
          </div>
          <div class="blunder-good">
            <div class="blunder-label"><i class="fa-solid fa-thumbs-up"></i> The 100% CBSE Topper Way</div>
            <p>Set up an algebraic variable: let initial ages be <em>4k</em> and <em>1k</em>.
              <br>After 10 years, ages are <em>(4k + 10)</em> and <em>(k + 10)</em>.
              <br>New Ratio = <em><strong>(4k + 10) / (k + 10)</strong></em>, which strictly decreases towards 1.
            </p>
            <p style="font-size: 0.85rem; color: #166534;">
              <strong>Rule:</strong> Proportionality is preserved ONLY by multiplication or division by a non-zero factor, NEVER by addition or subtraction.
            </p>
          </div>
        </div>
      </div>

      <!-- Blunder 3 -->
      <div class="blunder-card">
        <div class="blunder-header">
          <i class="fa-solid fa-circle-xmark"></i> Trap 3: Applying Direct Proportion to Inverse Variation (Speed vs Time)
        </div>
        <div class="blunder-body">
          <div class="blunder-bad">
            <div class="blunder-label"><i class="fa-solid fa-thumbs-down"></i> The Flawed Student Way</div>
            <p>If speed increases from 50 km/h (taking 2 hours) to 75 km/h, writing:
              <br><em>50 : 2 :: 75 : x ⇒ x = (2 × 75) / 50 = 3 hours</em>.
            </p>
            <p style="font-size: 0.85rem; color: #991b1b;">
              <strong>Why it fails:</strong> The student concluded that driving faster takes MORE time!
            </p>
          </div>
          <div class="blunder-good">
            <div class="blunder-label"><i class="fa-solid fa-thumbs-up"></i> The 100% CBSE Topper Way</div>
            <p>Recognize that speed and time are inversely proportional:
              <br><em>Speed₁ × Time₁ = Speed₂ × Time₂ = Distance</em>
              <br><em>50 × 2 = 75 × t ⇒ t = 100 / 75 = <strong>4/3 hours (1 h 20 min)</strong></em>.
            </p>
            <p style="font-size: 0.85rem; color: #166534;">
              <strong>Rule:</strong> When an increase in one variable decreases the other, use <em>x₁y₁ = x₂y₂</em>, NOT the direct Rule of Three.
            </p>
          </div>
        </div>
      </div>

      <!-- Blunder 4 -->
      <div class="blunder-card">
        <div class="blunder-header">
          <i class="fa-solid fa-circle-xmark"></i> Trap 4: Dividing by the Ratio Term Instead of Total Parts (m + n)
        </div>
        <div class="blunder-body">
          <div class="blunder-bad">
            <div class="blunder-label"><i class="fa-solid fa-thumbs-down"></i> The Flawed Student Way</div>
            <p>To divide ₹4,500 in ratio 2 : 3, dividing 4,500 by 2 or by 3 directly.</p>
            <p style="font-size: 0.85rem; color: #991b1b;">
              <strong>Why it fails:</strong> The student confused an individual share with the total number of parts in the whole.
            </p>
          </div>
          <div class="blunder-good">
            <div class="blunder-label"><i class="fa-solid fa-thumbs-up"></i> The 100% CBSE Topper Way</div>
            <p>First find the total number of units: <em>Total Parts = 2 + 3 = 5</em>.
              <br>Value of 1 part = <em>₹4,500 ÷ 5 = ₹900</em>.
              <br>Shares = <em>2 × 900 = <strong>₹1,800</strong></em> and <em>3 × 900 = <strong>₹2,700</strong></em>.
            </p>
            <p style="font-size: 0.85rem; color: #166534;">
              <strong>Rule:</strong> The whole corresponds to the sum of parts: <em>Whole = (m + n) units</em>.
            </p>
          </div>
        </div>
      </div>

      <!-- Blunder 5 -->
      <div class="blunder-card">
        <div class="blunder-header">
          <i class="fa-solid fa-circle-xmark"></i> Trap 5: Inverting Āryabhaṭa's Trairāśika Division Order
        </div>
        <div class="blunder-body">
          <div class="blunder-bad">
            <div class="blunder-label"><i class="fa-solid fa-thumbs-down"></i> The Flawed Student Way</div>
            <p>Writing: <em>Ichchhāphala = (Pramāṇa × Phala) ÷ Ichchhā</em> or <em>(Pramāṇa × Ichchhā) ÷ Phala</em>.</p>
            <p style="font-size: 0.85rem; color: #991b1b;">
              <strong>Why it fails:</strong> Swapping numerator and denominator scrambles the cross-multiplication equation.
            </p>
          </div>
          <div class="blunder-good">
            <div class="blunder-label"><i class="fa-solid fa-thumbs-up"></i> The 100% CBSE Topper Way</div>
            <p>Always align the proportion cleanly:
              <br><em>Pramāṇa (a) : Phala (b) :: Ichchhā (c) : Ichchhāphala (d)</em>
              <br>Extremes product = Means product ⇒ <em>a × d = b × c</em>
              <br><strong style="color: #4f46e5;">d = (b × c) ÷ a</strong>.
            </p>
            <p style="font-size: 0.85rem; color: #166534;">
              <strong>Rule:</strong> Multiply the "Fruit" by the "Desire" and divide by the "Measure"!
            </p>
          </div>
        </div>
      </div>

      <!-- 15 RAPID REVISION POINTS -->
      <h3 class="subheading"><i class="fa-solid fa-bolt"></i> 15 Rapid Revision Anchors (Teacher High-Yield Summary)</h3>
      <ol style="line-height: 1.85; font-size: 1rem; color: #334155;">
        <li><strong>Definition of Ratio:</strong> A ratio <em>a : b</em> compares two quantities of the same physical dimension by division. It is a pure, dimensionless number without any units.</li>
        <li><strong>Antecedent &amp; Consequent:</strong> In <em>a : b</em>, <em>a</em> is the antecedent (first term) and <em>b</em> is the consequent (second term). The order cannot be switched without altering the meaning.</li>
        <li><strong>Simplest Form:</strong> A ratio is in its simplest (irreducible) form when the HCF of both terms is 1, meaning the terms are co-prime integers.</li>
        <li><strong>Proportion:</strong> When two ratios represent the exact same quotient (<em>a : b = c : d</em>), they are in proportion, symbolized by <strong>a : b :: c : d</strong>.</li>
        <li><strong>Fundamental Law of Proportion:</strong> In any proportion <em>a : b :: c : d</em>, the product of the extremes equals the product of the means: <strong>a × d = b × c</strong>.</li>
        <li><strong>Cross-Multiplication Formula:</strong> Any unknown fourth term is computed as <strong>d = (b × c) ÷ a</strong>.</li>
        <li><strong>Ancient Trairāśika:</strong> Established by Āryabhaṭa I (499 CE) and Bhāskara II, Trairāśika calculates <em>Ichchhāphala = (Phala × Ichchhā) ÷ Pramāṇa</em>.</li>
        <li><strong>Addition Invariant Trap:</strong> Adding or subtracting a positive constant to both terms changes the ratio. Proportionality is preserved ONLY by non-zero multiplication or division.</li>
        <li><strong>Partitioning Whole x in Ratio m : n:</strong> Total parts = <em>(m + n)</em>. Unit part size = <em>x / (m + n)</em>. First share = <em>m × [x / (m+n)]</em>, Second share = <em>n × [x / (m+n)]</em>.</li>
        <li><strong>Partnership Profit Rule:</strong> Business partners distribute net profits in direct proportion to their initial capital investments (<em>Profit₁ : Profit₂ = Investment₁ : Investment₂</em>).</li>
        <li><strong>Aspect Ratio &amp; Visual Similarity:</strong> Two rectangles or digital images are geometrically similar if and only if their aspect ratio (<em>Width ÷ Height</em>) remains identical.</li>
        <li><strong>Dimensional Scaling Laws:</strong> Scaling linear lengths by factor <em>k</em> scales perimeter by <em>k</em>, surface area by <strong>k²</strong>, and volume capacity by <strong>k³</strong>.</li>
        <li><strong>Critical Unit Anchors:</strong> Always memorize: <strong>1 acre = 43,560 sq ft</strong>; <strong>1 hectare = 10,000 m² = 2.471 acres</strong>; <strong>1 L = 1,000 mL = 1,000 cc</strong>; <strong>1 m = 3.281 ft</strong>.</li>
        <li><strong>Temperature Conversion:</strong> Formulas are <strong>°F = (9/5)°C + 32</strong> and <strong>°C = (5/9)(°F - 32)</strong>. Both thermometers read the exact same value at <strong>-40°</strong>.</li>
        <li><strong>Direct vs Inverse Distinction:</strong> In direct proportion, the <em>ratio y/x</em> is constant (straight line through origin). In inverse variation (e.g., speed vs time), the <em>product x·y</em> is constant (hyperbolic curve).</li>
      </ol>
    </section>

    <!-- FOOTER -->
    <footer>
      <div class="footer-brand">
        <i class="fa-solid fa-graduation-cap"></i>
        <span>Sujit Classes • Excellence in Middle School Mathematics</span>
      </div>
      <p style="font-size: 0.9rem; color: #94a3b8; max-width: 800px; margin: 0 auto;">
        NCERT Class 8 Mathematics Chapter 7: "Proportional Reasoning - 1" (NEP Code: hegp107). Complete master teacher study notes, zero-omission solutions, and board examination bank designed for CBSE English Medium and BSE Odisha students.
      </p>
      <div class="footer-links">
        <a href="../../index.html"><i class="fa-solid fa-house"></i> Home Portal</a>
        <a href="#section1"><i class="fa-solid fa-sitemap"></i> Mind Map</a>
        <a href="#section2"><i class="fa-solid fa-book-open"></i> Conceptual Blueprint</a>
        <a href="#section3"><i class="fa-solid fa-table-list"></i> Formula Vault</a>
        <a href="#section4"><i class="fa-solid fa-pen-ruler"></i> NCERT Solved</a>
        <a href="#section5"><i class="fa-solid fa-award"></i> Exam Bank</a>
        <a href="#section6"><i class="fa-solid fa-triangle-exclamation"></i> Common Traps</a>
      </div>
      <p style="font-size: 0.8rem; color: #64748b; margin-top: 1.5rem; border-top: 1px solid rgba(255, 255, 255, 0.08); padding-top: 1rem;">
        © 2026 Sujit Classes. All pedagogical models, SVG illustrations, and bilingual glossaries are strictly aligned with the NEP 2020 Ganita Prakash curriculum.
      </p>
    </footer>
  </div>

  <!-- COMPLETE INTERACTIVE JAVASCRIPT ENGINE -->
  <script>
    // 1. TOP FIXED READING PROGRESS BAR
    window.addEventListener('scroll', function() {
      const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      document.getElementById('progressBar').style.width = scrolled + '%';
    });

    // 2. INTERACTIVE MCQ MASTERY ENGINE
    let currentQuizScore = 0;
    const answeredMCQs = {};

    function checkMCQ(questionNum, selectedOption, isCorrect) {
      if (answeredMCQs[questionNum]) return; // prevent re-answering
      answeredMCQs[questionNum] = true;

      const card = document.getElementById('mcqCard' + questionNum);
      const buttons = card.querySelectorAll('.option-btn');
      const feedback = document.getElementById('mcqFeedback' + questionNum);

      buttons.forEach(btn => {
        btn.disabled = true;
        const optionSpan = btn.querySelector('span').innerText.trim();
        if (optionSpan === selectedOption) {
          btn.classList.add(isCorrect ? 'correct' : 'wrong');
        }
      });

      if (isCorrect) {
        currentQuizScore++;
        feedback.classList.add('show', 'correct-feedback');
      } else {
        feedback.classList.add('show', 'wrong-feedback');
      }

      // Update score display
      document.getElementById('quizScoreDisplay').innerText = 'Score: ' + currentQuizScore + ' / 5';
    }

    // 3. INTERACTIVE WEB SPEECH API AUDIO READER
    let synth = window.speechSynthesis;
    let isPlayingAudio = false;
    let currentUtterance = null;
    let speechRate = 1.0;

    const chapterSummarySpeechText = 
      "Welcome to Sujit Classes Master Study Notes for Class 8 Mathematics, Chapter 7: Proportional Reasoning - 1. " +
      "Proportional reasoning is the foundation of advanced mathematics, physics, engineering, and everyday decision making. " +
      "First, a ratio a is to b compares two quantities of the same kind by division. It is a pure dimensionless number without units. " +
      "Second, two ratios are in proportion if their simplest forms are equal. The fundamental law of proportion states that the product of the extremes equals the product of the means, meaning a times d equals b times c. " +
      "Third, in ancient India, Aryabhata and Bhaskara the second developed the Rule of Three, known as Trairasika. It links three known quantities: Pramana the measure, Phala the fruit, and Ichchha the requisition, to calculate Ichchhaphala the yield, as Phala times Ichchha divided by Pramana. " +
      "Fourth, when dividing a whole quantity x into parts in the ratio m is to n, we divide x by m plus n to find the size of one unit group, then multiply by m and n. " +
      "Fifth, remember the critical unit conversion factors: one acre equals 43,560 square feet, one hectare equals 10,000 square metres or 2.471 acres, and one litre equals 1,000 millilitres. " +
      "Finally, beware the common traps! Adding a constant to both terms of a ratio changes the ratio, and direct proportion does not apply to inverse variations like speed and travel time. " +
      "Happy learning with Sujit Classes!";

    function toggleAudioReader() {
      if (!synth) {
        alert("Sorry, your browser does not support the Web Speech synthesis API.");
        return;
      }

      const btn = document.getElementById('ttsPlayBtn');
      const icon = document.getElementById('ttsIcon');
      const status = document.getElementById('ttsStatus');

      if (isPlayingAudio) {
        synth.cancel();
        isPlayingAudio = false;
        icon.className = "fa-solid fa-play";
        status.innerText = "Audio paused. Click Play to resume teacher narration.";
      } else {
        synth.cancel(); // clear queue
        currentUtterance = new SpeechSynthesisUtterance(chapterSummarySpeechText);
        currentUtterance.rate = speechRate;
        currentUtterance.pitch = 1.0;
        currentUtterance.lang = 'en-US';

        currentUtterance.onend = function() {
          isPlayingAudio = false;
          icon.className = "fa-solid fa-play";
          status.innerText = "Narration completed. Click Play to listen again.";
        };

        currentUtterance.onerror = function() {
          isPlayingAudio = false;
          icon.className = "fa-solid fa-play";
          status.innerText = "Audio playback interrupted.";
        };

        synth.speak(currentUtterance);
        isPlayingAudio = true;
        icon.className = "fa-solid fa-pause";
        status.innerText = "Playing audio narration... Listen attentively to key concepts.";
      }
    }

    function updateSpeechRate() {
      const select = document.getElementById('ttsRate');
      speechRate = parseFloat(select.value);
      if (isPlayingAudio) {
        toggleAudioReader();
        toggleAudioReader();
      }
    }
  </script>
</body>
</html>
"""
