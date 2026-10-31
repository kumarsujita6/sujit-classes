# -*- coding: utf-8 -*-
"""
Module: ch8_section6_footer.py
Contains Section 6: Exam Hall Trap Alerts (5 common student blunders),
an intricate SVG visualizer for the Successive Discount Area Dissection,
15 Rapid Revision Points, Master Chapter Summary, Footer, and complete
production JavaScript (Progress bar, Audio TTS reader, Interactive MCQ quiz engine).
"""

def get_section6_and_footer():
    return """
    <!-- ========================================== -->
    <!-- SECTION 6: TRAP ALERTS & REVISION POINTS   -->
    <!-- ========================================== -->
    <section id="section6">
      <div class="section-header">
        <div class="section-tag"><i class="fa-solid fa-triangle-exclamation"></i> Exam Hall Defenses</div>
        <h2 class="section-title">Section 6: Exam Hall Trap Alerts &amp; 15 Rapid Revision Points</h2>
        <p class="section-desc">
          Five notorious psychological traps where students routinely lose marks, paired with immediate tactical corrections, followed by 15 high-speed memory anchors for the night before exams.
        </p>
      </div>

      <!-- PART 6.1: EXAM HALL TRAP ALERTS (5 BLUNDERS) -->
      <h3 class="subheading"><i class="fa-solid fa-shield-halved"></i> Part 6.1: Five Common Exam Hall Blunders &amp; Fixes</h3>

      <!-- BLUNDER 1 -->
      <div class="blunder-card">
        <div class="blunder-header">
          <i class="fa-solid fa-circle-xmark"></i> Blunder 1: Dividing by the New Value Instead of the Original Base
        </div>
        <p style="font-size: 0.95rem; color: #475569; margin-bottom: 0.5rem;">
          When tomato prices rise from ₹30 to ₹42, students often write: <code>(12 / 42) × 100 = 28.57%</code>.
        </p>
        <div class="blunder-body">
          <div class="blunder-bad">
            <span class="blunder-label"><i class="fa-solid fa-thumbs-down"></i> WRONG APPROACH</span>
            Dividing the price change by the new final price (₹42). This measures change against the future, which is mathematically invalid in percentage change.
          </div>
          <div class="blunder-good">
            <span class="blunder-label"><i class="fa-solid fa-thumbs-up"></i> CORRECT METHOD</span>
            Always divide by the <strong>ORIGINAL starting price (₹30)</strong>:<br>
            <code>Percentage Increase = (12 / 30) × 100% = 40%</code>.
          </div>
        </div>
      </div>

      <!-- BLUNDER 2 -->
      <div class="blunder-card">
        <div class="blunder-header">
          <i class="fa-solid fa-circle-xmark"></i> Blunder 2: The Successive Discount Addition Fallacy
        </div>
        <p style="font-size: 0.95rem; color: #475569; margin-bottom: 0.5rem;">
          Assuming that two successive discounts of 30% and 20% add up to a flat 50% discount.
        </p>
        <div class="blunder-body">
          <div class="blunder-bad">
            <span class="blunder-label"><i class="fa-solid fa-thumbs-down"></i> WRONG APPROACH</span>
            Adding percentages directly: <code>30% + 20% = 50%</code>. Successive discounts operate on different baselines and cannot be summed arithmetically!
          </div>
          <div class="blunder-good">
            <span class="blunder-label"><i class="fa-solid fa-thumbs-up"></i> CORRECT METHOD</span>
            Multiply the remaining price fractions:<br>
            <code>Net Multiplier = 0.70 × 0.80 = 0.56</code>.<br>
            Net discount = <code>(1 - 0.56) × 100% = 44%</code> (NOT 50%!).
          </div>
        </div>
      </div>

      <!-- INTRICATE SVG DIAGRAM 4: SUCCESSIVE DISCOUNT AREA DISSECTION -->
      <div class="svg-container">
        <h4 style="margin-bottom: 0.5rem; color: #1e1b4b; font-family: 'Space Grotesk', sans-serif;"><i class="fa-solid fa-chart-pie"></i> SVG Diagram 4: Geometric Dissection of Successive Discount (30% + 20% = 44% Net)</h4>
        <svg viewBox="0 0 880 340" xmlns="http://www.w3.org/2000/svg" style="background: #ffffff; border-radius: 14px;">
          <!-- Frame -->
          <rect x="10" y="10" width="860" height="320" rx="12" fill="#ffffff" stroke="#e2e8f0" stroke-width="2"/>

          <!-- Title -->
          <text x="440" y="38" fill="#1e1b4b" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="15" text-anchor="middle">WHY "30% + 20%" LEAVES 56% OF PRICE (A 44% DISCOUNT, NOT 50%)</text>

          <!-- Total Bar (100% = 700px width from x=90 to x=790) -->
          <!-- Base background: Full Price ₹100 / 100% -->
          <rect x="90" y="70" width="700" height="60" rx="8" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="2"/>
          <text x="440" y="105" fill="#64748b" font-weight="700" font-size="14" text-anchor="middle">ORIGINAL MARKED PRICE (100% / ₹100)</text>

          <!-- Stage 1 Discount: 30% (width = 210px) -->
          <rect x="90" y="160" width="210" height="60" rx="8" fill="#fee2e2" stroke="#ef4444" stroke-width="2"/>
          <text x="195" y="195" fill="#991b1b" font-weight="700" font-size="13" text-anchor="middle">1st Discount: 30%</text>

          <!-- Stage 2 Remaining: 70% (width = 490px) -->
          <rect x="300" y="160" width="490" height="60" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
          <text x="545" y="195" fill="#1e40af" font-weight="700" font-size="13" text-anchor="middle">Price after 1st Discount: 70% (₹70)</text>

          <!-- Stage 3 Breakdown: 20% of Remaining 70% (width = 0.20 * 490 = 98px) -->
          <rect x="300" y="240" width="98" height="60" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
          <text x="349" y="270" fill="#92400e" font-weight="700" font-size="11" text-anchor="middle">2nd Discount</text>
          <text x="349" y="288" fill="#b45309" font-weight="800" font-size="12" text-anchor="middle">14% (₹14)</text>

          <!-- Final Amount Paid: 56% (width = 0.80 * 490 = 392px) -->
          <rect x="398" y="240" width="392" height="60" rx="8" fill="#d1fae5" stroke="#10b981" stroke-width="2"/>
          <text x="594" y="268" fill="#064e3b" font-weight="800" font-size="14" text-anchor="middle">CUSTOMER ACTUALLY PAYS: 56% (₹56)</text>
          <text x="594" y="288" fill="#047857" font-weight="600" font-size="11" text-anchor="middle">Total Discount = 30% + 14% = 44%</text>

          <!-- Phantom 6% Gap (What students wrongly think they get!) -->
          <line x1="90" y1="315" x2="440" y2="315" stroke="#dc2626" stroke-width="2" stroke-dasharray="4,4"/>
          <text x="265" y="332" fill="#dc2626" font-size="11" font-weight="700" text-anchor="middle">Flat 50% mark would be here (Leaves ₹50, not ₹56!)</text>
        </svg>
        <p class="svg-caption">Figure 6.1: Visual Breakdown of the 30% + 20% Successive Discount — The second 20% discount applies only to the remaining 70%, yielding just 14% off the original price, resulting in a 44% total discount.</p>
      </div>

      <!-- BLUNDER 3 -->
      <div class="blunder-card">
        <div class="blunder-header">
          <i class="fa-solid fa-circle-xmark"></i> Blunder 3: The Surbhi Reversal Delusion (Equal Markup and Discount)
        </div>
        <p style="font-size: 0.95rem; color: #475569; margin-bottom: 0.5rem;">
          Believing that marking up by <em>X%</em> and then discounting by <em>X%</em> brings you back to the exact starting cost price.
        </p>
        <div class="blunder-body">
          <div class="blunder-bad">
            <span class="blunder-label"><i class="fa-solid fa-thumbs-down"></i> WRONG APPROACH</span>
            Thinking <code>Cost + 50% - 50% = Cost</code>. This ignores the fact that 50% of the larger marked-up amount is much greater than 50% of the original cost!
          </div>
          <div class="blunder-good">
            <span class="blunder-label"><i class="fa-solid fa-thumbs-up"></i> CORRECT METHOD</span>
            A 50% markup gives <em>1.50x</em>. A 50% discount gives <em>1.50x × 0.50 = 0.75x</em>, creating a <strong>25% net loss</strong>!<br>
            To break even, the discount needed is: <code>0.5x / 1.5x = 33.33%</code>.
          </div>
        </div>
      </div>

      <!-- BLUNDER 4 -->
      <div class="blunder-card">
        <div class="blunder-header">
          <i class="fa-solid fa-circle-xmark"></i> Blunder 4: Calculating Profit or Loss on Selling Price Instead of Cost Price
        </div>
        <p style="font-size: 0.95rem; color: #475569; margin-bottom: 0.5rem;">
          When an article bought for ₹300 is sold for ₹400 (Profit = ₹100), writing Profit% = (100 / 400) × 100 = 25%.
        </p>
        <div class="blunder-body">
          <div class="blunder-bad">
            <span class="blunder-label"><i class="fa-solid fa-thumbs-down"></i> WRONG APPROACH</span>
            Dividing profit by the Selling Price (₹400). This calculates the retailer's <em>margin on sales</em>, NOT the mathematical profit percentage prescribed in CBSE/NCERT syllabus!
          </div>
          <div class="blunder-good">
            <span class="blunder-label"><i class="fa-solid fa-thumbs-up"></i> CORRECT METHOD</span>
            Always divide by <strong>Cost Price (₹300)</strong>:<br>
            <code>Profit% = (100 / 300) × 100% = 33.33%</code>.
          </div>
        </div>
      </div>

      <!-- BLUNDER 5 -->
      <div class="blunder-card">
        <div class="blunder-header">
          <i class="fa-solid fa-circle-xmark"></i> Blunder 5: Adding Non-Homogeneous Percentage Literacy Rates Across Genders
        </div>
        <p style="font-size: 0.95rem; color: #475569; margin-bottom: 0.5rem;">
          In the NSS Survey graph (NCERT Page 30), adding Male literacy (37%) and Female literacy (26%) to claim that 63% of young people use computers.
        </p>
        <div class="blunder-body">
          <div class="blunder-bad">
            <span class="blunder-label"><i class="fa-solid fa-thumbs-down"></i> WRONG APPROACH</span>
            Adding percentage rates from two distinct subgroups: <code>37% + 26% = 63%</code>. Percentages are rates, not raw counts!
          </div>
          <div class="blunder-good">
            <span class="blunder-label"><i class="fa-solid fa-thumbs-up"></i> CORRECT METHOD</span>
            Take the weighted average across both populations:<br>
            <code>Overall Rate ≈ (37% + 26%) / 2 = 31.5%</code> (assuming roughly equal gender numbers).
          </div>
        </div>
      </div>

      <!-- PART 6.2: 15 RAPID REVISION POINTS -->
      <h3 class="subheading"><i class="fa-solid fa-bookmark"></i> Part 6.2: 15 Rapid Revision Memory Anchors</h3>
      <div class="points-grid">
        <div class="point-card">
          <div class="point-num">1</div>
          <p><strong>"Per Centum" Literal Meaning:</strong> Percent literally means <em>parts out of 100</em>. The sign ‘%’ represents a fraction with denominator 100: <code>p% = p / 100</code>.</p>
        </div>
        <div class="point-card">
          <div class="point-num">2</div>
          <p><strong>Three Conversion Routes:</strong> Convert fraction to percent by (a) finding equivalent denominator 100, (b) unitary scaling, or (c) multiplying by 100%.</p>
        </div>
        <div class="point-card">
          <div class="point-num">3</div>
          <p><strong>Decimals to Percentages:</strong> Shift the decimal point exactly <strong>two places to the right</strong>: <code>0.375 = 37.5%</code>. For percent to decimal, shift two places left.</p>
        </div>
        <div class="point-card">
          <div class="point-num">4</div>
          <p><strong>Commutative Magic:</strong> <code>x% of y = y% of x</code>. Always flip cumbersome percentage calculations to their easy counterparts (e.g., <code>14% of 50 = 50% of 14 = 7</code>!).</p>
        </div>
        <div class="point-card">
          <div class="point-num">5</div>
          <p><strong>The Mental Anchors:</strong> 10% = divide by 10; 1% = divide by 100; 5% = half of 10%; 20% = double of 10%; 25% = divide by 4; 15% = 10% + 5%.</p>
        </div>
        <div class="point-card">
          <div class="point-num">6</div>
          <p><strong>Multipliers &gt; 1.0:</strong> Percentages above 100% indicate expansion: 120% = 1.20×; 150% = 1.50×; 200% = double (2.0×); 250% = 2.50×.</p>
        </div>
        <div class="point-card">
          <div class="point-num">7</div>
          <p><strong>Percentage Change Base:</strong> Always divide absolute change by the <strong>original starting quantity</strong>: <code>(Change / Original) × 100%</code>.</p>
        </div>
        <div class="point-card">
          <div class="point-num">8</div>
          <p><strong>Effective Cost Price:</strong> Overhead expenses (transportation, labor, packaging, repairs) must ALWAYS be added to the purchase price before computing profit or loss.</p>
        </div>
        <div class="point-card">
          <div class="point-num">9</div>
          <p><strong>Profit/Loss Baseline:</strong> Profit and Loss percentages are <strong>strictly calculated on Cost Price (CP)</strong>: <code>Profit% = (Profit / CP) × 100%</code>.</p>
        </div>
        <div class="point-card">
          <div class="point-num">10</div>
          <p><strong>Discount Baseline:</strong> Trade discount is <strong>strictly calculated on Marked Price (MP)</strong>: <code>Discount% = (Discount / MP) × 100%</code>; <code>SP = MP × (1 - d/100)</code>.</p>
        </div>
        <div class="point-card">
          <div class="point-num">11</div>
          <p><strong>GST Billing:</strong> Goods and Services Tax is added to the <strong>net selling price</strong> after all discounts are subtracted: <code>Bill = SP × (1 + GST/100)</code>.</p>
        </div>
        <div class="point-card">
          <div class="point-num">12</div>
          <p><strong>Successive Discount Rule:</strong> Two discounts <em>d_1%</em> and <em>d_2%</em> give net discount: <code>[1 - (1 - d₁/100)(1 - d₂/100)] × 100%</code>. They NEVER add directly.</p>
        </div>
        <div class="point-card">
          <div class="point-num">13</div>
          <p><strong>Simple Interest (SI):</strong> Linear growth where principal remains constant: <code>SI = (P × R × T) / 100</code>; <code>Amount = P + SI</code>.</p>
        </div>
        <div class="point-card">
          <div class="point-num">14</div>
          <p><strong>Compound Interest (CI):</strong> Geometric growth where each year's interest is added to the principal: <code>A = P × (1 + R/100)ᵗ</code>. Compounding always surpasses SI over time.</p>
        </div>
        <div class="point-card">
          <div class="point-num">15</div>
          <p><strong>Depreciation Law:</strong> Physical assets (cars, electronics) lose value via exponential decay: <code>A = P × (1 - R/100)ⁿ</code>. Multiplier is strictly less than 1.0.</p>
        </div>
      </div>

      <!-- MASTER CHAPTER SUMMARY -->
      <div style="background: linear-gradient(135deg, #1e1b4b 0%, #312e81 100%); color: #ffffff; padding: 2rem; border-radius: var(--radius-lg); margin-top: 2rem; box-shadow: var(--shadow-lg);">
        <h4 style="color: #fbbf24; font-family: 'Space Grotesk', sans-serif; font-size: 1.25rem; margin-bottom: 0.75rem;"><i class="fa-solid fa-graduation-cap"></i> Teacher Master Summary</h4>
        <p style="color: #e0e7ff; line-height: 1.8; margin-bottom: 0.75rem;">
          In Class 8 Chapter 8, we discovered that percentages are not a foreign mathematical species—they are simply fractions wearing a universal disguise with denominator 100. By mastering the FDP conversion trinity, students unlock lightning-fast mental arithmetic through decimal shifting and commutative flips (<em>x%  of  y = y%  of  x</em>).
        </p>
        <p style="color: #cbd5e1; line-height: 1.8; margin-bottom: 0;">
          In the commercial domain, we established that Cost Price governs profit/loss, Marked Price governs discounts, and Selling Price anchors GST. Finally, by comparing Simple and Compound Interest, we witnessed the power of exponential growth, where "interest on interest" compounds wealth, while depreciation models asset decay. Keep your mathematical base clear, beware of successive discount traps, and let fractions work for you!
        </p>
      </div>
    </section>
  </div> <!-- END .container -->

  <!-- ========================================== -->
  <!-- FOOTER                                     -->
  <!-- ========================================== -->
  <footer>
    <div class="footer-container">
      <div class="footer-brand">
        <i class="fa-solid fa-graduation-cap"></i>
        <span>Sujit Classes • Digital Learning Portal</span>
      </div>
      <div class="footer-links">
        <a href="../../index.html"><i class="fa-solid fa-house"></i> Home</a>
        <a href="#section1"><i class="fa-solid fa-arrow-up"></i> Top</a>
        <a href="mailto:support@sujitclasses.edu"><i class="fa-solid fa-envelope"></i> Contact</a>
      </div>
      <div class="footer-copy">
        &copy; 2026 Sujit Classes. Curricular content aligned with NCERT NEP 2020 Ganita Prakash (Grade 8 Mathematics). Designed for CBSE and BSE Odisha middle school students.
      </div>
    </div>
  </footer>

  <!-- ========================================== -->
  <!-- COMPLETE INTERACTIVE JAVASCRIPT ENGINE     -->
  <!-- ========================================== -->
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
        const optLetter = btn.querySelector('.pos-badge').innerText.trim();
        if (optLetter === selectedOption) {
          if (isCorrect) {
            btn.classList.add('selected-correct');
            btn.innerHTML += ' <i class="fa-solid fa-circle-check" style="margin-left: auto; color: #059669;"></i>';
          } else {
            btn.classList.add('selected-wrong');
            btn.innerHTML += ' <i class="fa-solid fa-circle-xmark" style="margin-left: auto; color: #dc2626;"></i>';
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
        scoreDisplay.innerText = 'Score: ' + quizScore + ' / 5';
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
      "Welcome to Class 8 Mathematics Chapter 8: Fractions in Disguise. " +
      "In this chapter, we discover that percentages are simply fractions whose denominator is fixed at 100. " +
      "The Latin root per centum literally means out of one hundred. " +
      "By standardizing all fractions to denominator 100, we can instantly compare unequal quantities like biscuit sugar contents. " +
      "To convert any fraction to a percentage, multiply by 100 percent. " +
      "To convert a percentage to a fraction, divide by 100 and reduce to simplest terms. " +
      "One of the most powerful mental calculation tools is the commutative law: x percent of y equals y percent of x. " +
      "For example, 16 percent of 50 equals 50 percent of 16, which is simply 8. " +
      "In commercial arithmetic, profit and loss percentages are strictly calculated on the Cost Price. " +
      "Trade discounts are strictly calculated on the Marked Price. " +
      "Goods and Services Tax is added to the actual net selling price. " +
      "Beware of deceptive successive discounts: a 30 percent plus 20 percent discount is not 50 percent; it equals a 44 percent net discount. " +
      "Finally, in financial capital growth, Simple Interest grows linearly because the principal stays fixed, " +
      "while Compound Interest grows exponentially because earned interest is reinvested each year to earn interest on interest. " +
      "Depreciation models the loss in asset value over time using a decay multiplier less than one. " +
      "Keep practicing, explore the solved exercises, and conquer your exams with Sujit Classes!";

    function toggleAudioReader() {
      const btn = document.getElementById('ttsPlayBtn');
      const icon = document.getElementById('ttsIcon');
      const status = document.getElementById('ttsStatus');

      if (!synth) {
        status.innerText = "Speech synthesis is not supported on this browser.";
        return;
      }

      if (isPlayingAudio) {
        synth.cancel();
        isPlayingAudio = false;
        icon.className = "fa-solid fa-play";
        status.innerText = "Audio paused. Click Play to resume teacher narration.";
      } else {
        synth.cancel(); // clear previous speech queue
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
