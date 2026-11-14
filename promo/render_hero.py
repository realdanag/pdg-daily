"""Hero-object promos (guides: 2026-11-14b refs). One gold object, two-tone Montserrat headline, contact strip.
Usage: python3 promo/render_hero.py KEY PHOTO OUT_BASENAME     KEY in P1..P6
"""
import sys, os, re, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image
P = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(P); B = f'{R}/book-flyer'
sys.path.insert(0, B)
import render_book as rb
from contacts import IC
key, photo, out = sys.argv[1:4]
F = f'{R}/fonts/'; G = '#FFC107'; N = '#022452'
CFG = {
 'P1': dict(theme='navy', pos='top', pic='center 70%',
   head='Make every<br>move <span class="box">count</span>', sub='Bold, intentional designs that keep your business a step ahead.'),
 'P2': dict(theme='white', pos='left', pic='70% center', size=118,
   head='Be the<br>brand<br><span class="g">that<br>stands</span><br>in the<br>light', sub='Designs that put your business where everyone can see it.'),
 'P3': dict(theme='navy', pos='top', pic='center 75%',
   head='Complete<br>your <span class="g">brand</span>', sub='DANAG STUDIO is the missing piece between you and designs that sell.'),
 'P4': dict(theme='white', pos='topc', pic='center 80%', size=78,
   head='Good <span class="box">design</span> is what<br>separates you from<br>everyone else', sub='Flyers, product visuals and social media that make you instantly recognisable.', btn='Stand out now'),
 'P5': dict(theme='navy', pos='left', pic='70% center', size=96,
   head='You\'ve got<br><span class="g">the audience</span>', sub2='But not their <span class="g">attention?</span>', sub='Having followers isn\'t enough. You need designs that make them stop.'),
 'P6': dict(theme='white', pos='left', pic='right center', size=128,
   head='We<br><b>Can<span class="g" style="display:inline-block;transform:rotate(18deg) translateY(-14px)">\'t</span></b><br><b>Fix</b><br>Your<br>Brand', light=True,
   sub='Just kidding. We can. Let\'s talk business.'),
}[key]
navy = CFG['theme'] == 'navy'; TXT = '#fff' if navy else N; SUBC = '#dfe5f1' if navy else '#3a4d6e'
logo = re.sub(r'<\?xml[^>]*>', '', open(f'{B}/logo-on-{"navy" if navy else "white"}.svg').read()).replace('<svg', '<svg style="height:56px;width:auto;display:block"', 1)
ic = lambda k, c, s=18: f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" style="color:{c};flex:none">{IC[k]}</svg>'
circ = lambda k: f'<span style="width:36px;height:36px;border-radius:50%;background:{G if k=="PH" else ("rgba(255,255,255,.12)" if navy else N)};display:inline-flex;align-items:center;justify-content:center">{ic(k, N if k=="PH" else ("#fff" if navy else "#fff"))}</span>'
DOT = f'<span style="display:inline-block;width:.236em;height:.236em;border-radius:50%;background:{G};margin-left:.04em"></span>'
pos = CFG['pos']; size = CFG.get('size', 104)
if pos == 'top':
    shade = f'linear-gradient(180deg,{"rgba(1,15,33,.92)" if navy else "rgba(255,255,255,.95)"} 0%,{"rgba(1,15,33,.55)" if navy else "rgba(255,255,255,.55)"} 34%,transparent 52%)'
    box = f'left:90px;right:90px;top:200px'
elif pos == 'topc':
    shade = 'linear-gradient(180deg,rgba(255,255,255,.96) 0%,rgba(255,255,255,.75) 45%,transparent 60%)'
    box = 'left:90px;right:90px;top:220px;text-align:center'
else:
    shade = f'linear-gradient(90deg,{"rgba(1,15,33,.94)" if navy else "rgba(255,255,255,.96)"} 0%,{"rgba(1,15,33,.6)" if navy else "rgba(255,255,255,.7)"} 40%,transparent 60%)'
    box = 'left:90px;width:520px;top:250px'
head_w = 400 if CFG.get('light') else 900
html = f"""<html><head><style>
@font-face{{font-family:M;font-weight:400;src:url({F}montserrat-latin-400-normal.woff2)}}
@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}
@font-face{{font-family:M;font-weight:600;src:url({F}montserrat-latin-600-normal.woff2)}}
@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}
@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;color:{TXT};background:{"#011631" if navy else "#f4f5f8"}}}
.a{{position:absolute}} .g{{color:{G}}} b{{font-weight:900}}
.box{{display:inline-block;background:{G};color:{N};padding:0 .14em;border-radius:.08em;line-height:1.02}}
</style></head><body>
<div class="a" style="inset:0;background:url({pathlib.Path(photo).as_uri()}) {CFG['pic']}/cover"></div>
<div class="a" style="inset:0;background:{shade}"></div>
<div class="a" style="left:0;right:0;bottom:0;height:300px;background:linear-gradient(180deg,transparent,{"rgba(1,15,33,.95)" if navy else "rgba(255,255,255,.92)"})"></div>
{"" if navy else '<div class="a" style="inset:0;background:radial-gradient(700px 560px at 0% 0%,rgba(255,193,7,.22),transparent 62%)"></div>'}
<div class="a" style="left:90px;top:84px">{logo}</div>
<div class="a" style="{box}">
 <div style="font-weight:{head_w};font-size:{size}px;line-height:1.0;letter-spacing:-{size*0.035:.1f}px">{CFG['head']}{DOT}</div>
 {f'<div style="font-weight:900;font-size:52px;letter-spacing:-1.5px;margin-top:34px">{CFG["sub2"]}</div>' if CFG.get('sub2') else ''}
 <div style="font-weight:500;font-size:30px;line-height:1.42;margin-top:{26 if CFG.get('sub2') else 34}px;color:{SUBC};{'margin-left:auto;margin-right:auto;' if pos=='topc' else ''}max-width:{860 if pos.startswith('top') else 500}px">{CFG['sub']}</div>
 {f'<div style="display:inline-block;margin-top:40px;background:{N};color:#fff;border-radius:16px;padding:18px 34px;font-weight:700;font-size:30px">{CFG["btn"]}</div>' if CFG.get('btn') else ''}
</div>
<div class="a" style="left:90px;right:90px;bottom:80px;display:flex;align-items:center;justify-content:space-between;font-weight:700;font-size:23px">
 <div style="display:flex;align-items:center;gap:12px">{circ('PH')}<span style="font-weight:900;font-size:30px">+233 (0)50 332 0548</span></div>
 <div style="display:flex;align-items:center;gap:8px">{circ('IG')}{circ('TT')}{circ('X')}<span style="margin-left:4px">@thedanagstudio</span></div>
</div>
<div class="a" style="inset:0;z-index:50;pointer-events:none;opacity:{.16 if navy else .1};mix-blend-mode:{"overlay" if navy else "multiply"};background-size:256px;background-image:url({R}/grain.png)"></div>
<script>document.fonts.ready.then(()=>document.body.dataset.done=1)</script></body></html>"""
tmp = '/tmp/_hero.html'; open(tmp, 'w').write(html)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
    pg.goto(pathlib.Path(tmp).as_uri()); pg.wait_for_selector('body[data-done]'); pg.wait_for_timeout(400)
    pg.screenshot(path='/tmp/_hero.png'); b.close()
im = Image.open('/tmp/_hero.png').convert('RGB')
im.save(out + '.jpg', quality=93, subsampling=0); im.resize((1080, 1350), Image.LANCZOS).save(out + '-1080.jpg', quality=93)
print('ok', out)
