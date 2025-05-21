def print_vim_cheatsheet():
    sections = {
        "🧠 Basics (Mode Awareness)": [
            "i     – insert before cursor",
            "a     – insert after cursor",
            "Esc   – return to normal mode",
            "v     – visual mode",
            ":     – command mode",
            "u     – undo",
            "Ctrl+r – redo"
        ],
        "💾 File Operations": [
            ":w         – write/save",
            ":q         – quit",
            ":wq        – save and quit",
            ":q!        – force quit without saving",
            ":e file    – open file",
            ":vs file   – vertical split",
            ":sp file   – horizontal split",
            "Ctrl+w     – then arrow key to switch splits"
        ],
        "🧭 Movement": [
            "h/l         – left/right",
            "j/k         – down/up",
            "0/^/$       – line start / first non-blank / end",
            "w/W         – next word / WORD",
            "b/B         – back a word",
            "gg/G        – top/bottom of file",
            ":n          – go to line n",
            "%           – jump to matching bracket"
        ],
        "✂️ Editing": [
            "x           – delete character",
            "dd/yy       – delete/yank line",
            "p/P         – paste below/above",
            "cw/cc       – change word/line",
            "r<char>     – replace character"
        ],
        "🧱 Text Objects": [
            "ciw         – change inner word",
            "di\"        – delete inside quotes",
            "da(         – delete around parentheses",
            "vi{         – visually select inside curly braces"
        ],
        "🔍 Search and Replace": [
            "/text       – search forward",
            "?text       – search backward",
            "n/N         – next/previous match",
            ":%s/old/new/g    – replace all",
            ":%s/old/new/gc   – replace with confirm"
        ],
        "🧰 Macros and Registers": [
            "qa      – start recording macro to register a",
            "q       – stop recording",
            "@a      – play macro a",
            "@@      – repeat last macro"
        ],
        "➕ Increment / ➖ Decrement Numbers": [
            "Ctrl+a  – increment number under cursor",
            "Ctrl+x  – decrement number under cursor",
            "5Ctrl+a – increment by 5",
            "3Ctrl+x – decrement by 3",
            "Works on decimal, hex (0x), and octal (0) numbers"
        ],
        "🔧 Useful": [
            ".           – repeat last change",
            ":set number – show line numbers",
            ":set relativenumber – show relative numbers",
            ":noh        – clear search highlight",
            "Ctrl+o / Ctrl+i – jump back/forward in jumplist"
        ]
    }

    print("\n📜 Vim Cheatsheet:\n" + "="*80)
    for section, items in sections.items():
        print(f"\n{section}\n" + "-"*len(section))
        for line in items:
            print(f"  {line}")
    print("\n" + "="*80)

if __name__ == "__main__":
    print_vim_cheatsheet()
