import re, sys, math
from playwright.sync_api import sync_playwright
from PIL import Image
R='/home/claude/pdg-daily'; B=f'{R}/book-flyer'
sys.path.insert(0,B)
from contacts import IC
F=f'{R}/fonts/'; G='#FFC107'; N='#022452'
OUT=sys.argv[1] if len(sys.argv)>1 else f'{R}/flyers/2026-11-25-v1'
logo=re.sub(r'<\?xml[^>]*>','',open('/home/claude/brand/DANAG-STUDIO-horizontal-mono-white.svg').read()).replace('<svg','<svg style="height:44px;width:auto;display:block"',1)
ic=lambda k,c,s=20: f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" style="color:{c};flex:none">{IC[k]}</svg>'
CSS=f'''@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}@font-face{{font-family:M;font-weight:600;src:url({F}montserrat-latin-600-normal.woff2)}}@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;background:linear-gradient(165deg,#022452 0%,#011b3e 45%,#011129 80%,#010b1c 100%)}}.a{{position:absolute}}'''
noise='''<svg class="a" style="inset:0;width:1080px;height:1350px;z-index:20;pointer-events:none;mix-blend-mode:overlay;opacity:.35"><filter id="nz"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="3" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter><rect width="100%" height="100%" filter="url(#nz)"/></svg>'''
# dial
CX,CY,RO,RI=540,1890,1190,1095
def pt(r,a): a=math.radians(a); return CX+r*math.sin(a), CY-r*math.cos(a)
def arcpath(r,a0,a1):
    x0,y0=pt(r,a0); x1,y1=pt(r,a1); return f'M{x0:.1f},{y0:.1f} A{r},{r} 0 0 1 {x1:.1f},{y1:.1f}'
days=['Monday','Tuesday','Wednesday','Thursday','Friday']; angs=[-26,-13,0,13,26]
band=f'<path d="{arcpath(RO,-40,40)}" stroke="{G}" stroke-width="3" fill="none"/><path d="{arcpath(RI,-40,40)}" stroke="{G}" stroke-width="3" fill="none"/>'
band+=f'<path d="{arcpath((RO+RI)/2,-40,40)}" stroke="rgba(255,255,255,.05)" stroke-width="{RO-RI-6}" fill="none"/>'
# highlighted wednesday segment
band+=f'<path d="{arcpath((RO+RI)/2,-6.5,6.5)}" stroke="{G}" stroke-width="{RO-RI-14}" fill="none"/>'
for a in (-32.5,-19.5,-6.5,6.5,19.5,32.5):
    x0,y0=pt(RI+8,a); x1,y1=pt(RO-8,a); band+=f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="rgba(255,255,255,.85)" stroke-width="3"/>'
for d,a in zip(days,angs):
    x,y=pt((RO+RI)/2,a); w=d=='Wednesday'
    band+=f'<text x="{x:.1f}" y="{y:.1f}" transform="rotate({a} {x:.1f} {y:.1f})" text-anchor="middle" dominant-baseline="central" font-family="M" font-weight="{900 if w else 600}" font-size="{29 if w else 32}" letter-spacing="1" fill="{N if w else "rgba(255,255,255,.8)"}">{d.upper() if w else d}</text>'
def needle(L,ang,fill,px,py,w=1):
    k=L/320*w
    p=f'M0,{-L} L{13*k:.1f},{-.70*L} C{60*k:.1f},{-.65*L} {60*k:.1f},{-.53*L} {13*k:.1f},{-.50*L} L{10*k:.1f},0 L{-10*k:.1f},0 L{-13*k:.1f},{-.50*L} C{-60*k:.1f},{-.53*L} {-60*k:.1f},{-.65*L} {-13*k:.1f},{-.70*L} Z'
    return f'<path d="{p}" transform="translate({px},{py}) rotate({ang})" fill="{fill}" filter="url(#sh)"/>'
dial=f'''<svg class="a" style="inset:0;width:1080px;height:1350px;z-index:3" viewBox="0 0 1080 1350"><defs>
<linearGradient id="gg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffd54a"/><stop offset=".5" stop-color="#FFC107"/><stop offset="1" stop-color="#e0a200"/></linearGradient>
<linearGradient id="ww" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#dfe6f2"/></linearGradient>
<filter id="sh" x="-50%" y="-20%" width="200%" height="140%"><feDropShadow dx="-10" dy="14" stdDeviation="12" flood-color="#000814" flood-opacity=".55"/></filter></defs>
<path d="M-40,560 C150,470 260,700 420,600 S700,430 860,560 S1040,620 1140,500" stroke="rgba(255,255,255,.22)" stroke-width="2" fill="none"/>
{band}
{needle(340,-53,"url(#ww)",540,1215,.72)}
{needle(410,0,"url(#gg)",540,1215,.95)}<circle cx="540" cy="1215" r="58" fill="url(#gg)" filter="url(#sh)"/><circle cx="540" cy="1215" r="40" fill="#011129"/><circle cx="540" cy="1215" r="16" fill="url(#gg)"/>
</svg>'''
brush=f'''<svg class="a" style="left:300px;top:448px;width:480px;height:40px;z-index:6" viewBox="0 0 480 40"><path d="M6,26 C120,10 300,8 474,14 L470,20 C320,18 160,22 10,32 Z" fill="{G}"/><path d="M60,34 C200,26 330,25 440,27" stroke="{G}" stroke-width="3" fill="none" opacity=".7"/></svg>'''
bell='<svg viewBox="0 0 24 24" width="54" height="54"><path fill="#FFC107" d="M12 22a2.5 2.5 0 0 0 2.45-2h-4.9A2.5 2.5 0 0 0 12 22zm7-6V11a7 7 0 0 0-5.5-6.84V3.5a1.5 1.5 0 0 0-3 0v.66A7 7 0 0 0 5 11v5l-2 2v1h18v-1z"/></svg>'
html=f'''<body>
{dial}
<div class="a" style="left:76px;top:72px;z-index:6;color:rgba(255,255,255,.85);font-weight:600;font-size:22px;line-height:1.55">IG · TikTok · X: @thedanagstudio<br>FB: Danag Studio</div>
<div class="a" style="right:76px;top:72px;z-index:6">{logo}</div>
<div class="a" style="left:0;right:0;top:190px;z-index:6;text-align:center">
 <div style="font-weight:900;font-size:136px;line-height:1;letter-spacing:-4px;color:#fff">Halfway</div>
 <div style="font-weight:900;font-size:150px;line-height:1;letter-spacing:-4px;color:{G};margin-top:-6px">Check-In<span style="display:inline-block;width:30px;height:30px;border-radius:50%;background:#fff;margin-left:8px"></span></div>
</div>
{brush}
<div class="a" style="left:50%;top:540px;transform:translateX(-50%);z-index:6;display:flex;align-items:center;gap:22px">
 <div style="position:relative;flex:none">{bell}<div style="position:absolute;right:-6px;top:-4px;width:28px;height:28px;border-radius:50%;background:#fff;color:{N};font-weight:900;font-size:17px;display:flex;align-items:center;justify-content:center">1</div></div>
 <div style="background:rgba(1,16,42,.75);border:2px dashed rgba(255,193,7,.6);border-radius:18px;padding:18px 30px">
  <div style="color:#fff;font-weight:700;font-size:31px;line-height:1.2;white-space:nowrap">Wednesday is your halfway mark.</div>
  <div style="color:rgba(255,255,255,.75);font-weight:500;font-size:23px;margin-top:6px;white-space:nowrap">Refocus now. Small steps still finish strong.</div>
 </div>
</div>

<div class="a" style="left:76px;right:76px;bottom:28px;z-index:9;display:flex;align-items:center;justify-content:space-between">
 <div style="display:flex;align-items:center;gap:12px;background:{G};color:{N};font-weight:800;font-weight:900;font-size:26px;border-radius:40px;padding:18px 32px;box-shadow:0 10px 24px rgba(0,5,16,.6)">{ic("PH",N,26)}Book: +233 (0)50 332 0548</div>
 <div style="color:#fff;font-weight:700;font-size:26px">#danagstudio</div>
</div>
<svg class="a" style="left:0;top:1215px;width:1080px;height:160px;z-index:7" viewBox="0 0 1080 160"><defs>
<pattern id="pt" width="18" height="18" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="18" stroke="rgba(255,193,7,.16)" stroke-width="2"/></pattern>
<filter id="up" x="-10%" y="-60%" width="120%" height="200%"><feDropShadow dx="0" dy="-10" stdDeviation="12" flood-color="#000510" flood-opacity=".7"/></filter></defs>
<g filter="url(#up)"><path d="M0,58 C120,30 230,62 360,44 C470,28 520,70 640,52 C760,34 860,64 960,40 C1010,30 1050,36 1080,44 L1080,160 L0,160 Z" fill="#010d22"/></g>
<path d="M0,58 C120,30 230,62 360,44 C470,28 520,70 640,52 C760,34 860,64 960,40 C1010,30 1050,36 1080,44 L1080,160 L0,160 Z" fill="url(#pt)"/>
<path d="M0,58 C120,30 230,62 360,44 C470,28 520,70 640,52 C760,34 860,64 960,40 C1010,30 1050,36 1080,44" fill="none" stroke="#FFC107" stroke-width="2.5"/></svg>
{noise}<svg class="a" style="inset:0;width:1080px;height:1350px;z-index:21;opacity:.09"><filter id="nz2"><feTurbulence type="fractalNoise" baseFrequency="1.2" numOctaves="2" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter><rect width="100%" height="100%" filter="url(#nz2)"/></svg>
</body>'''
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    open('/tmp/_w.html','w').write(f'<html><head><style>{CSS}</style></head>{html}</html>')
    pg.goto('file:///tmp/_w.html'); pg.wait_for_timeout(900); pg.screenshot(path='/tmp/_w.png')
    im=Image.open('/tmp/_w.png').convert('RGB'); im.save(f'{OUT}.jpg',quality=93,subsampling=0); im.resize((1080,1350),Image.LANCZOS).save(f'{OUT}-1080.jpg',quality=93)
    b.close()
