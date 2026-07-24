import os

try:
    with open("nobg_b64.txt", "r") as f:
        nobg_b64 = f.read().strip()
    with open("face_b64.txt", "r") as f:
        face_b64 = f.read().strip()
except Exception as e:
    nobg_b64 = ""
    face_b64 = ""

# COLORS (Based on the screenshot's dark purple aesthetic)
BG = "#0d1117"
PANEL_BG = "#161b22"
BORDER = "#4d3472"
TEXT_MAIN = "#c9d1d9"
TEXT_DIM = "#8b949e"
ACCENT_PINK = "#ff7eb3"
ACCENT_PURPLE = "#b266ff"

def generate_banner(is_light=False):
    # Ignoring light for now, forcing dark aesthetic to match screenshot
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600" width="100%" height="100%">
    <defs>
        <linearGradient id="gradText" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="{ACCENT_PURPLE}" />
            <stop offset="100%" stop-color="{ACCENT_PINK}" />
        </linearGradient>
        <style>
            .font-mono {{ font-family: "Courier New", monospace; }}
            .font-sans {{ font-family: -apple-system, sans-serif; }}
            .font-cursive {{ font-family: "Caveat", "Pacifico", "Comic Sans MS", cursive, sans-serif; font-weight: bold; }}
            
            .terminal {{ font-size: 14px; fill: {ACCENT_PINK}; font-weight: bold; }}
            .title-small {{ font-size: 24px; fill: #fff; font-weight: bold; }}
            .name {{ font-size: 64px; fill: url(#gradText); }}
            .role {{ font-size: 16px; fill: {TEXT_MAIN}; font-weight: bold; }}
            .box-text {{ font-size: 16px; fill: #fff; font-weight: 500; font-style: italic; }}
            .section-title {{ font-size: 16px; fill: #fff; font-weight: bold; }}
            .pill-text {{ font-size: 12px; fill: #fff; font-weight: bold; }}
            .bullet {{ font-size: 12px; fill: {TEXT_MAIN}; }}
            
            .code-text {{ font-size: 12px; fill: #8b949e; white-space: pre; }}
            .code-hi {{ fill: {ACCENT_PINK}; }}
            .code-kw {{ fill: #79c0ff; }}
            .code-str {{ fill: #a5d6ff; }}
            
            @keyframes slideRight {{ from {{ transform: translateX(-20px); opacity: 0; }} to {{ transform: translateX(0); opacity: 1; }} }}
            @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
            @keyframes float {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-10px); }} }}
            @keyframes neon {{ 0%, 100% {{ filter: drop-shadow(0 0 5px {ACCENT_PINK}); }} 50% {{ filter: drop-shadow(0 0 15px {ACCENT_PINK}); }} }}
            
            .animate-slide {{ animation: slideRight 0.8s ease forwards; opacity: 0; }}
            .animate-fade {{ animation: fadeIn 1s ease forwards; opacity: 0; }}
            .animate-float {{ animation: float 6s ease-in-out infinite; }}
            .animate-neon {{ animation: neon 2s ease-in-out infinite; }}
        </style>
        <clipPath id="bannerClip">
            <rect width="1000" height="600" rx="10" />
        </clipPath>
        <filter id="glow">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>

    <g clip-path="url(#bannerClip)">
        <!-- Background -->
        <rect width="1000" height="600" fill="{BG}" stroke="{BORDER}" stroke-width="2" rx="10" />
        
        <!-- Ambient background glows -->
        <circle cx="200" cy="200" r="150" fill="{ACCENT_PURPLE}" opacity="0.05" filter="blur(40px)" />
        <circle cx="800" cy="400" r="200" fill="{ACCENT_PINK}" opacity="0.05" filter="blur(60px)" />

        <!-- Left Content Group -->
        <g transform="translate(40, 50)">
            <g class="animate-slide" style="animation-delay: 0.1s;">
                <text x="0" y="0" class="font-mono terminal">user@dev:~$ cat README.md</text>
            </g>
            
            <g class="animate-slide" style="animation-delay: 0.2s;">
                <text x="0" y="40" class="font-sans title-small">Hi, I'm 👋</text>
            </g>
            
            <g class="animate-slide" style="animation-delay: 0.3s;">
                <text x="0" y="100" class="font-cursive name">Shiza Ahsan 💖</text>
            </g>
            
            <g class="animate-slide" style="animation-delay: 0.4s;">
                <text x="0" y="140" class="font-mono role">&lt; Software Engineering Student /&gt;</text>
            </g>
            
            <g class="animate-slide" style="animation-delay: 0.5s;">
                <!-- Tagline Box -->
                <rect x="0" y="160" width="350" height="50" fill="{PANEL_BG}" stroke="{BORDER}" stroke-width="1" rx="8" />
                <text x="20" y="190" class="font-sans box-text">" 404 Sleep Not Found. "</text>
            </g>
            
            <g class="animate-slide" style="animation-delay: 0.6s;" transform="translate(0, 240)">
                <text x="0" y="0" class="font-sans section-title">💡 Tech I Know</text>
                
                <!-- Pills Row 1 -->
                <g transform="translate(0, 20)">
                    <rect x="0" y="0" width="60" height="24" fill="#E34F26" fill-opacity="0.2" stroke="#E34F26" rx="12" />
                    <text x="30" y="16" class="font-sans pill-text" text-anchor="middle" fill="#E34F26">HTML</text>
                    
                    <rect x="70" y="0" width="50" height="24" fill="#1572B6" fill-opacity="0.2" stroke="#1572B6" rx="12" />
                    <text x="95" y="16" class="font-sans pill-text" text-anchor="middle" fill="#1572B6">CSS</text>
                    
                    <rect x="130" y="0" width="80" height="24" fill="#F7DF1E" fill-opacity="0.2" stroke="#F7DF1E" rx="12" />
                    <text x="170" y="16" class="font-sans pill-text" text-anchor="middle" fill="#F7DF1E">JavaScript</text>
                    
                    <rect x="220" y="0" width="60" height="24" fill="#61DAFB" fill-opacity="0.2" stroke="#61DAFB" rx="12" />
                    <text x="250" y="16" class="font-sans pill-text" text-anchor="middle" fill="#61DAFB">React</text>
                </g>
                
                <!-- Pills Row 2 -->
                <g transform="translate(0, 50)">
                    <rect x="0" y="0" width="50" height="24" fill="#00599C" fill-opacity="0.2" stroke="#00599C" rx="12" />
                    <text x="25" y="16" class="font-sans pill-text" text-anchor="middle" fill="#00599C">C++</text>
                    
                    <rect x="60" y="0" width="60" height="24" fill="#3776AB" fill-opacity="0.2" stroke="#3776AB" rx="12" />
                    <text x="90" y="16" class="font-sans pill-text" text-anchor="middle" fill="#3776AB">Python</text>
                    
                    <rect x="130" y="0" width="50" height="24" fill="#4479A1" fill-opacity="0.2" stroke="#4479A1" rx="12" />
                    <text x="155" y="16" class="font-sans pill-text" text-anchor="middle" fill="#4479A1">SQL</text>
                    
                    <rect x="190" y="0" width="80" height="24" fill="#339933" fill-opacity="0.2" stroke="#339933" rx="12" />
                    <text x="230" y="16" class="font-sans pill-text" text-anchor="middle" fill="#339933">Node.js</text>
                </g>
            </g>
            
            <g class="animate-slide" style="animation-delay: 0.7s;" transform="translate(0, 360)">
                <text x="0" y="0" class="font-sans section-title">💖 About Me</text>
                
                <text x="0" y="25" class="font-sans bullet">✓ A web developer, user-friendly and expertise with experiences.</text>
                <text x="0" y="45" class="font-sans bullet">✓ Always learning, always building.</text>
                <text x="0" y="65" class="font-sans bullet">✓ Turning ideas into real world solutions.</text>
            </g>
            
            <!-- Bottom stats -->
            <g class="animate-fade" style="animation-delay: 1.2s;" transform="translate(0, 470)">
                <rect x="0" y="0" width="450" height="60" fill="{PANEL_BG}" stroke="{BORDER}" rx="8" />
                <g transform="translate(30, 25)">
                    <text x="0" y="0" class="font-sans pill-text" fill="{TEXT_DIM}">★ Repos</text>
                    <text x="20" y="20" class="font-sans title-small" font-size="16">14</text>
                </g>
                <g transform="translate(140, 25)">
                    <text x="0" y="0" class="font-sans pill-text" fill="{TEXT_DIM}">★ Commits</text>
                    <text x="20" y="20" class="font-sans title-small" font-size="16">1K+</text>
                </g>
                <g transform="translate(260, 25)">
                    <text x="0" y="0" class="font-sans pill-text" fill="{TEXT_DIM}">★ Stars</text>
                    <text x="20" y="20" class="font-sans title-small" font-size="16">40+</text>
                </g>
                <g transform="translate(360, 25)">
                    <text x="0" y="0" class="font-sans pill-text" fill="{TEXT_DIM}">★ Followers</text>
                    <text x="20" y="20" class="font-sans title-small" font-size="16">20+</text>
                </g>
            </g>
        </g>
        
        <!-- Top Right Code Window -->
        <g transform="translate(550, 40)" class="animate-slide" style="animation-delay: 0.8s;">
            <rect x="0" y="0" width="380" height="150" fill="{PANEL_BG}" stroke="{BORDER}" rx="8" opacity="0.9" />
            <circle cx="15" cy="15" r="5" fill="#ff5f56" />
            <circle cx="30" cy="15" r="5" fill="#ffbd2e" />
            <circle cx="45" cy="15" r="5" fill="#27c93f" />
            
            <g transform="translate(15, 40)">
                <text x="0" y="0" class="font-mono code-text"><tspan class="code-kw">function</tspan> <tspan class="code-hi">buildDreams</tspan>() {{</text>
                <text x="15" y="20" class="font-mono code-text"><tspan class="code-kw">while</tspan> (alive) {{</text>
                <text x="30" y="40" class="font-mono code-text">eat();</text>
                <text x="30" y="60" class="font-mono code-text">sleep(404); <tspan fill="#6a9955">// Sleep Not Found</tspan></text>
                <text x="30" y="80" class="font-mono code-text">code();</text>
                <text x="15" y="100" class="font-mono code-text">}}</text>
                <text x="0" y="120" class="font-mono code-text">}}</text>
            </g>
            
            <!-- Floating Neon Sign next to it -->
            <g transform="translate(300, 30)" class="animate-neon">
                <rect x="-10" y="-20" width="130" height="40" fill="none" stroke="{ACCENT_PINK}" rx="4" />
                <text x="55" y="-5" class="font-sans" font-size="10" font-weight="bold" fill="#fff" text-anchor="middle">&lt; / &gt;</text>
                <text x="55" y="10" class="font-sans" font-size="10" font-weight="bold" fill="#fff" text-anchor="middle">KEEP CODING</text>
            </g>
        </g>

        <!-- Right User Image (Hologram) -->
        <g transform="translate(600, 100)" class="animate-fade animate-float" style="animation-delay: 1.0s;">
            <!-- Render the actual base64 image nicely -->
            <image href="data:image/png;base64,{nobg_b64}" x="0" y="0" width="400" height="500" preserveAspectRatio="xMidYMax meet" />
        </g>
        
    </g>
</svg>'''
    return svg

def generate_streak():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 200" width="100%" height="100%">
    <style>
        @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
        .bg {{ fill: {PANEL_BG}; stroke: {BORDER}; stroke-width: 1px; rx: 8px; }}
        .title {{ font-family: -apple-system, sans-serif; font-size: 24px; fill: {ACCENT_PINK}; font-weight: bold; }}
        .label {{ font-family: -apple-system, sans-serif; font-size: 14px; fill: {TEXT_DIM}; font-weight: bold; }}
        .date {{ font-family: -apple-system, sans-serif; font-size: 10px; fill: {TEXT_DIM}; }}
        .val {{ font-family: -apple-system, sans-serif; font-size: 24px; fill: #fff; font-weight: bold; }}
        .ring {{ fill: none; stroke: {ACCENT_PINK}; stroke-width: 4; stroke-linecap: round; }}
        .ring-bg {{ fill: none; stroke: #30363d; stroke-width: 4; }}
        .animate-fade {{ animation: fadeIn 1s ease forwards; opacity: 0; }}
    </style>
    
    <rect width="800" height="200" class="bg" />
    
    <g class="animate-fade" style="animation-delay: 0.2s;" transform="translate(150, 60)">
        <text x="0" y="0" class="val" text-anchor="middle">64</text>
        <text x="0" y="25" class="label" text-anchor="middle">Total Contributions</text>
        <text x="0" y="45" class="date" text-anchor="middle">Aug 20, 2022 - Present</text>
    </g>

    <g class="animate-fade" style="animation-delay: 0.4s;" transform="translate(400, 100)">
        <circle cx="0" cy="-20" r="40" class="ring-bg" />
        <!-- Partial ring to show current streak -->
        <path d="M 0 -60 A 40 40 0 0 1 40 -20" class="ring" />
        <text x="0" y="-12" class="val" text-anchor="middle" fill="#ffbd2e">4</text>
        <text x="0" y="35" class="label" text-anchor="middle">Current Streak</text>
        <text x="0" y="55" class="date" text-anchor="middle">Jul 19 - Jul 22</text>
    </g>

    <g class="animate-fade" style="animation-delay: 0.6s;" transform="translate(650, 60)">
        <text x="0" y="0" class="val" text-anchor="middle">4</text>
        <text x="0" y="25" class="label" text-anchor="middle">Longest Streak</text>
        <text x="0" y="45" class="date" text-anchor="middle">Jul 19 - Jul 22</text>
    </g>

    <!-- Divider Lines -->
    <line x1="280" y1="50" x2="280" y2="150" stroke="{BORDER}" stroke-width="2" />
    <line x1="520" y1="50" x2="520" y2="150" stroke="{BORDER}" stroke-width="2" />
</svg>'''
    return svg

def generate_activity():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 250" width="100%" height="100%">
    <style>
        .bg {{ fill: {PANEL_BG}; stroke: {BORDER}; stroke-width: 1px; rx: 8px; }}
        .title {{ font-family: -apple-system, sans-serif; font-size: 14px; fill: {ACCENT_PINK}; font-weight: bold; text-anchor: middle; }}
        .grid {{ stroke: #30363d; stroke-width: 1; }}
        .axis {{ font-family: -apple-system, sans-serif; font-size: 10px; fill: {TEXT_DIM}; }}
        .line {{ fill: none; stroke: {ACCENT_PURPLE}; stroke-width: 2; }}
        .dot {{ fill: {ACCENT_PINK}; }}
        @keyframes draw {{ from {{ stroke-dasharray: 0 2000; }} to {{ stroke-dasharray: 2000 2000; }} }}
        .animate-draw {{ animation: draw 2s ease-out forwards; }}
    </style>
    
    <rect width="800" height="250" class="bg" />
    <text x="400" y="30" class="title">Contribution Graph 💖</text>
    
    <!-- Grid -->
    <g transform="translate(50, 50)">
        <!-- Horizontal lines -->
        <line x1="0" y1="0" x2="700" y2="0" class="grid" />
        <line x1="0" y1="30" x2="700" y2="30" class="grid" />
        <line x1="0" y1="60" x2="700" y2="60" class="grid" />
        <line x1="0" y1="90" x2="700" y2="90" class="grid" />
        <line x1="0" y1="120" x2="700" y2="120" class="grid" />
        <line x1="0" y1="150" x2="700" y2="150" class="grid" />
        
        <!-- Y-Axis labels -->
        <text x="-10" y="5" class="axis" text-anchor="end">20</text>
        <text x="-10" y="35" class="axis" text-anchor="end">16</text>
        <text x="-10" y="65" class="axis" text-anchor="end">12</text>
        <text x="-10" y="95" class="axis" text-anchor="end">8</text>
        <text x="-10" y="125" class="axis" text-anchor="end">4</text>
        <text x="-10" y="155" class="axis" text-anchor="end">0</text>
        
        <text x="-35" y="75" class="axis" font-weight="bold" transform="rotate(-90 -35 75)" fill="{ACCENT_PINK}">Contributions</text>

        <!-- X-Axis Labels (Days) -->
        <g class="axis" text-anchor="middle" transform="translate(0, 165)">
            <text x="0">24</text>
            <text x="50">26</text>
            <text x="100">28</text>
            <text x="150">30</text>
            <text x="200">1</text>
            <text x="250">3</text>
            <text x="300">5</text>
            <text x="350">7</text>
            <text x="400">9</text>
            <text x="450">11</text>
            <text x="500">13</text>
            <text x="550">15</text>
            <text x="600">17</text>
            <text x="650">19</text>
            <text x="700">21</text>
        </g>
        <text x="350" y="185" class="axis" font-weight="bold">Days</text>

        <!-- Graph Line -->
        <path d="M 0 150 L 50 150 L 100 150 L 150 40 L 200 130 L 250 150 L 300 110 L 350 150 L 400 150 L 450 150 L 500 120 L 550 40 L 600 150 L 650 30 L 700 150" class="line animate-draw" />
        
        <!-- Dots -->
        <circle cx="150" cy="40" r="4" class="dot" />
        <circle cx="200" cy="130" r="4" class="dot" />
        <circle cx="300" cy="110" r="4" class="dot" />
        <circle cx="500" cy="120" r="4" class="dot" />
        <circle cx="550" cy="40" r="4" class="dot" />
        <circle cx="650" cy="30" r="4" class="dot" />
    </g>
</svg>'''
    return svg

def generate_lanyard():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 600" width="100%" height="100%">
    <defs>
        <linearGradient id="strapGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="{ACCENT_PINK}" />
            <stop offset="100%" stop-color="{ACCENT_PURPLE}" />
        </linearGradient>
        <clipPath id="avatarClip">
            <circle cx="150" cy="350" r="50" />
        </clipPath>
        <style>
            @keyframes swing {{ 0% {{ transform: rotate(5deg); }} 50% {{ transform: rotate(-5deg); }} 100% {{ transform: rotate(5deg); }} }}
            .lanyard-group {{ transform-origin: 150px 0px; animation: swing 6s ease-in-out infinite; }}
        </style>
    </defs>

    <rect width="300" height="600" fill="none" />
    <g class="lanyard-group">
        <!-- Strap -->
        <path d="M 130,0 L 140,200 L 160,200 L 170,0" fill="none" stroke="url(#strapGrad)" stroke-width="12" />
        
        <!-- Clasp -->
        <rect x="140" y="200" width="20" height="25" fill="silver" rx="3" />
        <circle cx="150" cy="230" r="10" fill="none" stroke="silver" stroke-width="4" />

        <!-- Card -->
        <rect x="60" y="240" width="180" height="280" fill="{PANEL_BG}" stroke="{BORDER}" stroke-width="2" rx="15" />
        
        <circle cx="150" cy="350" r="53" fill="none" stroke="{ACCENT_PINK}" stroke-width="3" />
        <image href="data:image/png;base64,{face_b64}" x="80" y="280" width="140" height="140" clip-path="url(#avatarClip)" preserveAspectRatio="xMidYMid slice" />
        
        <text x="150" y="440" font-family="sans-serif" font-size="16" font-weight="bold" fill="{ACCENT_PINK}" text-anchor="middle">Shiza Ahsan</text>
        <text x="150" y="460" font-family="sans-serif" font-size="10" fill="{TEXT_DIM}" text-anchor="middle">Software Engineer</text>
        
        <text x="150" y="480" font-family="monospace" font-size="12" fill="#fff" text-anchor="middle">404 SLEEP</text>
        
        <!-- Barcode -->
        <g transform="translate(90, 495)">
            <rect x="0" y="0" width="5" height="15" fill="#fff" />
            <rect x="8" y="0" width="3" height="15" fill="#fff" />
            <rect x="15" y="0" width="8" height="15" fill="#fff" />
            <rect x="26" y="0" width="5" height="15" fill="#fff" />
            <rect x="35" y="0" width="10" height="15" fill="#fff" />
            <rect x="50" y="0" width="4" height="15" fill="#fff" />
            <rect x="58" y="0" width="12" height="15" fill="#fff" />
            <rect x="75" y="0" width="6" height="15" fill="#fff" />
            <rect x="85" y="0" width="10" height="15" fill="#fff" />
            <rect x="100" y="0" width="5" height="15" fill="#fff" />
            <rect x="110" y="0" width="10" height="15" fill="#fff" />
        </g>
    </g>
</svg>'''
    return svg

def generate_stats():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 220" width="100%" height="100%">
    <style>
        .bg {{ fill: {PANEL_BG}; stroke: {BORDER}; stroke-width: 1px; rx: 8px; }}
        .title {{ fill: {ACCENT_PINK}; font-family: -apple-system, sans-serif; font-size: 14px; font-weight: bold; }}
        .text {{ fill: #fff; font-family: -apple-system, sans-serif; font-size: 12px; font-weight: 500; }}
        .val {{ fill: #fff; font-family: -apple-system, sans-serif; font-size: 12px; font-weight: bold; }}
        .ring {{ fill: none; stroke: {ACCENT_PURPLE}; stroke-width: 8; stroke-linecap: round; stroke-dasharray: 200 1000; }}
        .ring-bg {{ fill: none; stroke: #30363d; stroke-width: 8; }}
        .rank {{ fill: {ACCENT_PINK}; font-family: -apple-system, sans-serif; font-size: 28px; font-weight: bold; text-anchor: middle; }}
        @keyframes fillRing {{ from {{ stroke-dasharray: 0 1000; }} to {{ stroke-dasharray: 200 1000; }} }}
        .animate-ring {{ animation: fillRing 1.5s ease forwards; transform: rotate(-90deg); transform-origin: center; }}
    </style>
    <rect width="450" height="220" class="bg" />
    <text x="20" y="30" class="title">🌸 Shiza Ahsan's GitHub Stats</text>
    
    <g transform="translate(30, 70)">
        <text x="0" y="0" class="text">⭐ Total Stars Earned:</text>
        <text x="200" y="0" class="val">50+</text>
        
        <text x="0" y="30" class="text">✅ Total Commits:</text>
        <text x="200" y="30" class="val">1000+</text>
        
        <text x="0" y="60" class="text">🚀 Public Repos:</text>
        <text x="200" y="60" class="val">14+</text>
        
        <text x="0" y="90" class="text">👥 Followers:</text>
        <text x="200" y="90" class="val">25+</text>
        
        <text x="0" y="120" class="text">🔥 Action Gits Rolls:</text>
        <text x="200" y="120" class="val">4</text>
    </g>
    
    <g transform="translate(350, 120)">
        <circle cx="0" cy="0" r="45" class="ring-bg" />
        <circle cx="0" cy="0" r="45" class="ring animate-ring" />
        <text x="0" y="10" class="rank">A</text>
    </g>
</svg>'''
    return svg

def generate_langs():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 220" width="100%" height="100%">
    <style>
        .bg {{ fill: {PANEL_BG}; stroke: {BORDER}; stroke-width: 1px; rx: 8px; }}
        .title {{ fill: {ACCENT_PINK}; font-family: -apple-system, sans-serif; font-size: 14px; font-weight: bold; }}
        .text {{ fill: #fff; font-family: -apple-system, sans-serif; font-size: 11px; font-weight: bold; }}
        .pct {{ fill: {TEXT_DIM}; font-family: -apple-system, sans-serif; font-size: 10px; }}
        .bar-bg {{ fill: #30363d; rx: 4px; }}
        @keyframes grow {{ from {{ width: 0; }} }}
        .animate-grow {{ animation: grow 1s ease-out forwards; }}
    </style>
    <rect width="450" height="220" class="bg" />
    <text x="20" y="30" class="title">💡 Top Languages</text>
    
    <g transform="translate(30, 60)">
        <!-- HTML -->
        <text x="0" y="0" class="text">HTML</text>
        <rect x="0" y="10" width="350" height="8" class="bar-bg" />
        <rect x="0" y="10" width="150" height="8" fill="#e34c26" rx="4" class="animate-grow" />
        <text x="360" y="18" class="pct">42.8%</text>
        
        <!-- CSS -->
        <g transform="translate(0, 35)">
            <text x="0" y="0" class="text">CSS</text>
            <rect x="0" y="10" width="350" height="8" class="bar-bg" />
            <rect x="0" y="10" width="120" height="8" fill="#563d7c" rx="4" class="animate-grow" style="animation-delay: 0.1s;" />
            <text x="360" y="18" class="pct">34.3%</text>
        </g>
        
        <!-- JavaScript -->
        <g transform="translate(0, 70)">
            <text x="0" y="0" class="text">JavaScript</text>
            <rect x="0" y="10" width="350" height="8" class="bar-bg" />
            <rect x="0" y="10" width="80" height="8" fill="#f1e05a" rx="4" class="animate-grow" style="animation-delay: 0.2s;" />
            <text x="360" y="18" class="pct">22.9%</text>
        </g>

        <!-- TypeScript -->
        <g transform="translate(0, 105)">
            <text x="0" y="0" class="text">TypeScript</text>
            <rect x="0" y="10" width="350" height="8" class="bar-bg" />
            <rect x="0" y="10" width="40" height="8" fill="#3178c6" rx="4" class="animate-grow" style="animation-delay: 0.3s;" />
            <text x="360" y="18" class="pct">12.0%</text>
        </g>
    </g>
</svg>'''
    return svg

def generate_trophies():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 120" width="100%" height="100%">
    <style>
        .box {{ fill: {PANEL_BG}; stroke: {BORDER}; stroke-width: 1px; rx: 8px; }}
        .title {{ font-family: -apple-system, sans-serif; font-size: 10px; font-weight: bold; fill: #fff; text-anchor: middle; }}
        .subtitle {{ font-family: -apple-system, sans-serif; font-size: 8px; fill: {TEXT_DIM}; text-anchor: middle; }}
        .rank-s {{ fill: #ffbd2e; font-family: -apple-system, sans-serif; font-size: 12px; font-weight: bold; }}
        .rank-a {{ fill: {ACCENT_PINK}; font-family: -apple-system, sans-serif; font-size: 12px; font-weight: bold; }}
        .rank-b {{ fill: #3776AB; font-family: -apple-system, sans-serif; font-size: 12px; font-weight: bold; }}
        @keyframes pop {{ 0% {{ transform: scale(0); opacity: 0; }} 100% {{ transform: scale(1); opacity: 1; }} }}
        .animate-pop {{ animation: pop 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards; opacity: 0; transform-origin: 50% 50%; }}
    </style>
    
    <!-- 6 Trophies Layout -->
    <g transform="translate(20, 20)">
        
        <!-- Trophy 1 -->
        <g transform="translate(0, 0)">
            <g class="animate-pop" style="transform-origin: 55px 40px;">
                <rect x="0" y="0" width="110" height="80" class="box" stroke="{ACCENT_PINK}" />
                <text x="95" y="15" class="rank-a">SSS</text>
                <text x="55" y="45" font-size="24" text-anchor="middle">🔮</text>
                <text x="55" y="60" class="title">Shiza Dev</text>
                <text x="55" y="72" class="subtitle">Always codes late</text>
            </g>
        </g>

        <!-- Trophy 2 -->
        <g transform="translate(130, 0)">
            <g class="animate-pop" style="animation-delay: 0.1s; transform-origin: 55px 40px;">
                <rect x="0" y="0" width="110" height="80" class="box" stroke="#ffbd2e" />
                <text x="95" y="15" class="rank-s">S</text>
                <text x="55" y="45" font-size="24" text-anchor="middle">🌟</text>
                <text x="55" y="60" class="title">Starstruck</text>
                <text x="55" y="72" class="subtitle">50+ Stars</text>
            </g>
        </g>
        
        <!-- Trophy 3 -->
        <g transform="translate(260, 0)">
            <g class="animate-pop" style="animation-delay: 0.2s; transform-origin: 55px 40px;">
                <rect x="0" y="0" width="110" height="80" class="box" stroke="{ACCENT_PINK}" />
                <text x="95" y="15" class="rank-a">A</text>
                <text x="55" y="45" font-size="24" text-anchor="middle">⭐</text>
                <text x="55" y="60" class="title">Stargazer</text>
                <text x="55" y="72" class="subtitle">User's repo</text>
            </g>
        </g>
        
        <!-- Trophy 4 -->
        <g transform="translate(390, 0)">
            <g class="animate-pop" style="animation-delay: 0.3s; transform-origin: 55px 40px;">
                <rect x="0" y="0" width="110" height="80" class="box" stroke="{ACCENT_PINK}" />
                <text x="95" y="15" class="rank-a">A</text>
                <text x="55" y="45" font-size="24" text-anchor="middle">💖</text>
                <text x="55" y="60" class="title">Rising Star</text>
                <text x="55" y="72" class="subtitle">Gained 10+ PRs</text>
            </g>
        </g>
        
        <!-- Trophy 5 -->
        <g transform="translate(520, 0)">
            <g class="animate-pop" style="animation-delay: 0.4s; transform-origin: 55px 40px;">
                <rect x="0" y="0" width="110" height="80" class="box" stroke="#3776AB" />
                <text x="95" y="15" class="rank-b">B</text>
                <text x="55" y="45" font-size="24" text-anchor="middle">💻</text>
                <text x="55" y="60" class="title">CodeMaster</text>
                <text x="55" y="72" class="subtitle">Commits: 1000+</text>
            </g>
        </g>
        
        <!-- Trophy 6 -->
        <g transform="translate(650, 0)">
            <g class="animate-pop" style="animation-delay: 0.5s; transform-origin: 55px 40px;">
                <rect x="0" y="0" width="110" height="80" class="box" stroke="#4ec9b0" />
                <text x="95" y="15" class="rank-b" fill="#4ec9b0">B</text>
                <text x="55" y="45" font-size="24" text-anchor="middle">📦</text>
                <text x="55" y="60" class="title">Creator</text>
                <text x="55" y="72" class="subtitle">Repos: 14+</text>
            </g>
        </g>
        
    </g>
</svg>'''
    return svg


def generate_readme():
    return """<div align="center">
  <picture>
    <img alt="Animated GitHub Banner" src="./banner.svg?v=3" width="100%">
  </picture>
</div>

<br>

<table align="center" border="1" bordercolor="#4d3472" cellpadding="20" cellspacing="0" width="100%" style="background-color: #0d1117; border-collapse: collapse; border-radius: 10px;">
  <tr>
    <td align="center" valign="top" width="30%" style="border-right: none;">
      <img src="./lanyard.svg?v=3" alt="Lanyard" width="200">
    </td>
    <td align="left" valign="top" width="70%" style="border-left: none;">
      <h3 style="color: white; font-weight: bold;">🌸 My Code Creations</h3>
      <table border="1" bordercolor="#30363d" cellpadding="10" cellspacing="0" width="100%" style="border-collapse: collapse; background-color: #161b22; color: #c9d1d9;">
        <tr style="background-color: #0d1117;">
          <th>🚀 Project</th>
          <th>💻 Tech</th>
          <th>⭐</th>
        </tr>
        <tr>
          <td><a href="#" style="color: #ff7eb3; text-decoration: none;">🔮 Image Rotator App</a></td>
          <td><img src="https://img.shields.io/badge/C++-00599C?style=flat-square&logo=c%2B%2B&logoColor=white"></td>
          <td>25</td>
        </tr>
        <tr>
          <td><a href="#" style="color: #ff7eb3; text-decoration: none;">🎮 Quiz App CLI</a></td>
          <td><img src="https://img.shields.io/badge/C++-00599C?style=flat-square&logo=c%2B%2B&logoColor=white"></td>
          <td>9</td>
        </tr>
        <tr>
          <td><a href="#" style="color: #ff7eb3; text-decoration: none;">📅 Smart Scheduler</a></td>
          <td><img src="https://img.shields.io/badge/JS-F7DF1E?style=flat-square&logo=javascript&logoColor=black"></td>
          <td>8</td>
        </tr>
        <tr>
          <td><a href="#" style="color: #ff7eb3; text-decoration: none;">🏥 Clinic Management</a></td>
          <td><img src="https://img.shields.io/badge/TS-3178C6?style=flat-square&logo=typescript&logoColor=white"></td>
          <td>8</td>
        </tr>
        <tr>
          <td><a href="#" style="color: #ff7eb3; text-decoration: none;">📱 QR Code Generator</a></td>
          <td><img src="https://img.shields.io/badge/CSS-1572B6?style=flat-square&logo=css3&logoColor=white"></td>
          <td>2</td>
        </tr>
      </table>
      <br>
      <div align="center">
        <p style="color: #ff7eb3; font-style: italic;">"404 Sleep Not Found."</p>
      </div>
    </td>
  </tr>
</table>

<br>

<h3 align="center">📊 GitHub Stats & Graphs</h3>

<table align="center" border="0" cellpadding="10" cellspacing="0" width="100%">
  <tr>
    <td align="center" width="50%">
      <img src="./stats.svg?v=3" alt="Stats Card" width="100%" />
    </td>
    <td align="center" width="50%">
      <img src="./langs.svg?v=3" alt="Languages Card" width="100%" />
    </td>
  </tr>
</table>

<div align="center">
  <img src="./streak.svg?v=3" alt="Streak Card" width="100%" style="max-width: 800px;" />
</div>

<br>

<div align="center">
  <img src="./activity.svg?v=3" alt="Activity Graph" width="100%" style="max-width: 800px;" />
</div>

<br>

<div align="center">
  <img src="./trophies.svg?v=3" alt="Trophies Card" width="100%" style="max-width: 800px;" />
</div>

<br>

<h3 align="center">🐍 Watch the snake eat my contributions</h3>
<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ShizaAhsan/ShizaAhsan/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/ShizaAhsan/ShizaAhsan/output/github-contribution-grid-snake.svg">
    <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/ShizaAhsan/ShizaAhsan/output/github-contribution-grid-snake.svg">
  </picture>
</div>

<br><br>

<h3 align="center">📫 Let's Connect</h3>
<div align="center">
  <a href="mailto:shizaahsan2006@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email">
  </a>
  <a href="https://github.com/ShizaAhsan">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
</div>

<br>

<div align="center">
  <img src="https://komarev.com/ghpvc/?username=ShizaAhsan&label=Profile%20views&color=ff7eb3&style=flat" alt="Profile views" />
</div>
"""

with open("banner.svg", "w", encoding="utf-8") as f: f.write(generate_banner(is_light=False))
with open("lanyard.svg", "w", encoding="utf-8") as f: f.write(generate_lanyard())
with open("stats.svg", "w", encoding="utf-8") as f: f.write(generate_stats())
with open("langs.svg", "w", encoding="utf-8") as f: f.write(generate_langs())
with open("trophies.svg", "w", encoding="utf-8") as f: f.write(generate_trophies())
with open("streak.svg", "w", encoding="utf-8") as f: f.write(generate_streak())
with open("activity.svg", "w", encoding="utf-8") as f: f.write(generate_activity())
with open("README.md", "w", encoding="utf-8") as f: f.write(generate_readme())

print("Massive redesign executed successfully.")
