"""Hero-object promo: hanging gold phone, "Hey you, let's get in touch." (guide: Uplix Orbit, 2026-11-14). Navy, no glow.
Usage: python3 promo/render_phone.py OUT_BASENAME [photo]
"""
import sys, os, re, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image
P = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(P); B = f'{R}/book-flyer'
sys.path.insert(0, B)
import render_book as rb
from contacts import IC
out = sys.argv[1]
PHOTO = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else '/home/claude/assets/phone-nb.jpg').as_uri()
F = f'{R}/fonts/'; GOLD = '#FFC107'
logo = re.sub(r'<\?xml[^>]*>', '', open(f'{B}/logo-on-navy.svg').read()).replace('<svg', '<svg style="height:58px;width:auto;display:block"', 1)
ic = lambda k, c, s=22: f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" style="color:{c};flex:none">{IC[k]}</svg>'
circ = lambda k: f'<span style="width:34px;height:34px;border-radius:50%;border:1.5px solid rgba(255,193,7,.7);display:inline-flex;align-items:center;justify-content:center">{ic(k, GOLD, 17)}</span>'
dot = '<span style="display:inline-block;width:.236em;height:.236em;border-radius:50%;background:#FFC107;margin-left:.04em"></span>'
html = f"""<html><head><style>
@font-face{{font-family:M;font-weight:400;src:url({F}montserrat-latin-400-normal.woff2)}}
@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}
@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}
@font-face{{font-family:M;font-weight:600;src:url({F}montserrat-latin-600-normal.woff2)}}
@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
@font-face{{font-family:SC;src:url({F}sacramento-latin-400-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;color:#fff;background:#011631}}
.a{{position:absolute}} .g{{color:{GOLD}}}
</style></head><body>
<div class="a" style="inset:0;background:url({PHOTO}) center 38%/cover"></div>
<div class="a" style="inset:0;background:radial-gradient(520px 640px at 50% 40%,transparent 0%,rgba(1,15,33,.35) 70%),linear-gradient(180deg,rgba(1,22,49,.55) 0%,rgba(1,22,49,0) 22%,rgba(1,22,49,0) 55%,rgba(1,15,33,.92) 82%,#010F21 100%)"></div>
<svg class="a" viewBox="252 255 749 664" style="right:-220px;bottom:-60px;width:640px;opacity:.025"><path fill="#fff" fill-rule="evenodd" d="{rb.MK['nodot']}"/><path fill="#fff" d="{rb.MK['dot']}"/></svg>
<div class="a" style="left:90px;top:84px">{logo}</div>
<div class="a" style="right:90px;top:92px;font-weight:700;font-size:16px;letter-spacing:6px;color:rgba(255,255,255,.75)">CROWNED IN CRAFT</div>
<div class="a" style="right:632px;top:560px;text-align:right;font-size:70px;line-height:1;letter-spacing:-2px;white-space:nowrap"><b class="g" style="font-weight:900">Hey</b> <span style="font-weight:500;font-style:italic">you,</span></div>
<div class="a" style="left:648px;top:560px;font-size:70px;line-height:1.02;letter-spacing:-2px;font-weight:500;white-space:nowrap">let's <b class="g" style="font-weight:900">get</b><br>in touch{dot}</div>
<div class="a" style="left:0;right:0;top:1000px;text-align:center;font-size:40px;line-height:1.28;font-weight:500;letter-spacing:-.5px">Let's design what your<br><b class="g" style="font-weight:900">brand</b> <b style="font-weight:900">says</b> <b class="g" style="font-weight:900">next</b>.</div>
<div class="a" style="left:90px;right:90px;top:1170px;height:1px;background:linear-gradient(90deg,transparent,rgba(255,193,7,.6),transparent)"></div>
<div class="a" style="left:90px;right:90px;top:1206px;display:flex;align-items:center;justify-content:center;gap:34px;font-weight:600;font-size:21px;color:#e8ecf4">
 <div style="display:flex;align-items:center;gap:10px">{circ('PH')}+233 (0)50 332 0548</div>
 <div style="width:1.5px;height:30px;background:rgba(255,255,255,.35)"></div>
 <div style="display:flex;align-items:center;gap:8px">{circ('IG')}{circ('TT')}{circ('X')}<span style="margin-left:4px">@thedanagstudio</span></div>
</div>
<div class="a" style="inset:0;z-index:50;pointer-events:none;opacity:.16;mix-blend-mode:overlay;background-size:256px;background-image:url({R}/grain.png)"></div>
<script>document.fonts.ready.then(()=>document.body.dataset.done=1)</script>
</body></html>"""
tmp = '/tmp/_phone.html'; open(tmp, 'w').write(html)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
    pg.goto(pathlib.Path(tmp).as_uri()); pg.wait_for_selector('body[data-done]'); pg.wait_for_timeout(400)
    pg.screenshot(path='/tmp/_phone.png'); b.close()
im = Image.open('/tmp/_phone.png').convert('RGB')
im.save(out + '.jpg', quality=95, subsampling=0)
im.resize((1080, 1350), Image.LANCZOS).save(out + '-1080.jpg', quality=95, subsampling=0)
print('ok', out)
