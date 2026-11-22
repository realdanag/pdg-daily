import re, sys
from playwright.sync_api import sync_playwright
from PIL import Image
R='/home/claude/pdg-daily'; B=f'{R}/book-flyer'; M='/home/claude/models'
sys.path.insert(0,B)
from contacts import IC
F=f'{R}/fonts/'; G='#FFC107'; N='#022452'
logoN=re.sub(r'<\?xml[^>]*>','',open('/home/claude/brand/DANAG-STUDIO-horizontal-on-white.svg').read()).replace('<svg','<svg style="height:46px;width:auto;display:block"',1)
logo=re.sub(r'<\?xml[^>]*>','',open('/home/claude/brand/DANAG-STUDIO-horizontal-mono-white.svg').read()).replace('<svg','<svg style="height:46px;width:auto;display:block"',1)
ic=lambda k,c,s=20: f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" style="color:{c};flex:none">{IC[k]}</svg>'
CSS=f'''@font-face{{font-family:M;font-weight:600;src:url({F}montserrat-latin-600-normal.woff2)}}@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M}}.a{{position:absolute}}'''
spots=''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="rgba(120,170,255,{o})" stroke-width="{w}"/>' for x,y,r,o,w in [(80,120,60,.35,26),(200,60,40,.3,20),(140,260,70,.25,30),(40,380,50,.35,22),(230,330,45,.3,18),(110,520,80,.22,34),(260,470,35,.35,16),(60,650,55,.3,24),(220,640,60,.25,26),(140,800,70,.3,30)])
blobL=f'''<svg class="a" viewBox="0 0 400 900" style="left:-40px;top:560px;width:420px;height:900px"><defs><linearGradient id="bl" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1d5fc0"/><stop offset=".55" stop-color="#0a3778"/><stop offset="1" stop-color="#021a3d"/></linearGradient><clipPath id="cl"><path d="M0 60 C 120 40, 210 130, 220 260 C 232 420, 120 470, 160 620 C 190 740, 300 800, 330 900 L 0 900 Z"/></clipPath></defs><g clip-path="url(#cl)"><rect width="400" height="900" fill="url(#bl)"/>{spots}</g></svg>'''
blobR=f'''<svg class="a" viewBox="0 0 400 600" style="right:-40px;top:-30px;width:420px;height:620px"><defs><linearGradient id="br" x1="1" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#021a3d"/><stop offset=".5" stop-color="#0a3778"/><stop offset="1" stop-color="#1d5fc0"/></linearGradient><clipPath id="cr"><path d="M400 0 L 120 0 C 160 90, 300 110, 290 230 C 280 360, 330 470, 400 560 Z"/></clipPath></defs><g clip-path="url(#cr)"><rect width="400" height="600" fill="url(#br)"/>{spots}</g></svg>'''
def build(white):
  TX=N if white else '#fff'
  BG='#ffffff' if white else 'radial-gradient(ellipse 60% 55% at 55% 45%,#ffc928 0%,#f2aa00 40%,#d98f00 72%,#b87200 100%)'
  LOGO=logoN if white else logo
  return f'''<body style="background:{BG}">
{"" if white else '<div class="a" style="left:-120px;top:-160px;width:900px;height:700px;border-radius:50%;background:radial-gradient(ellipse,rgba(255,220,120,.35),transparent 65%)"></div>'}

<svg class="a" style="inset:0;width:1080px;height:1350px;fill:none;stroke:{"rgba(2,36,82,.12)" if white else "rgba(255,255,255,.3)"};stroke-width:1.5"><circle cx="560" cy="760" r="260"/><circle cx="560" cy="760" r="420"/><line x1="0" y1="700" x2="1080" y2="700" stroke="rgba(255,255,255,.25)"/></svg>
{blobR}{blobL}
<div class="a" style="left:76px;top:70px;right:110px;display:flex;align-items:center;gap:28px">{LOGO}<div style="flex:1;height:2px;background:{TX}"></div></div>
<img class="a" src="file://{M}/tue2_cut.png" style="left:170px;top:60px;width:1260px;height:auto;filter:drop-shadow(-20px 30px 50px rgba(60,30,0,.3))">
<div class="a" style="left:470px;top:1020px;width:420px;height:16px;border-radius:10px;background:linear-gradient(90deg,transparent,rgba(255,255,255,.9),transparent);transform:rotate(-24deg);filter:blur(4px);mix-blend-mode:screen"></div>
<div class="a" style="left:430px;top:1080px;width:300px;height:10px;border-radius:10px;background:linear-gradient(90deg,transparent,rgba(255,255,255,.7),transparent);transform:rotate(-24deg);filter:blur(3px);mix-blend-mode:screen"></div>
<div class="a" style="left:200px;top:180px;width:2px;height:820px;background:{TX};opacity:.85;z-index:5"></div>
<div class="a" style="z-index:5;left:140px;top:340px;transform-origin:0 0;transform:rotate(-90deg)"><span style="display:inline-block;background:{N};color:#fff;font-weight:900;font-size:40px;letter-spacing:4px;padding:10px 22px">HELLO</span></div>
<div class="a" style="z-index:5;left:228px;top:1010px;transform-origin:0 0;transform:rotate(-90deg);white-space:nowrap;font-weight:900;font-size:168px;line-height:.8;letter-spacing:-3px;color:{TX};text-shadow:{"none" if white else "0 8px 30px rgba(90,40,0,.45)"}">TUESDAY</div>
<div class="a" style="left:-40px;top:1135px;width:300px;height:240px;border-radius:50%;background:radial-gradient(ellipse,rgba(60,140,255,.85),transparent 70%);filter:blur(10px)"></div>
<div class="a" style="z-index:6;left:74px;right:74px;top:1180px;height:112px;border:2px solid {"rgba(2,36,82,.35)" if white else "rgba(255,255,255,.9)"};border-radius:60px;display:flex;align-items:center;justify-content:space-between;padding:0 16px;backdrop-filter:blur(2px)">
<div style="background:{N if white else '#fff'};color:{'#fff' if white else N};border-radius:40px;padding:20px 30px;display:flex;align-items:center;gap:12px;font-weight:900;font-size:25px;box-shadow:0 10px 24px rgba(2,36,82,.25)">{ic("PH",G if white else N,24)}+233 (0)50 332 0548</div>
<div style="display:flex;align-items:center;gap:8px;font-weight:800;font-size:24px;color:#fff;padding-right:20px;text-shadow:0 2px 10px rgba(0,0,0,.35)">{''.join(f'<span style="width:36px;height:36px;border-radius:50%;background:#fff;display:inline-flex;align-items:center;justify-content:center">{ic(k,N,18)}</span>' for k in ("IG","TT","X"))}<span style="margin-left:4px">@thedanagstudio</span></div></div>
</body>'''
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    for name,white in (('2026-11-24-v6',False),('2026-11-24-v6w',True)):
        open('/tmp/_t.html','w').write(f'<html><head><style>{CSS}</style></head>{build(white)}</html>')
        pg.goto('file:///tmp/_t.html'); pg.wait_for_timeout(900); pg.screenshot(path='/tmp/_t.png')
        im=Image.open('/tmp/_t.png').convert('RGB'); im.save(f'{R}/flyers/{name}.jpg',quality=93,subsampling=0); im.resize((1080,1350),Image.LANCZOS).save(f'{R}/flyers/{name}-1080.jpg',quality=93)
    b.close()
