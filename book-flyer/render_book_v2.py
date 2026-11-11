"""Booking flyer v2 (slide 2 of the DAILY post only), inspired by Danag's 2026-11-11 reference set:
big Gobold word inside a gold selection frame with handles, services in ruled columns, grain, soft gold glow (top-left only).
Usage: python3 book-flyer/render_book_v2.py OUT_BASENAME "EYEBROW" "LINE 1" "BOX LINE" [THEME]
  THEME = white (when the daily flyer is navy) or navy / plain (when the daily flyer is white).
Writes OUT.jpg (2160x2700) and OUT-1080.jpg. The navy gradient background is never covered by glows on the right.
"""
import sys, os, pathlib, re
from playwright.sync_api import sync_playwright
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(D)
sys.path.insert(0, D)
import render_book as rb
from contacts import contacts

SERVICES = [('Flyer &amp; Poster', 'Design'), ('Business Card', 'Design'), ('Brochure', 'Design'),
            ('Website', 'Design'), ('Social Media', 'Management'), ('Product', 'Visuals')]


def html(ey, l1, big, theme):
    dark = theme != 'white'
    F = f'{R}/fonts/'
    logo = open(f'{D}/logo-on-{"navy" if dark else "white"}.svg').read()
    logo = re.sub(r'<\?xml[^>]*>', '', logo).replace('<svg', '<svg style="height:64px;width:auto;display:block"', 1)
    bg = ('#022452' if theme == 'plain' else 'linear-gradient(135deg,#032F65 0%,#022452 45%,#011631 80%,#010F21 100%)') if dark \
        else 'linear-gradient(180deg,#ffffff 0%,#eef1f6 100%)'
    ink = '#fff' if dark else '#022452'
    soft = 'rgba(255,255,255,.62)' if dark else '#6b7488'
    rule = 'rgba(255,255,255,.22)' if dark else 'rgba(2,36,82,.18)'
    gold = '#FFC107'
    svc = ''.join(f'<div style="border-left:3px solid {gold};padding-left:20px"><div style="font-weight:900;font-size:30px;line-height:1.15">{a}</div>'
                  f'<div style="font-weight:500;font-size:24px;margin-top:4px;color:{soft}">{b}</div></div>' for a, b in SERVICES)
    h = 18  # handle size
    handles = ''.join(f'<div class="a" style="{p};width:{h}px;height:{h}px;background:{gold};margin:-{h//2}px"></div>'
                      for p in ('left:0;top:0', 'right:0;top:0;margin-right:-9px', 'left:0;bottom:0;margin-bottom:-9px', 'right:0;bottom:0;margin-right:-9px;margin-bottom:-9px'))
    foot_bg = gold if dark else 'linear-gradient(135deg,#032F65 0%,#022452 45%,#011631 80%,#010F21 100%)'
    btn_bg, btn_fg = ('#022452', gold) if dark else (gold, '#022452')
    foot_txt = '#022452' if dark else '#fff'
    gr_op, gr_bl = ('.16', 'overlay') if dark else ('.12', 'multiply')
    return f"""<html><head><style>
@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}
@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}
@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
@font-face{{font-family:SC;src:url({F}sacramento-latin-400-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;background:{bg};color:{ink}}}
.a{{position:absolute}}
</style></head><body>
{'' if dark else '<div class="a" style="width:640px;height:640px;left:-330px;top:-300px;border-radius:50%;filter:blur(30px);background:radial-gradient(circle,rgba(255,193,7,.26) 0%,transparent 62%)"></div>'}
<svg class="a" viewBox="252 255 749 664" style="right:-260px;top:520px;width:760px;opacity:{'.05' if dark else '.045'}"><path fill="{ink}" fill-rule="evenodd" d="{rb.MK['nodot']}"/><path fill="{ink}" d="{rb.MK['dot']}"/></svg>
<div class="a" style="left:72px;top:64px">{logo}</div>
<div class="a" style="right:72px;top:72px;font-weight:700;font-size:21px">{contacts('#022452' if dark else '#fff', gold if dark else '#022452', ink, 34, phone=False)}</div>
<div class="a" style="left:72px;right:72px;top:170px;bottom:210px;display:flex;flex-direction:column;justify-content:space-evenly">
 <div>
  <div style="font-weight:700;font-size:26px;letter-spacing:7px;color:{gold if dark else '#b38600'}">{ey.upper()}</div>
  <div style="font-weight:900;font-size:64px;letter-spacing:-1px;margin-top:18px;line-height:1">{l1.upper()}</div>
  <div style="position:relative;display:inline-block;margin-top:34px;padding:30px 34px;border:2.5px solid {gold}">{handles}{big}</div>
  <div style="font-family:SC;font-size:64px;margin-top:22px;color:{ink}">Crowned in Craft</div>
 </div>
 <div style="display:grid;grid-template-columns:1fr 1fr 1fr;row-gap:30px;column-gap:28px">{svc}</div>
 <div style="font-weight:500;font-size:27px;line-height:1.45;color:{soft};max-width:860px">Let's bring your ideas to life with clean, bold designs that get people talking and get your phone ringing.</div>
</div>
<div class="a" style="left:0;right:0;bottom:0;height:210px;background:{foot_bg}"></div>
<div class="a" style="left:72px;bottom:66px;height:78px;padding:0 44px;border-radius:40px;background:{btn_bg};color:{btn_fg};display:flex;align-items:center;font-weight:900;font-size:28px;letter-spacing:3px">BOOK NOW</div>
<div class="a" style="right:72px;bottom:58px;text-align:right;color:{foot_txt}"><div style="font-weight:900;font-size:34px">+233 (0)50 332 0548</div><div style="font-weight:500;font-size:22px;opacity:.85;margin-top:8px">realprincedanag@gmail.com</div></div>
<div class="a" style="inset:0;z-index:50;pointer-events:none;opacity:{gr_op};mix-blend-mode:{gr_bl};background-size:256px;background-image:url({R}/grain.png)"></div>
</body></html>"""


if __name__ == '__main__':
    out, ey, l1, l2 = sys.argv[1:5]
    theme = sys.argv[5] if len(sys.argv) > 5 else 'white'
    dark = theme != 'white'
    c = rb.fit(l2, 936 - 72, 230, True)
    big = rb.line(l2, c, '#FFC107' if dark else '#022452', True, dot_color='#fff' if dark else '#FFC107')
    tmp = '/tmp/_book2.html'; open(tmp, 'w').write(html(ey, l1, big, theme))
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
        pg.goto(pathlib.Path(tmp).as_uri()); pg.wait_for_timeout(900)
        pg.evaluate("""()=>{for(const s of document.querySelectorAll('svg.hs')){const bb=s.getBBox();
            s.setAttribute('viewBox',`${bb.x} ${bb.y} ${bb.width} ${bb.height}`);s.setAttribute('width',bb.width);s.setAttribute('height',bb.height)}}""")
        pg.wait_for_timeout(200)
        os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
        pg.screenshot(path='/tmp/_book2.png'); b.close()
    im = Image.open('/tmp/_book2.png').convert('RGB')
    im.save(out + '.jpg', quality=95, subsampling=0)
    im.resize((1080, 1350), Image.LANCZOS).save(out + '-1080.jpg', quality=95, subsampling=0)
    print('ok', out, 'cap', c)
