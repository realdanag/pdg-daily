import re, sys
from playwright.sync_api import sync_playwright
from PIL import Image
R='/home/claude/pdg-daily'; B=f'{R}/book-flyer'; M='/home/claude/models'
sys.path.insert(0,B)
import render_book as rb
from contacts import IC
F=f'{R}/fonts/'; G='#FFC107'; N='#022452'
def logo(navy,h=56):
    s=re.sub(r'<\?xml[^>]*>','',open(f'{B}/logo-on-{"navy" if navy else "white"}.svg').read()); return s.replace('<svg',f'<svg style="height:{h}px;width:auto;display:block"',1)
ic=lambda k,c,s=18: f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" style="color:{c};flex:none">{IC[k]}</svg>'
def mark(navy,style): return f'<svg class="a" viewBox="252 255 749 664" style="{style}"><path fill="{"#fff" if navy else N}" fill-rule="evenodd" d="{rb.MK["nodot"]}"/><path fill="{"#fff" if navy else N}" d="{rb.MK["dot"]}"/></svg>'
CSS=f'''@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}@font-face{{font-family:M;font-weight:600;src:url({F}montserrat-latin-600-normal.woff2)}}@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}@font-face{{font-family:S;src:url({F}sacramento-latin-400-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M}}.a{{position:absolute}}.dot{{display:inline-block;width:.236em;height:.236em;border-radius:50%;background:{G};margin-left:.03em}}'''
grain=f'<div class="a" style="inset:0;z-index:60;pointer-events:none;opacity:.17;mix-blend-mode:overlay;background-size:256px;background-image:url({R}/grain.png)"></div>'
big='font-weight:900;font-size:270px;line-height:.82;letter-spacing:-10px;color:#fff;text-shadow:0 0 30px rgba(255,193,7,.55),0 0 90px rgba(255,193,7,.35),0 10px 30px rgba(0,0,0,.35)'
mon=f'''<body style="background:radial-gradient(ellipse 70% 55% at 55% 38%,#0d4a8c 0%,#043067 35%,#021d45 65%,#010c1f 100%)">
<div class="a" style="left:420px;top:120px;width:620px;height:620px;border-radius:50%;background:radial-gradient(circle,rgba(255,193,7,.35),rgba(255,193,7,0) 65%);filter:blur(10px)"></div>
<div class="a" style="right:-80px;top:40px;width:520px;height:260px;border-radius:50%;background:radial-gradient(ellipse,rgba(255,255,255,.22),transparent 70%);filter:blur(30px)"></div>
<div class="a" style="left:-120px;top:520px;width:600px;height:260px;border-radius:50%;background:radial-gradient(ellipse,rgba(255,255,255,.12),transparent 70%);filter:blur(30px)"></div>
{mark(True,"left:-160px;bottom:-60px;width:620px;opacity:.04")}
<div class="a" style="left:84px;top:70px">{logo(True)}</div>
<div class="a" style="right:84px;top:84px;font-weight:700;font-size:20px;letter-spacing:6px;color:#fff">MONDAY · <span style="color:{G}">23 NOV</span></div>
<svg class="a" viewBox="0 0 120 120" style="left:96px;top:208px;width:110px;fill:none;stroke:#fff;stroke-width:4;stroke-linecap:round"><path d="M90 30 C 60 0, 10 20, 20 60 C 28 92, 70 92, 72 66 C 74 44, 44 44, 46 62"/><path d="M80 20 L 92 30 L 78 40"/></svg>
<div class="a" style="left:240px;top:220px;font-weight:600;font-size:34px;letter-spacing:34px;color:#fff">BRAND</div>
<div class="a" style="left:150px;top:280px;{big}">NEW</div>
<div class="a" style="left:90px;top:500px;{big}">WEEK<span class="dot" style="box-shadow:0 0 30px rgba(255,193,7,.7)"></span></div>
<img class="a" src="file://{M}/mon_rc.png" style="left:150px;top:400px;width:950px;height:950px;filter:drop-shadow(0 30px 40px rgba(0,0,0,.45))">
<div class="a" style="right:52px;top:262px;text-align:left;font-weight:800;font-size:30px;line-height:1.2;color:#fff;text-shadow:0 4px 18px rgba(0,0,0,.5)">new week<br>new goals<br>new wins<br><span style="color:{G}">new grace</span><br>hard work</div>
<div class="a" style="left:86px;top:660px;width:0px;height:0px;background:linear-gradient({G},transparent)"></div>
<svg class="a" style="left:90px;top:700px;width:360px;height:200px;overflow:visible"><circle cx="150" cy="10" r="11" fill="{G}"/><line x1="150" y1="10" x2="70" y2="110" stroke="{G}" stroke-width="3"/><line x1="150" y1="10" x2="280" y2="128" stroke="{G}" stroke-width="3"/></svg>
<div class="a" style="left:110px;top:800px;width:300px;padding:20px 0;text-align:center;background:linear-gradient(135deg,#ffd54a,#e0a800);color:{N};font-weight:900;font-size:34px;letter-spacing:1px;transform:rotate(7deg);box-shadow:0 18px 30px rgba(0,0,0,.45);border-radius:6px">KEEP GOING</div>
<img class="a" src="file://{M}/pawn.png" style="left:-150px;top:900px;height:560px;filter:blur(7px) drop-shadow(0 20px 30px rgba(0,0,0,.5));opacity:.95">
<img class="a" src="file://{M}/pawn.png" style="right:-150px;top:150px;height:420px;filter:blur(12px) grayscale(1) brightness(.55) sepia(1) hue-rotate(185deg) saturate(3);opacity:.55;transform:scaleX(-1)">
<div class="a" style="left:0;right:0;bottom:0;height:200px;background:linear-gradient(180deg,transparent,rgba(1,12,31,.92))"></div>
<div class="a" style="left:84px;right:84px;bottom:52px;display:flex;justify-content:space-between;align-items:center;font-weight:700;font-size:24px;color:#fff">
<div style="display:flex;align-items:center;gap:12px"><span style="width:38px;height:38px;border-radius:50%;background:{G};display:inline-flex;align-items:center;justify-content:center">{ic("PH",N)}</span><span style="font-weight:900;font-size:30px">+233 (0)50 332 0548</span></div>
<div style="display:flex;align-items:center;gap:8px">{''.join(f'<span style="width:38px;height:38px;border-radius:50%;background:rgba(255,255,255,.14);display:inline-flex;align-items:center;justify-content:center">{ic(k,"#fff")}</span>' for k in ("IG","TT","X"))}<span style="margin-left:4px">@thedanagstudio</span></div></div>
{grain}</body>'''
blob=lambda st,c: f'<div class="a" style="{st};background:{c};border-radius:46% 54% 38% 62% / 55% 40% 60% 45%"></div>'
tue=f'''<body style="background:#ffffff">
{blob("left:-260px;top:420px;width:520px;height:620px","#eef1f6")}
{blob("right:-240px;top:-120px;width:560px;height:520px","#eef1f6")}
{blob("right:-280px;bottom:-320px;width:420px;height:420px","#022452")}
<div class="a" style="left:84px;top:66px;display:flex;align-items:center;gap:26px;right:84px">{logo(False,52)}<div style="flex:1;height:2px;background:linear-gradient(90deg,{N},rgba(2,36,82,.1))"></div></div>
<div class="a" style="left:150px;top:170px;width:820px;height:1000px;border-radius:44px;overflow:hidden;background:radial-gradient(ellipse 80% 60% at 65% 35%,#0d4a8c 0%,#043067 40%,#021d45 75%,#010f21 100%);box-shadow:0 40px 80px rgba(2,36,82,.35)">
<div class="a" style="left:300px;top:40px;width:560px;height:560px;border-radius:50%;background:radial-gradient(circle,rgba(255,193,7,.55),rgba(255,193,7,0) 62%)"></div>
<div class="a" style="left:330px;top:90px;width:520px;height:520px;border-radius:50%;border:2px solid rgba(255,255,255,.18)"></div>
<div class="a" style="left:250px;top:10px;width:680px;height:680px;border-radius:50%;border:1.5px solid rgba(255,193,7,.25)"></div>
<div class="a" style="left:-10px;bottom:-30px;width:900px;height:260px;background:repeating-linear-gradient(170deg,rgba(255,255,255,.05) 0 3px,transparent 3px 26px)"></div>
{mark(True,"right:-120px;bottom:-60px;width:420px;opacity:.05")}
<img class="a" src="file://{M}/tue_gold.png" style="left:90px;top:120px;width:1010px;height:auto;-webkit-mask-image:linear-gradient(180deg,#000 84%,transparent 99%);filter:drop-shadow(0 20px 40px rgba(0,0,0,.4))">
</div>
<div class="a" style="left:112px;top:1115px;transform-origin:0 0;transform:rotate(-90deg);display:flex;align-items:center;gap:26px;white-space:nowrap">
<span style="background:{G};color:{N};font-weight:900;font-size:36px;letter-spacing:5px;padding:10px 24px;border-radius:6px;box-shadow:0 10px 24px rgba(0,0,0,.3)">HELLO</span>
<span style="font-weight:900;font-size:134px;line-height:.8;letter-spacing:-4px;color:#fff;text-shadow:0 12px 30px rgba(0,0,0,.35)">TUESDAY<span class="dot"></span></span></div>
<div class="a" style="left:120px;right:120px;top:1205px;height:92px;border:2px solid rgba(2,36,82,.25);border-radius:60px;display:flex;align-items:center;justify-content:space-between;padding:0 14px">
<div style="background:{N};color:#fff;border-radius:40px;padding:16px 26px;display:flex;align-items:center;gap:12px;font-weight:900;font-size:24px"><span style="width:34px;height:34px;border-radius:50%;background:{G};display:inline-flex;align-items:center;justify-content:center">{ic("PH",N)}</span>+233 (0)50 332 0548</div>
<div style="display:flex;align-items:center;gap:8px;font-weight:800;font-size:22px;color:{N};padding-right:16px">{''.join(f'<span style="width:34px;height:34px;border-radius:50%;background:{N};display:inline-flex;align-items:center;justify-content:center">{ic(k,"#fff",16)}</span>' for k in ("IG","TT","X"))}<span style="margin-left:4px">@thedanagstudio</span></div></div>
</body>'''
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    for n,h in (('2026-11-23-v4',mon),('2026-11-24-v4',tue)):
        open('/tmp/_g.html','w').write(f'<html><head><style>{CSS}</style></head>{h}</html>')
        pg.goto('file:///tmp/_g.html'); pg.wait_for_timeout(800); pg.screenshot(path='/tmp/_g.png')
        im=Image.open('/tmp/_g.png').convert('RGB'); im.save(f'{R}/flyers/{n}.jpg',quality=93,subsampling=0); im.resize((1080,1350),Image.LANCZOS).save(f'{R}/flyers/{n}-1080.jpg',quality=93)
    b.close()
