import re,sys
from playwright.sync_api import sync_playwright
from PIL import Image
R='/home/claude/pdg-daily'; sys.path.insert(0,f'{R}/book-flyer')
from contacts import IC
F=f'{R}/fonts/'; G='#FFC107'; N='#022452'
OUT=sys.argv[1]; TOP=int(sys.argv[2]); SC=float(sys.argv[3]); W=int(1080*SC); L=(1080-W)//2; T=1350-int(1349*SC)+20
logo=re.sub(r'<\?xml[^>]*>','',open(f'{R}/book-flyer/logo-on-white.svg').read()).replace('<svg','<svg style="height:56px;width:auto;display:block"',1)
ic=lambda svg:f'<span style="width:38px;height:38px;border-radius:50%;background:{N};display:inline-flex;align-items:center;justify-content:center"><svg viewBox="0 0 24 24" width="19" height="19" style="color:#fff">{svg}</svg></span>'
soc=''.join(ic(x) for x in (IC['IG'],IC['TT'],IC['X']))
CSS=f'''@font-face{{font-family:GB;src:url("/home/claude/fonts-private/Gobold Extra2.otf")}}@font-face{{font-family:SC;src:url({F}sacramento-latin-400-normal.woff2)}}@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;color:{N};background:#fff}}.a{{position:absolute}}
.gb{{font-family:GB;font-size:150px;line-height:.86;letter-spacing:6px;-webkit-text-stroke:6px {N};display:inline-block;transform:scaleY(1.18);transform-origin:center bottom}}'''
html=f'''<body><img class="a" src="file:///home/claude/posts/img/trotro_bg.png" style="left:{L}px;top:{T}px;width:{W}px;-webkit-mask-image:linear-gradient(to right,transparent 0,#000 18%,#000 82%,transparent 100%)">
<div class="a" style="left:80px;top:70px">{logo}</div>
<div class="a" style="right:80px;top:84px;font-weight:700;font-size:19px;letter-spacing:5px;color:{G}">NEW WEEK</div>
<div class="a" style="left:0;right:0;top:{TOP}px;text-align:center">
 <div style="font-family:SC;font-size:86px;line-height:1;color:{N};margin-bottom:58px">It's Monday</div>
 <div><span class="gb">THE GRIND</span></div>
 <div style="margin-top:52px;position:relative;display:inline-block"><span class="gb">RESUMES</span><span style="position:absolute;right:-30px;bottom:2px;width:34px;height:34px;border-radius:50%;background:{G}"></span></div>
</div>
<img class="a" src="file:///home/claude/posts/img/trotro_cut.png" style="left:{L}px;top:{T}px;width:{W}px">
<div class="a" style="left:50%;transform:translateX(-50%);bottom:52px;display:flex;align-items:center;gap:14px;background:#fff;font-weight:900;font-size:25px;border-radius:22px;padding:14px 24px;white-space:nowrap;box-shadow:0 10px 30px rgba(2,36,82,.18)">
 <span style="width:38px;height:38px;border-radius:50%;background:{G};display:inline-flex;align-items:center;justify-content:center"><svg viewBox="0 0 24 24" width="19" height="19" style="color:{N}">{IC['PH']}</svg></span>+233 (0)50 332 0548
 <span style="width:1.5px;height:32px;background:rgba(2,36,82,.2)"></span>{soc}<span style="font-weight:700;font-size:21px">@thedanagstudio</span></div>
</body>'''
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    open('/tmp/_t.html','w').write(f'<html><head><style>{CSS}</style></head>{html}</html>')
    pg.goto('file:///tmp/_t.html'); pg.wait_for_timeout(900); pg.screenshot(path='/tmp/_t.png')
    im=Image.open('/tmp/_t.png').convert('RGB'); im.save(f'{OUT}.jpg',quality=93,subsampling=0); im.resize((1080,1350),Image.LANCZOS).save(f'{OUT}-1080.jpg',quality=93); b.close()
print('ok')
