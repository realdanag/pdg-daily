import re, pathlib, sys
from playwright.sync_api import sync_playwright
from PIL import Image
R='/home/claude/pdg-daily'; B=f'{R}/book-flyer'; M='/home/claude/models'
sys.path.insert(0,B)
import render_book as rb
from contacts import IC
F=f'{R}/fonts/'; G='#FFC107'; N='#022452'
def logo(navy): 
    s=re.sub(r'<\?xml[^>]*>','',open(f'{B}/logo-on-{"navy" if navy else "white"}.svg').read()); return s.replace('<svg','<svg style="height:58px;width:auto;display:block"',1)
ic=lambda k,c,s=18: f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" style="color:{c};flex:none">{IC[k]}</svg>'
def circ(k,navy): return f'<span style="width:36px;height:36px;border-radius:50%;background:{G if k=="PH" else ("rgba(255,255,255,.12)" if navy else N)};display:inline-flex;align-items:center;justify-content:center">{ic(k, N if k=="PH" else "#fff")}</span>'
def mark(navy,style): return f'<svg class="a" viewBox="252 255 749 664" style="{style}"><path fill="{"#fff" if navy else N}" fill-rule="evenodd" d="{rb.MK["nodot"]}"/><path fill="{"#fff" if navy else N}" d="{rb.MK["dot"]}"/></svg>'
CSS=f'''@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}@font-face{{font-family:M;font-weight:600;src:url({F}montserrat-latin-600-normal.woff2)}}@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}@font-face{{font-family:S;src:url({F}sacramento-latin-400-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M}}.a{{position:absolute}}.dot{{display:inline-block;width:.236em;height:.236em;border-radius:50%;background:{G};margin-left:.03em}}'''
def footer(navy,top):
    tx='#fff' if navy else N
    return f'''<div class="a" style="left:90px;right:90px;top:{top}px;padding-top:28px;border-top:1px solid {"rgba(255,255,255,.18)" if navy else "rgba(2,36,82,.15)"};display:flex;align-items:center;justify-content:space-between;font-weight:700;font-size:23px;color:{tx}">
<div style="display:flex;align-items:center;gap:12px">{circ("PH",navy)}<span style="font-weight:900;font-size:30px">+233 (0)50 332 0548</span></div>
<div style="display:flex;align-items:center;gap:8px">{circ("IG",navy)}{circ("TT",navy)}{circ("X",navy)}<span style="margin-left:4px">@thedanagstudio</span></div></div>'''
def datebox(day,date,navy):
    return f'<div class="a" style="right:90px;top:84px;display:flex;align-items:center;gap:20px;color:{"#fff" if navy else N}"><div style="font-weight:900;font-size:96px;line-height:.78;color:{G};letter-spacing:-3px">{date}</div><div style="width:3px;height:72px;background:{G}"></div><div style="font-weight:700;font-size:20px;letter-spacing:6px;line-height:1.55">{day}<span style="display:block;font-weight:900;font-size:32px;letter-spacing:4px;line-height:1.1;margin-top:4px;color:{G}">NOVEMBER</span></div></div>'
mon=f'''<body style="background:linear-gradient(160deg,#032F65 0%,#022452 40%,#011631 78%,#010F21 100%)">
{mark(True,"right:-220px;top:160px;width:600px;opacity:.035")}
<div class="a" style="left:-40px;right:-40px;top:640px;text-align:center;font-weight:900;font-size:330px;letter-spacing:-8px;line-height:1;color:transparent;-webkit-text-stroke:2px rgba(255,255,255,.08)">MONDAY</div>
<div class="a" style="left:90px;top:84px">{logo(True)}</div>{datebox("MONDAY","23",True)}
<div class="a" style="left:0;right:0;top:230px;text-align:center;color:#fff">
<div style="font-family:S;font-size:96px;line-height:1;color:{G}">Welcome to a</div>
<div style="font-weight:900;font-size:150px;line-height:1;letter-spacing:-6px;margin-top:-6px">New Week<span class="dot"></span></div>
<div style="font-weight:500;font-size:30px;margin-top:22px;color:#dfe5f1">Fresh goals, bold moves and great designs ahead.</div></div>
<img class="a" src="file://{M}/mon_rc.png" style="left:170px;top:560px;width:740px;height:740px;-webkit-mask-image:linear-gradient(180deg,#000 64%,transparent 86%)">
{footer(True,1215)}
<div class="a" style="inset:0;z-index:50;pointer-events:none;opacity:.16;mix-blend-mode:overlay;background-size:256px;background-image:url({R}/grain.png)"></div></body>'''
tue=f'''<body style="background:#ffffff">
<div class="a" style="right:-150px;top:200px;width:820px;height:980px;border-radius:410px 410px 60px 410px;background:linear-gradient(160deg,#032F65 0%,#022452 50%,#011631 100%)"></div>
<div class="a" style="right:470px;top:300px;width:150px;height:150px;border-radius:50%;border:16px solid {G}"></div>
<div class="a" style="right:40px;top:1010px;width:90px;height:90px;border-radius:50%;background:{G}"></div>
{mark(False,"left:-200px;bottom:120px;width:520px;opacity:.03")}
<div class="a" style="left:90px;top:84px">{logo(False)}</div>
<div class="a" style="right:90px;top:96px;font-weight:700;font-size:20px;letter-spacing:6px;color:{N}">TUESDAY · <span style="color:#c99700">24 NOVEMBER</span></div>
<div class="a" style="left:96px;top:1175px;transform-origin:0 0;transform:rotate(-90deg);display:flex;align-items:center;gap:30px;white-space:nowrap">
<span style="background:{G};color:{N};font-weight:900;font-size:34px;letter-spacing:5px;padding:10px 22px;border-radius:6px">HELLO</span>
<span style="font-weight:900;font-size:150px;line-height:.8;letter-spacing:-4px;color:{N}">TUESDAY<span class="dot"></span></span></div>
<img class="a" src="file://{M}/tue_rc.png" style="right:-30px;top:330px;width:760px;height:auto;-webkit-mask-image:linear-gradient(180deg,#000 80%,transparent 98%)">
{footer(False,1215)}</body>'''
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    for n,h in (('2026-11-23-v3',mon),('2026-11-24-v3',tue)):
        open('/tmp/_g.html','w').write(f'<html><head><style>{CSS}</style></head>{h}</html>')
        pg.goto('file:///tmp/_g.html'); pg.wait_for_timeout(700); pg.screenshot(path='/tmp/_g.png')
        im=Image.open('/tmp/_g.png').convert('RGB'); im.save(f'{R}/flyers/{n}.jpg',quality=93,subsampling=0); im.resize((1080,1350),Image.LANCZOS).save(f'{R}/flyers/{n}-1080.jpg',quality=93)
    b.close()
