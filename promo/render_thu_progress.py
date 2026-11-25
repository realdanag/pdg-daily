import re, sys
from playwright.sync_api import sync_playwright
from PIL import Image
R='/home/claude/pdg-daily'; sys.path.insert(0,f'{R}/book-flyer')
from contacts import IC
F=f'{R}/fonts/'; G='#FFC107'; N='#022452'
OUT=f'{R}/flyers/2026-11-26-v1'
logo=re.sub(r'<\?xml[^>]*>','',open('/home/claude/brand/DANAG-STUDIO-horizontal-on-white.svg').read()).replace('<svg','<svg style="height:46px;width:auto;display:block"',1)
mark=re.sub(r'<\?xml[^>]*>','',open('/home/claude/brand/DS-mark-navy.svg').read()).replace('<svg','<svg style="width:100%;height:100%;display:block"',1)
FB='<path fill="currentColor" d="M9.101 23.691v-7.98H6.627v-3.667h2.474v-1.58c0-4.085 1.848-5.978 5.858-5.978.401 0 .955.042 1.468.103a8.68 8.68 0 0 1 1.141.195v3.325a8.623 8.623 0 0 0-.653-.036 26.805 26.805 0 0 0-.733-.009c-.707 0-1.259.096-1.675.309a1.686 1.686 0 0 0-.679.622c-.258.42-.374.995-.374 1.752v1.297h3.919l-.386 2.103-.287 1.564h-3.246v8.245C19.396 23.238 24 18.179 24 12.044c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.628 3.874 10.35 9.101 11.647Z"/>'
circ=lambda svg:f'<div style="width:42px;height:42px;border-radius:50%;background:{N};display:flex;align-items:center;justify-content:center"><svg viewBox="0 0 24 24" width="22" height="22" style="color:#fff">{svg}</svg></div>'
soc=''.join(circ(x) for x in (IC['IG'],IC['TT'],IC['X'],FB))
CSS=f'''@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}@font-face{{font-family:S;src:url({F}sacramento-latin-400-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;background:#fff;color:{N}}}.a{{position:absolute}}'''
days=['MON','TUE','WED','THU','FRI']
seg=''.join(f'''<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:16px">
 <div style="width:100%;height:{70 if i==3 else 54}px;border-radius:14px;background:{G if i<4 else '#ffffff'};border:{'0' if i<4 else '3px dashed rgba(2,36,82,.35)'};{'box-shadow:0 14px 30px rgba(2,36,82,.22);' if i==3 else ''}display:flex;align-items:center;justify-content:center">{'<svg width="30" height="30" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="'+N+'" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg>' if i<3 else ('<span style="font-weight:900;font-size:22px;letter-spacing:2px">TODAY</span>' if i==3 else '')}</div>
 <div style="font-weight:{900 if i==3 else 700};font-size:24px;letter-spacing:3px;color:{N if i==3 else 'rgba(2,36,82,.55)'}">{d}</div></div>''' for i,d in enumerate(days))
html=f'''<body>
<div class="a" style="right:-170px;top:250px;width:760px;height:760px;opacity:.03">{mark}</div>
<div class="a" style="left:80px;right:80px;top:76px;display:flex;justify-content:space-between;align-items:center">{logo}<div style="display:flex;align-items:center;gap:10px">{soc}<span style="font-weight:700;font-size:23px;margin-left:6px">@thedanagstudio</span></div></div>
<div class="a" style="left:80px;right:80px;top:270px">
 <div style="font-family:S;font-size:150px;line-height:.8;color:{N};margin-left:6px">Happy</div>
 <div style="font-weight:900;font-size:176px;line-height:.95;letter-spacing:-7px;margin-top:-4px">Thursday<span style="display:inline-block;width:40px;height:40px;border-radius:50%;background:{G};margin-left:8px"></span></div>
</div>
<div class="a" style="left:80px;right:80px;top:680px">
 <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:26px"><div style="font-weight:900;font-size:30px;letter-spacing:4px">WEEK PROGRESS</div><div style="font-weight:900;font-size:44px;color:{N}">80<span style="color:{G}">%</span></div></div>
 <div style="display:flex;gap:16px;align-items:flex-start">{seg}</div>
</div>
<div class="a" style="left:80px;right:80px;top:985px;display:flex;gap:26px"><div style="width:6px;background:{G};border-radius:3px"></div>
 <div style="font-weight:500;font-size:38px;line-height:1.4;color:#3a4d6e">One more push. Finish what you started and let Friday find you proud of the work.</div></div>
<div class="a" style="left:80px;right:80px;bottom:76px;display:flex;justify-content:space-between;align-items:center;border-top:2px solid rgba(2,36,82,.12);padding-top:34px">
 <div style="display:flex;align-items:center;gap:12px;background:{N};color:#fff;font-weight:900;font-size:26px;border-radius:40px;padding:18px 32px"><svg viewBox="0 0 24 24" width="26" height="26" style="color:{G}">{IC['PH']}</svg>Book: +233 (0)50 332 0548</div>
 <div style="font-weight:700;font-size:26px">#danagstudio</div></div>
</body>'''
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    open('/tmp/_th.html','w').write(f'<html><head><style>{CSS}</style></head>{html}</html>')
    pg.goto('file:///tmp/_th.html'); pg.wait_for_timeout(900); pg.screenshot(path='/tmp/_th.png')
    im=Image.open('/tmp/_th.png').convert('RGB'); im.save(f'{OUT}.jpg',quality=93,subsampling=0); im.resize((1080,1350),Image.LANCZOS).save(f'{OUT}-1080.jpg',quality=93)
    b.close()
