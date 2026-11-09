"""Render the DANAG STUDIO booking flyer (slide 2 of the DAILY post only).
Usage: python3 book-flyer/render_book.py OUT_BASENAME "EYEBROW" "LINE 1" "BOX LINE"
  e.g. python3 book-flyer/render_book.py book-flyer/daily/2026-11-10 "NEED A DESIGNER?" "MAKE ME YOUR" "DESIGN PLUG"
Writes OUT.jpg (2160x2700) and OUT-1080.jpg.
Headline lines are drawn from Gobold Bold outlines (gobold_bold_outlines.json); the font file is never stored here.
The box line ends with a round white dot (brand mark). Box padding is exactly 40px on all sides of the ink.
Layout, services, colours and footer are fixed: do not edit them.
"""
import sys, json, os, re, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

D = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(D)
G = json.load(open(f'{D}/gobold_bold_outlines.json'))
MK = json.load(open(f'{D}/mark.json'))
IC = json.load(open(f'{D}/icons.json'))


def icons():
    return ''.join(f'<svg viewBox="0 0 24 24" width="24" height="24" style="color:#022452">{IC[k]}</svg>' for k in ('IG', 'TT', 'LI'))


def line(text, cap, color, dot=False, track=0.02):
    s = cap / G['cap']; x = 0; paths = ''
    for ch in text.upper().replace('’', "'"):
        g = G['g'].get(ch) or G['g'][' ']
        paths += f'<path transform="translate({x:.2f},0)" d="{g["d"]}"/>'
        x += g['w'] + track * G['upm']
    x -= track * G['upm']
    w = x * s; extra = ''
    if dot:
        r = cap * 0.085; gap = cap * 0.07
        extra = f'<circle cx="{w + gap + r:.2f}" cy="{cap - r:.2f}" r="{r:.2f}" fill="#fff"/>'
        w += gap + 2 * r
    return (f'<svg class="hs" width="{w:.1f}" height="{cap:.1f}" viewBox="0 0 {w:.1f} {cap:.1f}" style="display:block;overflow:visible">'
            f'<g fill="{color}" transform="translate(0,{cap:.2f}) scale({s:.6f},{-s:.6f})">{paths}</g>{extra}</svg>')


def width(text, cap, dot=False):
    return float(line(text, cap, '#000', dot).split('width="')[1].split('"')[0])


def fit(text, maxw, cap, dot=False):
    while width(text, cap, dot) > maxw and cap > 50:
        cap -= 1
    return cap


def html(eyebrow, l1svg, l2svg):
    F = f'{R}/fonts/'
    logo = open(f'{D}/logo-on-white.svg').read()
    logo = re.sub(r'<\?xml[^>]*>', '', logo).replace('<svg', '<svg style="height:64px;width:auto;display:block"', 1)

    def col(h, items):
        out = f'<div><div class="gh">{h}</div>'
        for i in items:
            st = ' style="color:#b38600"' if i == 'And more' else ''
            out += f'<div class="it"{st}><span class="d"></span>{i}</div>'
        return out + '</div>'
    svc = (col('GRAPHIC DESIGN', ['Flyer &amp; Poster Design', 'Business Card Design', 'Brochure Design', 'Product Visuals'])
           + col('DIGITAL', ['Social Media Management', 'Website Design', 'Website Redesign', 'And more']))
    return f"""<html><head><style>
@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}
@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}
@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
@font-face{{font-family:SC;src:url({F}sacramento-latin-400-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;background:linear-gradient(180deg,#fff 0%,#f1f3f8 100%);color:#022452}}
.a{{position:absolute}}
.ey{{font-weight:900;font-size:24px;letter-spacing:7px;color:#b38600}}
.gh{{font-weight:900;font-size:22px;letter-spacing:5px;color:#b38600;margin-bottom:10px}}
.it{{display:flex;align-items:center;gap:16px;font-weight:700;font-size:27px;height:54px;border-bottom:1.5px solid rgba(2,36,82,.12)}}
.d{{width:12px;height:12px;border-radius:50%;background:#FFC107;flex:none}}
#box{{display:inline-block;background:linear-gradient(135deg,#032F65,#022452 45%,#011631);border-radius:22px;padding:40px}}
</style></head><body>
<svg class="a" viewBox="252 255 749 664" style="right:-300px;top:560px;width:760px;opacity:.045"><path fill="#022452" fill-rule="evenodd" d="{MK['nodot']}"/><path fill="#022452" d="{MK['dot']}"/></svg>
<div class="a" style="left:72px;top:64px">{logo}</div>
<div class="a" style="right:72px;top:80px;display:flex;align-items:center;gap:12px;font-weight:700;font-size:24px">{icons()}<span style="margin-left:4px">realdanag</span></div>
<div class="a" style="left:72px;top:222px"><div class="ey">{eyebrow.upper()}</div>
<div style="margin-top:30px">{l1svg}</div>
<div id="box" style="margin-top:28px">{l2svg}</div>
<div style="font-family:SC;font-size:66px;margin-top:10px">Crowned in Craft</div></div>
<div class="a" style="left:72px;right:72px;top:850px;display:grid;grid-template-columns:1fr 1fr;column-gap:56px">{svc}</div>
<div class="a" style="left:0;right:0;bottom:0;height:210px;background:linear-gradient(135deg,#032F65 0%,#022452 45%,#011631 80%,#010F21 100%)"></div>
<div class="a" style="left:72px;bottom:66px;height:78px;padding:0 44px;border-radius:40px;background:#FFC107;display:flex;align-items:center;font-weight:900;font-size:28px;letter-spacing:3px">BOOK NOW</div>
<div class="a" style="right:72px;bottom:58px;text-align:right;color:#fff"><div style="font-weight:900;font-size:34px">+233 (0)50 332 0548</div><div style="font-weight:500;font-size:22px;opacity:.85;margin-top:8px">realprincedanag@gmail.com &nbsp;|&nbsp; @realdanag</div></div>
</body></html>"""


if __name__ == '__main__':
    out, ey, l1, l2 = sys.argv[1:5]
    c = min(fit(l1, 936, 140), fit(l2, 936 - 80, 140, True))
    h = html(ey, line(l1, c, '#022452'), line(l2, c, '#FFC107', True))
    tmp = '/tmp/_book.html'; open(tmp, 'w').write(h)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
        pg.goto(pathlib.Path(tmp).as_uri()); pg.wait_for_timeout(900)
        # crop each headline svg to its real ink bounds so the box padding is exactly 40 on every side
        pg.evaluate("""()=>{for(const s of document.querySelectorAll('svg.hs')){const bb=s.getBBox();
            s.setAttribute('viewBox',`${bb.x} ${bb.y} ${bb.width} ${bb.height}`);s.setAttribute('width',bb.width);s.setAttribute('height',bb.height)}}""")
        pg.wait_for_timeout(200)
        os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
        pg.screenshot(path='/tmp/_book.png'); b.close()
    im = Image.open('/tmp/_book.png').convert('RGB')
    im.save(out + '.jpg', quality=95, subsampling=0)
    im.resize((1080, 1350), Image.LANCZOS).save(out + '-1080.jpg', quality=95, subsampling=0)
    print('ok', out, 'cap', c)
