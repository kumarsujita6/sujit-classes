# -*- coding: utf-8 -*-
"""
Module: ch3_section6_footer.py
Contains Section 6: Exam Hall Trap Alerts (5 common blunders),
15 High-Yield Examination Takeaways, Comprehensive Footer,
and Complete Client-Side JavaScript Engine (Progress bar, Audio TTS, Quiz, Back-to-Top).
"""

def get_section_6_and_footer():
    return """
    <!-- ======================================================== -->
    <!-- SECTION 6: EXAM HALL TRAP ALERTS & 15 REVISION POINTS    -->
    <!-- ======================================================== -->
    <section id="section-6">
      <div class="section-header">
        <span class="section-badge"><i class="fa-solid fa-triangle-exclamation"></i> Critical Exam Hall Strategy</span>
        <h2 class="section-title">Section 6: Exam Hall Trap Alerts (5 Student Blunders) & 15 Revision Points</h2>
        <p class="section-desc">
          Identify the 5 most lethal misconceptions that cost middle-school students marks in board examinations, followed by 15 high-yield revision takeaways.
        </p>
      </div>

      <!-- 5 COMMON STUDENT BLUNDERS -->
      <h3><i class="fa-solid fa-bomb" style="color: var(--danger);"></i> The 5 Most Fatal Student Blunders in Number Systems</h3>

      <div style="display: flex; flex-direction: column; gap: 1.5rem; margin-top: 1.5rem;">

        <!-- BLUNDER 1 -->
        <div style="background: #fff5f5; border: 1.5px solid #fecaca; border-radius: var(--radius-md); padding: 1.5rem;">
          <h4 style="color: #991b1b; margin-top: 0; margin-bottom: 0.5rem; font-size: 1.15rem;">
            <i class="fa-solid fa-circle-xmark"></i> Blunder 1: Confusing Face Value with Place Value
          </h4>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-top: 0.75rem;">
            <div style="background: white; border-left: 4px solid var(--danger); padding: 1rem; border-radius: var(--radius-sm);">
              <strong style="color: var(--danger-dark);"><i class="fa-solid fa-skull"></i> The Mistake Alert:</strong>
              <p style="font-size: 0.9rem; margin: 0.4rem 0 0 0; color: #475569;">
                When asked for the value of digit <code>7</code> in the numeral <code>7,530</code>, writing simply <em>"The value is 7"</em>.
              </p>
            </div>
            <div style="background: white; border-left: 4px solid #16a34a; padding: 1rem; border-radius: var(--radius-sm);">
              <strong style="color: #15803d;"><i class="fa-solid fa-check"></i> The Topper's Way:</strong>
              <p style="font-size: 0.9rem; margin: 0.4rem 0 0 0; color: #475569;">
                Always distinguish: <strong>Face Value = 7</strong> (the digit's intrinsic shape). <strong>Place Value = Face Value × Column Weight = 7 × 1,000 = 7,000</strong>!
              </p>
            </div>
          </div>
        </div>

        <!-- BLUNDER 2 -->
        <div style="background: #fff5f5; border: 1.5px solid #fecaca; border-radius: var(--radius-md); padding: 1.5rem;">
          <h4 style="color: #991b1b; margin-top: 0; margin-bottom: 0.5rem; font-size: 1.15rem;">
            <i class="fa-solid fa-circle-xmark"></i> Blunder 2: Using the Base Number 'n' as a Single Digit in Base-n
          </h4>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-top: 0.75rem;">
            <div style="background: white; border-left: 4px solid var(--danger); padding: 1rem; border-radius: var(--radius-sm);">
              <strong style="color: var(--danger-dark);"><i class="fa-solid fa-skull"></i> The Mistake Alert:</strong>
              <p style="font-size: 0.9rem; margin: 0.4rem 0 0 0; color: #475569;">
                Writing the decimal number 5 as <code>5₅</code> in Base-5, or writing 8 as <code>8₈</code> in Base-8.
              </p>
            </div>
            <div style="background: white; border-left: 4px solid #16a34a; padding: 1rem; border-radius: var(--radius-sm);">
              <strong style="color: #15803d;"><i class="fa-solid fa-check"></i> The Topper's Way:</strong>
              <p style="font-size: 0.9rem; margin: 0.4rem 0 0 0; color: #475569;">
                In any base-n system, digits can ONLY range from <strong>0 to n - 1</strong>. The symbol 'n' never exists as a digit! In Base-5, 5 is written as <strong>10₅</strong> (one five and zero ones). In Base-8, 8 is written as <strong>10₈</strong>!
              </p>
            </div>
          </div>
        </div>

        <!-- BLUNDER 3 -->
        <div style="background: #fff5f5; border: 1.5px solid #fecaca; border-radius: var(--radius-md); padding: 1.5rem;">
          <h4 style="color: #991b1b; margin-top: 0; margin-bottom: 0.5rem; font-size: 1.15rem;">
            <i class="fa-solid fa-circle-xmark"></i> Blunder 3: Illegal Roman Subtractive Shortcuts (e.g. Writing IL for 49)
          </h4>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-top: 0.75rem;">
            <div style="background: white; border-left: 4px solid var(--danger); padding: 1rem; border-radius: var(--radius-sm);">
              <strong style="color: var(--danger-dark);"><i class="fa-solid fa-skull"></i> The Mistake Alert:</strong>
              <p style="font-size: 0.9rem; margin: 0.4rem 0 0 0; color: #475569;">
                Writing 49 as <code>IL</code> (50 - 1), writing 99 as <code>IC</code> (100 - 1), or writing 95 as <code>VC</code> (100 - 5).
              </p>
            </div>
            <div style="background: white; border-left: 4px solid #16a34a; padding: 1rem; border-radius: var(--radius-sm);">
              <strong style="color: #15803d;"><i class="fa-solid fa-check"></i> The Topper's Way:</strong>
              <p style="font-size: 0.9rem; margin: 0.4rem 0 0 0; color: #475569;">
                Roman subtraction respects decimal place orders! <code>I</code> can only be subtracted from <code>V</code> and <code>X</code>. <code>X</code> can only be subtracted from <code>L</code> and <code>C</code>. <code>C</code> can only be subtracted from <code>D</code> and <code>M</code>. <code>V</code>, <code>L</code>, and <code>D</code> are NEVER subtracted! <br>
                • 49 = 40 + 9 = <strong>XLIX</strong> (never IL). <br>
                • 99 = 90 + 9 = <strong>XCIX</strong> (never IC). <br>
                • 95 = 90 + 5 = <strong>XCV</strong> (never VC).
              </p>
            </div>
          </div>
        </div>

        <!-- BLUNDER 4 -->
        <div style="background: #fff5f5; border: 1.5px solid #fecaca; border-radius: var(--radius-md); padding: 1.5rem;">
          <h4 style="color: #991b1b; margin-top: 0; margin-bottom: 0.5rem; font-size: 1.15rem;">
            <i class="fa-solid fa-circle-xmark"></i> Blunder 4: Omitting the Zero Placeholder in Positional Multi-Digit Numbers
          </h4>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-top: 0.75rem;">
            <div style="background: white; border-left: 4px solid var(--danger); padding: 1rem; border-radius: var(--radius-sm);">
              <strong style="color: var(--danger-dark);"><i class="fa-solid fa-skull"></i> The Mistake Alert:</strong>
              <p style="font-size: 0.9rem; margin: 0.4rem 0 0 0; color: #475569;">
                When converting a number that has zero in a certain power place (e.g. <code>3605 = 1×3600 + 0×60 + 5×1</code>), writing only the non-zero digits and dropping the placeholder: writing <code>1 5</code> or <code>15</code>!
              </p>
            </div>
            <div style="background: white; border-left: 4px solid #16a34a; padding: 1rem; border-radius: var(--radius-sm);">
              <strong style="color: #15803d;"><i class="fa-solid fa-check"></i> The Topper's Way:</strong>
              <p style="font-size: 0.9rem; margin: 0.4rem 0 0 0; color: #475569;">
                In any positional system, an empty column MUST be occupied by an unambiguous zero placeholder. Otherwise, the column values collapse! In Base-60, 3605 is <code>[1] [0] [5]</code>, never <code>[1] [5]</code> (which would equal 1×60 + 5 = 65)!
              </p>
            </div>
          </div>
        </div>

        <!-- BLUNDER 5 -->
        <div style="background: #fff5f5; border: 1.5px solid #fecaca; border-radius: var(--radius-md); padding: 1.5rem;">
          <h4 style="color: #991b1b; margin-top: 0; margin-bottom: 0.5rem; font-size: 1.15rem;">
            <i class="fa-solid fa-circle-xmark"></i> Blunder 5: Miscalculating the Mayan Third Tier Multiplier
          </h4>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-top: 0.75rem;">
            <div style="background: white; border-left: 4px solid var(--danger); padding: 1rem; border-radius: var(--radius-sm);">
              <strong style="color: var(--danger-dark);"><i class="fa-solid fa-skull"></i> The Mistake Alert:</strong>
              <p style="font-size: 0.9rem; margin: 0.4rem 0 0 0; color: #475569;">
                Treating the Mayan system as a pure base-20 geometric progression and multiplying Tier 3 by <code>20² = 400</code>.
              </p>
            </div>
            <div style="background: white; border-left: 4px solid #16a34a; padding: 1rem; border-radius: var(--radius-sm);">
              <strong style="color: #15803d;"><i class="fa-solid fa-check"></i> The Topper's Way:</strong>
              <p style="font-size: 0.9rem; margin: 0.4rem 0 0 0; color: #475569;">
                Remember the Mayan calendar anomaly! To match the 360-day solar year, Tier 3 has a weight of <strong>18 × 20 = 360</strong> (not 400). Tier 4 has a weight of <code>360 × 20 = 7,200</code>!
              </p>
            </div>
          </div>
        </div>

      </div>

      <!-- 15 REVISION TAKEAWAYS -->
      <h3><i class="fa-solid fa-list-check" style="color: var(--primary);"></i> 15 High-Yield Examination Revision Takeaways</h3>

      <div style="background: var(--light); border: 1px solid var(--border); border-radius: var(--radius-md); padding: 2rem; margin-top: 1.5rem;">
        <ol style="margin-left: 1.5rem; line-height: 2; font-size: 0.975rem; color: var(--text);">
          <li><strong>Origin of Counting:</strong> Began over 44,000 years ago during the Paleolithic Stone Age to track livestock, food stores, barter transactions, ritual offerings, and lunar phases.</li>
          <li><strong>One-to-One Mapping (Bijection):</strong> The fundamental mechanism of counting where each physical object is paired with exactly one distinct counter (pebble, stick, notch).</li>
          <li><strong>Subitizing Threshold:</strong> Human vision can immediately identify quantities from 1 to 4 without counting. Groups of 5 or more require grouping or sequential counting, giving rise to packet sizes of 2, 5, 10, and 20.</li>
          <li><strong>Tally Bones:</strong> The <strong>Lebombo Bone (44,000 BCE)</strong> has 29 notches (lunar calendar); the <strong>Ishango Bone (25,000 BCE)</strong> displays prime and doubling columns.</li>
          <li><strong>Counting in Twos:</strong> Indigenous tribes (Gumulgal of Australia, Bakairi of South America, Bushmen of South Africa) independently developed 2-based spoken systems (urapon = 1, ukasar = 2).</li>
          <li><strong>Roman Landmark System:</strong> Uses 7 fixed letters (I=1, V=5, X=10, L=50, C=100, D=500, M=1000). Additive and subtractive rules, but lacks place value and zero, making multiplication arduous.</li>
          <li><strong>Base-n System Definition:</strong> The 1st landmark is 1 (n⁰ = 1); every subsequent landmark is obtained by multiplying the previous landmark by a fixed positive integer n (powers: n⁰, n¹, n², n³...).</li>
          <li><strong>Base-n Regrouping Axiom:</strong> In any base-n system, exactly n units of any landmark consolidate into 1 unit of the next higher landmark.</li>
          <li><strong>Closure of Landmark Multiplication:</strong> In a base-n system, <code>nᵃ × nᵇ = nᵃ⁺ᵇ</code>, guaranteeing that the product of any two landmarks is always another landmark.</li>
          <li><strong>Egyptian Hieroglyphic System (~3000 BCE):</strong> A base-10 additive system with 7 distinct pictorial hieroglyphs for powers 10⁰ to 10⁶. Suffered from the need to invent infinite pictures for higher powers.</li>
          <li><strong>Mesopotamian Sexagesimal System (~2000 BCE):</strong> The first true positional system (Base 60), using wedges (1) and corner wedges (10). Gave humanity 60 seconds, 60 minutes, and 360° in a circle.</li>
          <li><strong>Mayan Vigesimal System (300–900 CE):</strong> Positional base-20 system stacked vertically (1s, 20s, 360s, 7200s) using dots (1), bars (5), and an independently invented <strong>seashell zero placeholder</strong>.</li>
          <li><strong>Chinese Rod Numerals (3rd c. BCE):</strong> Decimal positional system using counting rods. Alternated between <strong>Zong (vertical)</strong> and <strong>Heng (horizontal)</strong> to prevent adjacent digit collisions.</li>
          <li><strong>The Bakhshali Manuscript (c. 3rd–4th c. CE):</strong> Ancient Indian birch-bark document containing the world's oldest physical evidence of zero written as a dot (śūnya-bindu).</li>
          <li><strong>The Crown Jewel — Hindu Decimal System:</strong> United 10 universal digits (0–9) with positional decimal place value. Zero was elevated by Aryabhata and Brahmagupta (628 CE) to both an unambiguous placeholder and an algebraic number, establishing the foundation of all modern science and computing.</li>
        </ol>
      </div>

    </section>

    <!-- FOOTER -->
    <footer>
      <div class="footer-content">
        <div class="footer-brand">
          <h4><i class="fa-solid fa-graduation-cap"></i> Sujit Classes</h4>
          <p>
            Empowering students in Odisha and across India with crystal-clear, exhaustive, zero-omission master study materials for CBSE and BSE State Board curriculums.
          </p>
        </div>
        <div class="footer-links">
          <h5>Class 8 Mathematics</h5>
          <ul>
            <li><a href="math-ch1-a-square-and-a-cube.html">Chapter 1: A Square and a Cube</a></li>
            <li><a href="math-ch2-power-play.html">Chapter 2: Power Play (Exponents)</a></li>
            <li><a href="math-ch3-a-story-of-numbers.html">Chapter 3: A Story of Numbers</a></li>
            <li><a href="math-ch4-quadrilaterals.html">Chapter 4: Quadrilaterals</a></li>
          </ul>
        </div>
        <div class="footer-links">
          <h5>Quick Portal Links</h5>
          <ul>
            <li><a href="../../index.html">Portal Home</a></li>
            <li><a href="../../index.html#english-medium">English Medium Notes</a></li>
            <li><a href="../../index.html#odia-medium">Odia Medium Notes</a></li>
            <li><a href="#section-1">Back to Chapter Top</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 Sujit Classes. All rights reserved. Strictly aligned with NCERT NEP 2020 curriculum guidelines (Code: hegp103).</p>
      </div>
    </footer>

    <!-- BACK TO TOP FLOATING BUTTON -->
    <button id="backToTopBtn" onclick="scrollToTop()" aria-label="Back to Top">
      <i class="fa-solid fa-arrow-up"></i>
    </button>

  </div><!-- /container -->

  <!-- CLIENT-SIDE INTERACTIVE JAVASCRIPT ENGINE -->
  <script>
    // 1. TOP READING PROGRESS BAR
    window.addEventListener('scroll', function() {
      const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      document.getElementById('progressBar').style.width = scrolled + '%';

      // Back to top button visibility
      const backBtn = document.getElementById('backToTopBtn');
      if (winScroll > 400) {
        backBtn.classList.add('visible');
      } else {
        backBtn.classList.remove('visible');
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
          if (qNum === 1 && text.startsWith('B)')) btn.classList.add('correct');
          if (qNum === 2 && text.startsWith('C)')) btn.classList.add('correct');
          if (qNum === 3 && text.startsWith('B)')) btn.classList.add('correct');
          if (qNum === 4 && text.startsWith('B)')) btn.classList.add('correct');
          if (qNum === 5 && text.startsWith('C)')) btn.classList.add('correct');
        });
      }

      // Show feedback
      if (isCorrect) {
        currentQuizScore++;
        feedback.classList.add('show', 'correct-feedback');
      } else {
        feedback.classList.add('show', 'wrong-feedback');
      }

      // Update score display
      document.getElementById('quizScoreDisplay').innerText = currentQuizScore + ' / 5';
    }

    // 3. INTERACTIVE WEB SPEECH API AUDIO READER
    let synth = window.speechSynthesis;
    let isPlayingAudio = false;
    let currentUtterance = null;
    let speechRate = 1.0;

    const chapterSummarySpeechText = 
      "Welcome to Sujit Classes Master Notes for Class 8 Mathematics, Chapter 3: A Story of Numbers. " +
      "Counting began over 44,000 years ago during the Stone Age. Early humans etched tally notches onto bones like the Lebombo bone and Ishango bone to track lunar phases and livestock. " +
      "Human perception can only recognize up to 4 items at a glance, a phenomenon called subitizing. To count larger sets, diverse civilizations invented base systems. " +
      "Ancient Egypt built a base 10 system with 7 landmark hieroglyphs representing powers of 10. " +
      "Mesopotamia invented the base 60 sexagesimal place-value system, which still gives us 60 minutes in an hour and 360 degrees in a circle. " +
      "The Mayans developed a vertical base 20 system with a seashell zero placeholder. " +
      "Ancient China computed with bamboo rod numerals, alternating horizontal and vertical rods to prevent digits from merging. " +
      "Finally, ancient India created the ultimate masterpiece: the decimal place-value system with the digits 0 to 9. " +
      "Mathematicians like Aryabhata and Brahmagupta elevated zero to an autonomous algebraic number. " +
      "Transmitted through scholars like Al-Khwarizmi and Fibonacci, this Indian system became the universal language of global science, technology, and computing. " +
      "Study these notes thoroughly, review the solved exercises, and conquer your exams!";

    function toggleChapterAudio() {
      if (!synth) {
        alert("Sorry, your browser does not support the Web Speech Synthesis API.");
        return;
      }

      if (isPlayingAudio) {
        synth.cancel();
        isPlayingAudio = false;
        document.getElementById('audioIcon').className = 'fa-solid fa-volume-high';
        document.getElementById('audioStatusText').innerText = "Audio paused. Click play to resume listening.";
      } else {
        synth.cancel(); // clear previous queue
        currentUtterance = new SpeechSynthesisUtterance(chapterSummarySpeechText);
        currentUtterance.rate = speechRate;
        currentUtterance.pitch = 1.0;

        // Try to pick an English voice
        const voices = synth.getVoices();
        const engVoice = voices.find(v => v.lang.startsWith('en') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('India')));
        if (engVoice) currentUtterance.voice = engVoice;

        currentUtterance.onend = function() {
          isPlayingAudio = false;
          document.getElementById('audioIcon').className = 'fa-solid fa-volume-high';
          document.getElementById('audioStatusText').innerText = "Audio finished. Click to listen again.";
        };

        currentUtterance.onerror = function() {
          isPlayingAudio = false;
          document.getElementById('audioIcon').className = 'fa-solid fa-volume-high';
          document.getElementById('audioStatusText').innerText = "Audio playback interrupted. Click play to retry.";
        };

        synth.speak(currentUtterance);
        isPlayingAudio = true;
        document.getElementById('audioIcon').className = 'fa-solid fa-pause';
        document.getElementById('audioStatusText').innerText = "Speaking chapter master summary... Click pause anytime.";
      }
    }

    function updateSpeechRate() {
      const select = document.getElementById('speechRate');
      speechRate = parseFloat(select.value);
      if (isPlayingAudio) {
        toggleChapterAudio();
        toggleChapterAudio();
      }
    }
  </script>
</body>
</html>
"""
