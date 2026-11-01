# -*- coding: utf-8 -*-
"""
Section 6 Module: Exam Hall Trap Alerts, 15 Revision Points & Interactive Scripts
Class 8 Mathematics Chapter 12: Tales by Dots and Lines (NCERT NEP code: hegp112)
"""

def get_section_6():
    return """
    <!-- SECTION 6: EXAM HALL TRAPS & 15 REVISION POINTS -->
    <section id="section6" class="section-box">
      <div class="section-header">
        <div class="section-header-left">
          <span class="section-tag">Score Maximizer</span>
          <h2 class="section-title">§ 6. Exam Hall Trap Alerts &amp; 15 High-Yield Revision Points</h2>
          <p class="section-desc">
            Learn to recognize the 5 most fatal student blunders that cost marks in board and talent examinations, followed by 15 crisp, high-yield summary points for 5-minute pre-exam revision.
          </p>
        </div>
        <div>
          <span class="badge badge-gold"><i class="fa-solid fa-triangle-exclamation"></i> 0% Error Goal</span>
        </div>
      </div>

      <!-- 5 COMMON STUDENT BLUNDERS & TRAP ALERTS -->
      <div style="margin-bottom: 2.5rem;">
        <h3 style="font-family: 'Space Grotesk', sans-serif; font-size: 1.4rem; color: var(--primary-dark); margin-bottom: 1.25rem;">
          <i class="fa-solid fa-skull-crossbones"></i> 5 Common Exam Hall Student Blunders
        </h3>

        <!-- Trap 1 -->
        <div class="callout callout-warn">
          <div class="callout-title"><i class="fa-solid fa-triangle-exclamation"></i> Blunder 1: Dividing by Category Count Instead of &Sigma;f in Frequency Tables</div>
          <p>
            <strong>The Student Blunder:</strong> When given a table of family sizes (3, 4, 5, 6, 7, 8, 9, 10) with frequencies, a student simply counts 8 rows and computes <span class="math-inline">Average = (3+4+5+6+7+8+9+10)/8 = 52/8 = 6.5</span>.
            <br><strong>Why It Loses Marks:</strong> This ignores frequency completely! It assumes there is only 1 family of size 4, whereas in reality there are 11 families of size 4! You cannot treat high-frequency scores the same as rare scores.
            <br><strong>Correct Exam Strategy:</strong> Always compute the weighted sum <span class="math-inline">&Sigma; (f_i &middot; x_i)</span> and divide by the total number of students/families <span class="math-inline">N = &Sigma; f_i</span>.
            <div class="math-block">x̄ = (&Sigma; (f_i &middot; x_i)) / (&Sigma; f_i) = (188) / (36) &approx; <strong>5.22</strong></div>
          </p>
        </div>

        <!-- Trap 2 -->
        <div class="callout callout-warn">
          <div class="callout-title"><i class="fa-solid fa-triangle-exclamation"></i> Blunder 2: Adding the New Value Directly to the Old Average</div>
          <p>
            <strong>The Student Blunder:</strong> A batsman has an average of 40 runs across 9 innings. In the 10th innings, he scores 60 runs. A student thinks: <em>"New average = (40 + 60)/2 = 50 runs!"</em>
            <br><strong>Why It Loses Marks:</strong> The old average of 40 represents <strong>9 separate innings</strong> (a total of 360 runs), while 60 is just <strong>1 innings</strong>! You cannot give 1 innings equal weight to 9 innings combined.
            <br><strong>Correct Exam Strategy:</strong> Always revert to total sums or use the incremental deviation formula:
            <div class="math-block">
              Total Runs = (40 &times; 9) + 60 = 360 + 60 = 420<br>
              New Average = (420) / (10) = <strong>42  runs</strong> &nbsp;&nbsp;&nbsp;&nbsp;&le;ft[Or:  40 + (60 - 40) / (10) = 40 + 2 = 42]
            </div>
          </p>
        </div>

        <!-- Trap 3 -->
        <div class="callout callout-warn">
          <div class="callout-title"><i class="fa-solid fa-triangle-exclamation"></i> Blunder 3: Assuming the Median Explodes When an Outlier is Added</div>
          <p>
            <strong>The Student Blunder:</strong> Assuming that adding a massive number (like ₹1,00,00,000) causes both the mean and the median to skyrocket.
            <br><strong>Why It Loses Marks:</strong> The median is purely a <strong>positional rank indicator</strong>. Whether the largest number in a 5-person dataset is 20 or 20,000,000, it still occupies the exact same single position at the extreme right end!
            <br><strong>Correct Exam Strategy:</strong> Remember that <strong>Mean is sensitive</strong> to magnitudes, but <strong>Median is robust and immune</strong> to outliers.
          </p>
        </div>

        <!-- Trap 4 -->
        <div class="callout callout-warn">
          <div class="callout-title"><i class="fa-solid fa-triangle-exclamation"></i> Blunder 4: Falling for Truncated (Compressed) Y-Axes on Line Graphs</div>
          <p>
            <strong>The Student Blunder:</strong> Looking at a line graph where the Y-axis starts at 980 instead of 0, seeing a steep upward cliff, and concluding that sales have increased five-fold.
            <br><strong>Why It Loses Marks:</strong> Truncating the axis magnifies tiny percentage changes into dramatic visual cliffs. A change from 990 to 1010 looks massive if the baseline is 980, but it is actually only a tiny 2% increase!
            <br><strong>Correct Exam Strategy:</strong> Always check the origin: <strong>Does the Y-axis start at zero?</strong> If not, look at the numerical labels, calculate <span class="math-inline">&Delta; y / y_{initial} &times; 100%</span>, and never judge magnitude by visual height alone.
          </p>
        </div>

        <!-- Trap 5 -->
        <div class="callout callout-warn">
          <div class="callout-title"><i class="fa-solid fa-triangle-exclamation"></i> Blunder 5: Confusing "Sunset Time" with "Day Length" on Solar Graphs</div>
          <p>
            <strong>The Student Blunder:</strong> When asked to find the place with the longest day length, a student looks only for the highest peak on the sunset curve.
            <br><strong>Why It Loses Marks:</strong> Day length is <strong>NOT</strong> sunset time! Day length is the <em>duration of daylight</em>, which equals:
            <div class="math-block">Day Length = Sunset Time - Sunrise Time</div>
            A place where sun sets at 7:00 PM but rose at 7:00 AM has only 12 hours of light. Another place where sun sets at 6:30 PM but rose at 4:30 AM has 14 hours of light!
            <br><strong>Correct Exam Strategy:</strong> Measure the <strong>vertical distance between the top (sunset) and bottom (sunrise) lines</strong> at that date to determine true photoperiod day length.
          </p>
        </div>
      </div>

      <!-- 15 HIGH-YIELD REVISION POINTS -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-list-check"></i> 15 High-Yield Rapid Revision Points</h3>
        <ol style="margin-left: 1.5rem; line-height: 2; font-size: 0.95rem; color: var(--text-main);">
          <li><strong>The Physical Fulcrum:</strong> The arithmetic mean is the unique center of gravity of a dataset on a number line where the sum of leftward distances equals the sum of rightward distances: <span class="math-inline">&Sigma; (x_i - x̄) = 0</span>.</li>
          <li><strong>Uniqueness of Mean:</strong> There is exactly one balance point for any collection of data. Shifting the candidate center to the right strictly increases LHS distance while decreasing RHS distance, destroying balance.</li>
          <li><strong>Inclusion Dynamics:</strong> Adding a value greater than the mean increases the mean; adding a value less than the mean decreases it; adding a value equal to the mean leaves it unchanged.</li>
          <li><strong>Removal Dynamics:</strong> Removing a value above the mean decreases the mean; removing a value below the mean increases it; removing a value equal to the mean leaves it unchanged.</li>
          <li><strong>Unchanging Mean Principle:</strong> Multiple values can be added or removed without altering the mean if and only if their net deviation from the mean sums to zero: <span class="math-inline">&Sigma; (x_{new} - x̄) = 0</span>.</li>
          <li><strong>Linear Shifting Invariant:</strong> Adding or subtracting a constant <span class="math-inline">c</span> to every observation shifts the mean by exactly <span class="math-inline">c</span>: <span class="math-inline">x̄' = x̄ &plusmn; c</span>. Geometrically, the entire dot plot slides rigidly without distortion.</li>
          <li><strong>Uniform Scaling Invariant:</strong> Multiplying or dividing every observation by a non-zero constant <span class="math-inline">k</span> scales the mean by <span class="math-inline">k</span>: <span class="math-inline">x̄' = k &middot; x̄</span>.</li>
          <li><strong>Median Calculation:</strong> For odd <span class="math-inline">N</span>, median is the <span class="math-inline">(N+1) / (2)</span>-th sorted value. For even <span class="math-inline">N</span>, it is the average of the <span class="math-inline">(N) / (2)</span>-th and <span class="math-inline">((N) / (2) + 1)</span>-th sorted values.</li>
          <li><strong>Outlier Resilience:</strong> While the arithmetic mean is sensitive to extreme values, the median is robust and immune to outliers because it depends solely on rank order.</li>
          <li><strong>Weighted Mean Formula:</strong> In frequency distributions, the mean is <span class="math-inline">x̄ = (&Sigma; f_i x_i) / (&Sigma; f_i)</span>. Never divide by the number of categories!</li>
          <li><strong>Cumulative Frequency Ranking:</strong> To find the median in frequency tables, construct a cumulative frequency (<span class="math-inline">cf</span>) column and locate the group containing the median rank.</li>
          <li><strong>Spreadsheet Formulas:</strong> Digital calculations use reactive formulas beginning with '=': <span class="math-inline">=SUM(Start:End)</span> sums a range; <span class="math-inline">=AVERAGE(Start:End)</span> computes the mean.</li>
          <li><strong>Line Graphs for Time Series:</strong> Line graphs connect discrete chronological points to display continuous trends. The steepness (slope) of a line segment directly represents the rate of change over time.</li>
          <li><strong>Activity Strips:</strong> A 24-hour day can be mapped into 48 half-hour boxes to visually analyze time allocation across sleep, study, meals, travel, and play.</li>
          <li><strong>Nash's Hex Theorem:</strong> In the Game of Hex on an 11 &times; 11 rhombus board, a draw is topologically impossible; exactly one player is guaranteed to complete an unbroken connecting path.</li>
        </ol>
      </div>
    </section>
  </main>

  <!-- FOOTER -->
  <footer class="footer">
    <div style="max-width: 1200px; margin: 0 auto;">
      <p style="font-weight: 700; color: #ffffff; font-size: 1.1rem; margin-bottom: 0.5rem;">Sujit Classes Study Portal • Master Study Notes</p>
      <p style="margin-bottom: 1rem;">NCERT Ganita Prakash Grade 8 Part-II • Chapter 12: Tales by Dots and Lines (hegp112)</p>
      <p style="font-size: 0.8rem; color: #64748b;">
        Crafted with zero omissions, bilingual terminology, responsive SVGs, and interactive learning tools for CBSE and BSE Odisha middle school students.
      </p>
      <div style="margin-top: 1.5rem;">
        <a href="../../index.html"><i class="fa-solid fa-arrow-left"></i> Return to Study Portal Home</a>
      </div>
    </div>
  </footer>

  <!-- ==========================================================
       CLIENT-SIDE JAVASCRIPT: PROGRESS BAR, TTS & QUIZ ENGINE
       ========================================================== -->
  <script>
    // 1. Reading Progress Bar
    window.addEventListener('scroll', () => {
      const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      document.getElementById('progressBar').style.width = scrolled + '%';
    });

    // 2. Audio Reader (Text-to-Speech)
    let isSpeaking = false;
    let synth = window.speechSynthesis;
    let speechUtterance = null;

    const summaryText = "Welcome to Chapter 12: Tales by Dots and Lines. In this chapter, we discover that the arithmetic mean is the physical fulcrum or balance point of a dataset on a number line. The sum of distances to the left of the mean exactly equals the sum of distances to the right. When every value in a dataset is increased by a constant, the mean increases by that same constant. When values are multiplied by a factor, the mean scales proportionally. While the mean is sensitive to every single data point, the median is robust against extreme outliers. We also learn how to calculate weighted averages from frequency tables, use digital spreadsheet formulas like SUM and AVERAGE, and interpret real-world trends using line graphs, activity strips, and the Game of Hex.";

    function toggleAudioReader() {
      if (!('speechSynthesis' in window)) {
        alert("Sorry, your browser does not support Web Speech Text-to-Speech!");
        return;
      }

      const btn = document.getElementById('ttsPlayBtn');
      const icon = document.getElementById('ttsIcon');
      const status = document.getElementById('ttsStatus');

      if (synth.speaking && !synth.paused) {
        synth.pause();
        icon.className = "fa-solid fa-play";
        btn.innerHTML = '<i class="fa-solid fa-play"></i> Resume Reading';
        status.innerText = "Audio paused. Click to resume listening.";
        isSpeaking = false;
      } else if (synth.paused) {
        synth.resume();
        icon.className = "fa-solid fa-pause";
        btn.innerHTML = '<i class="fa-solid fa-pause"></i> Pause Reading';
        status.innerText = "Listening to Chapter 12 audio summary...";
        isSpeaking = true;
      } else {
        synth.cancel();
        speechUtterance = new SpeechSynthesisUtterance(summaryText);
        const rateSelect = document.getElementById('ttsRate');
        speechUtterance.rate = parseFloat(rateSelect.value) || 1.0;
        speechUtterance.pitch = 1.0;

        speechUtterance.onend = function() {
          btn.innerHTML = '<i class="fa-solid fa-play"></i> Listen to Summary';
          status.innerText = "Audio summary complete. Click to listen again.";
          isSpeaking = false;
        };

        speechUtterance.onerror = function() {
          btn.innerHTML = '<i class="fa-solid fa-play"></i> Listen to Summary';
          status.innerText = "Error playing audio. Please try again.";
          isSpeaking = false;
        };

        synth.speak(speechUtterance);
        btn.innerHTML = '<i class="fa-solid fa-pause"></i> Pause Reading';
        status.innerText = "Listening to Chapter 12 audio summary...";
        isSpeaking = true;
      }
    }

    function updateSpeechRate() {
      if (isSpeaking && speechUtterance) {
        toggleAudioReader();
        toggleAudioReader();
      }
    }

    // 3. Interactive Quiz Engine
    let userScore = 0;
    const answeredQuestions = new Set();

    const explanations = {
      1: "Correct! By Theorem 1 (Shifting), adding 7 makes the mean 45 + 7 = 52. By Theorem 2 (Scaling), multiplying by 2 doubles the mean: 52 &times; 2 = 104! TRAP: Simply multiplying 45 &times; 2 and forgetting to double the 7 gives 97, which is a classic error.",
      2: "Correct! Leftward distances from 18: (18 - 12) + (18 - 14) = 6 + 4 = 10. Rightward distance from 18 of known points: (22 - 18) = 4. The point at 18 contributes 0 distance. To balance 10 on the left, the right side needs 10 - 4 = 6 more units of distance! Hence x = 18 + 6 = 24.",
      3: "Correct! Total students N = 2 + 5 + 8 + 5 = 20 (even). Median is average of 10th and 11th values. Cumulative frequencies: Score 10 has cf = 2; Score 20 has cf = 7; Score 30 has cf = 15. Since positions 8 through 15 are all Score 30, both the 10th and 11th values are 30! Hence Median = 30.",
      4: "Correct! In spreadsheet applications (Excel, Google Sheets), the standard formula to compute arithmetic mean across a contiguous range is =AVERAGE(Start:End), written here as =AVERAGE(C4:C9). Note that =MEAN is not a valid spreadsheet function.",
      5: "Correct! On any time-series line graph, the steepness or slope (&Delta;y / &Delta;x) represents the rate of change per unit of time. A steeper positive slope directly indicates that temperature was surging at a much faster rate during that interval."
    };

    function checkMCQ(qNum, selectedOpt, isCorrect) {
      const card = document.getElementById('mcqCard' + qNum);
      const evalBox = document.getElementById('evalBox' + qNum);
      const buttons = card.querySelectorAll('.opt-btn');

      // Disable buttons for this question
      buttons.forEach(btn => {
        btn.disabled = true;
        if (btn.innerText.includes('(' + selectedOpt + ')')) {
          if (isCorrect) {
            btn.classList.add('correct');
          } else {
            btn.classList.add('wrong');
          }
        }
      });

      if (isCorrect) {
        evalBox.className = "eval-box correct";
        evalBox.innerHTML = '<i class="fa-solid fa-circle-check"></i> <strong>Spot On!</strong> ' + explanations[qNum];
        if (!answeredQuestions.has(qNum)) {
          userScore++;
        }
      } else {
        evalBox.className = "eval-box wrong";
        evalBox.innerHTML = '<i class="fa-solid fa-circle-xmark"></i> <strong>Incorrect Choice!</strong> ' + explanations[qNum];
      }

      answeredQuestions.add(qNum);
      document.getElementById('currentScore').innerText = userScore;
    }
  </script>
</body>
</html>
"""
