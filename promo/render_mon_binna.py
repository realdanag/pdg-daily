import re, sys
from playwright.sync_api import sync_playwright
from PIL import Image
R='/home/claude/pdg-daily'; B=f'{R}/book-flyer'; M='/home/claude/models'
F=f'{R}/fonts/'; G='#FFC107'; N='#022452'
logo=re.sub(r'<\?xml[^>]*>','',open(f'{B}/logo-on-white.svg').read()).replace('<svg','<svg style="height:54px;width:auto;display:block"',1)
CSS=f'''@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}@font-face{{font-family:S;src:url({F}sacramento-latin-400-normal.woff2)}}@font-face{{font-family:GB;src:url(/home/claude/fonts2/GoboldBold.otf)}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;background:#010c1f}}.a{{position:absolute}}'''
html=f'''<body>
<div class="a" style="inset:0;background:linear-gradient(90deg,#021a3d 0%,#0a3f80 14%,#1f6fd1 20.5%,#cfe3ff 21.6%,#ffffff 22%,#ffffff 78%,#cfe3ff 78.4%,#1f6fd1 79.5%,#0a3f80 86%,#021a3d 100%)"></div>
<div class="a" style="left:120px;top:0;width:150px;height:1350px;background:linear-gradient(90deg,transparent,rgba(160,205,255,.55));filter:blur(18px)"></div>
<div class="a" style="right:120px;top:0;width:150px;height:1350px;background:linear-gradient(270deg,transparent,rgba(160,205,255,.55));filter:blur(18px)"></div>
<div class="a" style="left:0;right:0;top:0;height:1350px;background:linear-gradient(180deg,transparent 0%,transparent 55%,rgba(2,26,61,.35) 66%,rgba(2,26,61,.8) 76%,#021a3d 84%,#010c1f 100%)"></div>
<div class="a" style="left:0;right:0;top:118px;display:flex;justify-content:center">{logo}</div>
<div class="a" style="left:0;right:0;top:205px;text-align:center">
<div style="font-family:S;font-size:92px;line-height:1;color:{N}">Welcome to a</div>
<div style="font-weight:900;font-size:86px;line-height:1;letter-spacing:-3px;color:{N};margin-top:-4px">New Week<span style="display:inline-block;width:.236em;height:.236em;border-radius:50%;background:{G};margin-left:.03em"></span></div></div>
<img class="a" src="file://{M}/mon_grade.png" style="left:20px;top:330px;width:1040px;height:1040px;-webkit-mask-image:linear-gradient(180deg,#000 70%,transparent 100%)">
<div class="a" style="left:0;right:0;top:0;height:1350px;background:linear-gradient(180deg,transparent 0%,transparent 62%,rgba(1,12,31,.55) 76%,rgba(1,12,31,.85) 90%)"></div>
<div class="a" style="left:0;right:0;top:880px;display:flex;justify-content:center;align-items:center;font-family:GB;color:#fff;font-size:228px;line-height:.8;letter-spacing:1px;text-shadow:0 10px 40px rgba(0,0,0,.35)">
<span>MON</span><span style="position:relative;display:inline-block"><span style="clip-path:inset(0 0 0 34%);display:inline-block">D</span><span style="position:absolute;left:1%;width:33%;top:1%;height:90%;display:flex;flex-direction:column;align-items:center;justify-content:space-between;font-family:GB;font-size:62px;line-height:.82;color:#fff;letter-spacing:0"><span>23</span><span>11</span><span>26</span></span></span><span>AY</span></div>
<div class="a" style="left:200px;right:200px;top:1112px;text-align:center;font-weight:500;font-size:27px;line-height:1.4;color:#fff">A fresh week to build, create and grow. Keep pushing until the work speaks for itself.</div>
<div class="a" style="left:0;right:0;top:1225px;display:flex;justify-content:center"><div style="background:linear-gradient(135deg,#ffd54a,#FFC107);color:{N};font-weight:900;font-size:26px;padding:20px 44px;border-radius:40px;box-shadow:0 0 40px rgba(255,193,7,.45)">Book: +233 (0)50 332 0548</div></div>
</body>'''
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    open('/tmp/_m.html','w').write(f'<html><head><style>{CSS}</style></head>{html}</html>')
    pg.goto('file:///tmp/_m.html'); pg.wait_for_timeout(900); pg.screenshot(path='/tmp/_m.png'); b.close()
im=Image.open('/tmp/_m.png').convert('RGB'); im.save(f'{R}/flyers/2026-11-23-v6.jpg',quality=93,subsampling=0); im.resize((1080,1350),Image.LANCZOS).save(f'{R}/flyers/2026-11-23-v6-1080.jpg',quality=93)
