"""Hero promos laid out after their samples (2026-11-14b refs 03,05,06,02). Navy, no glow, full-bleed photos.
Usage: python3 promo/render_layouts.py KEY...   (P8 P9 P10 P11)"""
import sys, os, re, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image
P = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(P); B = f'{R}/book-flyer'
sys.path.insert(0, B)
from contacts import IC
F = f'{R}/fonts/'; G = '#FFC107'; N = '#022452'; A = f'{R}/assets-hero'
logo = lambda h=56: re.sub(r'<\?xml[^>]*>', '', open(f'{B}/logo-on-navy.svg').read()).replace('<svg', f'<svg style="height:{h}px;width:auto;display:block"', 1)
ic = lambda k, c, s=18: f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" style="color:{c};flex:none">{IC[k]}</svg>'
circ = lambda k: f'<span style="width:36px;height:36px;border-radius:50%;background:{G if k=="PH" else "rgba(255,255,255,.12)"};display:inline-flex;align-items:center;justify-content:center">{ic(k, N if k=="PH" else "#fff")}</span>'
FOOT = f'''<div class="a" style="left:90px;right:90px;bottom:70px;display:flex;align-items:center;justify-content:space-between;font-weight:700;font-size:23px;z-index:9">
 <div style="display:flex;align-items:center;gap:12px">{circ('PH')}<span style="font-weight:900;font-size:30px">+233 (0)50 332 0548</span></div>
 <div style="display:flex;align-items:center;gap:8px">{circ('IG')}{circ('TT')}{circ('X')}<span style="margin-left:4px">@thedanagstudio</span></div></div>'''
DOT = f'<span style="display:inline-block;width:.236em;height:.236em;border-radius:50%;background:{G};margin-left:.04em"></span>'
def photo(f, pos='center/cover'): return f'<div class="a" style="inset:0;background:url({pathlib.Path(f"{A}/{f}").as_uri()}) {pos}"></div>'
D = {}
D['P9'] = '<div class="a" style="inset:0;background:radial-gradient(ellipse at 50% 52%,#051528,#060f1f 90%)"></div>' + photo('P9.jpg', 'center 52%/82% auto no-repeat;-webkit-mask-image:radial-gradient(ellipse 40% 40% at 50% 52%,#000 60%,transparent 100%)') + f'''
<div class="a" style="left:0;right:0;top:84px;display:flex;justify-content:center">{logo(60)}</div>
<div class="a" style="left:40px;width:360px;top:330px;text-align:center;line-height:1">
 <div style="font-weight:500;font-size:54px">Time to</div>
 <div style="font-weight:900;font-size:80px;color:{G};letter-spacing:-2px;margin-top:10px">POWER</div>
 <div style="font-weight:900;font-size:80px;color:{G};letter-spacing:-2px">UP</div></div>
<div class="a" style="right:40px;width:380px;top:840px;text-align:center;line-height:1.02">
 <div style="font-weight:500;font-size:56px">YOUR</div>
 <div style="font-weight:900;font-size:84px;color:{G};letter-spacing:-2px">BRAND</div>
 <div style="font-weight:500;font-size:52px;letter-spacing:-1px">PRESENCE{DOT}</div></div>
<div class="a" style="left:0;right:0;bottom:0;height:260px;background:linear-gradient(180deg,transparent,rgba(1,12,28,.9))"></div>''' + FOOT
D['P8'] = photo('P8.jpg', 'center top/112% auto') + f'''
<div class="a" style="left:0;right:0;bottom:0;height:300px;background:linear-gradient(180deg,transparent,rgba(1,12,28,.95) 70%)"></div>
<div class="a" style="left:90px;right:90px;top:84px;display:flex;align-items:center;justify-content:space-between;padding-bottom:22px;border-bottom:2px solid {G}">{logo(54)}<div style="font-weight:900;font-size:30px;color:{G}">@thedanagstudio</div></div>
<div class="a" style="left:560px;right:90px;top:330px;padding:44px 42px 48px;border-radius:34px;border:1.5px solid rgba(255,255,255,.28);background:rgba(4,20,48,.38);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px)">
 <svg width="46" height="46" viewBox="0 0 24 24" fill="none" stroke="{G}" stroke-width="3" stroke-linecap="round"><path d="M5 5L19 19M19 8V19H8"/></svg>
 <div style="font-weight:500;font-size:46px;line-height:1.18;margin-top:22px">Unseen brands are easily forgotten...</div>
 <div style="font-weight:900;font-size:46px;line-height:1.15;color:{G};margin-top:30px">Stand out, and the spotlight is yours{DOT}</div></div>''' + FOOT
D['P10'] = photo('P10.jpg') + f'''
<div class="a" style="left:90px;top:80px">{logo(54)}</div>
<div class="a" style="left:0;right:0;top:168px;text-align:center;line-height:1.16">
 <div style="font-weight:500;font-size:54px;color:{G}">Your <b style="font-weight:900;color:#fff">Brand</b> can carry</div>
 <div style="font-weight:500;font-size:54px;color:{G}">more than you think{DOT}</div>
 <svg width="440" height="30" viewBox="0 0 440 30" style="display:block;margin:6px 0 0 520px"><path d="M6 18 C120 6 300 4 434 10 M60 26 C170 18 300 16 400 20" fill="none" stroke="{G}" stroke-width="5" stroke-linecap="round"/></svg></div>
<div class="a" style="left:0;right:0;top:965px;text-align:center;font-weight:900;font-size:50px;line-height:1.02;color:#5a3d00;mix-blend-mode:multiply;text-shadow:0 1px 0 rgba(255,230,160,.6)">Your<br>Brand</div>
<div class="a" style="left:0;right:0;bottom:56px;display:flex;justify-content:center"><div style="border:2px solid {G};background:rgba(255,193,7,.12);border-radius:40px;padding:14px 34px;font-weight:900;font-size:28px">Let's talk: <span style="color:{G}">+233 (0)50 332 0548</span></div></div>'''
D['P11'] = photo('P11-sharp.jpg') + f'''
<div class="a" style="left:0;right:0;top:70px;display:flex;justify-content:center">{logo(58)}</div>
<div class="a" style="left:90px;top:175px;line-height:1.04">
 <div style="font-weight:900;font-size:110px;color:{G};height:62px;line-height:1">&ldquo;</div>
 <div style="font-weight:500;font-size:62px;letter-spacing:-1.5px">Your Ideas</div>
 <div style="font-weight:500;font-size:62px;letter-spacing:-1.5px;color:#c9d3e6">Our Craft</div>
 <div style="font-weight:900;font-size:62px;letter-spacing:-1.5px;color:{G}">Real Results{DOT}</div>
 <div style="font-weight:500;font-size:24px;line-height:1.4;margin-top:22px;width:270px;color:#dfe5f1">Good looks are the start. We design brands people trust and remember.</div></div>
<div class="a" style="right:90px;top:900px;text-align:right;line-height:1.02">
 <div style="font-weight:500;font-size:66px;letter-spacing:-1.5px">Big Ideas.</div>
 <div style="font-weight:500;font-size:66px;letter-spacing:-1.5px;color:#c9d3e6">Bold Designs.</div>
 <div style="font-weight:900;font-size:76px;letter-spacing:-2px;color:{G}">Real Impact{DOT}</div>
 <div style="height:4px;width:260px;background:{G};margin:10px 0 0 auto;border-radius:3px"></div></div>''' + FOOT
CSS = f"""@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}
@font-face{{font-family:M;font-weight:600;src:url({F}montserrat-latin-600-normal.woff2)}}
@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}
@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}} body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;color:#fff;background:#011631}} .a{{position:absolute}}"""
GR = f'<div class="a" style="inset:0;z-index:50;pointer-events:none;opacity:.14;mix-blend-mode:overlay;background-size:256px;background-image:url({R}/grain.png)"></div>'
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
    for k in sys.argv[1:]:
        t = f'/tmp/_lay{k}.html'; open(t, 'w').write(f'<html><head><style>{CSS}</style></head><body>{D[k]}{GR}<script>document.fonts.ready.then(()=>document.body.dataset.done=1)</script></body></html>')
        pg.goto(pathlib.Path(t).as_uri()); pg.wait_for_selector('body[data-done]'); pg.wait_for_timeout(300); pg.screenshot(path='/tmp/_lay.png')
        im = Image.open('/tmp/_lay.png').convert('RGB'); im.save(f'{R}/promo/hero-{k}.jpg', quality=93, subsampling=0)
        im.resize((1080, 1350), Image.LANCZOS).save(f'{R}/promo/hero-{k}-1080.jpg', quality=93); print('ok', k)
    b.close()
