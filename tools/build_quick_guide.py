from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, Color
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.utils import simpleSplit

OUT = Path(__file__).resolve().parents[1] / 'docs' / 'guida-rapida.pdf' if 'tools' in Path(__file__).parts else Path('/mnt/data/guide-redesign/guida-rapida.pdf')
OUT.parent.mkdir(parents=True, exist_ok=True)

W,H = A4
INK=HexColor('#0B1713'); GREEN=HexColor('#0F3D2E'); GREEN2=HexColor('#1B5D46'); GOLD=HexColor('#C8A15A')
IVORY=HexColor('#F5F1E8'); PAPER=HexColor('#FBFAF6'); PAPER2=HexColor('#EEE8DC'); TEXT=HexColor('#17231E'); MUTED=HexColor('#657069'); WHITE=HexColor('#FFFFFF')
LINE=HexColor('#D9D4C9'); WARM=HexColor('#F6EEDC'); WARMINK=HexColor('#6F5422')

# Use built-ins for portability on GitHub Actions.
SANS='Helvetica'; SANS_B='Helvetica-Bold'; SERIF='Times-Roman'; SERIF_I='Times-Italic'; SERIF_B='Times-Bold'

IT = {
 'cover_k':'BILIARDOOS · GUIDA OPERATIVA', 'cover_t':'Guida rapida', 'cover_s':'Dal primo avvio al podio.',
 'cover_p':'Dieci passaggi essenziali per organizzare il tuo primo campionato a batterie: configurazione, sorteggio, convocazioni, serata di gara, fase finale e backup.',
 'chips':['WINDOWS 10 / 11','10 PASSAGGI','DATI LOCALI','ITALIANO + ENGLISH'],
 'flow_title':'UN CAMPIONATO, SEI MOMENTI',
 'flow':[('01','Impostazione','dati · sedi · giocatori'),('02','Sorteggio','regole · abbinamenti'),('03','Convocazioni','tagliandi · invii'),('04','Serate','appello · risultati'),('05','Fase finale','tabellone · podio'),('06','Chiusura','report · archivio')],
 'page1_k':'01 · PREPARARE', 'page1_t':'Dall’installazione\nal sorteggio.',
 'page2_k':'02 · GESTIRE', 'page2_t':'Dalla convocazione\nalla chiusura.',
 'safety_title':'SMARTSCREEN, SENZA SCORCIATOIE',
 'safety':'L’installer può essere segnalato perché non è ancora firmato digitalmente. Scaricalo solo dal sito o dal repository ufficiale, verifica il file con Sicurezza di Windows e non disattivare le protezioni di sistema.',
 'gold_title':'REGOLA D’ORO', 'gold':'Crea un backup prima di un aggiornamento importante, di un trasferimento su un altro PC o della fase finale.',
 'steps':[
 ('01','Installazione','Scarica BiliardoOS dalla pagina ufficiale o da Releases. Avvia BiliardoOS-Setup-*.exe: l’installazione è per l’utente corrente e normalmente non richiede privilegi amministrativi.'),
 ('02','Primo avvio','Scegli “Inizia da zero” oppure “Ripristina da una copia”. Configura circolo, sedi, ufficiali di gara, copia esterna e - se vuoi - l’assistente AI locale.'),
 ('03','Crea il campionato','Da Tornei avvia un campionato a batterie. Scegli singolo o coppie, batterie da 4 o 8, poi assegna sedi, date, orari e regole di punteggio.'),
 ('04','Sorteggio','Usa Anteprima sorteggio per generare le proposte. Conferma solo quando la distribuzione è corretta: BiliardoOS crea il verbale e conserva il seed del sorteggio.'),
 ('05','Convocazioni','Scegli Ticket singolo oppure 4 per A4. Esporta il PDF o prepara le comunicazioni via email e WhatsApp. Controlla sempre sede, data e orario prima dell’invio.'),
 ('06','Serata di gara','Prepara il kit serata, usa Appello per segnare presenti e assenti, quindi inserisci i risultati batteria per batteria. A fine serata chiudi e condividi i risultati.'),
 ('07','Fase finale','Quando le batterie qualificanti sono concluse, genera la fase finale. Registra i risultati del tabellone fino a campione, secondo posto e piazzamenti.'),
 ('08','Classifiche e chiusura','Le classifiche si aggiornano automaticamente. Quando podio e serate sono completi, chiudi il campionato e genera report, pacchetto finale ed esportazione Excel.'),
 ('09','Backup e più PC','Da Impostazioni → Backup crea, esporta o ripristina una copia. Per casa + portatile usa la funzione dedicata oppure una copia esterna su OneDrive, USB o NAS.'),
 ('10','Serve aiuto?','Apri la Guida in-app per le funzioni avanzate. L’assistente AI locale può aiutarti sull’uso del programma; Discussions e Issues raccolgono domande, idee e bug.')
 ],
 'footer':'BiliardoOS · Guida rapida · plagemes.github.io/biliardoos-releases'
}
EN = {
 'cover_k':'BILIARDOOS · OPERATING GUIDE', 'cover_t':'Quick guide', 'cover_s':'From first launch to the podium.',
 'cover_p':'Ten essential steps for running your first heat-format championship: setup, draw, call-ups, match night, final phase and backups.',
 'chips':['WINDOWS 10 / 11','10 STEPS','LOCAL DATA','ITALIANO + ENGLISH'],
 'flow_title':'ONE CHAMPIONSHIP, SIX MOMENTS',
 'flow':[('01','Setup','data · venues · players'),('02','Draw','rules · pairings'),('03','Call-ups','slips · messages'),('04','Match nights','roll call · scores'),('05','Final phase','bracket · podium'),('06','Closeout','reports · archive')],
 'page1_k':'01 · PREPARE', 'page1_t':'From installation\nto the draw.',
 'page2_k':'02 · RUN', 'page2_t':'From call-ups\nto closeout.',
 'safety_title':'SMARTSCREEN, NO SHORTCUTS',
 'safety':'Windows may warn because the installer is not yet digitally signed. Download only from the official website or repository, scan the file with Windows Security and do not disable system protections.',
 'gold_title':'GOLDEN RULE', 'gold':'Make a backup before a major update, moving to another PC or starting the final phase.',
 'steps':[
 ('01','Installation','Download BiliardoOS from the official page or Releases. Run BiliardoOS-Setup-*.exe: installation is per Windows user and normally does not require administrator privileges.'),
 ('02','First launch','Choose “Start from scratch” or “Restore from a backup”. Configure the club, venues, officials, external copy and - if you want - the local AI assistant.'),
 ('03','Create the championship','Open Tournaments and create a heat-format championship. Choose singles or pairs, heats of 4 or 8, then assign venues, dates, call-up times and scoring rules.'),
 ('04','Draw','Use Draw preview to generate proposals. Confirm only when the distribution is right: BiliardoOS creates the draw report and stores the random seed.'),
 ('05','Call-ups','Choose Single ticket or 4 per A4. Export the PDF or prepare email and WhatsApp messages. Always verify venue, date and time before sending.'),
 ('06','Match night','Prepare the match-night pack, use Roll call to mark players present or absent, then enter results heat by heat. When the session is complete, close it and share the results.'),
 ('07','Final phase','Once qualifying heats are complete, generate the final phase. Record bracket results through to champion, runner-up and final placements.'),
 ('08','Standings and closeout','Standings update automatically. When the podium and match nights are complete, close the championship and generate the report, final package and Excel export.'),
 ('09','Backups and multiple PCs','Open Settings → Backup to create, export or restore a copy. For home + laptop use the dedicated option or an external copy on OneDrive, USB or NAS.'),
 ('10','Need help?','Use the in-app Help for advanced features. The local AI assistant can explain the app; Discussions and Issues are available for questions, ideas and bug reports.')
 ],
 'footer':'BiliardoOS · Quick guide · plagemes.github.io/biliardoos-releases'
}

def text(c, s, x, y, size=10, font=SANS, color=TEXT):
    c.setFont(font,size); c.setFillColor(color); c.drawString(x,y,s)

def rtext(c, s, x, y, size=10, font=SANS, color=TEXT):
    c.setFont(font,size); c.setFillColor(color); c.drawRightString(x,y,s)

def wrap(c, s, x, y, width, size=10, leading=None, font=SANS, color=TEXT, max_lines=None):
    if leading is None: leading=size*1.35
    lines=simpleSplit(s,font,size,width)
    if max_lines and len(lines)>max_lines:
        lines=lines[:max_lines]
        if len(lines[-1])>3: lines[-1]=lines[-1][:-3]+'...'
    c.setFont(font,size); c.setFillColor(color)
    for i,line in enumerate(lines): c.drawString(x,y-i*leading,line)
    return y-len(lines)*leading

def round_rect(c,x,y,w,h,r=12,fill=WHITE,stroke=LINE,sw=.6):
    c.setLineWidth(sw); c.setStrokeColor(stroke); c.setFillColor(fill); c.roundRect(x,y,w,h,r,stroke=1,fill=1)

def brand(c,x,y,dark=False):
    c.setFillColor(GREEN2 if not dark else HexColor('#23503D')); c.roundRect(x,y-18,24,24,8,0,1)
    c.setFillColor(IVORY); c.circle(x+12,y-6,4.6,0,1)
    text(c,'Biliardo',x+33,y-11,14,SANS_B,IVORY if dark else INK); text(c,'OS',x+85,y-11,14,SANS_B,GOLD)

def page_footer(c,d,page,total):
    c.setStrokeColor(Color(1,1,1,.12) if page==1 else LINE); c.setLineWidth(.5); c.line(36,29,W-36,29)
    col=HexColor('#AAB5AF') if page==1 else MUTED
    text(c,d['footer'],36,17,6.8,SANS,col); rtext(c,f'{page:02d} / {total:02d}',W-36,17,6.8,SANS_B,col)

def cover(c,d,page,total,lang):
    c.setFillColor(INK); c.rect(0,0,W,H,0,1)
    c.setFillColor(Color(0.78,0.63,0.35,.08)); c.circle(W+18,H-115,190,0,1); c.circle(W+18,H-115,135,0,0)
    brand(c,40,H-38,True)
    text(c,d['cover_k'],40,H-118,7.4,SANS_B,HexColor('#BCC7C1'))
    text(c,d['cover_t'],40,H-190,42,SERIF,IVORY); text(c,d['cover_s'],40,H-232,21,SERIF_I,GOLD)
    wrap(c,d['cover_p'],40,H-276,345,10.5,15,SANS,HexColor('#C7D0CB'))
    x=40; y=H-352
    for chip in d['chips']:
        w=stringWidth(chip,SANS_B,6.4)+18; c.setFillColor(Color(1,1,1,.04)); c.setStrokeColor(Color(1,1,1,.13)); c.roundRect(x,y,w,20,10,1,1); text(c,chip,x+9,y+7,6.4,SANS_B,HexColor('#DBE1DE')); x+=w+6
    # workflow card
    cx,cy,cw,ch=40,105,W-80,260
    c.setFillColor(PAPER); c.roundRect(cx,cy,cw,ch,18,0,1)
    text(c,d['flow_title'],cx+20,cy+ch-28,7.2,SANS_B,GREEN)
    cellw=(cw-40)/2; rowh=61
    for i,(n,t,sub) in enumerate(d['flow']):
        col=i%2; row=i//2; bx=cx+20+col*cellw; by=cy+ch-55-(row+1)*rowh
        c.setStrokeColor(LINE); c.setFillColor(WHITE); c.roundRect(bx,by,cellw-8,rowh-8,10,1,1)
        c.setFillColor(GREEN); c.circle(bx+20,by+26,10,0,1); text(c,n,bx+13.4,by+23,6.8,SANS_B,WHITE)
        text(c,t,bx+40,by+30,8.8,SANS_B,INK); text(c,sub,bx+40,by+16,6.8,SANS,MUTED)
        c.setFillColor(GOLD); c.circle(bx+cellw-25,by+26,3,0,1)
    text(c,'IT',W-77,H-48,7,SANS_B,GOLD if lang=='it' else HexColor('#78867F')); text(c,'EN',W-52,H-48,7,SANS_B,GOLD if lang=='en' else HexColor('#78867F'))
    page_footer(c,d,page,total)

def step_card(c,step,x,y,w,h):
    n,title,body=step
    round_rect(c,x,y,w,h,13,WHITE,LINE,.7)
    c.setFillColor(GREEN); c.circle(x+21,y+h-23,11,0,1); text(c,n,x+13.7,y+h-26.2,7,SANS_B,WHITE)
    text(c,title,x+42,y+h-27,11,SANS_B,INK)
    wrap(c,body,x+18,y+h-53,w-36,8.3,11.8,SANS,HexColor('#4F5E56'),max_lines=8)

def steps_page(c,d,page,total,which):
    c.setFillColor(PAPER); c.rect(0,0,W,H,0,1)
    c.setFillColor(INK); c.rect(0,H-94,W,94,0,1)
    brand(c,36,H-42,True)
    k=d['page1_k'] if which==1 else d['page2_k']; title=d['page1_t'] if which==1 else d['page2_t']
    text(c,k,36,H-130,7,SANS_B,GREEN)
    yy=H-171
    for line in title.split('\n'):
        text(c,line,36,yy,28,SERIF,INK); yy-=30
    # top note
    if which==1:
        round_rect(c,36,H-305,W-72,62,12,WARM,HexColor('#E0C99B'),.6)
        text(c,d['safety_title'],50,H-267,7,SANS_B,WARMINK)
        wrap(c,d['safety'],50,H-282,W-100,7.6,10.6,SANS,WARMINK,max_lines=4)
        start_y=H-470
        indices=range(0,5)
    else:
        round_rect(c,36,H-305,W-72,56,12,INK,INK,.6)
        text(c,d['gold_title'],50,H-269,7,SANS_B,GOLD)
        wrap(c,d['gold'],50,H-286,W-100,8,11,SANS,HexColor('#D1D9D5'),max_lines=3)
        start_y=H-462
        indices=range(5,10)
    gap=12; cardw=(W-72-gap)/2; cardh=122
    for j,idx in enumerate(indices):
        if j<4:
            row=j//2; col=j%2; x=36+col*(cardw+gap); y=start_y-row*(cardh+gap)
            step_card(c,d['steps'][idx],x,y,cardw,cardh)
        else:
            y=start_y-2*(cardh+gap); step_card(c,d['steps'][idx],36,y,W-72,cardh-6)
    page_footer(c,d,page,total)

def build():
    c=canvas.Canvas(str(OUT),pagesize=A4,pageCompression=1)
    c.setTitle('BiliardoOS - Guida rapida / Quick guide')
    c.setAuthor('Plagemes')
    total=6; p=1
    for d,lang in [(IT,'it'),(EN,'en')]:
        cover(c,d,p,total,lang); c.showPage(); p+=1
        steps_page(c,d,p,total,1); c.showPage(); p+=1
        steps_page(c,d,p,total,2); c.showPage(); p+=1
    c.save(); print(OUT)

if __name__=='__main__': build()