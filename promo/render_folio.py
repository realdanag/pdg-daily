"""DANAG STUDIO portfolio carousel, "tabbed" style (guide: Danag's Khamp Studio references, 2026-11-11).
Usage: python3 promo/render_folio.py OUTDIR   -> OUTDIR/NN.jpg (2160x2700) + NN-1080.jpg
Slides alternate white / navy. Each slide: tab bar (active tab highlighted), big two-line headline
(Montserrat line + Gobold line with gradient and stem-thick dot), content, faint work collage and a footer
with the logo (once) and contact pill. No glow on navy; soft gold glow top-left on white; light grain.
"""
import sys, os, re, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image
P = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(P); B = f'{R}/book-flyer'; A = f'{R}/portfolio/src/assets'
sys.path.insert(0, B)
import render_book as rb
from contacts import IC
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
PORTRAIT = '/home/claude/assets/danag-portrait.jpg'
GOLD = '#FFC107'; F = f'{R}/fonts/'
NAVYG = 'linear-gradient(135deg,#032F65 0%,#022452 45%,#011631 80%,#010F21 100%)'
TABS = ['COVER', 'ABOUT ME', 'MY WORK', 'CLIENTS', 'CONTACT']
u = lambda n: pathlib.Path(f'{A}/{n}.jpg').as_uri()
ic = lambda k, c, s=22: f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" style="color:{c};flex:none">{IC[k]}</svg>'
COLLAGE = ['my-beast-nj', 'ss-084', 'my-dallas', 'tf-gmg-red', 'fl-ss-open', 'my-066', 'my-xmas', 'wk-011', 'ss-student', 'my-exclyusif']


def logo(dark, h=46):
    s = re.sub(r'<\?xml[^>]*>', '', open(f'{B}/logo-on-{"navy" if dark else "white"}.svg').read())
    return s.replace('<svg', f'<svg style="height:{h}px;width:auto;display:block"', 1)


def head(l1, l2, dark, maxw=880, cap=200, align='left'):
    c = rb.fit(l2, maxw, cap, True)
    g = rb.line(l2, c, GOLD if dark else '#022452', True, dot_color='#fff' if dark else GOLD)
    return (f'<div style="text-align:{align}"><div style="font-weight:900;font-size:84px;letter-spacing:-3px;line-height:1">{l1}</div>'
            f'<div style="margin-top:20px;display:inline-block">{g}</div></div>')


def frame(i, dark, body):
    ink = '#fff' if dark else '#022452'
    tabs = ''.join(
        (f'<span style="padding:12px 22px;border-radius:12px;background:{GOLD if dark else NAVYG};color:{"#022452" if dark else "#fff"};box-shadow:0 10px 22px rgba(1,15,33,.22)">{t}</span>'
         if k == i else f'<span style="padding:12px 4px;opacity:.75">{t}</span>') for k, t in enumerate(TABS))
    tiles = ''.join(f'<div style="background:url({u(n)}) center/cover;border-radius:10px"></div>' for n in COLLAGE)
    fade = ('linear-gradient(180deg,#022452 0%,rgba(2,36,82,.86) 40%,rgba(2,36,82,.80) 100%)' if dark
            else 'linear-gradient(180deg,#f1f3f8 0%,rgba(241,243,248,.88) 40%,rgba(241,243,248,.82) 100%)')
    pill_bg = GOLD if dark else NAVYG; pill_fg = '#022452' if dark else '#fff'; icc = '#022452' if dark else GOLD
    glow = '' if dark else '<div class="a" style="width:680px;height:680px;left:-340px;top:-320px;border-radius:50%;filter:blur(30px);background:radial-gradient(circle,rgba(255,193,7,.24) 0%,transparent 62%)"></div>'
    return f"""<html><head><style>
@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}
@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}
@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
@font-face{{font-family:SC;src:url({F}sacramento-latin-400-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;color:{ink};background:{NAVYG if dark else 'linear-gradient(180deg,#ffffff 0%,#eef1f6 100%)'}}}
.a{{position:absolute}}
.card{{border-radius:22px;overflow:hidden;box-shadow:0 18px 40px rgba(1,15,33,{'.45' if dark else '.18'});border:3px solid {GOLD if dark else '#022452'}}}
</style></head><body>{glow}
<svg class="a" viewBox="252 255 749 664" style="right:-230px;top:330px;width:720px;opacity:{'.05' if dark else '.04'}"><path fill="{ink}" fill-rule="evenodd" d="{rb.MK['nodot']}"/><path fill="{ink}" d="{rb.MK['dot']}"/></svg>
<div class="a" style="left:0;right:0;top:66px;display:flex;justify-content:center;gap:34px;font-weight:700;font-size:19px;letter-spacing:1px">{tabs}</div>
<div class="a" style="left:-20px;right:-20px;bottom:-60px;height:330px;display:grid;grid-template-columns:repeat(5,1fr);grid-template-rows:1fr 1fr;gap:14px;opacity:.5;filter:grayscale(.6)">{tiles}</div>
<div class="a" style="left:0;right:0;bottom:0;height:330px;background:{fade}"></div>
<div class="a" style="left:0;right:0;top:140px;bottom:170px;display:flex;flex-direction:column;justify-content:space-evenly;padding:0 84px">{body}</div>
<div class="a" style="left:84px;right:84px;bottom:70px;display:flex;align-items:center;justify-content:space-between">
 <div style="display:flex;align-items:center;gap:16px">{logo(dark, 50)}</div>
 <div style="display:flex;align-items:center;gap:12px;background:{pill_bg};color:{pill_fg};height:62px;padding:0 24px;border-radius:40px;font-weight:700;font-size:18px;white-space:nowrap;box-shadow:0 14px 30px rgba(1,15,33,.25)">
  {ic('PH', icc)}+233 (0)50 332 0548<span style="width:2px;height:28px;background:currentColor;opacity:.3;margin:0 6px"></span>{ic('IG', icc)}{ic('TT', icc)}{ic('X', icc)}@thedanagstudio</div>
</div>
<div class="a" style="inset:0;z-index:50;pointer-events:none;opacity:{'.16' if dark else '.12'};mix-blend-mode:{'overlay' if dark else 'multiply'};background-size:256px;background-image:url({R}/grain.png)"></div>
</body></html>"""


def grid(names, dark):
    if len(names) == 3:
        return ('<div style="display:flex;gap:24px;justify-content:center">' + ''.join(f'<div class="card" style="width:288px;height:360px;background:url({u(n)}) center/cover"></div>' for n in names) + '</div>')
    a, b2, c, d = names
    cd = lambda n, w, h: f'<div class="card" style="width:{w}px;height:{h}px;background:url({u(n)}) center/cover"></div>'
    return (f'<div style="display:flex;gap:22px;justify-content:center;align-items:flex-start">{cd(a, 400, 500)}'
            f'<div style="display:flex;flex-direction:column;gap:22px">{cd(b2, 230, 239)}{cd(c, 230, 239)}</div>{cd(d, 230, 500)}</div>')


def work(i, dark, kick, l1, l2, text, names, **kw):
    sub = f'<div style="font-weight:900;font-size:22px;letter-spacing:6px;color:{GOLD if dark else "#b38600"};margin-bottom:18px">{kick}</div>'
    top = (f'<div style="display:flex;align-items:flex-end;gap:36px"><div>{sub}{head(l1, l2, dark, maxw=520, cap=170)}</div>'
           f'<div style="border-left:3px solid {GOLD};padding-left:24px;font-weight:500;font-size:24px;line-height:1.45;max-width:340px;margin-bottom:10px;opacity:.85">{text}</div></div>')
    return frame(i, dark, top + grid(names, dark, **kw))


SL = []
# 1 cover (white)
SL.append(frame(0, False, f"""<div style="text-align:center;display:flex;flex-direction:column;align-items:center">
 <div style="font-weight:900;font-size:30px;letter-spacing:14px;color:#b38600">DANAG STUDIO</div>
 <div style="margin-top:26px">{rb.line('PORTFOLIO', rb.fit('PORTFOLIO', 900, 330, True), '#022452', True, dot_color=GOLD)}</div>
 <svg viewBox="0 0 600 60" width="520" style="margin-top:34px"><path d="M10 40 C120 10 300 8 590 22 C420 30 260 34 120 50" fill="none" stroke="{GOLD}" stroke-width="6" stroke-linecap="round"/></svg>
 <div style="margin-top:30px;font-weight:500;font-size:30px;color:#4d5870">Graphic design, product visuals, social media and websites.<br><b style="font-weight:900;color:#022452">Selected work, 2025 to 2026.</b></div>
</div>"""))
# 2 about (navy)
about = ("I'm Danag, the designer behind DANAG STUDIO, a graphic design studio in Accra, Ghana.",
         "I design flyers and posters, product visuals, social media content, brochures, business cards and websites, and I work closely with brand founders, especially in luxury fragrance and fashion.",
         "My aim is simple: design that looks premium, says one clear thing, and gets people to act.",
         "Crowned in craft. That's how I create.")
paras = ''.join(f'<p style="margin-top:{0 if k == 0 else 22}px">{t}</p>' for k, t in enumerate(about))
SL.append(frame(1, True, f"""<div style="display:flex;align-items:center;gap:44px">
 <div style="flex:1">{head('Who is', 'DANAG STUDIO?'.replace('?', ''), True, maxw=520, cap=170)}
  <div style="margin-top:34px;font-weight:500;font-size:24px;line-height:1.5;color:rgba(255,255,255,.82)">{paras}</div></div>
 <div style="width:330px;flex:none">
  <div class="card" style="height:470px;background:url({pathlib.Path(PORTRAIT).as_uri()}) center 18%/cover no-repeat"></div>
  <div style="margin-top:-30px;position:relative;margin-left:30px;margin-right:30px;background:{GOLD};color:#022452;border-radius:16px;padding:16px 0;text-align:center;font-weight:900;font-size:26px">Danag &#183; Founder</div>
 </div></div>"""))
# 3-6 work
SL.append(work(2, False, 'MY WORK · 01', 'Product', 'VISUALS', 'Campaign images for luxury perfume brands, made to stop the scroll.', ['ss-084', 'my-066', 'ss-076', 'wk-011']))
SL.append(work(2, True, 'MY WORK · 02', 'Flyers &amp;', 'CAMPAIGNS', 'Launches, sales, exhibitions and store openings that got people talking.', ['my-beast-nj', 'my-dallas', 'my-xmas']))
SL.append(work(2, False, 'MY WORK · 03', 'Fashion', 'LOOKBOOKS', 'On-location campaign visuals at Ghanaian landmarks and in the studio.', ['tf-gmg-red', 'tf-barrel-front', 'tf-faces-portrait', 'tf-wig-navy']))
web = f"""<div style="display:flex;flex-direction:column;gap:30px;align-items:center">""" + ''.join(
    f"""<div style="display:flex;align-items:flex-end;gap:-30px;position:relative;width:900px;height:250px">
  <div class="card" style="width:720px;height:250px;background:url({u(d)}) top/cover"></div>
  <div class="card" style="position:absolute;right:0;bottom:-18px;width:126px;height:262px;border-radius:22px;background:url({u(m)}) top/cover;border-width:5px"></div>
  <div style="position:absolute;left:24px;bottom:18px;background:{GOLD};color:#022452;font-weight:900;font-size:18px;padding:8px 16px;border-radius:20px">{t}</div></div>"""
    for d, m, t in [('web-ss-desktop', 'web-ss-mobile', 'scentxspice.com'), ('web-cc-desktop', 'web-cc-mobile', 'careercaptains.org')]) + '</div>'
SL.append(frame(2, True, f"""<div style="display:flex;align-items:flex-end;gap:36px"><div><div style="font-weight:900;font-size:22px;letter-spacing:6px;color:{GOLD};margin-bottom:18px">MY WORK · 04</div>{head('Website', 'DESIGN', True, maxw=520, cap=170)}</div>
<div style="border-left:3px solid {GOLD};padding-left:24px;font-weight:500;font-size:24px;line-height:1.45;max-width:340px;margin-bottom:10px;opacity:.85">Custom websites built for desktop and mobile, new to the studio.</div></div>{web}"""))
# clients (white): real chat screenshots, names covered
RV = '/home/claude/assets/reviews'
rv = lambda n, w: f'<img src="{pathlib.Path(f"{RV}/{n}.jpg").as_uri()}" style="width:{w}px;display:block;border-radius:18px;border:3px solid #022452;box-shadow:0 16px 34px rgba(1,15,33,.2)">'
SL.append(frame(3, False, f"""<div style="display:flex;align-items:flex-end;gap:36px"><div><div style="font-weight:900;font-size:22px;letter-spacing:6px;color:#b38600;margin-bottom:18px">CLIENTS · IN THEIR WORDS</div>{head("Clients'", 'REVIEWS', False, maxw=470, cap=170)}</div>
<div style="border-left:3px solid {GOLD};padding-left:24px;font-weight:500;font-size:23px;line-height:1.45;max-width:360px;margin-bottom:10px;color:#4d5870">Real messages from clients after their work was delivered.</div></div>
<div style="display:flex;gap:22px;justify-content:center;align-items:flex-start">
 <div style="display:flex;flex-direction:column;gap:20px">{rv('r1', 340)}{rv('r2', 340)}</div>
 <div style="display:flex;flex-direction:column;gap:20px">{rv('r4', 340)}{rv('r3', 340)}</div></div>"""))
# clients (navy): kind words
q = lambda t, n: (f'<div style="background:rgba(255,255,255,.06);border:2px solid rgba(255,193,7,.55);border-radius:26px;padding:40px 44px">'
                  f'<div style="font-family:Georgia,serif;font-size:110px;line-height:.6;color:{GOLD}">&ldquo;</div>'
                  f'<div style="font-weight:700;font-size:34px;line-height:1.4;margin-top:6px">{t}</div>'
                  f'<div style="margin-top:22px;font-weight:900;font-size:22px;letter-spacing:3px;color:{GOLD}">{n}</div></div>')
SL.append(frame(3, True, f"""<div style="text-align:left">{head('Kind words', 'FROM CLIENTS', True, maxw=760, cap=170)}</div>
{q("The work is really beautiful and I love the way you were very patient even with all my stubbornness.", "MS. ADELINE")}
{q("I love it, thank you very much.", "MAMLE")}"""))
# contact (white)
svc = ['Flyer &amp; Poster Design', 'Product Visuals', 'Social Media Design', 'Social Media Management', 'Brochure Design', 'Business Card Design', 'Website Design &amp; Redesign']
svc_html = ''.join(f'<div style="display:flex;align-items:center;gap:14px;padding:9px 0"><svg width="18" height="18" viewBox="0 0 10 10"><path d="M1 1 L9 5 L1 9 Z" fill="{GOLD}"/></svg>{s}</div>' for s in svc)
con = [('IG', '@thedanagstudio'), ('TT', '@thedanagstudio'), ('X', '@thedanagstudio'), ('SC', '@realdanag'), ('PH', '+233 (0)50 332 0548')]
con_html = ''.join(f'<div style="display:flex;align-items:center;gap:14px;padding:9px 0">{ic(k, "#022452", 24)}{t}</div>' for k, t in con)
box = lambda title, inner, bg, fg, tbg, tfg: (f'<div style="position:relative;padding-top:28px"><div style="position:absolute;top:0;left:50%;transform:translateX(-50%);background:{tbg};color:{tfg};font-weight:900;font-size:22px;letter-spacing:3px;padding:14px 34px;border-radius:30px;white-space:nowrap">{title}</div>'
                                              f'<div style="background:{bg};color:{fg};border-radius:26px;padding:46px 34px 30px;font-weight:700;font-size:22px;box-shadow:0 18px 40px rgba(1,15,33,.2)">{inner}</div></div>')
SL.append(frame(4, False, f"""<div style="display:flex;justify-content:center">{head("Let's work", 'TOGETHER', False, maxw=760, cap=200, align='center')}</div>
<div style="text-align:center;font-weight:500;font-size:27px;color:#4d5870">You've seen the work. Your brand could be next.</div>
<div style="display:grid;grid-template-columns:1.15fr 1fr;gap:34px">{box('SERVICES', svc_html, NAVYG, '#fff', GOLD, '#022452')}{box('CONTACT', con_html, 'linear-gradient(180deg,#FFD54F,#FFC107 60%,#E3A600)', '#022452', NAVYG, '#fff')}</div>"""))

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
    pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
    for k, h in enumerate(SL, 1):
        t = f'/tmp/_folio{k}.html'; open(t, 'w').write(h); pg.goto(pathlib.Path(t).as_uri()); pg.wait_for_timeout(900)
        pg.evaluate("""()=>{for(const s of document.querySelectorAll('svg.hs')){const bb=s.getBBox();
            s.setAttribute('viewBox',`${bb.x} ${bb.y} ${bb.width} ${bb.height}`);s.setAttribute('width',bb.width);s.setAttribute('height',bb.height)}}""")
        pg.wait_for_timeout(150); pg.screenshot(path='/tmp/_f.png')
        im = Image.open('/tmp/_f.png').convert('RGB'); im.save(f'{OUT}/{k:02d}.jpg', quality=95, subsampling=0)
        im.resize((1080, 1350), Image.LANCZOS).save(f'{OUT}/{k:02d}-1080.jpg', quality=95, subsampling=0)
    b.close()
print('slides', len(SL))
