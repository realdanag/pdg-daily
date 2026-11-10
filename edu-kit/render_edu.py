"""Render a DANAG STUDIO design-tip carousel from a JSON spec.
usage: python3 render_edu.py spec.json outdir
spec = {"tip_no": 2, "kicker": "DESIGN TIP 02", "cover_big": "3 FONTS", "cover_title": "Never use more<br>than three",
        "cover_text": "...", "slides": [ {"big": "01", "title": "...", "text": "..."}, ... (3 to 6) ],
        "example_title": "...", "example_html": "<optional inner html for a white example card>"}
Slides alternate navy (odd) and white (even). Max 10 slides total (Instagram limit via Metricool)."""
import json,sys,pathlib
from playwright.sync_api import sync_playwright
K=pathlib.Path(__file__).resolve().parent; F=K/'fonts'
spec=json.load(open(sys.argv[1])); out=pathlib.Path(sys.argv[2]); out.mkdir(parents=True,exist_ok=True)
CSS=f'''@font-face{{font-family:M;font-weight:500;src:url({(F/"montserrat-latin-500-normal.woff2").as_uri()})}}
@font-face{{font-family:M;font-weight:700;src:url({(F/"montserrat-latin-700-normal.woff2").as_uri()})}}
@font-face{{font-family:M;font-weight:900;src:url({(F/"montserrat-latin-900-normal.woff2").as_uri()})}}
@font-face{{font-family:GB;src:url({(F/"anton-latin-400-normal.woff2").as_uri()})}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;font-family:M}}
.s{{position:relative;width:1080px;height:1350px;overflow:hidden}}
.w{{background:linear-gradient(180deg,#fff,#eef1f6);color:#022452}}.n{{background:linear-gradient(135deg,#032F65 0%,#022452 45%,#011631 80%,#010F21 100%);color:#fff}}
.hd{{position:absolute;left:96px;right:96px;top:72px;display:flex;justify-content:space-between;font-weight:700;font-size:17px;letter-spacing:4px}}.hd span:last-child{{opacity:.55}}
.ft{{position:absolute;left:96px;right:96px;bottom:64px;display:flex;justify-content:space-between;font-weight:500;font-size:18px;opacity:.7}}
.k{{font-weight:700;font-size:20px;letter-spacing:5px;color:#FFC107}}.w .k{{color:#b38600}}
h1{{font-weight:900;font-size:84px;line-height:1.02;letter-spacing:-2px}}h1 i{{font-style:normal;color:#FFC107}}
p{{font-weight:500;font-size:30px;line-height:1.5}}.w p{{color:#33415c}}.n p{{color:rgba(255,255,255,.82)}}.a{{position:absolute}}'''
NUM=json.load(open(K/'numerals.json'))
MK=json.load(open(K/'mark.json'))
def bgmark(th): return f'<svg class="a" viewBox="252 255 749 664" style="right:-260px;bottom:-60px;width:820px;opacity:{.05 if th=="n" else .045}"><path fill="{"#fff" if th=="n" else "#022452"}" fill-rule="evenodd" d="{MK["nodot"]}"/><path fill="{"#fff" if th=="n" else "#022452"}" d="{MK["dot"]}"/></svg>'
def big(txt,size,color='#FFC107'):
    """Gobold High outlines for numerals; other text falls back to Anton."""
    if not all(c in NUM['g'] for c in txt):
        return f'<span style="font-family:GB">{txt}</span>'
    sc=size/NUM['upm']; x=0; paths=''; base=NUM['asc']*sc*0.78
    for c in txt:
        paths+=f'<path fill="{color}" transform="translate({x:.1f} {base:.1f}) scale({sc:.4f} {-sc:.4f})" d="{NUM['g'][c]['d']}"/>'; x+=NUM['g'][c]['w']*sc+size*0.03
    return f'<svg width="{x:.0f}" height="{base:.0f}" style="display:block;overflow:visible">{paths}</svg>'
S=[]
S.append(f'''<div class="a fit" style="left:96px;top:250px;font-family:GB;font-size:300px;line-height:.85;color:#FFC107;white-space:nowrap">{big(spec["cover_big"],380)}</div>
<div class="a" style="left:96px;right:96px;top:600px"><div class="k">{spec["kicker"]}</div><h1 style="margin-top:22px;font-size:96px">{spec["cover_title"]}<i>.</i></h1><p style="margin-top:34px;max-width:840px">{spec["cover_text"]}</p></div>''')
for sl in spec["slides"]:
    S.append(f'''<div class="a" style="left:96px;top:230px;font-family:GB;font-size:280px;line-height:.8;color:#FFC107">{big(sl["big"],340)}</div>
<div class="a" style="left:96px;right:96px;top:560px"><h1 style="font-size:84px">{sl["title"]}<i>.</i></h1><p style="margin-top:32px;max-width:860px;font-size:32px">{sl["text"]}</p></div>''')
if spec.get("example_title"):
    S.append(f'''<div class="a" style="left:96px;right:96px;top:200px"><div class="k">REAL EXAMPLE</div><h1 style="margin-top:20px">{spec["example_title"]}<i>.</i></h1></div>
<div class="a" style="left:96px;right:96px;top:540px;height:520px;border-radius:28px;overflow:hidden;background:linear-gradient(135deg,#032F65,#011631);box-shadow:0 20px 40px rgba(2,36,82,.25);color:#fff;padding:60px">{spec.get("example_html","")}</div>''')
S.append(f'''<div class="a" style="left:0;right:0;top:250px;display:flex;justify-content:center"><img src="__CLOSELOGO__" style="width:420px"></div>
<div class="a" style="left:96px;right:96px;top:840px;text-align:center"><h1 style="font-size:80px">Save this for<br>your next design<i>.</i></h1><p style="margin-top:24px">Follow @thedanagstudio for design tips every week.</p></div>''')
assert len(S)<=10
T=len(S)
with sync_playwright() as pw:
    b=pw.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
    for i,inner in enumerate(S,1):
        th='n' if i%2 else 'w'; logo=K/f'DANAG-STUDIO-horizontal-{"on-navy" if th=="n" else "on-white"}.svg'
        html=f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s {th}">{bgmark(th) if i<T else ""}
<div class="hd"><span><img src="{logo.as_uri()}" style="height:44px;margin-top:-10px"></span><span>DESIGN TIPS · {i:02d}/{T}</span></div>{inner}
<div class="ft"><span>@thedanagstudio</span><span>{"Save for later" if i==T else "Swipe &rarr;"}</span></div></div></body></html>'''
        html=html.replace('__CLOSELOGO__',(K/('DANAG-STUDIO-stacked-on-navy.svg' if th=='n' else 'DANAG-STUDIO-stacked-on-white.svg')).as_uri())
        tmp=out/f'_s{i}.html'; tmp.write_text(html); pg.goto(tmp.as_uri()); pg.wait_for_timeout(600)
        pg.evaluate("document.querySelectorAll('.fit').forEach(e=>{let s=parseFloat(getComputedStyle(e).fontSize);while(e.scrollWidth>888&&s>60){s-=4;e.style.fontSize=s+'px'}})"); pg.wait_for_timeout(100); pg.screenshot(path=str(out/f'{i:02d}.png')); tmp.unlink()
    b.close()
from PIL import Image
for i in range(1,T+1):
    im=Image.open(out/f'{i:02d}.png').convert('RGB'); im.save(out/f'{i:02d}.jpg',quality=95,subsampling=0)
    im.resize((1080,1350),Image.LANCZOS).save(out/f'{i:02d}-1080.jpg',quality=95,subsampling=0); (out/f'{i:02d}.png').unlink()
print(T)
