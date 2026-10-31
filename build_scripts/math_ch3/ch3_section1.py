# -*- coding: utf-8 -*-
"""
Module: ch3_section1.py
Contains Section 1: Visual Blueprint, Interactive Audio Reader Bar,
4 Core Pedagogical Pillars, and SVG Diagram 1.1 (Grand 5-Stage Evolutionary Mind Map).
"""

def get_section_1():
    return """
    <!-- ======================================================== -->
    <!-- SECTION 1: VISUAL BLUEPRINT & DETAILED MIND MAP          -->
    <!-- ======================================================== -->
    <section id="section-1">
      <div class="section-header">
        <span class="section-badge"><i class="fa-solid fa-compass"></i> Pedagogical Architecture</span>
        <h2 class="section-title">Section 1: Visual Blueprint & Detailed Conceptual Mind Map</h2>
        <p class="section-desc">
          An architectural helicopter view of Chapter 3 — tracing the intellectual journey of humanity from physical tallies to modern place-value mathematics.
        </p>
      </div>

      <!-- AUDIO READER COMPONENT -->
      <div class="audio-player-card">
        <div class="audio-info">
          <button id="audioControlBtn" class="audio-icon-btn" onclick="toggleChapterAudio()" aria-label="Listen to Audio Summary">
            <i class="fa-solid fa-volume-high" id="audioIcon"></i>
          </button>
          <div class="audio-text">
            <h5><i class="fa-solid fa-headphones"></i> Listen to Chapter 3 Master Summary</h5>
            <p id="audioStatusText">Click play to listen to a caring teacher walk you through the Story of Numbers (Speech Synthesis).</p>
          </div>
        </div>
        <div class="audio-controls-right">
          <label for="speechRate" style="font-size: 0.85rem; font-weight: 700; color: var(--primary-dark);">Speed:</label>
          <select id="speechRate" style="padding: 0.35rem 0.65rem; border-radius: var(--radius-sm); border: 1.5px solid #bae6fd; font-weight: 700; background: white; color: var(--primary-dark);" onchange="updateSpeechRate()">
            <option value="0.85">0.85×</option>
            <option value="1.0" selected>1.0×</option>
            <option value="1.15">1.15×</option>
            <option value="1.3">1.3×</option>
          </select>
        </div>
      </div>

      <!-- 4 ARCHITECTURAL BLUEPRINT CARDS -->
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.5rem; margin-bottom: 2.5rem;">
        
        <div style="background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); border: 1px solid #bae6fd; border-radius: var(--radius-lg); padding: 1.6rem; box-shadow: var(--shadow-sm);">
          <div style="width: 44px; height: 44px; border-radius: 10px; background: #0284c7; color: white; display: flex; align-items: center; justify-content: center; font-size: 1.25rem; margin-bottom: 1rem;">
            <i class="fa-solid fa-bone"></i>
          </div>
          <h4 style="color: #0369a1; margin-bottom: 0.5rem; font-size: 1.15rem;">1. The Counting Instinct</h4>
          <p style="font-size: 0.925rem; color: #334155; line-height: 1.6; margin: 0;">
            Counting began with one-to-one mapping (cows to pebbles/sticks). Earliest mathematical artifacts like the <strong>Lebombo Bone (44,000 BCE)</strong> with 29 notches and <strong>Ishango Bone (25,000 BCE)</strong> record lunar cycles and tallies.
          </p>
        </div>

        <div style="background: linear-gradient(135deg, #f0fdfa 0%, #ccfbf1 100%); border: 1px solid #99f6e4; border-radius: var(--radius-lg); padding: 1.6rem; box-shadow: var(--shadow-sm);">
          <div style="width: 44px; height: 44px; border-radius: 10px; background: #0d9488; color: white; display: flex; align-items: center; justify-content: center; font-size: 1.25rem; margin-bottom: 1rem;">
            <i class="fa-solid fa-layer-group"></i>
          </div>
          <h4 style="color: #0f766e; margin-bottom: 0.5rem; font-size: 1.15rem;">2. Landmark & Base-n Power</h4>
          <p style="font-size: 0.925rem; color: #334155; line-height: 1.6; margin: 0;">
            Human perception has a limit (subitizing 1 to 4 items). To count higher, cultures grouped by landmarks. In a <strong>base-n system</strong> (like Egypt's base-10), landmarks are powers of n (n⁰, n¹, n², n³...), making products predictable!
          </p>
        </div>

        <div style="background: linear-gradient(135deg, #ede9fe 0%, #ddd6fe 100%); border: 1px solid #c4b5fd; border-radius: var(--radius-lg); padding: 1.6rem; box-shadow: var(--shadow-sm);">
          <div style="width: 44px; height: 44px; border-radius: 10px; background: #7c3aed; color: white; display: flex; align-items: center; justify-content: center; font-size: 1.25rem; margin-bottom: 1rem;">
            <i class="fa-solid fa-cubes-stacked"></i>
          </div>
          <h4 style="color: #6d28d9; margin-bottom: 0.5rem; font-size: 1.15rem;">3. Positional Revolution</h4>
          <p style="font-size: 0.925rem; color: #334155; line-height: 1.6; margin: 0;">
            Instead of inventing infinite symbols for larger numbers, <strong>place-value systems</strong> let the position determine the multiplier. Pioneered in Mesopotamia (Base-60), Maya (Base-20), and China (Rod Numerals with alternating Zong & Heng).
          </p>
        </div>

        <div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); border: 1px solid #fcd34d; border-radius: var(--radius-lg); padding: 1.6rem; box-shadow: var(--shadow-sm);">
          <div style="width: 44px; height: 44px; border-radius: 10px; background: #d97706; color: white; display: flex; align-items: center; justify-content: center; font-size: 1.25rem; margin-bottom: 1rem;">
            <i class="fa-solid fa-circle-notch"></i>
          </div>
          <h4 style="color: #b45309; margin-bottom: 0.5rem; font-size: 1.15rem;">4. The Crown Jewel: Zero</h4>
          <p style="font-size: 0.925rem; color: #334155; line-height: 1.6; margin: 0;">
            India united 10 digits (0-9) with decimal place value. <strong>Zero (Śūnya)</strong> was elevated from an empty placeholder to an algebraic number by Aryabhata and Brahmagupta (628 CE), forming the ring of arithmetic that powers modern science.
          </p>
        </div>

      </div>

      <!-- DETAILED SVG MIND MAP 1.1 -->
      <div class="svg-container">
        <h4 style="margin-top: 0; color: var(--dark); font-size: 1.2rem;">
          <i class="fa-solid fa-diagram-project" style="color: var(--primary);"></i>
          Diagram 1.1: The Grand 5-Stage Evolutionary Mind Map of Number Systems
        </h4>
        <svg viewBox="0 0 1100 620" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background: #fafcff; border-radius: 12px; font-family: 'Plus Jakarta Sans', sans-serif;">
          <defs>
            <linearGradient id="gradStage1" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#38bdf8"/>
              <stop offset="100%" stop-color="#0284c7"/>
            </linearGradient>
            <linearGradient id="gradStage2" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#2dd4bf"/>
              <stop offset="100%" stop-color="#0d9488"/>
            </linearGradient>
            <linearGradient id="gradStage3" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#a78bfa"/>
              <stop offset="100%" stop-color="#7c3aed"/>
            </linearGradient>
            <linearGradient id="gradStage4" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#fbbf24"/>
              <stop offset="100%" stop-color="#d97706"/>
            </linearGradient>
            <linearGradient id="gradStage5" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#f87171"/>
              <stop offset="100%" stop-color="#dc2626"/>
            </linearGradient>
            <linearGradient id="gradCenter" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#1e293b"/>
              <stop offset="100%" stop-color="#0f172a"/>
            </linearGradient>
            <filter id="shadowFilter" x="-5%" y="-5%" width="110%" height="110%">
              <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.12"/>
            </filter>
            <!-- Arrow Marker -->
            <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 1 L 10 5 L 0 9 z" fill="#64748b"/>
            </marker>
          </defs>

          <!-- CONNECTING FLOW LINES (TIMELINE BACKBONE) -->
          <path d="M 110 310 L 310 150 L 550 120 L 790 150 L 990 310 L 790 470 L 550 500 L 310 470 Z" fill="none" stroke="#e2e8f0" stroke-width="4" stroke-dasharray="8 6"/>

          <!-- CENTER MASTER NODE -->
          <g transform="translate(420, 240)" filter="url(#shadowFilter)">
            <rect width="260" height="140" rx="20" fill="url(#gradCenter)" stroke="#38bdf8" stroke-width="2.5"/>
            <text x="130" y="42" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle" letter-spacing="1">THE ULTIMATE DESTINATION</text>
            <text x="130" y="72" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-size="20" font-weight="800" text-anchor="middle">HINDU DECIMAL SYSTEM</text>
            <text x="130" y="96" fill="#cbd5e1" font-size="12" font-weight="600" text-anchor="middle">Base-10 • Place-Value • True Zero</text>
            <rect x="40" y="108" width="180" height="20" rx="10" fill="rgba(56, 189, 248, 0.15)"/>
            <text x="130" y="122" fill="#7dd3fc" font-size="10.5" font-weight="700" text-anchor="middle">Aryabhata (499 CE) & Brahmagupta (628 CE)</text>
          </g>

          <!-- STAGE 1 NODE (LEFT) -->
          <g transform="translate(30, 230)" filter="url(#shadowFilter)">
            <rect width="200" height="160" rx="16" fill="#ffffff" stroke="#0284c7" stroke-width="2"/>
            <rect width="200" height="38" rx="16" fill="url(#gradStage1)"/>
            <text x="100" y="24" fill="#ffffff" font-size="13" font-weight="800" text-anchor="middle">STAGE 1: TALLIES & TWOS</text>
            <text x="100" y="65" fill="#0369a1" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700" text-anchor="middle">One-to-One Mapping</text>
            <text x="100" y="85" fill="#475569" font-size="11.5" text-anchor="middle">• Sticks & Pebble counts</text>
            <text x="100" y="104" fill="#475569" font-size="11.5" text-anchor="middle">• Lebombo Bone (44,000 BCE)</text>
            <text x="100" y="123" fill="#475569" font-size="11.5" text-anchor="middle">• Gumulgal: urapon (1), ukasar (2)</text>
            <text x="100" y="145" fill="#0284c7" font-size="10.5" font-weight="700" text-anchor="middle">Limit: Tedious for large sets</text>
          </g>

          <!-- STAGE 2 NODE (TOP-LEFT) -->
          <g transform="translate(230, 60)" filter="url(#shadowFilter)">
            <rect width="210" height="150" rx="16" fill="#ffffff" stroke="#0d9488" stroke-width="2"/>
            <rect width="210" height="38" rx="16" fill="url(#gradStage2)"/>
            <text x="105" y="24" fill="#ffffff" font-size="13" font-weight="800" text-anchor="middle">STAGE 2: LANDMARKS</text>
            <text x="105" y="64" fill="#0f766e" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700" text-anchor="middle">Grouping by Key Anchors</text>
            <text x="105" y="84" fill="#475569" font-size="11.5" text-anchor="middle">• Roman Numerals (8th c. BCE)</text>
            <text x="105" y="103" fill="#475569" font-size="11.5" text-anchor="middle">• I, V, X, L, C, D, M (Fixed)</text>
            <text x="105" y="122" fill="#475569" font-size="11.5" text-anchor="middle">• Additive & Subtractive Rules</text>
            <text x="105" y="140" fill="#0d9488" font-size="10.5" font-weight="700" text-anchor="middle">Limit: Arithmetic nightmare</text>
          </g>

          <!-- STAGE 3 NODE (TOP-RIGHT) -->
          <g transform="translate(660, 60)" filter="url(#shadowFilter)">
            <rect width="210" height="150" rx="16" fill="#ffffff" stroke="#7c3aed" stroke-width="2"/>
            <rect width="210" height="38" rx="16" fill="url(#gradStage3)"/>
            <text x="105" y="24" fill="#ffffff" font-size="13" font-weight="800" text-anchor="middle">STAGE 3: THE BASE-n IDEA</text>
            <text x="105" y="64" fill="#6d28d9" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700" text-anchor="middle">Landmarks = Powers n⁰, n¹...</text>
            <text x="105" y="84" fill="#475569" font-size="11.5" text-anchor="middle">• Egyptian Hieroglyphs (3000 BCE)</text>
            <text x="105" y="103" fill="#475569" font-size="11.5" text-anchor="middle">• Decimal powers 10⁰ to 10⁷</text>
            <text x="105" y="122" fill="#475569" font-size="11.5" text-anchor="middle">• Regrouping: 10 of a unit = next</text>
            <text x="105" y="140" fill="#7c3aed" font-size="10.5" font-weight="700" text-anchor="middle">Limit: Infinite symbols needed</text>
          </g>

          <!-- STAGE 4A NODE (RIGHT - MESOPOTAMIA & MAYA) -->
          <g transform="translate(860, 230)" filter="url(#shadowFilter)">
            <rect width="210" height="160" rx="16" fill="#ffffff" stroke="#d97706" stroke-width="2"/>
            <rect width="210" height="38" rx="16" fill="url(#gradStage4)"/>
            <text x="105" y="24" fill="#ffffff" font-size="13" font-weight="800" text-anchor="middle">STAGE 4: PLACE VALUE</text>
            <text x="105" y="64" fill="#b45309" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700" text-anchor="middle">Position Sets Value!</text>
            <text x="105" y="84" fill="#475569" font-size="11.5" text-anchor="middle">• Babylon (2000 BCE): Base 60</text>
            <text x="105" y="103" fill="#475569" font-size="11.5" text-anchor="middle">• Maya (300 CE): Base 20 + Shell</text>
            <text x="105" y="122" fill="#475569" font-size="11.5" text-anchor="middle">• Chinese Rods: Zong / Heng</text>
            <text x="105" y="143" fill="#d97706" font-size="10.5" font-weight="700" text-anchor="middle">Invention of Empty Placeholders</text>
          </g>

          <!-- STAGE 5 SYNTHESIS (BOTTOM CALLOUT) -->
          <g transform="translate(260, 440)" filter="url(#shadowFilter)">
            <rect width="580" height="145" rx="16" fill="#ffffff" stroke="#dc2626" stroke-width="2"/>
            <rect width="580" height="36" rx="16" fill="url(#gradStage5)"/>
            <text x="290" y="24" fill="#ffffff" font-size="13.5" font-weight="800" text-anchor="middle">STAGE 5: THE INDIAN REVOLUTION & GLOBAL TRANSMISSION</text>
            <text x="20" y="65" fill="#334155" font-size="12.5" font-weight="700">1. Yajurveda Samhita:</text>
            <text x="165" y="65" fill="#475569" font-size="12">Oral powers of 10 from eka (1) to parardha (10¹²)</text>
            <text x="20" y="88" fill="#334155" font-size="12.5" font-weight="700">2. Bakhshali Manuscript (c. 3rd c. CE):</text>
            <text x="260" y="88" fill="#475569" font-size="12">Earliest zero written as a dot (bindu)</text>
            <text x="20" y="111" fill="#334155" font-size="12.5" font-weight="700">3. Aryabhata (499 CE):</text>
            <text x="160" y="111" fill="#475569" font-size="12">"Sthanat sthanam dashagunam syat" (place-to-place 10-fold rule)</text>
            <text x="20" y="133" fill="#334155" font-size="12.5" font-weight="700">4. Al-Khwarizmi & Fibonacci:</text>
            <text x="215" y="133" fill="#dc2626" font-size="11.5" font-weight="700">Transmitted to Baghdad (825 CE) and Europe (1202 CE) -> Universal standard</text>
          </g>

          <!-- DIRECTION ARROWS FROM STAGES TO CENTER -->
          <line x1="230" y1="310" x2="415" y2="310" stroke="#0284c7" stroke-width="2.5" marker-end="url(#arrow)"/>
          <line x1="390" y1="210" x2="470" y2="240" stroke="#0d9488" stroke-width="2.5" marker-end="url(#arrow)"/>
          <line x1="710" y1="210" x2="630" y2="240" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrow)"/>
          <line x1="860" y1="310" x2="685" y2="310" stroke="#d97706" stroke-width="2.5" marker-end="url(#arrow)"/>
          <line x1="550" y1="440" x2="550" y2="385" stroke="#dc2626" stroke-width="2.5" marker-end="url(#arrow)"/>
        </svg>
        <div class="svg-caption">
          <i class="fa-solid fa-circle-info"></i>
          <strong>Figure 1.1:</strong> The 5-stage architectural ascent of number systems — from prehistoric tallies to India's decimal place-value system with zero.
        </div>
      </div>

    </section>
"""
