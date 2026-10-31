# -*- coding: utf-8 -*-
"""
Module: ch4_section6_footer.py
Contains Section 6: Exam Hall Trap Alerts (5 common student blunders) & 15 Revision Points,
Back-to-Top button, footer, and interactive JavaScript engine (progress bar, quiz engine, TTS audio).
"""

def get_section_6_and_footer():
    return """
    <!-- SECTION 6: TRAP ALERTS & 15 REVISION POINTS -->
    <section id="section-6">
      <div class="section-header">
        <div class="section-tag"><i class="fa-solid fa-triangle-exclamation"></i> Exam Hall Survival Shield</div>
        <h2 class="section-title">Section 6: Exam Hall Trap Alerts (5 Student Blunders) &amp; 15 Revision Points</h2>
        <p class="section-desc">
          Arm yourself against the most frequent negative-marking traps and review the 15 golden conceptual takeaways before stepping into the examination hall.
        </p>
      </div>

      <!-- 5 EXAM HALL BLUNDERS -->
      <h3 class="subheading"><i class="fa-solid fa-skull-crossbones"></i> The 5 Most Fatal Student Blunders in Quadrilateral Exams</h3>

      <!-- BLUNDER 1 -->
      <div class="blunder-card">
        <div class="blunder-header">
          <i class="fa-solid fa-circle-xmark"></i> Blunder 1: The "Perpendicular Diagonals = Rhombus" Fallacy
        </div>
        <p>Students read <em>"Diagonals intersect at 90°"</em> and automatically write that the quadrilateral must be a Rhombus or Square.</p>
        <div class="blunder-comparison">
          <div class="bad-box">
            <strong><i class="fa-solid fa-xmark"></i> Fatal Exam Mistake:</strong><br>
            "Since diagonals AC ⊥ BD, ABCD is definitely a rhombus." (Loses marks!)
          </div>
          <div class="good-box">
            <strong><i class="fa-solid fa-check"></i> Topper's Precision:</strong><br>
            "A <strong>Kite</strong> also has perpendicular diagonals (AC ⊥ BD), but its adjacent sides are unequal in pairs and its diagonals do not mutually bisect! A quadrilateral is only a rhombus if the diagonals are <strong>perpendicular bisectors of each other</strong>."
          </div>
        </div>
      </div>

      <!-- BLUNDER 2 -->
      <div class="blunder-card">
        <div class="blunder-header">
          <i class="fa-solid fa-circle-xmark"></i> Blunder 2: The "Equal Diagonals = Square" Fallacy
        </div>
        <p>Assuming that equal diagonals (AC = BD) automatically guarantee a four-sided figure is a square.</p>
        <div class="blunder-comparison">
          <div class="bad-box">
            <strong><i class="fa-solid fa-xmark"></i> Fatal Exam Mistake:</strong><br>
            "The diagonals are equal (8 cm each), so the shape is a square."
          </div>
          <div class="good-box">
            <strong><i class="fa-solid fa-check"></i> Topper's Precision:</strong><br>
            "Equal bisecting diagonals define a <strong>Rectangle</strong>! Furthermore, an <strong>Isosceles Trapezium</strong> also has equal diagonals without even being a parallelogram! For a square, diagonals must be equal, bisecting, <strong>AND perpendicular (90°)</strong>."
          </div>
        </div>
      </div>

      <!-- BLUNDER 3 -->
      <div class="blunder-card">
        <div class="blunder-header">
          <i class="fa-solid fa-circle-xmark"></i> Blunder 3: Confusing Adjacent and Opposite Angles in Parallelograms
        </div>
        <p>Students accidentally equate adjacent angles instead of making them supplementary, or sum opposite angles to 180°.</p>
        <div class="blunder-comparison">
          <div class="bad-box">
            <strong><i class="fa-solid fa-xmark"></i> Fatal Exam Mistake:</strong><br>
            Writing: "Adjacent angles are equal, so (2x + 10) = (3x − 20)." (Zero marks!)
          </div>
          <div class="good-box">
            <strong><i class="fa-solid fa-check"></i> Topper's Precision:</strong><br>
            Remember the mnemonic: <strong>O-E &amp; A-S</strong>!<br>
            • <strong>Opposite angles are EQUAL</strong>: ∠A = ∠C and ∠B = ∠D.<br>
            • <strong>Adjacent angles are SUPPLEMENTARY</strong>: ∠A + ∠B = 180° and ∠B + ∠C = 180°.
          </div>
        </div>
      </div>

      <!-- BLUNDER 4 -->
      <div class="blunder-card">
        <div class="blunder-header">
          <i class="fa-solid fa-circle-xmark"></i> Blunder 4: The Concave Quadrilateral Angle Sum Misconception
        </div>
        <p>Believing that the 360° interior angle sum theorem fails when a quadrilateral is dart-shaped or has a reflex angle.</p>
        <div class="blunder-comparison">
          <div class="bad-box">
            <strong><i class="fa-solid fa-xmark"></i> Fatal Exam Mistake:</strong><br>
            "Angle sum is 360° only for convex shapes; for concave dart shapes it is different."
          </div>
          <div class="good-box">
            <strong><i class="fa-solid fa-check"></i> Topper's Precision:</strong><br>
            "Drawing internal diagonal BD always partitions ANY four-sided polygon into two non-overlapping triangles. Each triangle contributes 180°, so the sum is <strong>strictly 360° for every quadrilateral without exception</strong>!"
          </div>
        </div>
      </div>

      <!-- BLUNDER 5 -->
      <div class="blunder-card">
        <div class="blunder-header">
          <i class="fa-solid fa-circle-xmark"></i> Blunder 5: Over-Generalizing Kite Symmetry
        </div>
        <p>Assuming that in a kite, both pairs of opposite angles are equal or both diagonals bisect each other.</p>
        <div class="blunder-comparison">
          <div class="bad-box">
            <strong><i class="fa-solid fa-xmark"></i> Fatal Exam Mistake:</strong><br>
            "In kite ABCD, ∠B = ∠D and OA = OC, OB = OD."
          </div>
          <div class="good-box">
            <strong><i class="fa-solid fa-check"></i> Topper's Precision:</strong><br>
            "A kite has <strong>only ONE line of symmetry</strong>! Only the angles between unequal sides are equal (∠A = ∠C). The other pair is unequal (∠B ≠ ∠D). The main diagonal bisects the cross diagonal (AO = OC), but the cross diagonal does NOT bisect the main diagonal (OB ≠ OD)!"
          </div>
        </div>
      </div>

      <!-- 15 GOLDEN REVISION POINTS -->
      <h3 class="subheading"><i class="fa-solid fa-list-check"></i> 15 High-Yield Golden Revision Points for Toppers</h3>
      <div class="revision-grid">
        <div class="revision-card">
          <div class="rev-num">1</div>
          <div class="rev-text">
            <strong>Etymology &amp; Definition:</strong> <em>Quadri</em> (four) + <em>latus</em> (side). A closed 2D polygon bounded by 4 non-collinear segments with 4 vertices, 4 sides, 4 angles, and 2 diagonals.
          </div>
        </div>
        <div class="revision-card">
          <div class="rev-num">2</div>
          <div class="rev-text">
            <strong>Angle Sum Property:</strong> Interior angles always sum to <strong>360°</strong> [proof: (4 − 2) × 180° = 360° via diagonal triangulation]. Valid for convex &amp; concave quads.
          </div>
        </div>
        <div class="revision-card">
          <div class="rev-num">3</div>
          <div class="rev-text">
            <strong>The Rigidity Principle:</strong> Unlike triangles (which are rigid), four-sided frames are flexible linkages. A diagonal brace triangulates the interior to provide structural rigidity.
          </div>
        </div>
        <div class="revision-card">
          <div class="rev-num">4</div>
          <div class="rev-text">
            <strong>Carpenter's Problem Law:</strong> If two equal strips bisect each other at any arbitrary angle x, the taut thread joining their tips always forms a <strong>Rectangle</strong>.
          </div>
        </div>
        <div class="revision-card">
          <div class="rev-num">5</div>
          <div class="rev-text">
            <strong>Minimal Rectangle Definition:</strong> A rectangle can simply be defined as <em>a quadrilateral in which all four angles are 90°</em> (opposite sides are then proven equal via AAS).
          </div>
        </div>
        <div class="revision-card">
          <div class="rev-num">6</div>
          <div class="rev-text">
            <strong>Square Perfection:</strong> A square is the unique regular quadrilateral. It is simultaneously a rectangle, a rhombus, a parallelogram, a trapezium, and a kite.
          </div>
        </div>
        <div class="revision-card">
          <div class="rev-num">7</div>
          <div class="rev-text">
            <strong>Square Diagonal Signature:</strong> Diagonals of a square are <strong>equal</strong>, <strong>bisect each other at 90°</strong>, and <strong>bisect vertex angles into 45° each</strong>.
          </div>
        </div>
        <div class="revision-card">
          <div class="rev-num">8</div>
          <div class="rev-text">
            <strong>Parallelogram Definition:</strong> A quadrilateral with both pairs of opposite sides parallel (AB ∥ CD and AD ∥ BC).
          </div>
        </div>
        <div class="revision-card">
          <div class="rev-num">9</div>
          <div class="rev-text">
            <strong>Parallelogram Angle &amp; Side Rules:</strong> Opposite sides are equal (AB = CD), opposite angles are equal (∠A = ∠C), and adjacent angles are supplementary (∠A + ∠B = 180°).
          </div>
        </div>
        <div class="revision-card">
          <div class="rev-num">10</div>
          <div class="rev-text">
            <strong>Minimal Parallelogram Condition:</strong> If <strong>ONE pair</strong> of opposite sides of a quadrilateral is <strong>BOTH equal and parallel</strong>, it is guaranteed to be a parallelogram!
          </div>
        </div>
        <div class="revision-card">
          <div class="rev-num">11</div>
          <div class="rev-text">
            <strong>Rhombus Equilateral Nature:</strong> All 4 sides equal. Diagonals are <strong>perpendicular bisectors of each other</strong> and bisect the opposite vertex angles.
          </div>
        </div>
        <div class="revision-card">
          <div class="rev-num">12</div>
          <div class="rev-text">
            <strong>Trapezium Fundamentals:</strong> At least one pair of parallel opposite sides. Consecutive angles along non-parallel legs sum to 180° (∠P + ∠S = 180°).
          </div>
        </div>
        <div class="revision-card">
          <div class="rev-num">13</div>
          <div class="rev-text">
            <strong>Isosceles Trapezium:</strong> Non-parallel legs are equal (AD = BC). Proved via RHS congruence: <strong>base angles are equal (∠A = ∠B)</strong> and <strong>diagonals are equal (AC = BD)</strong>.
          </div>
        </div>
        <div class="revision-card">
          <div class="rev-num">14</div>
          <div class="rev-text">
            <strong>Kite Symmetry:</strong> Two pairs of equal adjacent sides (AB = AD, CB = CD). Main diagonal is perpendicular bisector of cross diagonal, bisects vertex angles, and has 1 axis of symmetry.
          </div>
        </div>
        <div class="revision-card">
          <div class="rev-num">15</div>
          <div class="rev-text">
            <strong>Midpoint Theorem Corollary:</strong> Joining the midpoints of the sides of a square creates an inner <strong>Square</strong> with exactly <strong>50% (half)</strong> the area of the outer square!
          </div>
        </div>
      </div>
    </section>

    <!-- FOOTER -->
    <footer>
      <p style="font-weight: 700; color: #f8fafc; font-size: 1.1rem; margin-bottom: 0.5rem;">
        Sujit Classes — Transforming School Education Across Odisha
      </p>
      <p style="margin-bottom: 1rem;">
        Dedicated to CBSE &amp; BSE Odisha Students | Master Study Notes for Class 8 Mathematics (Ganita Prakash NEP 2020)
      </p>
      <p style="font-size: 0.85rem; color: #64748b;">
        Crafted with zero omission, pedagogical excellence, and interactive learning tools.
        <br>&copy; 2026 Sujit Classes. All rights reserved.
      </p>
    </footer>

  </div> <!-- End .container -->

  <!-- BACK TO TOP BUTTON -->
  <button id="backToTopBtn" onclick="scrollToTop()" title="Go to top">
    <i class="fa-solid fa-arrow-up"></i>
  </button>

  <!-- INTERACTIVE JAVASCRIPT ENGINE -->
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
      if (answeredQuestions[qNum]) return; // prevent duplicate clicks
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
      document.getElementById('quizScoreDisplay').innerText = 'Score: ' + currentQuizScore + ' / 5';
    }

    // 3. INTERACTIVE WEB SPEECH API AUDIO READER
    let synth = window.speechSynthesis;
    let isPlayingAudio = false;
    let currentUtterance = null;
    let speechRate = 1.0;

    const chapterSummarySpeechText = 
      "Welcome to Sujit Classes Master Study Notes for Class 8 Mathematics, Chapter 4: Quadrilaterals. " +
      "The word quadrilateral comes from the Latin roots quadri meaning four, and latus meaning side. " +
      "Every planar quadrilateral has four vertices, four sides, four interior angles, and two diagonals. " +
      "The interior angle sum of any quadrilateral, whether convex or concave, is strictly 360 degrees, as proven by dividing the figure into two triangles with a single diagonal. " +
      "In the famous Carpenter's Problem, two equal wooden strips pinned at their midpoints always form a rectangle when their ends are joined by thread, regardless of the angle between them. " +
      "A rectangle has four 90-degree angles and equal bisecting diagonals. " +
      "A square is a special rectangle with all sides equal, whose diagonals bisect each other at right angles and cut corner angles into 45 degrees. " +
      "A parallelogram has both pairs of opposite sides parallel and equal, with opposite angles equal and adjacent angles adding to 180 degrees. " +
      "A rhombus has all four sides equal and diagonals intersecting perpendicularly at 90 degrees. " +
      "A kite has two pairs of equal adjacent sides and one axis of symmetry. " +
      "A trapezium has at least one pair of parallel sides, and an isosceles trapezium has equal non-parallel legs and equal diagonals. " +
      "Study these notes thoroughly, practice the proofs, and ace your mathematics examinations!";

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

        // Pick an English voice
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
