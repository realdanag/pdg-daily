"""Happy Sunday portrait set, white theme (guides: references/sunday 04-07, Danag 22 Nov 2026; he loved 06 and 07).
Variants: c = split panel + halo + stacked SU/ND/AY (04), d = script Happy + SUN DAY right, ring, services band (05),
          e = giant condensed SUN | DAY with portrait between, navy band, centred message (06),
          f = big HAPPY SUNDAY over portrait, faceted background, navy shard footer (07).
Ideas shared across: greyscale portrait, gold dot grids, gold spheres, gold message box. Navy/white/gold only.
Usage: python3 promo/render_sunday_set.py OUT VARIANT YYYY-MM-DD "message" [portrait.png] [portrait height px, v2e]
"""
import sys, os, re, random, pathlib, datetime as dt
from playwright.sync_api import sync_playwright
from PIL import Image
P = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(P); B = f'{R}/book-flyer'
sys.path.insert(0, B)
import render_book as rb
from contacts import IC
out, V, ds, msg = sys.argv[1:5]
PSRC = pathlib.Path(sys.argv[5] if len(sys.argv) > 5 else f'{R}/assets-hero/S1-cut.png').resolve(); PORT = PSRC.as_uri()
PH = float(sys.argv[6]) if len(sys.argv) > 6 else None  # optional portrait height (v2e), centred by the photo's aspect
_pw, _ph = Image.open(PSRC).size; ASP = _pw / _ph
d = dt.date.fromisoformat(ds)
F = f'{R}/fonts/'; G = '#FFC107'; G2 = '#E3A600'; N = '#022452'; SUB = '#3a4d6e'
NAVYGR = 'linear-gradient(135deg,#033A7A 0%,#022452 50%,#011631 100%)'
GOLDGR = f'linear-gradient(135deg,#FFD54F 0%,{G} 55%,{G2} 100%)'
def logo(on, h=56):
    return re.sub(r'<\?xml[^>]*>', '', open(f'{B}/logo-on-{on}.svg').read()).replace('<svg', f'<svg style="height:{h}px;width:auto;display:block"', 1)
ic = lambda k, c, s=18: f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" style="color:{c};flex:none">{IC[k]}</svg>'
circ = lambda k, bg, fg, s=34: f'<span style="width:{s}px;height:{s}px;border-radius:50%;background:{bg};display:inline-flex;align-items:center;justify-content:center;flex:none">{ic(k, fg, int(s*.52))}</span>'
def dots(c, cols=5, rows=6, gap=26, r=4):
    return f'<svg width="{cols*gap}" height="{rows*gap}">' + ''.join(f'<circle cx="{gap/2+i*gap}" cy="{gap/2+j*gap}" r="{r}" fill="{c}"/>' for i in range(cols) for j in range(rows)) + '</svg>'
sphere = lambda x, y, s: f'<div class="a" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px;border-radius:50%;background:radial-gradient(circle at 32% 28%,#FFF3C4 0%,#FFD54F 22%,{G} 50%,{G2} 80%,#B98500 100%);box-shadow:0 {s*.18:.0f}px {s*.35:.0f}px rgba(185,133,0,.35)"></div>'
def datebox(c1=N, c2=G, s=1.0):
    return (f'<div style="display:flex;align-items:center;gap:{14*s:.0f}px"><div style="font-weight:900;font-size:{70*s:.0f}px;line-height:.78;color:{c2};letter-spacing:-3px">{d.strftime("%d")}</div>'
            f'<div style="width:3px;height:{54*s:.0f}px;background:{c2}"></div><div style="font-weight:700;font-size:{16*s:.0f}px;letter-spacing:5px;line-height:1.55;color:{c1}">{d.strftime("%A").upper()}'
            f'<span style="display:block;font-weight:900;font-size:{25*s:.0f}px;letter-spacing:3px;line-height:1.1;margin-top:3px;color:{c2}">{d.strftime("%B").upper()}</span></div></div>')
def contact(fg, circbg, phfg=N, s=1.0):
    return (f'<div style="display:flex;align-items:center;gap:10px;font-weight:900;font-size:{24*s:.0f}px;color:{fg};white-space:nowrap">{circ("PH", G, phfg, int(32*s))}+233 (0)50 332 0548</div>')
def handles(fg, circbg, cfg='#fff', s=1.0):
    return (f'<div style="display:flex;align-items:center;gap:7px;font-weight:700;font-size:{19*s:.0f}px;color:{fg};white-space:nowrap">'
            f'{circ("IG", circbg, cfg, int(30*s))}{circ("TT", circbg, cfg, int(30*s))}{circ("X", circbg, cfg, int(30*s))}<span style="margin-left:4px">@thedanagstudio</span></div>')
GREY = 'filter:grayscale(1) contrast(1.08) brightness(1.03)'

if V == 'c':  # split panel (04)
    big = lambda t, c: f'<div style="font-weight:900;font-size:206px;line-height:.86;letter-spacing:-6px;color:{c}">{t}</div>'
    body = f"""
<div class="a" style="left:0;top:0;width:540px;height:1350px;background:{NAVYGR}"></div>
<div class="a" style="left:0;top:0;width:540px;height:1350px;background:radial-gradient(circle at 60% 40%,rgba(255,193,7,.16),transparent 55%)"></div>
<div class="a" style="left:60px;top:64px">{logo('navy', 50)}</div>
<div class="a" style="left:330px;top:150px;opacity:.85">{dots('#fff')}</div>
<div class="a" style="left:110px;top:330px;width:500px;height:500px;border-radius:50%;background:#fff;box-shadow:0 0 0 14px rgba(255,193,7,.9),0 0 90px rgba(255,193,7,.35)"></div>
<div class="a" style="left:-40px;bottom:0;width:960px;height:1030px;overflow:hidden"><img src="{PORT}" style="position:absolute;left:0;bottom:0;height:1030px;{GREY};filter:grayscale(1) contrast(1.1) drop-shadow(0 20px 40px rgba(0,0,0,.35))"></div>
<div class="a" style="right:60px;top:70px">{datebox()}</div>
{sphere(1010, 210, 120)}{sphere(470, 1225, 80)}
<div class="a" style="left:620px;top:280px">
 <div style="display:inline-block;background:{GOLDGR};color:{N};font-weight:900;font-size:48px;letter-spacing:2px;padding:6px 24px;line-height:1.1">HAPPY</div>
 <div style="margin-top:22px">{big('SU', N)}{big('ND', N)}{big('AY', G)}</div>
 <div style="margin-top:30px;width:400px;background:{GOLDGR};color:{N};font-weight:600;font-size:23px;line-height:1.42;padding:20px 24px">{msg}</div>
 <div style="display:inline-block;margin-top:16px;background:{N};color:#fff;font-weight:900;font-size:20px;letter-spacing:1.5px;padding:10px 18px">HAVE A BLESSED SUNDAY</div>
</div>
<div class="a" style="right:60px;bottom:70px;display:flex;flex-direction:column;align-items:flex-end;gap:14px">{contact(N, N)}{handles(N, N)}</div>"""

elif V == 'd':  # script Happy, SUN DAY right, ring, services band (05)
    body = f"""
<div class="a" style="inset:0;background:linear-gradient(180deg,#ffffff 0%,#ffffff 45%,#FFF6DA 100%)"></div>
<div class="a" style="left:-190px;top:-230px;width:500px;height:500px;border-radius:50%;border:58px solid {G};opacity:.95"></div>
<div class="a" style="left:300px;top:340px;width:34px;height:34px;border-radius:50%;border:7px solid {N}"></div>
<div class="a" style="right:70px;top:70px">{logo('white', 56)}</div>
<div class="a" style="left:70px;top:300px;opacity:.9">{dots(G, 4, 5)}</div>
<img class="a" src="{PORT}" style="left:-70px;bottom:0;height:950px;{GREY};filter:grayscale(1) contrast(1.1) drop-shadow(0 20px 40px rgba(2,36,82,.25))">
<div class="a" style="right:80px;top:250px;text-align:right">
 <div style="font-family:S;font-size:150px;line-height:.7;color:{G2};margin-right:10px">Happy</div>
 <div style="font-weight:900;font-size:210px;line-height:.86;letter-spacing:-7px;color:{N};margin-top:6px">SUN<br>DAY</div>
 <div style="display:flex;justify-content:flex-end;margin-top:34px"><div style="width:400px;font-weight:500;font-size:24px;line-height:1.45;color:{SUB}">{msg}</div><div style="width:4px;background:{G};margin-left:20px"></div></div>
 <div style="margin-top:28px;display:flex;justify-content:flex-end">{datebox(N, G, .85)}</div>
</div>
<div class="a" style="left:0;right:0;bottom:0;height:170px;background:{NAVYGR};opacity:.96;border-top:5px solid {G}"></div>
<div class="a" style="left:70px;bottom:44px;color:#fff;font-weight:700;font-size:19px;letter-spacing:1px;line-height:1.5">FLYERS &amp; POSTERS,<br>SOCIAL MEDIA DESIGNS,<br>WEBSITES, etc.</div>
<div class="a" style="right:70px;bottom:40px;display:flex;flex-direction:column;align-items:flex-end;gap:12px">{contact('#fff', G)}{handles('#fff', 'rgba(255,255,255,.14)')}</div>"""

elif V == 'e':  # giant condensed SUN | DAY, portrait between, navy band (06)
    cap = 272
    sun = rb.line('SUN', cap, N); day = rb.line('DAY', cap, N)
    ws, wd = rb.width('SUN', cap), rb.width('DAY', cap)
    body = f"""
<div class="a" style="inset:0;background:#fff"></div>
<svg class="a" width="1080" height="1350" style="left:0;top:0"><polygon points="1080,0 1080,1190 120,1190" fill="#EEF3FA"/></svg>
<div class="a" style="left:70px;top:70px">{datebox()}</div>
<div class="a" style="right:70px;top:84px">{handles(N, N, s=.95)}</div>
<div class="a" style="left:60px;top:250px">{sun}</div>
<div class="a" style="left:{1080-60-wd:.0f}px;top:400px">{day}</div>
<div class="a" style="right:60px;top:318px;background:{GOLDGR};color:{N};font-weight:900;font-size:62px;letter-spacing:2px;padding:0 20px;line-height:72px;height:72px">HAPPY</div>
<div class="a" style="left:0;right:0;top:380px;height:22px;background:linear-gradient(180deg,rgba(255,255,255,0),rgba(255,255,255,.55) 45%,rgba(2,36,82,.10) 55%,rgba(2,36,82,0));z-index:1"></div>
<div class="a" style="left:0;right:0;top:780px;height:130px;background:{NAVYGR};border-bottom:5px solid {G}"></div>
<div class="a" style="right:110px;top:810px;opacity:.9">{dots(G, 9, 3, 22, 3)}</div>
<div class="a" style="left:0;top:0;width:1080px;height:910px;overflow:hidden;z-index:2"><img src="{PORT}" style="position:absolute;left:{540-(PH or 820)*ASP/2:.0f}px;top:{400 if not PH else 410}px;height:{PH or 820:.0f}px;{"-webkit-mask-image:linear-gradient(90deg,transparent 0,#000 14%,#000 86%,transparent 100%);" if PH else ""}filter:grayscale(1) contrast(1.1) drop-shadow(0 20px 40px rgba(2,36,82,.3))"></div>
<div class="a" style="left:140px;right:140px;top:960px;text-align:center;font-weight:700;font-size:31px;line-height:1.45;color:{N}">“{msg}”
 <div style="width:90px;height:5px;background:{G};margin:22px auto 0"></div></div>
<div class="a" style="left:0;right:0;bottom:0;height:160px;background:{NAVYGR};border-top:5px solid {G}"></div>
<div class="a" style="left:70px;bottom:52px">{logo('navy', 56)}</div>
<div class="a" style="right:70px;bottom:62px">{contact('#fff', G)}</div>"""

elif V == 'f':  # big HAPPY SUNDAY, faceted bg, navy shard footer (07)
    random.seed(22)
    pts = {}
    for j in range(-1, 9):
        for i in range(-1, 8):
            pts[i, j] = (i * 180 + random.uniform(-60, 60), j * 180 + random.uniform(-60, 60))
    tri = ''
    for j in range(-1, 8):
        for i in range(-1, 7):
            a, b, c, e = pts[i, j], pts[i+1, j], pts[i, j+1], pts[i+1, j+1]
            for t in ((a, b, c), (b, e, c)):
                sh = random.randint(236, 252); tri += f'<polygon points="{" ".join(f"{x:.0f},{y:.0f}" for x, y in t)}" fill="rgb({sh},{sh+1},{min(255, sh+4)})"/>'
    body = f"""
<svg class="a" width="1080" height="1350" style="left:0;top:0">{tri}</svg>
<div class="a" style="left:70px;top:64px">{logo('white', 50)}</div>
<div class="a" style="right:70px;top:64px">{datebox(N, G, .8)}</div>
<div class="a" style="left:0;right:0;top:180px;text-align:center;font-weight:900;line-height:.9;letter-spacing:-6px;background:linear-gradient(180deg,#033A7A 0%,{N} 60%,#011631 100%);-webkit-background-clip:text;color:transparent;filter:drop-shadow(0 8px 14px rgba(2,36,82,.18))">
 <div style="font-size:190px">HAPPY</div><div style="font-size:190px">SUNDAY</div></div>
<svg class="a" width="1080" height="1350" style="left:0;top:0"><polygon points="1080,640 1080,900 380,1180 330,1090" fill="{G}" opacity=".85"/><polygon points="1080,600 1080,640 330,1090 300,1060" fill="{G2}" opacity=".5"/></svg>
<img class="a" src="{PORT}" style="left:{540-430:.0f}px;bottom:120px;height:860px;filter:drop-shadow(0 24px 40px rgba(2,36,82,.28))">
<div class="a" style="left:700px;top:560px;width:310px;font-weight:600;font-size:23px;line-height:1.45;color:{N}">{msg}</div>
<svg class="a" width="1080" height="1350" style="left:0;top:0"><defs><linearGradient id="nv" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#033A7A"/><stop offset=".5" stop-color="{N}"/><stop offset="1" stop-color="#011631"/></linearGradient>
 <pattern id="dp" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="11" cy="11" r="2.4" fill="#fff" opacity=".08"/></pattern></defs>
 <polygon points="0,1130 1080,1010 1080,1350 0,1350" fill="url(#nv)"/><polygon points="0,1130 1080,1010 1080,1350 0,1350" fill="url(#dp)"/>
 <polygon points="0,1122 1080,1002 1080,1012 0,1132" fill="{G}"/></svg>
{sphere(940, 940, 70)}
<div class="a" style="left:70px;right:70px;bottom:60px;display:flex;justify-content:space-between;align-items:center">{contact('#fff', G)}{handles('#fff', 'rgba(255,255,255,.14)')}</div>"""
else:
    sys.exit('variant must be c, d, e or f')

html = f"""<html><head><style>
@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}
@font-face{{font-family:M;font-weight:600;src:url({F}montserrat-latin-600-normal.woff2)}}
@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}
@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
@font-face{{font-family:S;src:url({F}sacramento-latin-400-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;color:{N};background:#fff}}
.a{{position:absolute}}
</style></head><body>{body}
<div class="a" style="inset:0;z-index:50;pointer-events:none;opacity:.10;mix-blend-mode:multiply;background-size:256px;background-image:url({R}/grain.png)"></div>
<script>document.fonts.ready.then(()=>document.body.dataset.done=1)</script></body></html>"""
tmp = f'/tmp/_sset{V}.html'; open(tmp, 'w').write(html)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
    pg.goto(pathlib.Path(tmp).as_uri()); pg.wait_for_selector('body[data-done]'); pg.wait_for_timeout(400)
    pg.screenshot(path=f'/tmp/_sset{V}.png'); b.close()
im = Image.open(f'/tmp/_sset{V}.png').convert('RGB')
im.save(out + '.jpg', quality=93, subsampling=0); im.resize((1080, 1350), Image.LANCZOS).save(out + '-1080.jpg', quality=93)
print('ok', out)
