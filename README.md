# 🛠️ Markdown to HTML Converter (Command Line Tool)

## 📄 Description

This command-line Python tool converts `.md` (Markdown) files into `.html` (HTML) format. It supports both:

- Markdown files from a **local directory**
- Markdown files hosted on **GitHub** or any valid **raw URL**

It also smartly detects and converts GitHub file links into raw file URLs automatically, so users don't need to manually extract raw links.

---

## 🚀 Features

- Supports both **online** (URL-based) and **offline** (local) `.md` files.the online urls can be directly the link of the README file no need the raw link the code will directly convert it to the raw link.
- Converts all standard Markdown syntax to HTML
- Automatically detects and processes GitHub URLs
- Saves clean and valid `.html` output ready to open in any browser

---

## 📦 Requirements

Install the required libraries with:

```bash
pip install markdown requests
```
## 🧠 Approach

The tool is designed with simplicity and flexibility in mind. Here's how it works internally:

### 🔹 User Prompt for Mode
The user is asked to choose between:
- **URL-based conversion**
- **Local file conversion**

### 🔹 Input Handling
- If the user enters a GitHub file link  
  *(e.g., `https://github.com/user/repo/blob/main/file.md`)*,  
  the tool automatically converts it to a raw file link  
  *(e.g., `https://raw.githubusercontent.com/user/repo/main/file.md`)*
  
- If the user selects local file mode, the tool reads the file directly from the local system

### 🔹 Markdown to HTML Conversion
The tool uses the `markdown` library to convert the fetched or read `.md` content into valid HTML

### 🔹 Saving the Output
The resulting HTML is saved to a user-specified filename (like `output.html`)
