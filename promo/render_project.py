"""DANAG STUDIO promo flyer: "Let's handle your next DESIGN PROJECT" (recreated from a reference Danag loves).
Usage: python3 promo/render_project.py OUT_BASENAME [PORTRAIT_PNG_WITH_TRANSPARENCY|-] [navy|white]
Without a portrait a neutral placeholder is drawn where Danag's cut-out photo goes.
Navy gradient (no glow), grain, faint collage of Danag's own work, logo once, stem-thick gold dot.
"""
import sys, os, pathlib, re
from playwright.sync_api import sync_playwright
from PIL import Image
P = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(P); B = f'{R}/book-flyer'
sys.path.insert(0, B)
import render_book as rb
from contacts import IC

out = sys.argv[1]; portrait = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] != '-' else None
TH = sys.argv[3] if len(sys.argv) > 3 else 'navy'; DARK = TH != 'white'
A = f'{R}/portfolio/src/assets'
WORK = ['my-beast-nj', 'my-dallas', 'fl-ss-open', 'my-xmas', 'my-exclyusif', 'my-100k', 'ss-student', 'my-tamale']
GOLD = '#FFC107'
F = f'{R}/fonts/'
logo = re.sub(r'<\?xml[^>]*>', '', open(f'{B}/logo-on-{"navy" if DARK else "white"}.svg').read()).replace('<svg', '<svg style="height:58px;width:auto;display:block"', 1)
INK = '#fff' if DARK else '#022452'
ic = lambda k, c=None, s=26: (lambda c:  f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" style="color:{c};flex:none">{IC[k]}</svg>')(c or INK)

cap = rb.fit('PROJECT', 500, 190, True)
l1 = rb.line('DESIGN', cap, '#fff' if DARK else '#022452')
l2 = rb.line('PROJECT', cap, '#fff' if DARK else '#022452', True, dot_color=GOLD)
tiles = ''.join(f'<div style="background:url({pathlib.Path(f"{A}/{w}.jpg").as_uri()}) center top/cover"></div>' for w in WORK)
svc = ''.join(f'<div style="display:flex;align-items:center;gap:14px"><span style="width:10px;height:10px;border-radius:50%;background:{GOLD};flex:none"></span>{s}</div>'
              for s in ['Flyer &amp; Poster Design', 'Social Media Design', 'Product Visuals', 'Website Design'])
if portrait:
    person = f'<img src="{pathlib.Path(portrait).as_uri()}" style="position:absolute;right:-230px;bottom:0;height:880px;-webkit-mask-image:linear-gradient(90deg,transparent 0,#000 90px);filter:drop-shadow(0 20px 40px rgba(1,15,33,.35))">'
else:
    person = ('<div style="position:absolute;right:30px;bottom:0;width:400px;height:640px;border-radius:200px 215px 0 0;'
              'background:linear-gradient(180deg,rgba(255,255,255,.18),rgba(255,255,255,.06));border:2px dashed rgba(255,255,255,.45);'
              'display:flex;align-items:center;justify-content:center;text-align:center;color:rgba(255,255,255,.75);font-weight:700;font-size:24px;letter-spacing:4px">YOUR<br>PORTRAIT<br>HERE</div>')

BG = 'linear-gradient(135deg,#032F65 0%,#022452 45%,#011631 80%,#010F21 100%)' if DARK else 'linear-gradient(180deg,#ffffff 0%,#eef1f6 100%)'
OV = 'linear-gradient(180deg,#022a5c 0%,rgba(2,36,82,.55) 22%,rgba(2,36,82,.62) 55%,#022452 100%)' if DARK else 'linear-gradient(180deg,#ffffff 0%,rgba(255,255,255,.45) 22%,rgba(244,246,250,.55) 55%,#f1f3f8 100%)'
GLOW = '' if DARK else '<div class="a" style="width:640px;height:640px;left:-330px;top:-300px;border-radius:50%;filter:blur(30px);background:radial-gradient(circle,rgba(255,193,7,.26) 0%,transparent 62%);z-index:1"></div>'
html = f"""<html><head><style>
@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}
@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}
@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;color:{INK};
 background:{BG}}}
.a{{position:absolute}}
</style></head><body>{GLOW}
<div class="a" style="left:0;top:170px;width:1080px;height:600px;display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:1fr 1fr;gap:6px;opacity:{".55" if DARK else ".22"};filter:grayscale({".35" if DARK else "1"})">{tiles}</div>
<div class="a" style="left:0;top:170px;width:1080px;height:600px;background:{OV};mix-blend-mode:normal"></div>
<div class="a" style="left:0;top:170px;width:1080px;height:600px;background:#032F65;mix-blend-mode:color;opacity:{".75" if DARK else ".35"}"></div>
<div class="a" style="left:610px;top:440px;width:660px;height:660px;border-radius:50%;background:linear-gradient(160deg,#FFD54F,#FFC107 55%,#E3A600)"></div>
{person}
<div class="a" style="left:72px;top:455px;width:600px">
 <div style="display:flex;align-items:center;justify-content:space-between">
  <div style="font-weight:700;font-size:25px;letter-spacing:5px;color:{GOLD if DARK else '#b38600'}">LET'S HANDLE YOUR NEXT</div>
 </div>
 <div style="margin-top:22px">{l1}</div>
 <div style="margin-top:16px">{l2}</div>
 <div style="position:relative;margin-top:44px;width:470px">
  <div style="position:absolute;left:0;top:-24px;background:{GOLD};color:#022452;font-weight:900;font-size:23px;letter-spacing:2px;padding:12px 26px;border-radius:30px 30px 30px 0">SERVICES OFFERED</div>
  <div style="background:{"rgba(1,15,33,.88)" if DARK else "#022452"};color:#fff;padding:42px 30px 22px;display:flex;flex-direction:column;gap:8px;font-weight:700;font-size:25px">{svc}</div>
 </div>
 <div style="margin-top:30px;font-weight:700;font-size:21px;letter-spacing:5px;color:{GOLD if DARK else '#b38600'}">REACH ME ON WHATSAPP</div>
 <div style="font-weight:900;font-size:48px;letter-spacing:-1px;margin-top:6px">+233 50 332 0548</div>
 <div style="display:flex;align-items:center;gap:16px;margin-top:18px">
  <div style="background:{GOLD};color:#022452;font-weight:900;font-size:20px;letter-spacing:1px;padding:10px 22px">FOLLOW ME</div>
  {ic('IG',s=24)}{ic('TT',s=24)}{ic('X',s=24)}<span style="font-weight:700;font-size:21px">@thedanagstudio</span>
 </div>
</div>
<div class="a" style="left:72px;top:64px">{logo}</div><div class="a" style="right:72px;top:80px;font-weight:700;font-size:20px;letter-spacing:6px;color:{"rgba(255,255,255,.7)" if DARK else "#b38600"}">CROWNED IN CRAFT</div>
<div class="a" style="inset:0;z-index:50;pointer-events:none;opacity:{'.16' if DARK else '.12'};mix-blend-mode:{'overlay' if DARK else 'multiply'};background-size:256px;background-image:url({R}/grain.png)"></div>
</body></html>"""
tmp = '/tmp/_proj.html'; open(tmp, 'w').write(html)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
    pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
    pg.goto(pathlib.Path(tmp).as_uri()); pg.wait_for_timeout(1200)
    pg.evaluate("""()=>{for(const s of document.querySelectorAll('svg.hs')){const bb=s.getBBox();
        s.setAttribute('viewBox',`${bb.x} ${bb.y} ${bb.width} ${bb.height}`);s.setAttribute('width',bb.width);s.setAttribute('height',bb.height)}}""")
    pg.wait_for_timeout(200); pg.screenshot(path='/tmp/_proj.png'); b.close()
im = Image.open('/tmp/_proj.png').convert('RGB')
os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
im.save(out + '.jpg', quality=95, subsampling=0)
im.resize((1080, 1350), Image.LANCZOS).save(out + '-1080.jpg', quality=95, subsampling=0)
print('ok', out, cap)
