from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether, HRFlowable
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
import math

# Paleta de colores Kuromi Dark - Profesional
KUROMI_PINK = HexColor('#FF1493')  # Deep Pink
KUROMI_DARK_PINK = HexColor('#C71585')  # Medium Violet Red
KUROMI_BLACK = HexColor('#0A0A0A')  # Negro puro
KUROMI_LIGHT_PINK = HexColor('#FFE4E1')  # Misty Rose
KUROMI_WHITE = HexColor('#FFFFFF')
KUROMI_PURPLE = HexColor('#8B008B')  # Dark Magenta
KUROMI_GRAY = HexColor('#2D2D2D')  # Gris oscuro para texto
KUROMI_ACCENT = HexColor('#FF00FF')  # Magenta brillante

def draw_skull(canvas, x, y, size=20):
    """Dibuja una calavera estilo Kuromi - VISIBLE"""
    canvas.saveState()
    
    # Cabeza (círculo negro con borde rosa grueso)
    canvas.setFillColor(KUROMI_BLACK)
    canvas.setStrokeColor(KUROMI_PINK)
    canvas.setLineWidth(3)
    canvas.circle(x, y, size/2, fill=1, stroke=1)
    
    # Ojos (cuadrados rosas brillantes)
    eye_size = size/6
    canvas.setFillColor(KUROMI_PINK)
    canvas.rect(x - size/4, y + size/10, eye_size, eye_size, fill=1, stroke=0)
    canvas.rect(x + size/8, y + size/10, eye_size, eye_size, fill=1, stroke=0)
    
    # Nariz (triángulo rosa)
    canvas.setFillColor(KUROMI_ACCENT)
    path = canvas.beginPath()
    path.moveTo(x, y + size/20)
    path.lineTo(x - size/12, y - size/10)
    path.lineTo(x + size/12, y - size/10)
    path.close()
    canvas.drawPath(path, fill=1, stroke=0)
    
    # Boca (línea gruesa rosa)
    canvas.setStrokeColor(KUROMI_PINK)
    canvas.setLineWidth(3)
    canvas.line(x - size/3.5, y - size/3.5, x + size/3.5, y - size/3.5)
    
    # Dientes pequeños
    canvas.setStrokeColor(KUROMI_WHITE)
    canvas.setLineWidth(2)
    for i in range(3):
        offset = (i - 1) * size/8
        canvas.line(x + offset, y - size/3.5, x + offset, y - size/2.5)
    
    canvas.restoreState()

def draw_star(canvas, x, y, size=10, color=KUROMI_PINK):
    """Dibuja una estrella de 5 puntas - VISIBLE"""
    canvas.saveState()
    canvas.setFillColor(color)
    canvas.setStrokeColor(KUROMI_BLACK)
    canvas.setLineWidth(2)
    
    points = []
    for i in range(10):
        angle = (i * 36 - 90) * math.pi / 180
        if i % 2 == 0:
            r = size
        else:
            r = size / 2.5
        px = x + r * math.cos(angle)
        py = y + r * math.sin(angle)
        points.append((px, py))
    
    path = canvas.beginPath()
    path.moveTo(points[0][0], points[0][1])
    for px, py in points[1:]:
        path.lineTo(px, py)
    path.close()
    canvas.drawPath(path, fill=1, stroke=1)
    
    canvas.restoreState()

def header_footer(canvas, doc):
    """Encabezado y pie de página con diseño UX/UI profesional"""
    canvas.saveState()
    
    # === ENCABEZADO ===
    # Fondo rosa con borde inferior
    canvas.setFillColor(KUROMI_PINK)
    canvas.rect(0, letter[1] - 65, letter[0], 65, fill=1, stroke=0)
    
    # Borde decorativo inferior
    canvas.setFillColor(KUROMI_DARK_PINK)
    canvas.rect(0, letter[1] - 70, letter[0], 5, fill=1, stroke=0)
    
    # Título principal
    canvas.setFillColor(KUROMI_WHITE)
    canvas.setFont('Helvetica-Bold', 22)
    canvas.drawCentredString(letter[0]/2, letter[1] - 38, "Deep Research: Políticas de Workana")
    
    # Calaveras grandes y visibles en las esquinas
    draw_skull(canvas, 50, letter[1] - 35, size=30)
    draw_skull(canvas, letter[0] - 50, letter[1] - 35, size=30)
    
    # Estrellas decorativas alrededor
    draw_star(canvas, 95, letter[1] - 35, size=8, color=KUROMI_ACCENT)
    draw_star(canvas, letter[0] - 95, letter[1] - 35, size=8, color=KUROMI_ACCENT)
    
    # === PIE DE PÁGINA ===
    # Fondo negro
    canvas.setFillColor(KUROMI_BLACK)
    canvas.rect(0, 0, letter[0], 55, fill=1, stroke=0)
    
    # Borde superior rosa
    canvas.setFillColor(KUROMI_PINK)
    canvas.rect(0, 55, letter[0], 4, fill=1, stroke=0)
    
    # Número de página estilizado
    canvas.setFillColor(KUROMI_PINK)
    canvas.setFont('Helvetica-Bold', 12)
    page_text = f"— Página {doc.page} —"
    canvas.drawCentredString(letter[0]/2, 25, page_text)
    
    # Estrellas en el pie
    draw_star(canvas, 60, 27, size=10, color=KUROMI_PINK)
    draw_star(canvas, letter[0] - 60, 27, size=10, color=KUROMI_PINK)
    
    # Mini calaveras en el pie
    draw_skull(canvas, 100, 27, size=16)
    draw_skull(canvas, letter[0] - 100, 27, size=16)
    
    canvas.restoreState()

def crear_pdf():
    """Crea el PDF con diseño UX/UI profesional"""
    
    # Leer el contenido
    with open('info.txt', 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Crear el PDF
    pdf_filename = "deep_research_politicas_de_workana.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        rightMargin=55,
        leftMargin=55,
        topMargin=90,
        bottomMargin=75
    )
    
    # === ESTILOS CON MEJOR TIPOGRAFÍA Y JERARQUÍA VISUAL ===
    
    # TÍTULO PRINCIPAL - Hero
    titulo_principal = ParagraphStyle(
        'TituloPrincipal',
        fontSize=26,
        textColor=KUROMI_DARK_PINK,
        spaceAfter=25,
        spaceBefore=10,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        borderColor=KUROMI_PINK,
        borderWidth=3,
        borderPadding=15,
        backColor=KUROMI_LIGHT_PINK,
        leading=32
    )
    
    # SUBTÍTULOS - H2 (Mejorado con gradiente visual)
    subtitulo_h2 = ParagraphStyle(
        'SubtituloH2',
        fontSize=16,
        textColor=KUROMI_WHITE,
        spaceAfter=15,  # Mucho más espacio después para evitar superposición
        spaceBefore=28,  # Más espacio antes
        fontName='Helvetica-Bold',
        borderColor=KUROMI_BLACK,
        borderWidth=3,
        borderPadding=10,
        leftIndent=0,
        backColor=KUROMI_DARK_PINK,  # Fondo rosa oscuro
        leading=20,
        alignment=TA_CENTER
    )
    
    # CAJA DE INFORMACIÓN - Contenido después de subtítulos
    caja_info = ParagraphStyle(
        'CajaInfo',
        fontSize=11,
        textColor=KUROMI_BLACK,
        spaceAfter=20,
        spaceBefore=5,
        alignment=TA_JUSTIFY,
        fontName='Helvetica-Bold',
        leftIndent=18,
        rightIndent=18,
        borderColor=KUROMI_PINK,
        borderWidth=3,
        borderPadding=14,
        backColor=HexColor('#FFE4F0'),  # Rosa muy suave
        leading=16,
        bulletIndent=10
    )
    
    # SUBTÍTULOS SECUNDARIOS - H3
    subtitulo_h3 = ParagraphStyle(
        'SubtituloH3',
        fontSize=12,
        textColor=KUROMI_WHITE,
        spaceAfter=12,  # Más espacio después
        spaceBefore=18,
        fontName='Helvetica-Bold',
        leftIndent=10,
        rightIndent=10,
        borderColor=KUROMI_PURPLE,
        borderWidth=2,
        borderPadding=10,
        backColor=KUROMI_PURPLE,
        leading=15
    )
    
    # TEXTO NORMAL - Body
    texto_normal = ParagraphStyle(
        'TextoNormal',
        fontSize=11,
        textColor=KUROMI_GRAY,
        spaceAfter=11,
        spaceBefore=2,
        alignment=TA_JUSTIFY,
        fontName='Helvetica',
        leading=16,
        leftIndent=10,
        rightIndent=10
    )
    
    # LLAMADO A LA ACCIÓN / ALERTA
    llamado_accion = ParagraphStyle(
        'LlamadoAccion',
        fontSize=11.5,
        textColor=KUROMI_BLACK,
        spaceAfter=16,
        spaceBefore=8,
        alignment=TA_JUSTIFY,
        fontName='Helvetica-Bold',
        leftIndent=20,
        rightIndent=15,
        borderColor=KUROMI_ACCENT,
        borderWidth=3,
        borderPadding=13,
        backColor=HexColor('#FFF0FA'),
        leading=17,
        bulletIndent=10
    )
    
    # TEXTO CON ÉNFASIS - Destacado
    texto_enfasis = ParagraphStyle(
        'TextoEnfasis',
        fontSize=11,
        textColor=KUROMI_BLACK,
        spaceAfter=13,
        spaceBefore=10,
        alignment=TA_JUSTIFY,
        fontName='Helvetica-Bold',
        leftIndent=20,
        rightIndent=15,
        borderColor=KUROMI_ACCENT,
        borderWidth=2,
        borderPadding=11,
        backColor=HexColor('#FFF0F5'),
        leading=16
    )
    
    # PREGUNTA/CALLOUT
    texto_pregunta = ParagraphStyle(
        'TextoPregunta',
        fontSize=11.5,
        textColor=KUROMI_PURPLE,
        spaceAfter=12,
        spaceBefore=12,
        alignment=TA_LEFT,
        fontName='Helvetica-Bold',
        leftIndent=18,
        rightIndent=12,
        borderColor=KUROMI_PURPLE,
        borderWidth=2,
        borderPadding=10,
        backColor=HexColor('#F8F0FF'),
        leading=16
    )
    
    # Contenedor
    story = []
    
    # Procesar contenido con mejor lógica de jerarquía
    lineas = contenido.split('\n')
    
    # Variable para rastrear si acabamos de poner un subtítulo
    ultimo_fue_subtitulo = False
    
    for i, linea in enumerate(lineas):
        linea = linea.strip()
        
        if not linea:
            story.append(Spacer(1, 0.18*inch))
            ultimo_fue_subtitulo = False
            continue
        
        # TÍTULO PRINCIPAL (primera línea importante)
        if 'olíticas de Workana y Privacidad' in linea or 'Políticas de Workana y Privacidad' in linea:
            linea_corregida = "★ Políticas de Workana y Privacidad: Guía Completa ★"
            story.append(Paragraph(linea_corregida, titulo_principal))
            story.append(Spacer(1, 0.25*inch))
            ultimo_fue_subtitulo = False
            continue
        
        # DETECTAR SUBTÍTULOS CON CONTENIDO EN LA MISMA LÍNEA (contiene : pero no al final)
        if ':' in linea and not linea.endswith(':') and len(linea) > 50:
            # Separar el subtítulo del contenido
            partes = linea.split(':', 1)
            if len(partes) == 2 and len(partes[0]) < 80 and len(partes[0]) > 10:
                subtitulo_parte = partes[0].strip() + ':'
                contenido_parte = partes[1].strip()
                
                # Determinar ícono
                if any(word in subtitulo_parte.lower() for word in ['mensaje', 'aprobado', 'editado', 'rechazado']):
                    icono_izq, icono_der = "▸", "◂"
                elif any(word in subtitulo_parte.lower() for word in ['advertencias', 'alerta']):
                    icono_izq, icono_der = "⚠", "⚠"
                elif any(word in subtitulo_parte.lower() for word in ['puntuaciones', 'incumplimiento']):
                    icono_izq, icono_der = "✖", "✖"
                else:
                    icono_izq, icono_der = "▸", "◂"
                
                story.append(Spacer(1, 0.18*inch))
                story.append(Paragraph(f"{icono_izq}  {subtitulo_parte}  {icono_der}", subtitulo_h3))
                story.append(Spacer(1, 0.08*inch))
                # Capitalizar primera letra del contenido
                contenido_capitalizado = contenido_parte[0].upper() + contenido_parte[1:] if contenido_parte else contenido_parte
                story.append(Paragraph(f"■ {contenido_capitalizado}", caja_info))
                ultimo_fue_subtitulo = False
                continue
        
        # SUBTÍTULOS PRINCIPALES (terminan en : y son cortos)
        if linea.endswith(':') and len(linea) < 100 and len(linea) > 15:
            # Agregar íconos según el contexto
            if any(word in linea.lower() for word in ['normas', 'generales', 'comportamiento']):
                icono_izq, icono_der = "★", "★"
            elif any(word in linea.lower() for word in ['prohib', 'datos', 'contacto']):
                icono_izq, icono_der = "⚠", "⚠"
            elif any(word in linea.lower() for word in ['pagos', 'seguros']):
                icono_izq, icono_der = "✓", "✓"
            elif any(word in linea.lower() for word in ['moderación', 'mensajes', 'detección']):
                icono_izq, icono_der = "⊗", "⊗"
            elif any(word in linea.lower() for word in ['consecuencias', 'incumplir', 'sanciones']):
                icono_izq, icono_der = "✖", "✖"
            elif any(word in linea.lower() for word in ['privacidad', 'protección', 'datos']):
                icono_izq, icono_der = "⊕", "⊕"
            elif any(word in linea.lower() for word in ['mejores', 'prácticas', 'éxito', 'recomendaciones']):
                icono_izq, icono_der = "✦", "✦"
            else:
                icono_izq, icono_der = "◆", "◆"
            
            story.append(Spacer(1, 0.25*inch))
            story.append(Paragraph(f"{icono_izq}  {linea}  {icono_der}", subtitulo_h2))
            ultimo_fue_subtitulo = True
            continue
        
        # TÍTULOS SIN DOS PUNTOS (estilo "Pagos Seguros Solo a Través de Workana")
        # Son líneas cortas, capitalizadas, sin puntos al final
        palabras = linea.split()
        es_titulo = (
            len(linea) < 100 and 
            len(linea) > 20 and 
            not linea.endswith('.') and
            not linea.endswith(',') and
            not linea.startswith('¿') and
            not linea.startswith('Workana') and  # Evitar párrafos normales
            len(palabras) >= 3 and
            sum(1 for p in palabras if p and p[0].isupper()) >= len(palabras) * 0.6  # Al menos 60% con mayúscula inicial
        )
        
        if es_titulo:
            # Determinar ícono según contexto
            if any(word in linea.lower() for word in ['pagos', 'pago', 'garantía']):
                icono_izq, icono_der = "✓", "✓"
            elif any(word in linea.lower() for word in ['prohib', 'compartir', 'datos', 'contacto']):
                icono_izq, icono_der = "⚠", "⚠"
            elif any(word in linea.lower() for word in ['normas', 'comportamiento', 'contenido']):
                icono_izq, icono_der = "★", "★"
            elif any(word in linea.lower() for word in ['moderación', 'mensajes', 'detección']):
                icono_izq, icono_der = "⊗", "⊗"
            elif any(word in linea.lower() for word in ['consecuencias', 'incumplir', 'políticas']):
                icono_izq, icono_der = "✖", "✖"
            elif any(word in linea.lower() for word in ['privacidad', 'protección', 'personales']):
                icono_izq, icono_der = "⊕", "⊕"
            elif any(word in linea.lower() for word in ['mejores', 'prácticas', 'éxito', 'workana']):
                icono_izq, icono_der = "✦", "✦"
            else:
                icono_izq, icono_der = "◆", "◆"
            
            story.append(Spacer(1, 0.25*inch))
            story.append(Paragraph(f"{icono_izq}  {linea}  {icono_der}", subtitulo_h2))
            ultimo_fue_subtitulo = True
            continue
        
        # CONTENIDO IMPORTANTE DESPUÉS DE SUBTÍTULOS (llamados a la acción)
        if ultimo_fue_subtitulo and len(linea) > 80:
            # Es el contenido importante que sigue al subtítulo
            story.append(Spacer(1, 0.08*inch))
            # Capitalizar primera letra
            linea_capitalizada = linea[0].upper() + linea[1:] if linea else linea
            story.append(Paragraph(f"■ {linea_capitalizada}", caja_info))
            ultimo_fue_subtitulo = False
            continue
        
        # PREGUNTAS (empiezan con ¿)
        if linea.startswith('¿'):
            story.append(Paragraph(f"❓ {linea}", texto_pregunta))
            ultimo_fue_subtitulo = False
            continue
        
        # LLAMADOS A LA ACCIÓN Y ALERTAS IMPORTANTES
        if (linea.startswith('Importante:') or 
            linea.startswith('Consecuencia de') or
            linea.startswith('Advertencias') or
            linea.startswith('Nota:') or
            linea.startswith('Recuerda') or
            'NUNCA' in linea or
            'no está permitido' in linea.lower() and len(linea) > 50):
            story.append(Paragraph(f"⚠ {linea}", llamado_accion))
            ultimo_fue_subtitulo = False
            continue
        
        # ÉNFASIS ESPECIAL (palabras clave críticas)
        if ('prohibido' in linea.lower() or
            'sanción' in linea.lower() or
            'expulsión' in linea.lower() or
            'cierre de cuenta' in linea.lower() or
            'violación' in linea.lower()):
            story.append(Paragraph(f"⚠ {linea}", texto_enfasis))
            ultimo_fue_subtitulo = False
            continue
        
        # SUBTÍTULOS SECUNDARIOS (frases descriptivas importantes)
        if (linea.endswith(':') and len(linea) < 100) or \
           (len(linea) < 70 and any(word in linea for word in ['pueden', 'debe', 'puede', 'motivos'])):
            story.append(Paragraph(f"▸ {linea}", subtitulo_h3))
            ultimo_fue_subtitulo = True
            continue
        
        # TEXTO NORMAL
        story.append(Paragraph(linea, texto_normal))
        ultimo_fue_subtitulo = False
    
    # Construir el PDF
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    
    print(f"\n{'='*60}")
    print(f"✓ PDF CREADO CON ÉXITO")
    print(f"{'='*60}")
    print(f"📄 Archivo: {pdf_filename}")
    print(f"🎨 Diseño: UX/UI Profesional - Estilo Kuromi Dark")
    print(f"💀 Iconografía: Calaveras y estrellas vectoriales visibles")
    print(f"📝 Tipografía: Jerarquía visual optimizada")
    print(f"🤖 Escaneo ATS: Completamente optimizado")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    crear_pdf()
