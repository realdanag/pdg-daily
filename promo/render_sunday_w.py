"""Happy Sunday, white portrait style (guide: Danag's sample 22 Nov 2026, references/sunday/03.jpg): 'HAPPY' gold speech tag,
stacked SUN / DAY, gold swoosh, message, LOVE/JOY/PEACE navy card on the left edge, portrait cut-out right with gold arcs,
navy 'Get in touch' contact bar. White only.
Usage: python3 promo/render_sunday_w.py OUT YYYY-MM-DD "message" [portrait.png]
"""
import sys, os, re, math, pathlib, datetime as dt
from playwright.sync_api import sync_playwright
from PIL import Image
P = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(P); B = f'{R}/book-flyer'
sys.path.insert(0, B)
import render_book as rb
from contacts import IC
out, ds, msg = sys.argv[1:4]
PORT = pathlib.Path(sys.argv[4] if len(sys.argv) > 4 else f'{R}/assets-hero/S1-cut.png').resolve().as_uri()
d = dt.date.fromisoformat(ds)
F = f'{R}/fonts/'; G = '#FFC107'; G2 = '#F2A900'; N = '#022452'; SUB = '#3a4d6e'
logo = re.sub(r'<\?xml[^>]*>', '', open(f'{B}/logo-on-white.svg').read()).replace('<svg', '<svg style="height:58px;width:auto;display:block"', 1)
ic = lambda k, c, s=18: f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" style="color:{c};flex:none">{IC[k]}</svg>'
circ = lambda k, bg, fg, s=34: f'<span style="width:{s}px;height:{s}px;border-radius:50%;background:{bg};display:inline-flex;align-items:center;justify-content:center">{ic(k, fg, int(s*.5))}</span>'
# faint wavy line texture
waves = ''.join(
    f'<path d="M-50 {y} ' + ' '.join(f'Q {x+60} {y + 26*math.sin(i*.7+x/180):.0f} {x+120} {y}' for x in range(-50, 1150, 120)) + '" />'
    for i, y in enumerate(range(40, 1350, 34)))
html = f"""<html><head><style>
@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}
@font-face{{font-family:M;font-weight:600;src:url({F}montserrat-latin-600-normal.woff2)}}
@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}
@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;color:{N};background:#ffffff}}
.a{{position:absolute}}
</style></head><body>
<svg class="a" width="1080" height="1350" style="left:0;top:0" fill="none" stroke="{N}" stroke-opacity=".035" stroke-width="1.4">{waves}</svg>
<svg class="a" width="1080" height="1350" style="left:0;top:0" fill="none">
 <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{G}"/><stop offset="1" stop-color="{G2}"/></linearGradient></defs>
 <path d="M 600 470 A 330 330 0 0 1 1100 380" stroke="url(#g)" stroke-width="42" stroke-linecap="round"/>
 <path d="M 640 1180 A 300 300 0 0 1 1120 860" stroke="url(#g)" stroke-width="42" stroke-linecap="round"/>
</svg>
<img class="a" src="{PORT}" style="left:400px;bottom:0;height:1000px;filter:drop-shadow(0 24px 40px rgba(2,36,82,.22))">
<div class="a" style="left:90px;top:84px">{logo}</div>
<div class="a" style="right:90px;top:84px;display:flex;align-items:center;gap:18px">
 <div style="font-weight:900;font-size:88px;line-height:.78;color:{G};letter-spacing:-3px">{d.strftime('%d')}</div>
 <div style="width:3px;height:66px;background:{G}"></div>
 <div style="font-weight:700;font-size:19px;letter-spacing:6px;line-height:1.55">{d.strftime('%A').upper()}<span style="display:block;font-weight:900;font-size:30px;letter-spacing:4px;line-height:1.1;margin-top:4px;color:{G}">{d.strftime('%B').upper()}</span></div>
</div>
<div class="a" style="left:90px;top:282px;background:{G};color:{N};font-weight:900;font-size:46px;letter-spacing:1px;padding:8px 26px;border-radius:12px;line-height:1.1">HAPPY
 <span style="position:absolute;left:34px;bottom:-16px;width:0;height:0;border-left:0 solid transparent;border-right:24px solid transparent;border-top:18px solid {G}"></span></div>
<div class="a" style="left:84px;top:370px;font-weight:900;font-size:212px;line-height:.9;letter-spacing:-8px">SUN<br>DAY</div>
<svg class="a" viewBox="0 0 300 30" style="left:96px;top:772px;width:300px;height:30px"><path d="M4 22 Q 150 -6 296 14" stroke="{G}" stroke-width="9" fill="none" stroke-linecap="round"/></svg>
<div class="a" style="left:90px;top:826px;width:470px;display:flex;gap:20px"><div style="width:4px;background:{G};flex:none"></div><div style="font-weight:500;font-size:24px;line-height:1.42;color:{SUB}">{msg}</div></div>
<div class="a" style="left:0;top:1000px;width:300px;padding:26px 0 26px 90px;border-radius:0 22px 22px 0;background:linear-gradient(135deg,#033A7A 0%,{N} 55%,#011631 100%);color:#fff;font-weight:900;font-size:34px;line-height:1.22;letter-spacing:1px;box-shadow:0 18px 40px rgba(2,36,82,.25)">LOVE<br><span style="color:{G}">JOY</span><br>PEACE</div>
<div class="a" style="left:60px;right:60px;bottom:40px;height:118px;border-radius:20px;border:3px solid {G};background:linear-gradient(135deg,#033A7A 0%,{N} 50%,#011631 100%);display:flex;align-items:center;padding:0 28px;justify-content:space-between;white-space:nowrap;color:#fff;box-shadow:0 18px 40px rgba(2,36,82,.28)">
 <div style="font-weight:900;font-size:27px;line-height:1">Get in touch<svg viewBox="0 0 170 14" style="display:block;width:170px;height:14px;margin-top:6px"><path d="M3 10 Q 85 -2 167 7" stroke="{G}" stroke-width="5" fill="none" stroke-linecap="round"/></svg></div>
 <div style="width:2px;height:64px;background:rgba(255,255,255,.25)"></div>
 <div><div style="font-weight:700;font-size:16px;color:{G};letter-spacing:1px">CALL / WHATSAPP</div><div style="display:flex;align-items:center;gap:8px;font-weight:900;font-size:23px;margin-top:4px">{circ('PH', G, N, 30)}+233 (0)50 332 0548</div></div>
 <div style="width:2px;height:64px;background:rgba(255,255,255,.25)"></div>
 <div style="font-weight:700;font-size:15px;line-height:1.3">Flyers &amp; Posters<br>Social Media<br>Websites etc.</div>
 <div style="width:2px;height:64px;background:rgba(255,255,255,.25)"></div>
 <div><div style="display:flex;gap:6px">{circ('IG', 'rgba(255,255,255,.14)', '#fff', 30)}{circ('TT', 'rgba(255,255,255,.14)', '#fff', 30)}{circ('X', 'rgba(255,255,255,.14)', '#fff', 30)}</div><div style="font-weight:700;font-size:17px;margin-top:6px">@thedanagstudio</div></div>
</div>
<script>document.fonts.ready.then(()=>document.body.dataset.done=1)</script></body></html>"""
tmp = '/tmp/_sunw.html'; open(tmp, 'w').write(html)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
    pg.goto(pathlib.Path(tmp).as_uri()); pg.wait_for_selector('body[data-done]'); pg.wait_for_timeout(400)
    pg.screenshot(path='/tmp/_sunw.png'); b.close()
im = Image.open('/tmp/_sunw.png').convert('RGB')
im.save(out + '.jpg', quality=93, subsampling=0); im.resize((1080, 1350), Image.LANCZOS).save(out + '-1080.jpg', quality=93)
print('ok', out)
