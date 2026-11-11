"""Round-3 assets (11 Nov 2026): whole 4:5 images supplied by Danag, no cropping."""
from PIL import Image
import pathlib
Image.MAX_IMAGE_PIXELS = None
U = pathlib.Path('/mnt/user-data/uploads'); D = U / 'DANAG STUDIO'; A = pathlib.Path(__file__).parent / 'assets'
def save(im, name, mx=2000):
    im = im.convert('RGB'); im.thumbnail((mx, mx), Image.LANCZOS); im.save(A / f'{name}.jpg', quality=92, subsampling=0); print(name, im.size, round(im.size[0]/im.size[1],3))
src = {
 'my-083': U / 'M_Y__IMAGE_083.png', 'my-063b': U / 'M_Y__IMAGE_063_B.png',
 'my-066': U / 'a1cb3669-image.png' if False else U / '73cf12fa-image.png',
 'my-073': U / 'a1cb3669-image.png', 'my-074': U / '3f201a54-image.png',
 'ss-178': U / '0f9f9469-image.png', 'ss-030': U / 'b5ed64f7-image.png',
 'tf-barrel-front': U / 'd0e24627-image.png', 'tf-barrel-side': U / 'd5101c00-image.png',
 'tf-faces-portrait': D / 'Treadfix/FOUR FACES/FACES OUTDOOR PORTRAIT SHOT.png',
 'fl-ss-open': U / '7d46eb8e-image.png',
}
for k, v in src.items(): save(Image.open(v), k)
