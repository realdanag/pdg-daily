"""Design Tip 05: How eyes read your design. Linking (seamless) carousel, 8 slides on one wide canvas with a gold thread.
Guide: references/2026-11-14 (Brandlite / FEFTY hero-object tips). Navy, no glow.
Usage: python3 promo/render_tip05.py OUTDIR
"""
import sys, os, re, math, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image
P = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(P); B = f'{R}/book-flyer'
sys.path.insert(0, B)
import render_book as rb
OUT = os.path.abspath(sys.argv[1]); os.makedirs(OUT, exist_ok=True)
F = f'{R}/fonts/'; G = '#FFC107'; A = f'{R}/assets-hero'
logo = re.sub(r'<\?xml[^>]*>', '', open(f'{B}/logo-on-navy.svg').read()).replace('<svg', '<svg style="height:50px;width:auto;display:block"', 1)
DOT = f'<span style="display:inline-block;width:.236em;height:.236em;border-radius:50%;background:{G};margin-left:.04em"></span>'
# (photo, bg-position, text box css, shade, lines, sub)
S = [
 ('T05-1.jpg', 'center', 'left:90px;bottom:250px;width:860px', 'linear-gradient(20deg,rgba(1,15,33,.9) 0%,rgba(1,15,33,.4) 50%,transparent 70%)',
  ['Your customers', "don't read.", 'They scan'], 'Eyes move fast. Good design works with that, not against it.', 'DESIGN TIP 05'),
 ('T05-2.jpg', 'center', 'left:90px;top:200px;width:820px', 'linear-gradient(160deg,rgba(1,15,33,.85) 0%,rgba(1,15,33,.3) 45%,transparent 60%)',
  ['Eyes start', 'top left'], 'Readers enter at the top left by instinct. Put your most important message there.', ''),
 ('T05-3.jpg', '0px -250px/125% auto no-repeat', 'left:90px;top:200px;width:900px', 'linear-gradient(180deg,rgba(1,15,33,.8) 0%,rgba(1,15,33,.3) 40%,transparent 55%)',
  ['Big things', 'get seen', 'first'], 'The largest element wins the first glance. Size things on purpose.', ''),
 ('T05-4-alt.jpg', '120px -110px/100% auto no-repeat', 'left:90px;bottom:250px;width:600px', 'linear-gradient(20deg,rgba(1,15,33,.9) 0%,rgba(1,15,33,.35) 50%,transparent 68%)',
  ['Contrast', 'leads the', 'eye'], 'Light against dark, bold against thin. Contrast is a map for the eye.', ''),
 ('T05-5.jpg', '300px 50%/auto 100% no-repeat', 'left:90px;top:200px;width:520px;--fs:70px', 'linear-gradient(90deg,rgba(1,15,33,.85) 0%,rgba(1,15,33,.3) 45%,transparent 62%)',
  ['Feeling', 'comes before', 'thinking'], 'People feel your design in a split second. The logic comes later.', ''),
 ('T05-6.jpg', 'center', 'left:90px;top:260px;width:360px;--fs:58px', 'linear-gradient(90deg,rgba(1,15,33,.88) 0%,rgba(1,15,33,.35) 45%,transparent 60%)',
  ['One surprise', 'makes it', 'stick'], "You don't need to change everything. One unexpected detail is enough.", ''),
 ('T05-7.jpg', 'center', 'left:90px;top:200px;width:900px', 'linear-gradient(180deg,rgba(1,15,33,.8) 0%,rgba(1,15,33,.3) 40%,transparent 55%)',
  ['Predictable', 'gets forgotten'], 'If it looks like everything else, the brain skips it.', ''),
 (None, 'center', 'left:140px;right:140px;top:420px;text-align:center', 'radial-gradient(520px 420px at 50% 50%,rgba(1,15,33,.6),transparent 70%)',
  ['Design for eyes,', 'not yourself'], 'Save this carousel and follow for more design tips.', ''),
]
N = len(S); W = 1080 * N
RINGS = ''.join(f'<svg class="a" viewBox="0 0 600 600" style="{p};width:620px;height:620px"><defs><linearGradient id="rg{k}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFF1C4"/><stop offset=".35" stop-color="#FFC107"/><stop offset=".7" stop-color="#C98F00"/><stop offset="1" stop-color="#7A5500"/></linearGradient></defs><ellipse cx="300" cy="300" rx="230" ry="150" transform="rotate({r} 300 300)" fill="none" stroke="url(#rg{k})" stroke-width="64"/><ellipse cx="300" cy="300" rx="230" ry="150" transform="rotate({r} 300 300)" fill="none" stroke="rgba(255,255,255,.35)" stroke-width="6" stroke-dasharray="180 900"/></svg>' for k, (p, r) in enumerate([('right:-230px;top:-170px', -28), ('left:-240px;bottom:-150px', -28)]))
def thread_y(x): return 1120 + 55 * math.sin(x / 1080 * math.pi * 1.0 + 0.6) + 20 * math.sin(x / 300)
pts = ' '.join(f'{x},{thread_y(x):.1f}' for x in range(0, W + 1, 12))
pts2 = ' '.join(f'{x},{thread_y(x) + 9 * math.sin(x / 90):.1f}' for x in range(0, W + 1, 12))
panels = ''
for i, (img, pos, box, shade, lines, sub, kick) in enumerate(S):
    x = i * 1080
    head = ''.join(f'<div style="color:{G if j % 2 else "#fff"}">{t}{DOT if j == len(lines) - 1 else ""}</div>' for j, t in enumerate(lines))
    cta = (f'<div style="display:inline-block;margin-top:34px;background:{G};color:#022452;border-radius:40px;padding:16px 30px;font-weight:900;font-size:26px">Book a design: +233 (0)50 332 0548</div>' if i == N - 1 else '')
    panels += f'''<div class="a" style="left:{x}px;top:0;width:1080px;height:1350px;overflow:hidden;background:#06101f">
 <div class="a" style="inset:0;background:{('url(' + pathlib.Path(f"{A}/{img}").as_uri() + ') ' + (pos if '/' in pos else pos + '/cover')) if img else 'linear-gradient(160deg,#032F65,#011631)'}"></div>
 {RINGS if not img else ''}
 <div class="a" style="inset:0;background:{shade}"></div>
 <div class="a" style="left:0;right:0;bottom:0;height:200px;background:linear-gradient(180deg,transparent,rgba(1,15,33,.85))"></div>
 <div class="a" style="left:90px;top:84px">{logo}</div>
 <div class="a" style="right:90px;top:96px;font-weight:900;font-size:20px;letter-spacing:4px;color:{G}">{i + 1:02d}/{N:02d}</div>
 <div class="a" style="{box};z-index:5">
  {f'<div style="font-weight:900;font-size:20px;letter-spacing:6px;color:{G};margin-bottom:22px">{kick}</div>' if kick else ''}
  <div style="font-weight:900;font-size:var(--fs,92px);line-height:.98;letter-spacing:-3px;text-transform:uppercase">{head}</div>
  <div style="font-weight:600;font-size:28px;line-height:1.42;color:#e3e9f4;margin-top:34px;max-width:560px;{'margin-left:auto;margin-right:auto;' if i == N - 1 else ''}">{sub}</div>{cta}
 </div>
 <div class="a" style="left:90px;bottom:70px;font-weight:600;font-size:20px;color:rgba(255,255,255,.75);z-index:6">@thedanagstudio</div>
 {f'<div class="a" style="right:90px;bottom:68px;font-weight:900;font-size:20px;letter-spacing:4px;color:{G};z-index:6">SWIPE &gt;&gt;</div>' if i < N - 1 else ''}
</div>'''
html = f"""<html><head><style>
@font-face{{font-family:M;font-weight:600;src:url({F}montserrat-latin-600-normal.woff2)}}
@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}} body{{width:{W}px;height:1350px;overflow:hidden;position:relative;font-family:M;color:#fff;background:#011631}} .a{{position:absolute}}
</style></head><body>{panels}
<svg class="a" style="left:0;top:0;z-index:4" width="{W}" height="1350" viewBox="0 0 {W} 1350"><polyline points="{pts}" fill="none" stroke="#FFC107" stroke-width="4" stroke-linecap="round"/><polyline points="{pts2}" fill="none" stroke="#E3A600" stroke-width="1.6" opacity=".8"/></svg>
<div class="a" style="inset:0;z-index:50;pointer-events:none;opacity:.14;mix-blend-mode:overlay;background-size:256px;background-image:url({R}/grain.png)"></div>
<script>document.fonts.ready.then(()=>document.body.dataset.done=1)</script></body></html>"""
tmp = '/tmp/_t05.html'; open(tmp, 'w').write(html)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page(viewport={'width': W, 'height': 1350}, device_scale_factor=2)
    pg.goto(pathlib.Path(tmp).as_uri()); pg.wait_for_selector('body[data-done]'); pg.wait_for_timeout(800)
    for i in range(N):
        pg.screenshot(path='/tmp/_t5.png', clip={'x': i * 1080, 'y': 0, 'width': 1080, 'height': 1350})
        im = Image.open('/tmp/_t5.png').convert('RGB'); im.save(f'{OUT}/{i + 1:02d}.jpg', quality=92, subsampling=0)
        im.resize((1080, 1350), Image.LANCZOS).save(f'{OUT}/{i + 1:02d}-1080.jpg', quality=92)
    b.close()
print('ok', N)
