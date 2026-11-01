# -*- coding: utf-8 -*-
"""
Module: ch2_section6_footer.py
Contains Section 6: Exam Hall Trap Alerts (5 common student blunders with Wrong Way / Correct Way)
& 15 Comprehensive Rapid Revision Points,
followed by the Portal Footer, Back to Top button, and complete JavaScript scripts
(Reading Progress Bar, Interactive Quiz Engine, Audio Reader with SpeechSynthesis).
"""

def get_section_6_and_footer():
    return """
    <!-- ============================================================ -->
    <!-- SECTION 6: EXAM HALL TRAP ALERTS & 15 REVISION POINTS -->
    <!-- ============================================================ -->
    <section id="section-6" class="study-section">
      <div class="section-header">
        <span class="section-badge"><i class="fa-solid fa-triangle-exclamation"></i> Error Prevention Protocol</span>
        <h2 class="section-title">Exam Hall Trap Alerts & 15 Rapid Revision Points</h2>
        <p class="section-subtitle">
          Over 65% of marks lost in exponents result from standard conceptual traps rather than difficult calculations. Study these 5 common exam hall blunders and lock in your 15 core revision takeaways.
        </p>
      </div>

      <!-- ======================================================== -->
      <!-- 5 COMMON STUDENT BLUNDERS (EXAM HALL TRAPS) -->
      <!-- ======================================================== -->
      <h3 class="topic-title"><i class="fa-solid fa-ban"></i> The 5 Most Fatal Student Blunders in Exponents</h3>

      <!-- Trap 1 -->
      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-bug"></i> Trap Alert 1: Multiplying the Base by the Exponent</div>
        <p><strong>The Blunder:</strong> Thinking that <span class="math-font">2⁵ = 2 × 5 = 10</span>, or <span class="math-font">3³ = 3 × 3 = 9</span>.</p>
        <p><strong>Why This Mistake Happens:</strong> Students confuse repeated multiplication with normal multiplication when writing in a hurry.</p>
        <p><strong>The Correct Way:</strong> An exponent is a <em>repetition counter</em>!
          <br><span class="math-font">2⁵ = 2 × 2 × 2 × 2 × 2 = 32</span> (NOT 10!).
          <br><span class="math-font">3³ = 3 × 3 × 3 = 27</span> (NOT 9!).
        </p>
        <p><strong>Examiner Tip:</strong> Say out loud in your mind: <em>"Two multiplied by itself five times."</em></p>
      </div>

      <!-- Trap 2 -->
      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-bug"></i> Trap Alert 2: Dropping Parentheses on Negative Bases (–3² vs (–3)²)</div>
        <p><strong>The Blunder:</strong> Treating <span class="math-font">–3²</span> and <span class="math-font">(–3)²</span> as identical.</p>
        <p><strong>Why This Mistake Happens:</strong> In informal handwriting, students omit brackets, assuming the negative sign is automatically squared.</p>
        <p><strong>The Correct Way:</strong>
          <br>• <span class="math-font">(–3)² = (–3) × (–3) = +9</span> (The bracket ensures the negative sign is part of the repeating base).
          <br>• <span class="math-font">–3² = –(3 × 3) = –9</span> (By BODMAS, exponentiation happens before negation!).
        </p>
        <p><strong>Examiner Tip:</strong> When substituting a negative number for a variable (e.g., <span class="math-font">x²</span> when <span class="math-font">x = –4</span>), ALWAYS wrap it in brackets: <span class="math-font">(–4)² = 16</span>.</p>
      </div>

      <!-- Trap 3 -->
      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-bug"></i> Trap Alert 3: Believing Negative Exponents Create Negative Numbers</div>
        <p><strong>The Blunder:</strong> Writing <span class="math-font">5⁻² = –25</span> or <span class="math-font">2⁻³ = –8</span>.</p>
        <p><strong>Why This Mistake Happens:</strong> The brain associates the minus sign with negative quantities on the number line.</p>
        <p><strong>The Correct Way:</strong> A negative exponent NEVER changes the sign of a positive base! It only signals a <strong>reciprocal (division)</strong>:
          <br><span class="math-font">5⁻² = \frac{1}{5²} = \frac{1}{25} = +0.04</span> (A perfectly positive small fraction!).
          <br><span class="math-font">2⁻³ = \frac{1}{2³} = \frac{1}{8} = +0.125</span>.
        </p>
        <p><strong>Examiner Tip:</strong> Think of the minus sign in the exponent as an elevator that moves the power down into the denominator!</p>
      </div>

      <!-- Trap 4 -->
      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-bug"></i> Trap Alert 4: Multiplying Bases or Adding Bases During Product Law</div>
        <p><strong>The Blunder:</strong> Writing <span class="math-font">2³ × 2⁴ = 4⁷</span> or <span class="math-font">2³ × 2⁴ = 4¹²</span>.</p>
        <p><strong>Why This Mistake Happens:</strong> Students see the multiplication sign between the terms and mistakenly multiply the base numbers (<span class="math-font">2 × 2 = 4</span>).</p>
        <p><strong>The Correct Way:</strong> The base represents the item being counted; it NEVER changes!
          <br><span class="math-font">2³ × 2⁴ = (2 × 2 × 2) × (2 × 2 × 2 × 2) = 2³⁺⁴ = 2⁷ = 128</span>. (NOT <span class="math-font">4⁷ = 16,384</span>!).
        </p>
        <p><strong>Examiner Tip:</strong> Keep the base fixed; only add the exponents!</p>
      </div>

      <!-- Trap 5 -->
      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-bug"></i> Trap Alert 5: Adding Exponents When Adding Powers</div>
        <p><strong>The Blunder:</strong> Writing <span class="math-font">10⁹ + 10⁹ = 10¹⁸</span>, or <span class="math-font">2³ + 2⁴ = 2⁷</span>.</p>
        <p><strong>Why This Mistake Happens:</strong> Students falsely apply the Product Law to addition.</p>
        <p><strong>The Correct Way:</strong> There is NO exponent law for addition! You must treat identical powers like algebraic variables (<span class="math-font">x + x = 2x</span>):
          <br><span class="math-font">10⁹ + 10⁹ = 2 × 10⁹</span> (Two billion, NOT <span class="math-font">10¹⁸</span> which is one quintillion!).
          <br><span class="math-font">2³ + 2⁴ = 8 + 16 = 24</span> (Whereas <span class="math-font">2⁷ = 128</span>!).
        </p>
        <p><strong>Examiner Tip:</strong> Factor out the common power: <span class="math-font">2³ + 2⁴ = 2³(1 + 2¹) = 8 × 3 = 24</span>.</p>
      </div>

      <!-- ======================================================== -->
      <!-- 15 RAPID REVISION POINTS -->
      <!-- ======================================================== -->
      <h3 class="topic-title"><i class="fa-solid fa-list-ol"></i> 15 High-Yield Examination Revision Takeaways</h3>
      <div class="card-grid">
        <div class="concept-card">
          <div class="card-icon">1</div>
          <div class="card-title">Exponential Growth</div>
          <div class="card-text">Multiplicative growth (<span class="math-font">× 2</span>) explodes vastly faster than linear additive growth (<span class="math-font">+ d</span>). Just 46 paper folds reach beyond the Moon!</div>
        </div>
        <div class="concept-card">
          <div class="card-icon">2</div>
          <div class="card-title">Anatomy of a Power</div>
          <div class="card-text">In <span class="math-font">aⁿ</span>, <span class="math-font">a</span> is the base (the repeated factor), and <span class="math-font">n</span> is the exponent (the count of factors).</div>
        </div>
        <div class="concept-card">
          <div class="card-icon">3</div>
          <div class="card-title">Negative Base Parity</div>
          <div class="card-text"><span class="math-font">(–1)ⁿ = +1</span> if <span class="math-font">n</span> is even, and <span class="math-font">–1</span> if <span class="math-font">n</span> is odd. Even powers are always positive; odd powers preserve the negative sign.</div>
        </div>
        <div class="concept-card">
          <div class="card-icon">4</div>
          <div class="card-title">Product Law</div>
          <div class="card-text"><span class="math-font">aᵐ × aⁿ = aᵐ⁺ⁿ</span>. Keep the common base unchanged; add the exponents.</div>
        </div>
        <div class="concept-card">
          <div class="card-icon">5</div>
          <div class="card-title">Quotient Law</div>
          <div class="card-text"><span class="math-font">aᵐ ÷ aⁿ = aᵐ⁻ⁿ</span> (<span class="math-font">a ≠ 0</span>). Keep the common base unchanged; subtract the denominator exponent.</div>
        </div>
        <div class="concept-card">
          <div class="card-icon">6</div>
          <div class="card-title">Power of a Power</div>
          <div class="card-text"><span class="math-font">(aᵐ)ⁿ = aᵐˣⁿ</span>. Powers raised to powers multiply their exponents.</div>
        </div>
        <div class="concept-card">
          <div class="card-icon">7</div>
          <div class="card-title">Distributive Power Laws</div>
          <div class="card-text"><span class="math-font">(ab)ᵐ = aᵐ × bᵐ</span> and <span class="math-font">(a/b)ᵐ = aᵐ / bᵐ</span> (<span class="math-font">b ≠ 0</span>). Powers distribute over multiplication and division.</div>
        </div>
        <div class="concept-card">
          <div class="card-icon">8</div>
          <div class="card-title">The Zero Power</div>
          <div class="card-text"><span class="math-font">a⁰ = 1</span> for every real number <span class="math-font">a ≠ 0</span>. However, <span class="math-font">0⁰</span> is mathematically undefined!</div>
        </div>
        <div class="concept-card">
          <div class="card-icon">9</div>
          <div class="card-title">The Reciprocal Rule</div>
          <div class="card-text"><span class="math-font">a⁻ⁿ = 1 / aⁿ</span> and <span class="math-font">1 / a⁻ⁿ = aⁿ</span> (<span class="math-font">a ≠ 0</span>). Moving a power between numerator and denominator flips the sign of its exponent.</div>
        </div>
        <div class="concept-card">
          <div class="card-icon">10</div>
          <div class="card-title">The Counting Principle</div>
          <div class="card-text">If independent choices have <span class="math-font">c₁, c₂, ..., cₖ</span> options, the total number of combinations is <span class="math-font">c₁ × c₂ × ... × cₖ</span>. A 5-digit PIN has <span class="math-font">10⁵ = 1,00,000</span> codes.</div>
        </div>
        <div class="concept-card">
          <div class="card-icon">11</div>
          <div class="card-title">Standard Scientific Form</div>
          <div class="card-text"><span class="math-font">m × 10ᵏ</span>, where <span class="math-font">1 ≤ m &lt; 10</span> and <span class="math-font">k</span> is an integer. Shift decimal left for positive powers (<span class="math-font">k &gt; 0</span>), and right for negative powers (<span class="math-font">k &lt; 0</span>).</div>
        </div>
        <div class="concept-card">
          <div class="card-icon">12</div>
          <div class="card-title">Comparing Scientific Values</div>
          <div class="card-text">Check the exponent of 10 first. The larger power of 10 always wins regardless of coefficient. Only compare coefficients if exponents are identical.</div>
        </div>
        <div class="concept-card">
          <div class="card-icon">13</div>
          <div class="card-title">Square & Cube Coincidence</div>
          <div class="card-text">A number is both a square and a cube if and only if it is a <strong>sixth power (<span class="math-font">n⁶</span>)</strong>: <span class="math-font">n⁶ = (n³)² = (n²)³</span>. Examples: 1, 64, 729.</div>
        </div>
        <div class="concept-card">
          <div class="card-icon">14</div>
          <div class="card-title">Human Scale vs Cosmic Scale</div>
          <div class="card-text">One million seconds is ~11.5 days; one billion seconds is ~31.7 years. The universe is ~<span class="math-font">4.35 × 10¹⁷ s</span> old.</div>
        </div>
        <div class="concept-card">
          <div class="card-icon">15</div>
          <div class="card-title">Indian Mathematical Heritage</div>
          <div class="card-text">Ancient Indian texts (Lalitavistara) named decimal powers up to <span class="math-font">10⁵³</span> (Tallakkhana) and <span class="math-font">10¹⁴⁰</span> (Asankhyeya) centuries ahead of modern scientific notations!</div>
        </div>
      </div>
    </section>

  </main>

  <!-- ========================================== -->
  <!-- PORTAL FOOTER -->
  <!-- ========================================== -->
  <footer class="portal-footer">
    <div class="footer-inner">
      <div>
        <div class="footer-brand"><i class="fa-solid fa-graduation-cap"></i> Sujit Classes</div>
        <p class="footer-text">
          Empowering middle school students across Odisha with crystal-clear, zero-omission NCERT & BSE study notes, interactive visual proofs, and bilingual master guides.
        </p>
      </div>
      <div>
        <div class="footer-heading">Class 8 Mathematics (Ganita Prakash)</div>
        <ul class="footer-links">
          <li><a href="math-ch1-a-square-and-a-cube.html">Chapter 1: A Square and A Cube</a></li>
          <li><a href="math-ch2-power-play.html">Chapter 2: Power Play (Exponents)</a></li>
          <li><a href="math-ch3-a-story-of-numbers.html">Chapter 3: A Story of Numbers</a></li>
          <li><a href="math-ch4-quadrilaterals.html">Chapter 4: Quadrilaterals</a></li>
        </ul>
      </div>
      <div>
        <div class="footer-heading">Bilingual Medium Portals</div>
        <ul class="footer-links">
          <li><a href="../../index.html">CBSE English Medium Portal</a></li>
          <li><a href="../../index.html">BSE Odisha Odia Medium Portal (ଓଡ଼ିଆ ମାଧ୍ୟମ)</a></li>
          <li><a href="../../index.html">Class 6 NCERT Full Notes</a></li>
          <li><a href="../../index.html">Class 7 NCERT Full Notes</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      &copy; 2026 Sujit Classes. All rights reserved. Built strictly in compliance with NCERT NEP 2020 & BSE Odisha curriculum.
    </div>
  </footer>

  <!-- Floating Back to Top Button -->
  <button id="backToTopBtn" onclick="scrollToTop()" title="Scroll to Top">
    <i class="fa-solid fa-arrow-up"></i>
  </button>

  <!-- ========================================== -->
  <!-- JAVASCRIPT CONTROLLERS -->
  <!-- ========================================== -->
  <script>
    // 1. TOP READING PROGRESS BAR
    window.addEventListener('scroll', function() {
      const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      document.getElementById('progressBar').style.width = scrolled + '%';

      // Back to top button visibility
      const backBtn = document.getElementById('backToTopBtn');
      if (winScroll > 350) {
        backBtn.style.display = 'flex';
      } else {
        backBtn.style.display = 'none';
      }
    });

    function scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // 2. INTERACTIVE QUIZ ENGINE
    let currentQuizScore = 0;
    const answeredQuestions = {};

    function handleMcqChoice(qNum, selectedOption, isCorrect, cardId) {
      if (answeredQuestions[qNum]) return; // prevent re-answering
      answeredQuestions[qNum] = true;

      const card = document.getElementById(cardId);
      const buttons = card.querySelectorAll('.option-btn');
      const feedback = document.getElementById('feedback-' + qNum);

      buttons.forEach(btn => {
        btn.disabled = true;
        btn.style.cursor = 'default';
        const text = btn.innerText.trim();
        if (text.startsWith(selectedOption + ')')) {
          if (isCorrect) {
            btn.classList.add('correct');
            btn.innerHTML = '<i class="fa-solid fa-circle-check"></i> ' + btn.innerHTML;
          } else {
            btn.classList.add('wrong');
            btn.innerHTML = '<i class="fa-solid fa-circle-xmark"></i> ' + btn.innerHTML;
          }
        }
      });

      // If wrong, highlight the correct option in green
      if (!isCorrect) {
        buttons.forEach(btn => {
          const text = btn.innerText.trim();
          // Detect correct button from feedback text
          if (feedback.innerText.includes('Correct Option: ' + text.charAt(0))) {
            btn.classList.add('correct');
            btn.innerHTML = '<i class="fa-solid fa-circle-check"></i> ' + btn.innerHTML + ' (Correct Answer)';
          }
        });
      } else {
        currentQuizScore++;
      }

      document.getElementById('quizScoreDisplay').innerText = 'Score: ' + currentQuizScore + ' / 5';
      feedback.style.display = 'block';
    }

    // 3. TEXT-TO-SPEECH AUDIO READER
    let speechSynth = window.speechSynthesis;
    let speechUtterance = null;
    let isPlayingAudio = false;

    function toggleAudioReader() {
      if (!speechSynth) {
        alert('Text-to-speech is not supported on this browser.');
        return;
      }

      if (isPlayingAudio) {
        speechSynth.cancel();
        isPlayingAudio = false;
        updateAudioButtonUI(false);
      } else {
        // Read out chapter core summary
        const summaryText = "Welcome to Sujit Classes Master Study Notes for Class 8 Mathematics, Chapter 2: Power Play. " +
          "In this chapter, you will master exponential and multiplicative growth, where quantities double or triple rapidly. " +
          "You will learn the seven fundamental laws of exponents: " +
          "First, the product law, a to the power m multiplied by a to the power n equals a to the power m plus n. " +
          "Second, the quotient law, a to the power m divided by a to the power n equals a to the power m minus n. " +
          "Third, the power of a power law, a to the power m, all raised to power n, equals a to the power m times n. " +
          "Fourth, a to the power 0 equals 1 for all non-zero numbers. Remember, zero to the power zero is undefined. " +
          "Fifth, a to the negative n equals 1 divided by a to the positive n. Negative exponents indicate reciprocals, not negative answers. " +
          "Finally, standard scientific notation expresses quantities as m times 10 to the power k, where m is between 1 and 10. " +
          "Explore the interactive diagrams and test your knowledge in the quiz section below!";

        speechUtterance = new SpeechSynthesisUtterance(summaryText);
        speechUtterance.rate = 0.95;
        speechUtterance.pitch = 1.0;
        speechUtterance.lang = 'en-IN';

        speechUtterance.onend = function() {
          isPlayingAudio = false;
          updateAudioButtonUI(false);
        };

        speechUtterance.onerror = function() {
          isPlayingAudio = false;
          updateAudioButtonUI(false);
        };

        speechSynth.cancel(); // clear queue
        speechSynth.speak(speechUtterance);
        isPlayingAudio = true;
        updateAudioButtonUI(true);
      }
    }

    function stopAudioReader() {
      if (speechSynth) {
        speechSynth.cancel();
        isPlayingAudio = false;
        updateAudioButtonUI(false);
      }
    }

    function updateAudioButtonUI(playing) {
      const topBtn = document.getElementById('topAudioBtn');
      const playBtn = document.getElementById('playAudioBtn');
      const stopBtn = document.getElementById('stopAudioBtn');

      if (playing) {
        topBtn.innerHTML = '<i class="fa-solid fa-volume-xmark"></i> Stop Audio';
        playBtn.style.display = 'none';
        stopBtn.style.display = 'inline-flex';
      } else {
        topBtn.innerHTML = '<i class="fa-solid fa-volume-high"></i> Listen to Notes';
        playBtn.style.display = 'inline-flex';
        stopBtn.style.display = 'none';
      }
    }
  </script>
</body>
</html>
"""
