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
CSS=f'''@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}@font-face{{font-family:M;font-weight:600;src:url({F}montserrat-latin-600-normal.woff2)}}@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}@font-face{{font-family:SC;src:url({F}sacramento-latin-400-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;color:{N};background:#fff}}.a{{position:absolute}}
.it{{display:flex;align-items:baseline;gap:14px;margin-top:30px}}.nm{{font-weight:900;font-size:34px;white-space:nowrap}}.ld{{flex:1;border-bottom:3px dotted rgba(2,36,82,.3);transform:translateY(-8px)}}.tg{{font-weight:700;font-size:18px;letter-spacing:3px;color:{G};white-space:nowrap}}.ds{{font-weight:500;font-size:22px;color:#4a5b78;margin-top:6px}}'''
items=[('Flyers &amp; Posters','BOOK','Bold, clear and made to get calls.'),
('Product Visuals','CHEF\'S PICK','Studio-quality shots, no studio needed.'),
('Social Media Designs','BOOK','Posts that stop the scroll.'),
('Websites','BOOK','Fast, mobile-first and built to sell.'),
('Brochures &amp; Business Cards','BOOK','First impressions you can hold.')]
rows=''.join(f'<div class="it"><span class="nm">{n}</span><span class="ld"></span><span class="tg">{t}</span></div><div class="ds">{d}</div>' for n,t,d in items)
html=f'''<body>
<svg class="a" viewBox="252 255 749 664" style="right:-170px;top:-40px;width:560px;opacity:.03"><path fill="{N}" fill-rule="evenodd" d="{MK['nodot']}"/><path fill="{N}" d="{MK['dot']}"/></svg>
<div class="a" style="left:90px;top:80px">{logo}</div>
<div class="a" style="right:90px;top:96px;font-weight:700;font-size:20px;letter-spacing:5px;color:{G}">THIS WEEK</div>
<div class="a" style="left:90px;right:90px;top:190px;text-align:center">
 <div style="font-family:SC;font-size:76px;line-height:1;color:{N}">Today's menu</div>
 <div style="font-weight:900;font-size:92px;line-height:1;letter-spacing:-3px;margin-top:4px">Fresh designs<span style="display:inline-block;width:22px;height:22px;border-radius:50%;background:{G};margin-left:6px"></span></div>
</div>
<div class="a" style="left:90px;right:90px;top:430px;border:3px solid {N};border-radius:30px;padding:26px 56px 44px">
 <div style="position:absolute;left:50%;top:-20px;transform:translateX(-50%);background:#fff;padding:0 22px;font-weight:700;font-size:20px;letter-spacing:8px;white-space:nowrap">DANAG STUDIO KITCHEN</div>
 {rows}
</div>
<div class="a" style="left:90px;right:90px;top:1112px;text-align:center;font-weight:600;font-size:26px;color:#3a4d6e">Place your order today. Your customers are hungry for it.</div>
<div class="a" style="left:90px;right:90px;bottom:70px;padding-top:26px;border-top:1px solid rgba(2,36,82,.15);display:flex;align-items:center;justify-content:space-between">
 <div style="display:flex;align-items:center;gap:12px"><span style="width:40px;height:40px;border-radius:50%;background:{G};display:inline-flex;align-items:center;justify-content:center"><svg viewBox="0 0 24 24" width="20" height="20" style="color:{N}">{IC['PH']}</svg></span><span style="font-weight:900;font-size:28px">+233 (0)50 332 0548</span></div>
 <div style="display:flex;align-items:center;gap:8px">{soc}<span style="font-weight:700;font-size:21px;margin-left:4px">@thedanagstudio</span></div></div>
</body>'''
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    open('/tmp/_m.html','w').write(f'<html><head><style>{CSS}</style></head>{html}</html>')
    pg.goto('file:///tmp/_m.html'); pg.wait_for_timeout(900); pg.screenshot(path='/tmp/_m.png')
    im=Image.open('/tmp/_m.png').convert('RGB'); im.save(f'{OUT}.jpg',quality=93,subsampling=0); im.resize((1080,1350),Image.LANCZOS).save(f'{OUT}-1080.jpg',quality=93); b.close()
print('ok')
