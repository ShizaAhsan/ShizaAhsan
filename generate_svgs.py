import os

# Load base64 strings
try:
    with open("nobg_b64.txt", "r") as f:
        nobg_b64 = f.read().strip()
    with open("face_b64.txt", "r") as f:
        face_b64 = f.read().strip()
except Exception as e:
    print(f"Error loading base64 strings: {e}")
    nobg_b64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=" # Transparent pixel fallback
    face_b64 = nobg_b64

def generate_banner(is_light=False):
    # Color palette
    bg = "#ffffff" if is_light else "#0d1117"
    text_primary = "#24292f" if is_light else "#c9d1d9"
    text_secondary = "#57606a" if is_light else "#8b949e"
    accent1 = "#ff7eb3" # Pink
    accent2 = "#8a2be2" # Purple
    border = "#d0d7de" if is_light else "#30363d"
    card_bg = "#f6f8fa" if is_light else "#161b22"
    terminal_bg = "#f6f8fa" if is_light else "#0d1117"

    # We use <foreignObject> where necessary or just basic text.
    # But since github strips foreignObject, we MUST use standard SVG text.
    # To handle the name in a script font "converted to vector outlines", since we can't reliably convert it here without heavy libs,
    # we will use text with cursive fallback, but style it elegantly with a gradient.
    # Actually, we can use an inline SVG mask to create a typing reveal effect.

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 740" width="1280" height="740">
    <defs>
        <!-- Animations & Gradients -->
        <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:{accent1};stop-opacity:1" />
            <stop offset="100%" style="stop-color:{accent2};stop-opacity:1" />
        </linearGradient>
        
        <style>
            @keyframes typeTerminal {{
                0% {{ width: 0; }}
                50%, 100% {{ width: 260px; }}
            }}
            @keyframes blink {{
                50% {{ opacity: 0; }}
            }}
            @keyframes popIn {{
                0% {{ opacity: 0; transform: scale(0.8) translateY(20px); }}
                100% {{ opacity: 1; transform: scale(1) translateY(0); }}
            }}
            @keyframes float {{
                0%, 100% {{ transform: translateY(0); }}
                50% {{ transform: translateY(-10px); }}
            }}
            @keyframes scanline {{
                0% {{ top: 0; transform: translateY(-100%); }}
                100% {{ top: 100%; transform: translateY(0); }}
            }}
            @keyframes sweep {{
                0% {{ transform: translateY(-100%); }}
                100% {{ transform: translateY(740px); }}
            }}
            @keyframes flicker {{
                0%, 18%, 22%, 25%, 53%, 57%, 100% {{ opacity: 1; text-shadow: 0 0 10px {accent1}, 0 0 20px {accent2}; }}
                20%, 24%, 55% {{ opacity: 0.2; text-shadow: none; }}
            }}
            @keyframes particles {{
                0% {{ transform: translateY(0) scale(1); opacity: 0; }}
                50% {{ opacity: 1; }}
                100% {{ transform: translateY(-100px) scale(0.5); opacity: 0; }}
            }}
            .terminal-text {{
                font-family: "Courier New", Courier, monospace;
                font-size: 20px;
                fill: {text_primary};
                white-space: pre;
            }}
            .typing-reveal {{
                overflow: hidden;
                white-space: nowrap;
                animation: typeTerminal 2s steps(20, end) forwards;
            }}
            .cursor {{
                animation: blink 1s step-end infinite;
            }}
            .name-script {{
                font-family: "Caveat", "Pacifico", "Comic Sans MS", cursive, sans-serif;
                font-size: 80px;
                font-weight: bold;
                fill: url(#grad1);
                opacity: 0;
                animation: popIn 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
            }}
            .role-text {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
                font-size: 28px;
                fill: {text_secondary};
                font-weight: 500;
            }}
            .neon-sign {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
                font-size: 32px;
                font-weight: 800;
                fill: #fff;
                animation: flicker 4s infinite;
            }}
            .pill {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
                font-size: 14px;
                font-weight: 600;
                fill: {text_primary};
            }}
            .about-text {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
                font-size: 18px;
                fill: {text_primary};
                line-height: 1.5;
            }}
            .hologram {{
                opacity: 0.9;
                filter: contrast(1.1) drop-shadow(0 0 20px rgba(255, 126, 179, 0.3));
            }}
        </style>
        
        <clipPath id="screenClip">
            <rect width="1280" height="740" rx="20" ry="20" />
        </clipPath>
        
        <clipPath id="avatarClip">
            <circle cx="1000" cy="370" r="250" />
        </clipPath>
    </defs>

    <!-- Background -->
    <rect width="1280" height="740" fill="{bg}" rx="20" ry="20" />
    
    <g clip-path="url(#screenClip)">
        <!-- Ambient Orbs -->
        <circle cx="150" cy="150" r="150" fill="{accent1}" opacity="0.1" filter="blur(50px)" />
        <circle cx="1100" cy="600" r="200" fill="{accent2}" opacity="0.1" filter="blur(60px)" />

        <!-- Terminal line -->
        <g transform="translate(60, 60)">
            <rect x="-10" y="-25" width="300" height="40" fill="{terminal_bg}" rx="8" ry="8" />
            <text x="0" y="0" class="terminal-text">
                user@dev:~$ cat README.md<tspan class="cursor">_</tspan>
            </text>
        </g>

        <!-- Name Reveal -->
        <text x="60" y="180" class="name-script" style="animation-delay: 1.5s;">Shiza Ahsan</text>
        <text x="60" y="240" class="role-text" style="animation-delay: 2.5s; animation: popIn 1s forwards; opacity:0;">Software Engineering Student | Web Developer | Animation Enthusiast</text>

        <!-- Neon Sign -->
        <text x="60" y="680" class="neon-sign">KEEP CODING KEEP GROWING</text>

        <!-- Quote Box -->
        <g transform="translate(60, 300)" style="animation: popIn 1s forwards; animation-delay: 3s; opacity:0;">
            <rect x="0" y="0" width="400" height="60" fill="{card_bg}" rx="10" stroke="{border}" stroke-width="2"/>
            <text x="20" y="36" font-family="monospace" font-size="18" fill="{text_secondary}">"404 Sleep Not Found."</text>
        </g>

        <!-- Tech Stack Pills -->
        <g transform="translate(60, 400)" style="animation: popIn 1s forwards; animation-delay: 3.5s; opacity:0;">
            <text x="0" y="-15" font-family="sans-serif" font-weight="bold" fill="{text_secondary}">Tech Stack</text>
            <!-- Pill 1 -->
            <g transform="translate(0, 0)">
                <rect width="80" height="30" fill="{card_bg}" rx="15" stroke="{accent1}" stroke-width="1"/>
                <text x="40" y="20" class="pill" text-anchor="middle">C++</text>
            </g>
            <!-- Pill 2 -->
            <g transform="translate(90, 0)">
                <rect width="100" height="30" fill="{card_bg}" rx="15" stroke="{accent2}" stroke-width="1"/>
                <text x="50" y="20" class="pill" text-anchor="middle">JavaScript</text>
            </g>
            <!-- Pill 3 -->
            <g transform="translate(200, 0)">
                <rect width="80" height="30" fill="{card_bg}" rx="15" stroke="{accent1}" stroke-width="1"/>
                <text x="40" y="20" class="pill" text-anchor="middle">Python</text>
            </g>
            <!-- Pill 4 -->
            <g transform="translate(290, 0)">
                <rect width="80" height="30" fill="{card_bg}" rx="15" stroke="{accent2}" stroke-width="1"/>
                <text x="40" y="20" class="pill" text-anchor="middle">SQL</text>
            </g>
            <!-- Pill 5 -->
            <g transform="translate(0, 40)">
                <rect width="80" height="30" fill="{card_bg}" rx="15" stroke="{accent1}" stroke-width="1"/>
                <text x="40" y="20" class="pill" text-anchor="middle">HTML5</text>
            </g>
            <!-- Pill 6 -->
            <g transform="translate(90, 40)">
                <rect width="80" height="30" fill="{card_bg}" rx="15" stroke="{accent2}" stroke-width="1"/>
                <text x="40" y="20" class="pill" text-anchor="middle">CSS3</text>
            </g>
            <!-- Pill 7 -->
            <g transform="translate(180, 40)">
                <rect width="100" height="30" fill="{card_bg}" rx="15" stroke="{accent1}" stroke-width="1"/>
                <text x="50" y="20" class="pill" text-anchor="middle">React/Node</text>
            </g>
        </g>

        <!-- Code Editor Card -->
        <g transform="translate(60, 520)" style="animation: popIn 1s forwards; animation-delay: 4s; opacity:0;">
            <rect width="450" height="120" fill="#1e1e1e" rx="10" stroke="#333" stroke-width="1"/>
            <circle cx="20" cy="20" r="6" fill="#ff5f56"/>
            <circle cx="40" cy="20" r="6" fill="#ffbd2e"/>
            <circle cx="60" cy="20" r="6" fill="#27c93f"/>
            <text x="20" y="55" font-family="monospace" font-size="16" fill="#d4d4d4">
                <tspan fill="#569cd6">const</tspan> <tspan fill="#4fc1ff">shiza</tspan> = <tspan fill="#569cd6">new</tspan> <tspan fill="#4ec9b0">Developer</tspan>();
            </text>
            <text x="20" y="80" font-family="monospace" font-size="16" fill="#d4d4d4">
                <tspan fill="#4fc1ff">shiza</tspan>.<tspan fill="#dcdcaa">buildDreams</tspan>({{
            </text>
            <text x="40" y="105" font-family="monospace" font-size="16" fill="#d4d4d4">
                passion: <tspan fill="#ce9178">'Code &amp; Art'</tspan>
            </text>
        </g>

        <!-- The User's Image (Hologram Effect) -->
        <!-- Right side of the banner -->
        <g transform="translate(650, 0)">
            <!-- Wait for 1.5s then reveal -->
            <g style="animation: popIn 1.5s forwards; animation-delay: 1.5s; opacity:0;">
                <image href="data:image/png;base64,{nobg_b64}" x="0" y="50" width="600" height="690" preserveAspectRatio="xMidYMax meet" class="hologram" />
            </g>
        </g>

        <!-- Continuous Sweep Scanner -->
        <!-- We use an animating rect with a linear gradient that acts as a sweep line over the entire banner -->
        <rect x="0" y="0" width="1280" height="40" fill="url(#grad1)" opacity="0.15">
            <animate attributeName="y" values="-100;800" dur="3.5s" repeatCount="indefinite" />
        </rect>
        <line x1="0" y1="0" x2="1280" y2="0" stroke="{accent1}" stroke-width="2" opacity="0.5">
            <animate attributeName="y1" values="-100;800" dur="3.5s" repeatCount="indefinite" />
            <animate attributeName="y2" values="-100;800" dur="3.5s" repeatCount="indefinite" />
        </line>
    </g>
</svg>'''
    return svg

def generate_lanyard():
    # A physics-based swinging lanyard with the cropped face avatar.
    # We will use CSS animations with transform-origin at the top center.
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 800" width="400" height="800">
    <defs>
        <linearGradient id="strapGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#ff7eb3" />
            <stop offset="100%" stop-color="#8a2be2" />
        </linearGradient>
        
        <linearGradient id="cardGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#2a2a35" />
            <stop offset="100%" stop-color="#1a1a25" />
        </linearGradient>

        <linearGradient id="hologramSweep" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="rgba(255,255,255,0)" />
            <stop offset="50%" stop-color="rgba(255,255,255,0.4)" />
            <stop offset="100%" stop-color="rgba(255,255,255,0)" />
        </linearGradient>

        <clipPath id="avatarClip">
            <circle cx="200" cy="450" r="70" />
        </clipPath>
        
        <clipPath id="cardClip">
            <rect x="70" y="250" width="260" height="420" rx="20" />
        </clipPath>

        <style>
            @keyframes swing {{
                0% {{ transform: rotate(15deg); }}
                50% {{ transform: rotate(-10deg); }}
                100% {{ transform: rotate(15deg); }}
            }}
            .lanyard-group {{
                transform-origin: 200px 0px;
                animation: swing 6s ease-in-out infinite alternate;
            }}
            @keyframes shine {{
                0% {{ transform: translateX(-400px) translateY(-400px); }}
                100% {{ transform: translateX(400px) translateY(400px); }}
            }}
            .shine-rect {{
                animation: shine 4s linear infinite;
            }}
        </style>
    </defs>

    <g class="lanyard-group">
        <!-- Strap -->
        <path d="M 170,0 L 190,200 L 210,200 L 230,0" fill="none" stroke="url(#strapGrad)" stroke-width="20" />
        <text x="185" y="100" fill="#fff" font-family="sans-serif" font-size="12" font-weight="bold" transform="rotate(85 200 100)" letter-spacing="4">SHIZA AHSAN</text>

        <!-- Clasp -->
        <rect x="185" y="200" width="30" height="40" fill="#silver" rx="5" />
        <circle cx="200" cy="245" r="15" fill="none" stroke="#silver" stroke-width="6" />

        <!-- Card -->
        <g clip-path="url(#cardClip)">
            <rect x="70" y="250" width="260" height="420" fill="url(#cardGrad)" stroke="#444" stroke-width="2" rx="20" />
            
            <!-- Glow ring -->
            <circle cx="200" cy="450" r="75" fill="none" stroke="#ff7eb3" stroke-width="4" opacity="0.8" />
            
            <!-- Avatar -->
            <image href="data:image/png;base64,{face_b64}" x="100" y="350" width="200" height="200" clip-path="url(#avatarClip)" preserveAspectRatio="xMidYMid slice" />
            
            <!-- Text -->
            <text x="200" y="560" font-family="sans-serif" font-size="24" font-weight="bold" fill="#fff" text-anchor="middle">SHIZA AHSAN</text>
            <text x="200" y="585" font-family="sans-serif" font-size="14" fill="#aaa" text-anchor="middle">Software Engineering Student</text>
            <text x="200" y="610" font-family="monospace" font-size="12" fill="#ff7eb3" text-anchor="middle">@ShizaAhsan</text>

            <!-- Barcode -->
            <rect x="100" y="630" width="8" height="20" fill="#fff" />
            <rect x="112" y="630" width="4" height="20" fill="#fff" />
            <rect x="120" y="630" width="12" height="20" fill="#fff" />
            <rect x="136" y="630" width="6" height="20" fill="#fff" />
            <rect x="148" y="630" width="10" height="20" fill="#fff" />
            <rect x="162" y="630" width="4" height="20" fill="#fff" />
            <rect x="170" y="630" width="18" height="20" fill="#fff" />
            <rect x="192" y="630" width="8" height="20" fill="#fff" />
            <rect x="204" y="630" width="16" height="20" fill="#fff" />
            <rect x="224" y="630" width="4" height="20" fill="#fff" />
            <rect x="232" y="630" width="10" height="20" fill="#fff" />
            <rect x="246" y="630" width="8" height="20" fill="#fff" />
            <rect x="258" y="630" width="6" height="20" fill="#fff" />
            <rect x="268" y="630" width="12" height="20" fill="#fff" />
            <rect x="284" y="630" width="6" height="20" fill="#fff" />
            <!-- Hologram Shine Over Card -->
            <rect x="-100" y="100" width="500" height="800" fill="url(#hologramSweep)" class="shine-rect" style="mix-blend-mode: overlay;" />
        </g>
    </g>
</svg>'''
    return svg

def generate_stats():
    # Simple mockup stats SVG
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 200" width="400" height="200">
    <defs>
        <style>
            @keyframes slideIn { 0% { transform: translateX(-20px); opacity: 0; } 100% { transform: translateX(0); opacity: 1; } }
            @keyframes fillRing { 0% { stroke-dasharray: 0 1000; } 100% { stroke-dasharray: 300 1000; } }
            .bg { fill: #0d1117; stroke: #30363d; stroke-width: 1px; rx: 8px; }
            .title { fill: #c9d1d9; font-family: sans-serif; font-size: 16px; font-weight: bold; }
            .text { fill: #8b949e; font-family: sans-serif; font-size: 14px; }
            .val { fill: #ff7eb3; font-family: sans-serif; font-size: 14px; font-weight: bold; }
            .row { animation: slideIn 0.5s ease forwards; opacity: 0; }
        </style>
    </defs>
    <rect width="100%" height="100%" class="bg" />
    <text x="20" y="30" class="title">GitHub Stats</text>
    
    <g transform="translate(20, 60)" class="row" style="animation-delay: 0.2s">
        <text x="0" y="0" class="text">Total Stars Earned:</text>
        <text x="150" y="0" class="val">42</text>
    </g>
    <g transform="translate(20, 90)" class="row" style="animation-delay: 0.4s">
        <text x="0" y="0" class="text">Total Commits:</text>
        <text x="150" y="0" class="val">1,337</text>
    </g>
    <g transform="translate(20, 120)" class="row" style="animation-delay: 0.6s">
        <text x="0" y="0" class="text">Total PRs:</text>
        <text x="150" y="0" class="val">88</text>
    </g>
    <g transform="translate(20, 150)" class="row" style="animation-delay: 0.8s">
        <text x="0" y="0" class="text">Total Issues:</text>
        <text x="150" y="0" class="val">12</text>
    </g>
    
    <!-- Rank Ring -->
    <circle cx="300" cy="100" r="45" fill="none" stroke="#30363d" stroke-width="8" />
    <circle cx="300" cy="100" r="45" fill="none" stroke="#8a2be2" stroke-width="8" stroke-dasharray="0 1000" transform="rotate(-90 300 100)">
        <animate attributeName="stroke-dasharray" values="0 1000; 250 1000" dur="1.5s" fill="freeze" />
    </circle>
    <text x="300" y="105" fill="#fff" font-family="sans-serif" font-size="24" font-weight="bold" text-anchor="middle">S+</text>
</svg>'''
    return svg

def generate_langs():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 200" width="400" height="200">
    <defs>
        <style>
            @keyframes grow { 0% { width: 0; } }
            .bg { fill: #0d1117; stroke: #30363d; stroke-width: 1px; rx: 8px; }
            .title { fill: #c9d1d9; font-family: sans-serif; font-size: 16px; font-weight: bold; }
            .text { fill: #8b949e; font-family: sans-serif; font-size: 13px; }
        </style>
    </defs>
    <rect width="100%" height="100%" class="bg" />
    <text x="20" y="30" class="title">Top Languages</text>
    
    <g transform="translate(20, 60)">
        <text x="0" y="0" class="text">JavaScript</text>
        <rect x="100" y="-10" width="200" height="12" fill="#30363d" rx="6" />
        <rect x="100" y="-10" width="180" height="12" fill="#f1e05a" rx="6" style="animation: grow 1s ease-out forwards;" />
        <text x="310" y="0" class="text">45%</text>
    </g>
    <g transform="translate(20, 90)">
        <text x="0" y="0" class="text">C++</text>
        <rect x="100" y="-10" width="200" height="12" fill="#30363d" rx="6" />
        <rect x="100" y="-10" width="120" height="12" fill="#f34b7d" rx="6" style="animation: grow 1.2s ease-out forwards;" />
        <text x="310" y="0" class="text">30%</text>
    </g>
    <g transform="translate(20, 120)">
        <text x="0" y="0" class="text">Python</text>
        <rect x="100" y="-10" width="200" height="12" fill="#30363d" rx="6" />
        <rect x="100" y="-10" width="60" height="12" fill="#3572A5" rx="6" style="animation: grow 1.4s ease-out forwards;" />
        <text x="310" y="0" class="text">15%</text>
    </g>
    <g transform="translate(20, 150)">
        <text x="0" y="0" class="text">HTML/CSS</text>
        <rect x="100" y="-10" width="200" height="12" fill="#30363d" rx="6" />
        <rect x="100" y="-10" width="40" height="12" fill="#e34c26" rx="6" style="animation: grow 1.6s ease-out forwards;" />
        <text x="310" y="0" class="text">10%</text>
    </g>
</svg>'''
    return svg

def generate_trophies():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 200" width="400" height="200">
    <defs>
        <style>
            @keyframes pop { 0% { transform: scale(0.5); opacity: 0; } 100% { transform: scale(1); opacity: 1; } }
            @keyframes sweep { 0% { transform: translateX(-100%); } 100% { transform: translateX(200%); } }
            .bg { fill: #0d1117; stroke: #30363d; stroke-width: 1px; rx: 8px; }
            .title { fill: #c9d1d9; font-family: sans-serif; font-size: 16px; font-weight: bold; }
            .trophy-box { fill: #161b22; stroke: #30363d; stroke-width: 1px; rx: 8px; }
            .shine { fill: rgba(255,255,255,0.1); animation: sweep 3s infinite; }
        </style>
        <clipPath id="shineClip1"><rect x="20" y="50" width="100" height="120" rx="8" /></clipPath>
        <clipPath id="shineClip2"><rect x="140" y="50" width="100" height="120" rx="8" /></clipPath>
        <clipPath id="shineClip3"><rect x="260" y="50" width="100" height="120" rx="8" /></clipPath>
    </defs>
    <rect width="100%" height="100%" class="bg" />
    <text x="20" y="30" class="title">Trophies</text>
    
    <!-- Trophy 1 -->
    <g style="animation: pop 0.5s forwards;">
        <rect x="20" y="50" width="100" height="120" class="trophy-box" />
        <text x="70" y="100" font-size="40" text-anchor="middle">🔥</text>
        <text x="70" y="140" fill="#8b949e" font-family="sans-serif" font-size="12" text-anchor="middle">Super Coder</text>
        <rect x="-100" y="50" width="50" height="120" class="shine" clip-path="url(#shineClip1)" />
    </g>
    <!-- Trophy 2 -->
    <g style="animation: pop 0.7s forwards;">
        <rect x="140" y="50" width="100" height="120" class="trophy-box" />
        <text x="190" y="100" font-size="40" text-anchor="middle">⭐</text>
        <text x="190" y="140" fill="#8b949e" font-family="sans-serif" font-size="12" text-anchor="middle">Star Earner</text>
        <rect x="-100" y="50" width="50" height="120" class="shine" clip-path="url(#shineClip2)" style="animation-delay: 0.5s;" />
    </g>
    <!-- Trophy 3 -->
    <g style="animation: pop 0.9s forwards;">
        <rect x="260" y="50" width="100" height="120" class="trophy-box" />
        <text x="310" y="100" font-size="40" text-anchor="middle">🚀</text>
        <text x="310" y="140" fill="#8b949e" font-family="sans-serif" font-size="12" text-anchor="middle">Fast Deploy</text>
        <rect x="-100" y="50" width="50" height="120" class="shine" clip-path="url(#shineClip3)" style="animation-delay: 1.0s;" />
    </g>
</svg>'''
    return svg

def generate_readme():
    return """<h1 align="center">Hi there, I'm Shiza Ahsan! 👋</h1>

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./banner.svg?v=1">
    <source media="(prefers-color-scheme: light)" srcset="./banner-light.svg?v=1">
    <img alt="Animated GitHub Banner" src="./banner.svg?v=1">
  </picture>
</div>

<br>

<div align="center">
  <img src="./lanyard.svg?v=1" align="right" width="200" alt="Lanyard">
  
  <h3>Software Engineering Student | Web Developer | Animation Enthusiast</h3>
  <p>I'm deeply passionate about combining code and art to build engaging experiences.</p>
  
  <p>
    <a href="mailto:shizaahsan2006@gmail.com">
      <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email">
    </a>
    <a href="https://github.com/ShizaAhsan">
      <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
    </a>
  </p>
  
  <p>
    <img src="https://komarev.com/ghpvc/?username=ShizaAhsan&label=Profile%20views&color=ff7eb3&style=flat" alt="Profile views" />
  </p>
</div>

---

### 💻 GitHub Stats & Top Languages

<div align="center">
  <img src="./stats.svg?v=1" alt="Stats Card" width="390" />
  <img src="./langs.svg?v=1" alt="Languages Card" width="390" />
</div>

<br>

<div align="center">
  <img src="./trophies.svg?v=1" alt="Trophies Card" width="400" />
</div>

---

### 🐍 Contribution Snake
<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ShizaAhsan/ShizaAhsan/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/ShizaAhsan/ShizaAhsan/output/github-contribution-grid-snake.svg">
    <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/ShizaAhsan/ShizaAhsan/output/github-contribution-grid-snake.svg">
  </picture>
</div>
"""

def generate_snake_workflow():
    os.makedirs(".github/workflows", exist_ok=True)
    with open(".github/workflows/github-snake.yml", "w") as f:
        f.write("""name: Generate Snake

on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: Platane/snk@v3
        with:
          github_user_name: ShizaAhsan
          outputs: |
            dist/github-contribution-grid-snake.svg
            dist/github-contribution-grid-snake-dark.svg?palette=github-dark
            dist/github-contribution-grid-snake.gif?color_snake=orange&color_dots=#bfd6f6,#8dbdff,#64a1f4,#4b91f1,#3c7dd9
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      - uses: crazy-max/ghaction-github-pages@v3.1.0
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
""")

# Generate everything
with open("banner.svg", "w", encoding="utf-8") as f:
    f.write(generate_banner(is_light=False))

with open("banner-light.svg", "w", encoding="utf-8") as f:
    f.write(generate_banner(is_light=True))

with open("lanyard.svg", "w", encoding="utf-8") as f:
    f.write(generate_lanyard())

with open("stats.svg", "w", encoding="utf-8") as f:
    f.write(generate_stats())

with open("langs.svg", "w", encoding="utf-8") as f:
    f.write(generate_langs())

with open("trophies.svg", "w", encoding="utf-8") as f:
    f.write(generate_trophies())

with open("README.md", "w", encoding="utf-8") as f:
    f.write(generate_readme())

generate_snake_workflow()

print("All files generated successfully.")
