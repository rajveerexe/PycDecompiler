# PYC Decompiler

<div align="center">

![PYC Decompiler Banner](https://raw.githubusercontent.com/rajveerexe/PycDecompiler/refs/heads/main/PycDecompiler.jpg)

### Marshal → PYC Converter & Python Bytecode Decompiler

[![Python](https://img.shields.io/badge/Python-3.6%20→%203.14-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)](LICENSE)
![Visitors](https://api.visitorbadge.io/api/visitors?path=github.com/rajveerexe/PycDecompiler&label=Visitors&countColor=%2300ff99&style=for-the-badge)

*A powerful utility for converting marshal files to PYC and decompiling Python bytecode back to source*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [CLI Mode](#-cli-mode) • [License](#-license)

</div>

---

## 📖 About

**PYC Decompiler** is a comprehensive Python utility designed for bytecode analysis and reverse engineering. It enables you to:

- Convert **marshal-based Python files** into valid `.pyc` bytecode files
- Decompile `.pyc` files back into **readable Python source code**
- Handle **multiple Python versions automatically** (3.6 through 3.14)
- Detect file types automatically and process accordingly

> ⚠️ **Important**: This tool operates strictly at the bytecode/marshal layer and does not crack encryption or bypass licensing mechanisms.

### Use Cases

- 🔍 Reverse engineering (educational purposes)
- 🛡️ Malware analysis and security research
- 📚 Bytecode research and Python internals learning
- 🧪 Code recovery and archival
- 🔧 Python internals debugging

---

## ⭐ Features

- 🧠 **Marshal → PYC Conversion** - Transform marshal files into proper bytecode
- 🧩 **PYC → Source Decompilation** - Recover readable Python source code
- 🔢 **Multi-Version Support** - Compatible with Python 3.6 through 3.14
- 🎯 **Automatic Detection** - Intelligently detects marshal and PYC files
- ⚡ **Fast & Automated** - Streamlined workflow with minimal manual intervention
- 🖥️ **Interactive Menu** - User-friendly interface for easy operation
- 🧪 **CLI Mode** - Command-line interface for scripting and automation
- 🌐 **PyLingual Backend** - Powered by PyLingual decompilation service
- 📦 **Zero External Binaries** - No need for separate decompiler installations

---

## 🔧 How It Works

```
Marshal / PYC File
       ↓
File Type Detection
       ↓
Version Detection
       ↓
Magic Header Injection (if marshal)
       ↓
Upload to PyLingual API
       ↓
Decompilation Process
       ↓
Recovered Python Source
```

**Key Principles:**
- ✅ No VM patching required
- ✅ No opcode tampering
- ✅ Pure bytecode-level logic
- ✅ Cloud-based decompilation engine

---

## 🐍 Supported Python Versions

| Version | Magic Number | Status |
|---------|-------------|--------|
| Python 3.6 | `33 0D 0D 0A` | ✅ Supported |
| Python 3.7 | `42 0D 0D 0A` | ✅ Supported |
| Python 3.8 | `55 0D 0D 0A` | ✅ Supported |
| Python 3.9 | `61 0D 0D 0A` | ✅ Supported |
| Python 3.10 | `6F 0D 0D 0A` | ✅ Supported |
| Python 3.11 | `A7 0D 0D 0A` | ✅ Supported |
| Python 3.12 | `CB 0D 0D 0A` | ✅ Supported |
| Python 3.13 | `F3 0D 0D 0A` | ✅ Supported |
| Python 3.14 | `2B 0E 0D 0A` | ✅ Supported |

---

## 📋 Requirements

- **Python** 3.6 or higher
- **Internet connection** (for PyLingual API access)
- **Dependencies:**
  - `requests` - HTTP library for API communication

### Install Dependencies

```bash
pip install requests
```

---

## 🚀 Installation

### Method 1: Clone from GitHub

```bash
# Clone the repository
git clone https://github.com/rajveerexe/PycDecompiler.git

# Navigate to directory
cd PycDecompiler

# Install dependencies
pip install -r requirements.txt

# Run the decompiler
python PycDecompiler.py
```

### Method 2: Direct Download

```bash
# Download the script
wget https://raw.githubusercontent.com/rajveerexe/PycDecompiler/main/PycDecompiler.py

# Install dependencies
pip install requests

# Run the script
python PycDecompiler.py
```

---

## 💻 Usage

### Interactive Mode

Launch the interactive menu (recommended for beginners):

```bash
python PycDecompiler.py
```

**Interactive Menu:**

```
═══════════════════════════════════════════════════════
    ____        __    _                         __
   / __ \__  __/ /   (_)___  ____ ___  ______ _/ /
  / /_/ / / / / /   / / __ \/ __ `/ / / / __ `/ /
 / ____/ /_/ / /___/ / / / / /_/ / /_/ / /_/ / /
/_/    \__, /_____/_/_/ /_/\__, /\__,_/\__,_/_/
      /____/              /____/
═══════════════════════════════════════════════════════
                    P Y L I N G U A L
═══════════════════════════════════════════════════════

[ 1 ] Convert Marshal to PYC
[ 2 ] Decompile PYC to Python Source
[ 0 ] Exit
```

### Option 1: Convert Marshal to PYC

1. Select option `1` from the menu
2. Enter the path to your marshal file (`.py` file containing marshal data)
3. Select Python version (or use current version)
4. The tool will generate a `.pyc` file

**Example:**

```
[ ? ] Select option: 1
[ ? ] Enter Marshal file path: obfuscated_script.py

Available Python Versions:
[ 1 ] Python 3.6
[ 2 ] Python 3.7
[ 3 ] Python 3.8
[ 4 ] Python 3.9
[ 5 ] Python 3.10
[ 6 ] Python 3.11
[ 7 ] Python 3.12
[ 8 ] Python 3.13
[ 9 ] Python 3.14
[ 0 ] Current Version (3.11)

[ ? ] Select version: 0
[ * ] Converting Marshal to PYC (Python 3.11)...
[ ✓ ] Saved: obfuscated_script.pyc
[ ✓ ] Done!
```

### Option 2: Decompile PYC to Python Source

1. Select option `2` from the menu
2. Enter the path to your `.pyc` file
3. Wait for the decompilation process (uploads to PyLingual API)
4. Decompiled source will be saved as `decoded_[filename].py`

**Example:**

```
[ ? ] Select option: 2
[ ? ] Enter PYC file path: script.pyc

[ * ] Processing: script.pyc
[ ✓ ] File validated
[ ✓ ] Uploaded with identifier: abc123xyz456
[ 1 ] Stage: decompiling | Elapsed: 2.3s
[ 2 ] Stage: decompiling | Elapsed: 3.8s
[ ✓ ] Decompilation complete (Attempts: 2, Time: 3.85s)
[ ✓ ] Decompiled code saved to: ./decoded_script.py
[ ✓ ] Total execution time: 4.12s
[ ✓ ] Done!
```

---

## 🧪 CLI Mode

### Basic PYC Decompilation

```bash
python PycDecompiler.py script.pyc
```

### Marshal File Conversion + Decompilation

The tool automatically detects marshal files and converts them:

```bash
python PycDecompiler.py obfuscated_script.py
```

Output:
```
[ * ] Detected: Marshal file
[ * ] Converting Marshal to PYC (Python 3.11)...
[ ✓ ] Saved: obfuscated_script.pyc

[ * ] Now decompiling PYC...
[ * ] Processing: obfuscated_script.pyc
[ ✓ ] Decompiled code saved to: decoded_obfuscated_script.py
[ ✓ ] Done!
```

### Specify Python Version

```bash
python PycDecompiler.py marshal_file.py 3.10
```

### Batch Processing

```bash
# Process all PYC files in directory
for file in *.pyc; do
    python PycDecompiler.py "$file"
done
```

```bash
# Process all marshal files
for file in obfuscated_*.py; do
    python PycDecompiler.py "$file" 3.11
done
```

---

## 🔍 Technical Details

### Marshal Detection

The tool automatically detects marshal files by:
1. Checking file extension (`.py`)
2. Reading file content and searching for `marshal` keyword
3. If detected, converts to PYC before decompilation

### PYC Magic Numbers

Each Python version has a unique magic number (first 4 bytes of `.pyc` file):

```python
magic_map = {
    "3.6": b"3\r\r\n\x8bq\x98d\x0c\x00\x00\x00\xe3\x00\x00\x00",
    "3.7": b"B\r\r\n\x00\x00\x00\x00\x8bq\x98d\x0c\x00\x00\x00",
    "3.8": b"U\r\r\n\x00\x00\x00\x00\tq\x98d\x0b\x00\x00\x00",
    "3.9": b"a\r\r\n\x00\x00\x00\x00\tq\x98d\x0b\x00\x00\x00",
    "3.10": b"o\r\r\n\x00\x00\x00\x00\tq\x98d\x0b\x00\x00\x00",
    "3.11": b"\xa7\r\r\n\x00\x00\x00\x004\x0eAi\n\x00\x00\x00",
    "3.12": b"\xcb\r\r\n\x00\x00\x00\x00{\x0eAi\n\x00\x00\x00",
    "3.13": b"\xf3\r\r\n\x00\x00\x00\x00\x90\x0eAi\n\x00\x00\x00",
    "3.14": b"+\x0e\r\n\x00\x00\x00\x00\x7f\xf8\xbfj\x0f\x00\x00\x00",
}
```

### Decompilation Process

1. **Upload**: File is uploaded to PyLingual API
2. **Processing**: Backend analyzes bytecode structure
3. **Decompilation**: Bytecode is reverse-engineered to source
4. **Retrieval**: Decompiled code is downloaded and saved

---

## ⚠️ Legal Disclaimer

This project is intended **for educational and research purposes only**.

### Important Guidelines

- ✅ You are responsible for complying with local laws and regulations
- ✅ Only decompile code you own or have explicit permission to analyze
- ✅ Respect intellectual property and licensing agreements
- ❌ Do not use for DRM bypass or license cracking
- ❌ Do not use for commercial piracy or unauthorized distribution
- ❌ Do not violate software licenses or terms of service
- ❌ The author assumes no responsibility for misuse

**Use responsibly and ethically.**

> 🔒 **Note**: This tool does NOT break encryption, bypass obfuscation, or crack protected software. It works only on standard Python bytecode.

---

## 🛠️ Troubleshooting

### Common Issues

#### 1. Unsupported Python Version

```
Error: Invalid Python version: 3.5
```

**Solution**: Use Python 3.6 or higher. Check available versions with:
```bash
python --version
```

#### 2. File Not Found

```
[ ! ] File not found: script.pyc
```

**Solution**: 
- Verify the file path is correct
- Use absolute paths if relative paths fail
- Check file permissions

#### 3. Not a Valid Marshal File

```
[ ! ] Not a valid marshal file
```

**Solution**:
- Ensure the file contains marshal data
- Try opening the file to verify it's a Python marshal file
- Some obfuscated files may not be standard marshal format

#### 4. Decompilation Failed

```
[ ! ] Decompilation Error: Upload failed with status code: 502
```

**Possible Causes:**
- PyLingual API is temporarily down
- Network connectivity issues
- File is corrupted or heavily obfuscated

**Solution**:
- Wait a few minutes and try again
- Check your internet connection
- Verify the `.pyc` file is valid

#### 5. Service Unavailable (502)

```
[ ! ] Decompilation Error: Service temporarily unavailable (502)
```

**Solution**: The PyLingual API is experiencing high traffic. Try again in a few minutes.

#### 6. Decompilation Timeout

```
[ ! ] Decompilation Error: Decompilation timeout exceeded
```

**Solution**: 
- Large or complex files may take longer
- The default timeout is 300 seconds (5 minutes)
- Try again or use a smaller test file

#### 7. Messy or Incomplete Output

**Note**: This is normal for:
- Heavily optimized bytecode
- Obfuscated code
- Code with advanced Python features

The decompiler reconstructs source from bytecode, which may result in:
- Different variable names
- Restructured control flow
- Missing comments and docstrings

---

## 📂 Project Structure

```
PycDecompiler/
├── PycDecompiler.py          # Main decompiler script
├── README.md               # This file
├── LICENSE                 # MIT License
└── examples/               # Sample files (optional)
    ├── sample_marshal.py
    └── sample_script.pyc
```

---

## 🔧 Advanced Usage

### Error Handling

The tool includes comprehensive error handling:

```python
try:
    decompile_pyc("script.pyc")
except FileNotFoundError:
    print("File not found")
except FileNotPyc:
    print("Not a valid PYC file")
except DecompilationError:
    print("Decompilation failed")
```

### Custom Integration

You can integrate the decompiler into your own scripts:

```python
from PYC_Decoder import decompile_pyc, marshal_to_pyc

# Convert marshal to PYC
pyc_file = marshal_to_pyc("obfuscated.py", "3.11")

# Decompile PYC
if pyc_file:
    decompile_pyc(pyc_file)
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Reporting Issues

1. Check existing issues first
2. Provide detailed information:
   - Python version
   - Operating system
   - Error messages
   - Sample files (if possible)

### Pull Requests

1. Fork the repository
2. Create a feature branch:
   ```bash
   git checkout -b feature/improvement
   ```
3. Make your changes
4. Test thoroughly
5. Commit with clear messages:
   ```bash
   git commit -am 'Add new feature: XYZ'
   ```
6. Push to your fork:
   ```bash
   git push origin feature/improvement
   ```
7. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide
- Add docstrings to functions
- Include error handling
- Test with multiple Python versions
- Update documentation

---

## 📊 API Information

This tool uses the **PyLingual** decompilation service:

- **Website**: https://pylingual.io
- **API Endpoint**: https://api.pylingual.io
- **Features**:
  - Cloud-based decompilation
  - Multi-version support
  - High accuracy rate
  - No local dependencies

**Note**: PyLingual is a third-party service. Availability and performance depend on their infrastructure.

---

## 🗺️ Roadmap

Future improvements:

- [ ] Online decompilation mode
- [ ] GUI interface
- [ ] Batch processing with progress bars
- [ ] Support for more obfuscation techniques
- [ ] Web interface version
- [ ] Plugin system for custom decompilers

---

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2026 Souk

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

**Summary:**
- ✅ Free to use for any purpose
- ✅ Free to modify and distribute
- ✅ No warranty provided
- ✅ Attribution appreciated

---

## 🙏 Credits & Acknowledgments

### Special Thanks

- **PyLingual** ([pylingual.io](https://pylingual.io)) - Decompilation backend service
- **Python Software Foundation** - For the amazing Python language
- **Reverse Engineering Community** - For bytecode research and tools

### Inspiration

This project was inspired by:
- `uncompyle6` - Python bytecode decompiler
- `decompyle3` - Python 3 decompiler
- Various bytecode analysis tools

### Developer

- **GitHub**: [@rajveerexe](https://github.com/rajveerexe)
- **Telegram**: [@SoukPy](https://t.me/SoukPy)

---

## 📞 Support & Contact

### Get Help

- 🐛 **Report bugs**: [GitHub Issues](https://github.com/rajveerexe/PycDecompiler/issues)
- 💬 **Ask questions**: [GitHub Discussions](https://github.com/rajveerexe/PycDecompiler/discussions)
- 📧 **Contact developer**: Open an issue or reach out via Telegram

### Community

Join the discussion and stay updated:
- Star ⭐ this repository
- Watch 👀 for updates
- Fork 🍴 to contribute

---

## 📈 Statistics

![GitHub Stars](https://img.shields.io/github/stars/rajveerexe/PycDecompiler?style=social)
![GitHub Forks](https://img.shields.io/github/forks/rajveerexe/PycDecompiler?style=social)
![GitHub Issues](https://img.shields.io/github/issues/rajveerexe/PycDecompiler)
![GitHub Pull Requests](https://img.shields.io/github/issues-pr/rajveerexe/PycDecompiler)

---

## ⚡ Quick Reference

### Commands Cheat Sheet

```bash
# Interactive mode
python PycDecompiler.py

# Decompile PYC file
python PycDecompiler.py script.pyc

# Convert + decompile marshal file
python PycDecompiler.py obfuscated.py

# Specify Python version
python PycDecompiler.py file.py 3.11

# Batch process
for f in *.pyc; do python PycDecompiler.py "$f"; done
```

### Supported Extensions

- `.pyc` - Python bytecode files (direct decompilation)
- `.py` - Python source files (marshal detection & conversion)

### Output Files

- `decoded_[filename].py` - Decompiled source code
- `[filename].pyc` - Converted PYC file (from marshal)

---

<div align="center">

### 🌟 If you find this tool useful, please star the repository!

---

**Learn Bytecode • Respect Licenses • Open Source Always**

---

Made with ❤️ by **Souk**

**PycDecompiler** | 2026

---

[⬆ Back to Top](#pyc-decompiler)

</div>
