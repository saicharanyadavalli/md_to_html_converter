import requests
import markdown
import os

def convtoraw(url):
    if 'github.com' in url and '/blob/' in url:
        url = url.replace('github.com', 'raw.githubusercontent.com').replace('/blob', '')
    return url

def web(url):
    url = convtoraw(url)
    res = requests.get(url)
    if res.status_code == 200:
        return res.text
    raise Exception("Invalid URL")

def file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def savehtml(data, out):
    html = markdown.markdown(data)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)

def main():
    print("Choose an option:")
    print("1. Convert Markdown from a URL")
    print("2. Convert Markdown from a local file")
    opt = input("Enter 1 or 2: ").strip()

    if opt == '1':
        link = input("Enter the Markdown file URL : ")
        txt = web(link)
    elif opt == '2':
        path = input('Enter the local .md file path (remove the " at start and end): ')
        txt = file(path)
    else:
        print("Invalid option.")
        return

    while True:
        out = input("Enter output HTML file name with .html tag (eg: output.html): ")
        if os.path.exists(out):
            print(f"File '{out}' already exists. Please choose a different name.")
        else:
            break

    savehtml(txt, out)
    print("HTML file saved as:", out)

if __name__ == "__main__":
    main()
