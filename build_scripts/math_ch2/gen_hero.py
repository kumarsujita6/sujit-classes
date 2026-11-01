# -*- coding: utf-8 -*-
"""
Hero Section and Navigation Wrapper
"""

def get_hero_and_nav():
    return '''<body>
  <!-- READING PROGRESS BAR -->
  <div id="progressBarContainer">
    <div id="progressBar"></div>
  </div>

  <!-- STICKY TOP NAVBAR -->
  <nav class="top-nav">
    <a href="../../index.html" class="nav-brand">
      <i class="fa-solid fa-shapes"></i>
      <span>Sujit Classes</span>
    </a>
    <div class="nav-links">
      <a href="#section-1" class="nav-link">Blueprint</a>
      <a href="#section-2" class="nav-link">Concepts &amp; Odia</a>
      <a href="#section-3" class="nav-link">Formula Bank</a>
      <a href="#section-4" class="nav-link">NCERT Solutions</a>
      <a href="#section-5" class="nav-link">Exam Bank</a>
      <a href="#section-6" class="nav-link">Trap Alerts</a>
    </div>
    <button class="btn-audio" onclick="toggleAudioNarrator()" id="navAudioBtn">
      <i class="fa-solid fa-volume-high"></i>
      <span id="navAudioText">Listen Note</span>
    </button>
  </nav>

  <div class="container">
    <!-- HERO SECTION -->
    <header class="hero">
      <div class="hero-badges">
        <span class="badge badge-gold"><i class="fa-solid fa-award"></i> NCERT NEP 2020 Edition</span>
        <span class="badge badge-white"><i class="fa-solid fa-book"></i> Ganita Prakash • Code: gegp102</span>
        <span class="badge badge-white"><i class="fa-solid fa-landmark"></i> CBSE &amp; BSE Odisha Curriculum</span>
        <span class="badge badge-white"><i class="fa-solid fa-certificate"></i> 100% Zero-Omission Master Note</span>
      </div>
      <h1>Arithmetic Expressions</h1>
      <p style="font-family: 'Noto Sans Oriya', 'Plus Jakarta Sans', sans-serif; font-size: 1.4rem; color: #fde047; font-weight: 600; margin-bottom: 0.5rem;">
        ଦ୍ୱିତୀୟ ଅଧ୍ୟାୟ: ପାଟୀଗାଣିତିକ ରାଶି
      </p>
      <p>
        The definitive, high-performance study note for Class 7 Mathematics. Master the structural anatomy of mathematical terms, 
        commutative and associative laws, bracket unpacking mechanisms, the geometric power of the distributive law, 
        and 100% fully solved in-text activities, 'Figure it Out' prompts, and competency-based exam problems.
      </p>
      <div class="hero-meta">
        <span><i class="fa-solid fa-graduation-cap"></i> Target Audience: Class 7 Students (English &amp; Odia Medium)</span>
        <span><i class="fa-solid fa-diagram-project"></i> 6 Intricate Responsive SVG Diagrams</span>
        <span><i class="fa-solid fa-clock"></i> Est. Study Time: 2.5 Hours</span>
        <span><i class="fa-solid fa-file-circle-check"></i> 100% Solved NCERT &amp; Teacher Manual Solutions</span>
      </div>
    </header>

    <!-- ACTION TOOLBAR -->
    <div class="action-bar">
      <div class="action-group">
        <a href="#section-4" class="btn-action btn-primary-action">
          <i class="fa-solid fa-square-root-variable"></i> Jump to Solved NCERT (100%)
        </a>
        <a href="#section-5" class="btn-action btn-secondary-action">
          <i class="fa-solid fa-trophy"></i> Practice Exam Question Bank
        </a>
        <a href="#section-2" class="btn-action" style="background: #f1f5f9; color: #334155;">
          <i class="fa-solid fa-language"></i> 30-Term Bilingual Glossary (Odia)
        </a>
      </div>
      <div class="action-group">
        <button class="btn-audio" onclick="toggleAudioNarrator()">
          <i class="fa-solid fa-headphones"></i> Listen to Audio Summary
        </button>
      </div>
    </div>
'''
