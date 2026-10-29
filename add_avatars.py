#!/usr/bin/env python3
"""
Script to add illustrated SVG avatars to the Fourth Wing character guide.
"""

# Read the original file
with open('index.html.backup', 'r') as f:
    lines = f.readlines()

# Find the line with "const EMBEDDED = {};"
insert_line = None
for i, line in enumerate(lines):
    if 'const EMBEDDED = {};' in line:
        insert_line = i + 1
        break

if insert_line is None:
    print("Could not find insertion point")
    exit(1)

# Avatar functions to insert
avatar_functions = '''
/* =========================================================
   CHARACTER AVATARS — Illustrated SVG Portraits
   ========================================================= */

function avatarViolet(){
  return `<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" role="img">
    <defs>
      <radialGradient id="av-violet-skin" cx="50%" cy="45%" r="60%">
        <stop offset="0%" stop-color="#e8d4c8"/>
        <stop offset="100%" stop-color="#d4b8a8"/>
      </radialGradient>
      <linearGradient id="av-violet-hair" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#1a1a2e"/>
        <stop offset="100%" stop-color="#0f0f1e"/>
      </linearGradient>
    </defs>
    <rect width="100" height="100" fill="#0a0c10"/>
    <path d="M20 35 Q20 15 50 12 Q80 15 80 35 L80 55 Q80 50 75 48 Q70 46 65 48 Q60 45 50 44 Q40 45 35 48 Q30 46 25 48 Q20 50 20 55 Z" fill="url(#av-violet-hair)"/>
    <ellipse cx="50" cy="50" rx="22" ry="26" fill="url(#av-violet-skin)"/>
    <circle cx="42" cy="45" r="3.5" fill="#6b4c9a"/>
    <circle cx="58" cy="45" r="3.5" fill="#6b4c9a"/>
    <circle cx="43" cy="44" r="1.5" fill="#e8d4c8"/>
    <circle cx="59" cy="44" r="1.5" fill="#e8d4c8"/>
    <path d="M40 48 L38 52" stroke="#9d7bb8" stroke-width="0.8" fill="none" opacity="0.6"/>
    <path d="M60 48 L62 52" stroke="#9d7bb8" stroke-width="0.8" fill="none" opacity="0.6"/>
    <path d="M50 45 L50 55" stroke="#d4b8a8" stroke-width="1" fill="none"/>
    <path d="M45 60 Q50 62 55 60" stroke="#c9a896" stroke-width="1.2" fill="none" stroke-linecap="round"/>
    <path d="M35 42 Q32 40 30 42" stroke="#d4b8a8" stroke-width="0.6" fill="none" opacity="0.4"/>
    <path d="M65 42 Q68 40 70 42" stroke="#d4b8a8" stroke-width="0.6" fill="none" opacity="0.4"/>
    <rect x="45" y="72" width="10" height="8" fill="url(#av-violet-skin)"/>
  </svg>`;
}

function avatarXaden(){
  return `<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" role="img">
    <defs>
      <linearGradient id="av-xaden-hair" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#0d0d1a"/>
        <stop offset="100%" stop-color="#050508"/>
      </linearGradient>
      <radialGradient id="av-xaden-skin" cx="50%" cy="45%" r="60%">
        <stop offset="0%" stop-color="#e0ccc0"/>
        <stop offset="100%" stop-color="#c8b0a0"/>
      </radialGradient>
    </defs>
    <rect width="100" height="100" fill="#0a0c10"/>
    <ellipse cx="50" cy="50" rx="24" ry="28" fill="#1a1a2e" opacity="0.15"/>
    <path d="M18 32 Q18 12 50 10 Q82 12 82 32 L82 58 Q82 52 76 50 Q70 48 64 50 Q58 46 50 45 Q42 46 36 50 Q30 48 24 50 Q18 52 18 58 Z" fill="url(#av-xaden-hair)"/>
    <ellipse cx="50" cy="50" rx="23" ry="27" fill="url(#av-xaden-skin)"/>
    <circle cx="41" cy="44" r="3.8" fill="#2c2c3e"/>
    <circle cx="59" cy="44" r="3.8" fill="#2c2c3e"/>
    <circle cx="42" cy="43" r="1.5" fill="#8b7355"/>
    <circle cx="60" cy="43" r="1.5" fill="#8b7355"/>
    <path d="M32 48 Q30 50 32 52" stroke="#4a3f35" stroke-width="1" fill="none" opacity="0.7"/>
    <path d="M68 48 Q70 50 68 52" stroke="#4a3f35" stroke-width="1" fill="none" opacity="0.7"/>
    <path d="M50 44 L50 56" stroke="#c8b0a0" stroke-width="1.2" fill="none"/>
    <path d="M44 61 Q50 62 56 61" stroke="#b89888" stroke-width="1.2" fill="none" stroke-linecap="round"/>
    <path d="M28 55 Q28 65 50 68 Q72 65 72 55" stroke="#c8b0a0" stroke-width="0.8" fill="none" opacity="0.3"/>
    <rect x="45" y="73" width="10" height="8" fill="url(#av-xaden-skin)"/>
  </svg>`;
}

function avatarTairn(){
  return `<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" role="img">
    <defs>
      <radialGradient id="av-tairn-eye" cx="60%" cy="40%" r="50%">
        <stop offset="0%" stop-color="#ffd700"/>
        <stop offset="100%" stop-color="#daa520"/>
      </radialGradient>
    </defs>
    <rect width="100" height="100" fill="#0a0c10"/>
    <path d="M15 50 Q15 30 35 25 Q50 22 65 28 Q75 32 80 45 Q82 50 80 60 Q75 70 60 75 Q45 78 30 75 Q18 70 15 60 Z" fill="#0d0d1a" stroke="#1a1a2e" stroke-width="1"/>
    <ellipse cx="78" cy="50" rx="8" ry="10" fill="#151520"/>
    <circle cx="82" cy="50" r="1.5" fill="#0a0c10"/>
    <circle cx="55" cy="38" r="6" fill="url(#av-tairn-eye)"/>
    <circle cx="56" cy="37" r="2.5" fill="#1a1a2e" opacity="0.6"/>
    <circle cx="55" cy="38" r="6.5" fill="none" stroke="#ffd700" stroke-width="0.8" opacity="0.4"/>
    <path d="M40 20 Q35 10 38 5" stroke="#2a2a3e" stroke-width="2" fill="none" stroke-linecap="round"/>
    <path d="M60 18 Q65 8 62 3" stroke="#2a2a3e" stroke-width="2" fill="none" stroke-linecap="round"/>
    <circle cx="45" cy="45" r="2" fill="#1a1a2e" opacity="0.5"/>
    <circle cx="50" cy="52" r="1.8" fill="#1a1a2e" opacity="0.5"/>
    <circle cx="38" cy="55" r="1.5" fill="#1a1a2e" opacity="0.5"/>
    <path d="M30 60 Q50 65 75 62" stroke="#1a1a2e" stroke-width="1.2" fill="none"/>
  </svg>`;
}

function avatarAndarna(){
  return `<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" role="img">
    <defs>
      <radialGradient id="av-andarna-eye" cx="60%" cy="40%" r="50%">
        <stop offset="0%" stop-color="#ffd700"/>
        <stop offset="100%" stop-color="#daa520"/>
      </radialGradient>
    </defs>
    <rect width="100" height="100" fill="#0a0c10"/>
    <ellipse cx="50" cy="50" rx="20" ry="24" fill="#f4d03f" opacity="0.9"/>
    <path d="M35 35 Q32 25 35 20" stroke="#d4af37" stroke-width="1.5" fill="none" opacity="0.7"/>
    <path d="M50 30 Q50 18 50 12" stroke="#d4af37" stroke-width="1.5" fill="none" opacity="0.7"/>
    <path d="M65 35 Q68 25 65 20" stroke="#d4af37" stroke-width="1.5" fill="none" opacity="0.7"/>
    <ellipse cx="68" cy="50" rx="7" ry="8" fill="#f4d03f"/>
    <circle cx="52" cy="42" r="5" fill="url(#av-andarna-eye)"/>
    <circle cx="53" cy="41" r="2" fill="#0a0c10" opacity="0.7"/>
    <circle cx="52" cy="42" r="5.5" fill="none" stroke="#ffd700" stroke-width="0.7" opacity="0.5"/>
    <circle cx="72" cy="50" r="1.2" fill="#d4af37" opacity="0.6"/>
    <path d="M30 50 L25 50" stroke="#ffd700" stroke-width="0.8" opacity="0.3"/>
    <path d="M70 35 L75 30" stroke="#ffd700" stroke-width="0.8" opacity="0.3"/>
    <path d="M70 65 L75 70" stroke="#ffd700" stroke-width="0.8" opacity="0.3"/>
    <circle cx="42" cy="55" r="1.5" fill="#d4af37" opacity="0.5"/>
    <circle cx="58" cy="60" r="1.5" fill="#d4af37" opacity="0.5"/>
  </svg>`;
}

function avatarSgaeyl(){
  return `<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" role="img">
    <defs>
      <radialGradient id="av-sgaeyl-eye" cx="60%" cy="40%" r="50%">
        <stop offset="0%" stop-color="#87ceeb"/>
        <stop offset="100%" stop-color="#4a90e2"/>
      </radialGradient>
    </defs>
    <rect width="100" height="100" fill="#0a0c10"/>
    <path d="M20 50 Q20 30 40 25 Q55 22 70 30 Q80 35 82 50 Q80 65 70 72 Q55 78 40 75 Q20 70 20 50 Z" fill="#4a90e2" stroke="#2c5aa0" stroke-width="1"/>
    <ellipse cx="78" cy="50" rx="7" ry="9" fill="#5ba3f5"/>
    <circle cx="81" cy="50" r="1.3" fill="#2c5aa0"/>
    <circle cx="52" cy="40" r="5.5" fill="url(#av-sgaeyl-eye)"/>
    <circle cx="53" cy="39" r="2" fill="#0a0c10" opacity="0.7"/>
    <circle cx="52" cy="40" r="6" fill="none" stroke="#87ceeb" stroke-width="0.8" opacity="0.4"/>
    <path d="M38 22 L35 12" stroke="#2c5aa0" stroke-width="1.8" fill="none" stroke-linecap="round"/>
    <path d="M55 20 L55 8" stroke="#2c5aa0" stroke-width="1.8" fill="none" stroke-linecap="round"/>
    <path d="M72 24 L75 12" stroke="#2c5aa0" stroke-width="1.8" fill="none" stroke-linecap="round"/>
    <path d="M45 35 Q42 32 40 35" stroke="#2c5aa0" stroke-width="0.8" fill="none" opacity="0.5"/>
    <circle cx="35" cy="50" r="1.8" fill="#2c5aa0" opacity="0.6"/>
    <circle cx="48" cy="58" r="1.6" fill="#2c5aa0" opacity="0.6"/>
  </svg>`;
}

'''

# Continue with more avatars in the next part...
print(f"Will insert avatar functions at line {insert_line}")
print("Creating modified file...")

# Insert the avatar functions
lines.insert(insert_line, avatar_functions)

# Write the modified file
with open('index.html', 'w') as f:
    f.writelines(lines)

print("Avatar functions inserted successfully!")
print("File updated: index.html")
