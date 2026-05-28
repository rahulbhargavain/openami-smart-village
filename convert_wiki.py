import os
import re
import shutil

# Paths
SRC_DIR = r"C:\Users\rhlbh\.gemini\antigravity\scratch\sattal-pitch\extracted_pages"
MD_OUT_DIR = r"C:\Users\rhlbh\.gemini\antigravity\scratch\sattal-pitch\wiki-markdown"
HTML_OUT_DIR = r"C:\Users\rhlbh\.gemini\antigravity\scratch\sattal-pitch\wiki"

os.makedirs(MD_OUT_DIR, exist_ok=True)
os.makedirs(HTML_OUT_DIR, exist_ok=True)

# Styling template
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — IEEE Smart Village Wiki</title>
  <meta name="description" content="Centralized collaborate archive for IEEE Smart Village Wiki. Migrated from DokuWiki with version control.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #f8fafc;
      --bg2: #f1f5f9;
      --card: #ffffff;
      --border: #e2e8f0;
      --teal: #0891b2;
      --teal-dim: rgba(8, 145, 178, 0.08);
      --text: #0f172a;
      --sub: #475569;
      --muted: #64748b;
    }}
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text); line-height: 1.75; }}
    
    header {{
      background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
      color: white; padding: 24px 40px; border-bottom: 3px solid var(--teal);
    }}
    header .container {{ display: flex; justify-content: space-between; align-items: center; max-width: 1200px; margin: 0 auto; }}
    header h1 {{ font-size: 1.4rem; font-weight: 800; letter-spacing: -0.02em; display: flex; align-items: center; gap: 8px; }}
    header h1 strong {{ color: var(--teal); }}
    header nav a {{ color: #cbd5e1; text-decoration: none; font-size: 0.85rem; font-weight: 600; margin-left: 20px; transition: color 0.2s; }}
    header nav a:hover {{ color: white; }}

    .main-layout {{ max-width: 1200px; margin: 40px auto; padding: 0 40px; display: grid; grid-template-columns: 3fr 1fr; gap: 40px; }}
    .content-card {{ background: var(--card); border: 1px solid var(--border); border-radius: 16px; padding: 40px; box-shadow: 0 4px 12px rgba(15,23,42,0.02); }}
    
    h1, h2, h3, h4, h5 {{ font-weight: 800; letter-spacing: -0.02em; color: var(--text); margin-top: 1.8em; margin-bottom: 0.6em; line-height: 1.25; }}
    h1 {{ font-size: 2.2rem; border-bottom: 2px solid var(--border); padding-bottom: 12px; margin-top: 0; }}
    h2 {{ font-size: 1.6rem; border-bottom: 1px solid var(--border); padding-bottom: 8px; }}
    h3 {{ font-size: 1.25rem; }}
    
    p {{ margin-bottom: 1.5em; font-size: 0.95rem; color: var(--sub); }}
    strong {{ color: var(--text); }}
    
    /* Links */
    a {{ color: var(--teal); text-decoration: none; font-weight: 500; transition: color 0.2s; }}
    a:hover {{ color: #06b6d4; text-decoration: underline; }}
    
    /* Lists */
    ul, ol {{ margin-bottom: 1.5em; padding-left: 24px; }}
    li {{ font-size: 0.95rem; color: var(--sub); margin-bottom: 0.5em; }}
    
    /* Tables */
    .table-wrapper {{ overflow-x: auto; border-radius: 12px; border: 1px solid var(--border); margin: 28px 0; box-shadow: 0 2px 8px rgba(15,23,42,0.02); }}
    table {{ width: 100%; border-collapse: collapse; font-size: 0.85rem; text-align: left; }}
    thead tr {{ background: rgba(8, 145, 178, 0.06); border-bottom: 1px solid var(--border); }}
    th {{ padding: 12px 16px; font-weight: 700; color: var(--teal); text-transform: uppercase; letter-spacing: 0.5px; font-size: 0.75rem; }}
    td {{ padding: 12px 16px; border-top: 1px solid var(--border); color: var(--sub); vertical-align: middle; }}
    tr:hover td {{ background: rgba(8, 145, 178, 0.01); }}
    
    /* PDF/Attachment Cards */
    .pdf-card {{ display: flex; align-items: center; gap: 16px; padding: 18px 24px; border: 1px solid var(--border); border-radius: 12px; margin: 24px 0; background: var(--bg); }}
    .pdf-icon {{ font-size: 2rem; color: var(--teal); }}
    .pdf-info {{ flex: 1; }}
    .pdf-title {{ font-weight: 700; font-size: 0.9rem; color: var(--text); margin-bottom: 4px; }}
    .pdf-btn {{ display: inline-flex; align-items: center; justify-content: center; padding: 6px 14px; background: var(--teal); color: white !important; font-size: 0.78rem; font-weight: 700; border-radius: 6px; text-decoration: none !important; transition: background 0.2s; }}
    .pdf-btn:hover {{ background: #06b6d4; }}
    
    /* Image Styling */
    .wiki-image {{ max-width: 100%; border-radius: 8px; border: 1px solid var(--border); box-shadow: 0 4px 12px rgba(15,23,42,0.04); margin: 20px 0; display: block; }}
    
    /* Sidebar */
    .sidebar {{ display: flex; flex-direction: column; gap: 24px; }}
    .sidebar-card {{ background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 24px; box-shadow: 0 4px 12px rgba(15,23,42,0.01); }}
    .sidebar-title {{ font-size: 0.85rem; font-weight: 800; color: var(--teal); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 14px; border-bottom: 1px solid var(--border); padding-bottom: 8px; }}
    .sidebar-list {{ list-style: none; padding: 0; }}
    .sidebar-list li {{ font-size: 0.85rem; margin-bottom: 8px; }}
    
    hr {{ border: 0; border-top: 1px solid var(--border); margin: 32px 0; }}
    footer {{ background: var(--bg2); border-top: 1px solid var(--border); padding: 36px 40px; text-align: center; color: var(--muted); font-size: 0.8rem; margin-top: 60px; }}
    footer strong {{ color: var(--teal); }}
    
    @media(max-width: 768px) {{
      .main-layout {{ grid-template-columns: 1fr; gap: 30px; margin: 20px auto; padding: 0 20px; }}
      header {{ padding: 20px; }}
    }}
  </style>
</head>
<body>

<header>
  <div class="container">
    <h1>🌐 IEEE Smart Village <strong>Wiki</strong></h1>
    <nav>
      <a href="/wiki/home">Home</a>
      <a href="/reports">Reports Index</a>
    </nav>
  </div>
</header>

<div class="main-layout">
  <article class="content-card">
    {content}
  </article>
  
  <aside class="sidebar">
    <div class="sidebar-card">
      <div class="sidebar-title">Navigation</div>
      <ul class="sidebar-list">
        <li><a href="/wiki/home">🏠 Wiki Home</a></li>
        <li><a href="/wiki/wiki/syntax">📝 Syntax Guide</a></li>
        <li><a href="/wiki/ieeeguidelines">⚖️ IEEE Guidelines</a></li>
        <li><a href="/wiki/playground/playground">🧪 Wiki Playground</a></li>
        <li><a href="/wiki/wg/tech">⚙️ Technology Committee</a></li>
        <li><a href="/wiki/home/technologies">🏭 Technologies Hub</a></li>
        <li><a href="/wiki/home/projects">🌍 Initiatives Index</a></li>
      </ul>
    </div>
    
    <div class="sidebar-card">
      <div class="sidebar-title">Repository</div>
      <p style="font-size: 0.78rem; color: var(--muted); margin-bottom: 12px;">This wiki is fully version-controlled on GitHub with continuous integration deployment.</p>
      <a href="https://github.com/rahulbhargavain/openami-smart-village" target="_blank" style="font-size: 0.8rem; font-weight: 700; color: var(--teal);">📂 View on GitHub</a>
    </div>
  </aside>
</div>

<footer>
  <p>© 2026 <strong>IEEE Smart Village</strong> · <strong>wiki.smartvillage.ieee.org</strong> · Migrated by Antigravity</p>
</footer>

</body>
</html>
"""

def clean_dokuwiki_formatting(content):
    """
    Parses DokuWiki text formatting recursively into GFM Markdown syntax.
    """
    # 1. Bold: **bold** -> **bold** (already matches)
    
    # 2. Italic: //italic// -> *italic* (ignore URL protocol double slashes)
    content = re.sub(r'(?<!https:)(?<!http:)//(.*?)(?<!https:)(?<!http:)//', r'*\1*', content)
    
    # 3. Underline: __underline__ -> <u>underline</u>
    content = re.sub(r'__(.*?)__', r'<u>\1</u>', content)
    
    # 4. Code: ''code'' -> `code`
    content = re.sub(r"''(.*?)''", r'`\1`', content)
    
    # 5. Horizontal rule: ---- -> ---
    content = re.sub(r'^----+', '---', content, flags=re.MULTILINE)
    
    # 6. Line break: \\ followed by space or end of line -> <br>
    content = re.sub(r'\\\\(\s|$)', r'<br>\1', content)
    
    return content

def parse_headings(content):
    """
    Translates DokuWiki H1-H5 boundaries to GFM markdown.
    """
    # ====== Heading 1 ====== -> # Heading 1
    content = re.sub(r'^======\s*(.*?)\s*======\s*$', r'# \1', content, flags=re.MULTILINE)
    # ===== Heading 2 ===== -> ## Heading 2
    content = re.sub(r'^=====\s*(.*?)\s*=====\s*$', r'## \1', content, flags=re.MULTILINE)
    # ==== Heading 3 ==== -> ### Heading 3
    content = re.sub(r'^====\s*(.*?)\s*====\s*$', r'### \1', content, flags=re.MULTILINE)
    # === Heading 4 === -> #### Heading 4
    content = re.sub(r'^===\s*(.*?)\s*===\s*$', r'#### \1', content, flags=re.MULTILINE)
    # == Heading 5 == -> ##### Heading 5
    content = re.sub(r'^==\s*(.*?)\s*==\s*$', r'##### \1', content, flags=re.MULTILINE)
    
    return content

def parse_lists(content):
    """
    Translates DokuWiki indent lists to GFM Markdown lists.
    """
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        # Check if line starts with spaces followed by * or -
        bullet_match = re.match(r'^(\s+)\*\s*(.*)$', line)
        number_match = re.match(r'^(\s+)-\s*(.*)$', line)
        if bullet_match:
            new_lines.append('* ' + bullet_match.group(2))
        elif number_match:
            new_lines.append('1. ' + number_match.group(2))
        else:
            new_lines.append(line)
    return '\n'.join(new_lines)

def parse_links(content):
    """
    Translates DokuWiki internal and external links into GFM.
    """
    def replace_link(match):
        target = match.group(1).strip()
        text = match.group(2).strip() if match.group(2) else ""
        
        # If it's an external link
        if target.startswith("http://") or target.startswith("https://"):
            display_text = text if text else target
            return f"[{display_text}]({target})"
        
        # If it's an internal DokuWiki path link
        # SGC/PAN paths represent absolute or relative paths with colons
        clean_target = target
        if clean_target.startswith(":"):
            clean_target = clean_target[1:]
        
        # Map colons to slashes
        clean_target = clean_target.replace(":", "/")
        
        # Resolve target name
        if not text:
            display_text = clean_target.split("/")[-1].replace("_", " ").title()
        else:
            display_text = text
            
        # Clean relative URLs served cleanly via Firebase Hosting
        return f"[{display_text}](/wiki/{clean_target})"
        
    # Pattern: [[target|text]] or [[target]]
    content = re.sub(r'\[\[([^\]|]+)(?:\|([^\]]*))?\]\]', replace_link, content)
    return content

def parse_media(content):
    """
    Translates DokuWiki media/image/PDF embeds into standard markdown/HTML.
    """
    # 1. Handle pdfjs embeds
    # {{pdfjs 100%,800px>:home:technologies:powerledger_transactive_energy_solutions_v2_pdf.pdf}}
    def replace_pdf(match):
        pdf_path = match.group(1).strip()
        if pdf_path.startswith(":"):
            pdf_path = pdf_path[1:]
        pdf_path = pdf_path.replace(":", "/")
        filename = pdf_path.split("/")[-1]
        display_title = filename.replace("_pdf.pdf", ".pdf").replace("_", " ").title()
        
        # HTML responsive card
        return f"""
<div class="pdf-card">
  <span class="pdf-icon">📄</span>
  <div class="pdf-info">
    <div class="pdf-title">{display_title}</div>
    <a href="/media/{pdf_path}" class="pdf-btn" target="_blank">View / Download PDF Manual</a>
  </div>
</div>
"""
    content = re.sub(r'\{\{pdfjs[^>]*>(.*?)\}\}', replace_pdf, content)

    # 2. Handle image embeds
    # {{  :isv_org.png?nolink&400}} or {{ :boxen-1.png?direct&800 |}}
    def replace_image(match):
        img_path = match.group(1).strip()
        # strip parameters like ?nolink&400
        clean_path = img_path.split("?")[0].strip()
        if clean_path.startswith(":"):
            clean_path = clean_path[1:]
        clean_path = clean_path.replace(":", "/")
        
        # HTML visual component
        return f'<img src="/media/{clean_path}" class="wiki-image" alt="Embedded Image">'
        
    content = re.sub(r'\{\{\s*([^}]+?\.(?:png|jpg|jpeg|gif|svg|bmp)[^}]*?)\}\}', replace_image, content)
    return content

def parse_tables(content):
    """
    Translates DokuWiki tables into GFM Markdown tables.
    """
    lines = content.split('\n')
    new_lines = []
    in_table = False
    col_count = 0
    
    for line in lines:
        is_header = line.strip().startswith('^')
        is_row = line.strip().startswith('|')
        
        if is_header or is_row:
            in_table = True
            # Split by column separators
            sep = '^' if is_header else '|'
            parts = [p.strip() for p in line.strip().split(sep) if p.strip() or p == '']
            # Clean empty elements at ends
            if parts and parts[0] == '': parts = parts[1:]
            if parts and parts[-1] == '': parts = parts[:-1]
            
            # Format row
            formatted_row = "| " + " | ".join(parts) + " |"
            new_lines.append(formatted_row)
            
            if is_header:
                col_count = len(parts)
                # Output a separator row
                separator_row = "| " + " | ".join(["---"] * col_count) + " |"
                new_lines.append(separator_row)
        else:
            in_table = False
            new_lines.append(line)
            
    return '\n'.join(new_lines)

def convert_markdown_to_html(md_content):
    """
    Converts compiled GFM Markdown into semantic, publication-grade HTML body elements.
    """
    lines = md_content.split('\n')
    html_lines = []
    
    in_ul = False
    in_ol = False
    in_table = False
    p_buffer = []
    
    def format_inline_html(text):
        # Format markdown links [text](url) -> <a href="url">text</a>
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
        # Format bold (handle greedy matching gracefully by using non-greedy)
        text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
        # Format inline code
        text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
        return text

    def flush_p_buffer():
        if p_buffer:
            p_text = " ".join(p_buffer).strip()
            if p_text:
                html_lines.append(f"<p>{format_inline_html(p_text)}</p>")
            p_buffer.clear()

    for line in lines:
        stripped = line.strip()
        is_ul = stripped.startswith('* ')
        is_ol = stripped.startswith('1. ') or re.match(r'^\d+\.\s', stripped)
        is_table = stripped.startswith('|')
        is_header = re.match(r'^(#{1,6})\s*(.*)$', stripped)
        is_hr = (stripped == "---")
        is_img = stripped.startswith('<img')
        is_pdf = stripped.startswith('<div class="pdf-card"')
        
        # If we hit a block element or empty line, flush paragraph buffer
        if is_ul or is_ol or is_table or is_header or is_hr or is_img or is_pdf or stripped == "":
            flush_p_buffer()
            
        # Handle list/table transitions
        if in_ul and not is_ul:
            html_lines.append("</ul>")
            in_ul = False
        if in_ol and not is_ol:
            html_lines.append("</ol>")
            in_ol = False
        if in_table and not is_table:
            html_lines.append("</tbody></table></div>")
            in_table = False
            
        if is_ul:
            if not in_ul:
                html_lines.append("<ul>")
                in_ul = True
            item_text = stripped[2:]
            html_lines.append(f"  <li>{format_inline_html(item_text)}</li>")
        elif is_ol:
            if not in_ol:
                html_lines.append("<ol>")
                in_ol = True
            item_text = re.sub(r'^\d+\.\s*', '', stripped)
            html_lines.append(f"  <li>{format_inline_html(item_text)}</li>")
        elif is_table:
            if not in_table:
                html_lines.append('<div class="table-wrapper"><table>')
                in_table = True
            
            parts = [p.strip() for p in stripped.split('|')[1:-1]]
            if all(p.startswith('-') for p in parts):
                html_lines.append("<tbody>")
                continue
                
            # If the last line added was the start of the table, this must be the header row
            if len(html_lines) > 0 and html_lines[-1] == '<div class="table-wrapper"><table>':
                html_lines.append("<thead><tr>")
                for p in parts:
                    html_lines.append(f"  <th>{format_inline_html(p)}</th>")
                html_lines.append("</tr></thead>")
            else:
                html_lines.append("<tr>")
                for p in parts:
                    html_lines.append(f"  <td>{format_inline_html(p)}</td>")
                html_lines.append("</tr>")
        elif is_header:
            level = len(is_header.group(1))
            title = is_header.group(2)
            html_lines.append(f"<h{level}>{format_inline_html(title)}</h{level}>")
        elif is_hr:
            html_lines.append("<hr>")
        elif is_img or is_pdf:
            html_lines.append(stripped)
        elif stripped != "":
            p_buffer.append(stripped)
            
    # Flush remaining paragraph buffer
    flush_p_buffer()
    
    # Close any open structures
    if in_ul: html_lines.append("</ul>")
    if in_ol: html_lines.append("</ol>")
    if in_table: html_lines.append("</tbody></table></div>")
    
    return '\n'.join(html_lines)
                
    # Close any open structures
    if in_ul: html_lines.append("</ul>")
    if in_ol: html_lines.append("</ol>")
    if in_table: html_lines.append("</tbody></table></div>")
    
    return '\n'.join(html_lines)

def process_file(src_path, relative_path):
    """
    Main file pipeline: Read DokuWiki -> translate to GFM -> save GFM -> compile GFM to HTML -> save HTML.
    """
    with open(src_path, "r", encoding="utf-8", errors="ignore") as f:
        raw_content = f.read()
        
    # Enforce basic standard GFM translations
    content = clean_dokuwiki_formatting(raw_content)
    content = parse_headings(content)
    content = parse_lists(content)
    content = parse_tables(content)
    content = parse_media(content)
    content = parse_links(content)
    
    # Save the GFM file (.md)
    md_rel_path = relative_path.replace(".txt", ".md")
    md_dest_path = os.path.join(MD_OUT_DIR, md_rel_path)
    os.makedirs(os.path.dirname(md_dest_path), exist_ok=True)
    with open(md_dest_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    # Compile the Markdown to styled HTML body
    html_body = convert_markdown_to_html(content)
    
    # Wrap in our premium Slate/Teal shell layout
    title_name = os.path.basename(md_rel_path).replace(".md", "").replace("_", " ").title()
    full_html = HTML_TEMPLATE.format(title=title_name, content=html_body)
    
    # Save the HTML file (.html)
    html_rel_path = relative_path.replace(".txt", ".html")
    html_dest_path = os.path.join(HTML_OUT_DIR, html_rel_path)
    os.makedirs(os.path.dirname(html_dest_path), exist_ok=True)
    with open(html_dest_path, "w", encoding="utf-8") as f:
        f.write(full_html)

# Recursively crawl the pages
print("Crawling through extracted files...")
count = 0
for root, dirs, files in os.walk(SRC_DIR):
    for file in files:
        if file.endswith(".txt"):
            abs_path = os.path.join(root, file)
            rel_path = os.path.relpath(abs_path, SRC_DIR)
            process_file(abs_path, rel_path)
            count += 1

print(f"Success! Converted {count} DokuWiki pages to GFM Markdown and premium HTML.")
