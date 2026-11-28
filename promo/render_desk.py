import re,sys
from playwright.sync_api import sync_playwright
from PIL import Image
R='/home/claude/pdg-daily'; sys.path.insert(0,f'{R}/book-flyer')
from contacts import IC
F=f'{R}/fonts/'; G='#FFC107'; N='#022452'
OUT=sys.argv[1]
logo=re.sub(r'<\?xml[^>]*>','',open(f'{R}/book-flyer/logo-on-white.svg').read()).replace('<svg','<svg style="height:56px;width:auto;display:block"',1)
ic=lambda svg:f'<span style="width:38px;height:38px;border-radius:50%;background:{N};display:inline-flex;align-items:center;justify-content:center"><svg viewBox="0 0 24 24" width="19" height="19" style="color:#fff">{svg}</svg></span>'
soc=''.join(ic(x) for x in (IC['IG'],IC['TT'],IC['X']))
CSS=f'''@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}@font-face{{font-family:M;font-weight:600;src:url({F}montserrat-latin-600-normal.woff2)}}@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;color:{N};background:#fff}}.a{{position:absolute}}
.chip{{position:absolute;font-weight:700;font-size:22px;padding:12px 22px;border-radius:30px;white-space:nowrap;box-shadow:0 10px 24px rgba(2,36,82,.15)}}'''
html=f'''<body><img class="a" src="file:///home/claude/posts/img/desk_bg.png" style="left:0;top:40px;width:1080px">
<div class="a" style="left:80px;top:70px">{logo}</div>
<div class="a" style="right:80px;top:86px;font-weight:700;font-size:19px;letter-spacing:5px;color:{G}">LET'S TALK</div>
<div class="a" style="left:0;right:0;top:170px;text-align:center">
 <div style="display:inline-block;position:relative">
  <span style="position:absolute;left:-40px;top:-44px;background:{G};color:{N};font-weight:800;font-size:22px;padding:7px 16px;border-radius:14px 14px 14px 2px;transform:none">Hello</span>
  <div style="font-weight:900;font-size:70px;line-height:1.04;letter-spacing:-2px">Your next client</div>
 </div>
 <div style="font-weight:900;font-size:70px;line-height:1.04;letter-spacing:-2px;color:#7d8aa3">is one call away<span style="display:inline-block;width:17px;height:17px;border-radius:50%;background:{G};margin-left:4px"></span></div>
</div>
<div class="chip" style="left:745px;top:430px;background:{N};color:#fff">Flyers &amp; Posters</div>
<div class="chip" style="left:790px;top:505px;background:{G};color:{N}">Product Visuals</div>
<div class="chip" style="left:760px;top:580px;background:#fff;color:{N};border:1.5px solid rgba(2,36,82,.15)">Websites</div>
<div class="a" style="left:70px;top:440px;width:170px;background:{G};color:{N};padding:20px 18px 22px;border-radius:6px;box-shadow:0 12px 26px rgba(2,36,82,.18);font-weight:900;font-size:26px;line-height:1.1">Your brand<br>deserves<br>better<span style="display:inline-block;width:9px;height:9px;border-radius:50%;background:{N};margin-left:2px"></span><div style="position:absolute;left:72px;top:-12px;width:26px;height:26px;border-radius:50%;background:{N};box-shadow:0 3px 6px rgba(0,0,0,.25)"></div></div>
<div class="a" style="left:0;right:0;bottom:0;height:150px;background:linear-gradient(to bottom,rgba(255,255,255,0),#fff 55%)"></div>
<div class="a" style="left:50%;transform:translateX(-50%);bottom:52px;display:flex;align-items:center;gap:14px;background:{N};color:#fff;font-weight:900;font-size:25px;border-radius:22px;padding:14px 24px;white-space:nowrap;box-shadow:0 10px 30px rgba(2,36,82,.25)">
 <span style="width:38px;height:38px;border-radius:50%;background:{G};display:inline-flex;align-items:center;justify-content:center"><svg viewBox="0 0 24 24" width="19" height="19" style="color:{N}">{IC['PH']}</svg></span>+233 (0)50 332 0548
 <span style="width:1.5px;height:32px;background:rgba(255,255,255,.3)"></span>{''.join(x.replace("background:"+N,"background:rgba(255,255,255,.15)") for x in [soc])}<span style="font-weight:700;font-size:21px">@thedanagstudio</span></div>
</body>'''
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    open('/tmp/_d.html','w').write(f'<html><head><style>{CSS}</style></head>{html}</html>')
    pg.goto('file:///tmp/_d.html'); pg.wait_for_timeout(900); pg.screenshot(path='/tmp/_d.png')
    im=Image.open('/tmp/_d.png').convert('RGB'); im.save(f'{OUT}.jpg',quality=93,subsampling=0); im.resize((1080,1350),Image.LANCZOS).save(f'{OUT}-1080.jpg',quality=93); b.close()
print('ok')
