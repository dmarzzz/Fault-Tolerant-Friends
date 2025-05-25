# Fault Tolerant Friends Website

A retro-styled website for the Fault Tolerant Friends distributed systems study group, featuring a Blue Screen of Death aesthetic with neon glowing effects.

## 🚀 Quick Start

### Prerequisites

- Python 3.x
- `markdown` package

### Installation

1. Install the required Python package:
   ```bash
   pip3 install --break-system-packages markdown
   ```
   
   *Note: Use `--break-system-packages` flag if you encounter an "externally-managed-environment" error on macOS/Linux.*

### Usage

2. Run the script to generate the website:
   ```bash
   python3 update_sessions.py
   ```

3. Open `index.html` in your browser to view the website.

## 📁 How It Works

The `update_sessions.py` script:

- **Scans** the `../Sessions/` directory for `.md` files
- **Converts** Markdown content to HTML
- **Generates** a single-page website with:
  - Session list on the homepage
  - Individual session pages accessible via URL fragments
  - Clean navigation between sessions
  - Responsive design for mobile and desktop


## 📝 Adding New Sessions

1. Create a new `.md` file in the `../Sessions/` directory
2. Use the following format:
   ```markdown
   # Session Title
   
   - **Topic**: Your Topic Name
   - **Date**: YYYY-MM-DD
   
   ## Content
   Your session content here...
   ```
3. Run `python3 update_sessions.py` to regenerate the website

## 🔧 Troubleshooting

**Q: "ModuleNotFoundError: No module named 'markdown'"**
A: Install the markdown package using the installation command above.

**Q: Website doesn't update after adding a session**
A: Make sure to run `python3 update_sessions.py` after adding new `.md` files.

**Q: Session links not working**
A: Ensure your `.md` files are in the `../Sessions/` directory and not named `template.md`.

## 📱 Live Website

The generated `index.html` file contains everything needed to run the website. Simply open it in any modern web browser or serve it from a web server.

---

*Built with ❤️ for the distributed systems community* 