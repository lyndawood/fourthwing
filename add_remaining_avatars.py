# Read the file
with open('index.html', 'r') as f:
    content = f.read()

# Find the avatars object and add more characters
old_avatars = '''  const avatars = {
    violet: avatarViolet,
    xaden: avatarXaden,
    tairn: avatarTairn
  };'''

new_avatars = '''  const avatars = {
    violet: avatarViolet,
    xaden: avatarXaden,
    tairn: avatarTairn,
    andarna: avatarAndarna,
    sgaeyl: avatarSgaeyl,
    rhiannon: avatarRhiannon,
    ridoc: avatarRidoc,
    sawyer: avatarSawyer,
    liam: avatarLiam,
    dain: avatarDain,
    mira: avatarMira,
    brennan: avatarBrennan,
    lilith: avatarLilith,
    imogen: avatarImogen,
    bodhi: avatarBodhi
  };'''

# Additional avatar functions to insert after avatarTairn
additional_avatars = '''
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

function avatarRhiannon(){
  return `<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" role="img">
    <defs>
      <radialGradient id="av-rhiannon-skin" cx="50%" cy="45%" r="60%">
        <stop offset="0%" stop-color="#e8d4c8"/>
        <stop offset="100%" stop-color="#d4b8a8"/>
      </radialGradient>
      <linearGradient id="av-rhiannon-hair" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#5c4033"/>
        <stop offset="100%" stop-color="#3e2723"/>
      </linearGradient>
    </defs>
    <rect width="100" height="100" fill="#0a0c10"/>
    <path d="M18 35 Q18 15 50 12 Q82 15 82 35 L82 55 Q82 50 76 48 Q70 46 64 48 Q58 45 50 44 Q42 45 36 48 Q30 46 24 48 Q18 50 18 55 Z" fill="url(#av-rhiannon-hair)"/>
    <ellipse cx="50" cy="50" rx="22" ry="26" fill="url(#av-rhiannon-skin)"/>
    <circle cx="42" cy="45" r="3.5" fill="#5c4033"/>
    <circle cx="58" cy="45" r="3.5" fill="#5c4033"/>
    <circle cx="43" cy="44" r="1.5" fill="#e8d4c8"/>
    <circle cx="59" cy="44" r="1.5" fill="#e8d4c8"/>
    <path d="M35 42 Q32 40 30 42" stroke="#d4b8a8" stroke-width="0.6" fill="none" opacity="0.4"/>
    <path d="M65 42 Q68 40 70 42" stroke="#d4b8a8" stroke-width="0.6" fill="none" opacity="0.4"/>
    <path d="M50 45 L50 55" stroke="#d4b8a8" stroke-width="1" fill="none"/>
    <path d="M44 60 Q50 62 56 60" stroke="#c9a896" stroke-width="1.2" fill="none" stroke-linecap="round"/>
    <path d="M28 55 Q28 65 50 68 Q72 65 72 55" stroke="#d4b8a8" stroke-width="0.8" fill="none" opacity="0.3"/>
    <rect x="45" y="72" width="10" height="8" fill="url(#av-rhiannon-skin)"/>
  </svg>`;
}

function avatarRidoc(){
  return `<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" role="img">
    <defs>
      <radialGradient id="av-ridoc-skin" cx="50%" cy="45%" r="60%">
        <stop offset="0%" stop-color="#e8d4c8"/>
        <stop offset="100%" stop-color="#d4b8a8"/>
      </radialGradient>
      <linearGradient id="av-ridoc-hair" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#6b4423"/>
        <stop offset="100%" stop-color="#4a2c17"/>
      </linearGradient>
    </defs>
    <rect width="100" height="100" fill="#0a0c10"/>
    <path d="M20 32 Q20 12 50 10 Q80 12 80 32 L80 56 Q80 50 74 48 Q68 46 62 48 Q56 45 50 44 Q44 45 38 48 Q32 46 26 48 Q20 50 20 56 Z" fill="url(#av-ridoc-hair)"/>
    <ellipse cx="50" cy="50" rx="21" ry="25" fill="url(#av-ridoc-skin)"/>
    <circle cx="42" cy="46" r="3.2" fill="#6b4423"/>
    <circle cx="58" cy="46" r="3.2" fill="#6b4423"/>
    <circle cx="43" cy="45" r="1.3" fill="#e8d4c8"/>
    <circle cx="59" cy="45" r="1.3" fill="#e8d4c8"/>
    <path d="M38 48 Q36 50 38 52" stroke="#d4b8a8" stroke-width="0.6" fill="none" opacity="0.3"/>
    <path d="M62 48 Q64 50 62 52" stroke="#d4b8a8" stroke-width="0.6" fill="none" opacity="0.3"/>
    <path d="M50 46 L50 56" stroke="#d4b8a8" stroke-width="0.9" fill="none"/>
    <path d="M43 61 Q50 63 57 61" stroke="#c9a896" stroke-width="1.1" fill="none" stroke-linecap="round"/>
    <circle cx="38" cy="62" r="0.8" fill="#d4b8a8" opacity="0.4"/>
    <rect x="45" y="72" width="10" height="8" fill="url(#av-ridoc-skin)"/>
  </svg>`;
}

function avatarSawyer(){
  return `<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" role="img">
    <defs>
      <radialGradient id="av-sawyer-skin" cx="50%" cy="45%" r="60%">
        <stop offset="0%" stop-color="#e8d4c8"/>
        <stop offset="100%" stop-color="#d4b8a8"/>
      </radialGradient>
      <linearGradient id="av-sawyer-hair" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#c85a3a"/>
        <stop offset="100%" stop-color="#a0421f"/>
      </linearGradient>
    </defs>
    <rect width="100" height="100" fill="#0a0c10"/>
    <path d="M18 35 Q18 15 50 12 Q82 15 82 35 L82 55 Q82 50 76 48 Q70 46 64 48 Q58 45 50 44 Q42 45 36 48 Q30 46 24 48 Q18 50 18 55 Z" fill="url(#av-sawyer-hair)"/>
    <ellipse cx="50" cy="50" rx="22" ry="26" fill="url(#av-sawyer-skin)"/>
    <circle cx="42" cy="45" r="3.5" fill="#5c4033"/>
    <circle cx="58" cy="45" r="3.5" fill="#5c4033"/>
    <circle cx="43" cy="44" r="1.5" fill="#e8d4c8"/>
    <circle cx="59" cy="44" r="1.5" fill="#e8d4c8"/>
    <path d="M35 42 Q32 40 30 42" stroke="#d4b8a8" stroke-width="0.6" fill="none" opacity="0.4"/>
    <path d="M50 45 L50 55" stroke="#d4b8a8" stroke-width="1" fill="none"/>
    <path d="M45 60 Q50 61 55 60" stroke="#c9a896" stroke-width="1.1" fill="none" stroke-linecap="round"/>
    <circle cx="38" cy="52" r="0.6" fill="#c85a3a" opacity="0.4"/>
    <circle cx="62" cy="52" r="0.6" fill="#c85a3a" opacity="0.4"/>
    <rect x="45" y="72" width="10" height="8" fill="url(#av-sawyer-skin)"/>
  </svg>`;
}

function avatarLiam(){
  return `<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" role="img">
    <defs>
      <radialGradient id="av-liam-skin" cx="50%" cy="45%" r="60%">
        <stop offset="0%" stop-color="#e8d4c8"/>
        <stop offset="100%" stop-color="#d4b8a8"/>
      </radialGradient>
      <linearGradient id="av-liam-hair" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#d4a574"/>
        <stop offset="100%" stop-color="#b8885c"/>
      </linearGradient>
    </defs>
    <rect width="100" height="100" fill="#0a0c10"/>
    <path d="M18 35 Q18 15 50 12 Q82 15 82 35 L82 55 Q82 50 76 48 Q70 46 64 48 Q58 45 50 44 Q42 45 36 48 Q30 46 24 48 Q18 50 18 55 Z" fill="url(#av-liam-hair)"/>
    <ellipse cx="50" cy="50" rx="22" ry="26" fill="url(#av-liam-skin)"/>
    <circle cx="42" cy="45" r="3.5" fill="#8b6f47"/>
    <circle cx="58" cy="45" r="3.5" fill="#8b6f47"/>
    <circle cx="43" cy="44" r="1.5" fill="#e8d4c8"/>
    <circle cx="59" cy="44" r="1.5" fill="#e8d4c8"/>
    <path d="M35 42 Q32 41 30 42" stroke="#d4b8a8" stroke-width="0.6" fill="none" opacity="0.3"/>
    <path d="M65 42 Q68 41 70 42" stroke="#d4b8a8" stroke-width="0.6" fill="none" opacity="0.3"/>
    <path d="M50 45 L50 55" stroke="#d4b8a8" stroke-width="1" fill="none"/>
    <path d="M44 60 Q50 62 56 60" stroke="#c9a896" stroke-width="1.2" fill="none" stroke-linecap="round"/>
    <path d="M38 48 Q36 50 38 52" stroke="#d4b8a8" stroke-width="0.5" fill="none" opacity="0.3"/>
    <path d="M62 48 Q64 50 62 52" stroke="#d4b8a8" stroke-width="0.5" fill="none" opacity="0.3"/>
    <rect x="45" y="72" width="10" height="8" fill="url(#av-liam-skin)"/>
  </svg>`;
}

function avatarDain(){
  return `<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" role="img">
    <defs>
      <radialGradient id="av-dain-skin" cx="50%" cy="45%" r="60%">
        <stop offset="0%" stop-color="#e8d4c8"/>
        <stop offset="100%" stop-color="#d4b8a8"/>
      </radialGradient>
      <linearGradient id="av-dain-hair" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#3d3d4d"/>
        <stop offset="100%" stop-color="#1a1a2e"/>
      </linearGradient>
    </defs>
    <rect width="100" height="100" fill="#0a0c10"/>
    <path d="M18 35 Q18 15 50 12 Q82 15 82 35 L82 55 Q82 50 76 48 Q70 46 64 48 Q58 45 50 44 Q42 45 36 48 Q30 46 24 48 Q18 50 18 55 Z" fill="url(#av-dain-hair)"/>
    <ellipse cx="50" cy="50" rx="22" ry="26" fill="url(#av-dain-skin)"/>
    <circle cx="42" cy="45" r="3.5" fill="#4a5568"/>
    <circle cx="58" cy="45" r="3.5" fill="#4a5568"/>
    <circle cx="43" cy="44" r="1.5" fill="#e8d4c8"/>
    <circle cx="59" cy="44" r="1.5" fill="#e8d4c8"/>
    <path d="M35 42 Q32 40 30 42" stroke="#d4b8a8" stroke-width="0.6" fill="none" opacity="0.4"/>
    <path d="M65 42 Q68 40 70 42" stroke="#d4b8a8" stroke-width="0.6" fill="none" opacity="0.4"/>
    <path d="M50 45 L50 55" stroke="#d4b8a8" stroke-width="1" fill="none"/>
    <path d="M45 60 Q50 61 55 60" stroke="#c9a896" stroke-width="1.1" fill="none" stroke-linecap="round"/>
    <rect x="45" y="72" width="10" height="8" fill="url(#av-dain-skin)"/>
  </svg>`;
}

function avatarMira(){
  return `<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" role="img">
    <defs>
      <radialGradient id="av-mira-skin" cx="50%" cy="45%" r="60%">
        <stop offset="0%" stop-color="#e8d4c8"/>
        <stop offset="100%" stop-color="#d4b8a8"/>
      </radialGradient>
      <linearGradient id="av-mira-hair" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#1a1a2e"/>
        <stop offset="100%" stop-color="#0f0f1e"/>
      </linearGradient>
    </defs>
    <rect width="100" height="100" fill="#0a0c10"/>
    <path d="M18 35 Q18 15 50 12 Q82 15 82 35 L82 55 Q82 50 76 48 Q70 46 64 48 Q58 45 50 44 Q42 45 36 48 Q30 46 24 48 Q18 50 18 55 Z" fill="url(#av-mira-hair)"/>
    <ellipse cx="50" cy="50" rx="22" ry="26" fill="url(#av-mira-skin)"/>
    <circle cx="42" cy="45" r="3.5" fill="#3d3d4d"/>
    <circle cx="58" cy="45" r="3.5" fill="#3d3d4d"/>
    <circle cx="43" cy="44" r="1.5" fill="#e8d4c8"/>
    <circle cx="59" cy="44" r="1.5" fill="#e8d4c8"/>
    <path d="M35 42 Q32 39 30 42" stroke="#d4b8a8" stroke-width="0.7" fill="none" opacity="0.5"/>
    <path d="M65 42 Q68 39 70 42" stroke="#d4b8a8" stroke-width="0.7" fill="none" opacity="0.5"/>
    <path d="M50 45 L50 55" stroke="#d4b8a8" stroke-width="1" fill="none"/>
    <path d="M45 60 Q50 61 55 60" stroke="#c9a896" stroke-width="1.2" fill="none" stroke-linecap="round"/>
    <path d="M48 58 L49 62" stroke="#b89888" stroke-width="0.6" fill="none" opacity="0.4"/>
    <rect x="45" y="72" width="10" height="8" fill="url(#av-mira-skin)"/>
  </svg>`;
}

function avatarBrennan(){
  return `<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" role="img">
    <defs>
      <radialGradient id="av-brennan-skin" cx="50%" cy="45%" r="60%">
        <stop offset="0%" stop-color="#e8d4c8"/>
        <stop offset="100%" stop-color="#d4b8a8"/>
      </radialGradient>
      <linearGradient id="av-brennan-hair" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#5c4033"/>
        <stop offset="100%" stop-color="#3e2723"/>
      </linearGradient>
    </defs>
    <rect width="100" height="100" fill="#0a0c10"/>
    <path d="M18 35 Q18 15 50 12 Q82 15 82 35 L82 55 Q82 50 76 48 Q70 46 64 48 Q58 45 50 44 Q42 45 36 48 Q30 46 24 48 Q18 50 18 55 Z" fill="url(#av-brennan-hair)"/>
    <ellipse cx="50" cy="50" rx="22" ry="26" fill="url(#av-brennan-skin)"/>
    <circle cx="42" cy="45" r="3.5" fill="#5c4033"/>
    <circle cx="58" cy="45" r="3.5" fill="#5c4033"/>
    <circle cx="43" cy="44" r="1.5" fill="#e8d4c8"/>
    <circle cx="59" cy="44" r="1.5" fill="#e8d4c8"/>
    <path d="M35 42 Q32 41 30 42" stroke="#d4b8a8" stroke-width="0.6" fill="none" opacity="0.3"/>
    <path d="M50 45 L50 55" stroke="#d4b8a8" stroke-width="1" fill="none"/>
    <path d="M44 60 Q50 62 56 60" stroke="#c9a896" stroke-width="1.2" fill="none" stroke-linecap="round"/>
    <circle cx="42" cy="45" r="4" fill="none" stroke="#d4af37" stroke-width="0.5" opacity="0.3"/>
    <circle cx="58" cy="45" r="4" fill="none" stroke="#d4af37" stroke-width="0.5" opacity="0.3"/>
    <rect x="45" y="72" width="10" height="8" fill="url(#av-brennan-skin)"/>
  </svg>`;
}

function avatarLilith(){
  return `<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" role="img">
    <defs>
      <radialGradient id="av-lilith-skin" cx="50%" cy="45%" r="60%">
        <stop offset="0%" stop-color="#e8d4c8"/>
        <stop offset="100%" stop-color="#d4b8a8"/>
      </radialGradient>
      <linearGradient id="av-lilith-hair" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#1a1a2e"/>
        <stop offset="100%" stop-color="#0f0f1e"/>
      </linearGradient>
    </defs>
    <rect width="100" height="100" fill="#0a0c10"/>
    <path d="M18 35 Q18 15 50 12 Q82 15 82 35 L82 55 Q82 50 76 48 Q70 46 64 48 Q58 45 50 44 Q42 45 36 48 Q30 46 24 48 Q18 50 18 55 Z" fill="url(#av-lilith-hair)"/>
    <ellipse cx="50" cy="50" rx="22" ry="26" fill="url(#av-lilith-skin)"/>
    <circle cx="42" cy="45" r="3.5" fill="#2c2c3e"/>
    <circle cx="58" cy="45" r="3.5" fill="#2c2c3e"/>
    <circle cx="43" cy="44" r="1.5" fill="#e8d4c8"/>
    <circle cx="59" cy="44" r="1.5" fill="#e8d4c8"/>
    <path d="M35 42 Q32 39 30 42" stroke="#d4b8a8" stroke-width="0.7" fill="none" opacity="0.5"/>
    <path d="M65 42 Q68 39 70 42" stroke="#d4b8a8" stroke-width="0.7" fill="none" opacity="0.5"/>
    <path d="M50 45 L50 55" stroke="#d4b8a8" stroke-width="1" fill="none"/>
    <path d="M45 60 Q50 60 55 60" stroke="#c9a896" stroke-width="1.2" fill="none" stroke-linecap="round"/>
    <path d="M28 55 Q28 65 50 68 Q72 65 72 55" stroke="#d4b8a8" stroke-width="1" fill="none" opacity="0.4"/>
    <rect x="45" y="72" width="10" height="8" fill="url(#av-lilith-skin)"/>
  </svg>`;
}

function avatarImogen(){
  return `<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" role="img">
    <defs>
      <radialGradient id="av-imogen-skin" cx="50%" cy="45%" r="60%">
        <stop offset="0%" stop-color="#e8d4c8"/>
        <stop offset="100%" stop-color="#d4b8a8"/>
      </radialGradient>
      <linearGradient id="av-imogen-hair" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#ff69b4"/>
        <stop offset="100%" stop-color="#db1f7d"/>
      </linearGradient>
    </defs>
    <rect width="100" height="100" fill="#0a0c10"/>
    <path d="M18 35 Q18 15 50 12 Q82 15 82 35 L82 55 Q82 50 76 48 Q70 46 64 48 Q58 45 50 44 Q42 45 36 48 Q30 46 24 48 Q18 50 18 55 Z" fill="url(#av-imogen-hair)"/>
    <ellipse cx="50" cy="50" rx="22" ry="26" fill="url(#av-imogen-skin)"/>
    <circle cx="42" cy="45" r="3.5" fill="#3d3d4d"/>
    <circle cx="58" cy="45" r="3.5" fill="#3d3d4d"/>
    <circle cx="43" cy="44" r="1.5" fill="#e8d4c8"/>
    <circle cx="59" cy="44" r="1.5" fill="#e8d4c8"/>
    <path d="M35 42 Q32 39 30 42" stroke="#d4b8a8" stroke-width="0.7" fill="none" opacity="0.5"/>
    <path d="M65 42 Q68 39 70 42" stroke="#d4b8a8" stroke-width="0.7" fill="none" opacity="0.5"/>
    <path d="M50 45 L50 55" stroke="#d4b8a8" stroke-width="1" fill="none"/>
    <path d="M44 60 Q50 61 56 60" stroke="#c9a896" stroke-width="1.2" fill="none" stroke-linecap="round"/>
    <circle cx="50" cy="50" r="23" fill="none" stroke="#ff69b4" stroke-width="0.5" opacity="0.2"/>
    <rect x="45" y="72" width="10" height="8" fill="url(#av-imogen-skin)"/>
  </svg>`;
}

function avatarBodhi(){
  return `<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" role="img">
    <defs>
      <radialGradient id="av-bodhi-skin" cx="50%" cy="45%" r="60%">
        <stop offset="0%" stop-color="#e8d4c8"/>
        <stop offset="100%" stop-color="#d4b8a8"/>
      </radialGradient>
      <linearGradient id="av-bodhi-hair" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#3d3d4d"/>
        <stop offset="100%" stop-color="#1a1a2e"/>
      </linearGradient>
    </defs>
    <rect width="100" height="100" fill="#0a0c10"/>
    <path d="M18 35 Q18 15 50 12 Q82 15 82 35 L82 55 Q82 50 76 48 Q70 46 64 48 Q58 45 50 44 Q42 45 36 48 Q30 46 24 48 Q18 50 18 55 Z" fill="url(#av-bodhi-hair)"/>
    <ellipse cx="50" cy="50" rx="22" ry="26" fill="url(#av-bodhi-skin)"/>
    <circle cx="42" cy="45" r="3.5" fill="#4a5568"/>
    <circle cx="58" cy="45" r="3.5" fill="#4a5568"/>
    <circle cx="43" cy="44" r="1.5" fill="#e8d4c8"/>
    <circle cx="59" cy="44" r="1.5" fill="#e8d4c8"/>
    <path d="M35 42 Q32 40 30 42" stroke="#d4b8a8" stroke-width="0.6" fill="none" opacity="0.4"/>
    <path d="M50 45 L50 55" stroke="#d4b8a8" stroke-width="1" fill="none"/>
    <path d="M45 60 Q50 61 55 60" stroke="#c9a896" stroke-width="1.1" fill="none" stroke-linecap="round"/>
    <circle cx="50" cy="50" r="23" fill="none" stroke="#d4af37" stroke-width="0.5" opacity="0.2"/>
    <rect x="45" y="72" width="10" height="8" fill="url(#av-bodhi-skin)"/>
  </svg>`;
}

'''

# Insert additional avatars after avatarTairn
marker = 'function avatarTairn(){'
if marker in content:
    # Find the end of avatarTairn function
    start_pos = content.find(marker)
    # Find the closing brace of the function
    brace_count = 0
    in_function = False
    end_pos = start_pos
    for i in range(start_pos, len(content)):
        if content[i] == '{':
            brace_count += 1
            in_function = True
        elif content[i] == '}':
            brace_count -= 1
            if in_function and brace_count == 0:
                end_pos = i + 1
                break
    
    # Insert the additional avatars after avatarTairn
    content = content[:end_pos] + additional_avatars + content[end_pos:]
    print("Added 12 additional avatar functions")
else:
    print("ERROR: Could not find avatarTairn function")
    exit(1)

# Update the avatars object
if old_avatars in content:
    content = content.replace(old_avatars, new_avatars)
    print("Updated avatars object with all 15 characters")
else:
    print("ERROR: Could not find avatars object to update")
    exit(1)

# Write the updated file
with open('index.html', 'w') as f:
    f.write(content)

print("SUCCESS: All 15 illustrated avatars added!")
