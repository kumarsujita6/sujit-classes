# -*- coding: utf-8 -*-
"""
Part 8: Section 6 - Exam Hall Trap Alerts (5 Common Student Blunders),
15 Bulletproof Flash Revision Points, Portal Footer, and
Complete Client-Side JavaScript Logic (Reading Progress, Quiz Engine, Audio Reader, Accordions).
"""

PART8_CONTENT = '''
    <!-- ========================================== -->
    <!-- SECTION 6: TRAP ALERTS & REVISION BANK    -->
    <!-- ========================================== -->
    <section class="section-block" id="section-6">
      <div class="section-header">
        <div class="section-title-wrap">
          <span class="section-tag"><i class="fa-solid fa-triangle-exclamation"></i> Exam Hall Survival</span>
          <h2 class="section-title">Section 6: Exam Hall Trap Alerts & 15 Revision Points</h2>
          <p class="section-desc">
            Common traps where top students lose marks, plus 15 bulletproof memory points to revise in 5 minutes right outside the examination hall.
          </p>
        </div>
      </div>

      <!-- FIVE COMMON STUDENT BLUNDERS -->
      <h3 class="subsection-title">
        <i class="fa-solid fa-bomb" style="color: #be123c;"></i>
        Five Common Student Blunders & Exam Traps
      </h3>

      <div style="display: flex; flex-direction: column; gap: 1.25rem; margin: 1.5rem 0;">
        <!-- TRAP 1 -->
        <div class="callout-box callout-warn">
          <div class="callout-title">
            <i class="fa-solid fa-circle-xmark"></i> Trap 1: The "Who Runs Panchayat Elections?" Blunder
          </div>
          <p><strong>The Common Mistake:</strong> Writing that the <em>Election Commission of India (ECI)</em> conducts Gram Panchayat, Sarpanch, and Municipal Ward elections.</p>
          <p><strong>Why Students Slip:</strong> Students assume that because ECI manages national elections, it must manage every single election in India.</p>
          <p><strong>The Correct Concept:</strong> Under Articles 243K and 243ZA, <strong>State Election Commissions (SECs)</strong>—which are distinct, independent constitutional bodies—conduct all local Panchayat and Municipality polls. The ECI only conducts Lok Sabha, Rajya Sabha, Vidhan Sabha, Vidhan Parishad, President, and Vice-President elections!</p>
        </div>

        <!-- TRAP 2 -->
        <div class="callout-box callout-warn">
          <div class="callout-title">
            <i class="fa-solid fa-circle-xmark"></i> Trap 2: The Reserved Constituency Voting Misconception
          </div>
          <p><strong>The Common Mistake:</strong> Answering that in an SC-reserved or ST-reserved Lok Sabha constituency, <em>only citizens belonging to the SC or ST community</em> are allowed to cast votes.</p>
          <p><strong>Why Students Slip:</strong> Confusing modern reserved constituencies with pre-Independence British "Separate Electorates".</p>
          <p><strong>The Correct Concept:</strong> In an SC/ST reserved constituency, <strong>every registered adult citizen (general, OBC, SC, ST) votes on the exact same common roll</strong>! The only restriction is that the <strong>candidate standing for election must belong to the reserved SC or ST community</strong>.</p>
        </div>

        <!-- TRAP 3 -->
        <div class="callout-box callout-warn">
          <div class="callout-title">
            <i class="fa-solid fa-circle-xmark"></i> Trap 3: The "EVMs are Connected to Wi-Fi / Satellite" Myth
          </div>
          <p><strong>The Common Mistake:</strong> Claiming in exams that EVMs transmit votes to Nirvachan Sadan via internet servers or cellular data.</p>
          <p><strong>Why Students Slip:</strong> Confusing computer polling machines with modern mobile apps or online banking.</p>
          <p><strong>The Correct Concept:</strong> Indian Electronic Voting Machines (developed by BEL & ECIL) are <strong>100% standalone, battery-operated embedded hardware</strong>. They possess <em>zero internet, Bluetooth, cellular, or Wi-Fi circuitry</em>. They cannot be remotely hacked!</p>
        </div>

        <!-- TRAP 4 -->
        <div class="callout-box callout-warn">
          <div class="callout-title">
            <i class="fa-solid fa-circle-xmark"></i> Trap 4: The "50% Majority" Trap in FPTP Elections
          </div>
          <p><strong>The Common Mistake:</strong> Writing that a candidate must win more than 50% of total votes to become an MP or MLA.</p>
          <p><strong>Why Students Slip:</strong> Confusing an absolute majority in Parliament (to form a government) with the vote share in an individual constituency.</p>
          <p><strong>The Correct Concept:</strong> Under the <strong>First-Past-The-Post (FPTP)</strong> system, a candidate simply needs <em>more votes than any other individual opponent</em> (a plurality). If a candidate gets 32% while others get 30%, 25%, and 13%, the candidate with 32% wins!</p>
        </div>

        <!-- TRAP 5 -->
        <div class="callout-box callout-warn">
          <div class="callout-title">
            <i class="fa-solid fa-circle-xmark"></i> Trap 5: The Presidential Electoral College Nominated Trap
          </div>
          <p><strong>The Common Mistake:</strong> Including the 12 nominated members of the Rajya Sabha in the Presidential Electoral College.</p>
          <p><strong>Why Students Slip:</strong> Forgetting the crucial distinction between "all members" and "elected members".</p>
          <p><strong>The Correct Concept:</strong> Only <strong>ELECTED</strong> members of Lok Sabha, Rajya Sabha, and State Legislative Assemblies can vote for the President. Nominated members (and all Legislative Council MLCs) are strictly excluded!</p>
        </div>
      </div>

      <!-- 15 BULLETPROOF REVISION POINTS -->
      <h3 class="subsection-title">
        <i class="fa-solid fa-bolt" style="color: #b45309;"></i>
        15 Bulletproof Flash Revision Points
      </h3>

      <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: var(--radius-lg); padding: 1.5rem; margin: 1.5rem 0;">
        <ol style="padding-left: 1.3rem; margin: 0; display: flex; flex-direction: column; gap: 0.65rem; font-size: 0.94rem;">
          <li><strong>Universal Adult Franchise:</strong> Enshrined in <strong>Article 326</strong>; gives every Indian citizen aged 18+ equal voting rights without discrimination.</li>
          <li><strong>Voting Age Milestone:</strong> Reduced from <strong>21 to 18 years</strong> by the <strong>61st Constitutional Amendment Act, 1988</strong> (effective 1989).</li>
          <li><strong>Ambedkar\'s Vision:</strong> Establishes political democracy based on the sacred principle of <em>"one person, one vote, one value"</em>.</li>
          <li><strong>No Proxy Voting:</strong> Voting is personal and non-transferable; no citizen can vote on another\'s behalf.</li>
          <li><strong>Global Contrast:</strong> India granted women equal voting in 1950 from Day 1; Switzerland only gave women federal voting rights in 1971!</li>
          <li><strong>Ancient Democracy:</strong> The 10th-century Chola <strong>Uttaramerur inscriptions</strong> document the transparent <em>Kudavolai</em> (pot ticket) system with strict anti-corruption disqualifications.</li>
          <li><strong>Election Commission of India (ECI):</strong> Autonomous constitutional powerhouse established under <strong>Article 324</strong>, based at <em>Nirvachan Sadan</em>, New Delhi.</li>
          <li><strong>ECI Leadership:</strong> Led by the <strong>Chief Election Commissioner (CEC)</strong> and two Election Commissioners.</li>
          <li><strong>Administrative Hierarchy:</strong> National ECI → State CEO → District DEO (Collector) → Constituency RO → Polling Booth Presiding Officer.</li>
          <li><strong>Lok Sabha Scale:</strong> <strong>543 Constituencies</strong> (412 General, <strong>84 SC</strong> reserved, <strong>47 ST</strong> reserved); 2024 electorate: <strong>968.8 Million voters</strong>.</li>
          <li><strong>First-Past-The-Post (FPTP):</strong> The candidate securing the highest individual votes in a constituency wins, even without securing 50% of the total vote.</li>
          <li><strong>Secret Ballot & NOTA:</strong> Ensures voter privacy against coercion; NOTA (introduced in 2013) allows voters to reject all candidates secretly.</li>
          <li><strong>EVM & VVPAT:</strong> Standalone battery-operated voting machines; VVPAT displays a printed paper audit slip for <strong>7 seconds</strong> before dropping into a sealed box.</li>
          <li><strong>Model Code of Conduct (MCC):</strong> Voluntary code born in Kerala (1960); comes into effect the moment ECI announces poll dates; bans voter bribery, cash gifts, and misuse of official machinery.</li>
          <li><strong>T.N. Seshan Legacy:</strong> 10th CEC (1990–1996) who introduced Voter Photo Identity Cards (EPIC), enforced the MCC fearlessly, and stamped out booth capturing.</li>
        </ol>
      </div>
    </section>

  </main>

  <!-- Portal Footer -->
  <footer style="background: #0f172a; color: #94a3b8; padding: 3rem 1.5rem 2.5rem; border-top: 3px solid #1e3a8a; text-align: center; font-size: 0.9rem;">
    <div style="max-width: 1100px; margin: 0 auto;">
      <div style="display: flex; align-items: center; justify-content: center; gap: 0.75rem; margin-bottom: 1rem;">
        <i class="fa-solid fa-landmark-dome" style="color: #fbbf24; font-size: 1.5rem;"></i>
        <span style="color: #ffffff; font-family: 'Space Grotesk', sans-serif; font-size: 1.3rem; font-weight: 700;">Sujit Classes Digital Study Portal</span>
      </div>
      <p style="margin-bottom: 1.25rem; color: #cbd5e1; max-width: 750px; margin-left: auto; margin-right: auto;">
        Dedicated to empowering students of Odisha (CBSE & BSE) with exhaustive, crystal-clear, and visually rich academic master notes aligned with NEP 2020.
      </p>
      <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 1.5rem; margin-bottom: 1.5rem; font-weight: 600;">
        <a href="../../index.html" style="color: #60a5fa; text-decoration: none;">Portal Home</a>
        <a href="#section-1" style="color: #60a5fa; text-decoration: none;">Section 1: Blueprint</a>
        <a href="#section-2" style="color: #60a5fa; text-decoration: none;">Section 2: Concepts</a>
        <a href="#section-3" style="color: #60a5fa; text-decoration: none;">Section 3: Fact Bank</a>
        <a href="#section-4" style="color: #60a5fa; text-decoration: none;">Section 4: NCERT Solutions</a>
        <a href="#section-5" style="color: #60a5fa; text-decoration: none;">Section 5: Exam Bank</a>
        <a href="#section-6" style="color: #60a5fa; text-decoration: none;">Section 6: Trap Alerts</a>
      </div>
      <p style="font-size: 0.8rem; color: #64748b; margin: 0;">
        © Sujit Classes • Class 8 Social Science • Chapter 5: Universal Franchise and India\'s Electoral System (NCERT NEP code: hess105).
      </p>
    </div>
  </footer>

  <!-- ========================================== -->
  <!-- CLIENT-SIDE INTERACTIVE JAVASCRIPT LOGIC   -->
  <!-- ========================================== -->
  <script>
    // 1. Reading Progress Bar Controller
    window.addEventListener('scroll', function() {
      const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      const progressBar = document.getElementById('reading-progress-bar');
      if (progressBar) {
        progressBar.style.width = scrolled + '%';
      }
    });

    // 2. Interactive Quiz Engine Logic
    let currentScore = 0;
    const answeredQuestions = new Set();

    function checkAnswer(questionNum, selectedOptionIndex, isCorrect) {
      if (answeredQuestions.has(questionNum)) return;
      answeredQuestions.add(questionNum);

      const card = document.getElementById('mcq-card-' + questionNum);
      if (!card) return;

      const buttons = card.querySelectorAll('.quiz-opt-btn');
      const feedback = document.getElementById('feedback-' + questionNum);

      // Disable all option buttons for this question
      buttons.forEach(btn => btn.disabled = true);

      if (isCorrect) {
        buttons[selectedOptionIndex].classList.add('correct');
        buttons[selectedOptionIndex].innerHTML += ' <i class="fa-solid fa-circle-check" style="color:#16a34a; margin-left:auto;"></i>';
        if (feedback) feedback.classList.add('show', 'correct-feedback');
        currentScore++;
      } else {
        buttons[selectedOptionIndex].classList.add('incorrect');
        buttons[selectedOptionIndex].innerHTML += ' <i class="fa-solid fa-circle-xmark" style="color:#dc2626; margin-left:auto;"></i>';
        if (feedback) feedback.classList.add('show', 'incorrect-feedback');

        // Automatically reveal the correct option
        buttons.forEach((btn, idx) => {
          if ((questionNum === 1 && idx === 1) ||
              (questionNum === 2 && idx === 2) ||
              (questionNum === 3 && idx === 1) ||
              (questionNum === 4 && idx === 1) ||
              (questionNum === 5 && idx === 2)) {
            btn.classList.add('correct');
            btn.innerHTML += ' <i class="fa-solid fa-check" style="color:#16a34a; margin-left:auto;"></i>';
          }
        });
      }

      // Update score display
      const scoreElem = document.getElementById('quiz-score');
      if (scoreElem) {
        scoreElem.textContent = currentScore;
      }
    }

    // 3. Smart Audio Reader Companion (SpeechSynthesis)
    let isSpeaking = false;
    let synth = window.speechSynthesis;
    let utterance = null;

    const audioScriptText = "Welcome to Sujit Classes master study note for Class 8 Social Science: Universal Franchise and India\'s Electoral System. " +
      "Universal Adult Franchise, enshrined under Article 326 of our Constitution, means every Indian citizen aged 18 and above has one vote, and all votes have equal value. " +
      "In 1988, the 61st Constitutional Amendment lowered the voting age from 21 to 18 years, empowering youth. " +
      "While Western countries made women fight for decades, India granted equal voting rights to men and women right from Day One in 1950, despite an initial literacy rate of just 14 percent. " +
      "Our ancient roots trace back to the 10th-century Chola Uttaramerur inscriptions, which describe the transparent Kudavolai pot ticket system. " +
      "Under Article 324, the independent Election Commission of India conducts free and fair elections for 968 million voters across 543 Lok Sabha constituencies. " +
      "To ensure fair play, the Model Code of Conduct bans bribery, cash gifts, hate speech, and the misuse of government machinery. " +
      "On election day, voters use secure Electronic Voting Machines and VVPAT audit trail printers with total secrecy. " +
      "Citizens directly elect 543 Lok Sabha MPs and State MLAs using the First-Past-The-Post system, while Rajya Sabha MPs and the President of India are chosen through indirect elections. " +
      "By practicing vigilant, informed voting and utilizing apps like c-VIGIL, every citizen protects the world\'s largest democratic festival!";

    function toggleAudioReader() {
      if (!('speechSynthesis' in window)) {
        alert('Sorry! Your browser does not support text-to-speech synthesis.');
        return;
      }

      if (isSpeaking) {
        synth.pause();
        isSpeaking = false;
        updateAudioButtonUI(false, true);
      } else {
        if (synth.paused) {
          synth.resume();
          isSpeaking = true;
          updateAudioButtonUI(true, false);
        } else {
          utterance = new SpeechSynthesisUtterance(audioScriptText);
          utterance.rate = 0.95;
          utterance.pitch = 1.0;
          utterance.lang = 'en-IN';

          utterance.onend = function() {
            isSpeaking = false;
            updateAudioButtonUI(false, false);
          };

          utterance.onerror = function() {
            isSpeaking = false;
            updateAudioButtonUI(false, false);
          };

          synth.speak(utterance);
          isSpeaking = true;
          updateAudioButtonUI(true, false);
        }
      }
    }

    function stopAudioReader() {
      if (synth) {
        synth.cancel();
        isSpeaking = false;
        updateAudioButtonUI(false, false);
      }
    }

    function updateAudioButtonUI(playing, paused) {
      const mainBtn = document.getElementById('btn-audio-main');
      const navBtn = document.getElementById('btn-audio-nav');
      const mainText = document.getElementById('audio-btn-main-text');
      const navText = document.getElementById('audio-btn-nav-text');

      if (playing) {
        if (mainText) mainText.textContent = 'Pause Summary';
        if (navText) navText.textContent = 'Pause';
        if (mainBtn) mainBtn.innerHTML = '<i class="fa-solid fa-pause"></i> <span id="audio-btn-main-text">Pause Summary</span>';
        if (navBtn) navBtn.classList.add('playing');
      } else if (paused) {
        if (mainText) mainText.textContent = 'Resume Summary';
        if (navText) navText.textContent = 'Resume';
        if (mainBtn) mainBtn.innerHTML = '<i class="fa-solid fa-play"></i> <span id="audio-btn-main-text">Resume Summary</span>';
        if (navBtn) navBtn.classList.remove('playing');
      } else {
        if (mainText) mainText.textContent = 'Play Audio Summary';
        if (navText) navText.textContent = 'Listen Summary';
        if (mainBtn) mainBtn.innerHTML = '<i class="fa-solid fa-play"></i> <span id="audio-btn-main-text">Play Audio Summary</span>';
        if (navBtn) navBtn.classList.remove('playing');
      }
    }

    // 4. Expand / Collapse All Details in a Section
    function toggleAllDetails(sectionId) {
      const section = document.getElementById(sectionId);
      if (!section) return;
      const detailsList = section.querySelectorAll('details.ans-box');
      if (detailsList.length === 0) return;

      const anyClosed = Array.from(detailsList).some(d => !d.open);
      detailsList.forEach(d => d.open = anyClosed);
    }
  </script>
</body>
</html>
'''
