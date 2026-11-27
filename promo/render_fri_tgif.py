import re,sys
from playwright.sync_api import sync_playwright
from PIL import Image
R='/home/claude/pdg-daily'; sys.path.insert(0,f'{R}/book-flyer')
from contacts import IC
F=f'{R}/fonts/'; G='#FFC107'; N='#022452'
OUT=f'{R}/flyers/2026-11-27-v5-gold'
logo=re.sub(r'<\?xml[^>]*>','',open('/home/claude/brand/DANAG-STUDIO-stacked-on-navy.svg').read()).replace('<svg','<svg style="height:118px;width:auto;display:block"',1)
FB='<path fill="currentColor" d="M9.101 23.691v-7.98H6.627v-3.667h2.474v-1.58c0-4.085 1.848-5.978 5.858-5.978.401 0 .955.042 1.468.103a8.68 8.68 0 0 1 1.141.195v3.325a8.623 8.623 0 0 0-.653-.036 26.805 26.805 0 0 0-.733-.009c-.707 0-1.259.096-1.675.309a1.686 1.686 0 0 0-.679.622c-.258.42-.374.995-.374 1.752v1.297h3.919l-.386 2.103-.287 1.564h-3.246v8.245C19.396 23.238 24 18.179 24 12.044c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.628 3.874 10.35 9.101 11.647Z"/>'
ic=lambda svg:f'<svg viewBox="0 0 24 24" width="26" height="26" style="color:{N}">{svg}</svg>'
soc=''.join(ic(x) for x in (IC['IG'],IC['TT'],IC['X'],FB))
CSS=f'''@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;color:#fff;background:#022452}}.a{{position:absolute}}'''
blobs=f'''<svg class="a" style="left:0;top:0" width="1080" height="1350" viewBox="0 0 1080 1350">
<path d="M-60 300 C 120 120, 520 180, 760 230 C 1010 280, 1160 120, 1180 40 L 1180 1400 L -60 1400 Z" fill="#06336f"/>
<path d="M-80 720 C 60 520, 260 470, 430 560 C 610 650, 760 560, 900 470 C 1040 380, 1160 420, 1200 470 L 1200 1400 L -80 1400 Z" fill="#0a428a"/>
<path d="M-80 1190 C 120 1080, 330 1110, 520 1170 C 720 1230, 930 1150, 1180 1040 L 1180 1400 L -80 1400 Z" fill="#06336f"/>
</svg>'''
deco='''<div class="a" style="left:120px;top:540px;width:34px;height:8px;background:#FFC107;border-radius:4px;transform:rotate(-41deg);filter:blur(7px);opacity:0.8"></div><div class="a" style="left:130px;top:650px;width:26px;height:10px;background:#ffffff;border-radius:4px;transform:rotate(-51deg);filter:blur(0px);opacity:1"></div><div class="a" style="left:250px;top:1010px;width:34px;height:8px;background:#7fb3ff;border-radius:4px;transform:rotate(14deg);filter:blur(0px);opacity:1"></div><div class="a" style="left:960px;top:330px;width:14px;height:14px;background:#FFC107;border-radius:50%;transform:rotate(-56deg);filter:blur(0px);opacity:1"></div><div class="a" style="left:1035px;top:745px;width:18px;height:18px;background:#ffffff;border-radius:4px;transform:rotate(-7deg);filter:blur(0px);opacity:1"></div><div class="a" style="left:880px;top:860px;width:14px;height:14px;background:#7fb3ff;border-radius:50%;transform:rotate(-49deg);filter:blur(7px);opacity:0.8"></div><div class="a" style="left:990px;top:1020px;width:26px;height:10px;background:#FFC107;border-radius:4px;transform:rotate(45deg);filter:blur(0px);opacity:1"></div><div class="a" style="left:130px;top:1120px;width:14px;height:14px;background:#ffffff;border-radius:50%;transform:rotate(20deg);filter:blur(0px);opacity:1"></div><div class="a" style="left:560px;top:170px;width:18px;height:18px;background:#7fb3ff;border-radius:4px;transform:rotate(-54deg);filter:blur(0px);opacity:1"></div><div class="a" style="left:900px;top:215px;width:26px;height:10px;background:#FFC107;border-radius:4px;transform:rotate(11deg);filter:blur(0px);opacity:1"></div><div class="a" style="left:60px;top:420px;width:34px;height:8px;background:#ffffff;border-radius:4px;transform:rotate(-7deg);filter:blur(0px);opacity:1"></div><div class="a" style="left:1030px;top:460px;width:26px;height:10px;background:#7fb3ff;border-radius:4px;transform:rotate(13deg);filter:blur(3px);opacity:0.8"></div>'''
grain='''<div class="a" style="inset:0;background:url(file:///home/claude/pdg-daily/grain.png);opacity:.10;mix-blend-mode:overlay"></div>'''
html=f'''<body>{blobs}
{deco}<div class="a" style="right:64px;top:560px;width:200px;background:rgba(255,255,255,.1);border:1.5px solid rgba(255,255,255,.22);border-radius:18px;padding:16px 18px">
 <div style="font-weight:700;font-size:17px;letter-spacing:2px;opacity:.85">WEEKEND</div>
 <div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:2px"><span style="font-weight:900;font-size:22px">Loaded</span><span style="font-weight:900;font-size:22px;color:#FFC107">100%</span></div>
 <div style="height:8px;border-radius:4px;background:#FFC107;margin-top:10px"></div></div>
<div class="a" style="left:60px;top:640px;transform-origin:left top;transform:rotate(-90deg) translateX(-100%);font-weight:700;font-size:18px;letter-spacing:6px;opacity:.7;white-space:nowrap">FRIDAY · 27 NOV 2026</div><div class="a" style="left:80px;top:60px">{logo}</div>
<div class="a" style="right:80px;top:118px;font-weight:700;font-size:28px">...creating all week, resting tonight</div>
<div class="a" style="left:0;right:0;top:200px;text-align:center;font-weight:900;font-size:380px;line-height:.9;letter-spacing:-18px">tgif<span style="display:inline-block;width:76px;height:76px;border-radius:50%;background:{G};margin-left:14px"></span></div>
<div class="a" style="left:318px;top:238px;font-weight:700;font-size:30px">Hello weekend</div>
<img class="a" src="file:///home/claude/tgif/model_gold.png" style="left:50%;transform:translateX(-50%);bottom:0;height:880px">
<div class="a" style="left:50%;transform:translateX(-50%);bottom:64px;display:flex;align-items:center;gap:14px;background:#fff;color:{N};font-weight:900;font-size:26px;border-radius:22px;padding:18px 30px;white-space:nowrap"><svg viewBox="0 0 24 24" width="26" height="26" style="color:{N}">{IC['PH']}</svg>+233 (0)50 332 0548<span style="width:2px;height:30px;background:rgba(2,36,82,.2)"></span>{soc}</div>
{grain}</body>'''
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    open('/tmp/_tg2.html','w').write(f'<html><head><style>{CSS}</style></head>{html}</html>')
    pg.goto('file:///tmp/_tg2.html'); pg.wait_for_timeout(900); pg.screenshot(path='/tmp/_tg2.png')
    im=Image.open('/tmp/_tg2.png').convert('RGB'); im.save(f'{OUT}.jpg',quality=93,subsampling=0); im.resize((1080,1350),Image.LANCZOS).save(f'{OUT}-1080.jpg',quality=93)
    b.close()
