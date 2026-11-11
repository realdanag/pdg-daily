"""Round-2 asset swaps (11 Nov 2026 feedback). Sources: DANAG STUDIO\\DANAG STUDIO and DANAG STUDIO\\Dasamic (staged)."""
from PIL import Image
import pathlib
Image.MAX_IMAGE_PIXELS = None
U = pathlib.Path('/mnt/user-data/uploads'); D = U / 'DANAG STUDIO'; A = pathlib.Path(__file__).parent / 'assets'
def save(im, name, mx=2000):
    im = im.convert('RGB'); im.thumbnail((mx, mx), Image.LANCZOS); im.save(A / f'{name}.jpg', quality=92, subsampling=0); print(name, im.size)
src = {
 'my-leather': D / 'Maison Yusif/LEATHER TO EXCELLENCE.png',
 'my-specials-img': D / 'Maison Yusif/M.Y. SPECIALS IMAGE Design.png',
 'my-badinfluence': D / 'Maison Yusif/M.Y. AI PERFUME PHOTOGRAPHS/BAD INFLUENCE L.V.1.webp',
 'my-vatican': D / 'Maison Yusif/M.Y. AI PERFUME PHOTOGRAPHS/VATICAN1.webp',
 'my-paris': D / 'Maison Yusif/M.Y. PARIS PERFUME WEEK DES. 2.png',
 'my-tamale': D / 'Maison Yusif/M.Y. TAMALE SHOP OPENING FLYER DES.png',
 'tf-gmg-red': D / 'Treadfix/GHANA-MUST-GO/Red F&B/RED FULL SHOT.png',
 'tf-wig-navy': D / 'Treadfix/WRAPPED IN GRATITUDE/NAVY/FULL SHOT 2.png',
 'fl-persian': D / 'Scent and Spice/PERSIAN NIGHTS DOTW DESIGN.png',
 'fl-signature1': D / 'SIGNATURE.png',
 'pk-marmar-shampoo': U / 'Dasamic/marmar/marmar-shampoo-label.png',
 'pk-mamti': D / 'Mamle/Mamti Nutri-Delight 2.png',
 'lg-autoperf': D / 'MY PERSONAL PROJECTS/IMAGE.png',
}
for k, v in src.items(): save(Image.open(v), k)
# MarMar logo on an emerald square (logo rendered from marmar-logo-cream-on-emerald.svg)
lg = Image.open('/tmp/marmar-logo.png').convert('RGB'); c = Image.new('RGB', (2000, 2000), lg.getpixel((4, 4)))
lg.thumbnail((1400, 1400), Image.LANCZOS)
# fill the canvas with the logo's own vertical gradient so the padding blends in
top, bot = lg.getpixel((4, 4)), lg.getpixel((4, lg.height - 5))
for y in range(2000):
    t = y / 1999; c.paste(tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3)), (0, y, 2000, y + 1))
c.paste(lg, ((2000 - lg.width) // 2, (2000 - lg.height) // 2)); save(c, 'lg-marmar')
