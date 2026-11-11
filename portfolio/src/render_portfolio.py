"""DANAG STUDIO portfolio carousel (v2, 11 slides).
usage: python3 portfolio/src/render_portfolio.py   -> portfolio/NN.jpg (2160x2700) + NN-1080.jpg
Brand rules: slides alternate white (odd) / navy (even); logo once in the header + faint background mark;
headline line 1 strong, line 2 softer, round gold brand dot; Montserrat; balanced spacing (content area is
vertically balanced between header and footer, the image grid fills the rest with no dead space)."""
import json, pathlib, re
from playwright.sync_api import sync_playwright
from PIL import Image
S = pathlib.Path(__file__).resolve().parent; P = S.parent; R = P.parent; F = R / 'fonts'; A = S / 'assets'
MK = json.load(open(R / 'edu-kit' / 'mark.json')); IC = json.load(open(R / 'book-flyer' / 'icons.json'))
logo_w = (R / 'book-flyer' / 'logo-on-white.svg').read_text(); logo_n = (R / 'book-flyer' / 'logo-on-navy.svg').read_text()
def lg(dark, h): s = re.sub(r'<\?xml[^>]*>', '', logo_n if dark else logo_w); return s.replace('<svg', f'<svg style="height:{h}px;width:auto;display:block"', 1)
def img(name): return (A / f'{name}.jpg').as_uri()
CSS = f'''@font-face{{font-family:M;font-weight:500;src:url({(F/"montserrat-latin-500-normal.woff2").as_uri()})}}
@font-face{{font-family:M;font-weight:600;src:url({(F/"montserrat-latin-600-normal.woff2").as_uri()})}}
@font-face{{font-family:M;font-weight:700;src:url({(F/"montserrat-latin-700-normal.woff2").as_uri()})}}
@font-face{{font-family:M;font-weight:900;src:url({(F/"montserrat-latin-900-normal.woff2").as_uri()})}}
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;font-family:M}}
.s{{position:relative;width:1080px;height:1350px;overflow:hidden}}.a{{position:absolute}}
.w{{background:linear-gradient(180deg,#ffffff,#eef1f6);color:#022452}}
.n{{background:linear-gradient(135deg,#032F65 0%,#022452 45%,#011631 80%,#010F21 100%);color:#fff}}
.hd{{position:absolute;left:84px;right:84px;top:64px;display:flex;justify-content:space-between;align-items:center;font-weight:700;font-size:17px;letter-spacing:4px}}
.hd .pg{{opacity:.55}}
.col{{position:absolute;left:84px;right:84px;top:142px;bottom:128px;display:flex;flex-direction:column}}
.kick{{font-weight:900;font-size:20px;letter-spacing:6px}} .w .kick{{color:#b38600}} .n .kick{{color:#FFC107}}
.h1{{font-weight:900;font-size:76px;line-height:1.02;letter-spacing:-2.5px;margin-top:16px}}
.w .h1 .l2{{color:#7d879a}} .n .h1 .l2{{color:#9fb0cc}}
.dot{{display:inline-block;width:.2em;height:.2em;border-radius:50%;background:#FFC107;margin-left:.04em}}
.p1{{font-weight:500;font-size:26px;line-height:1.42;margin-top:20px;max-width:880px}} .w .p1{{color:#6b7488}} .n .p1{{color:rgba(255,255,255,.7)}}
.grid{{flex:1;min-height:0;margin-top:34px;position:relative}}
.c{{border-radius:26px;overflow:hidden;box-shadow:0 18px 40px rgba(1,15,33,.18);background:#dfe4ec}}
.n .c{{box-shadow:0 22px 50px rgba(0,0,0,.4);background:#0b2347}}
.c img{{width:100%;height:100%;object-fit:cover;display:block}}
.ft{{position:absolute;left:84px;right:84px;bottom:52px;display:flex;justify-content:space-between;font-weight:600;font-size:18px;opacity:.6}}'''
def mark(dark): return f'<svg class="a" viewBox="252 255 749 664" style="right:-230px;bottom:-80px;width:780px;opacity:{.05 if dark else .045}"><path fill="{"#fff" if dark else "#022452"}" fill-rule="evenodd" d="{MK["nodot"]}"/><path fill="{"#fff" if dark else "#022452"}" d="{MK["dot"]}"/></svg>'
def card(name, style, pos='50% 50%'): return f'<div class="c a" style="{style}"><img src="{img(name)}" style="object-position:{pos}"></div>'
def text(k, l1, l2, p): return f'<div class="kick">{k}</div><div class="h1">{l1}<br><span class="l2">{l2}</span><span class="dot"></span></div><div class="p1">{p}</div>'
# Grid helpers. The grid box is 912 wide; its height is measured in the page (var H) and laid out by JS so that
# every grid fills its area exactly (balanced spacing, no dead space under images).
def trio(a, b, c, pa='50% 50%', pb='50% 50%', pc='50% 50%'):  # tall left + two stacked right (v1 layout)
    return f'''<div class="grid" data-l="trio">{card(a,"left:0;top:0;width:497px;height:100%",pa)}
{card(b,"left:515px;top:0;width:397px;height:calc(50% - 9px)",pb)}{card(c,"left:515px;bottom:0;width:397px;height:calc(50% - 9px)",pc)}</div>'''
def quad(items):  # 2x2, cover
    pos = ['left:0;top:0', 'right:0;top:0', 'left:0;bottom:0', 'right:0;bottom:0']
    return '<div class="grid">' + ''.join(card(n, f'{pos[i]};width:447px;height:calc(50% - 9px)', p) for i, (n, p) in enumerate(items)) + '</div>'
def fit(items):  # 2x2 cells, each design shown whole at its own aspect ratio, centred in its cell
    cells = ''.join(f'<div style="display:flex;align-items:center;justify-content:center;min-height:0;min-width:0"><div class="c" style="height:100%;aspect-ratio:{r}"><img src="{img(n)}"></div></div>' for n, r in items)
    return f'<div class="grid" style="display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:18px">{cells}</div>'
def rows(spec):  # rows of whole designs; spec = [[(name, aspect), ...], ...]; JS sizes rows so each row spans 912 and the stack is centred
    out = ''.join('<div class="row" style="display:flex;gap:18px;justify-content:center">' + ''.join(f'<div class="c" data-r="{r}"><img src="{img(n)}"></div>' for n, r in row) + '</div>' for row in spec)
    return f'<div class="grid" data-l="rows" style="display:flex;flex-direction:column;justify-content:center;gap:18px">{out}</div>'
JS = '''document.querySelectorAll('[data-l=rows]').forEach(g=>{const H=g.clientHeight,W=g.clientWidth,rs=[...g.children];
 let hs=rs.map(r=>{const c=[...r.children],s=c.reduce((t,e)=>t+ +e.dataset.r,0);return (W-18*(c.length-1))/s});
 const tot=hs.reduce((a,b)=>a+b,0)+18*(rs.length-1); if(tot>H){const k=(H-18*(rs.length-1))/hs.reduce((a,b)=>a+b,0);hs=hs.map(h=>h*k)}
 rs.forEach((r,i)=>[...r.children].forEach(e=>{e.style.height=hs[i]+'px';e.style.width=hs[i]*e.dataset.r+'px'}))});'''
def device(desk, mob, url, flip):
    b = f'''<div class="c" style="flex:1;min-width:0;height:100%;display:flex;flex-direction:column;background:#fff;border-radius:18px">
<div style="height:34px;flex:none;background:#e9edf3;display:flex;align-items:center;padding:0 14px;gap:7px">
<span style="width:10px;height:10px;border-radius:50%;background:#ff5f57"></span><span style="width:10px;height:10px;border-radius:50%;background:#febc2e"></span><span style="width:10px;height:10px;border-radius:50%;background:#28c840"></span>
<span style="margin-left:14px;flex:1;height:20px;border-radius:10px;background:#fff;font:600 12px M;color:#55607a;display:flex;align-items:center;padding-left:12px;letter-spacing:.3px">{url}</span></div>
<div style="flex:1;min-height:0"><img src="{img(desk)}" style="width:100%;height:100%;object-fit:cover;object-position:50% 0"></div></div>'''
    p = f'''<div class="c" style="height:100%;aspect-ratio:.49;border-radius:30px;padding:9px;background:#0d1117;flex:none">
<div style="width:100%;height:100%;border-radius:22px;overflow:hidden"><img src="{img(mob)}" style="width:100%;height:100%;object-fit:cover;object-position:50% 0"></div></div>'''
    return f'<div style="flex:1;min-height:0;display:flex;gap:24px;justify-content:{"flex-end" if flip else "flex-start"}">{(p+b) if flip else (b+p)}</div>'
def cta(d):
    ic = lambda k: f'<span style="width:52px;height:52px;border-radius:50%;background:#FFC107;display:inline-flex;align-items:center;justify-content:center"><svg viewBox="0 0 24 24" width="28" height="28" style="color:#022452">{IC[k]}</svg></span>'
    return f'''<div style="flex:1;display:flex;flex-direction:column;justify-content:space-evenly">
<div><div class="kick">LET'S WORK TOGETHER</div><div class="h1" style="font-size:112px;margin-top:22px">Your brand<br><span class="l2">could be next</span><span class="dot"></span></div>
<div class="p1" style="font-size:34px;margin-top:30px">Flyers, product visuals, social media, packaging and websites.</div></div>
<div><div style="display:flex;align-items:center;justify-content:space-between;background:{"#FFC107" if d else "#022452"};border-radius:70px;padding:30px 34px 30px 50px;color:{"#022452" if d else "#fff"}">
<span style="font-weight:900;font-size:34px">Book DANAG STUDIO</span><span style="font-weight:700;font-size:32px">+233 (0)50 332 0548</span></div>
<div style="margin-top:40px;display:flex;align-items:center;gap:12px;font-weight:600;font-size:30px">{ic("IG")}{ic("X")}<span style="margin-left:12px">@thedanagstudio</span></div></div></div>'''
SL = [
 lambda d: text('SELECTED WORK · 2025–2026', 'Work that', 'wears the crown', 'A few favourite projects from DANAG STUDIO, from luxury fragrance and fashion to flyers, packaging and websites.')
           + trio('my-horse', 'tf-castle', 'my-leather', pc='50% 55%'),
 lambda d: text('PRODUCT VISUALS · MAISON YUSIF FRAGRANCE', 'Luxury perfume,', 'made cinematic', 'Campaign visuals that make every bottle feel like a story.')
           + trio('my-specials-img', 'my-badinfluence', 'my-vatican', pa='50% 60%'),
 lambda d: text('CAMPAIGNS · MAISON YUSIF FRAGRANCE', 'Stores, shows', 'and exhibitions', 'Posters and flyers for Paris Perfume Week, a US fragrance exhibition and a new store opening.')
           + '<div class="grid" style="display:flex;align-items:center;justify-content:center;gap:18px">' + card('my-paris', 'position:relative;width:592px;height:751px')
           + '<div style="display:flex;flex-direction:column;gap:18px">' + card('my-dallas', 'position:relative;width:293px;height:366px') + card('my-tamale', 'position:relative;width:293px;height:367px', '50% 50%') + '</div></div>',
 lambda d: text('PRODUCT VISUALS · SCENT &amp; SPICE BY GB', 'Every scent,', 'its own mood', 'Editorial portraits and still life for a growing Kumasi perfume brand.')
           + quad([('ss-086', '50% 30%'), ('ss-076', '50% 55%'), ('ss-084', '50% 50%'), ('ss-080', '50% 45%')]),
 lambda d: text('FASHION CAMPAIGN · TREADFIX', 'Ghanaian craft,', 'on location', 'Lookbook and campaign visuals, on location at Ghanaian landmarks and in the studio.')
           + trio('tf-left', 'tf-gmg-red', 'tf-wig-navy', pb='50% 18%', pc='50% 12%'),
 lambda d: text('WATCH VISUALS · CONCEPT WORK', 'Time,', 'beautifully told', 'Personal projects exploring premium watch photography and storytelling.')
           + trio('wk-011', 'cmw-13', 'wk-015', pa='50% 40%', pb='50% 40%', pc='50% 50%'),
 lambda d: text('FLYERS &amp; SOCIAL MEDIA', 'Designs that', 'get the call', 'Promo flyers and social posts for perfume brands, events and churches.')
           + fit([('fl-persian', 1856/2304), ('fl-signature1', .8), ('fl-wealth', .88), ('fl-wss', 1)]),
 lambda d: text('PACKAGING &amp; LABELS', 'Shelf-ready', 'from day one', 'Labels and product packaging that look premium and sell on sight.')
           + '<div class="grid" style="display:flex;align-items:center;justify-content:center;gap:18px">' + card('pk-jeksal', 'position:relative;width:468px;height:585px') + '<div style="display:flex;flex-direction:column;gap:18px">' + card('pk-marmar-shampoo', 'position:relative;width:426px;height:283.5px') + card('pk-mamti', 'position:relative;width:426px;height:283.5px') + '</div></div>',
 lambda d: text('LOGOS &amp; BRAND LAUNCHES', 'Marks made', 'to be remembered', 'Logos and brand marks for new and growing businesses.')
           + rows([[('lg-bea', 2000/1327), ('lg-gc', 1)], [('lg-autoperf', 1.5), ('lg-marmar', 2000/1566)]]),
 lambda d: text('WEBSITE DESIGN', 'Websites that', 'mean business', 'Custom sites for Scent &amp; Spice by GB and CareerCaptains International, built for desktop and mobile.')
           + '<div class="grid" style="display:flex;flex-direction:column;gap:22px">' + device('web-ss-desktop', 'web-ss-mobile', 'scentxspice.com', False) + device('web-cc-desktop', 'web-cc-mobile', 'careercaptains.org', True) + '</div>',
 cta,
]
T = len(SL)
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
    for i, fn in enumerate(SL, 1):
        d = (i % 2 == 0)
        html = f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s {"n" if d else "w"}">{mark(d)}
<div class="hd">{lg(d,40)}<span class="pg">PORTFOLIO · {i:02d}/{T:02d}</span></div><div class="col">{fn(d)}</div>
<div class="ft"><span>@thedanagstudio</span><span>{"Save for later" if i == T else "Swipe &rarr;"}</span></div></div><script>{JS}</script></body></html>'''
        p = S / f'_{i:02d}.html'; p.write_text(html); pg.goto(p.as_uri()); pg.wait_for_timeout(900)
        pg.screenshot(path=str(P / f'{i:02d}.png'))
        im = Image.open(P / f'{i:02d}.png').convert('RGB'); im.save(P / f'{i:02d}.jpg', quality=95, subsampling=0)
        im.resize((1080, 1350), Image.LANCZOS).save(P / f'{i:02d}-1080.jpg', quality=95, subsampling=0)
        (P / f'{i:02d}.png').unlink(); p.unlink()
    b.close()
print('slides', T)
