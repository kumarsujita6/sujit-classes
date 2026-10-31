# -*- coding: utf-8 -*-
"""Part 7: Section 5 - Complete Exam Question Bank for Class 8 Science Ch 11."""

PART7_CONTENT = """
    <!-- ========================================== -->
    <!-- SECTION 5: COMPLETE EXAM QUESTION BANK    -->
    <!-- ========================================== -->
    <section id="section-5" class="study-section">
      <div class="section-badge"><i class="fa-solid fa-graduation-cap"></i> Section 5 • Question Bank</div>
      <h2 class="section-title">Complete Exam Question Bank (27 CBE &amp; Board Models)</h2>
      <p class="section-description">
        Engineered according to CBSE Competency-Based Education (CBE) standards. Includes an interactive real-time score-evaluating MCQ quiz engine, assertion-reasoning items, differentiated 2M/3M short answers, 5M long answers with official marking schemes, data-driven case studies, and previous years' board questions.
      </p>

      <!-- ========================================== -->
      <!-- SUBSECTION 5.1: INTERACTIVE MCQS (5)       -->
      <!-- ========================================== -->
      <h3 class="sub-title"><i class="fa-solid fa-circle-question" style="color: #0284c7;"></i> 5.1 Conceptual Multiple-Choice Questions (Interactive Quiz Engine)</h3>
      
      <!-- Quiz Score Banner -->
      <div class="quiz-score-banner">
        <div>
          <h4 style="font-family:'Space Grotesk',sans-serif; margin-bottom:0.25rem;"><i class="fa-solid fa-trophy"></i> Test Your Celestial Mastery!</h4>
          <p style="font-size:0.88rem; opacity:0.9; margin-bottom:0;">Click your chosen answer to get instant feedback and see hidden traps explained.</p>
        </div>
        <div style="text-align:right;">
          <span style="font-size:0.8rem; text-transform:uppercase; letter-spacing:0.5px; opacity:0.8;">Current Score</span>
          <div id="quiz-score-display" style="font-family:'Space Grotesk',sans-serif; font-size:1.6rem; font-weight:800;">0 / 5</div>
        </div>
      </div>

      <!-- MCQ 1 -->
      <div class="mcq-card">
        <div class="mcq-question">
          Q1. An observer wakes up at sunrise (6:00 AM) and spots a half-illuminated Moon directly overhead in the sky. Which lunar phase is this, and which side of the Moon appears illuminated to the observer?
        </div>
        <div class="mcq-options">
          <button class="mcq-btn" onclick="checkMCQ(this, false, 'q1', 'First Quarter is overhead at SUNSET (6:00 PM), not sunrise! Remember: Waxing phases are evening objects.')">
            <span>A) First Quarter, illuminated on the western (right) side</span>
          </button>
          <button class="mcq-btn" onclick="checkMCQ(this, true, 'q1', 'Brilliant! At sunrise, the Sun is in the East. An overhead Moon is 90° West of the Sun. This is the Third (Last) Quarter, illuminated on its eastern (left) side facing the morning Sun!')">
            <span>B) Third (Last) Quarter, illuminated on the eastern (left) side</span>
          </button>
          <button class="mcq-btn" onclick="checkMCQ(this, false, 'q1', 'Waning Gibbous is more than 50% illuminated, not half-illuminated (50%).')">
            <span>C) Waning Gibbous, illuminated on the northern side</span>
          </button>
          <button class="mcq-btn" onclick="checkMCQ(this, false, 'q1', 'Full Moon is on the western horizon setting at sunrise, not directly overhead at zenith.')">
            <span>D) Full Moon, illuminated completely</span>
          </button>
        </div>
        <div class="mcq-feedback"></div>
      </div>

      <!-- MCQ 2 -->
      <div class="mcq-card">
        <div class="mcq-question">
          Q2. Suppose hypothetical gravitational changes caused the Moon to revolve around Earth in 35 days instead of 29.5 days. What would be the consequence for an Indian Luni-Solar calendar?
        </div>
        <div class="mcq-options">
          <button class="mcq-btn" onclick="checkMCQ(this, false, 'q2', 'Exam Trap! If 1 lunar month = 35 days, then 12 lunar months = 420 days, which EXCEEDS the solar year (365 days) by 55 days! You would need to SUBTRACT days, not add intercalary months.')">
            <span>A) Adhika Maasa (intercalary month) would have to be added every single year.</span>
          </button>
          <button class="mcq-btn" onclick="checkMCQ(this, true, 'q2', 'Perfect scientific deduction! The traditional Adhika Maasa was designed specifically to bridge a 354-day lunar year to a 365-day solar year. If 12 lunar months became 420 days, the entire concept of adding an extra 13th month would become obsolete!')">
            <span>B) The traditional Adhika Maasa addition would no longer work, as 12 lunar months (420 days) would exceed the solar year.</span>
          </button>
          <button class="mcq-btn" onclick="checkMCQ(this, false, 'q2', 'The solar year depends entirely on Earth orbiting the Sun (~365.25 days); the Moon\'s speed does not change Earth\'s orbital period!')">
            <span>C) The solar year would automatically expand to 420 days to match the Moon.</span>
          </button>
          <button class="mcq-btn" onclick="checkMCQ(this, false, 'q2', 'Leap years in solar calendars depend on Earth\'s extra quarter-day, completely independent of the Moon.')">
            <span>D) Leap years in the Gregorian calendar would have to be skipped every 2 years.</span>
          </button>
        </div>
        <div class="mcq-feedback"></div>
      </div>

      <!-- MCQ 3 -->
      <div class="mcq-card">
        <div class="mcq-question">
          Q3. On the sea beach at Puri, high tide occurs at 9:00 AM on Monday. At approximately what time will the corresponding high tide arrive on Tuesday morning?
        </div>
        <div class="mcq-options">
          <button class="mcq-btn" onclick="checkMCQ(this, false, 'q3', 'Incorrect! Tides do not repeat at the exact same hour because the Moon advances 13.2° along its orbit every day.')">
            <span>A) Exactly 9:00 AM</span>
          </button>
          <button class="mcq-btn" onclick="checkMCQ(this, false, 'q3', 'Common blunder! High tides shift later, not earlier.')">
            <span>B) 8:10 AM (50 minutes earlier)</span>
          </button>
          <button class="mcq-btn" onclick="checkMCQ(this, true, 'q3', 'Outstanding! Ocean tides are driven by the gravitational pull of the Moon. Because the Moon rises ~50 minutes later each day due to its orbital advance, high tide also arrives ~50 minutes later, at 9:50 AM!')">
            <span>C) 9:50 AM (approx. 50 minutes later)</span>
          </button>
          <button class="mcq-btn" onclick="checkMCQ(this, false, 'q3', 'Incorrect. 12 hours is the approximate interval between high tide and low tide, not the daily tidal phase shift.')">
            <span>D) 3:00 PM (6 hours later)</span>
          </button>
        </div>
        <div class="mcq-feedback"></div>
      </div>

      <!-- MCQ 4 -->
      <div class="mcq-card">
        <div class="mcq-question">
          Q4. Under the precise 3-step Gregorian calendar leap year rules, which of the following century years had 366 days (was a leap year)?
        </div>
        <div class="mcq-options">
          <button class="mcq-btn" onclick="checkMCQ(this, false, 'q4', 'Trap! 1700 is divisible by 4 and 100, but NOT by 400 (1700 ÷ 400 = 4.25). Hence, it was NOT a leap year.')">
            <span>A) 1700 CE</span>
          </button>
          <button class="mcq-btn" onclick="checkMCQ(this, false, 'q4', 'Trap! 1800 is not divisible by 400. It had 365 days.')">
            <span>B) 1800 CE</span>
          </button>
          <button class="mcq-btn" onclick="checkMCQ(this, false, 'q4', 'Trap! 1900 was skipped as a leap year because 1900 is not divisible by 400.')">
            <span>C) 1900 CE</span>
          </button>
          <button class="mcq-btn" onclick="checkMCQ(this, true, 'q4', 'Spot on! Century years divisible by 100 are leap years ONLY if they are also divisible by 400. 2000 ÷ 400 = 5 exactly, so 2000 was a leap year with 366 days!')">
            <span>D) 2000 CE</span>
          </button>
        </div>
        <div class="mcq-feedback"></div>
      </div>

      <!-- MCQ 5 -->
      <div class="mcq-card">
        <div class="mcq-question">
          Q5. Why is an artist's drawing of a star positioned inside the dark horns of a crescent Moon scientifically erroneous?
        </div>
        <div class="mcq-options">
          <button class="mcq-btn" onclick="checkMCQ(this, false, 'q5', 'The Moon is closer, but that does not explain why the star cannot be inside the circular disc outline.')">
            <span>A) Because stars shine much brighter than the Moon.</span>
          </button>
          <button class="mcq-btn" onclick="checkMCQ(this, true, 'q5', 'Correct! The Moon is a solid, completely opaque rocky sphere. Even when part of it is in darkness, its physical body is there, completely blocking any distant stars behind it!')">
            <span>B) Because the Moon is a solid opaque body whose unlit hemisphere blocks background stars.</span>
          </button>
          <button class="mcq-btn" onclick="checkMCQ(this, false, 'q5', 'Stars are immense luminous gas balls light-years away; the Moon has no gravitational power to pull them!')">
            <span>C) Because the Moon\'s gravity pulls stars into its craters.</span>
          </button>
          <button class="mcq-btn" onclick="checkMCQ(this, false, 'q5', 'Moonlight is simply reflected sunlight, not atmospheric refraction.')">
            <span>D) Because moonlight bends incoming starlight through total internal reflection.</span>
          </button>
        </div>
        <div class="mcq-feedback"></div>
      </div>

      <!-- ========================================== -->
      <!-- SUBSECTION 5.2: ASSERTION & REASONING (5)  -->
      <!-- ========================================== -->
      <h3 class="sub-title"><i class="fa-solid fa-arrows-split-up-and-left" style="color: #6366f1;"></i> 5.2 Assertion &amp; Reasoning Questions</h3>
      
      <div class="callout callout-def" style="margin-bottom:1.5rem;">
        <p><strong>Directions:</strong> In the following questions, a statement of Assertion (A) is followed by a statement of Reason (R). Choose the correct option:
        <br><strong>(A)</strong> Both (A) and (R) are true, and (R) is the correct explanation of (A).
        <br><strong>(B)</strong> Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).
        <br><strong>(C)</strong> (A) is true, but (R) is false.
        <br><strong>(D)</strong> (A) is false, but (R) is true.
        </p>
      </div>

      <!-- A&R 1 -->
      <details class="ans-box">
        <summary class="ans-header">
          <span><span class="summary-badge summary-badge-pyq">A&amp;R 1</span> Eclipses vs. 5° Orbital Incline</span>
          <i class="fa-solid fa-chevron-down"></i>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> Lunar eclipses do not occur on every single Full Moon day.<br>
          <strong>Reason (R):</strong> The orbital plane of the Moon is tilted by approximately 5° with respect to the Earth's orbital plane (the ecliptic) around the Sun.</p>
          <p><strong>Answer: (A) Both (A) and (R) are true, and (R) is the correct explanation of (A).</strong></p>
          <p><strong>Scientific Explanation:</strong> If the Moon's orbit lay in the exact same plane as the Earth's orbit, the Earth would cast its shadow on the Moon on every single Full Moon. But because of the 5° tilt, on most Full Moons, the Moon passes well above or below Earth's shadow cone, preventing an eclipse.</p>
        </div>
      </details>

      <!-- A&R 2 -->
      <details class="ans-box">
        <summary class="ans-header">
          <span><span class="summary-badge summary-badge-pyq">A&amp;R 2</span> Pure Lunar Calendars &amp; Seasonal Drift of Eid</span>
          <i class="fa-solid fa-chevron-down"></i>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> In the Islamic Hijri calendar, the festival of Eid-ul-Fitr drifts through all four seasons over a cycle of about 33 years.<br>
          <strong>Reason (R):</strong> A pure lunar year consisting of 12 synodic lunar months is approximately 11 days shorter than the solar tropical year.</p>
          <p><strong>Answer: (A) Both (A) and (R) are true, and (R) is the correct explanation of (A).</strong></p>
          <p><strong>Scientific Explanation:</strong> 12 lunar months equal <code>12 × 29.53 ≈ 354.36 days</code>, which falls short of the 365.24-day solar year by ~11 days. Without an intercalary month like Adhika Maasa, the entire calendar moves 11 days earlier every year, completing a 365-day circuit across all seasons in <code>365 ÷ 11 ≈ 33 years</code>.</p>
        </div>
      </details>

      <!-- A&R 3 -->
      <details class="ans-box">
        <summary class="ans-header">
          <span><span class="summary-badge summary-badge-pyq">A&amp;R 3</span> Far Side of the Moon &amp; Synchronous Rotation</span>
          <i class="fa-solid fa-chevron-down"></i>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> Observers on Earth can never see the far side of the Moon with the naked eye.<br>
          <strong>Reason (R):</strong> The Moon does not rotate on its own axis at all as it revolves around Earth.</p>
          <p><strong>Answer: (C) (A) is true, but (R) is false.</strong></p>
          <p><strong>Scientific Explanation:</strong> (A) is true: we only ever see the near hemisphere of the Moon. But (R) is completely false! The Moon DOES rotate on its axis. In fact, its axial rotation period strictly equals its orbital revolution period (~27.3 days). This synchronous rotation (tidal locking) is precisely why the same face is permanently turned toward Earth.</p>
        </div>
      </details>

      <!-- A&R 4 -->
      <details class="ans-box">
        <summary class="ans-header">
          <span><span class="summary-badge summary-badge-pyq">A&amp;R 4</span> Indian National Calendar &amp; Equinox Alignment</span>
          <i class="fa-solid fa-chevron-down"></i>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> The Indian National Calendar begins on March 22 in normal years and on March 21 in leap years.<br>
          <strong>Reason (R):</strong> The Indian National Calendar is a solar calendar whose first month, Chaitra, begins on the day following the Vernal (Spring) Equinox.</p>
          <p><strong>Answer: (A) Both (A) and (R) are true, and (R) is the correct explanation of (A).</strong></p>
          <p><strong>Scientific Explanation:</strong> Designed by the Calendar Reform Committee under Prof. Meghnad Saha, the Saka calendar is strictly solar and aligned to the tropical year. The vernal equinox occurs on March 21, so the new year (1 Chaitra) begins on March 22 (or March 21 in leap years when Chaitra has 31 days).</p>
        </div>
      </details>

      <!-- A&R 5 -->
      <details class="ans-box">
        <summary class="ans-header">
          <span><span class="summary-badge summary-badge-pyq">A&amp;R 5</span> Orbital Velocities of Satellites vs. The Moon</span>
          <i class="fa-solid fa-chevron-down"></i>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> Artificial satellites in Low Earth Orbit (LEO) circle the Earth once every 90 minutes, travelling much faster than the Moon.<br>
          <strong>Reason (R):</strong> Gravitational force is inversely proportional to the square of the distance; satellites closer to Earth experience stronger gravity and require higher orbital speeds to maintain stable orbits.</p>
          <p><strong>Answer: (A) Both (A) and (R) are true, and (R) is the correct explanation of (A).</strong></p>
          <p><strong>Scientific Explanation:</strong> At an altitude of 500 km, Earth's gravitational pull is immense, requiring an orbital speed of ~7.8 km/s (period ~90 min). In contrast, the Moon orbits at 384,400 km where gravity is much weaker, travelling at only ~1 km/s with an orbital period of ~27.3 days.</p>
        </div>
      </details>

      <!-- ========================================== -->
      <!-- SUBSECTION 5.3: SHORT ANSWER QUESTIONS (6) -->
      <!-- ========================================== -->
      <h3 class="sub-title"><i class="fa-solid fa-pen-to-square" style="color: #d97706;"></i> 5.3 Short Answer Questions (2M &amp; 3M)</h3>

      <!-- SAQ 1 -->
      <details class="ans-box">
        <summary class="ans-header">
          <span><span class="summary-badge">SAQ 1 (2M)</span> Differentiate between Shukla Paksha and Krishna Paksha</span>
          <i class="fa-solid fa-chevron-down"></i>
        </summary>
        <div class="ans-content">
          <p><strong>Answer (CBSE 2-Mark Point-Wise Model):</strong></p>
          <div class="table-container">
            <table>
              <thead>
                <tr><th>Comparison Parameter</th><th>Shukla Paksha (Waxing Phase)</th><th>Krishna Paksha (Waning Phase)</th></tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Size of Bright Portion</strong></td>
                  <td>The illuminated part <strong>increases (grows)</strong> from a thin crescent to a full bright circle.</td>
                  <td>The illuminated part <strong>decreases (shrinks)</strong> from a full bright circle to complete darkness.</td>
                </tr>
                <tr>
                  <td><strong>Starting &amp; Ending Days</strong></td>
                  <td>Begins day after New Moon (Amavasya) and culminates on Full Moon (Purnima).</td>
                  <td>Begins day after Full Moon (Purnima) and culminates on New Moon (Amavasya).</td>
                </tr>
                <tr>
                  <td><strong>Best Observation Time</strong></td>
                  <td>Easiest to spot at <strong>sunset</strong> in the western / southern sky.</td>
                  <td>Easiest to spot at <strong>sunrise</strong> in the eastern / southern sky.</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="marking-scheme"><strong>Marking Scheme:</strong> 1 mark for bright portion behavior + 1 mark for starting/ending days.</div>
        </div>
      </details>

      <!-- SAQ 2 -->
      <details class="ans-box">
        <summary class="ans-header">
          <span><span class="summary-badge">SAQ 2 (3M)</span> Mathematical Proof of the 50-Minute Daily Moonrise Delay</span>
          <i class="fa-solid fa-chevron-down"></i>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Why does the Moon rise approximately 50 minutes later every day? Show the mathematical calculation.</p>
          <p><strong>Answer:</strong></p>
          <ol style="margin-left:1.25rem; line-height:1.8;">
            <li><strong>Earth's Rotational Speed:</strong> Earth rotates 360° on its axis in 24 hours (1,440 minutes).
              <br><code>Speed = 360° ÷ 1,440 min = 0.25° per minute (or 1° every 4 minutes)</code>. [1 Mark]
            </li>
            <li><strong>Moon's Orbital Advance:</strong> The Moon revolves around Earth in approximately 27.3 days. In one day (24 hours), the Moon moves forward along its orbit by:
              <br><code>360° ÷ 27.3 days ≈ 13.2° per day</code>. [1 Mark]
            </li>
            <li><strong>Catch-up Time Calculation:</strong> After Earth completes one 360° spin, the observer must rotate an additional 13.2° to face the advanced Moon again:
              <br><code>Extra Time = 13.2° × 4 minutes/degree = 52.8 minutes ≈ 50 minutes</code>. [1 Mark]
            </li>
          </ol>
          <div class="marking-scheme"><strong>Marking Scheme:</strong> 1M for Earth rotation rate + 1M for Moon orbital advance + 1M for time calculation.</div>
        </div>
      </details>

      <!-- SAQ 3 -->
      <details class="ans-box">
        <summary class="ans-header">
          <span><span class="summary-badge">SAQ 3 (2M)</span> Concept &amp; Necessity of Adhika Maasa (Intercalary Month)</span>
          <i class="fa-solid fa-chevron-down"></i>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> What is an Adhika Maasa? Why is it necessary in a luni-solar calendar?</p>
          <p><strong>Answer:</strong></p>
          <ul style="margin-left:1.25rem; line-height:1.8;">
            <li><strong>Definition:</strong> An <strong>Adhika Maasa</strong> (ଅଧିକ ମାସ) or intercalary month is an extra 13th month inserted into a luni-solar calendar approximately every 2.7 years (about every 32 to 33 months). [1 Mark]</li>
            <li><strong>Necessity:</strong> A lunar year (12 months &times; 29.5 days = 354 days) falls short of the solar year (365.25 days) by <strong>11 days every year</strong>. After 2 to 3 years, this deficit accumulates to roughly 30 days (one full lunar month). Adding the Adhika Maasa resets the lunar calendar by 30 days, preventing festival dates from drifting across seasons and keeping agriculture synchronized. [1 Mark]</li>
          </ul>
          <div class="marking-scheme"><strong>Marking Scheme:</strong> 1 mark for clear definition + 1 mark for explaining the 11-day annual shortfall.</div>
        </div>
      </details>

      <!-- SAQ 4 -->
      <details class="ans-box">
        <summary class="ans-header">
          <span><span class="summary-badge">SAQ 4 (3M)</span> Tropical Year vs. Sidereal Year &amp; Axial Precession</span>
          <i class="fa-solid fa-chevron-down"></i>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Differentiate between a Tropical Year and a Sidereal Year. What causes the 20-minute difference between them?</p>
          <p><strong>Answer:</strong></p>
          <ol style="margin-left:1.25rem; line-height:1.8;">
            <li><strong>Tropical Year (365.2422 Days):</strong> The time interval between two successive Spring (Vernal) Equinoxes. It measures the exact repeating cycle of natural seasons on Earth and forms the basis of the Gregorian solar calendar. [1 Mark]</li>
            <li><strong>Sidereal Year (365.2564 Days):</strong> The time taken by Earth to complete one full orbit around the Sun relative to the background of <strong>fixed stars</strong> (the constellations rising at sunset). [1 Mark]</li>
            <li><strong>Cause of the 20-Minute Difference:</strong> The sidereal year is longer by <strong>20 minutes and 24 seconds</strong> due to <strong>axial precession</strong>—the slow, conical wobbling of Earth's rotational axis (like a spinning top), taking ~25,800 years per wobble. This causes the equinox points to slowly migrate backwards against the starry background. [1 Mark]</li>
          </ol>
          <div class="marking-scheme"><strong>Marking Scheme:</strong> 1M for tropical year definition + 1M for sidereal year definition + 1M for axial precession.</div>
        </div>
      </details>

      <!-- SAQ 5 -->
      <details class="ans-box">
        <summary class="ans-header">
          <span><span class="summary-badge">SAQ 5 (2M)</span> Uttarayan and Dakshinayan Explained</span>
          <i class="fa-solid fa-chevron-down"></i>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Explain the terms Uttarayan and Dakshinayan. On which dates do they begin?</p>
          <p><strong>Answer:</strong></p>
          <ul style="margin-left:1.25rem; line-height:1.8;">
            <li><strong>Uttarayan (ଉତ୍ତରାୟଣ):</strong> The six-month period during which the sunrise position on the eastern horizon moves progressively <strong>northward</strong> and daylight hours in the northern hemisphere increase. It begins on the <strong>Winter Solstice (around December 21/22)</strong>. [1 Mark]</li>
            <li><strong>Dakshinayan (ଦକ୍ଷିଣାୟନ):</strong> The six-month period during which the sunrise position retreats progressively <strong>southward</strong> and daylight hours shorten. It begins on the <strong>Summer Solstice (around June 21)</strong>. [1 Mark]</li>
          </ul>
          <div class="marking-scheme"><strong>Marking Scheme:</strong> 1 mark for Uttarayan + 1 mark for Dakshinayan with correct solstice dates.</div>
        </div>
      </details>

      <!-- SAQ 6 -->
      <details class="ans-box">
        <summary class="ans-header">
          <span><span class="summary-badge">SAQ 6 (3M)</span> Natural Satellite (Moon) vs. Artificial Satellite</span>
          <i class="fa-solid fa-chevron-down"></i>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> State three essential distinctions between Earth's natural satellite (the Moon) and an artificial satellite.</p>
          <p><strong>Answer:</strong></p>
          <div class="table-container">
            <table>
              <thead>
                <tr><th>Distinction Parameter</th><th>Earth's Natural Satellite (The Moon)</th><th>Artificial Satellite (e.g., Cartosat, GSAT)</th></tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Origin &amp; Nature</strong></td>
                  <td>Naturally formed astronomical rocky sphere (~4.5 billion years old).</td>
                  <td>Human-manufactured machine engineered with solar panels, sensors, and thrusters.</td>
                </tr>
                <tr>
                  <td><strong>Orbital Distance &amp; Period</strong></td>
                  <td>Orbits at ~384,400 km with an orbital period of ~27.3 days.</td>
                  <td>Orbits much closer: LEO (~500 km, 90 mins) or GEO (35,786 km, 24 hours).</td>
                </tr>
                <tr>
                  <td><strong>Controllability &amp; Function</strong></td>
                  <td>Uncontrolled natural motion; causes ocean tides and nocturnal illumination.</td>
                  <td>Active ground-control station maneuvering; performs telecommunications, GPS, and disaster imaging.</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="marking-scheme"><strong>Marking Scheme:</strong> 1 mark for each distinct, well-explained scientific difference (total 3 marks).</div>
        </div>
      </details>

      <!-- ========================================== -->
      <!-- SUBSECTION 5.4: LONG ANSWER QUESTIONS (4)  -->
      <!-- ========================================== -->
      <h3 class="sub-title"><i class="fa-solid fa-file-lines" style="color: #0d9488;"></i> 5.4 Long Answer Questions (5M) with Marking Schemes</h3>

      <!-- LAQ 1 -->
      <details class="ans-box">
        <summary class="ans-header">
          <span><span class="summary-badge summary-badge-pyq">LAQ 1 (5M)</span> Comprehensive Treatise on the Phases of the Moon</span>
          <i class="fa-solid fa-chevron-down"></i>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Explain in detail the phenomenon of the phases of the Moon. Discuss: (a) Why phases occur, (b) The eight distinct phases in sequence, (c) Why we only ever see one face of the Moon, and (d) Why phases are NOT caused by the Earth's shadow.</p>
          <p><strong>Model Answer (CBSE Topper 5-Step Structure):</strong></p>
          
          <p><strong>(a) Why Phases Occur (1 Mark):</strong><br>
          The Moon is an opaque, spherical, non-luminous body that shines strictly by reflecting sunlight. At all times, the Sun illuminates exactly 50% (one hemisphere) of the Moon. As the Moon revolves around Earth once every ~29.5 days, the angle between the Sun, Earth, and Moon changes continuously. Observers on Earth see varying fractions of this illuminated hemisphere, creating the apparent changing shapes called <strong>phases of the Moon</strong>.</p>

          <p><strong>(b) The 8 Distinct Phases in Sequence (1.5 Marks):</strong></p>
          <ol style="margin-left:1.25rem; line-height:1.8;">
            <li><em>New Moon (Amavasya):</em> Moon is between Earth and Sun; unlit face faces Earth (0% visible).</li>
            <li><em>Waxing Crescent:</em> A thin sliver of light appears on the right edge (&lt;50% lit).</li>
            <li><em>First Quarter:</em> Half of the illuminated hemisphere is seen on the right (50% lit).</li>
            <li><em>Waxing Gibbous:</em> The bright portion bulges into an egg-like shape (&gt;50% lit).</li>
            <li><em>Full Moon (Purnima):</em> Earth is between Sun and Moon; entire illuminated face is visible (100% lit).</li>
            <li><em>Waning Gibbous:</em> Bright portion begins shrinking from the right (&gt;50% lit on left).</li>
            <li><em>Third / Last Quarter:</em> Half of the illuminated hemisphere is seen on the left (50% lit).</li>
            <li><em>Waning Crescent:</em> A thin sliver of light remains on the left edge (&lt;50% lit), leading back to New Moon.</li>
          </ol>

          <p><strong>(c) Why We Only Ever See One Face of the Moon (1.5 Marks):</strong><br>
          This occurs due to <strong>Synchronous Rotation (Tidal Locking)</strong>. The gravitational tidal forces exerted by Earth on the Moon over billions of years have slowed the Moon's rotation until its <strong>period of axial rotation strictly equals its period of orbital revolution</strong> around Earth (~27.3 days). Because it spins once on its axis in the exact time it circles Earth once, the same hemisphere permanently faces Earth.</p>

          <p><strong>(d) Why Phases Are NOT Caused by Earth's Shadow (1 Mark):</strong><br>
          Earth's shadow plays <strong>zero role</strong> in regular moon phases! The dark portion of a crescent or quarter moon is simply the Moon's own nighttime hemisphere facing away from the Sun. Earth's shadow falls on the Moon <em>only during a lunar eclipse</em>, which can occur strictly on a Full Moon night, is rare, and lasts only a few hours because the Moon's orbit is tilted by 5° to the ecliptic.</p>

          <div class="marking-scheme">
            <strong>CBSE 5-Mark Marking Scheme:</strong><br>
            • Cause of phases (reflected sunlight &amp; changing viewing angle): <strong>1.0 Mark</strong><br>
            • Sequence of 8 phases named correctly with waxing/waning: <strong>1.5 Marks</strong><br>
            • Explanation of synchronous rotation / tidal locking: <strong>1.5 Marks</strong><br>
            • Misconception busting: phases vs. lunar eclipse (5° tilt): <strong>1.0 Mark</strong>
          </div>
        </div>
      </details>

      <!-- LAQ 2 -->
      <details class="ans-box">
        <summary class="ans-header">
          <span><span class="summary-badge summary-badge-pyq">LAQ 2 (5M)</span> Comparative Analysis of Calendar Systems &amp; Leap Mechanisms</span>
          <i class="fa-solid fa-chevron-down"></i>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Compare Solar, Lunar, and Luni-Solar calendars. Explain: (a) The astronomical basis of each, (b) The leap year rule of the Gregorian solar calendar with century exceptions, (c) The cause and remedy of the 11-day deficit in luni-solar calendars, and (d) Give two Indian festival examples for each calendar type.</p>
          <p><strong>Model Answer:</strong></p>

          <p><strong>(a) Astronomical Basis of the Three Systems (1.5 Marks):</strong></p>
          <ul style="margin-left:1.25rem; line-height:1.8;">
            <li><em>Solar Calendar:</em> Governed strictly by the tropical year (Earth's revolution around the Sun = 365.2422 days). Months are civil divisions (30/31 days) designed to sum to 365 days.</li>
            <li><em>Lunar Calendar:</em> Governed strictly by the synodic lunar cycle (Moon's revolution around Earth = 29.53 days). 12 lunar months equal 354 days.</li>
            <li><em>Luni-Solar Calendar:</em> Hybrid system. Days and months follow lunar phases (~29.5 days), but periodic intercalary months are added to synchronize the year with solar seasons.</li>
          </ul>

          <p><strong>(b) Gregorian Leap Year Mechanism &amp; Century Rules (1.5 Marks):</strong><br>
          A tropical year is ~365.2422 days (~365¼ days). The extra ~6 hours accumulate to 1 full day every 4 years.
          <br>1. <em>Divisible by 4 Rule:</em> Years divisible by 4 add February 29 (366 days).
          <br>2. <em>Century Exception (Divisible by 100):</em> Adding 1 day every 4 years adds 11 minutes too much per year. To compensate, century years divisible by 100 are NOT leap years (e.g., 1700, 1800, 1900 had 365 days).
          <br>3. <em>400-Year Correction:</em> Skipping every century year over-corrects. Thus, century years divisible by 400 ARE leap years (e.g., 1600, 2000 had 366 days).</p>

          <p><strong>(c) The 11-Day Deficit &amp; Adhika Maasa (1.0 Mark):</strong><br>
          A lunar year (354 days) is 11.25 days shorter than a solar year (365.25 days). In ~2.7 years, this shortfall equals ~30 days (1 full lunar month). Luni-solar calendars insert an extra 13th month—<strong>Adhika Maasa (ମଳମାସ)</strong>—every 32 to 33 months, resetting the lunar months back into seasonal alignment.</p>

          <p><strong>(d) Indian Festival Examples (1.0 Mark):</strong></p>
          <ul style="margin-left:1.25rem; line-height:1.8;">
            <li><em>Solar Calendar Festivals:</em> Makar Sankranti (Jan 14/15), Maha Bishuba Pana Sankranti (April 14/15) — fixed Gregorian dates.</li>
            <li><em>Luni-Solar Festivals:</em> Diwali (Kartika Amavasya), Holi (Phalguna Purnima) — dates shift within a 3-week seasonal window.</li>
            <li><em>Pure Lunar Festivals:</em> Eid-ul-Fitr (1st crescent of Shawwal), Muharram — dates shift 11 days earlier every year across all seasons.</li>
          </ul>

          <div class="marking-scheme">
            <strong>CBSE 5-Mark Marking Scheme:</strong><br>
            • Comparison of 3 calendar bases: <strong>1.5 Marks</strong><br>
            • 3-tier Gregorian leap rules (div 4, skip 100, add 400): <strong>1.5 Marks</strong><br>
            • 11-day deficit and Adhika Maasa explanation: <strong>1.0 Mark</strong><br>
            • Festival examples correctly categorized: <strong>1.0 Mark</strong>
          </div>
        </div>
      </details>

      <!-- LAQ 3 -->
      <details class="ans-box">
        <summary class="ans-header">
          <span><span class="summary-badge summary-badge-pyq">LAQ 3 (5M)</span> The Indian National Calendar (Saka Calendar) &amp; Prof. Meghnad Saha</span>
          <i class="fa-solid fa-chevron-down"></i>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Write a comprehensive account of the Indian National Calendar. Explain: (a) Why the Calendar Reform Committee was constituted and who chaired it, (b) Its starting epoch and relation to the Gregorian calendar, (c) The structure and distribution of days across its 12 months, and (d) How leap years are handled.</p>
          <p><strong>Model Answer:</strong></p>

          <p><strong>(a) Historical Background &amp; Leadership (1.0 Mark):</strong><br>
          At Independence, over 30 distinct regional calendars were in use across India, leading to widespread confusion in scheduling national holidays, civil administration, and meteorological records. In November 1952, the Government of India under CSIR established the <strong>Calendar Reform Committee (CRC)</strong> chaired by the renowned astrophysicist <strong>Prof. Meghnad Saha</strong>. The committee designed a scientific, uniform national calendar adopted on <strong>22 March 1957 CE (1 Chaitra 1879 Saka)</strong>.</p>

          <p><strong>(b) Starting Epoch &amp; Vernal Equinox Alignment (1.0 Mark):</strong><br>
          The Indian National Calendar uses the historical <strong>Saka Era</strong> (epoch year 0 = 78 CE; Saka year = Gregorian year - 78). It is a pure solar calendar locked to the tropical year. The civil year begins on <strong>1 Chaitra</strong>, which coincides with <strong>March 22</strong> in normal Gregorian years and <strong>March 21</strong> in Gregorian leap years (the day following the Spring Equinox).</p>

          <p><strong>(c) Month Structure &amp; Distribution of Days (1.5 Marks):</strong><br>
          The calendar has 12 months with traditional Indian names, scientifically structured into two halves:
          <br>• <em>Month 1 (Chaitra):</em> 30 days in normal years; 31 days in leap years.
          <br>• <em>Months 2 to 6 (Vaisakha, Jyeshtha, Ashadha, Shravana, Bhadrapada):</em> Exactly <strong>31 days each</strong>. (This accounts for Earth moving slightly slower along its elliptical orbit during northern hemisphere summer!).
          <br>• <em>Months 7 to 12 (Ashwina, Kartika, Margashirsha, Pausha, Magha, Phalguna):</em> Exactly <strong>30 days each</strong>.
          <br>Total = <code>30 + (5 × 31) + (6 × 30) = 365 days</code> (366 in leap year).</p>

          <p><strong>(d) Leap Year Handling &amp; Official Adoption (1.5 Marks):</strong><br>
          The Saka calendar adds its leap day to <strong>Chaitra</strong> in the exact same years that the Gregorian calendar has a leap year (divisible by 4, skipping century years unless divisible by 400). When 78 is added to the Saka year, if the resulting Gregorian year is a leap year, Chaitra has 31 days and the new year begins on March 21. It is officially published alongside the Gregorian calendar in the Gazette of India, All India Radio, and Doordarshan broadcasts.</p>

          <div class="marking-scheme">
            <strong>CBSE 5-Mark Marking Scheme:</strong><br>
            • CRC background &amp; Meghnad Saha: <strong>1.0 Mark</strong><br>
            • Epoch (Saka 78 CE) &amp; March 21/22 equinox connection: <strong>1.0 Mark</strong><br>
            • Distribution of 30/31 day months: <strong>1.5 Marks</strong><br>
            • Leap day in Chaitra &amp; official usage: <strong>1.5 Marks</strong>
          </div>
        </div>
      </details>

      <!-- LAQ 4 -->
      <details class="ans-box">
        <summary class="ans-header">
          <span><span class="summary-badge summary-badge-pyq">LAQ 4 (5M)</span> Artificial Satellites, ISRO Space Missions &amp; Space Debris</span>
          <i class="fa-solid fa-chevron-down"></i>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Describe the science and applications of artificial satellites. Discuss: (a) What an artificial satellite is and how it remains in orbit, (b) Differentiate between Low Earth Orbit (LEO) and Geostationary Orbit (GEO), (c) Four critical societal contributions of ISRO satellites, and (d) Dr. Vikram Sarabhai's vision and the growing menace of space debris.</p>
          <p><strong>Model Answer:</strong></p>

          <p><strong>(a) Definition &amp; Orbital Physics (1.0 Mark):</strong><br>
          An artificial satellite is an engineered spacecraft launched by multi-stage rockets into orbit around Earth. It stays in orbit by achieving high horizontal velocity (~7.8 km/s in LEO). At this speed, as Earth's gravity continuously pulls the satellite downward, Earth's spherical surface curves away beneath it at the exact same rate! The satellite is in perpetual free-fall around the planet.</p>

          <p><strong>(b) Low Earth Orbit (LEO) vs. Geostationary Orbit (GEO) (1.0 Mark):</strong></p>
          <ul style="margin-left:1.25rem; line-height:1.8;">
            <li><em>LEO (Low Earth Orbit):</em> Altitude 400–800 km; orbital period ~90 minutes. Satellites circle Earth multiple times daily; ideal for high-resolution earth imaging (Cartosat) and space telescopes (AstroSat).</li>
            <li><em>GEO (Geostationary Orbit):</em> Altitude exactly 35,786 km above the equator; orbital period is exactly <strong>24 hours</strong>, matching Earth's rotation. To a ground observer, the satellite appears permanently fixed at one spot in the sky; ideal for telecommunications and weather monitoring (INSAT/GSAT).</li>
          </ul>

          <p><strong>(c) Four Critical Contributions of ISRO Satellites (1.5 Marks):</strong></p>
          <ol style="margin-left:1.25rem; line-height:1.8;">
            <li><em>Cyclone Early Warning:</em> INSAT weather satellites track tropical cyclones over the Bay of Bengal, providing 72-hour advance landfall warnings that allow mass evacuations in Odisha.</li>
            <li><em>Sovereign Navigation:</em> NavIC (IRNSS) constellation provides self-reliant GPS services for Indian defense, civil aviation, and maritime fishermen.</li>
            <li><em>Natural Resource &amp; Flood Mapping:</em> Cartosat and Resourcesat provide imaging for city planning and flood extent mapping on the Bhuvan geoportal.</li>
            <li><em>Deep Space Astronomy:</em> AstroSat studies cosmic black holes; Chandrayaan-3 achieved historic soft landing at the Moon's South Pole; Aditya-L1 monitors the Sun.</li>
          </ol>

          <p><strong>(d) Vikram Sarabhai's Vision &amp; Space Debris (1.5 Marks):</strong><br>
          Dr. Vikram Sarabhai (Father of the Indian Space Programme) founded INCOSPAR/ISRO with the founding philosophy that space science must directly benefit the common citizen—farmers, fishermen, and students.
          <br><em>Space Debris Hazard:</em> Over 36,000 trackable pieces of spent rocket boosters and defunct satellites orbit at 28,000 km/h. At this hypervelocity, a collision can shatter operational satellites (Kessler Syndrome). ISRO actively mitigates this via Project NETRA and mandatory deorbiting burns to incinerate dead satellites in the upper atmosphere.</p>

          <div class="marking-scheme">
            <strong>CBSE 5-Mark Marking Scheme:</strong><br>
            • Satellite definition &amp; orbital free-fall mechanism: <strong>1.0 Mark</strong><br>
            • LEO vs. GEO altitude, speed, and function: <strong>1.0 Mark</strong><br>
            • 4 ISRO societal contributions: <strong>1.5 Marks</strong><br>
            • Dr. Vikram Sarabhai &amp; Space debris (Project NETRA): <strong>1.5 Marks</strong>
          </div>
        </div>
      </details>

      <!-- ========================================== -->
      <!-- SUBSECTION 5.5: CASE STUDIES (2)           -->
      <!-- ========================================== -->
      <h3 class="sub-title"><i class="fa-solid fa-microscope" style="color: #6366f1;"></i> 5.5 Competency-Based Case Studies (Data Analysis)</h3>

      <!-- CASE STUDY 1 -->
      <details class="ans-box" open>
        <summary class="ans-header">
          <span><span class="summary-badge summary-badge-pyq">Case Study 1</span> The Tale of Two Festivals — Diwali vs. Eid-ul-Fitr</span>
          <i class="fa-solid fa-chevron-down"></i>
        </summary>
        <div class="ans-content">
          <p><strong>Source Context &amp; Observational Data:</strong><br>
          Rohan compiled a comparative record of the Gregorian celebration dates of two major Indian festivals—Eid-ul-Fitr and Diwali—over five consecutive years from 2021 to 2025:</p>
          
          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th>Year</th>
                  <th>Date of Eid-ul-Fitr</th>
                  <th>Annual Shift in Eid Date</th>
                  <th>Date of Diwali</th>
                  <th>Annual Shift in Diwali Date</th>
                </tr>
              </thead>
              <tbody>
                <tr><td>2021</td><td>13 May 2021</td><td>—</td><td>04 November 2021</td><td>—</td></tr>
                <tr><td>2022</td><td>02 May 2022</td><td>11 days earlier</td><td>24 October 2022</td><td>11 days earlier</td></tr>
                <tr><td>2023</td><td>21 April 2023</td><td>11 days earlier</td><td>12 November 2023</td><td><strong>19 days later (Jump!)</strong></td></tr>
                <tr><td>2024</td><td>10 April 2024</td><td>11 days earlier</td><td>31 October 2024</td><td>12 days earlier</td></tr>
                <tr><td>2025</td><td>31 March 2025</td><td>10 days earlier</td><td>20 October 2025</td><td>11 days earlier</td></tr>
              </tbody>
            </table>
          </div>

          <p><strong>Competency-Based Sub-Questions:</strong></p>
          <ol style="margin-left:1.25rem; line-height:1.8;">
            <li><strong>Q1 (1 Mark):</strong> Why does Eid-ul-Fitr shift earlier by approximately 10 to 11 days with strict mathematical regularity every single year?</li>
            <li><strong>Q2 (1 Mark):</strong> Why did the date of Diwali jump forward by 19 days in 2023 instead of moving 11 days earlier like Eid?</li>
            <li><strong>Q3 (1 Mark):</strong> Predict the approximate Gregorian month in which Eid-ul-Fitr will be celebrated in the year 2038 (~16 years after 2022).</li>
            <li><strong>Q4 (1 Mark):</strong> What would happen to the festival of Diwali if Indian panjikas stopped including the Adhika Maasa?</li>
          </ol>

          <p><strong>Answers:</strong></p>
          <ul style="margin-left:1.25rem; line-height:1.8;">
            <li><strong>A1:</strong> Eid-ul-Fitr is governed by the Islamic Hijri calendar, which is a <strong>pure lunar calendar (354 days)</strong> with no intercalary month adjustments. Because it is 11 days shorter than the 365-day Gregorian solar year, every lunar date shifts 11 days earlier each solar year.</li>
            <li><strong>A2:</strong> Diwali follows a <strong>luni-solar calendar</strong>. In 2023, the accumulated deficit reached ~30 days, triggering the insertion of an intercalary month—<strong>Adhika Shravana Maasa</strong> (July 18 to August 16, 2023). This 30-day insertion caused Diwali to leap forward to November 12, preserving its autumn season!</li>
            <li><strong>A3:</strong> In 16 years, 16 &times; 11 days = 176 days (~6 months shift). Moving 6 months earlier from May places Eid-ul-Fitr in <strong>November / December (late autumn / winter)</strong> in 2038!</li>
            <li><strong>A4:</strong> Without Adhika Maasa, Diwali would lose 11 days every year, drifting into summer, spring, and winter, completely separating the "Festival of Lights" from its traditional post-monsoon autumn harvest season.</li>
          </ul>
        </div>
      </details>

      <!-- CASE STUDY 2 -->
      <details class="ans-box">
        <summary class="ans-header">
          <span><span class="summary-badge summary-badge-pyq">Case Study 2</span> Space Surveillance &amp; Cyclone Early Warning in Coastal Odisha</span>
          <i class="fa-solid fa-chevron-down"></i>
        </summary>
        <div class="ans-content">
          <p><strong>Source Context:</strong><br>
          In October 2024, severe cyclonic storm 'Dana' formed over the east-central Bay of Bengal, heading straight towards the coast of Odisha and West Bengal. Using ISRO's INSAT-3DR geostationary meteorological satellite, scientists at the India Meteorological Department tracked the cyclone's central eye, cloud-top temperatures, and rotational wind velocity every 15 minutes. Simultaneously, high-resolution Cartosat optical sensors provided spatial models of low-lying coastal embankments in Kendrapara and Bhadrak districts on the Bhuvan geoportal, while NavIC emergency receivers alerted deep-sea fishing trawlers to return to port immediately. As a result, over 600,000 citizens were evacuated safely, resulting in near-zero casualties.</p>

          <p><strong>Competency-Based Sub-Questions:</strong></p>
          <ol style="margin-left:1.25rem; line-height:1.8;">
            <li><strong>Q1 (1 Mark):</strong> Why was a <em>geostationary</em> satellite (INSAT-3DR) chosen for 15-minute cyclone tracking instead of a Low Earth Orbit satellite?</li>
            <li><strong>Q2 (1 Mark):</strong> What is ISRO's <em>Bhuvan geoportal</em>, and how did it assist disaster management teams in Odisha?</li>
            <li><strong>Q3 (1 Mark):</strong> How did the <em>NavIC constellation</em> assist fishermen at sea beyond cell-phone tower range?</li>
            <li><strong>Q4 (1 Mark):</strong> If space debris in LEO collides with an imaging satellite, what dangerous phenomenon can cascade through space?</li>
          </ol>

          <p><strong>Answers:</strong></p>
          <ul style="margin-left:1.25rem; line-height:1.8;">
            <li><strong>A1:</strong> A geostationary satellite orbits at 35,786 km with a 24-hour period matching Earth's rotation, remaining permanently stationary over India. This allows <strong>continuous, non-stop surveillance</strong> of the cyclone's eye, unlike LEO satellites which pass over a region for only 10 minutes every few days.</li>
            <li><strong>A2:</strong> <strong>Bhuvan</strong> is ISRO's national geographic information system (GIS) mapping platform. It provided multi-layered topographical maps of low-lying flood zones, helping officials identify vulnerable villages for urgent evacuation.</li>
            <li><strong>A3:</strong> <strong>NavIC</strong> transmits satellite-based positioning and short text emergency warnings directly to satellite receivers installed on fishing boats, communicating cyclone alerts hundreds of kilometers beyond mobile network range.</li>
            <li><strong>A4:</strong> It triggers the <strong>Kessler Syndrome</strong>—a cascading chain reaction where fragments from one collision smash into other satellites, generating thousands of hypervelocity debris particles that could render entire orbital zones unusable for decades.</li>
          </ul>
        </div>
      </details>

      <!-- ========================================== -->
      <!-- SUBSECTION 5.6: PYQS & MOST PROBABLE (5)   -->
      <!-- ========================================== -->
      <h3 class="sub-title"><i class="fa-solid fa-clock-rotate-left" style="color: #ea580c;"></i> 5.6 Previous Years Questions (PYQs) &amp; Most Probable Exam Models</h3>

      <!-- PYQ 1 -->
      <details class="ans-box">
        <summary class="ans-header">
          <span><span class="summary-badge summary-badge-pyq">PYQ 1 (2M)</span> Shortest Shadow at Solar Noon &amp; Sundial Construction</span>
          <i class="fa-solid fa-chevron-down"></i>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Why does an upright vertical stick cast the shortest shadow at solar noon? How did ancient astronomers use this principle to construct sundials?</p>
          <p><strong>Answer:</strong></p>
          <ul style="margin-left:1.25rem; line-height:1.8;">
            <li><strong>Cause of Shortest Shadow:</strong> The length of a shadow is inversely proportional to the Sun's elevation angle. At <strong>Local Solar Noon</strong>, the Sun reaches its highest point in the sky as it crosses the local celestial meridian. Because the sun rays strike the vertical stick at the steepest (most direct) angle, the shadow cast on the horizontal ground is at its absolute minimum length. [1 Mark]</li>
            <li><strong>Sundial Construction:</strong> Ancient astronomers calibrated a flat dial plate with hour lines radiating from the base of the gnomon. As the Earth rotated from West to East, the shadow cast by the Sun rotated like a clock hand from West to North to East, allowing people to read the exact solar time of day. [1 Mark]</li>
          </ul>
        </div>
      </details>

      <!-- PYQ 2 -->
      <details class="ans-box">
        <summary class="ans-header">
          <span><span class="summary-badge summary-badge-pyq">PYQ 2 (3M)</span> Long-Term Impact of Lunar Orbital Recession (3.8 cm/year)</span>
          <i class="fa-solid fa-chevron-down"></i>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Laser measurements show that the Moon is moving away from Earth at a rate of 3.8 cm per year. Explain the long-term scientific consequences of this recession on: (a) Total Solar Eclipses, (b) Duration of the month, and (c) Ocean tides.</p>
          <p><strong>Answer:</strong></p>
          <ol style="margin-left:1.25rem; line-height:1.8;">
            <li><strong>(a) Disappearance of Total Solar Eclipses:</strong> As the Moon's distance increases, its apparent angular size in the sky will shrink. In roughly 600 million years, the Moon will appear too small to completely cover the Sun's disc, ending all Total Solar Eclipses forever (leaving only Annular "Ring of Fire" eclipses!). [1 Mark]</li>
            <li><strong>(b) Lengthening of the Month:</strong> By Kepler's Third Law (T² &prop; r³), as the orbital radius increases, the Moon revolves slower, making the lunar month longer than 29.5 days. [1 Mark]</li>
            <li><strong>(c) Weaker Ocean Tides:</strong> Gravitational tidal force decreases with the cube of distance (F &prop; 1/r³). As the Moon recedes, its tidal pull on Earth's oceans will weaken significantly, diminishing the height difference between high and low tides. [1 Mark]</li>
          </ol>
        </div>
      </details>

      <!-- PYQ 3 -->
      <details class="ans-box">
        <summary class="ans-header">
          <span><span class="summary-badge summary-badge-pyq">PYQ 3 (2M)</span> Why Solar Festivals Shift by 1 Day Every 71 Years</span>
          <i class="fa-solid fa-chevron-down"></i>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Why do solar festivals like Makar Sankranti shift forward in the Gregorian calendar by 1 day every 71 years?</p>
          <p><strong>Answer:</strong></p>
          <ul style="margin-left:1.25rem; line-height:1.8;">
            <li>Makar Sankranti is based on the <strong>Sidereal Solar Calendar</strong> (the Sun entering the constellation of Capricorn relative to fixed stars). In contrast, the Gregorian calendar is based on the <strong>Tropical Year</strong> (the cycle of equinoxes and solstices). [1 Mark]</li>
            <li>Due to <strong>axial precession</strong> (the slow 25,800-year wobble of Earth's rotational axis), the sidereal year is longer than the tropical year by ~20.4 minutes. This minute gap accumulates to 1 full day every <code>24 hours ÷ 20.4 min ≈ 71 years</code>. Consequently, Makar Sankranti, which was celebrated on December 21 in ancient times, has shifted to January 14/15 today! [1 Mark]</li>
          </ul>
        </div>
      </details>

      <!-- PYQ 4 -->
      <details class="ans-box">
        <summary class="ans-header">
          <span><span class="summary-badge summary-badge-pyq">PYQ 4 (3M)</span> Amant vs. Purnimant Systems in Indian Panchangs</span>
          <i class="fa-solid fa-chevron-down"></i>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Distinguish between the Amant and Purnimant calendar conventions. Explain their paksha arrangement and name the regions of India where each is prevalent.</p>
          <p><strong>Answer:</strong></p>
          <ol style="margin-left:1.25rem; line-height:1.8;">
            <li><strong>Amant System (ଅମାନ୍ତ):</strong>
              <br>• The lunar month begins on the day after New Moon (Shukla Pratipada) and ends on the New Moon (Amavasya).
              <br>• <em>Paksha Order:</em> Shukla Paksha occurs first, followed by Krishna Paksha.
              <br>• <em>Prevalence:</em> Followed in South India (Karnataka, Andhra Pradesh, Telangana, Tamil Nadu), Maharashtra, Gujarat, and parts of Odisha. [1.5 Marks]
            </li>
            <li><strong>Purnimant System (ପୂର୍ଣ୍ଣିମାନ୍ତ):</strong>
              <br>• The lunar month begins on the day after Full Moon (Krishna Pratipada) and ends on the Full Moon (Purnima).
              <br>• <em>Paksha Order:</em> Krishna Paksha occurs first, followed by Shukla Paksha.
              <br>• <em>Prevalence:</em> Followed in Odisha (widely used in temple panjikas and Jagannath Temple rituals), Uttar Pradesh, Bihar, Rajasthan, and Madhya Pradesh. [1.5 Marks]
            </li>
          </ol>
        </div>
      </details>

      <!-- PYQ 5 -->
      <details class="ans-box">
        <summary class="ans-header">
          <span><span class="summary-badge summary-badge-pyq">PYQ 5 (3M)</span> AstroSat vs. Cartosat: Science vs. Earth Observation</span>
          <i class="fa-solid fa-chevron-down"></i>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> How does India's AstroSat mission differ fundamentally from the Cartosat series of satellites?</p>
          <p><strong>Answer:</strong></p>
          <div class="table-container">
            <table>
              <thead>
                <tr><th>Comparison Parameter</th><th>AstroSat (Space Astronomy Observatory)</th><th>Cartosat (Earth Observation Satellite)</th></tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Direction of Pointing</strong></td>
                  <td>Points <strong>outward into deep space</strong> away from Earth.</td>
                  <td>Points <strong>inward towards Earth's surface</strong>.</td>
                </tr>
                <tr>
                  <td><strong>Target of Investigation</strong></td>
                  <td>Distant celestial objects: active galactic nuclei, neutron stars, black holes, and binary star systems.</td>
                  <td>Earth's surface features: terrain elevation, urban roads, coastal erosion, forest canopy, and river basins.</td>
                </tr>
                <tr>
                  <td><strong>Sensors &amp; Wavelengths</strong></td>
                  <td>Multi-wavelength instruments: Ultraviolet (UVIT), X-ray (LAXPC, SXT, CZTI), and visible light.</td>
                  <td>High-resolution panchromatic and multispectral optical cameras (sub-meter ground resolution).</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="marking-scheme"><strong>Marking Scheme:</strong> 1 mark each for pointing direction, targets studied, and sensors utilized (3 marks total).</div>
        </div>
      </details>
    </section>
"""
