import re,sys,json
from playwright.sync_api import sync_playwright
from PIL import Image
R='/home/claude/pdg-daily'; sys.path.insert(0,f'{R}/book-flyer')
from contacts import IC
F=f'{R}/fonts/'; G='#FFC107'; N='#022452'
OUT=sys.argv[1]
logo=re.sub(r'<\?xml[^>]*>','',open(f'{R}/book-flyer/logo-on-white.svg').read()).replace('<svg','<svg style="height:56px;width:auto;display:block"',1)
MK=json.load(open(f'{R}/edu-kit/mark.json'))
ic=lambda svg:f'<span style="width:40px;height:40px;border-radius:50%;background:{N};display:inline-flex;align-items:center;justify-content:center"><svg viewBox="0 0 24 24" width="20" height="20" style="color:#fff">{svg}</svg></span>'
soc=''.join(ic(x) for x in (IC['IG'],IC['TT'],IC['X']))
CSS=f'''@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}@font-face{{font-family:M;font-weight:600;src:url({F}montserrat-latin-600-normal.woff2)}}@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;color:{N};background:#fff}}.a{{position:absolute}}'''
W,H=900,640
before=f'''<div style="position:absolute;inset:0;background:#f4efe4">
<div style="position:absolute;left:40px;top:90px;color:#6b4b1f;font-weight:700;font-size:26px">Mama Esi's Kitchen</div>
<div style="position:absolute;left:40px;top:140px;width:380px;color:#7a6650;font-weight:500;font-size:19px;line-height:1.55">We sell jollof, waakye, fried rice, banku and tilapia, kenkey, red red and more. Open Monday to Saturday from 8am to 9pm. Delivery available in Madina, Adenta and East Legon. Call us on 000 000 0000 to order today.</div>
</div>'''
after=f'''<div style="position:absolute;inset:0;background:linear-gradient(150deg,#b3261e,#5c0f0b)">
<div style="position:absolute;right:-80px;top:120px;width:470px;height:470px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#ffb347,#e2621b 55%,#a3330c)"></div>
<div style="position:absolute;right:20px;top:200px;width:300px;height:300px;border-radius:50%;background:radial-gradient(circle,#f7c873 0 30%,#d9822b 31% 60%,#b3261e 61%)"></div>
<div style="position:absolute;left:470px;top:40px;color:#ffd166;font-weight:700;font-size:15px;letter-spacing:5px">MAMA ESI'S KITCHEN</div>
<div style="position:absolute;left:468px;top:78px;color:#fff;font-weight:900;font-size:70px;line-height:.92;letter-spacing:-2px">Jollof<br>Sunday<span style="color:#ffd166">.</span></div>
<div style="position:absolute;left:470px;top:250px;display:flex;gap:8px"><span style="background:rgba(255,255,255,.16);border:1.5px solid rgba(255,255,255,.4);color:#fff;font-weight:700;font-size:15px;padding:7px 14px;border-radius:20px">Jollof</span><span style="background:rgba(255,255,255,.16);border:1.5px solid rgba(255,255,255,.4);color:#fff;font-weight:700;font-size:15px;padding:7px 14px;border-radius:20px">Waakye</span></div>
<div style="position:absolute;left:470px;bottom:40px;background:#ffd166;color:#5c0f0b;font-weight:800;font-size:18px;padding:13px 20px;border-radius:14px">Order · 000 000 0000</div></div>'''
html=f'''<body>
<svg class="a" viewBox="252 255 749 664" style="right:-160px;bottom:-60px;width:620px;opacity:.03"><path fill="{N}" fill-rule="evenodd" d="{MK['nodot']}"/><path fill="{N}" d="{MK['dot']}"/></svg>
<div class="a" style="left:90px;top:80px">{logo}</div>
<div class="a" style="right:90px;top:96px;font-weight:700;font-size:20px;letter-spacing:5px;color:{G}">BEFORE · AFTER</div>
<div class="a" style="left:90px;right:90px;top:200px">
 <div style="font-weight:900;font-size:76px;line-height:1.02;letter-spacing:-2.5px">Same business,</div>
 <div style="font-weight:900;font-size:76px;line-height:1.02;letter-spacing:-2.5px;color:#7d8aa3">different first impression<span style="display:inline-block;width:18px;height:18px;border-radius:50%;background:{G};margin-left:4px"></span></div>
</div>
<div class="a" style="left:90px;top:460px;width:{W}px;height:{H}px;border-radius:28px;overflow:hidden;box-shadow:0 30px 60px rgba(2,36,82,.18)">
 <div style="position:absolute;inset:0;clip-path:inset(0 {W-450}px 0 0)">{before}</div>
 <div style="position:absolute;inset:0;clip-path:inset(0 0 0 450px)">{after}</div>
 <div style="position:absolute;left:448px;top:0;bottom:0;width:4px;background:#fff"></div>
 <div style="position:absolute;left:418px;top:{H//2-32}px;width:64px;height:64px;border-radius:50%;background:{G};box-shadow:0 6px 18px rgba(0,0,0,.3);display:flex;align-items:center;justify-content:center;gap:6px;color:{N};font-weight:900;font-size:22px">&#8249;&nbsp;&#8250;</div>
 <div style="position:absolute;left:24px;top:24px;background:rgba(2,36,82,.85);color:#fff;font-weight:700;font-size:16px;padding:8px 16px;border-radius:20px">Before</div>
 <div style="position:absolute;right:24px;top:24px;background:{G};color:{N};font-weight:800;font-size:16px;padding:8px 16px;border-radius:20px">After</div>
</div>
<div class="a" style="left:90px;right:90px;top:1140px;font-weight:500;font-size:28px;line-height:1.45;color:#3a4d6e">Customers decide in one look. Let's make that look count.</div>
<div class="a" style="left:90px;right:90px;bottom:70px;padding-top:26px;border-top:1px solid rgba(2,36,82,.15);display:flex;align-items:center;justify-content:space-between">
 <div style="display:flex;align-items:center;gap:12px"><span style="width:40px;height:40px;border-radius:50%;background:{G};display:inline-flex;align-items:center;justify-content:center"><svg viewBox="0 0 24 24" width="20" height="20" style="color:{N}">{IC['PH']}</svg></span><span style="font-weight:900;font-size:28px">+233 (0)50 332 0548</span></div>
 <div style="display:flex;align-items:center;gap:8px">{soc}<span style="font-weight:700;font-size:21px;margin-left:4px">@thedanagstudio</span></div></div>
</body>'''
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    open('/tmp/_p.html','w').write(f'<html><head><style>{CSS}</style></head>{html}</html>')
    pg.goto('file:///tmp/_p.html'); pg.wait_for_timeout(900); pg.screenshot(path='/tmp/_p.png')
    im=Image.open('/tmp/_p.png').convert('RGB'); im.save(f'{OUT}.jpg',quality=93,subsampling=0); im.resize((1080,1350),Image.LANCZOS).save(f'{OUT}-1080.jpg',quality=93); b.close()
print('ok')
