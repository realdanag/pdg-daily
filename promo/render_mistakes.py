"""Design Tip 07: '5 design mistakes costing you customers' (guide: Techvint white numbered carousel, 2026-11-14). White, gold glow top-left.
Usage: python3 promo/render_mistakes.py OUTDIR
"""
import sys, os, re, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image
P = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(P); B = f'{R}/book-flyer'
sys.path.insert(0, B)
import render_book as rb
OUT = os.path.abspath(sys.argv[1]); os.makedirs(OUT, exist_ok=True)
F = f'{R}/fonts/'; G = '#FFC107'; N = '#022452'
logo = re.sub(r'<\?xml[^>]*>', '', open(f'{B}/logo-on-white.svg').read()).replace('<svg', '<svg style="height:52px;width:auto;display:block"', 1)
DOT = f'<span style="display:inline-block;width:.236em;height:.236em;border-radius:50%;background:{G};margin-left:.04em"></span>'
CSS = f"""@font-face{{font-family:M;font-weight:400;src:url({F}montserrat-latin-400-normal.woff2)}}
@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}
@font-face{{font-family:M;font-weight:600;src:url({F}montserrat-latin-600-normal.woff2)}}
@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}
@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;color:{N};
 background:#ffffff}}
.a{{position:absolute}}
.gn{{background:linear-gradient(90deg,#022452 0%,#2a4d82 100%);-webkit-background-clip:text;background-clip:text;color:transparent}}
.gg{{background:linear-gradient(90deg,#C98F00 0%,#FFC107 100%);-webkit-background-clip:text;background-clip:text;color:transparent;padding-right:.03em}}
.num{{font-weight:400;font-size:230px;line-height:.8;letter-spacing:-12px}}
svg.d *{{fill:none;stroke:{N};stroke-width:5;stroke-linecap:round;stroke-linejoin:round}} svg.d .y{{stroke:{G}}} svg.d .f{{fill:{G};stroke:none}}"""
MARK = f'<svg class="a" viewBox="252 255 749 664" style="right:-220px;top:380px;width:640px;opacity:.022"><path fill="{N}" fill-rule="evenodd" d="{rb.MK["nodot"]}"/><path fill="{N}" d="{rb.MK["dot"]}"/></svg>'
GRAIN = f'<div class="a" style="inset:0;z-index:50;pointer-events:none;opacity:0;mix-blend-mode:multiply;background-size:256px;background-image:url({R}/grain.png)"></div>'
def page(body, swipe=True):
    foot = f'<div class="a" style="left:90px;bottom:84px;font-weight:700;font-size:24px">@thedanagstudio</div>'
    if swipe: foot += f'<div class="a" style="right:90px;bottom:84px;font-weight:900;font-size:20px;letter-spacing:4px;color:#C98F00">SWIPE &gt;&gt;</div>'
    return f'<html><head><style>{CSS}</style></head><body>{MARK}<div class="a" style="left:90px;top:80px">{logo}</div>{body}{foot}{GRAIN}<script>document.fonts.ready.then(()=>document.body.dataset.done=1)</script></body></html>'

D = {  # 420x420 line doodles
 'text': '''<rect x="70" y="40" width="230" height="300" rx="14"/>''' + ''.join(f'<path d="M100 {y} H{270 - (y % 3) * 20}"/>' for y in range(85, 300, 26)) +
         '''<circle class="y" cx="290" cy="270" r="62"/><path class="y" d="M334 314 L392 372"/><path d="M262 250 q8-20 26-22"/>''',
 'cta': '''<rect x="40" y="250" width="250" height="90" rx="45"/><path d="M90 296 H230"/><path class="y" d="M300 60 q60 40 40 130 q-6 30-40 52"/><path class="y" d="M282 222 l18 22 l24-14"/>
           <path d="M330 300 l40-16 M332 330 l44 6 M318 270 l28-34"/>''',
 'photo': '''<rect x="50" y="60" width="300" height="240" rx="12"/><path d="M70 270 L160 170 L220 230 L260 195 L330 270"/><circle class="y" cx="280" cy="120" r="24"/>
           <path class="y" d="M60 330 q20-14 40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0"/><path d="M110 120 q10 6 0 14 q-10 8 0 14 M140 110 q10 6 0 14 q-10 8 0 14"/>''',
 'mix': '''<rect x="40" y="90" width="150" height="120" rx="8" transform="rotate(-10 115 150)"/><rect x="210" y="50" width="140" height="170" rx="8" transform="rotate(8 280 135)"/>
           <rect x="90" y="230" width="170" height="110" rx="8" transform="rotate(4 175 285)"/><circle class="f" cx="300" cy="300" r="34"/><path class="y" d="M70 130 h60 M240 90 l60 50"/>
           <path d="M120 270 h90 M120 300 h60"/>''',
 'self': '''<circle cx="120" cy="110" r="38"/><path d="M60 330 v-90 q0-60 60-60 q60 0 60 60 v90"/><path class="y" d="M190 170 l70-40 v120 l-70-40 z"/><path class="y" d="M286 160 q20 30 0 60 M310 140 q34 50 0 100"/>
           <circle cx="300" cy="300" r="20"/><circle cx="360" cy="300" r="20"/><path d="M276 360 q24-30 48 0 M336 360 q24-30 48 0"/>''',
}
def doodle(k): return f'<svg class="a d" viewBox="0 0 420 420" style="right:70px;bottom:150px;width:440px;height:440px">{D[k]}</svg>'
ITEMS = [
 ('Too much', 'text', 'Nobody reads a paragraph on a flyer. Say less and say it bigger.', 'text'),
 ('No clear', 'next step', "If people don't know what to do next, they do nothing. Tell them to call, book or buy.", 'cta'),
 ('Blurry', 'photos', 'A great business looks cheap with poor pictures. Your visuals speak before you do.', 'photo'),
 ('A new look', 'every week', 'New colours and fonts every post make you forgettable. Pick a style and own it.', 'mix'),
 ('Designing', 'for yourself', "Your customer's taste matters more than yours. Design for the person you want to reach.", 'self'),
]
slides = [page(f'''<div class="a" style="left:90px;top:300px;font-weight:700;font-size:20px;letter-spacing:6px;color:#C98F00">DESIGN TIP 07</div>
<div class="a" style="left:78px;top:360px"><span class="num gg" style="font-weight:900;font-size:470px;letter-spacing:-20px">5</span></div>
<div class="a" style="left:400px;top:400px;font-weight:900;font-size:118px;line-height:.98;letter-spacing:-4px"><span class="gn">Design</span><br><span class="gn">mistakes</span></div>
<div class="a" style="left:404px;top:650px;font-weight:700;font-size:54px;line-height:1.08;letter-spacing:-1.5px"><span class="gg">that are costing<br>you customers</span>{DOT}</div>
<div class="a" style="left:92px;top:930px;width:880px;font-weight:600;font-size:32px;line-height:1.4;color:#2a3f63">Fix these five and your designs will start doing their job: getting people to stop, read and buy.</div>''')]
for i, (a, b, t, k) in enumerate(ITEMS, 1):
    slides.append(page(f'''<div class="a" style="left:84px;top:250px"><span class="num gn">0{i}</span></div>
<div class="a" style="left:90px;top:480px;right:90px"><div style="font-weight:900;font-size:92px;line-height:1;letter-spacing:-3.5px;text-transform:uppercase"><span class="gn">{a}</span><br><span class="gg">{b}</span>{DOT}</div>
<div style="width:480px;margin-top:40px;font-weight:600;font-size:31px;line-height:1.38;color:#2a3f63">{t}</div></div>{doodle(k)}'''))
slides.append(page(f'''<div class="a" style="left:90px;top:480px;right:90px">
 <div style="font-weight:900;font-size:96px;line-height:1.02;letter-spacing:-3px"><span class="gn">Fix these and</span><br><span class="gg">watch people stop</span>{DOT}</div>
 <div style="font-weight:600;font-size:30px;line-height:1.5;margin-top:44px;color:#2a3f63">Save this and share it with a business owner who needs it.</div>
 <div style="display:inline-block;margin-top:50px;background:linear-gradient(160deg,#032F65,#011631);color:#fff;border-radius:60px;padding:24px 44px;font-weight:900;font-size:34px">Book a design: <span style="color:{G}">+233 (0)50 332 0548</span></div></div>''', swipe=False))
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
    for i, h in enumerate(slides, 1):
        t = f'/tmp/_mis{i}.html'; open(t, 'w').write(h)
        pg.goto(pathlib.Path(t).as_uri()); pg.wait_for_selector('body[data-done]'); pg.wait_for_timeout(250)
        pg.screenshot(path='/tmp/_m.png')
        im = Image.open('/tmp/_m.png').convert('RGB'); im.save(f'{OUT}/{i:02d}.jpg', quality=93, subsampling=0)
        im.resize((1080, 1350), Image.LANCZOS).save(f'{OUT}/{i:02d}-1080.jpg', quality=93)
    b.close()
print('ok', len(slides))
