"""Happy Sunday (guide: references/sunday 01-02): giant condensed SUNDAY behind a portrait cut-out, HAPPY in a gold box,
LOVE/JOY/PEACE tags, verse, ring text. Navy, no glow.
Usage: python3 promo/render_sunday.py OUT YYYY-MM-DD [portrait.png]
"""
import sys, os, re, pathlib, datetime as dt
from playwright.sync_api import sync_playwright
from PIL import Image
P = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(P); B = f'{R}/book-flyer'
sys.path.insert(0, B)
import render_book as rb
from contacts import IC
out, ds = sys.argv[1:3]
PORT = pathlib.Path(sys.argv[3] if len(sys.argv) > 3 else '/home/claude/assets/danag-portrait-cut.png').as_uri()
d = dt.date.fromisoformat(ds)
F = f'{R}/fonts/'; G = '#FFC107'; N = '#022452'
logo = re.sub(r'<\?xml[^>]*>', '', open(f'{B}/logo-on-navy.svg').read()).replace('<svg', '<svg style="height:56px;width:auto;display:block"', 1)
ic = lambda k, c, s=18: f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" style="color:{c};flex:none">{IC[k]}</svg>'
cap = 470
while rb.width('SUNDAY', cap) > 900: cap -= 4
big = rb.line('SUNDAY', cap, '#fff')
bw = rb.width('SUNDAY', cap)
ring = 'SUNDAY VIBES  ·  CROWNED IN CRAFT  ·  '
html = f"""<html><head><style>
@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}
@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}
@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;color:#fff;background:linear-gradient(160deg,#032F65 0%,#022452 40%,#011631 78%,#010F21 100%)}}
.a{{position:absolute}} .tag{{background:{G};color:{N};font-weight:900;font-size:22px;letter-spacing:4px;padding:10px 0;width:170px;text-align:center;border-radius:4px}}
</style></head><body>
<svg class="a" viewBox="252 255 749 664" style="left:-240px;top:520px;width:640px;opacity:.035"><path fill="#fff" fill-rule="evenodd" d="{rb.MK['nodot']}"/><path fill="#fff" d="{rb.MK['dot']}"/></svg>
<div class="a" style="left:90px;top:84px">{logo}</div>
<div class="a" style="right:90px;top:84px;display:flex;align-items:center;gap:18px">
 <div style="font-weight:900;font-size:88px;line-height:.78;color:{G};letter-spacing:-3px">{d.strftime('%d')}</div>
 <div style="width:3px;height:66px;background:{G}"></div>
 <div style="font-weight:700;font-size:19px;letter-spacing:6px;line-height:1.55">SUNDAY<span style="display:block;font-weight:900;font-size:30px;letter-spacing:4px;line-height:1.1;margin-top:4px;color:{G}">{d.strftime('%B').upper()}</span></div>
</div>
<div class="a" style="left:{(1080 - bw) / 2:.0f}px;top:300px">{big}</div>
<div class="a" style="left:{(1080 - bw) / 2 + bw - 330:.0f}px;top:236px;background:{G};color:{N};font-weight:900;font-size:66px;letter-spacing:2px;padding:4px 22px;line-height:1.05">HAPPY</div>
<img class="a" src="{PORT}" style="left:50%;transform:translateX(-50%);bottom:0;height:1010px;filter:drop-shadow(0 30px 50px rgba(0,0,0,.5))">
<div class="a" style="left:0;right:0;bottom:0;height:260px;background:linear-gradient(180deg,transparent,rgba(1,15,33,.92))"></div>
<div class="a" style="left:90px;top:840px;display:flex;flex-direction:column;gap:12px"><div class="tag">LOVE</div><div class="tag" style="background:#fff">JOY</div><div class="tag">PEACE</div></div>
<div class="a" style="right:90px;top:820px;width:250px;text-align:right;font-weight:500;font-size:20px;line-height:1.45;color:#dfe5f1">I will bless the Lord at all times: his praise shall continually be in my mouth.<div style="color:{G};font-weight:700;margin-top:8px">Psalm 34:1</div></div>
<svg class="a" viewBox="0 0 300 300" style="right:40px;bottom:120px;width:210px;height:210px"><defs><path id="c" d="M150,150 m-112,0 a112,112 0 1,1 224,0 a112,112 0 1,1 -224,0"/></defs>
 <circle cx="150" cy="150" r="138" fill="none" stroke="{G}" stroke-width="2"/><text font-family="M" font-weight="900" font-size="22" letter-spacing="5" fill="{G}"><textPath href="#c" textLength="690">{ring}</textPath></text>
 <circle cx="150" cy="150" r="13" fill="{G}"/></svg>
<div class="a" style="left:90px;bottom:80px;display:flex;align-items:center;gap:12px;font-weight:900;font-size:28px"><span style="width:38px;height:38px;border-radius:50%;background:{G};display:inline-flex;align-items:center;justify-content:center">{ic('PH', N)}</span>+233 (0)50 332 0548</div>
<div class="a" style="left:90px;bottom:40px;font-weight:700;font-size:19px;color:#c9d3e6">@thedanagstudio</div>
<div class="a" style="inset:0;z-index:50;pointer-events:none;opacity:.16;mix-blend-mode:overlay;background-size:256px;background-image:url({R}/grain.png)"></div>
<script>document.fonts.ready.then(()=>document.body.dataset.done=1)</script></body></html>"""
tmp = '/tmp/_sun.html'; open(tmp, 'w').write(html)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
    pg.goto(pathlib.Path(tmp).as_uri()); pg.wait_for_selector('body[data-done]'); pg.wait_for_timeout(400)
    pg.screenshot(path='/tmp/_sun.png'); b.close()
im = Image.open('/tmp/_sun.png').convert('RGB')
im.save(out + '.jpg', quality=93, subsampling=0); im.resize((1080, 1350), Image.LANCZOS).save(out + '-1080.jpg', quality=93)
print('ok', out)
