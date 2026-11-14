"""Daily greeting v2 (week of 16 Nov 2026). Giant outlined weekday behind, 'Happy' + weekday with a gold highlight box
(guide: KD 'Count.' box, Techvint big type), message with gold rule, service chips, contact strip. Navy (no glow) or white.
Usage: python3 promo/render_daily2.py OUT theme YYYY-MM-DD "Word" "BoxPart" "message"
   e.g. ... navy 2026-11-15 "Sun" "day" "Rest, reset ..."
"""
import sys, os, re, pathlib, datetime as dt
from playwright.sync_api import sync_playwright
from PIL import Image
P = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(P); B = f'{R}/book-flyer'
sys.path.insert(0, B)
import render_book as rb
from contacts import IC
out, theme, ds, w1, w2, msg = sys.argv[1:7]
d = dt.date.fromisoformat(ds); navy = theme == 'navy'
F = f'{R}/fonts/'; G = '#FFC107'; N = '#022452'; TX = '#fff' if navy else N; SUB = '#dfe5f1' if navy else '#3a4d6e'
logo = re.sub(r'<\?xml[^>]*>', '', open(f'{B}/logo-on-{"navy" if navy else "white"}.svg').read()).replace('<svg', '<svg style="height:58px;width:auto;display:block"', 1)
ic = lambda k, c, s=18: f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" style="color:{c};flex:none">{IC[k]}</svg>'
circ = lambda k: f'<span style="width:36px;height:36px;border-radius:50%;background:{G if k=="PH" else ("rgba(255,255,255,.12)" if navy else N)};display:inline-flex;align-items:center;justify-content:center">{ic(k, N if k=="PH" else "#fff")}</span>'
chips = ''.join(f'<span style="border:1.5px solid {"rgba(255,193,7,.6)" if navy else "rgba(2,36,82,.25)"};border-radius:40px;padding:12px 22px;font-weight:600;font-size:22px">{t}</span>'
                for t in ['Flyers &amp; Posters', 'Product Visuals', 'Social Media', 'Websites'])
bg = ('linear-gradient(160deg,#032F65 0%,#022452 40%,#011631 78%,#010F21 100%)' if navy else
      '#ffffff')
WD = d.strftime('%A').upper()
html = f"""<html><head><style>
@font-face{{font-family:M;font-weight:400;src:url({F}montserrat-latin-400-normal.woff2)}}
@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}
@font-face{{font-family:M;font-weight:600;src:url({F}montserrat-latin-600-normal.woff2)}}
@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}
@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;color:{TX};background:{bg}}}
.a{{position:absolute}}
</style></head><body>
<div class="a" style="left:-30px;top:690px;width:1140px;font-weight:900;font-size:300px;line-height:1;letter-spacing:-10px;white-space:nowrap;color:transparent;-webkit-text-stroke:2px {"rgba(255,255,255,.07)" if navy else "rgba(2,36,82,.07)"}" id="ghost">{WD}</div>
<svg class="a" viewBox="252 255 749 664" style="right:-200px;top:120px;width:560px;opacity:{.035 if navy else .022}"><path fill="{"#fff" if navy else N}" fill-rule="evenodd" d="{rb.MK['nodot']}"/><path fill="{"#fff" if navy else N}" d="{rb.MK['dot']}"/></svg>
<div class="a" style="left:90px;top:84px">{logo}</div>
<div class="a" style="right:90px;top:84px;display:flex;align-items:center;gap:20px">
 <div style="font-weight:900;font-size:96px;line-height:.78;color:{G};letter-spacing:-3px">{d.strftime('%d')}</div>
 <div style="width:3px;height:72px;background:{G}"></div>
 <div style="font-weight:700;font-size:20px;letter-spacing:6px;line-height:1.55">{WD}<span style="display:block;font-weight:900;font-size:32px;letter-spacing:4px;line-height:1.1;margin-top:4px;color:{G}">{d.strftime('%B').upper()}</span></div>
</div>
<div class="a" style="left:90px;right:90px;top:330px">
 <div style="font-weight:500;font-size:84px;line-height:1;letter-spacing:-2px">Happy</div>
 <div id="h" style="font-weight:900;font-size:190px;line-height:1;letter-spacing:-8px;margin-top:6px;white-space:nowrap">{w1}<span style="display:inline-block;background:{G};color:{N};padding:0 .1em 0 .06em;margin-left:.04em;border-radius:.06em;line-height:1.08">{w2}<span style="display:inline-block;width:.236em;height:.236em;border-radius:50%;background:{N};margin-left:.03em"></span></span></div>
 <div style="display:flex;gap:26px;margin-top:56px;max-width:760px"><div style="width:4px;background:{G};flex:none"></div><div style="font-weight:500;font-size:34px;line-height:1.42;color:{SUB}">{msg}</div></div>
</div>
<div class="a" style="left:90px;right:90px;top:1010px;display:flex;flex-wrap:wrap;gap:14px">{chips}</div>
<div class="a" style="left:90px;right:90px;bottom:80px;padding-top:30px;border-top:1px solid {"rgba(255,255,255,.18)" if navy else "rgba(2,36,82,.15)"};display:flex;align-items:center;justify-content:space-between;font-weight:700;font-size:23px">
 <div style="display:flex;align-items:center;gap:12px">{circ('PH')}<span style="font-weight:900;font-size:30px">+233 (0)50 332 0548</span></div>
 <div style="display:flex;align-items:center;gap:8px">{circ('IG')}{circ('TT')}{circ('X')}<span style="margin-left:4px">@thedanagstudio</span></div>
</div>
<div class="a" style="inset:0;z-index:50;pointer-events:none;opacity:{.16 if navy else 0};mix-blend-mode:{"overlay" if navy else "multiply"};background-size:256px;background-image:url({R}/grain.png)"></div>
<script>document.fonts.ready.then(()=>{{const h=document.getElementById('h');let f=190;while(h.scrollWidth>900&&f>100){{f-=4;h.style.fontSize=f+'px'}}document.body.dataset.done=1}})</script></body></html>"""
tmp = '/tmp/_d2.html'; open(tmp, 'w').write(html)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
    pg.goto(pathlib.Path(tmp).as_uri()); pg.wait_for_selector('body[data-done]'); pg.wait_for_timeout(300)
    pg.screenshot(path='/tmp/_d2.png'); b.close()
im = Image.open('/tmp/_d2.png').convert('RGB')
im.save(out + '.jpg', quality=93, subsampling=0); im.resize((1080, 1350), Image.LANCZOS).save(out + '-1080.jpg', quality=93)
print('ok', out)
