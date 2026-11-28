import re,sys
from playwright.sync_api import sync_playwright
from PIL import Image
R='/home/claude/pdg-daily'; sys.path.insert(0,f'{R}/book-flyer')
from contacts import IC
F=f'{R}/fonts/'; G='#FFC107'; N='#022452'
OUT=sys.argv[1]
logo=re.sub(r'<\?xml[^>]*>','',open(f'{R}/book-flyer/logo-on-navy.svg').read()).replace('<svg','<svg style="height:56px;width:auto;display:block"',1)
ic=lambda svg:f'<span style="width:40px;height:40px;border-radius:50%;background:rgba(255,255,255,.12);display:inline-flex;align-items:center;justify-content:center"><svg viewBox="0 0 24 24" width="20" height="20" style="color:#fff">{svg}</svg></span>'
soc=''.join(ic(x) for x in (IC['IG'],IC['TT'],IC['X']))
CSS=f'''@font-face{{font-family:GB;src:url("/home/claude/fonts-private/Gobold Extra2.otf")}}@font-face{{font-family:SC;src:url({F}sacramento-latin-400-normal.woff2)}}@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;color:#fff;background:#020b26}}.a{{position:absolute}}'''
html=f'''<body><img class="a" src="file:///home/claude/posts/img/cup.png" style="left:0;top:0;width:1080px">
<div class="a" style="left:80px;top:70px">{logo}</div>
<div class="a" style="right:80px;top:88px;font-weight:700;font-size:19px;letter-spacing:5px;opacity:.8">29 · 11 · 2026</div>
<div class="a" style="left:0;right:0;top:140px;text-align:center">
 <div style="font-family:SC;font-size:84px;line-height:1;color:{G};margin-bottom:44px">Happy</div>
 <div style="display:inline-block;position:relative;font-family:GB;font-size:200px;line-height:.86;letter-spacing:8px;-webkit-text-stroke:5px #fff;margin-top:-6px"><span style="display:inline-block;transform:scaleY(1.2);transform-origin:left bottom">SUNDAY</span><span style="position:absolute;right:-30px;bottom:-4px;width:36px;height:36px;border-radius:50%;background:{G}"></span></div>
 <div style="font-weight:500;font-size:26px;line-height:1.45;color:#c9d4ea;margin-top:30px">Slow sips, soft plans and a grateful heart.</div>
</div>
<div class="a" style="left:80px;right:80px;bottom:56px;padding-top:24px;border-top:1px solid rgba(255,255,255,.18);display:flex;align-items:center;justify-content:space-between">
 <div style="display:flex;align-items:center;gap:12px"><span style="width:40px;height:40px;border-radius:50%;background:{G};display:inline-flex;align-items:center;justify-content:center"><svg viewBox="0 0 24 24" width="20" height="20" style="color:{N}">{IC['PH']}</svg></span><span style="font-weight:900;font-size:28px">+233 (0)50 332 0548</span></div>
 <div style="display:flex;align-items:center;gap:8px">{soc}<span style="font-weight:700;font-size:21px;margin-left:4px">@thedanagstudio</span></div></div>
<div class="a" style="inset:0;background:url(file:///home/claude/pdg-daily/grain.png);opacity:.10;mix-blend-mode:overlay"></div>
</body>'''
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    open('/tmp/_cu.html','w').write(f'<html><head><style>{CSS}</style></head>{html}</html>')
    pg.goto('file:///tmp/_cu.html'); pg.wait_for_timeout(900); pg.screenshot(path='/tmp/_cu.png')
    im=Image.open('/tmp/_cu.png').convert('RGB'); im.save(f'{OUT}.jpg',quality=93,subsampling=0); im.resize((1080,1350),Image.LANCZOS).save(f'{OUT}-1080.jpg',quality=93); b.close()
print('ok')
