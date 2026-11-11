"""Make TikTok-safe 9:16 (1080x1920) versions of 4:5 designs so TikTok never crops the sides.
The 4:5 design sits in the middle; the top/bottom bands repeat the design's own edge rows (seamless).
Usage: python3 tools/tiktok916.py IN.jpg OUT.jpg   (or several pairs)"""
import sys
from PIL import Image, ImageFilter
band = lambda strip, h: strip.resize((108, 1), Image.BOX).filter(ImageFilter.GaussianBlur(3)).resize((1080, h), Image.BILINEAR)
a = sys.argv[1:]
for i in range(0, len(a), 2):
    im = Image.open(a[i]).convert('RGB').resize((1080, 1350), Image.LANCZOS)
    c = Image.new('RGB', (1080, 1920)); top = (1920 - 1350) // 2
    c.paste(band(im.crop((0, 0, 1080, 24)), top), (0, 0))
    c.paste(band(im.crop((0, 1326, 1080, 1350)), 1920 - top - 1350), (0, top + 1350))
    c.paste(im, (0, top)); c.save(a[i + 1], quality=95, subsampling=0)
    print('ok', a[i + 1])
