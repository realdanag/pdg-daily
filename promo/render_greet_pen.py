"""Daily greeting, 'hero object' style (guide: ArmsGrafix pen flyer, 2026-11-14).
Navy gradient, big 3D crown cropped at the right, script line + huge gold-gradient headline, message in a gold loop,
translucent services box, white footer band with contacts. No glow on navy.
Usage: python3 promo/render_greet_pen.py OUT_BASENAME "Script" "Headline" "KICKER" "message"
"""
import sys, os, re, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image
P = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(P); B = f'{R}/book-flyer'
sys.path.insert(0, B)
import render_book as rb
from contacts import IC
out, script, head, kick, msg = sys.argv[1:6]
import datetime as _dt
_d = _dt.date.fromisoformat(sys.argv[6]) if len(sys.argv) > 6 else _dt.date.today()
DAY = _d.strftime('%d'); WD = _d.strftime('%A').upper(); MON = _d.strftime('%B').upper()
F = f'{R}/fonts/'; GOLD = '#FFC107'
import os as _os
CROWN = pathlib.Path(_os.environ.get('OBJ', '/home/claude/assets/crown-cut.png')).as_uri()
OBJST = _os.environ.get('OBJSTYLE', 'right:-270px;top:190px;width:680px;transform:rotate(14deg)')
logo = re.sub(r'<\?xml[^>]*>', '', open(f'{B}/logo-on-navy.svg').read()).replace('<svg', '<svg style="height:58px;width:auto;display:block"', 1)
ic = lambda k, c, s=22: f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" style="color:{c};flex:none">{IC[k]}</svg>'
circ = lambda k: f'<span style="width:34px;height:34px;border-radius:50%;background:#022452;display:inline-flex;align-items:center;justify-content:center">{ic(k, CI, 18)}</span>'
CI = '#022452' if __import__('os').environ.get('THEME') == 'white' else '#fff'
cols = [['Flyer &amp; Poster Design', 'Business Card Design', 'Brochure Design'],
        ['Product Visuals', 'Social Media Design', 'Social Media Mgt.'],
        ['Website Design', 'Website Redesign', 'And more']]
svc = ''.join('<div>' + ''.join(f'<div style="display:flex;align-items:center;gap:12px;padding:9px 0"><span style="width:13px;height:13px;border-radius:50%;border:3px solid {GOLD};flex:none"></span>{t}</div>' for t in c) + '</div>' for c in cols)
html = f"""<html><head><style>
@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}
@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}
@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
@font-face{{font-family:SC;src:url({F}sacramento-latin-400-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;color:#fff;
 background:linear-gradient(160deg,#032F65 0%,#022452 40%,#011631 78%,#010F21 100%)}}
.a{{position:absolute}}
.g{{background:linear-gradient(180deg,#FFF1C4 0%,#FFD54F 38%,#FFC107 62%,#C98F00 100%);-webkit-background-clip:text;background-clip:text;color:transparent;padding-right:.04em}}
</style></head><body>
<svg class="a" viewBox="252 255 749 664" style="left:-260px;top:520px;width:720px;opacity:.04"><path fill="#fff" fill-rule="evenodd" d="{rb.MK['nodot']}"/><path fill="#fff" d="{rb.MK['dot']}"/></svg>
<img class="a" src="{CROWN}" style="{OBJST};filter:drop-shadow(0 40px 60px rgba(0,0,0,.55))">
<div class="a" style="left:90px;top:84px">{logo}</div>
<div class="a" style="right:90px;top:84px;display:flex;align-items:center;gap:20px;z-index:5">
 <div style="font-weight:900;font-size:96px;line-height:.78;color:{GOLD};letter-spacing:-3px">{DAY}</div>
 <div style="width:3px;height:72px;background:{GOLD}"></div>
 <div style="font-weight:700;font-size:20px;letter-spacing:6px;line-height:1.55">{WD}<span style="display:block;font-weight:900;font-size:32px;letter-spacing:4px;line-height:1.1;margin-top:4px;color:{GOLD}">{MON}</span></div>
</div>
<div class="a" style="left:90px;top:330px">
  <div style="font-weight:500;font-size:68px;line-height:1;letter-spacing:-1px;color:#fff;margin-top:0">{script}</div>
 <div id="h" style="font-weight:900;font-size:176px;line-height:.95;letter-spacing:-7px;margin-top:8px;white-space:nowrap"><span class="g">{head}</span><span style="display:inline-block;width:.236em;height:.236em;border-radius:50%;background:#fff;margin-left:.02em"></span></div>
 <div style="position:relative;width:600px;height:170px;margin-top:30px">
  <svg class="a" viewBox="0 0 560 150" preserveAspectRatio="none" style="inset:0"><path d="M30 118 C-10 70 40 22 230 14 C430 6 548 40 540 82 C532 124 400 140 250 140 C130 140 40 128 8 104" fill="none" stroke="{GOLD}" stroke-width="3.5" stroke-linecap="round"/><path d="M8 104 C0 118 -6 132 16 146" fill="none" stroke="{GOLD}" stroke-width="3.5" stroke-linecap="round"/></svg>
  <div class="a" style="left:74px;right:56px;top:58px;font-weight:700;font-size:23px;line-height:1.38">{msg}</div>
 </div>
</div>
<div class="a" style="left:90px;right:90px;top:860px;border:2px solid rgba(255,193,7,.55);border-radius:28px;background:linear-gradient(180deg,rgba(255,193,7,.16),rgba(255,193,7,.07));padding:30px 34px;display:grid;grid-template-columns:1.15fr 1fr 1fr;gap:10px;font-weight:500;font-size:22px">{svc}</div>
<div class="a" style="left:0;right:0;bottom:0;height:180px;background:#fff;color:#022452;display:flex;align-items:center;justify-content:space-between;padding:0 90px">
 <div><div style="display:flex;align-items:center;gap:8px;font-weight:700;font-size:20px">{circ('IG')}{circ('TT')}{circ('X')}<span style="margin-left:6px">@thedanagstudio</span></div>
  <div style="display:flex;align-items:center;gap:12px;margin-top:12px"><span style="width:46px;height:46px;border-radius:50%;background:{GOLD};display:inline-flex;align-items:center;justify-content:center">{ic('PH', '#022452', 24)}</span><span style="font-weight:900;font-size:44px;letter-spacing:-1px">+233 (0)50 332 0548</span></div></div>
 <div style="text-align:right;font-family:SC;font-size:52px;line-height:1;color:#022452">Crowned in Craft<div style="font-family:M;font-weight:500;font-size:17px;color:#4d5870;margin-top:10px">Premium designs that get you noticed.</div></div>
</div>
<div class="a" style="inset:0;z-index:50;pointer-events:none;opacity:.16;mix-blend-mode:overlay;background-size:256px;background-image:url({R}/grain.png)"></div>
<script>document.fonts.ready.then(()=>{{const h=document.getElementById('h');let f=176;while(h.scrollWidth>640&&f>90){{f-=2;h.style.fontSize=f+'px'}}document.body.dataset.done=1}})</script>
</body></html>"""
import os
if os.environ.get('THEME') == 'white':
    wl = re.sub(r'<\?xml[^>]*>', '', open(f'{B}/logo-on-white.svg').read()).replace('<svg', '<svg style="height:58px;width:auto;display:block"', 1) if os.path.exists(f'{B}/logo-on-white.svg') else logo
    html = html.replace(logo, wl)
    html = html.replace('background:linear-gradient(160deg,#032F65 0%,#022452 40%,#011631 78%,#010F21 100%)',
        'background:radial-gradient(900px 700px at 0% 0%,rgba(255,193,7,.20),transparent 60%),linear-gradient(160deg,#ffffff 0%,#f6f7fa 55%,#eceef3 100%)')
    html = html.replace('font-family:M;color:#fff;', 'font-family:M;color:#022452;', 1)
    html = html.replace('letter-spacing:-1px;color:#fff;margin-top:0', 'letter-spacing:-1px;color:#022452;margin-top:0')
    html = html.replace('border-radius:50%;background:#fff;margin-left:.02em', 'border-radius:50%;background:#022452;margin-left:.02em')
    html = html.replace('<path fill="#fff" fill-rule="evenodd"', '<path fill="#022452" fill-rule="evenodd"').replace('<path fill="#fff" d=', '<path fill="#022452" d=')
    html = html.replace('background:linear-gradient(180deg,rgba(255,193,7,.16),rgba(255,193,7,.07))', 'background:#fff;box-shadow:0 18px 40px rgba(2,36,82,.10)')
    html = html.replace('.g{background:linear-gradient(180deg,#FFF1C4 0%,#FFD54F 38%,#FFC107 62%,#C98F00 100%)', '.g{background:linear-gradient(180deg,#FFD54F 0%,#FFC107 45%,#C98F00 100%)')
    # footer band becomes navy
    html = html.replace('height:180px;background:#fff;color:#022452', 'height:180px;background:linear-gradient(160deg,#032F65,#011631);color:#fff')
    html = html.replace('background:#022452;display:inline-flex', 'background:#fff;display:inline-flex').replace('{ic(k, "#fff", 18)}', '')
    html = html.replace('font-family:SC;font-size:52px;line-height:1;color:#022452', 'font-family:SC;font-size:52px;line-height:1;color:#FFC107').replace('color:#4d5870', 'color:#c9d3e6')
tmp = '/tmp/_pen.html'; open(tmp, 'w').write(html)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
    pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
    pg.goto(pathlib.Path(tmp).as_uri()); pg.wait_for_selector('body[data-done]'); pg.wait_for_timeout(400)
    pg.screenshot(path='/tmp/_pen.png'); b.close()
im = Image.open('/tmp/_pen.png').convert('RGB')
im.save(out + '.jpg', quality=97, subsampling=0)
im.resize((1080, 1350), Image.LANCZOS).save(out + '-tiktok.jpg', quality=97, subsampling=0)
print('ok', out)
