
import json
import os
import html
from datetime import datetime

# ----------------------------
# User: set your JSON path here
# ----------------------------
json_path = r"C:\Users\PCS\Downloads\1\conversations.json"

# Output folder
output_dir = "chat_html"
os.makedirs(output_dir, exist_ok=True)

# ----------------------------
# Load JSON
# ----------------------------
print("📂 Loading JSON, please wait...")
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Normalize top-level conversations list
if isinstance(data, dict):
    convos = data.get("conversations") or data.get("items") or []
elif isinstance(data, list):
    convos = data
else:
    print("❌ Unsupported JSON structure.")
    exit()

print(f"✅ Total conversations found: {len(convos)}")

# Helper: convert text to safe HTML (escape + preserve line breaks)
def to_html(text):
    if text is None:
        return ""
    # escape HTML special chars and replace double newlines with paragraph breaks
    escaped = html.escape(text)
    # Convert single newlines to <br>
    return escaped.replace("\r\n", "\n").replace("\r", "\n").replace("\n", "<br>\n")

# Helper: try to extract messages from a conversation object
def extract_messages(convo):
    """
    Returns a list of (role, text) tuples in order.
    Handles several common export formats:
    - convo['mapping'] -> dict of message objects
    - convo['messages'] -> list of message objects
    - convo may directly be a message list (if top-level was just list)
    Each message object: message['author']['role'] and message['content']['parts'] (list)
    """
    msgs = []

    # Case 1: mapping (OpenAI export format)
    mapping = convo.get("mapping") if isinstance(convo, dict) else None
    if mapping and isinstance(mapping, dict):
        # mapping is usually unordered; try to sort by keys if keys are timestamps/ints; else keep insertion order
        for k, v in mapping.items():
            message = v.get("message") if isinstance(v, dict) else None
            if not message:
                continue
            role = message.get("author", {}).get("role", "unknown")
            parts = message.get("content", {}).get("parts", [])
            text = "\n".join(parts) if parts else ""
            msgs.append((role, text))
        return msgs

    # Case 2: messages list inside convo
    messages_list = convo.get("messages") if isinstance(convo, dict) else None
    if messages_list and isinstance(messages_list, list):
        for m in messages_list:
            # Different formats: m may directly have 'role' and 'content' or nested 'message'
            if "message" in m and isinstance(m["message"], dict):
                message = m["message"]
                role = message.get("author", {}).get("role", "unknown")
                parts = message.get("content", {}).get("parts", [])
                text = "\n".join(parts) if parts else ""
            else:
                role = m.get("role") or m.get("author") or "unknown"
                # content might be string or dict
                if isinstance(m.get("content"), dict):
                    parts = m["content"].get("parts", [])
                    text = "\n".join(parts) if parts else ""
                else:
                    text = m.get("content") or m.get("text") or ""
            msgs.append((role, text))
        return msgs

    # Case 3: convo itself might be a message-like dict (top-level list of messages)
    if isinstance(convo, dict):
        # Try common keys: 'author' + 'content'
        if "author" in convo and "content" in convo:
            role = convo.get("author", {}).get("role", "unknown")
            parts = convo.get("content", {}).get("parts", [])
            text = "\n".join(parts) if parts else ""
            msgs.append((role, text))
            return msgs

    # Fallback: no recognizable messages
    return msgs

# Basic HTML template parts (inline CSS for simplicity)
HTML_HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Conversation</title>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial; background:#f4f6f8; margin:0; padding:20px; }
.container { max-width:900px; margin:0 auto; }
.header { margin-bottom:16px; }
.card { background:white; border-radius:12px; padding:18px; box-shadow:0 2px 6px rgba(0,0,0,0.06); }
.message { margin:10px 0; padding:12px 14px; border-radius:12px; display:inline-block; max-width:86%; line-height:1.5; }
.user { background: #e8f0ff; color:#0b2545; align-self:flex-end; border-top-right-radius:4px; }
.assistant { background: #e9f7ee; color:#08321a; border-top-left-radius:4px; }
.meta { font-size:0.85rem; color:#666; margin-bottom:8px; }
.divider { height:1px; background:#eee; margin:12px 0; }
</style>
</head>
<body>
<div class="container">
"""

HTML_FOOT = """
</div>
</body>
</html>
"""

# ----------------------------
# Generate HTML files
# ----------------------------
created = 0
for i, convo in enumerate(convos, start=1):
    messages = extract_messages(convo)
    if not messages:
        # skip empty ones
        continue

    # Try to build a friendly title (if convo has 'title' or 'create_time' etc)
    title = convo.get("title") if isinstance(convo, dict) else None
    if not title:
        # try id or created time
        cid = convo.get("id") if isinstance(convo, dict) else None
        created_time = convo.get("create_time") if isinstance(convo, dict) else None
        if created_time:
            # if timestamp like 167... try to format as date; else keep raw
            try:
                ts = int(created_time)
                # assume seconds
                title = datetime.fromtimestamp(ts).isoformat(sep=' ')
            except Exception:
                title = str(created_time)
        elif cid:
            title = str(cid)
        else:
            title = f"Conversation {i}"

    # Build HTML content
    body_parts = []
    body_parts.append(f'<div class="header"><h2>{html.escape(title)}</h2><div class="meta">Conversation #{i}</div></div>')
    body_parts.append('<div class="card">')

    for role, text in messages:
        safe_html = to_html(text)
        role_lower = (role or "").lower()
        if "user" in role_lower:
            body_parts.append(f'<div class="message user"><strong>👤 User</strong><br>{safe_html}</div>')
        elif "assistant" in role_lower or "system" not in role_lower and ("assistant" in role_lower or "assistant" in str(role_lower)):
            # treat assistant or chatgpt as assistant
            body_parts.append(f'<div class="message assistant"><strong>🤖 ChatGPT</strong><br>{safe_html}</div>')
        elif "system" in role_lower:
            body_parts.append(f'<div class="message" style="background:#f0f0f0;color:#333;"><strong>System</strong><br>{safe_html}</div>')
        else:
            # unknown role
            body_parts.append(f'<div class="message" style="background:#fff7e6;color:#5a3900;"><strong>{html.escape(str(role))}</strong><br>{safe_html}</div>')

    body_parts.append('</div>')  # close card

    html_content = HTML_HEAD + "\n".join(body_parts) + HTML_FOOT

    # safe filename
    safe_title = "".join(c for c in title if c.isalnum() or c in (" ", "-", "_")).rstrip()
    filename = os.path.join(output_dir, f"conversation_{i}_{safe_title[:60].strip().replace(' ','_')}.html")
    with open(filename, "w", encoding="utf-8") as out:
        out.write(html_content)

    print(f"💾 Saved: {filename}")
    created += 1

print(f"\n🎉 Done. {created} HTML files created in: {os.path.abspath(output_dir)}")

#export chats to markdown

# import json
# import os

# # -------------------------------------------
# # 🔹 Apni JSON file ka path yahan likhein:
# # -------------------------------------------
# json_path = r"C:\Users\PCS\Downloads\1\conversations.json"

# # Output folder
# output_dir = "chat_markdowns"
# os.makedirs(output_dir, exist_ok=True)

# # -------------------------------------------
# # Load JSON file
# # -------------------------------------------
# print("📂 Loading data, please wait...")
# with open(json_path, "r", encoding="utf-8") as f:
#     data = json.load(f)

# # 🔹 Detect structure automatically
# if isinstance(data, dict):
#     convos = data.get("conversations", [])
# elif isinstance(data, list):
#     convos = data
# else:
#     print("❌ Unsupported JSON structure.")
#     exit()

# print(f"✅ Total conversations found: {len(convos)}")

# # -------------------------------------------
# # Generate Markdown Files
# # -------------------------------------------
# for i, convo in enumerate(convos, start=1):
#     chat_id = convo.get("id", f"chat_{i}")
#     mapping = convo.get("mapping", {})

#     if not mapping:
#         continue

#     lines = []
#     lines.append(f"# 💬 Conversation {i}\n")

#     for msg_id, msg_data in mapping.items():
#         message = msg_data.get("message")
#         if not message:
#             continue

#         role = message.get("author", {}).get("role", "")
#         text_parts = message.get("content", {}).get("parts", [])
#         if not text_parts:
#             continue

#         text = "\n".join(text_parts).strip()
#         if not text:
#             continue

#         # Role formatting
#         if role == "user":
#             lines.append(f"**👤 User:**\n{text}\n")
#         elif role == "assistant":
#             lines.append(f"**🤖 ChatGPT:**\n{text}\n")
#         else:
#             lines.append(f"**🧩 {role.capitalize()}:**\n{text}\n")

#         lines.append("---\n")  # separator

#     md_filename = os.path.join(output_dir, f"conversation_{i}.md")
#     with open(md_filename, "w", encoding="utf-8") as md_file:
#         md_file.write("\n".join(lines))

#     print(f"💾 Saved: {md_filename}")

# print("\n🎉 All conversations have been successfully converted into Markdown files!")
# print(f"📁 Output folder: {os.path.abspath(output_dir)}")



#export chats to pdfs

# import json
# import os
# from reportlab.lib.pagesizes import A4
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
# from reportlab.lib.units import inch
# from reportlab.lib import colors

# # -------------------------------------------
# # 🔹 Apni JSON file ka path yahan likhein:
# # مثال:
# # json_path = r"C:\Users\PCS\Downloads\conversations.json"
# # -------------------------------------------
# json_path = r"C:\Users\PCS\Downloads\1\conversations.json"

# # Output folder
# output_dir = "chat_pdfs"
# os.makedirs(output_dir, exist_ok=True)

# # -------------------------------------------
# # Load JSON file
# # -------------------------------------------
# print("📂 Loading data, please wait...")
# with open(json_path, "r", encoding="utf-8") as f:
#     data = json.load(f)

# # 🔹 Detect structure automatically
# if isinstance(data, dict):
#     convos = data.get("conversations", [])
# elif isinstance(data, list):
#     convos = data
# else:
#     print("❌ Unsupported JSON structure.")
#     exit()

# print(f"✅ Total conversations found: {len(convos)}")

# # -------------------------------------------
# # PDF Styles
# # -------------------------------------------
# styles = getSampleStyleSheet()
# styles.add(ParagraphStyle(name='User', textColor=colors.blue, leading=16))
# styles.add(ParagraphStyle(name='Assistant', textColor=colors.green, leading=16))
# styles.add(ParagraphStyle(name='System', textColor=colors.gray, leading=16))

# # -------------------------------------------
# # Generate PDFs
# # -------------------------------------------
# for i, convo in enumerate(convos, start=1):
#     chat_id = convo.get("id", f"chat_{i}")
#     mapping = convo.get("mapping", {})

#     if not mapping:
#         continue

#     story = []
#     story.append(Paragraph(f"<b>Conversation {i}</b>", styles["Title"]))
#     story.append(Spacer(1, 0.2 * inch))

#     for msg_id, msg_data in mapping.items():
#         message = msg_data.get("message")
#         if not message:
#             continue

#         role = message.get("author", {}).get("role", "")
#         text_parts = message.get("content", {}).get("parts", [])
#         if not text_parts:
#             continue

#         text = "\n".join(text_parts).strip()
#         if not text:
#             continue

#         if role == "user":
#             p = Paragraph(f"<b>User:</b> {text}", styles["User"])
#         elif role == "assistant":
#             p = Paragraph(f"<b>ChatGPT:</b> {text}", styles["Assistant"])
#         else:
#             p = Paragraph(f"<b>{role.capitalize()}:</b> {text}", styles["System"])

#         story.append(p)
#         story.append(Spacer(1, 0.1 * inch))

#     pdf_filename = os.path.join(output_dir, f"conversation_{i}.pdf")
#     doc = SimpleDocTemplate(pdf_filename, pagesize=A4)
#     doc.build(story)

#     print(f"💾 Saved: {pdf_filename}")

# print("\n🎉 All conversations have been successfully converted into PDFs!")
# print(f"📁 Output folder: {os.path.abspath(output_dir)}")
