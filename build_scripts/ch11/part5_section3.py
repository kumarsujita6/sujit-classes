# -*- coding: utf-8 -*-
"""Part 5: Section 3 - Rapid Revision Fact & Formula/Law Bank for Class 8 Science Ch 11."""

PART5_CONTENT = """
    <!-- ========================================== -->
    <!-- SECTION 3: RAPID REVISION FACT & LAW BANK -->
    <!-- ========================================== -->
    <section id="section-3" class="study-section">
      <div class="section-badge"><i class="fa-solid fa-table"></i> Section 3 • Fact &amp; Formula Bank</div>
      <h2 class="section-title">Rapid Revision Fact &amp; Formula / Law Bank</h2>
      <p class="section-description">
        Consolidated master tables, mathematical algorithms, and comparative matrices designed for lightning-fast pre-exam revision. Contains every numerical constant, calendar conversion rule, and astronomical relationship in Chapter 11.
      </p>

      <!-- TABLE 3.1: FUNDAMENTAL MOTIONS -->
      <h3 class="sub-title"><i class="fa-solid fa-circle-nodes" style="color: #0284c7;"></i> Table 3.1: Fundamental Celestial Motions &amp; Resulting Time Units</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Celestial Motion</th>
              <th>Physical Mechanism</th>
              <th>Exact Duration</th>
              <th>Resulting Unit of Time</th>
              <th>Observable Manifestation</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Earth's Axial Rotation</strong></td>
              <td>Earth rotates from West to East around its internal tilted axis (23.5°).</td>
              <td>24 hours (Mean Solar Day); 23h 56m 4s (Sidereal Day).</td>
              <td><strong>The Day</strong> (24 hours)</td>
              <td>Apparent rising of Sun in East, progression across sky, shortest shadow at solar noon, and sunset in West.</td>
            </tr>
            <tr>
              <td><strong>Moon's Orbital Revolution</strong></td>
              <td>Moon completes one counter-clockwise revolution around Earth.</td>
              <td>29.53 days (Synodic month / New Moon to New Moon); 27.32 days (Sidereal month).</td>
              <td><strong>The Month</strong> (~29.5 days)</td>
              <td>Cycle of 8 lunar phases; Moon rises ~50 minutes later each successive day; high tides shift by 50 min.</td>
            </tr>
            <tr>
              <td><strong>Earth's Orbital Revolution</strong></td>
              <td>Earth completes one elliptical orbit around the Sun.</td>
              <td>365.2422 days (Tropical year); 365.2564 days (Sidereal year).</td>
              <td><strong>The Year</strong> (~365.25 days)</td>
              <td>Cycle of four seasons; shifting sunrise point between Uttarayan (Dec-June) and Dakshinayan (June-Dec).</td>
            </tr>
            <tr>
              <td><strong>Moon's Synchronous Rotation</strong></td>
              <td>Tidal locking: Moon's axial rotation period strictly equals its orbital revolution period.</td>
              <td>27.32 days</td>
              <td><strong>One Face Permanence</strong></td>
              <td>The same hemisphere of the Moon permanently faces Earth; the far side is never visible from Earth's surface.</td>
            </tr>
            <tr>
              <td><strong>Earth's Axial Precession</strong></td>
              <td>Earth's rotational axis slowly wobbles in space like a spinning top.</td>
              <td>~25,800 years (1° every 71.6 years)</td>
              <td><strong>Sidereal Precessional Drift</strong></td>
              <td>Solstices and equinoxes slowly drift through zodiac constellations; Makar Sankranti shifted from Dec 21 to Jan 14.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 3.2: 8 LUNAR PHASES MASTER MATRIX -->
      <h3 class="sub-title"><i class="fa-solid fa-moon" style="color: #6366f1;"></i> Table 3.2: The 8 Lunar Phases Master Reference Matrix</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Phase Name</th>
              <th>Cycle Day</th>
              <th>Fraction Lit from Earth</th>
              <th>Separation from Sun</th>
              <th>Time Overhead</th>
              <th>Best Sighting Window &amp; Direction</th>
              <th>Indian Traditional Name</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>New Moon</strong></td>
              <td>Day 0 / 29.5</td>
              <td>0% (Completely dark)</td>
              <td>0° (In line with Sun)</td>
              <td>12:00 Solar Noon</td>
              <td>Not visible (crosses sky with Sun in daytime)</td>
              <td>Amavasya (ଅମାବାସ୍ୟା)</td>
            </tr>
            <tr>
              <td><strong>Waxing Crescent</strong></td>
              <td>Days 1 – 6</td>
              <td>1% to 49% (Lit on right)</td>
              <td>45° East of Sun</td>
              <td>3:00 PM (Afternoon)</td>
              <td>Just after sunset in low western sky</td>
              <td>Shukla Pratipada to Shasthi</td>
            </tr>
            <tr>
              <td><strong>First Quarter</strong></td>
              <td>Day 7 (~1 week)</td>
              <td>50% (Right half lit)</td>
              <td>90° East of Sun</td>
              <td>6:00 PM (Sunset)</td>
              <td>Directly overhead at sunset; sets around midnight</td>
              <td>Shukla Ashtami (ଅର୍ଦ୍ଧଚନ୍ଦ୍ର)</td>
            </tr>
            <tr>
              <td><strong>Waxing Gibbous</strong></td>
              <td>Days 8 – 13</td>
              <td>51% to 99% (Bulging right)</td>
              <td>135° East of Sun</td>
              <td>9:00 PM (Late evening)</td>
              <td>Afternoon in East; high in sky most of night</td>
              <td>Shukla Navami to Chaturdashi</td>
            </tr>
            <tr>
              <td><strong>Full Moon</strong></td>
              <td>Day 14 – 15 (~2 wks)</td>
              <td>100% (Full circular disc)</td>
              <td>180° (Opposite Sun)</td>
              <td>12:00 Midnight</td>
              <td>Rises at sunset in East, visible all night, sets sunrise</td>
              <td>Purnima (ପୂର୍ଣ୍ଣିମା)</td>
            </tr>
            <tr>
              <td><strong>Waning Gibbous</strong></td>
              <td>Days 16 – 21</td>
              <td>99% down to 51% (Lit on left)</td>
              <td>135° West of Sun</td>
              <td>3:00 AM (Pre-dawn)</td>
              <td>Rises late evening; visible in western sky in morning</td>
              <td>Krishna Pratipada to Shasthi</td>
            </tr>
            <tr>
              <td><strong>Third / Last Quarter</strong></td>
              <td>Day 22 (~3 weeks)</td>
              <td>50% (Left half lit)</td>
              <td>90° West of Sun</td>
              <td>6:00 AM (Sunrise)</td>
              <td>Directly overhead at sunrise; visible in broad morning daylight</td>
              <td>Krishna Ashtami</td>
            </tr>
            <tr>
              <td><strong>Waning Crescent</strong></td>
              <td>Days 23 – 28</td>
              <td>49% down to 1% (Thin sliver left)</td>
              <td>45° West of Sun</td>
              <td>9:00 AM (Morning)</td>
              <td>Just before sunrise in low eastern sky</td>
              <td>Krishna Navami to Chaturdashi</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 3.3: MASTER CALENDAR COMPARISON -->
      <h3 class="sub-title"><i class="fa-solid fa-calendar-week" style="color: #d97706;"></i> Table 3.3: Master Comparison: Solar vs. Lunar vs. Luni-Solar Calendars</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Feature</th>
              <th>Solar Calendar</th>
              <th>Lunar Calendar</th>
              <th>Luni-Solar Calendar</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Primary Astronomical Basis</strong></td>
              <td>Earth's revolution around the Sun (Tropical Year).</td>
              <td>Moon's revolution around Earth (Synodic Months).</td>
              <td>Moon phases for months; synchronized to Sun for year.</td>
            </tr>
            <tr>
              <td><strong>Standard Year Length</strong></td>
              <td>365 days (366 days in leap year).</td>
              <td>354 days (12 &times; 29.5 days).</td>
              <td>354 days in normal year; 384 days in leap year.</td>
            </tr>
            <tr>
              <td><strong>Month Lengths</strong></td>
              <td>Arbitrary: 30, 31, or 28/29 days.</td>
              <td>Strictly alternating 29 or 30 days.</td>
              <td>Strictly lunar: 29 or 30 days (tithi based).</td>
            </tr>
            <tr>
              <td><strong>Seasonal Synchronization</strong></td>
              <td>Permanently locked to agricultural seasons.</td>
              <td><strong>Drifts completely</strong> (loses 11 days every year).</td>
              <td><strong>Permanently locked</strong> via intercalary months.</td>
            </tr>
            <tr>
              <td><strong>Correction Mechanism</strong></td>
              <td>Leap Day added to February every 4 years.</td>
              <td>None (months cycle through all seasons in 33 yrs).</td>
              <td><strong>Adhika Maasa (13th month)</strong> added every 2.7 years.</td>
            </tr>
            <tr>
              <td><strong>Prominent Examples</strong></td>
              <td>Gregorian Calendar, Indian National (Saka) Calendar.</td>
              <td>Islamic Hijri Calendar.</td>
              <td>Odia Panjika, Hindu Vikram Samvat, Hebrew Calendar.</td>
            </tr>
            <tr>
              <td><strong>Primary Utility</strong></td>
              <td>Civil governance, business, global airline scheduling.</td>
              <td>Religious observances (Ramadan, Eid, Hajj).</td>
              <td>Traditional agriculture, cultural festivals (Diwali, Holi).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 3.4: LEAP YEAR DECISION ALGORITHM -->
      <h3 class="sub-title"><i class="fa-solid fa-square-check" style="color: #0d9488;"></i> Table 3.4: Leap Year Decision Algorithm &amp; Verification Matrix</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Year Evaluated</th>
              <th>Divisible by 4?</th>
              <th>Century Year (Div by 100)?</th>
              <th>Divisible by 400?</th>
              <th>Leap Year Status</th>
              <th>Scientific Astronomical Rationale</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>1900</strong></td>
              <td>Yes (1900 ÷ 4 = 475)</td>
              <td><strong>Yes</strong> (1900 ÷ 100 = 19)</td>
              <td><strong>No</strong> (1900 ÷ 400 = 4.75)</td>
              <td><span style="color:#dc2626; font-weight:700;">NOT Leap Year (365d)</span></td>
              <td>Century exception: skips leap day to prevent 11-min annual over-accumulation.</td>
            </tr>
            <tr>
              <td><strong>2000</strong></td>
              <td>Yes (2000 ÷ 4 = 500)</td>
              <td>Yes (2000 ÷ 100 = 20)</td>
              <td><strong>Yes</strong> (2000 ÷ 400 = 5)</td>
              <td><span style="color:#16a34a; font-weight:700;">LEAP YEAR (366d)</span></td>
              <td>400-year correction: restores leap day to prevent calendar from lagging behind.</td>
            </tr>
            <tr>
              <td><strong>2024</strong></td>
              <td><strong>Yes</strong> (2024 ÷ 4 = 506)</td>
              <td>No</td>
              <td>N/A</td>
              <td><span style="color:#16a34a; font-weight:700;">LEAP YEAR (366d)</span></td>
              <td>Standard leap year; February has 29 days.</td>
            </tr>
            <tr>
              <td><strong>2025</strong></td>
              <td><strong>No</strong> (2025 ÷ 4 = 506.25)</td>
              <td>No</td>
              <td>N/A</td>
              <td><span style="color:#dc2626; font-weight:700;">Normal Year (365d)</span></td>
              <td>Earth completes ~¼ day extra which will accumulate toward 2028.</td>
            </tr>
            <tr>
              <td><strong>2100</strong></td>
              <td>Yes (2100 ÷ 4 = 525)</td>
              <td><strong>Yes</strong> (2100 ÷ 100 = 21)</td>
              <td><strong>No</strong> (2100 ÷ 400 = 5.25)</td>
              <td><span style="color:#dc2626; font-weight:700;">NOT Leap Year (365d)</span></td>
              <td>Century year not divisible by 400; February will have only 28 days.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 3.5: FESTIVAL TO ASTRONOMICAL CALENDAR MAPPING -->
      <h3 class="sub-title"><i class="fa-solid fa-fire" style="color: #ea580c;"></i> Table 3.5: Master Festival to Astronomical Calendar Mapping Guide</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Festival</th>
              <th>Calendar System</th>
              <th>Exact Astronomical Tithi / Rule</th>
              <th>Gregorian Date Behavior</th>
              <th>Underlying Scientific Rationale</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Diwali (Deepavali)</strong></td>
              <td>Luni-Solar</td>
              <td>Kartika Amavasya (New Moon)</td>
              <td>Shifts within Oct 20 – Nov 15</td>
              <td>Shifts 11 days earlier annually until Adhika Maasa resets it back to late autumn.</td>
            </tr>
            <tr>
              <td><strong>Holi</strong></td>
              <td>Luni-Solar</td>
              <td>Phalguna Purnima (Full Moon)</td>
              <td>Shifts within March 1 – March 28</td>
              <td>Tied to spring full moon; stays in spring due to intercalary corrections.</td>
            </tr>
            <tr>
              <td><strong>Buddha Purnima</strong></td>
              <td>Luni-Solar</td>
              <td>Vaisakha Purnima (Full Moon)</td>
              <td>Shifts within April 25 – May 25</td>
              <td>Celebrated on the full moon of the second Indian month.</td>
            </tr>
            <tr>
              <td><strong>Eid-ul-Fitr</strong></td>
              <td>Pure Lunar (Hijri)</td>
              <td>Sighting of 1st Waxing Crescent (Shawwal 1)</td>
              <td>Moves <strong>11 days earlier</strong> every year</td>
              <td>Pure lunar year (354d) has no Adhika Maasa; cycles through all 4 seasons in 33 years.</td>
            </tr>
            <tr>
              <td><strong>Makar Sankranti / Pongal</strong></td>
              <td>Solar Sidereal</td>
              <td>Sun enters Makara (Capricorn) constellation</td>
              <td><strong>Fixed: Jan 14 or 15</strong></td>
              <td>Tied to the sidereal solar year; shifts 1 day every 71 years due to precession.</td>
            </tr>
            <tr>
              <td><strong>Maha Bishuba Pana Sankranti (Odia New Year)</strong></td>
              <td>Solar Sidereal</td>
              <td>Sun enters Mesha (Aries) constellation</td>
              <td><strong>Fixed: April 14 or 15</strong></td>
              <td>Solar transit marking traditional spring/summer entry; identical across Odisha &amp; Bengal.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 3.6: ISRO SATELLITE MISSIONS -->
      <h3 class="sub-title"><i class="fa-solid fa-satellite" style="color: #0284c7;"></i> Table 3.6: ISRO Satellite Missions &amp; Applications Classification Bank</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Satellite / Mission</th>
              <th>Orbit Category</th>
              <th>Altitude / Location</th>
              <th>Primary Scientific &amp; Societal Function</th>
              <th>National Benefit to India</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Cartosat Series</strong></td>
              <td>Sun-Synchronous Polar LEO</td>
              <td>~500 to 600 km</td>
              <td>Sub-meter high-resolution earth imaging, cartography, infrastructure mapping.</td>
              <td>Powers ISRO's Bhuvan geoportal; city planning; border management; flood damage mapping.</td>
            </tr>
            <tr>
              <td><strong>INSAT / GSAT Series</strong></td>
              <td>Geostationary Orbit (GEO)</td>
              <td>35,786 km (Equatorial)</td>
              <td>Continuous weather surveillance, telecommunications, television broadcast, search &amp; rescue.</td>
              <td>Tracks cyclones over Bay of Bengal; transmits real-time cyclone warnings saving thousands in Odisha.</td>
            </tr>
            <tr>
              <td><strong>NavIC (IRNSS)</strong></td>
              <td>GEO &amp; Geosynchronous</td>
              <td>~36,000 km</td>
              <td>Independent regional satellite positioning system (Indian GPS).</td>
              <td>Provides accurate positioning across India and 1,500 km around borders for ships, planes, and mobile phones.</td>
            </tr>
            <tr>
              <td><strong>AstroSat</strong></td>
              <td>Equatorial LEO</td>
              <td>650 km (6° inclination)</td>
              <td>India's first multi-wavelength space astronomy observatory (optical, UV, X-ray).</td>
              <td>Simultaneous observation of cosmic objects, black holes, neutron stars, and distant star clusters.</td>
            </tr>
            <tr>
              <td><strong>Aditya-L1</strong></td>
              <td>Halo Orbit around L1</td>
              <td>1.5 million km from Earth</td>
              <td>Continuous observation of the Sun's photosphere, chromosphere, corona, and solar wind.</td>
              <td>Early warning for solar storms and coronal mass ejections that could disrupt satellites on Earth.</td>
            </tr>
            <tr>
              <td><strong>Chandrayaan 1, 2, 3</strong></td>
              <td>Lunar Polar Orbit &amp; Lander</td>
              <td>Moon (~384,400 km)</td>
              <td>Exploration of lunar surface; Chandrayaan-3 achieved historic soft landing at Moon's South Pole.</td>
              <td>Discovered water molecules on Moon (Ch-1); verified sulfur and elements at South Pole (Ch-3).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 3.7: NUMERICAL PROBLEM-SOLVING SHORTCUT MATRIX -->
      <h3 class="sub-title"><i class="fa-solid fa-calculator" style="color: #6366f1;"></i> Table 3.7: Fast Mathematical &amp; Astronomical Problem-Solving Matrix</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Problem Type</th>
              <th>Core Scientific Principle</th>
              <th>Formula / Mathematical Rule</th>
              <th>Quick Benchmark Shortcut</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Daily Moonrise Delay Calculation</strong></td>
              <td>Earth rotates 360° in 24h (1° in 4m); Moon advances 13.2° per day in its orbit.</td>
              <td><code>Delay = (360° ÷ 27.32) × 4 min/° ≈ 52.8 minutes</code></td>
              <td>Always remember: <strong>~50 minutes later each day</strong>. High tides follow the exact same ~50m delay!</td>
            </tr>
            <tr>
              <td><strong>Multiple Full Moons in Months (Pigeonhole Principle)</strong></td>
              <td>Dirichlet's Box Principle: If <em>N</em> items are placed in <em>K</em> boxes where <em>N &gt; K</em>, at least one box has &ge; 2 items.</td>
              <td><code>Items = 37 full moons; Boxes = 3 &times; 12 = 36 calendar months. Since 37 &gt; 36, &ge; 1 month has 2 full moons.</code></td>
              <td>Any time (Full Moons) &gt; (Months), at least one month MUST contain two full moons (a "Blue Moon")!</td>
            </tr>
            <tr>
              <td><strong>Seasonal Drift without Leap Years</strong></td>
              <td>Each year without leap correction loses ~0.2422 days (~¼ day) relative to tropical seasons.</td>
              <td><code>Years for Drift D = D days ÷ 0.2422 days/year</code></td>
              <td>• 1 day drift = 4 years.<br>• 1 month (30d) drift = 120 years.<br>• 6-month seasonal reversal (182.5d) = ~750 years!</td>
            </tr>
            <tr>
              <td><strong>Adhika Maasa Frequency</strong></td>
              <td>Solar year (365.25d) exceeds 12 lunar months (354d) by 11.25 days annually.</td>
              <td><code>Accumulation Time = 29.53 days ÷ 11.25 days/year ≈ 2.62 years (~32–33 months)</code></td>
              <td>An intercalary month must be added roughly <strong>every 2 to 3 years</strong> (specifically, 7 times in 19 years).</td>
            </tr>
            <tr>
              <td><strong>Solar Day vs. Sidereal Day</strong></td>
              <td>Earth rotates 360° relative to distant stars in 23h 56m 4s; must rotate extra ~1° (4m) to face Sun.</td>
              <td><code>Solar Day = Sidereal Day + (360° ÷ 365.25) &times; 4 min/° = 24h 00m 00s</code></td>
              <td>Earth rotates ~361° in a solar day; exactly 360° in a sidereal day. Difference is 3m 56s (~4 min).</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
"""
