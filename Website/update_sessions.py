import os
import re
import markdown

SESSIONS_DIR = '../Sessions'
INDEX_FILE = 'index.html'

sessions = []

def extract_title(content):
    """Extract the proper title from markdown content"""
    lines = content.split('\n')
    
    # Get the H1 title (first line)
    h1_title = lines[0].strip('# ').strip() if lines else 'Untitled Session'
    
    # If H1 is generic "Session Topic", look for the actual topic in the content
    if h1_title == "Session Topic":
        for line in lines:
            # Look for lines like "- **Topic**: Amazon Dynamo" or "- **Topic:** Mysticeti"
            topic_match = re.search(r'-\s*\*\*Topic\*\*:?\s*(.+)', line)
            if topic_match:
                return topic_match.group(1).strip()
    
    return h1_title

def markdown_to_html(markdown_content):
    """Convert markdown content to HTML"""
    md = markdown.Markdown(extensions=['extra', 'codehilite'])
    return md.convert(markdown_content)

def create_session_id(title):
    """Create a URL-friendly ID from title"""
    return re.sub(r'[^a-zA-Z0-9]', '-', title.lower()).strip('-')

# Process all session files
for filename in os.listdir(SESSIONS_DIR):
    if filename.endswith('.md') and filename != 'template.md':  # Skip template
        with open(os.path.join(SESSIONS_DIR, filename), 'r') as f:
            content = f.read()
            title = extract_title(content)
            session_id = create_session_id(title)
            html_content = markdown_to_html(content)
            sessions.append({
                'title': title, 
                'content': content,
                'html_content': html_content,
                'id': session_id
            })

# Sort sessions alphabetically by title
sessions.sort(key=lambda x: x['title'])

# Generate the HTML content
session_links_html = ""
session_content_html = ""

for session in sessions:
    # Create navigation link
    session_links_html += f'        <a href="#{session["id"]}">{session["title"]}</a>\n'
    
    # Create session content section
    session_content_html += f'''
    <div id="{session["id"]}" class="session-section">
        <a href="index.html" class="back-link">&larr; Back to sessions</a>
        <div class="session-content-inner">
            {session["html_content"]}
        </div>
    </div>
'''

# Create the complete HTML
html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fault Tolerant Friends</title>
    <link rel="icon" type="image/x-icon" data-emoji="💾" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>💾</text></svg>">
    <link rel="apple-touch-icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>💾</text></svg>">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>&lt;Fault Tolerant Friends&gt;</h1>
    
{session_content_html}
    
    <div class="session-list">
{session_links_html}    </div>
    
    <div id="footer" style="text-align: center; margin-top: 40px; font-family: 'Courier New', Courier, monospace; white-space: normal; background-color: #0000AA; padding: 5px 0; font-size: 1vw;">
        <div style="margin-bottom: 15px;">
            <a href="https://t.me/+6-M1xag7xs05ZTlh" target="_blank" style="color: #FFFFFF; text-decoration: none; font-size: 0.8em; display: inline-block; padding: 8px 16px; border: 1px solid rgba(255, 255, 255, 0.3); border-radius: 15px; background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); transition: all 0.3s ease;">
                <span style="margin-right: 6px;">📱</span>Join the Telegram Chat
            </a>
        </div>
        <div style="white-space: pre; font-size: 1vw;">
        ...........           ...........           ...........
       .'------.'.|         .'------.'.|         .'------.'.|
      | .-----. | |        | .-----. | |        | .-----. | |
      | |     | | |        | |     | | |        | |     | | |
    __| |     | | |;     __| |     | | |;     __| |     | | |;
   /  |*`-----'.|.'     /  |*`-----'.|.'     /  |*`-----'.|.'
  /   `---------'      /   `---------'      /   `---------'
  |                    |                    |
  +--------------------+--------------------+
        </div>
    </div>
</body>
</html>'''

# Write the HTML file
with open(INDEX_FILE, 'w') as f:
    f.write(html_template)

print(f"Successfully processed {len(sessions)} sessions:")
for session in sessions:
    print(f"  - {session['title']}") 