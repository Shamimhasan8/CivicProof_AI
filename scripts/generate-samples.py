from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import shutil
root=Path(__file__).resolve().parents[1]
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
for kind,name in [('nid','Amina Rahman'),('passport','Amina Rahaman')]:
    image=Image.new('RGB',(1200,730),'#f6f7f2');d=ImageDraw.Draw(image)
    d.rectangle((0,0,1200,110),fill='#133d32')
    d.text((55,37),'CIVICPROOF / FICTIONAL '+kind.upper()+' SAMPLE',fill='white',font=ImageFont.truetype(font,31))
    for i,line in enumerate(['Name: '+name,'Date of Birth: 1998-04-12','Document Type: '+('NID' if kind=='nid' else 'Passport'),'Document ID: DEMO-'+kind.upper()+'-001']):
        d.text((55,177+i*72),line,fill='#29372e',font=ImageFont.truetype(font,30))
    d.text((55,595),'SYNTHETIC - NOT A REAL GOVERNMENT DOCUMENT',fill='#a14024',font=ImageFont.truetype(font,30))
    d.text((55,659),'No seal. No official ID. For software testing only.',fill='#a14024',font=ImageFont.truetype(font,23))
    out=root/'public'/'samples'/('synthetic-'+kind+'.png');image.save(out)
    shared=Path('/workspace/shared/civicproof-evidence');shared.mkdir(parents=True,exist_ok=True);shutil.copyfile(out,shared/out.name)
