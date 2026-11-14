"""DANAG STUDIO dark portfolio (all navy), guide: Danag's 'Oluchi Vanessa' reference, 2026-11-12.
Usage: python3 promo/render_folio_dark.py OUTDIR -> NN.jpg (2160x2700) + NN-1080.jpg
Navy gradient only (no glow), light grain, faint logo mark, Gobold two-tone headlines (white + gold),
gold dot grids, rounded image tiles. TikTok-safe picks only (no SEX label, no intimate shots).
"""
import sys, os, re, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image
P = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(P); B = f'{R}/book-flyer'; A = f'{R}/portfolio/src/assets'
sys.path.insert(0, B)
import render_book as rb
from contacts import IC
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
CUT = pathlib.Path('/home/claude/assets/danag-portrait-cut.png').as_uri()
RV = '/home/claude/assets/reviews'
GOLD = '#FFC107'; F = f'{R}/fonts/'
NAVYG = 'linear-gradient(160deg,#032F65 0%,#022452 40%,#011631 78%,#010F21 100%)'
u = lambda n: pathlib.Path(f'{A}/{n}.jpg').as_uri()
ic = lambda k, c=GOLD, s=30: f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" style="color:{c};flex:none">{IC[k]}</svg>'
LOGO = re.sub(r'<\?xml[^>]*>', '', open(f'{B}/logo-on-navy.svg').read()).replace('<svg', '<svg style="height:44px;width:auto;display:block"', 1)


def hl(a, b, cap, dot=True, gap=18, maxw=900):
    """Two-tone Gobold line: a white, b gold, side by side."""
    while cap > 30 and rb.width(a, cap) + rb.width(b, cap, dot) + gap > maxw: cap -= 2
    p = rb.line(a, cap, '#fff') if a else ''
    q = rb.line(b, cap, GOLD, dot, dot_color='#fff') if b else ''
    return f'<div style="display:flex;align-items:flex-end;gap:{gap}px">{p}{q}</div>'


def stack(a, b, cap, dot=True, maxw=900):
    cap = min(cap, rb.fit(a, maxw, cap), rb.fit(b, maxw, cap, dot))
    return (f'<div style="display:flex;flex-direction:column;gap:{int(cap*.14)}px">{rb.line(a, cap, "#fff")}'
            f'{rb.line(b, cap, GOLD, dot, dot_color="#fff")}</div>')


def dots(w=6, h=6):
    return (f'<svg width="{w*16}" height="{h*16}">' + ''.join(f'<circle cx="{8+16*i}" cy="{8+16*j}" r="2.2" fill="{GOLD}" opacity=".75"/>'
            for i in range(w) for j in range(h)) + '</svg>')


def tile(n, w, h, pos='center', fit='cover', bg='#0b1424'):
    return (f'<div style="width:{w}px;height:{h}px;border-radius:20px;overflow:hidden;flex:none;background:{bg};'
            f'box-shadow:0 18px 40px rgba(0,0,0,.35)"><div style="width:100%;height:100%;background:url({u(n)}) {pos}/{fit} no-repeat"></div></div>')


def page(body, head=True, foot=True):
    return f"""<html><head><style>
@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}
@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}
@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
@font-face{{font-family:SC;src:url({F}sacramento-latin-400-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;color:#fff;background:{NAVYG}}}
.a{{position:absolute}} p{{font-weight:500;font-size:25px;line-height:1.55;color:rgba(255,255,255,.86)}}
.k{{font-weight:900;font-size:20px;letter-spacing:7px;color:{GOLD}}}
</style></head><body>
<svg class="a" viewBox="252 255 749 664" style="right:-240px;top:420px;width:760px;opacity:.045"><path fill="#fff" fill-rule="evenodd" d="{rb.MK['nodot']}"/><path fill="#fff" d="{rb.MK['dot']}"/></svg>
{f'<div class="a" style="left:90px;top:70px">{LOGO}</div>' if head else ''}
{body}
{'' if not foot else ''}<div class="a" style="display:{'block' if foot else 'none'};left:90px;bottom:56px;font-weight:700;font-size:18px;letter-spacing:2px;color:rgba(255,255,255,.55)">@thedanagstudio</div>
<div class="a" style="inset:0;z-index:50;pointer-events:none;opacity:.16;mix-blend-mode:overlay;background-size:256px;background-image:url({R}/grain.png)"></div>
</body></html>"""


def project(kick, a, b, text, grid):
    return page(f"""<div class="a" style="left:90px;right:90px;top:150px;bottom:110px;display:flex;flex-direction:column;justify-content:space-evenly">
{grid}<div><div class="k" style="margin-bottom:22px">{kick}</div>{stack(a, b, 92)}<p style="margin-top:26px;max-width:860px">{text}</p></div></div>""")


def mosaic(big, s1, s2, s3, s4, pos=None):
    pos = pos or {}
    t = lambda n, w, h: tile(n, w, h, pos.get(n, 'center'))
    return (f'<div style="display:flex;gap:18px">{t(big, 430, 600)}<div style="display:flex;flex-direction:column;gap:18px">'
            f'<div style="display:flex;gap:18px">{t(s1, 215, 291)}{t(s2, 215, 291)}</div>'
            f'<div style="display:flex;gap:18px">{t(s3, 215, 291)}{t(s4, 215, 291)}</div></div></div>')


def grid(names, cols, w, h, fit='cover'):
    return (f'<div style="display:grid;grid-template-columns:repeat({cols},{w}px);gap:20px">'
            + ''.join(tile(n, w, h, fit=fit) for n in names) + '</div>')


SL = []
# 1 cover
SL.append(page(f"""<div class="a" style="left:90px;top:150px">{hl('PORT', 'FOLIO', 54, dot=False, gap=4)}
<div style="margin-top:34px">{stack('DANAG', 'STUDIO', 190, maxw=640)}</div>
<div style="margin-top:40px;font-weight:700;font-size:27px;line-height:1.5">Graphic Designer &#8226; Product Visuals<br>Social Media Design &#8226; Website Design</div>
<p style="margin-top:22px;font-size:22px;max-width:470px">Crafting premium visuals that make brands look good, get noticed and get booked.</p></div>
<div class="a" style="right:90px;top:150px">{dots()}</div><div class="a" style="left:90px;bottom:120px">{dots()}</div>
<div class="a" style="right:-120px;bottom:-60px;width:600px;height:720px;border-radius:300px 300px 0 0;background:linear-gradient(180deg,#FFD54F,#FFC107 50%,#E3A600)"></div>
<img class="a" src="{CUT}" style="right:-110px;bottom:0;height:690px">""", head=False))
# 2 about
SL.append(page(f"""<div class="a" style="left:90px;top:160px;width:640px">{hl('ABOUT', 'ME', 84)}
<p style="margin-top:34px">I'm Danag, the designer behind DANAG STUDIO, a graphic design studio crowned in craft.</p>
<p style="margin-top:22px">I design flyers and posters, product visuals, social media content, brochures, business cards and websites, working closely with brand founders, especially in luxury fragrance and fashion.</p>
<p style="margin-top:22px">My approach is simple: design that looks premium, says one clear thing, and gets people to act.</p>
<div style="font-family:SC;font-size:96px;color:{GOLD};margin-top:18px;line-height:1">Danag</div>
<div style="font-weight:700;font-size:26px;margin-top:6px">Based in Accra, Ghana.</div></div>
<div class="a" style="left:90px;bottom:130px">{dots(5, 5)}</div>
<img class="a" src="{CUT}" style="right:-170px;bottom:0;height:700px">""", head=False))
# 3 bring
items = [('CREATIVE & STRATEGIC', 'Every design starts with what you want people to do, then I make it look premium.'),
         ('DETAIL ORIENTED', 'Spacing, type and colour are handled with care so every piece feels polished.'),
         ('RELIABLE & PROFESSIONAL', 'Clear communication, patience with feedback and delivery on time.'),
         ('RESULT DRIVEN', 'Visuals built to get attention, build trust and get your phone ringing.')]
SL.append(page(f"""<div class="a" style="left:90px;right:90px;top:170px">{stack('WHAT I BRING', 'TO THE TABLE', 92)}
<div style="margin-top:60px;display:flex;flex-direction:column;gap:44px">""" + ''.join(
    f'<div style="display:flex;gap:26px"><div style="width:6px;background:{GOLD};border-radius:3px;flex:none"></div><div><div style="font-weight:900;font-size:28px;letter-spacing:1px">{t}</div><p style="margin-top:8px;max-width:760px">{d}</p></div></div>'
    for t, d in items) + f"""</div></div><div class="a" style="right:90px;bottom:110px">{dots()}</div>"""))
# 4 logos (DANAG logo shown as work, so no header logo)
logos = ['lg-bea', 'lg-gc', 'lg-marmar', 'lg-ayara1', 'lg-autoperf', 'lg-danag']
SL.append(page(f"""<div class="a" style="left:90px;top:120px">{hl('LOGO', 'DESIGN', 84)}</div>
<div class="a" style="right:90px;top:120px">{dots(5, 4)}</div>
<div class="a" style="left:90px;right:90px;top:300px;display:grid;grid-template-columns:repeat(2,440px);gap:24px">"""
    + ''.join(tile(n, 440, 260, fit='cover') for n in logos) + '</div>', head=False))
# 5-6 Maison Yusif
SL.append(project('PRODUCT VISUALS', 'CAMPAIGN VISUALS FOR', 'MAISON YUSIF FRAGRANCE',
                  'Luxury perfume visuals that turn every bottle into a story, from studio still life to editorial portraits.',
                  mosaic('my-066', 'my-apex', 'my-wood', 'my-vatican', 'my-sand', {'my-066': 'center top'})))
SL.append(project('SOCIAL MEDIA CAMPAIGNS', 'LAUNCHES & EVENTS FOR', 'MAISON YUSIF',
                  'A New Jersey launch, a Dallas exhibition, store openings and seasonal sales that got people talking.',
                  grid(['my-beast-nj', 'my-dallas', 'my-xmas', 'my-exclyusif', 'my-100k', 'my-tamale'], 3, 287, 290)))
# 7-8 Scents & Spice
SL.append(project('PRODUCT VISUALS', 'EDITORIAL VISUALS FOR', 'SCENTS & SPICE BY GB',
                  'Warm, editorial imagery for a growing perfume house, with every scent given its own mood.',
                  mosaic('ss-084', 'ss-076', 'ss-086', 'ss-080', 'ss-178', {'ss-084': 'center top'})))
SL.append(project('SOCIAL MEDIA CAMPAIGNS', 'PROMOS FOR', 'SCENTS & SPICE BY GB',
                  'Store opening, restock, back-to-school and deal-of-the-week flyers built to move stock.',
                  grid(['fl-ss-open', 'ss-restock', 'ss-student', 'fl-persian'], 2, 440, 330)))
# 9 Treadfix
SL.append(project('FASHION CAMPAIGN', 'LOOKBOOK FOR', 'TREADFIX',
                  'Campaign visuals on location at Ghanaian landmarks, from Black Star Gate to the castle coast.',
                  mosaic('tf-gmg-red', 'tf-barrel-front', 'tf-arch', 'tf-castle', 'tf-wig-navy', {'tf-gmg-red': 'center top'})))
# 10 watches
SL.append(project('CONCEPT WORK', 'PREMIUM', 'WATCH VISUALS',
                  'Personal projects exploring premium watch photography and storytelling.',
                  f'<div style="display:flex;gap:20px">{tile("wk-011", 430, 600)}<div style="display:flex;flex-direction:column;gap:20px">{tile("wk-015", 450, 290)}{tile("cmw-13", 450, 290)}</div></div>'))
# 11 marketing visuals
SL.append(page(f"""<div class="a" style="left:90px;top:150px">{hl('MARKETING', 'VISUALS', 84)}</div>
<div class="a" style="left:90px;top:300px">{grid(['fl-wss', 'fl-priscilla', 'fl-wealth', 'fl-signature1'], 2, 440, 440)}</div>"""))
# 12 packaging
SL.append(page(f"""<div class="a" style="left:90px;top:150px">{hl('PACKAGING', '& LABELS', 84)}</div>
<div class="a" style="left:90px;right:90px;top:300px;display:flex;gap:20px">{tile('pk-jeksal', 440, 550)}
<div style="display:flex;flex-direction:column;gap:20px">{tile('pk-marmar-shampoo', 440, 265)}{tile('pk-mamti', 440, 265)}</div></div>
<div class="a" style="left:90px;right:90px;top:870px">{tile('pk-tombrown', 900, 300, fit='contain', bg='#f3e7c9')}</div>"""))
# 13 websites
web = ''.join(f"""<div style="position:relative;width:900px;height:330px">{tile(d, 760, 330, 'top')}
<div style="position:absolute;right:0;bottom:-18px">{tile(m, 150, 310, 'top')}</div>
<div style="position:absolute;left:22px;bottom:20px;background:{GOLD};color:#022452;font-weight:900;font-size:19px;padding:9px 18px;border-radius:20px">{t}</div></div>"""
              for d, m, t in [('web-ss-desktop', 'web-ss-mobile', 'scentxspice.com'), ('web-cc-desktop', 'web-cc-mobile', 'careercaptains.org')])
SL.append(page(f"""<div class="a" style="left:90px;top:150px">{stack('WEBSITES THAT', 'WORK FOR YOU', 84)}</div>
<div class="a" style="left:90px;top:400px;display:flex;flex-direction:column;gap:46px">{web}</div>"""))
# 14 reviews quotes
card = lambda t, n, big=False: (f'<div style="border:2px solid rgba(255,193,7,.6);border-radius:24px;padding:{36 if big else 28}px;background:rgba(1,15,33,.45)">'
                                f'<div style="display:flex;justify-content:space-between;align-items:center"><span style="font-family:Georgia,serif;font-size:80px;line-height:.5;color:{GOLD}">&ldquo;</span>'
                                f'<span style="color:{GOLD};font-size:26px;letter-spacing:3px">&#9733;&#9733;&#9733;&#9733;&#9733;</span></div>'
                                f'<p style="margin-top:18px;font-size:{27 if big else 23}px;color:#fff">{t}</p>'
                                f'<div style="margin-top:18px;font-weight:900;font-size:19px;letter-spacing:3px;color:{GOLD}">{n}</div></div>')
SL.append(page(f"""<div class="a" style="left:90px;right:90px;top:150px;text-align:center;display:flex;flex-direction:column;align-items:center">
{hl('CLIENT', 'REVIEWS', 60, dot=False)}<div style="font-weight:900;font-size:56px;letter-spacing:1px;margin-top:20px">KIND WORDS. REAL IMPACT<span style="color:{GOLD}">.</span></div>
<div style="font-weight:500;font-size:22px;letter-spacing:4px;margin-top:12px;color:rgba(255,255,255,.75)">TRUSTED BY BRANDS. APPRECIATED FOR RESULTS.</div></div>
<div class="a" style="left:150px;right:150px;top:470px;display:flex;flex-direction:column;gap:22px">
{card('The work is really beautiful and I love the way you were very patient even with all my stubbornness.', 'MS. ADELINE', True)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:22px">{card('The logo is beautiful and I love the flyer design that came with it.', 'MS. GLORIA')}{card('I love it, thank you very much.', 'MAMLE')}</div></div>"""))
# 15 reviews screenshots
rv = lambda n, w: f'<img src="{pathlib.Path(f"{RV}/{n}.jpg").as_uri()}" style="width:{w}px;display:block;border-radius:18px;border:3px solid {GOLD}">'
SL.append(page(f"""<div class="a" style="left:90px;top:150px">{stack('STRAIGHT FROM', 'THE CHATS', 84)}</div>
<div class="a" style="left:90px;right:90px;top:400px;display:flex;gap:24px;justify-content:center;align-items:flex-start">
<div style="display:flex;flex-direction:column;gap:22px">{rv('r1', 430)}{rv('r2', 430)}</div>
<div style="display:flex;flex-direction:column;gap:22px">{rv('r4', 430)}</div></div>"""))
# 16 contact
con = [('PH', '+233 (0)50 332 0548'), ('IG', '@thedanagstudio'), ('TT', '@thedanagstudio'), ('X', '@thedanagstudio'), ('SC', '@realdanag')]
SL.append(page(f"""<div class="a" style="left:90px;right:90px;top:200px;font-weight:700;font-size:74px;line-height:1.2">
<span style="color:{GOLD}">Design</span> is more than visuals. It's how brands <span style="color:{GOLD}">communicate</span>, <span style="color:{GOLD}">connect</span> and stay memorable<span style="color:{GOLD}">.</span></div>
<div class="a" style="left:0;bottom:0;width:560px;height:700px;overflow:hidden"><div style="position:absolute;left:-60px;bottom:-120px;width:620px;height:620px;border-radius:50%;background:linear-gradient(180deg,#FFD54F,#FFC107 55%,#E3A600)"></div>
<img src="{CUT}" style="position:absolute;left:-40px;bottom:0;height:640px"></div>
<div class="a" style="left:600px;top:720px">
<div style="font-weight:900;font-size:30px;letter-spacing:1px;line-height:1.25">LET'S BUILD SOMETHING<br>MEMORABLE<span style="color:{GOLD}">.</span></div>
<div style="margin-top:28px;display:flex;flex-direction:column;gap:18px;font-weight:700;font-size:26px">""" + ''.join(
    f'<div style="display:flex;align-items:center;gap:16px">{ic(k)}{t}</div>' for k, t in con) + f"""</div></div>
<div class="a" style="right:90px;bottom:110px">{dots(5, 4)}</div>""", foot=False))

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
    pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
    for k, h in enumerate(SL, 1):
        if os.environ.get('ONLY') and str(k) != os.environ['ONLY']: continue
        t = f'/tmp/_fd{k}.html'; open(t, 'w').write(h); pg.goto(pathlib.Path(t).as_uri()); pg.wait_for_timeout(900)
        pg.evaluate("""()=>{for(const s of document.querySelectorAll('svg.hs')){const bb=s.getBBox();
            s.setAttribute('viewBox',`${bb.x} ${bb.y} ${bb.width} ${bb.height}`);s.setAttribute('width',bb.width);s.setAttribute('height',bb.height)}}""")
        pg.wait_for_timeout(150); pg.screenshot(path='/tmp/_fd.png')
        im = Image.open('/tmp/_fd.png').convert('RGB'); im.save(f'{OUT}/{k:02d}.jpg', quality=93, subsampling=0)
        im.resize((1080, 1350), Image.LANCZOS).save(f'{OUT}/{k:02d}-1080.jpg', quality=93, subsampling=0)
    b.close()
print('slides', len(SL))
