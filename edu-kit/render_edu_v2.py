"""DANAG STUDIO design-tip carousel v2: before/after examples.
usage: python3 edu-kit/render_edu_v2.py spec.json outdir
spec = {
 "kicker": "DESIGN TIP 02",
 "cover": {"l1": "...", "l2": "...", "text": "...", "visual": "<html for a 4:5 mini design, 380x475>"},
 "tips": [ {"title1": "...", "title2": "...", "problem": "...", "fix": "...",
            "before": "<mini design html>", "after": "<mini design html>",
            "before_note": "...", "after_note": "..."} , ... 3 to 6 ],
 "recap": {"l1": "...", "l2": "...", "items": ["Hierarchy", ...]},
 "cta": {"l1": "...", "l2": "...", "text": "..."}
}
Mini designs are inline-styled HTML rendered inside a 400x500 card (use only fictional businesses, never real brand
logos; placeholder phone 000 000 0000). Slides alternate white (odd) / navy (even); faint logo mark on every slide.
Content is vertically balanced between header and footer (space-evenly); the logo appears once per slide (header) plus the faint background mark. Headlines: line 1 strong, line 2 softer, round brand dot at the end. Max 10 slides."""
import sys, json, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image
K = pathlib.Path(__file__).resolve().parent; R = K.parent; F = R / 'fonts'
MK = json.load(open(K / 'mark.json')); IC = json.load(open(R / 'book-flyer' / 'icons.json'))
spec = json.load(open(sys.argv[1])); out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
logo_w = (R / 'book-flyer' / 'logo-on-white.svg').read_text(); logo_n = (R / 'book-flyer' / 'logo-on-navy.svg').read_text()
import re
def lg(dark, h): s = re.sub(r'<\?xml[^>]*>', '', logo_n if dark else logo_w); return s.replace('<svg', f'<svg style="height:{h}px;width:auto;display:block"', 1)
CSS = f'''@font-face{{font-family:M;font-weight:500;src:url({(F/"montserrat-latin-500-normal.woff2").as_uri()})}}
@font-face{{font-family:M;font-weight:600;src:url({(F/"montserrat-latin-600-normal.woff2").as_uri()})}}
@font-face{{font-family:M;font-weight:700;src:url({(F/"montserrat-latin-700-normal.woff2").as_uri()})}}
@font-face{{font-family:M;font-weight:900;src:url({(F/"montserrat-latin-900-normal.woff2").as_uri()})}}
@font-face{{font-family:SC;src:url({(F/"sacramento-latin-400-normal.woff2").as_uri()})}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;font-family:M}}
.s{{position:relative;width:1080px;height:1350px;overflow:hidden}}.a{{position:absolute}}
.w{{background:linear-gradient(180deg,#ffffff,#eef1f6);color:#022452}}
.n{{background:linear-gradient(135deg,#032F65 0%,#022452 45%,#011631 80%,#010F21 100%);color:#fff}}
.hd{{position:absolute;left:84px;right:84px;top:64px;display:flex;justify-content:space-between;align-items:center;font-weight:700;font-size:17px;letter-spacing:4px}}
.hd .pg{{opacity:.55}}
.num{{font-weight:700;font-size:30px;opacity:.6}}
.h1{{font-weight:900;font-size:78px;line-height:1.02;letter-spacing:-2.5px}}
.w .h1 .l2{{color:#7d879a}} .n .h1 .l2{{color:#9fb0cc}}
.dot{{display:inline-block;width:.236em;height:.236em;border-radius:50%;background:#FFC107;margin-left:.03em}}
.gl{{position:absolute;border-radius:50%;filter:blur(30px);pointer-events:none}}
.gr{{position:absolute;inset:0;pointer-events:none;z-index:50;background-image:url({(F.parent/'grain.png').as_uri()});background-size:256px}}
.n .gr{{opacity:.16;mix-blend-mode:overlay}} .w .gr{{opacity:.12;mix-blend-mode:multiply}}
.p1{{font-weight:500;font-size:29px;line-height:1.4}} .w .p1{{color:#6b7488}} .n .p1{{color:rgba(255,255,255,.7)}}
.p2{{font-weight:600;font-size:29px;line-height:1.4}}
.card{{width:430px;height:538px;border-radius:26px;overflow:hidden;position:relative;box-shadow:0 18px 40px rgba(1,15,33,.18)}}
.card>div{{position:absolute;left:0;top:0;width:400px;height:500px;transform:scale(1.075);transform-origin:0 0}}
.pill{{display:inline-block;padding:10px 26px;border-radius:30px;font-weight:700;font-size:22px;flex:none}}
.note{{font-weight:500;font-size:21px;line-height:1.35}} .w .note{{color:#6b7488}} .n .note{{color:rgba(255,255,255,.7)}}
.ft{{position:absolute;left:84px;right:84px;bottom:52px;display:flex;justify-content:space-between;font-weight:600;font-size:18px;opacity:.6}}'''
def mark(dark): return f'<svg class="a" viewBox="252 255 749 664" style="right:-230px;bottom:-80px;width:780px;opacity:{.05 if dark else .045}"><path fill="{"#fff" if dark else "#022452"}" fill-rule="evenodd" d="{MK["nodot"]}"/><path fill="{"#fff" if dark else "#022452"}" d="{MK["dot"]}"/></svg>'
def head(dark, i, T): return f'<div class="hd">{lg(dark,40)}<span class="pg">{spec["kicker"]} · {i:02d}/{T:02d}</span></div>'
def foot(dark, last=False): return f'<div class="ft"><span>@thedanagstudio</span><span>{"Save for later" if last else "Swipe &rarr;"}</span></div>'
GLOW = '<div class="gl" style="width:820px;height:820px;right:-380px;top:-300px;background:radial-gradient(circle,rgba(255,193,7,.26) 0%,rgba(255,193,7,.08) 40%,transparent 66%)"></div><div class="gl" style="width:600px;height:600px;left:-320px;bottom:-200px;background:radial-gradient(circle,rgba(255,193,7,.16) 0%,transparent 62%)"></div>'
slides = []
COL = 'position:absolute;left:84px;right:84px;top:118px;bottom:100px;display:flex;flex-direction:column;justify-content:space-evenly'
c = spec['cover']
slides.append(lambda d,i,T: f'''<div style="{COL}"><div><div style="color:#b38600;font-size:22px;letter-spacing:6px;font-weight:900">{spec["kicker"]}</div>
<div class="h1" style="font-size:96px;margin-top:22px">{c["l1"]}<br><span class="l2">{c["l2"]}</span><span class="dot"></span></div>
<div class="p1" style="margin-top:26px;max-width:760px">{c["text"]}</div></div>
<div style="position:relative;height:620px"><div class="a" style="left:20px;top:150px;transform:rotate(-7deg)"><div class="card" style="width:340px;height:425px"><div style="transform:scale(.85)">{c.get("visual_back","")}</div></div></div>
<div class="a" style="right:30px;top:0;transform:rotate(5deg)"><div class="card" style="width:480px;height:600px"><div style="transform:scale(1.2)">{c["visual"]}</div></div></div></div></div>''')
for k, t in enumerate(spec['tips'], 1):
    def mk(t=t, k=k):
        return lambda d,i,T: f'''<div style="{COL}"><div><div class="num">{k:02d}.</div>
<div class="h1" style="margin-top:10px">{t["title1"]}<br><span class="l2">{t["title2"]}</span><span class="dot"></span></div>
<div class="p1" style="margin-top:22px">{t["problem"]}</div><div class="p2" style="margin-top:10px">{t["fix"]}</div></div>
<div style="display:flex;justify-content:space-between;align-items:flex-end">
 <div><div class="card" style="width:400px;height:500px;filter:saturate(.85)"><div style="transform:none">{t["before"]}</div></div><div style="display:flex;gap:14px;align-items:center;margin-top:20px"><span class="pill" style="background:{"rgba(255,255,255,.12)" if d else "#e3e7ee"};color:{"#fff" if d else "#55607a"}">Before</span><span class="note">{t["before_note"]}</span></div></div>
 <div><div class="card" style="width:484px;height:605px;box-shadow:0 26px 60px rgba(1,15,33,.32)"><div style="transform:scale(1.21)">{t["after"]}</div></div><div style="display:flex;gap:14px;align-items:center;margin-top:20px"><span class="pill" style="background:#FFC107;color:#022452">After</span><span class="note">{t["after_note"]}</span></div></div>
</div></div>'''
    slides.append(mk())
r = spec['recap']
ico = ''.join(f'<div style="display:flex;align-items:center;gap:24px;padding:26px 0;border-bottom:1.5px solid rgba(127,140,160,.25)"><span style="width:60px;height:60px;border-radius:50%;background:#FFC107;color:#022452;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:24px;flex:none">{j:02d}</span><span style="font-weight:700;font-size:40px">{it}</span></div>' for j, it in enumerate(r['items'], 1))
slides.append(lambda d,i,T: f'''<div style="{COL}"><div class="h1" style="font-size:88px">{r["l1"]}<br><span class="l2">{r["l2"]}</span><span class="dot"></span></div>
<div>{ico}</div>
<div style="display:flex;align-items:center;gap:22px"><svg viewBox="0 0 24 24" width="56" height="56"><path d="M6 3h12v18l-6-4-6 4z" fill="none" stroke="currentColor" stroke-width="2"/></svg><span class="p1" style="font-size:34px">Save this for your next design.</span></div></div>''')
ct = spec['cta']
ic = lambda k: f'<span style="width:52px;height:52px;border-radius:50%;background:#FFC107;display:inline-flex;align-items:center;justify-content:center"><svg viewBox="0 0 24 24" width="28" height="28" style="color:#022452">{IC[k]}</svg></span>'
slides.append(lambda d,i,T: f'''<div style="{COL}"><div><div class="h1" style="font-size:112px">{ct["l1"]}<br><span class="l2">{ct["l2"]}</span><span class="dot"></span></div>
<div class="p1" style="margin-top:30px;font-size:34px">{ct["text"]}</div></div>
<div><div style="display:flex;align-items:center;justify-content:space-between;background:{"#FFC107" if d else "#022452"};border-radius:70px;padding:30px 34px 30px 50px;color:{"#022452" if d else "#fff"}">
<span style="font-weight:800;font-size:34px">Book DANAG STUDIO</span><span style="font-weight:700;font-size:32px">+233 (0)50 332 0548</span></div>
<div style="margin-top:40px;display:flex;align-items:center;gap:12px;font-weight:600;font-size:30px">{ic("IG")}{ic("TT")}{ic("X")}<span style="margin-left:12px">@thedanagstudio</span></div></div></div>''')
T = len(slides); assert T <= 10
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
    for i, fn in enumerate(slides, 1):
        d = (i % 2 == 0) != (spec.get('start') == 'navy')
        html = f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s {"n" if d else "w"}">{mark(d)}{"" if d else GLOW}<div class="gr"></div>{head(d,i,T)}{fn(d,i,T)}{foot(d, i==T)}</div></body></html>'
        p = out / f'{i:02d}.html'; p.write_text(html); pg.goto(p.as_uri()); pg.wait_for_timeout(700)
        pg.screenshot(path=str(out / f'{i:02d}.png'))
        im = Image.open(out / f'{i:02d}.png').convert('RGB'); im.save(out / f'{i:02d}.jpg', quality=95, subsampling=0)
        im.resize((1080, 1350), Image.LANCZOS).save(out / f'{i:02d}-1080.jpg', quality=95, subsampling=0)
        (out / f'{i:02d}.png').unlink(); p.unlink()
    b.close()
print('slides', T)
