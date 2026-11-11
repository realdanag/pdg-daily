"""Alternative booking flyer layouts (slide 2 of the DAILY post only), from Danag's 2026-11-11 reference set.
Usage: python3 book-flyer/render_book_alt.py LAYOUT OUT_BASENAME "EYEBROW" "LINE 1" "BOX LINE" [THEME]
  LAYOUT  A = centred giant word over a faint speech bubble, ruled service columns, DM pill
          B = headline + desktop monitor showing Danag's own work + ticked services
          C = stacked headline + ticked services + tilted phone showing his feed + round BOOK NOW badge
  THEME   white (when the daily flyer is navy) or navy / plain (when the daily flyer is white). No glow on navy.
Uses only Danag's own work from book-flyer/work/. Writes OUT.jpg (2160x2700) and OUT-1080.jpg.
"""
import sys, os, pathlib, re
from playwright.sync_api import sync_playwright
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(D)
sys.path.insert(0, D)
import render_book as rb
from contacts import contacts, IC

SV = [('Flyer &amp; Poster', 'Design'), ('Business Card', 'Design'), ('Brochure', 'Design'),
      ('Website', 'Design'), ('Social Media', 'Management'), ('Product', 'Visuals')]
WORK = sorted(f'{D}/work/{f}' for f in os.listdir(f'{D}/work'))
GOLD = '#FFC107'
NAVYG = 'linear-gradient(135deg,#032F65 0%,#022452 45%,#011631 80%,#010F21 100%)'


def ico(k, c, s=24):
    return f'<svg viewBox="0 0 24 24" width="{s}" height="{s}" style="color:{c};flex:none">{IC[k]}</svg>'


def tick(bg, fg, s=34):
    return (f'<span style="width:{s}px;height:{s}px;border-radius:50%;background:{bg};display:inline-flex;align-items:center;justify-content:center;flex:none">'
            f'<svg viewBox="0 0 24 24" width="{int(s*.6)}" height="{int(s*.6)}"><path d="M5 12.5l4.2 4.2L19 7" fill="none" stroke="{fg}" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>')


def page(theme, body):
    dark = theme != 'white'
    F = f'{R}/fonts/'
    bg = ('#022452' if theme == 'plain' else NAVYG) if dark else 'linear-gradient(180deg,#ffffff 0%,#eef1f6 100%)'
    ink = '#fff' if dark else '#022452'
    logo = open(f'{D}/logo-on-{"navy" if dark else "white"}.svg').read()
    logo = re.sub(r'<\?xml[^>]*>', '', logo).replace('<svg', '<svg style="height:64px;width:auto;display:block"', 1)
    glow = '' if dark else '<div class="a" style="width:640px;height:640px;left:-330px;top:-300px;border-radius:50%;filter:blur(30px);background:radial-gradient(circle,rgba(255,193,7,.26) 0%,transparent 62%)"></div>'
    gr = ('.16', 'overlay') if dark else ('.12', 'multiply')
    return f"""<html><head><style>
@font-face{{font-family:M;font-weight:500;src:url({F}montserrat-latin-500-normal.woff2)}}
@font-face{{font-family:M;font-weight:700;src:url({F}montserrat-latin-700-normal.woff2)}}
@font-face{{font-family:M;font-weight:900;src:url({F}montserrat-latin-900-normal.woff2)}}
@font-face{{font-family:SC;src:url({F}sacramento-latin-400-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:M;background:{bg};color:{ink}}}
.a{{position:absolute}}
</style></head><body>{glow}
<svg class="a" viewBox="252 255 749 664" style="right:-260px;bottom:-120px;width:700px;opacity:{'.05' if dark else '.045'}"><path fill="{ink}" fill-rule="evenodd" d="{rb.MK['nodot']}"/><path fill="{ink}" d="{rb.MK['dot']}"/></svg>
<div class="a" style="left:72px;top:64px">{logo}</div>
<div class="a" style="right:72px;top:72px;font-weight:700;font-size:21px">{contacts('#022452' if dark else '#fff', GOLD if dark else '#022452', ink, 34, phone=False)}</div>
{body}
<div class="a" style="inset:0;z-index:50;pointer-events:none;opacity:{gr[0]};mix-blend-mode:{gr[1]};background-size:256px;background-image:url({R}/grain.png)"></div>
</body></html>"""


def layout_A(ey, l1, l2, theme):
    dark = theme != 'white'
    ink = '#fff' if dark else '#022452'; soft = 'rgba(255,255,255,.62)' if dark else '#6b7488'
    big = rb.line(l2, rb.fit(l2, 936, 260, True), GOLD if dark else '#022452', True, dot_color='#fff' if dark else GOLD)
    cols = ''.join(f'<div style="border-left:3px solid {GOLD};padding-left:16px;text-align:left"><div style="font-weight:900;font-size:25px;line-height:1.15;white-space:nowrap">{a}</div>'
                   f'<div style="font-weight:500;font-size:22px;margin-top:4px;color:{soft}">{b}</div></div>' for a, b in SV[:4])
    bubble = (f'<svg class="a" viewBox="0 0 900 760" style="left:-120px;top:330px;width:900px;opacity:{".07" if dark else ".06"}">'
              f'<path d="M110 40H790Q860 40 860 110V470Q860 540 790 540H330L190 690V540H110Q40 540 40 470V110Q40 40 110 40Z" fill="none" stroke="{ink}" stroke-width="44" stroke-linejoin="round"/>'
              f'<rect x="150" y="200" width="420" height="44" rx="22" fill="{ink}"/><rect x="150" y="320" width="300" height="44" rx="22" fill="{ink}"/></svg>')
    pill_bg, pill_fg = ('#fff', '#022452') if dark else ('#022452', '#fff')
    return bubble + f"""<div class="a" style="left:72px;right:72px;top:150px;bottom:40px;display:flex;flex-direction:column;justify-content:space-evenly;align-items:center;text-align:center">
 <div style="display:flex;flex-direction:column;align-items:center">
  <div style="font-weight:700;font-size:26px;letter-spacing:7px;color:{GOLD if dark else '#b38600'}">{ey.upper()}</div>
  <div style="font-weight:900;font-size:60px;letter-spacing:-1px;margin-top:20px;line-height:1">{l1.upper()}</div>
  <div style="margin-top:30px">{big}</div>
  <div style="font-family:SC;font-size:62px;margin-top:16px">Crowned in Craft</div>
 </div>
 <div style="display:grid;grid-template-columns:repeat(4,1fr);column-gap:22px;width:100%">{cols}</div>
 <div style="display:flex;flex-direction:column;align-items:center;gap:20px">
  <div style="font-weight:500;font-size:25px;color:{soft}">Website design, social media management, product visuals and more.</div>
  <div style="display:flex;gap:18px;align-items:center">
   <div style="background:{pill_bg};color:{pill_fg};height:84px;padding:0 44px;border-radius:12px;display:flex;align-items:center;gap:16px;font-weight:900;font-size:30px;box-shadow:0 14px 30px rgba(1,15,33,.18)">{ico('IG', GOLD, 30)}Send me a DM today</div>
   <div style="border:2.5px solid {GOLD};height:84px;padding:0 34px;border-radius:12px;display:flex;align-items:center;gap:12px;font-weight:900;font-size:28px">{ico('PH', GOLD, 28)}+233 (0)50 332 0548</div>
  </div>
 </div>
</div>"""


def layout_B(ey, l1, l2, theme):
    dark = theme != 'white'
    ink = '#fff' if dark else '#022452'; soft = 'rgba(255,255,255,.62)' if dark else '#6b7488'
    big = rb.line(l2, rb.fit(l2, 760, 150, True), GOLD if dark else '#022452', True, dot_color='#fff' if dark else GOLD)
    grid = ''.join(f'<div style="background:url({pathlib.Path(w).as_uri()}) center/cover;border-radius:6px"></div>' for w in WORK[:12])
    monitor = f"""<div style="width:936px;margin:0 auto">
  <div style="background:#0b1424;border-radius:22px;padding:18px 18px 34px;box-shadow:0 30px 60px rgba(1,15,33,.35){",0 0 0 2px rgba(255,255,255,.22)" if dark else ""}">
   <div style="background:#13213a;border-radius:8px;padding:14px;display:grid;grid-template-columns:repeat(6,1fr);grid-auto-rows:181px;gap:10px">{grid}</div>
  </div>
  <div style="width:150px;height:46px;margin:0 auto;background:linear-gradient(#0b1424,#1c2a44)"></div>
  <div style="width:330px;height:14px;margin:0 auto;border-radius:8px;background:#1c2a44"></div>
 </div>"""
    items = ''.join(f'<div style="display:flex;align-items:center;gap:14px;font-weight:900;font-size:25px">{tick(GOLD, "#022452", 32)}{a} <span style="font-weight:500;color:{soft}">{b}</span></div>' for a, b in SV)
    return f"""<div class="a" style="left:72px;right:72px;top:160px;bottom:60px;display:flex;flex-direction:column;justify-content:space-evenly">
 <div>
  <div style="font-weight:700;font-size:26px;letter-spacing:7px;color:{GOLD if dark else '#b38600'}">{ey.upper()}</div>
  <div style="display:flex;align-items:flex-end;gap:26px;margin-top:16px"><div style="font-weight:900;font-size:56px;line-height:1;padding-bottom:8px">{l1.upper()}</div></div>
  <div style="margin-top:16px">{big}</div>
 </div>
 {monitor}
 <div style="display:grid;grid-template-columns:1fr 1fr;row-gap:16px;column-gap:30px">{items}</div>
 <div style="display:flex;justify-content:space-between;align-items:center">
  <div style="background:{GOLD};color:#022452;height:76px;padding:0 42px;border-radius:40px;display:flex;align-items:center;font-weight:900;font-size:27px;letter-spacing:3px">BOOK NOW</div>
  <div style="display:flex;align-items:center;gap:14px;font-weight:900;font-size:32px">{ico('PH', GOLD, 30)}+233 (0)50 332 0548</div>
 </div>
</div>"""


def layout_C(ey, l1, l2, theme):
    dark = theme != 'white'
    ink = '#fff' if dark else '#022452'; soft = 'rgba(255,255,255,.62)' if dark else '#6b7488'
    words = (l1 + ' ' + l2).upper().split()
    head = '<br>'.join(words[:-1]) + f'<br><span style="color:{GOLD}">{words[-1]}</span><span style="display:inline-block;width:.236em;height:.236em;border-radius:50%;background:{"#fff" if dark else GOLD};margin-left:.02em"></span>'
    if not dark:
        head = '<br>'.join(words[:-1]) + f'<br><span style="background:linear-gradient(180deg,#FFD54F,#E3A600);-webkit-background-clip:text;color:transparent">{words[-1]}</span><span style="display:inline-block;width:.236em;height:.236em;border-radius:50%;background:#022452;margin-left:.02em"></span>'
    feed = ''.join(f'<div style="background:url({pathlib.Path(w).as_uri()}) center/cover"></div>' for w in WORK[:12])
    items = ''.join(f'<div style="display:flex;align-items:center;gap:14px;font-weight:900;font-size:24px;line-height:1.15">{tick(GOLD, "#022452", 30)}<span>{a}<br><span style="font-weight:500;font-size:20px;color:{soft}">{b}</span></span></div>' for a, b in SV)
    ring = 'CROWNED IN CRAFT &#8226; DANAG STUDIO &#8226; '
    badge = f"""<div class="a" style="right:350px;top:250px;width:210px;height:210px;z-index:5">
  <div style="position:absolute;inset:0;border-radius:50%;background:{GOLD};box-shadow:0 0 0 14px rgba(255,193,7,.22),0 0 0 30px rgba(255,193,7,.10)"></div>
  <svg viewBox="0 0 210 210" style="position:absolute;inset:0"><defs><path id="rc" d="M105 105m-78 0a78 78 0 1 1 156 0a78 78 0 1 1-156 0"/></defs>
  <text font-family="M" font-weight="700" font-size="15.5" fill="#022452"><textPath href="#rc" textLength="486" lengthAdjust="spacing">{ring}</textPath></text></svg>
  <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;text-align:center;font-weight:900;font-size:30px;line-height:1;color:#022452">BOOK<br>NOW</div>
 </div>"""
    phone = f"""<div class="a" style="right:96px;top:316px;width:380px;height:770px;transform:rotate(7deg);border-radius:54px;background:#0b1424;padding:16px;box-shadow:0 40px 70px rgba(1,15,33,.35){',0 0 0 2px rgba(255,255,255,.22)' if dark else ''}">
  <div style="width:100%;height:100%;border-radius:40px;overflow:hidden;background:#fff;color:#022452">
   <div style="padding:46px 20px 12px;display:flex;align-items:center;gap:12px"><div style="width:64px;height:64px;border-radius:50%;background:#022452;display:flex;align-items:center;justify-content:center">{re.sub(r'<\?xml[^>]*>', '', open(f'{D}/logo-on-navy.svg').read()).replace('<svg', '<svg style="width:46px;height:auto;display:block;overflow:hidden" ', 1)}</div>
    <div style="font-weight:900;font-size:17px">thedanagstudio<div style="font-weight:500;font-size:13px;color:#6b7488;margin-top:3px">Graphic Designer &#183; Accra</div></div></div>
   <div style="display:flex;gap:8px;padding:0 20px 12px"><div style="flex:1;background:#022452;color:#fff;border-radius:8px;text-align:center;font-weight:700;font-size:13px;padding:8px">Follow</div><div style="flex:1;background:#eef1f6;border-radius:8px;text-align:center;font-weight:700;font-size:13px;padding:8px">Message</div></div>
   <div style="display:grid;grid-template-columns:repeat(3,1fr);grid-auto-rows:150px;gap:2px">{feed}</div>
  </div>
 </div>"""
    return badge + phone + f"""<div class="a" style="left:72px;width:520px;top:160px;bottom:60px;display:flex;flex-direction:column;justify-content:space-evenly">
 <div>
  <div style="font-weight:700;font-size:24px;letter-spacing:6px;color:{GOLD if dark else '#b38600'}">{ey.upper()}</div>
  <div style="font-weight:900;font-size:92px;line-height:.98;letter-spacing:-2px;margin-top:20px">{head}</div>
 </div>
 <div style="display:grid;grid-template-columns:1fr 1fr;row-gap:22px;column-gap:18px">{items}</div>
 <div>
  <div style="font-family:SC;font-size:56px;line-height:1">Crowned in Craft</div>
  <div style="display:flex;align-items:center;gap:14px;font-weight:900;font-size:30px;margin-top:22px">{ico('PH', GOLD, 30)}+233 (0)50 332 0548</div>
  <div style="font-weight:500;font-size:21px;color:{soft};margin-top:8px">realprincedanag@gmail.com</div>
 </div>
</div>"""


if __name__ == '__main__':
    lay, out, ey, l1, l2 = sys.argv[1:6]
    theme = sys.argv[6] if len(sys.argv) > 6 else 'white'
    body = {'A': layout_A, 'B': layout_B, 'C': layout_C}[lay](ey, l1, l2, theme)
    tmp = f'/tmp/_alt{lay}.html'; open(tmp, 'w').write(page(theme, body))
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
        pg.goto(pathlib.Path(tmp).as_uri()); pg.wait_for_timeout(1200)
        pg.evaluate("""()=>{for(const s of document.querySelectorAll('svg.hs')){const bb=s.getBBox();
            s.setAttribute('viewBox',`${bb.x} ${bb.y} ${bb.width} ${bb.height}`);s.setAttribute('width',bb.width);s.setAttribute('height',bb.height)}}""")
        pg.wait_for_timeout(200)
        os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
        pg.screenshot(path=f'/tmp/_alt{lay}.png'); b.close()
    im = Image.open(f'/tmp/_alt{lay}.png').convert('RGB')
    im.save(out + '.jpg', quality=95, subsampling=0)
    im.resize((1080, 1350), Image.LANCZOS).save(out + '-1080.jpg', quality=95, subsampling=0)
    print('ok', out)
