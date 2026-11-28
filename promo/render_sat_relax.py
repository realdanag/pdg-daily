import re,sys
from playwright.sync_api import sync_playwright
from PIL import Image
R='/home/claude/pdg-daily'; sys.path.insert(0,f'{R}/book-flyer')
from contacts import IC
F=f'{R}/fonts/'; G='#FFC107'; N='#022452'
OUT=sys.argv[1]; TOP=int(sys.argv[2]) if len(sys.argv)>2 else 200; FONT=sys.argv[3]; FS=sys.argv[4]
logo=re.sub(r'<\?xml[^>]*>','',open(f'{R}/book-flyer/logo-on-white.svg').read()).replace('<svg','<svg style="height:58px;width:auto;display:block"',1)
FB='<path fill="currentColor" d="M9.101 23.691v-7.98H6.627v-3.667h2.474v-1.58c0-4.085 1.848-5.978 5.858-5.978.401 0 .955.042 1.468.103a8.68 8.68 0 0 1 1.141.195v3.325a8.623 8.623 0 0 0-.653-.036 26.805 26.805 0 0 0-.733-.009c-.707 0-1.259.096-1.675.309a1.686 1.686 0 0 0-.679.622c-.258.42-.374.995-.374 1.752v1.297h3.919l-.386 2.103-.287 1.564h-3.246v8.245C19.396 23.238 24 18.179 24 12.044c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.628 3.874 10.35 9.101 11.647Z"/>'
ic=lambda svg:f'<span style="width:40px;height:40px;border-radius:50%;background:{N};display:inline-flex;align-items:center;justify-content:center"><svg viewBox="0 0 24 24" width="20" height="20" style="color:#fff">{svg}</svg></span>'
soc=''.join(ic(x) for x in (IC['IG'],IC['TT'],IC['X'],FB))
CSS=f'''@font-face{{font-family:A;src:url("/home/claude/fonts-private/{FONT}")}}@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;color:{N};background:#fff}}.a{{position:absolute}}'''
swoosh=f'''<svg class="a" style="left:0;top:0" width="1080" height="1350" viewBox="0 0 1080 1350" fill="none">

<path d="M-40 500 C 200 440, 430 560, 720 485 S 1050 410, 1140 440" stroke="{G}" stroke-opacity=".55" stroke-width="5" stroke-linecap="round"/></svg>'''
html=f'''<body><img class="a" src="file:///home/claude/tgif/sat/bg.png" style="left:0;top:0;width:1080px">
{swoosh}
<div class="a" style="left:70px;top:70px">{logo}</div>
<div class="a" style="right:70px;top:76px;display:flex;align-items:center;gap:14px;background:#fff;border:1.5px solid rgba(2,36,82,.15);border-radius:40px;padding:10px 12px 10px 22px;font-weight:700;font-size:20px;letter-spacing:2px">SLOW MODE
 <span style="width:64px;height:34px;border-radius:20px;background:{G};position:relative;display:inline-block"><span style="position:absolute;right:4px;top:4px;width:26px;height:26px;border-radius:50%;background:{N}"></span></span></div>
<div class="a" style="left:0;right:0;top:{TOP-40}px;text-align:center"><div style="display:inline-block;text-align:center"><div style="font-weight:700;font-size:28px;margin:0 0 104px 0">Hello weekend,</div><div style="font-family:A;font-size:{FS}px;line-height:.86;letter-spacing:6px;-webkit-text-stroke:7px {N};white-space:nowrap"><span style="position:relative;display:inline-block"><span style="display:inline-block;transform:scaleY(1.32);transform-origin:left bottom">SATURDAY</span><span style="position:absolute;right:-34px;bottom:-14px;width:40px;height:40px;border-radius:50%;background:{G}"></span></span></div></div></div>
<img class="a" src="file:///home/claude/tgif/sat/cut_top.png" style="left:0;top:0;width:1080px">
<div class="a" style="left:46px;top:980px;transform-origin:left top;transform:rotate(-90deg);font-weight:700;font-size:17px;letter-spacing:6px;color:{N};white-space:nowrap;opacity:.55">SATURDAY · 28 NOV 2026</div>
<div class="a" style="left:50%;transform:translateX(-50%);bottom:60px;display:flex;align-items:center;gap:16px;background:#fff;font-weight:900;font-size:26px;border-radius:24px;padding:16px 26px;white-space:nowrap;box-shadow:0 10px 30px rgba(2,36,82,.18)">
 <span style="width:40px;height:40px;border-radius:50%;background:{G};display:inline-flex;align-items:center;justify-content:center"><svg viewBox="0 0 24 24" width="20" height="20" style="color:{N}">{IC['PH']}</svg></span>+233 (0)50 332 0548
 <span style="width:1.5px;height:34px;background:rgba(2,36,82,.2)"></span>{soc}<span style="font-weight:700;font-size:22px">@thedanagstudio</span></div>
</body>'''
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    open('/tmp/_sat.html','w').write(f'<html><head><style>{CSS}</style></head>{html}</html>')
    pg.goto('file:///tmp/_sat.html'); pg.wait_for_timeout(900); pg.screenshot(path='/tmp/_sat.png')
    im=Image.open('/tmp/_sat.png').convert('RGB'); im.save(f'{OUT}.jpg',quality=93,subsampling=0); im.resize((1080,1350),Image.LANCZOS).save(f'{OUT}-1080.jpg',quality=93)
    b.close()
print('ok')
