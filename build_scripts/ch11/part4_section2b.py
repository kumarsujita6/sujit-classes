# -*- coding: utf-8 -*-
"""Part 4: Section 2 (Part B) - Conceptual Theory & Vocabulary Bank for Class 8 Science Ch 11."""

PART4_CONTENT = """
      <!-- 11.2 HOW DID CALENDARS COME INTO EXISTENCE? -->
      <h3 class="sub-title"><i class="fa-solid fa-calendar" style="color: #6366f1;"></i> 11.2 How Did Calendars Come into Existence?</h3>
      <p>
        Every clock or calendar that humanity has ever constructed relies on a single fundamental scientific principle: <strong>periodic natural events</strong>. A periodic event is any physical phenomenon that repeats itself at regular, predictable intervals of time.
      </p>
      <p>
        When ancient humans watched the sky, they discovered three great natural astronomical cycles:
      </p>
      <ul style="margin-left: 1.5rem; margin-bottom: 1.25rem; line-height: 1.8;">
        <li><strong>1. The Day:</strong> Caused by the <strong>Earth spinning once on its axis</strong> (24 hours). The Sun rises in the East, reaches its peak height at noon, sets in the West, and reappears the next morning.</li>
        <li><strong>2. The Month:</strong> Caused by the <strong>Moon revolving once around the Earth</strong> (~29.5 days). Marked by the steady, beautiful progression of lunar phases from New Moon to Full Moon and back.</li>
        <li><strong>3. The Year:</strong> Caused by the <strong>Earth completing one full orbit around the Sun</strong> (~365.25 days). Marked by the cyclical rhythm of nature: scorching summers, rejuvenating monsoons, and crisp winters.</li>
      </ul>

      <div class="callout callout-act">
        <div class="callout-header"><i class="fa-solid fa-ruler"></i> Activity 11.3: Let Us Measure a Solar Day with a Gnomon!</div>
        <p><strong>Apparatus &amp; Setup:</strong></p>
        <p>
          Find a level, unobstructed patch of ground bathed in direct sunlight. Firmly fix a straight, 1-meter long wooden stick or metal rod (called a <strong>gnomon</strong> - ଛାୟା ଶଙ୍କୁ) perfectly vertically into the ground.
        </p>
        <p><strong>Procedure &amp; Observations:</strong></p>
        <ol style="margin-left: 1.25rem; line-height: 1.8;">
          <li>Begin observations at 11:00 a.m. Every minute (or every 5 minutes), mark a tiny dot on the ground at the sharp tip of the stick's shadow.</li>
          <li>Continue marking dots until around 1:10 p.m. Notice that the shadow tip traces a smooth curve on the ground!</li>
          <li>Measure the distance from the base of the stick to each marked dot. You will find that the shadow starts long at 11:00 a.m., gradually shrinks to its <strong>minimum length</strong> around midday, and then begins to lengthen again!</li>
          <li>The exact instant when the shadow is at its absolute <strong>shortest</strong> is called <strong>Local Solar Noon</strong>. At this exact moment, the Sun has reached its highest altitude in the sky and is crossing the local meridian (directly North-South line).</li>
          <li>Repeat this experiment the following day. Measure the exact time elapsed between the shortest shadow of Day 1 and the shortest shadow of Day 2.</li>
        </ol>
        <p style="margin-top:0.5rem;">
          <strong>Scientific Conclusion:</strong> The time interval between two consecutive solar noons is called a <strong>Solar Day</strong>. Averaged across the year, its duration is precisely <strong>24 hours (1,440 minutes)</strong>, termed the <strong>Mean Solar Day</strong> (ମାଧ୍ୟ ସୌର ଦିବସ).
        </p>
      </div>

      <!-- SVG 5: The Gnomon Shadow Experiment -->
      <div class="svg-container">
        <svg viewBox="0 0 920 320" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="groundGrad" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#f8fafc" />
              <stop offset="100%" stop-color="#e2e8f0" />
            </linearGradient>
            <linearGradient id="sunRayGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.8" />
              <stop offset="100%" stop-color="#fef08a" stop-opacity="0.2" />
            </linearGradient>
          </defs>
          <rect width="920" height="320" rx="14" fill="#0f172a" />

          <text x="460" y="30" fill="#38bdf8" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="16" text-anchor="middle">
            ACTIVITY 11.3: MEASURING THE SOLAR DAY USING A 1-METER GNOMON STICK
          </text>

          <!-- Flat Ground Surface -->
          <rect x="50" y="240" width="820" height="40" rx="6" fill="#334155" />
          <line x1="50" y1="240" x2="870" y2="240" stroke="#64748b" stroke-width="2" />
          <text x="460" y="265" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" text-anchor="middle">Level Ground Plane</text>

          <!-- Vertical Gnomon Stick -->
          <rect x="455" y="100" width="10" height="140" rx="3" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1.5" />
          <circle cx="460" cy="98" r="6" fill="#e2e8f0" />
          <text x="460" y="85" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="12" text-anchor="middle">1-meter Vertical Stick</text>

          <!-- Sun Position 1: 11:00 AM (East/Higher morning angle) -->
          <g transform="translate(240, 70)">
            <circle cx="0" cy="0" r="20" fill="#f59e0b" />
            <text x="0" y="5" fill="#78350f" font-family="'Space Grotesk', sans-serif" font-weight="800" font-size="9" text-anchor="middle">SUN</text>
            <text x="0" y="-26" fill="#fde68a" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="700" text-anchor="middle">11:00 AM</text>
            <!-- Ray through stick tip -->
            <line x1="0" y1="0" x2="220" y2="30" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,4" />
          </g>
          <!-- Long Shadow 11:00 AM (Points North-West) -->
          <line x1="465" y1="240" x2="685" y2="240" stroke="#0284c7" stroke-width="7" stroke-linecap="round" opacity="0.7" />
          <text x="695" y="235" fill="#38bdf8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600">11:00 AM Long Shadow</text>

          <!-- Sun Position 2: 12:15 PM (Solar Noon: Directly overhead / highest) -->
          <g transform="translate(460, 45)">
            <circle cx="0" cy="0" r="24" fill="#fbbf24" class="svg-glow" />
            <text x="0" y="5" fill="#78350f" font-family="'Space Grotesk', sans-serif" font-weight="800" font-size="10" text-anchor="middle">SUN</text>
            <text x="0" y="-30" fill="#fef08a" font-family="'Space Grotesk', sans-serif" font-size="12" font-weight="700" text-anchor="middle">12:15 PM (SOLAR NOON)</text>
            <!-- Vertical Ray -->
            <line x1="0" y1="24" x2="0" y2="55" stroke="#fef08a" stroke-width="2" stroke-dasharray="3,3" />
          </g>
          <!-- Shortest Shadow at Noon -->
          <line x1="465" y1="240" x2="525" y2="240" stroke="#ef4444" stroke-width="8" stroke-linecap="round" />
          <text x="535" y="228" fill="#ef4444" font-family="'Space Grotesk', sans-serif" font-size="11" font-weight="700">SHORTEST SHADOW (Solar Noon)</text>

          <!-- Sun Position 3: 1:10 PM (Afternoon) -->
          <g transform="translate(680, 80)">
            <circle cx="0" cy="0" r="20" fill="#f59e0b" />
            <text x="0" y="5" fill="#78350f" font-family="'Space Grotesk', sans-serif" font-weight="800" font-size="9" text-anchor="middle">SUN</text>
            <text x="0" y="-26" fill="#fde68a" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="700" text-anchor="middle">1:10 PM</text>
          </g>
          <!-- Shadow 1:10 PM (Points North-East) -->
          <line x1="455" y1="240" x2="260" y2="240" stroke="#0284c7" stroke-width="7" stroke-linecap="round" opacity="0.7" />
          <text x="180" y="235" fill="#38bdf8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600">1:10 PM Long Shadow</text>

          <!-- Bottom Explanation -->
          <rect x="180" y="285" width="560" height="24" rx="6" fill="rgba(255,255,255,0.08)" />
          <text x="460" y="301" fill="#cbd5e1" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" text-anchor="middle">
            Time between Shortest Shadow on Day 1 &amp; Shortest Shadow on Day 2 = <tspan fill="#38bdf8" font-weight="700">1 Solar Day (24 Hours)</tspan>
          </text>
        </svg>
        <p class="svg-caption">Figure 1.5: Principle of the Solar Gnomon. When the Sun climbs to its highest elevation in the sky, it casts the shortest shadow of the day. The interval between two consecutive shortest shadows defines our 24-hour day.</p>
      </div>

      <h4 class="nested-title">11.2.1 Lunar Calendars &amp; The 11-Day Seasonal Deficit</h4>
      <p>
        In early human civilizations, tracking the phases of the Moon was far easier than measuring the subtle orbital movements of the Sun. Anyone looking up at night could instantly identify whether it was New Moon, crescent, half, or full!
      </p>
      <p>
        Our ancestors noticed that in the time it took for the seasons to cycle once, the Moon completed roughly <strong>12 full cycles of phases</strong>. This led to the birth of <strong>Lunar Calendars</strong> (ଚାନ୍ଦ୍ର ପଞ୍ଜିକା):
      </p>
      <ul style="margin-left: 1.5rem; margin-bottom: 1.25rem; line-height: 1.8;">
        <li>1 Lunar Month = ~29.5 days</li>
        <li>1 Lunar Year = 12 lunar months &times; 29.5 days = <strong>354 days</strong></li>
      </ul>

      <div class="callout callout-warn">
        <div class="callout-header"><i class="fa-solid fa-triangle-exclamation"></i> The Problem with Pure Lunar Calendars</div>
        <p>
          A true solar year (the cycle of seasons) takes approximately <strong>365.25 days</strong>.
        </p>
        <p>
          Notice the big mathematical difference:
          <br>
          <code style="background:#fee2e2; padding:3px 8px; border-radius:4px; font-weight:700; color:#b91c1c;">Annual Deficit = 365.25 - 354 ≈ 11.25 days every year!</code>
        </p>
        <p>
          Because a pure lunar calendar is <strong>11 days shorter than the solar year</strong>, its months rapidly lose sync with the natural seasons:
        </p>
        <ul style="margin-left: 1.25rem; margin-top: 0.5rem; line-height: 1.8;">
          <li>After 3 years, the calendar is out of sync by about 33 days (over an entire month!).</li>
          <li>After 16 years, seasons completely reverse (a winter month shifts into scorching midsummer!).</li>
          <li>After about <strong>33 solar years</strong>, a month completes one full circuit through all four seasons!</li>
        </ul>
        <p style="margin-top:0.5rem;">
          <strong>Real-World Example:</strong> The Islamic Hijri calendar is a pure lunar calendar. This is why the holy month of Ramadan and the celebration of Eid-ul-Fitr move earlier by about 11 days every year in the Gregorian calendar, falling in summer during some decades and in winter during others!
        </p>
      </div>

      <h4 class="nested-title">11.2.2 Solar Calendars &amp; The Science of Leap Years</h4>
      <p>
        While tracking the Moon was simple, agriculture demanded absolute synchronization with the <strong>seasons</strong>. Farmers needed to know exactly when monsoon rains would arrive to sow seeds, and when winter frost would set in to harvest crops. If a calendar shifted seasons by 11 days each year, agricultural planning would descend into chaos!
      </p>
      <p>
        This vital economic and survival need led to the invention of <strong>Solar Calendars</strong> (ସୌର ପଞ୍ଜିକା). The modern international calendar used worldwide today—the <strong>Gregorian Calendar</strong>—is a solar calendar.
      </p>
      
      <p>
        In a solar calendar, the year is tied strictly to the revolution of Earth around the Sun. The months are assigned arbitrary lengths of 30 or 31 days (and 28 days for February) so that all 12 months add up to <strong>365 days</strong>.
      </p>

      <div class="callout callout-def">
        <div class="callout-header"><i class="fa-solid fa-calculator"></i> The Exact Science of the Leap Year</div>
        <p>
          Earth does not take exactly 365 days to orbit the Sun. It takes approximately <strong>365 days, 5 hours, 48 minutes, and 46 seconds</strong> (roughly <strong>365.2422 days</strong>, or about 365¼ days).
        </p>
        <p>
          That extra quarter-day (about 6 hours) accumulates every single year:
          <br>
          <code style="background:#e0f2fe; padding:2px 6px; border-radius:4px; font-weight:700;">4 years × ~6 hours = ~24 hours = 1 Extra Full Day!</code>
        </p>
        <p>
          To keep the calendar locked to the seasons, solar calendars add an extra day—<strong>February 29</strong>—every four years. This 366-day year is called a <strong>Leap Year</strong> (ଅଧିବର୍ଷ).
        </p>
        <p><strong>The Complete 3-Step Gregorian Leap Year Rule:</strong></p>
        <ol style="margin-left: 1.25rem; line-height: 1.8;">
          <li><strong>Divisible by 4 Rule:</strong> If a year is evenly divisible by 4, it is a leap year (e.g., 2020, 2024, 2028).</li>
          <li><strong>Century Exception (Divisible by 100):</strong> Because the extra time is slightly <em>less</em> than a full 6 hours (it is 5h 48m 46s), adding a day every 4 years adds about 11 minutes too much each year! Over 100 years, this over-correction accumulates to nearly a whole day. To fix this, century years divisible by 100 are <strong>NOT leap years</strong> (e.g., 1700, 1800, and 1900 had only 365 days!).</li>
          <li><strong>400-Year Correction:</strong> Skipping every century year lags the calendar slightly behind again. Therefore, century years that are divisible by <strong>400 ARE leap years</strong> (e.g., 1600 and 2000 were leap years; 2400 will be a leap year).</li>
        </ol>
      </div>

      <div class="callout callout-def">
        <div class="callout-header"><i class="fa-solid fa-compass-drafting"></i> A Step Further: Tropical Year vs. Sidereal Year</div>
        <p>NCERT highlights two precise ways modern astronomers measure a solar year:</p>
        <ul style="margin-left: 1.25rem; line-height: 1.8;">
          <li>
            <strong>1. Tropical Year (କ୍ରାନ୍ତିକ ବର୍ଷ - 365.2422 days):</strong>
            <br>
            The time interval between two successive <strong>Spring (Vernal) Equinoxes</strong>. It measures the exact cycle of natural seasons on Earth. The Gregorian calendar is strictly based on the tropical year.
          </li>
          <li>
            <strong>2. Sidereal Year (ନାକ୍ଷତ୍ରିକ ବର୍ଷ - 365.2564 days):</strong>
            <br>
            The time duration required for the Sun to return to the exact same position relative to the <strong>fixed stars</strong> (the stellar constellations rising at sunset).
          </li>
          <li>
            <strong>The 20-Minute Precession Difference:</strong> The sidereal year is longer than the tropical year by about <strong>20 minutes and 24 seconds</strong>! This minute difference is caused by the slow, graceful wobble of Earth's rotational axis—called <strong>axial precession</strong> (similar to how a spinning toy top slowly wobbles in a circle). One complete wobble takes approximately <strong>25,800 years</strong>!
          </li>
        </ul>
      </div>

      <h4 class="nested-title">11.2.3 Luni-Solar Calendars &amp; The Intercalary Month (Adhika Maasa)</h4>
      <p>
        What if a culture wants the best of both worlds—to use the natural, easy-to-spot phases of the Moon for counting daily dates (tithis) and celebrating religious festivals, yet remain firmly anchored to agricultural seasons?
      </p>
      <p>
        This ingenious synthesis is called a <strong>Luni-Solar Calendar</strong> (ଚାନ୍ଦ୍ର-ସୌର ପଞ୍ଜିକା). It has been used across India for millennia!
      </p>

      <div class="callout callout-def">
        <div class="callout-header"><i class="fa-solid fa-plus-circle"></i> How Luni-Solar Calendars Work: The Adhika Maasa (ଅଧିକ ମାସ)</div>
        <p>
          As we learned, 12 lunar months equal 354 days, creating an annual deficit of <strong>11 days</strong> compared to the 365-day solar year:
        </p>
        <ul style="margin-left: 1.25rem; line-height: 1.8;">
          <li>After Year 1: Calendar falls behind by 11 days.</li>
          <li>After Year 2: Calendar falls behind by 22 days.</li>
          <li>After Year 2.7 (about 32 to 33 months): The accumulated shortfall reaches <strong>~30 days</strong>—which equals <strong>one full lunar month</strong>!</li>
        </ul>
        <p>
          At this point, traditional Indian astronomers insert an <strong>extra 13th month</strong> into the year! This intercalary month is called <strong>Adhika Maasa</strong> (ଅଧିକ ମାସ), <em>Malamaasa</em> (ମଳମାସ), or <em>Purushottama Maasa</em>.
        </p>
        <p>
          By inserting this extra month approximately <strong>every 2 to 3 years (specifically, 7 times in 19 years)</strong>, the lunar months jump forward by 30 days and land back in perfect harmony with the solar seasons!
        </p>
      </div>

      <h4 class="nested-title">Amant vs. Purnimant Systems: Two Ways to Count a Month</h4>
      <p>
        Across different regions of India, traditional communities follow one of two conventions for starting and ending a lunar month:
      </p>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>System</th>
              <th>Month Begins On</th>
              <th>Month Ends On</th>
              <th>Paksha Sequence</th>
              <th>Major Regions Where Practiced</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Amant System (ଅମାନ୍ତ)</strong></td>
              <td>Day immediately after New Moon (1st day of Shukla Paksha)</td>
              <td>New Moon day (Amavasya)</td>
              <td>Shukla Paksha &rarr; Krishna Paksha</td>
              <td>Odisha (for certain solar panjikas), South India (Karnataka, Andhra Pradesh, Telangana, Tamil Nadu), Maharashtra, Gujarat</td>
            </tr>
            <tr>
              <td><strong>Purnimant System (ପୂର୍ଣ୍ଣିମାନ୍ତ)</strong></td>
              <td>Day immediately after Full Moon (1st day of Krishna Paksha)</td>
              <td>Full Moon day (Purnima)</td>
              <td>Krishna Paksha &rarr; Shukla Paksha</td>
              <td>Odisha (widely followed in traditional temple calendars and Odia Panji), North India (Uttar Pradesh, Bihar, Rajasthan, Madhya Pradesh)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- OUR SCIENTIFIC HERITAGE -->
      <h3 class="sub-title"><i class="fa-solid fa-landmark" style="color: #ea580c;"></i> Our Scientific Heritage: Ancient Indian Astronomy</h3>
      <p>
        Thousands of years before the invention of telescopes and modern clocks, ancient Indian skywatchers carefully monitored the heavens. Even without modern equipment, their meticulous, daily records allowed them to calculate the length of the solar year with astonishing precision!
      </p>

      <h4 class="nested-title">Uttarayan and Dakshinayan: The Shifting Rising Point of the Sun</h4>
      <p>
        If you stand in the exact same spot outside your home every morning, you will notice that the Sun does <strong>not always rise at the exact same point on the eastern horizon</strong>:
      </p>
      <ul style="margin-left: 1.5rem; margin-bottom: 1.25rem; line-height: 1.8;">
        <li>On the <strong>Equinoxes</strong> (around March 21 and September 23), the Sun rises <strong>due East</strong> and sets <strong>due West</strong>. Day and night are exactly equal (12 hours each) everywhere on Earth.</li>
        <li>From December 21 to June 21, the sunrise point shifts progressively towards the <strong>North of East</strong>. This apparent northward movement of the Sun is called <strong>Uttarayan (ଉତ୍ତରାୟଣ)</strong>. On the Summer Solstice (around June 21), the Sun rises at its northernmost point, bringing the longest day and shortest night of the year in India.</li>
        <li>From June 21 to December 21, the sunrise point retreats southward, shifting towards the <strong>South of East</strong>. This apparent southward movement of the Sun is called <strong>Dakshinayan (ଦକ୍ଷିଣାୟନ)</strong>. On the Winter Solstice (around December 21), the Sun rises at its southernmost point, giving us the shortest day and longest night.</li>
      </ul>

      <div class="callout callout-heritage">
        <div class="callout-header"><i class="fa-solid fa-scroll"></i> Classical Sanskrit Records: Taittirīya Saṁhitā &amp; Sūrya Siddhānta</div>
        <p>The ancient Vedic text <strong>Taittirīya Saṁhitā</strong> (verse 6.5.3) clearly documents this six-month solstitial cycle:</p>
        <p style="font-family:'Space Grotesk', serif; font-size:1.1rem; color:#78350f; font-weight:700; margin:0.5rem 0;">
          तस्मादादित्यः षण्मासा दक्षिणेनैति षडुत्तरेण ।
        </p>
        <p><em>Translation:</em> "Thus the Sun moves southwards for six months (Dakshinayan) and northwards for six months (Uttarayan)."</p>
        
        <p style="margin-top:0.75rem;">Later, the celebrated classical astronomical treatise <strong>Sūrya Siddhānta</strong> (verse 9) linked these movements directly to constellations (Rāśis):</p>
        <p style="font-family:'Space Grotesk', serif; font-size:1.1rem; color:#78350f; font-weight:700; margin:0.5rem 0;">
          भानोर्मकरसंक्रान्तेः षण्मासा उत्तरायणम् ।<br>
          कर्क्यादेस्तु तथैव स्यात् षण्मासा दक्षिणायनम् ॥
        </p>
        <p><em>Translation:</em> "From the moment the Sun enters the constellation of Capricorn (Makara), six months make up its northward progress (Uttarayan); likewise from its entrance into Cancer (Karka), six months are its southward progress (Dakshinayan)."</p>
        <p style="margin-top:0.5rem; font-size:0.92rem; color:#9a3412;">
          <strong>Why Makar Sankranti Shifted:</strong> In ancient times (~1,500 years ago), the Sun entered Capricorn on the exact day of the Winter Solstice (December 21). Because of Earth's <strong>axial precession</strong>, the sidereal calendar shifts relative to the tropical solstices by <strong>1 day every 71 years</strong>! This is why Makar Sankranti is celebrated today on <strong>January 14 or 15</strong>, about 24 days after the true winter solstice!
        </p>
      </div>

      <!-- SVG 6: Uttarayan vs. Dakshinayan Sunrise Shift on Horizon -->
      <div class="svg-container">
        <svg viewBox="0 0 920 320" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="horizonSky" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#1e1b4b" />
              <stop offset="60%" stop-color="#312e81" />
              <stop offset="100%" stop-color="#f59e0b" stop-opacity="0.4" />
            </linearGradient>
            <linearGradient id="hillsGrad" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#1e293b" />
              <stop offset="100%" stop-color="#0f172a" />
            </linearGradient>
          </defs>
          <rect width="920" height="320" rx="14" fill="url(#horizonSky)" />

          <text x="460" y="30" fill="#fde68a" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="16" text-anchor="middle">
            UTTARAYAN &amp; DAKSHINAYAN: HORIZON SUNRISE DRIFT OVER ONE YEAR
          </text>

          <!-- Horizon Mountains / Hills -->
          <path d="M 0 230 Q 120 180 220 220 T 460 210 T 680 225 T 920 200 L 920 320 L 0 320 Z" fill="url(#hillsGrad)" />
          
          <!-- Direction Labels on Horizon -->
          <line x1="50" y1="260" x2="870" y2="260" stroke="#475569" stroke-width="1.5" />
          <text x="180" y="285" fill="#38bdf8" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="14" text-anchor="middle">NORTH OF EAST</text>
          <text x="460" y="285" fill="#fef08a" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="16" text-anchor="middle">DUE EAST</text>
          <text x="740" y="285" fill="#f43f5e" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="14" text-anchor="middle">SOUTH OF EAST</text>

          <!-- Position 1: Summer Solstice (June 21) - Extreme North -->
          <g transform="translate(180, 160)">
            <circle cx="0" cy="0" r="22" fill="#38bdf8" class="svg-glow" />
            <text x="0" y="5" fill="#0f172a" font-family="'Space Grotesk', sans-serif" font-weight="800" font-size="10" text-anchor="middle">JUN 21</text>
            <text x="0" y="-30" fill="#38bdf8" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="12" text-anchor="middle">SUMMER SOLSTICE</text>
            <text x="0" y="-45" fill="#93c5fd" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" text-anchor="middle">Peak Uttarayan (Longest Day)</text>
          </g>

          <!-- Position 2: Equinoxes (March 21 & Sept 23) - Exact Due East -->
          <g transform="translate(460, 150)">
            <circle cx="0" cy="0" r="24" fill="#fbbf24" class="svg-glow" />
            <text x="0" y="5" fill="#78350f" font-family="'Space Grotesk', sans-serif" font-weight="800" font-size="10" text-anchor="middle">EQUINOX</text>
            <text x="0" y="-32" fill="#fef08a" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="12" text-anchor="middle">SPRING &amp; AUTUMN EQUINOX</text>
            <text x="0" y="-47" fill="#fde68a" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" text-anchor="middle">Rises Exactly Due East (12h Day / 12h Night)</text>
          </g>

          <!-- Position 3: Winter Solstice (Dec 21) - Extreme South -->
          <g transform="translate(740, 160)">
            <circle cx="0" cy="0" r="22" fill="#f43f5e" class="svg-glow" />
            <text x="0" y="5" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-weight="800" font-size="10" text-anchor="middle">DEC 21</text>
            <text x="0" y="-30" fill="#f87171" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="12" text-anchor="middle">WINTER SOLSTICE</text>
            <text x="0" y="-45" fill="#fca5a5" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" text-anchor="middle">Peak Dakshinayan (Shortest Day)</text>
          </g>

          <!-- Movement Arrows -->
          <!-- Uttarayan Arrow (Right to Left: Dec to June) -->
          <path d="M 700 85 Q 460 60 220 85" fill="none" stroke="#38bdf8" stroke-width="2.5" />
          <polygon points="215,85 225,80 225,90" fill="#38bdf8" />
          <text x="460" y="75" fill="#38bdf8" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="12" text-anchor="middle">
            &#10229; UTTARAYAN: Northward March (December to June)
          </text>

          <!-- Dakshinayan Arrow (Left to Right: June to Dec) -->
          <path d="M 220 110 Q 460 135 700 110" fill="none" stroke="#f43f5e" stroke-width="2.5" />
          <polygon points="705,110 695,105 695,115" fill="#f43f5e" />
          <text x="460" y="125" fill="#f87171" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="12" text-anchor="middle">
            DAKSHINAYAN: Southward March (June to December) &#10230;
          </text>
        </svg>
        <p class="svg-caption">Figure 1.6: The Annual Horizon Sunrise Drift. The Sun rises directly due East only on the two equinoxes. Throughout Uttarayan, sunrise glides northward; throughout Dakshinayan, it glides southward.</p>
      </div>

      <h4 class="nested-title">11.2.4 The Indian National Calendar (Saka Calendar)</h4>
      <p>
        When India achieved independence in 1947, over 30 different regional calendars were being used across the country! This created immense administrative confusion for national holidays, financial accounts, and official gazettes.
      </p>
      <p>
        In November 1952, the Government of India established the <strong>Calendar Reform Committee (CRC)</strong> under the Council of Scientific and Industrial Research (CSIR). The committee was chaired by the internationally renowned Indian astrophysicist <strong>Prof. Meghnad Saha</strong>.
      </p>

      <div class="callout callout-def">
        <div class="callout-header"><i class="fa-solid fa-flag"></i> Key Features of the Indian National Calendar</div>
        <p>
          Formally adopted on <strong>22 March 1957 CE (corresponding to 1 Chaitra 1879 Saka Era)</strong>:
        </p>
        <ul style="margin-left: 1.25rem; line-height: 1.8;">
          <li><strong>Solar Calendar:</strong> It is a purely solar calendar tied directly to the tropical year, consisting of 365 days in a standard year and 366 days in a leap year.</li>
          <li><strong>Starting Point:</strong> The year begins on <strong>1 Chaitra</strong>, which corresponds to <strong>March 22</strong> in a standard Gregorian year, and <strong>March 21</strong> in a Gregorian leap year (the day after the vernal equinox).</li>
          <li><strong>Month Lengths:</strong>
            <ul style="margin-top:0.25rem;">
              <li>Month 1 (Chaitra): 30 days in a normal year; 31 days in a leap year.</li>
              <li>Months 2 to 6 (Vaisakha, Jyeshtha, Ashadha, Shravana, Bhadrapada): Exactly <strong>31 days each</strong> (coinciding with the longer summer season in the northern hemisphere!).</li>
              <li>Months 7 to 12 (Ashwina, Kartika, Margashirsha, Pausha, Magha, Phalguna): Exactly <strong>30 days each</strong>.</li>
            </ul>
          </li>
          <li><strong>Leap Year Synchronization:</strong> The Saka calendar adds a leap day to Chaitra in the exact same years as the Gregorian calendar (whenever the Gregorian year is a leap year). To find the Saka year, subtract 78 from the Gregorian year (e.g., 2025 - 78 = 1947 Saka).</li>
        </ul>
      </div>

      <div class="callout callout-heritage">
        <div class="callout-header"><i class="fa-solid fa-user-astronaut"></i> Be a Scientist: Meghnad Saha (1893–1956)</div>
        <p>
          Born in Seoratali (now Bangladesh), <strong>Meghnad Saha</strong> was one of modern India's greatest astrophysicists. In 1920, he formulated the world-famous <strong>Saha Ionization Equation</strong>, which relates the ionization state of chemical elements in a star to its temperature and pressure. This equation allowed astronomers for the first time to determine the temperatures and chemical compositions of distant stars simply by analyzing their light spectra!
        </p>
        <p>
          Saha was also a dedicated institution-builder. He founded the <em>Saha Institute of Nuclear Physics</em> in Kolkata and served as Member of Parliament. As chairperson of the Calendar Reform Committee, his scientific rigor gave India an accurate, uniform national solar calendar.
        </p>
      </div>

      <!-- 11.3 ARE FESTIVALS RELATED TO ASTRONOMICAL PHENOMENA? -->
      <h3 class="sub-title"><i class="fa-solid fa-cake-candles" style="color: #d97706;"></i> 11.3 Are Festivals Related to Astronomical Phenomena?</h3>
      <p>
        Have you ever wondered why your school winter vacation or Independence Day is always on the exact same date every year, whereas <strong>Diwali, Holi, Dussehra, and Eid-ul-Fitr</strong> fall on completely different dates each year?
      </p>

      <div class="callout callout-def">
        <div class="callout-header"><i class="fa-solid fa-star-and-crescent"></i> Why Indian Festival Dates Shift in the Gregorian Calendar</div>
        <p>
          The explanation lies in the <strong>calendar system</strong> upon which the festival is calculated:
        </p>
        <ol style="margin-left: 1.25rem; line-height: 1.8;">
          <li>
            <strong>1. Festivals Based on Pure Lunar Calendars (e.g., Eid-ul-Fitr):</strong>
            <br>
            Celebrated upon sighting the delicate new crescent Moon at the end of the Islamic month of Ramadan. Because a lunar year has only 354 days, Eid occurs approximately <strong>11 days earlier</strong> in the Gregorian calendar each successive year, cycling through every season over 33 years!
          </li>
          <li>
            <strong>2. Festivals Based on Luni-Solar Calendars (e.g., Diwali, Holi, Dussehra, Buddha Purnima):</strong>
            <br>
            These festivals are tied strictly to lunar phases within designated traditional months:
            <ul style="margin-top:0.25rem;">
              <li><strong>Diwali:</strong> Celebrated on the <em>Amavasya (New Moon)</em> of the month of Kartika.</li>
              <li><strong>Holi:</strong> Celebrated on the <em>Purnima (Full Moon)</em> of the month of Phalguna.</li>
              <li><strong>Buddha Purnima:</strong> Celebrated on the <em>Purnima</em> of the month of Vaisakha.</li>
              <li><strong>Dussehra (Vijaya Dashami):</strong> Celebrated on the 10th day of the waxing moon (Shukla Dashami) of Ashwina.</li>
              <li><strong>Raksha Bandhan:</strong> Celebrated on the <em>Purnima</em> of Shravana.</li>
            </ul>
            In consecutive years, these festivals shift earlier by 11 days. But whenever the shift reaches ~30 days, the calendar inserts an <strong>Adhika Maasa</strong>, causing the festival date to leap forward by a month! This keeps the festival firmly anchored inside its natural season (e.g., Diwali is always in autumn, Holi is always in spring!).
          </li>
          <li>
            <strong>3. Festivals Based on the Solar Sidereal Calendar (e.g., Makar Sankranti, Pongal, Bihu, Pana Sankranti):</strong>
            <br>
            These celebrate the Sun entering specific constellations (Sankranti). Because they are solar, they fall on <strong>almost the exact same Gregorian date every single year</strong>!
            <ul style="margin-top:0.25rem;">
              <li><strong>Makar Sankranti / Pongal / Magh Bihu:</strong> January 14 or 15 every year.</li>
              <li><strong>Maha Bishuba Pana Sankranti (Odia New Year) / Poila Boishakh / Vaisakhi / Puthandu:</strong> April 14 or 15 every year.</li>
            </ul>
          </li>
        </ol>
      </div>

      <div class="callout callout-act">
        <div class="callout-header"><i class="fa-solid fa-location-dot"></i> Positional Astronomy Centre &amp; The Rashtriya Panchang</div>
        <p>
          In India, festival dates are traditionally calculated based on the exact lunar phase (tithi) present at <strong>sunrise</strong>. Because India spans nearly 30° of longitude, the Sun rises roughly <strong>two hours earlier in Arunachal Pradesh and Odisha than in Gujarat</strong>!
        </p>
        <p>
          On rare occasions, a tithi may change during those two hours, causing two states to calculate different festival days! To establish uniform national holidays, the <strong>Positional Astronomy Centre (PAC)</strong> of the India Meteorological Department (IMD) in Kolkata calculates celestial coordinates for a central Indian location (82.5° E longitude, near Mirzapur/Prayagraj) and officially publishes the annual <strong>Rashtriya Panchang</strong>.
        </p>
      </div>

      <div class="callout callout-heritage">
        <div class="callout-header"><i class="fa-solid fa-guitar"></i> Cultural Reverberations: Moon in Indian Music, Dance &amp; Art</div>
        <p>The beauty of the Moon has deeply enriched India's artistic heritage for centuries:</p>
        <ul style="margin-left: 1.25rem; line-height: 1.8;">
          <li><strong>Classical Ragas:</strong> Melodies inspired by moonlight include <em>Raga Chandrakauns</em>, <em>Chandranandan</em>, and <em>Shubhapantuvarali</em> (which translates to "auspicious moon").</li>
          <li><strong>Classical Dance Mudras:</strong> In Bharatanatyam, Odissi, and Kathak, dancers use precise hand gestures such as <em>Chandrakala</em> (digit of the Moon) and <em>Ardhachandran</em> (half moon) to depict celestial serenity.</li>
          <li><strong>Indigenous Tribal Art:</strong> In Odisha's tribal <em>Saura paintings (Idital)</em>, Warli wall murals in Maharashtra, Madhubani folk art in Bihar, and Gond paintings in Madhya Pradesh, the Sun and Moon are revered as eternal witnesses to human life.</li>
        </ul>
      </div>

      <!-- 11.4 WHY DO WE LAUNCH ARTIFICIAL SATELLITES? -->
      <h3 class="sub-title"><i class="fa-solid fa-satellite-dish" style="color: #0d9488;"></i> 11.4 Why Do We Launch Artificial Satellites?</h3>
      <p>
        Just as the Moon is Earth's only natural satellite, humans have built and launched thousands of <strong>Artificial Satellites</strong> (କୃତ୍ରିମ ଉପଗ୍ରହ) into space. An artificial satellite is an engineered machine placed into orbit around the Earth using multi-stage rockets.
      </p>

      <div class="callout callout-def">
        <div class="callout-header"><i class="fa-solid fa-tower-broadcast"></i> Crucial Roles of Artificial Satellites in Modern Life</div>
        <ol style="margin-left: 1.25rem; line-height: 1.8;">
          <li><strong>Telecommunication &amp; Television:</strong> Relaying live sports, mobile telephone signals, and high-speed satellite internet across continents.</li>
          <li><strong>Weather Monitoring &amp; Cyclone Early Warning:</strong> Tracking massive tropical cyclones building over the Bay of Bengal and Arabian Sea, saving hundreds of thousands of lives along coastal Odisha, Andhra Pradesh, and West Bengal!</li>
          <li><strong>Navigation &amp; Mapping:</strong> Supplying real-time coordinates for smartphones and vehicle maps via GPS and India's own sovereign satellite constellation, <strong>NavIC (Navigation with Indian Constellation)</strong>.</li>
          <li><strong>Remote Sensing &amp; Earth Observation:</strong> ISRO's <strong>Cartosat</strong> and <strong>Resourcesat</strong> series capture hyper-detailed imagery of terrain, forest cover, soil moisture, and water bodies, accessible to citizens through ISRO's <strong>Bhuvan portal</strong>.</li>
          <li><strong>Deep Space Science:</strong> <strong>AstroSat</strong> (India's dedicated multi-wavelength space observatory studying neutron stars and black holes), <strong>Aditya-L1</strong> (stationed at the Sun-Earth L1 Lagrange point to study solar flares), <strong>Chandrayaan 1, 2, 3</strong> (discovering water molecules and soft-landing on the Moon's South Pole), and <strong>Mangalyaan</strong> (Mars Orbiter Mission).</li>
          <li><strong>Student &amp; Youth Satellites:</strong> ISRO empowers university and school students to build and launch cubesats, including <em>Jugnu</em> (IIT Kanpur), <em>InspireSat-1</em>, and <em>AzaadiSat</em> (built by 750 rural schoolgirls across India!).</li>
        </ol>
      </div>

      <div class="callout callout-act">
        <div class="callout-header"><i class="fa-solid fa-binoculars"></i> Activity 11.4: Spotting an Artificial Satellite in the Twilight Sky</div>
        <p><strong>When &amp; Where to Look:</strong></p>
        <p>
          The best time is <strong>twilight</strong>—roughly 30 to 60 minutes after sunset or before sunrise. At this time, the ground where you stand is dark, but satellites orbiting hundreds of kilometers high are still fully illuminated by sunlight!
        </p>
        <p><strong>How to Distinguish a Satellite from an Aeroplane or Star:</strong></p>
        <ul style="margin-left: 1.25rem; line-height: 1.8;">
          <li><strong>Stars:</strong> Twinkle and stay fixed in constellations.</li>
          <li><strong>Aeroplanes:</strong> Have flashing, blinking red and green strobe lights and make audible engine noise.</li>
          <li><strong>Artificial Satellites:</strong> Appear as a <strong>steady, silent, non-blinking point of white light</strong> gliding smoothly and rapidly across the sky, taking just 2 to 5 minutes to travel from one horizon to the other!</li>
        </ul>
      </div>

      <div class="callout callout-warn">
        <div class="callout-header"><i class="fa-solid fa-burst"></i> A Step Further: The Menace of Space Debris (Space Junk)</div>
        <p>
          Over six decades of space exploration, thousands of spent rocket upper stages, dead satellites, and fragments from past collisions have accumulated in orbit. This is called <strong>Space Debris</strong> (ମହାକାଶ ଆବର୍ଜନା).
        </p>
        <p>
          Because objects in Low Earth Orbit travel at hyper-velocity (around <strong>7.8 km/s or 28,000 km/h</strong>), even a tiny 1-cm paint fleck carries the kinetic punch of an exploding grenade! It can shatter functioning weather satellites or endanger astronauts aboard space stations. To protect our spacecraft, ISRO established the <strong>NETRA (Network for space object Tracking and Analysis)</strong> project, and international space agencies now require satellites to perform de-orbiting burns at the end of their mission to safely burn up in the upper atmosphere.
        </p>
      </div>

      <div class="callout callout-heritage">
        <div class="callout-header"><i class="fa-solid fa-rocket"></i> Be a Scientist: Dr. Vikram Ambalal Sarabhai (1919–1971)</div>
        <p>
          Widely revered as the <strong>Father of the Indian Space Programme</strong>, Dr. Vikram Sarabhai was a visionary physicist who foresaw that space technology should not be a luxury for rich nations, but a powerful catalyst to solve real-world problems in agriculture, education, and disaster management in developing India.
        </p>
        <p>
          In 1962, he convinced Prime Minister Jawaharlal Nehru to establish the Indian National Committee for Space Research (INCOSPAR), which evolved into the <strong>Indian Space Research Organisation (ISRO)</strong> in 1969. He set up India's first rocket launching station at Thumba near Thiruvananthapuram. Today, ISRO's premier launch vehicle development centre—the <strong>Vikram Sarabhai Space Centre (VSSC)</strong>—stands proudly in his honour.
        </p>
      </div>

      <div class="callout callout-def">
        <div class="callout-header"><i class="fa-solid fa-water"></i> A Step Further: Ocean Tides &amp; The Moon's 50-Minute Rhythm</div>
        <p>
          If you visit the seaside beaches of Puri, Chandrabhaga, or Gopalpur in Odisha, you will observe the rhythmic rise and fall of ocean water levels—known as <strong>Tides (ଜୁଆର-ଭଟ୍ଟା)</strong>:
        </p>
        <ul style="margin-left: 1.25rem; line-height: 1.8;">
          <li><strong>High Tide (ଜୁଆର):</strong> Sea water surges inland, submerging sandy shorelines.</li>
          <li><strong>Low Tide (ଭଟ୍ଟା):</strong> Sea water recedes hundreds of meters back into the ocean.</li>
          <li><strong>The Astounding 50-Minute Connection:</strong> If a high tide occurs at 10:00 a.m. on Monday, the corresponding tide on Tuesday will arrive at <strong>10:50 a.m. (50 minutes later)</strong>! Why? Because ocean tides are driven primarily by the <strong>gravitational pull of the Moon</strong>. As Earth rotates, the tidal bulge stays aligned with the Moon—and as we proved earlier, the Moon advances in its orbit, rising 50 minutes later each day! The ocean's heartbeat directly mirrors the Moon's orbital rhythm!</li>
        </ul>
      </div>

      <!-- EXHAUSTIVE BILINGUAL VOCABULARY TABLE -->
      <h3 class="sub-title"><i class="fa-solid fa-language" style="color: #6366f1;"></i> Complete Bilingual Scientific Vocabulary Bank</h3>
      <p>
        Master these 32 essential scientific and astronomical terms with their grammatical parts of speech, precise English explanations, and authentic Odia translations:
      </p>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>#</th>
              <th>Term / Scientific Concept</th>
              <th>Part of Speech</th>
              <th>English Meaning &amp; Definition</th>
              <th>ଓଡ଼ିଆ ଅର୍ଥ (Odia Meaning in Script)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1</td>
              <td><strong>Celestial Body</strong></td>
              <td>Noun</td>
              <td>Any natural object located outside Earth's atmosphere in space, such as the Sun, Moon, planet, or star.</td>
              <td>ମହାଜାଗତିକ ପିଣ୍ଡ / ଖଗୋଳୀୟ ପିଣ୍ଡ</td>
            </tr>
            <tr>
              <td>2</td>
              <td><strong>Phases of the Moon</strong></td>
              <td>Noun Phrase</td>
              <td>The recurring cycle of changing shapes of the bright, sunlit portion of the Moon as viewed from Earth.</td>
              <td>ଚନ୍ଦ୍ରର କଳା / ଚନ୍ଦ୍ରର ଅବସ୍ଥା</td>
            </tr>
            <tr>
              <td>3</td>
              <td><strong>New Moon</strong></td>
              <td>Noun</td>
              <td>The lunar phase when the non-illuminated side of the Moon faces Earth, making the Moon invisible in the sky.</td>
              <td>ଅମାବାସ୍ୟା</td>
            </tr>
            <tr>
              <td>4</td>
              <td><strong>Full Moon</strong></td>
              <td>Noun</td>
              <td>The lunar phase when the entire illuminated hemisphere of the Moon faces Earth, appearing as a complete glowing circle.</td>
              <td>ପୂର୍ଣ୍ଣିମା</td>
            </tr>
            <tr>
              <td>5</td>
              <td><strong>Waxing Phase (Shukla Paksha)</strong></td>
              <td>Noun Phrase</td>
              <td>The two-week period during which the illuminated portion of the Moon visible from Earth increases in size.</td>
              <td>ଶୁକ୍ଳ ପକ୍ଷ (ବର୍ଦ୍ଧିଷ୍ଣୁ ଅବସ୍ଥା)</td>
            </tr>
            <tr>
              <td>6</td>
              <td><strong>Waning Phase (Krishna Paksha)</strong></td>
              <td>Noun Phrase</td>
              <td>The two-week period during which the illuminated portion of the Moon visible from Earth decreases in size.</td>
              <td>କୃଷ୍ଣ ପକ୍ଷ (କ୍ଷୟିଷ୍ଣୁ ଅବସ୍ଥା)</td>
            </tr>
            <tr>
              <td>7</td>
              <td><strong>Crescent Moon</strong></td>
              <td>Noun</td>
              <td>The curved sickle shape of the Moon when less than half of its visible face is illuminated by sunlight.</td>
              <td>ଅର୍ଦ୍ଧଚନ୍ଦ୍ରାକାର ଚନ୍ଦ୍ର / କଳା ଚନ୍ଦ୍ର</td>
            </tr>
            <tr>
              <td>8</td>
              <td><strong>Gibbous Moon</strong></td>
              <td>Noun</td>
              <td>The swollen phase of the Moon when more than half, but not all, of its visible face is illuminated.</td>
              <td>ଉନ୍ନତ ଚନ୍ଦ୍ର / କୁବ୍ଜ ଚନ୍ଦ୍ର</td>
            </tr>
            <tr>
              <td>9</td>
              <td><strong>First Quarter</strong></td>
              <td>Noun</td>
              <td>The phase occurring one week after New Moon when exactly half of the sunlit face is visible from Earth (waxing half).</td>
              <td>ପ୍ରଥମ ପାଦ (ଶୁକ୍ଳ ଅର୍ଦ୍ଧଚନ୍ଦ୍ର)</td>
            </tr>
            <tr>
              <td>10</td>
              <td><strong>Third / Last Quarter</strong></td>
              <td>Noun</td>
              <td>The phase occurring one week after Full Moon when exactly half of the sunlit face is visible from Earth (waning half).</td>
              <td>ତୃତୀୟ ପାଦ (କୃଷ୍ଣ ଅର୍ଦ୍ଧଚନ୍ଦ୍ର)</td>
            </tr>
            <tr>
              <td>11</td>
              <td><strong>Mean Solar Day</strong></td>
              <td>Noun Phrase</td>
              <td>The average time interval (24 hours) between two consecutive passages of the Sun across the local meridian.</td>
              <td>ମାଧ୍ୟ ସୌର ଦିବସ</td>
            </tr>
            <tr>
              <td>12</td>
              <td><strong>Local Solar Noon</strong></td>
              <td>Noun Phrase</td>
              <td>The exact moment during the day when the Sun reaches its highest point in the sky and casts the shortest shadow.</td>
              <td>ସ୍ଥାନୀୟ ମଧ୍ୟାହ୍ନ / ସର୍ବୋଚ୍ଚ ସୂର୍ଯ୍ୟ ସମୟ</td>
            </tr>
            <tr>
              <td>13</td>
              <td><strong>Gnomon</strong></td>
              <td>Noun</td>
              <td>A vertical rod, pin, or stick used in sundials to cast a shadow indicating the time of day and solar altitude.</td>
              <td>ଛାୟା ଶଙ୍କୁ</td>
            </tr>
            <tr>
              <td>14</td>
              <td><strong>Solar Year</strong></td>
              <td>Noun Phrase</td>
              <td>The time taken by the Earth to complete one full revolution around the Sun (~365.2422 days), defining the seasonal cycle.</td>
              <td>ସୌର ବର୍ଷ</td>
            </tr>
            <tr>
              <td>15</td>
              <td><strong>Lunar Year</strong></td>
              <td>Noun Phrase</td>
              <td>A period of 12 lunar synodic months (~354 days), which is about 11 days shorter than a solar year.</td>
              <td>ଚାନ୍ଦ୍ର ବର୍ଷ</td>
            </tr>
            <tr>
              <td>16</td>
              <td><strong>Luni-Solar Calendar</strong></td>
              <td>Noun Phrase</td>
              <td>A hybrid calendar system whose months are based on the Moon's phases, but which adds intercalary months to synchronize with solar seasons.</td>
              <td>ଚାନ୍ଦ୍ର-ସୌର ପଞ୍ଜିକା</td>
            </tr>
            <tr>
              <td>17</td>
              <td><strong>Intercalary Month (Adhika Maasa)</strong></td>
              <td>Noun Phrase</td>
              <td>An extra month added to a luni-solar calendar approximately every 2.7 years to bridge the 11-day annual solar-lunar shortfall.</td>
              <td>ଅଧିକ ମାସ / ମଳମାସ</td>
            </tr>
            <tr>
              <td>18</td>
              <td><strong>Amant System</strong></td>
              <td>Noun Phrase</td>
              <td>The traditional lunar calendar system where each month begins the day after New Moon and ends on the next New Moon.</td>
              <td>ଅମାନ୍ତ ପଦ୍ଧତି</td>
            </tr>
            <tr>
              <td>19</td>
              <td><strong>Purnimant System</strong></td>
              <td>Noun Phrase</td>
              <td>The traditional lunar calendar system where each month begins the day after Full Moon and ends on the next Full Moon.</td>
              <td>ପୂର୍ଣ୍ଣିମାନ୍ତ ପଦ୍ଧତି</td>
            </tr>
            <tr>
              <td>20</td>
              <td><strong>Tropical Year</strong></td>
              <td>Noun Phrase</td>
              <td>The time interval between two successive vernal equinoxes (365.2422 days), serving as the basis of solar calendars.</td>
              <td>କ୍ରାନ୍ତିକ ବର୍ଷ</td>
            </tr>
            <tr>
              <td>21</td>
              <td><strong>Sidereal Year</strong></td>
              <td>Noun Phrase</td>
              <td>The time taken by Earth to orbit the Sun relative to the background fixed stars (365.2564 days).</td>
              <td>ନାକ୍ଷତ୍ରିକ ବର୍ଷ</td>
            </tr>
            <tr>
              <td>22</td>
              <td><strong>Equinox</strong></td>
              <td>Noun</td>
              <td>The astronomical date when the Sun crosses Earth's equator, resulting in equal day and night durations (12h each) across the globe.</td>
              <td>ବିଷୁବ (ସମରାତ୍ରି-ଦିବସ)</td>
            </tr>
            <tr>
              <td>23</td>
              <td><strong>Solstice</strong></td>
              <td>Noun</td>
              <td>The astronomical date when the Sun reaches its maximum northern or southern declination, producing the longest or shortest day.</td>
              <td>ଅୟନାନ୍ତ</td>
            </tr>
            <tr>
              <td>24</td>
              <td><strong>Uttarayan</strong></td>
              <td>Noun</td>
              <td>The six-month period from December to June during which the sunrise position drifts northward and days grow longer in the northern hemisphere.</td>
              <td>ଉତ୍ତରାୟଣ (ସୂର୍ଯ୍ୟଙ୍କ ଉତ୍ତରମୁଖୀ ଗତି)</td>
            </tr>
            <tr>
              <td>25</td>
              <td><strong>Dakshinayan</strong></td>
              <td>Noun</td>
              <td>The six-month period from June to December during which the sunrise position drifts southward and days grow shorter.</td>
              <td>ଦକ୍ଷିଣାୟନ (ସୂର୍ଯ୍ୟଙ୍କ ଦକ୍ଷିଣମୁଖୀ ଗତି)</td>
            </tr>
            <tr>
              <td>26</td>
              <td><strong>Axial Precession</strong></td>
              <td>Noun Phrase</td>
              <td>The slow, continuous conical wobble of Earth's rotational axis, taking ~25,800 years to complete one full cycle.</td>
              <td>ଅକ୍ଷୀୟ ପୁରଃସରଣ / ଅକ୍ଷୀୟ ଦୋଳନ</td>
            </tr>
            <tr>
              <td>27</td>
              <td><strong>Synchronous Rotation (Tidal Locking)</strong></td>
              <td>Noun Phrase</td>
              <td>The condition in which a satellite's rotational period strictly equals its orbital revolution period, keeping one face permanently toward the planet.</td>
              <td>ସମକାଳୀନ ଘୂର୍ଣ୍ଣନ (ଜୁଆରିୟ ଆବଦ୍ଧତା)</td>
            </tr>
            <tr>
              <td>28</td>
              <td><strong>Artificial Satellite</strong></td>
              <td>Noun Phrase</td>
              <td>A human-manufactured spacecraft placed into Earth's orbit for communication, surveillance, navigation, or scientific study.</td>
              <td>କୃତ୍ରିମ ଉପଗ୍ରହ</td>
            </tr>
            <tr>
              <td>29</td>
              <td><strong>Space Debris (Space Junk)</strong></td>
              <td>Noun Phrase</td>
              <td>Defunct artificial objects, inactive satellites, and spent rocket stages orbiting Earth that pose collision hazards.</td>
              <td>ମହାକାଶ ଆବର୍ଜନା</td>
            </tr>
            <tr>
              <td>30</td>
              <td><strong>Tides</strong></td>
              <td>Noun</td>
              <td>The periodic rise and fall of coastal ocean waters driven by the differential gravitational forces of the Moon and Sun.</td>
              <td>ଜୁଆର-ଭଟ୍ଟା</td>
            </tr>
            <tr>
              <td>31</td>
              <td><strong>Tithi</strong></td>
              <td>Noun</td>
              <td>A lunar day in the Indian calendar, defined as the duration in which the Moon advances 12° in longitudinal separation from the Sun.</td>
              <td>ତିଥି</td>
            </tr>
            <tr>
              <td>32</td>
              <td><strong>Rashtriya Panchang</strong></td>
              <td>Noun Phrase</td>
              <td>The official national calendar published annually by the Government of India providing unified astronomical festival coordinates.</td>
              <td>ରାଷ୍ଟ୍ରୀୟ ପଞ୍ଜିକା</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
"""
