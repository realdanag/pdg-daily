import re, sys
from playwright.sync_api import sync_playwright
from PIL import Image
R='/home/claude/pdg-daily'; sys.path.insert(0,f'{R}/book-flyer')
from contacts import IC
F=f'{R}/fonts/'; G='#FFC107'; N='#022452'
OUT=f'{R}/promo/feed-F1'
logo=re.sub(r'<\?xml[^>]*>','',open('/home/claude/brand/DANAG-STUDIO-horizontal-on-navy.svg').read()).replace('<svg','<svg style="height:46px;width:auto;display:block"',1)
mark=re.sub(r'<\?xml[^>]*>','',open('/home/claude/brand/DS-mark-white.svg').read()).replace('<svg','<svg style="width:100%;height:100%;display:block"',1)
FB='<path fill="currentColor" d="M9.101 23.691v-7.98H6.627v-3.667h2.474v-1.58c0-4.085 1.848-5.978 5.858-5.978.401 0 .955.042 1.468.103a8.68 8.68 0 0 1 1.141.195v3.325a8.623 8.623 0 0 0-.653-.036 26.805 26.805 0 0 0-.733-.009c-.707 0-1.259.096-1.675.309a1.686 1.686 0 0 0-.679.622c-.258.42-.374.995-.374 1.752v1.297h3.919l-.386 2.103-.287 1.564h-3.246v8.245C19.396 23.238 24 18.179 24 12.044c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.628 3.874 10.35 9.101 11.647Z"/>'
circ=lambda svg:f'<div style="width:40px;height:40px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center"><svg viewBox="0 0 24 24" width="21" height="21" style="color:{N}">{svg}</svg></div>'
soc=''.join(circ(x) for x in (IC['IG'],IC['TT'],IC['X'],FB))
CSS=f'''@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;color:#fff;background:linear-gradient(165deg,#032F65 0%,#022452 40%,#011631 78%,#010F21 100%)}}.a{{position:absolute}}'''
# feed tiles: competitors' posts (generic grey-navy) with one empty dashed slot
tiles=''
for i in range(12):
    if i==7:
        tiles+=f'<div style="aspect-ratio:1;border-radius:10px;border:3px dashed {G};display:flex;align-items:center;justify-content:center;font-weight:900;font-size:54px;color:{G}">?</div>'
    else:
        shade=['#0d3a7a','#0a2f63','#123f80','#082a58','#0f3670','#0b3166','#103c7a','#0a2d5e','#0e3874','#0a2f63','#123f80','#0b3166'][i]
        bar='' if i%2 else f'<div style="position:absolute;left:12px;right:30px;bottom:14px;height:8px;border-radius:4px;background:rgba(255,255,255,.35)"></div>'
        tiles+=f'<div style="position:relative;aspect-ratio:1;border-radius:10px;background:{shade}"><div style="position:absolute;left:12px;top:12px;width:34px;height:34px;border-radius:50%;background:rgba(255,255,255,.18)"></div>{bar}</div>'
html=f'''<body>
<div class="a" style="left:-150px;bottom:-130px;width:700px;height:700px;opacity:.04">{mark}</div>
<div class="a" style="left:80px;right:80px;top:76px;display:flex;justify-content:space-between;align-items:center">{logo}<div style="display:flex;align-items:center;gap:9px">{soc}<span style="font-weight:700;font-size:22px;margin-left:6px">@thedanagstudio</span></div></div>
<div class="a" style="left:80px;top:230px;bottom:250px;width:470px;display:flex;flex-direction:column;justify-content:center">
 <div style="font-weight:500;font-size:62px;line-height:1.06;letter-spacing:-1.5px">Your<br>competitors<br>are posting<span style="display:inline-block;width:.2em;height:.2em;border-radius:50%;background:{G};margin-left:.04em"></span></div>
 <div style="font-weight:900;font-size:100px;line-height:1;letter-spacing:-3px;color:{G};margin-top:26px;white-space:nowrap">Are you<span style="position:relative;display:inline-block;margin-left:.08em"><span style="color:#fff;display:inline-block;clip-path:inset(0 0 .375em 0)">?</span><span style="position:absolute;left:50%;bottom:.07em;transform:translateX(-50%);width:.25em;height:.25em;border-radius:50%;background:#FFC107"></span></span></div>
 <div style="display:flex;gap:20px;margin-top:40px"><div style="width:5px;background:{G};border-radius:3px"></div><div style="font-weight:500;font-size:28px;line-height:1.45;color:#dfe5f1">An empty page tells customers nothing. We design and manage posts that keep your brand seen every week.</div></div>
</div>
<div class="a" style="right:80px;top:200px;width:400px;height:860px;border-radius:56px;background:#010c1d;border:3px solid rgba(255,255,255,.22);box-shadow:0 40px 80px rgba(0,5,16,.6);padding:26px 20px">
 <div style="width:110px;height:26px;border-radius:14px;background:#000;margin:0 auto 22px"></div>
 <div style="display:flex;align-items:center;gap:14px;padding:0 6px 18px"><div style="width:64px;height:64px;border-radius:50%;border:3px solid {G};background:#0b3166"></div><div><div style="width:150px;height:14px;border-radius:7px;background:rgba(255,255,255,.55)"></div><div style="width:100px;height:10px;border-radius:5px;background:rgba(255,255,255,.25);margin-top:10px"></div></div></div>
 <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px">{tiles}</div>
 <div style="margin-top:26px;text-align:center;font-weight:700;font-size:21px;color:rgba(255,255,255,.65);letter-spacing:1px">Is this gap your brand?</div><div style="position:absolute;left:20px;right:20px;bottom:26px;display:flex;justify-content:space-around;opacity:.5"><div style="width:30px;height:30px;border-radius:8px;border:3px solid #fff"></div><div style="width:30px;height:30px;border-radius:8px;border:3px solid #fff"></div><div style="width:30px;height:30px;border-radius:8px;border:3px solid #fff"></div><div style="width:30px;height:30px;border-radius:8px;border:3px solid #fff"></div><div style="width:30px;height:30px;border-radius:8px;border:3px solid #fff"></div></div>
</div>
<div class="a" style="left:80px;right:80px;bottom:76px;display:flex;justify-content:space-between;align-items:center;border-top:2px solid rgba(255,193,7,.35);padding-top:34px">
 <div style="display:flex;align-items:center;gap:12px;background:{G};color:{N};font-weight:900;font-size:26px;border-radius:40px;padding:18px 32px"><svg viewBox="0 0 24 24" width="26" height="26" style="color:{N}">{IC['PH']}</svg>Book: +233 (0)50 332 0548</div>
 <div style="font-weight:700;font-size:26px">Social media management</div></div>
</body>'''
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    open('/tmp/_f.html','w').write(f'<html><head><style>{CSS}</style></head>{html}</html>')
    pg.goto('file:///tmp/_f.html'); pg.wait_for_timeout(800); pg.screenshot(path='/tmp/_f.png')
    im=Image.open('/tmp/_f.png').convert('RGB'); im.save(f'{OUT}.jpg',quality=93,subsampling=0); im.resize((1080,1350),Image.LANCZOS).save(f'{OUT}-1080.jpg',quality=93)
    b.close()
