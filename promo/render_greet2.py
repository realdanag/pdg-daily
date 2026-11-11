"""Greeting flyer style 2 (guide: the "Happy New Month" reference): mixed-case headline with gradient second word,
date label over a big gold arrow, short message, giant cropped day letters at the bottom, contact pill.
Usage: python3 promo/render_greet2.py OUT_BASENAME DAY_WORD DATE_NUM MONTH "BODY" [white|navy]
  e.g. python3 promo/render_greet2.py flyers/2026-11-12 Thursday 12 November "..." white
Writes OUT.jpg (2160x2700) and OUT-tiktok.jpg (1080x1350). Navy has no glow; white has a soft gold glow top-left.
"""
import sys, os, pathlib, re
from playwright.sync_api import sync_playwright
from PIL import Image
P = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(P); B = f'{R}/book-flyer'
sys.path.insert(0, B)
import render_book as rb
from contacts import IC

out, day, num, mon, body = sys.argv[1:6]
TH = sys.argv[6] if len(sys.argv) > 6 else 'white'; DARK = TH != 'white'
GOLD = '#FFC107'; F = f'{R}/fonts/'
INK = '#fff' if DARK else '#022452'; SOFT = 'rgba(255,255,255,.72)' if DARK else '#4d5870'
NAVYG = 'linear-gradient(135deg,#032F65 0%,#022452 45%,#011631 80%,#010F21 100%)'
GOLDG = 'linear-gradient(180deg,#FFD54F 0%,#FFC107 55%,#E3A600 100%)'
BG = NAVYG if DARK else 'linear-gradient(180deg,#ffffff 0%,#eef1f6 100%)'
logo = re.sub(r'<\?xml[^>]*>', '', open(f'{B}/logo-on-{"navy" if DARK else "white"}.svg').read()).replace('<svg', '<svg style="height:60px;width:auto;display:block"', 1)
ic = lambda k, c, s=24: f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" style="color:{c};flex:none">{IC[k]}</svg>'
circ = lambda k: f'<span style="width:38px;height:38px;border-radius:50%;background:{GOLD if DARK else "#022452"};display:inline-flex;align-items:center;justify-content:center">{ic(k, "#022452" if DARK else "#fff", 20)}</span>'
GLOW = '' if DARK else '<div class="a" style="width:700px;height:700px;left:-360px;top:-320px;border-radius:50%;filter:blur(30px);background:radial-gradient(circle,rgba(255,193,7,.26) 0%,transparent 62%)"></div>'
big_fill = 'linear-gradient(180deg,rgba(255,255,255,.95),rgba(255,255,255,.80))' if DARK else NAVYG
dot_c = '#fff' if DARK else '#022452'

html = f"""<html><head><style>
@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}
@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}
@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;color:{INK};background:{BG}}}
.a{{position:absolute}}
.gt{{-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;padding-right:.06em}}
</style></head><body>{GLOW}
<svg class="a" viewBox="252 255 749 664" style="right:-200px;top:300px;width:700px;opacity:{'.05' if DARK else '.045'}"><path fill="{INK}" fill-rule="evenodd" d="{rb.MK['nodot']}"/><path fill="{INK}" d="{rb.MK['dot']}"/></svg>
<div class="a" style="left:72px;top:64px;display:flex;align-items:center;gap:22px">{logo}<span style="width:2px;height:46px;background:{GOLD}"></span><span style="font-weight:700;font-size:19px;letter-spacing:5px;color:{SOFT}">CROWNED IN CRAFT</span></div>
<div class="a" style="right:72px;top:70px;display:flex;align-items:center;gap:8px">{circ('IG')}{circ('TT')}{circ('X')}<span style="margin-left:8px;font-weight:700;font-size:20px">@thedanagstudio</span></div>

<div class="a" id="hd" style="left:72px;top:215px">
 <div class="gt" style="font-weight:900;font-size:172px;line-height:1;letter-spacing:-6px;background-image:{NAVYG if not DARK else 'linear-gradient(180deg,#fff,#dfe6f2)'}">Happy</div>
 <div style="display:flex;align-items:baseline"><span class="gt" style="font-weight:900;font-size:172px;line-height:1.05;letter-spacing:-6px;background-image:{GOLDG}">{day}</span><span style="display:inline-block;width:.236em;height:.236em;font-size:172px;border-radius:50%;background:{dot_c};margin-left:.01em"></span></div>
</div>
<div class="a" style="right:72px;top:236px;text-align:right">
 <div style="font-weight:900;font-size:24px;letter-spacing:4px;color:{GOLD if DARK else '#b38600'}">{num} {mon.upper()}</div>
 <svg viewBox="0 0 120 120" width="140" height="140" style="display:block;margin:10px 0 0 auto"><defs><linearGradient id="ag" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#E3A600"/><stop offset=".55" stop-color="#FFC107"/><stop offset="1" stop-color="#FFE082"/></linearGradient></defs>
 <path d="M14 106 L84 36 L44 36 L44 14 L106 14 L106 76 L84 76 L84 51 L29 106 Z" fill="url(#ag)"/></svg>
</div>
<div class="a" style="left:72px;top:690px;border-left:5px solid #FFC107;padding-left:26px;margin-left:0;width:760px;font-weight:500;font-size:31px;line-height:1.5;color:{SOFT}">{body}</div>

<div class="a" style="left:-30px;right:-30px;bottom:-170px;text-align:center;white-space:nowrap"><span class="gt" style="font-weight:900;font-size:610px;line-height:1;letter-spacing:-30px;background-image:{big_fill}">{day[:3].upper()}</span></div>
<div class="a" style="left:72px;bottom:72px;display:flex;align-items:center;gap:14px;background:{GOLD};color:#022452;height:76px;padding:0 34px 0 14px;border-radius:40px;font-weight:900;font-size:28px;box-shadow:0 14px 30px rgba(1,15,33,.25)"><span style="width:52px;height:52px;border-radius:50%;background:#022452;display:flex;align-items:center;justify-content:center">{ic('PH', GOLD, 26)}</span>+233 (0)50 332 0548</div>
<div class="a" style="inset:0;z-index:50;pointer-events:none;opacity:{'.16' if DARK else '.12'};mix-blend-mode:{'overlay' if DARK else 'multiply'};background-size:256px;background-image:url({R}/grain.png)"></div>
</body></html>"""
tmp = '/tmp/_g2.html'; open(tmp, 'w').write(html)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
    pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
    pg.goto(pathlib.Path(tmp).as_uri()); pg.wait_for_timeout(1200)
    pg.screenshot(path='/tmp/_g2.png'); b.close()
im = Image.open('/tmp/_g2.png').convert('RGB')
os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
im.save(out + '.jpg', quality=97, subsampling=0)
im.resize((1080, 1350), Image.LANCZOS).save(out + '-tiktok.jpg', quality=97, subsampling=0)
print('ok', out)
