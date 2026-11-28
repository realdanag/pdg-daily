import re,sys,json
from playwright.sync_api import sync_playwright
from PIL import Image
R='/home/claude/pdg-daily'; sys.path.insert(0,f'{R}/book-flyer')
from contacts import IC
F=f'{R}/fonts/'; G='#FFC107'; N='#022452'
OUT=sys.argv[1]
logo=re.sub(r'<\?xml[^>]*>','',open(f'{R}/book-flyer/logo-on-navy.svg').read()).replace('<svg','<svg style="height:56px;width:auto;display:block"',1)
ic=lambda svg:f'<span style="width:40px;height:40px;border-radius:50%;background:rgba(255,255,255,.12);display:inline-flex;align-items:center;justify-content:center"><svg viewBox="0 0 24 24" width="20" height="20" style="color:#fff">{svg}</svg></span>'
soc=''.join(ic(x) for x in (IC['IG'],IC['TT'],IC['X']))
CSS=f'''@font-face{{font-family:GB;src:url("/home/claude/fonts-private/Gobold Extra2.otf")}}@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;color:#fff;background:#020b1f}}.a{{position:absolute}}'''
html=f'''<body><img class="a" src="file:///home/claude/posts/img/crown.png" style="left:0;top:90px;width:1080px;-webkit-mask-image:linear-gradient(to bottom,transparent 0,#000 260px)">
<div class="a" style="left:0;right:0;bottom:0;height:260px;background:linear-gradient(to bottom,rgba(2,11,31,0),rgba(2,11,31,.9))"></div>
<div class="a" style="left:80px;top:70px">{logo}</div>
<div class="a" style="right:80px;top:88px;font-weight:700;font-size:19px;letter-spacing:5px;color:{G}">BRAND TRUTH</div>
<div class="a" style="left:0;right:0;top:160px;text-align:center">
 <div style="font-weight:900;font-size:68px;line-height:1.04;letter-spacing:-2px">Your logo is not</div>
 <div style="font-weight:900;font-size:68px;line-height:1.04;letter-spacing:-2px;color:#9fb3d6">your brand<span style="display:inline-block;width:17px;height:17px;border-radius:50%;background:{G};margin-left:4px"></span></div>
 <div style="font-weight:500;font-size:25px;line-height:1.45;color:#c9d4ea;margin:18px auto 0;max-width:780px">A crown on its own is just an object. Your brand is how people feel every time they meet you.</div>
</div>
<div class="a" style="left:80px;right:80px;bottom:64px;padding-top:24px;border-top:1px solid rgba(255,255,255,.18);display:flex;align-items:center;justify-content:space-between">
 <div style="display:flex;align-items:center;gap:12px"><span style="width:40px;height:40px;border-radius:50%;background:{G};display:inline-flex;align-items:center;justify-content:center"><svg viewBox="0 0 24 24" width="20" height="20" style="color:{N}">{IC['PH']}</svg></span><span style="font-weight:900;font-size:28px">+233 (0)50 332 0548</span></div>
 <div style="display:flex;align-items:center;gap:8px">{soc}<span style="font-weight:700;font-size:21px;margin-left:4px">@thedanagstudio</span></div></div>
<div class="a" style="inset:0;background:url(file:///home/claude/pdg-daily/grain.png);opacity:.10;mix-blend-mode:overlay"></div>
</body>'''
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    open('/tmp/_c.html','w').write(f'<html><head><style>{CSS}</style></head>{html}</html>')
    pg.goto('file:///tmp/_c.html'); pg.wait_for_timeout(900); pg.screenshot(path='/tmp/_c.png')
    im=Image.open('/tmp/_c.png').convert('RGB'); im.save(f'{OUT}.jpg',quality=93,subsampling=0); im.resize((1080,1350),Image.LANCZOS).save(f'{OUT}-1080.jpg',quality=93); b.close()
print('ok')
