# -*- coding: utf-8 -*-
"""
Section 6: Exam Hall Trap Alerts & 15 Revision Points + Script Engine
"""

def get_section_6():
    return '''
    <!-- SECTION 6: EXAM HALL TRAP ALERTS & 15 REVISION POINTS -->
    <section id="section-6" class="study-section">
      <div class="section-header">
        <div class="section-icon icon-red">
          <i class="fa-solid fa-triangle-exclamation"></i>
        </div>
        <div>
          <h2>Section 6: Exam Hall Trap Alerts &amp; 15 Rapid Revision Points</h2>
          <p>Critical diagnostic warnings against 5 fatal exam mistakes, plus 15 high-yield revision bullet points for exam eve.</p>
        </div>
      </div>

      <!-- 5 TRAP ALERTS -->
      <h3><i class="fa-solid fa-skull-crossbones"></i> The 5 Fatal Exam Hall Traps (And How to Avoid Them)</h3>
      <p>
        Every year, thousands of students lose 5 to 10 marks in Class 7 mathematics examinations due to recurring mechanical mistakes. 
        Here are the five most dangerous traps and how you can sidestep them effortlessly:
      </p>

      <!-- TRAP 1 -->
      <div class="trap-card">
        <div class="trap-title">
          <i class="fa-solid fa-ban"></i> Trap 1: The Blind Left-to-Right Add/Multiply Trap (Purna's Blunder)
        </div>
        <p>
          <strong>Why students fall into the trap:</strong> In everyday English, we read from left to right. 
          When students see <span class="math-inline">30 + 5 × 4</span>, their eye naturally encounters "30 + 5" first, and they add them to get 35, 
          then multiply by 4 to get 140!
        </p>
        <div class="trap-grid">
          <div class="trap-wrong">
            <strong><i class="fa-solid fa-xmark"></i> WRONG APPROACH:</strong>
            <br><span class="math-inline">30 + 5 × 4 = 35 × 4 = 140</span>
            <br><em>(Blindly adding before multiplying breaks the integrity of terms!)</em>
          </div>
          <div class="trap-right">
            <strong><i class="fa-solid fa-check"></i> CORRECT APPROACH:</strong>
            <br><span class="math-inline">30 + (5 × 4) = 30 + 20 = 50</span>
            <br><em>(Multiplication forms a single term that must be evaluated first!)</em>
          </div>
        </div>
        <p style="margin:0; font-size: 0.9rem; color: #475569;">
          <strong>Teacher's Pro-Tip:</strong> Draw a mental boundary box around any multiplication or division expression. 
          Treat <span class="math-inline">5 × 4</span> as a single package labeled "20".
        </p>
      </div>

      <!-- TRAP 2 -->
      <div class="trap-card">
        <div class="trap-title">
          <i class="fa-solid fa-ban"></i> Trap 2: The Bracket Sign-Inversion Blind Spot
        </div>
        <p>
          <strong>Why students fall into the trap:</strong> When expanding <span class="math-inline">100 − (15 + 56)</span> or <span class="math-inline">500 − (250 − 100)</span>, 
          students only apply the minus sign to the first number inside and forget to flip the sign of the second number!
        </p>
        <div class="trap-grid">
          <div class="trap-wrong">
            <strong><i class="fa-solid fa-xmark"></i> WRONG APPROACH:</strong>
            <br><span class="math-inline">100 − (15 + 56) = 100 − 15 + 56 = 141</span>
            <br><span class="math-inline">500 − (250 − 100) = 500 − 250 − 100 = 150</span>
          </div>
          <div class="trap-right">
            <strong><i class="fa-solid fa-check"></i> CORRECT APPROACH:</strong>
            <br><span class="math-inline">100 − (15 + 56) = 100 − 15 − 56 = 29</span>
            <br><span class="math-inline">500 − (250 − 100) = 500 − 250 + 100 = 350</span>
          </div>
        </div>
        <p style="margin:0; font-size: 0.9rem; color: #475569;">
          <strong>Teacher's Pro-Tip:</strong> Remember the <em>Inversion Gate</em>: removing parentheses preceded by '−' inverts EVERY single sign inside (+ flips to −, and − flips to +).
        </p>
      </div>

      <!-- TRAP 3 -->
      <div class="trap-card">
        <div class="trap-title">
          <i class="fa-solid fa-ban"></i> Trap 3: The Half-Hearted Distributive Expansion
        </div>
        <p>
          <strong>Why students fall into the trap:</strong> When expanding <span class="math-inline">5 × (4 + 3)</span>, 
          students multiply the 5 by the 4, but simply copy the +3 without multiplying it by 5!
        </p>
        <div class="trap-grid">
          <div class="trap-wrong">
            <strong><i class="fa-solid fa-xmark"></i> WRONG APPROACH:</strong>
            <br><span class="math-inline">5 × (4 + 3) = 5 × 4 + 3 = 20 + 3 = 23</span>
            <br><em>(Forgetting to distribute the multiplier to the second addend!)</em>
          </div>
          <div class="trap-right">
            <strong><i class="fa-solid fa-check"></i> CORRECT APPROACH:</strong>
            <br><span class="math-inline">5 × (4 + 3) = 5 × 4 + 5 × 3 = 20 + 15 = 35</span>
            <br><em>(The multiplier distributes fairly to BOTH terms inside!)</em>
          </div>
        </div>
        <p style="margin:0; font-size: 0.9rem; color: #475569;">
          <strong>Teacher's Pro-Tip:</strong> Think of the multiplier as a teacher handing out chocolates: every student inside the classroom must receive a chocolate, not just the one sitting in the front row!
        </p>
      </div>

      <!-- TRAP 4 -->
      <div class="trap-card">
        <div class="trap-title">
          <i class="fa-solid fa-ban"></i> Trap 4: Illegally Swapping Numbers in Subtraction
        </div>
        <p>
          <strong>Why students fall into the trap:</strong> Students confuse the commutativity of addition with subtraction. 
          When they see <span class="math-inline">14 − 20</span>, they mentally flip it to <span class="math-inline">20 − 14 = 6</span> because they are uncomfortable with negative numbers.
        </p>
        <div class="trap-grid">
          <div class="trap-wrong">
            <strong><i class="fa-solid fa-xmark"></i> WRONG APPROACH:</strong>
            <br><span class="math-inline">14 − 20 = 20 − 14 = 6</span>
            <br><em>(Subtraction is NOT commutative: a − b ≠ b − a!)</em>
          </div>
          <div class="trap-right">
            <strong><i class="fa-solid fa-check"></i> CORRECT APPROACH:</strong>
            <br><span class="math-inline">14 − 20 = 14 + (−20) = −6</span>
            <br><em>(If you swap terms, you must carry the negative sign: (−20) + 14 = −6!)</em>
          </div>
        </div>
        <p style="margin:0; font-size: 0.9rem; color: #475569;">
          <strong>Teacher's Pro-Tip:</strong> Never swap numbers across a minus sign without attaching the sign to the number as an additive inverse: <span class="math-inline">a − b = (−b) + a</span>.
        </p>
      </div>

      <!-- TRAP 5 -->
      <div class="trap-card">
        <div class="trap-title">
          <i class="fa-solid fa-ban"></i> Trap 5: The Climbing Snail Endpoint Fallacy
        </div>
        <p>
          <strong>Why students fall into the trap:</strong> In climbing rate puzzles (climbs 3 cm day, slips 2 cm night on a 10 cm pole), 
          students calculate the net rate (<span class="math-inline">3 − 2 = 1</span> cm/day) and divide <span class="math-inline">10 ÷ 1 = 10  days</span>.
        </p>
        <div class="trap-grid">
          <div class="trap-wrong">
            <strong><i class="fa-solid fa-xmark"></i> WRONG APPROACH:</strong>
            <br><span class="math-inline">Net Rate = 1  cm/day ⇒ 10  cm ÷ 1 = 10  days</span>
            <br><em>(Assumes the snail slips down even after already reaching the treat!)</em>
          </div>
          <div class="trap-right">
            <string><i class="fa-solid fa-check"></i> CORRECT APPROACH:</strong>
            <br>At end of Day 7, snail is at <span class="math-inline">7 × 1 = 7</span> cm. 
            On Day 8 morning, it climbs 3 cm: <span class="math-inline">7 + 3 = 10</span> cm! 
            It touches the treat on <strong>Day 8</strong> and stops climbing!
          </div>
        </div>
        <p style="margin:0; font-size: 0.9rem; color: #475569;">
          <strong>Teacher's Pro-Tip:</strong> In all rate problems with nightly drops, subtract the single daytime climb from the total height first (<span class="math-inline">10 − 3 = 7</span> cm). Calculate days to reach that milestone, then add 1 day for the final climb!
        </p>
      </div>

      <!-- 15 RAPID REVISION POINTS -->
      <h3><i class="fa-solid fa-list-ol"></i> 15 Rapid Revision Points for Exam Eve</h3>
      <ol style="margin-left: 1.6rem; line-height: 1.8;">
        <li>An <strong>arithmetic expression</strong> is a meaningful combination of numbers and basic operators (+, −, ×, ÷) without an equals or inequality sign.</li>
        <li>Every arithmetic expression evaluates to a single unique <strong>numerical value</strong>.</li>
        <li>The equality sign (<span class="math-inline">=</span>) signifies that two expressions have identical numerical values.</li>
        <li><strong>Terms</strong> are the building blocks of an arithmetic expression, defined strictly as parts separated by '+' signs.</li>
        <li>Subtraction is universally treated as the addition of an additive inverse: <span class="math-inline">a − b = a + (−b)</span>.</li>
        <li>The <strong>Commutative Property of Addition</strong> states that swapping terms does not alter the sum: <span class="math-inline">Term 1 + Term 2 = Term 2 + Term 1</span>.</li>
        <li>The <strong>Associative Property of Addition</strong> guarantees that grouping terms in any order preserves the sum: <span class="math-inline">(a + b) + c = a + (b + c)</span>.</li>
        <li>Subtraction and division are <strong>neither commutative nor associative</strong>: <span class="math-inline">a − b ≠ b − a</span> and <span class="math-inline">a ÷ b ≠ b ÷ a</span>.</li>
        <li>When an expression has no brackets, operations inside terms (multiplication and division) are performed first, followed by addition of terms.</li>
        <li>When removing brackets preceded by a positive sign (+), all internal signs remain strictly unchanged: <span class="math-inline">a + (b − c) = a + b − c</span>.</li>
        <li>When removing brackets preceded by a negative sign (−), every sign inside the bracket inverts: <span class="math-inline">a − (b + c) = a − b − c</span> and <span class="math-inline">a − (b − c) = a − b + c</span>.</li>
        <li>The <strong>Distributive Property over Addition</strong> states: <span class="math-inline">a × (b + c) = a × b + a × c</span>.</li>
        <li>The <strong>Distributive Property over Subtraction</strong> states: <span class="math-inline">a × (b − c) = a × b − a × c</span>.</li>
        <li>Mental multiplication hacks utilize the distributive property by decomposing numbers near powers of 10 (e.g., <span class="math-inline">97 × 25 = (100 − 3) × 25 = 2500 − 75 = 2425</span>).</li>
        <li>In alternating arithmetic series <span class="math-inline">1 − 2 + 3 − 4 + ... + (2n − 1) − 2n</span>, the sum is always equal to <span class="math-inline">−n</span>.</li>
      </ol>

      <div class="callout callout-act">
        <div class="callout-title"><i class="fa-solid fa-graduation-cap"></i> Final Words of Encouragement</div>
        <p>
          Mathematics is not a spectator sport, nor is it a set of arbitrary rules to memorize blindly. 
          By seeing expressions as sums of living terms and understanding the physical geometry of the distributive law, 
          you now possess the exact conceptual toolkit used by top mathematicians and scientists. 
          Step into your exam hall with pride and total confidence!
        </p>
      </div>
    </section>

    <!-- FLOATING BACK TO TOP BUTTON -->
    <button id="backToTopBtn" onclick="scrollToTop()" title="Back to Top">
      <i class="fa-solid fa-arrow-up"></i>
    </button>

    <!-- FOOTER -->
    <footer>
      <div class="container" style="padding:0;">
        <p style="font-family: 'Space Grotesk', sans-serif; font-size: 1.25rem; font-weight: 700; color: #f8fafc; margin-bottom: 0.5rem;">
          <i class="fa-solid fa-shapes"></i> Sujit Classes • Holistic Mathematics Portal
        </p>
        <p style="font-size: 0.95rem; color: #94a3b8; max-width: 600px; margin: 0 auto 1.5rem auto;">
          Class 7 Mathematics Chapter 2: Arithmetic Expressions (NCERT Ganita Prakash gegp102). 
          Dedicated to students across Odisha studying in CBSE English Medium and BSE Odisha schools.
        </p>
        <div class="footer-links">
          <a href="../../index.html"><i class="fa-solid fa-house"></i> Home Portal</a>
          <a href="math-ch1-large-numbers-around-us.html"><i class="fa-solid fa-backward"></i> Previous Chapter (Ch 1)</a>
          <a href="#section-1"><i class="fa-solid fa-arrow-up"></i> Top of Page</a>
          <a href="https://ncert.nic.in" target="_blank" rel="noopener"><i class="fa-solid fa-book"></i> NCERT Official</a>
        </div>
        <p style="font-size: 0.85rem; color: #64748b; margin-top: 1.5rem;">
          &copy; 2026 Sujit Classes. Zero-omission pedagogical study materials crafted for academic excellence.
        </p>
      </div>
    </footer>

    <!-- INTERACTIVE JAVASCRIPT ENGINE -->
    <script>
      // 1. TOP FIXED READING PROGRESS BAR & BACK TO TOP BUTTON
      window.addEventListener('scroll', function() {
        const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (winScroll / height) * 100;
        document.getElementById('progressBar').style.width = scrolled + '%';

        const bttBtn = document.getElementById('backToTopBtn');
        if (winScroll > 300) {
          bttBtn.style.display = 'flex';
        } else {
          bttBtn.style.display = 'none';
        }
      });

      function scrollToTop() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }

      // 2. INTERACTIVE QUIZ ENGINE
      let currentQuizScore = 0;
      const answeredQuestions = new Set();

      const quizAnswers = {
        1: {
          correct: 'B',
          traps: {
            'A': 'Trap Alert: You treated numbers and operators as individual parts! Terms are separated strictly by "+", so products like 6 × 3 form a single term.',
            'C': 'Trap Alert: You grouped operations from left to right! Subtraction binds as an additive inverse, not with the subsequent addition.',
            'D': 'Trap Alert: Almost! But remember that subtraction converts to addition of inverse, so the term carries a negative sign: −(6 × 3).'
          },
          explanation: 'Correct! The expression is rewritten as 45 + (−(6 × 3)) + (28 ÷ 4). The three terms separated by + are 45, −(6 × 3), and 28 ÷ 4.'
        },
        2: {
          correct: 'C',
          traps: {
            'A': 'Trap Alert: You forgot that the minus sign in front of the bracket inverts the −15 into +15!',
            'B': 'Trap Alert: The positive 25 inside flips to −25, not +25.',
            'D': 'Trap Alert: The preceding minus sign inverts all signs; it does not turn everything into plus!'
          },
          explanation: 'Correct! When removing brackets preceded by minus, every internal term changes sign: +25 becomes −25, and −15 becomes +15. Thus, 75 − 25 + 15.'
        },
        3: {
          correct: 'B',
          traps: {
            'A': 'Trap Alert: Half-hearted distribution! You multiplied 18 by 20, but forgot to multiply 18 by 5.',
            'C': 'Trap Alert: That is an invented formula! The multiplier outside distributes to each term inside.',
            'D': 'Trap Alert: You replaced subtraction with addition! Distributing over subtraction must preserve the minus sign.'
          },
          explanation: 'Correct! a × (b − c) = a × b − a × c. Both 20 and 5 must be multiplied by 18, with the subtraction sign preserved.'
        },
        4: {
          correct: 'A',
          traps: {
            'B': 'Trap Alert: In 540 − 12 × 18, you are subtracting 18 groups of 12, which takes away MORE, leaving a SMALLER result!',
            'C': 'Trap Alert: 12 × 15 = 180, while 12 × 18 = 216. Since 180 < 216, 540 − 180 is strictly greater.',
            'D': 'Trap Alert: You can easily reason this! Subtracting a smaller amount always leaves a larger remainder.'
          },
          explanation: 'Correct! Both start at 540. Expression A subtracts 12 × 15 (= 180), while Expression B subtracts 12 × 18 (= 216). Subtracting less leaves a strictly greater remainder (360 > 324).'
        },
        5: {
          correct: 'B',
          traps: {
            'A': 'Trap Alert: You divided 14 by 2 = 7! But on Day 6 morning, the snail already touches the top and stops!',
            'C': 'Trap Alert: At the end of Day 4, the snail is at 8 cm. Day 5 morning climb of 4 cm reaches 12 cm, which is still 2 cm short of 14 cm.',
            'D': 'Trap Alert: 8 days would mean the snail slipped down even after reaching the treat, which it does not!'
          },
          explanation: 'Correct! Net climb = 4 − 2 = 2 cm/day. At the end of Day 5 (night), it is at 5 × 2 = 10 cm. On Day 6 daytime, it climbs 4 cm: 10 + 4 = 14 cm! It reaches the treat on Day 6.'
        }
      };

      function checkQuizAnswer(qNum, btn, selectedOpt) {
        if (answeredQuestions.has(qNum)) return;
        answeredQuestions.add(qNum);

        const card = document.getElementById('quiz-card-' + qNum);
        const buttons = card.querySelectorAll('.option-btn');
        const feedback = document.getElementById('feedback-' + qNum);
        const qData = quizAnswers[qNum];

        buttons.forEach(b => {
          b.disabled = true;
          b.style.cursor = 'default';
        });

        if (selectedOpt === qData.correct) {
          btn.classList.add('correct');
          feedback.className = 'quiz-feedback show success';
          feedback.innerHTML = '<strong><i class=\"fa-solid fa-circle-check\"></i> Brilliant!</strong> ' + qData.explanation;
          currentQuizScore++;
        } else {
          btn.classList.add('wrong');
          buttons.forEach(b => {
            if (b.innerText.startsWith(qData.correct + ')')) {
              b.classList.add('correct');
            }
          });
          feedback.className = 'quiz-feedback show error';
          feedback.innerHTML = '<strong><i class=\"fa-solid fa-circle-xmark\"></i> ' + qData.traps[selectedOpt] + '</strong><br>' + qData.explanation;
        }

        document.getElementById('userQuizScore').innerText = currentQuizScore + ' / 5';
      }

      // 3. AUDIO NARRATOR (TEXT-TO-SPEECH)
      let synth = window.speechSynthesis;
      let utterance = null;
      let isPlaying = false;

      function toggleAudioNarrator() {
        if (!synth) {
          alert('Sorry, text-to-speech is not supported on this browser.');
          return;
        }

        const navBtnText = document.getElementById('navAudioText');

        if (isPlaying) {
          synth.cancel();
          isPlaying = false;
          navBtnText.innerText = 'Listen Note';
        } else {
          const narrationText = "Welcome to Class 7 Mathematics, Chapter 2: Arithmetic Expressions. " +
            "In this chapter, you will master the fundamental anatomy of mathematical terms, the order of operations, and the power of brackets. " +
            "Remember: terms are the parts of an expression separated strictly by plus signs. Subtraction is simply adding an additive inverse. " +
            "When removing brackets preceded by a minus sign, every sign inside the bracket inverts. " +
            "And with the distributive property, multiplying across additions or subtractions turns hard calculations into lightning mental math. " +
            "Explore each section below, examine the 6 interactive diagrams, and solve every single NCERT problem step by step.";

          utterance = new SpeechSynthesisUtterance(narrationText);
          utterance.rate = 0.95;
          utterance.pitch = 1.0;

          utterance.onend = function() {
            isPlaying = false;
            navBtnText.innerText = 'Listen Note';
          };

          utterance.onerror = function() {
            isPlaying = false;
            navBtnText.innerText = 'Listen Note';
          };

          synth.speak(utterance);
          isPlaying = true;
          navBtnText.innerText = 'Stop Audio';
        }
      }
    </script>
</body>
</html>
'''
