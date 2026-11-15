from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont("CivicSans","/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("CivicBold","/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
from pathlib import Path
import shutil
root=Path(__file__).resolve().parents[1]
for kind,name in [('nid','Amina Rahman'),('passport','Amina Rahaman')]:
    out=root/'public'/'samples'/('synthetic-'+kind+'.pdf')
    c=Canvas(str(out),pagesize=(720,460));c.setTitle('CivicProof fictional '+kind+' sample')
    c.setFillColor(HexColor('#f6f7f2'));c.rect(0,0,720,460,fill=1,stroke=0)
    c.setFillColor(HexColor('#133d32'));c.rect(0,380,720,80,fill=1,stroke=0)
    c.setFillColor(HexColor('#ffffff'));c.setFont('CivicBold',19);c.drawString(35,412,'CIVICPROOF / FICTIONAL '+kind.upper()+' SAMPLE')
    c.setFillColor(HexColor('#29372e'));c.setFont('CivicSans',17)
    for i,line in enumerate(['Name: '+name,'Date of Birth: 1998-04-12','Document Type: '+('NID' if kind=='nid' else 'Passport'),'Document ID: DEMO-'+kind.upper()+'-001']):c.drawString(35,328-i*50,line)
    c.setFillColor(HexColor('#a14024'));c.setFont('CivicBold',14);c.drawString(35,76,'SYNTHETIC - NOT A REAL GOVERNMENT DOCUMENT')
    c.setFont('CivicSans',12);c.drawString(35,43,'No seal. No official ID. For software testing only.');c.save()
    shutil.copyfile(out,Path('/workspace/shared/civicproof-evidence')/out.name)
