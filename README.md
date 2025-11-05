# 4x6 Printer MCP Server

A powerful MCP (Model Context Protocol) server that enables Claude Desktop to print documents directly to your local Windows printer with intelligent formatting support for both standard documents and 4x6 index cards.

## ✨ Features

- **Professional Document Printing**: Full Markdown support with proper typography
- **4x6 Index Card Support**: Intelligent auto-scaling algorithm that fits content perfectly
- **Multiple Printers**: Supports any Windows printer with automatic detection
- **Silent Operation**: Background printing without user interaction
- **Robust Error Handling**: Multiple fallback methods and detailed error reporting
- **Debug Mode**: Comprehensive troubleshooting capabilities

## 🖨️ Printing Capabilities

### Standard Printing (Letter/A4/Legal)
- Professional document layout with 0.75" margins
- Normal font sizes (10-18pt range)
- Full Markdown formatting support
- No auto-scaling - preserves intended formatting

### 4x6 Index Card Printing ⭐
- **Smart Orientation**: 6" wide × 4" tall (landscape)
- **Optimized Margins**: 0.1" for maximum content space
- **Intelligent Auto-Scaling**: Recursive algorithm that adjusts font size (6pt-12pt) and spacing
- **Page Limiting**: Automatically fits content on ≤2 pages
- **Readability Priority**: Never goes below 6pt font size

## 📋 Requirements

### System Requirements
- **Windows 10/11** (with PowerShell)
- **Python 3.8+** with asyncio support
- **A configured printer** (inkjet, laser, or thermal)

### Python Dependencies
```bash
pip install -r requirements.txt
```

Required packages:
- `mistune>=3.0.0` - Markdown to HTML conversion
- `reportlab>=4.0.0` - PDF generation with professional typography
- `PyPDF2>=3.0.0` - PDF page counting for 4x6 verification

### Included Components
- **PDFtoPrinter.exe** (12.5MB) - Reliable Windows printing utility
- **MCP Protocol Support** - Claude Desktop integration

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ljbred08/4x6-printer-mcp.git
   cd 4x6-printer-mcp
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify setup**:
   ```bash
   # Check that PDFtoPrinter.exe exists
   dir PDFtoPrinter.exe

   # Test server startup
   python server.py --help
   ```

## 🎯 Usage with Claude Desktop

### MCP Server Installation

Add this to your Claude Desktop configuration:

```json
{
  "mcpServers": {
    "4x6-printer": {
      "command": "python",
      "args": ["C:\\path\\to\\4x6-printer-mcp\\server.py"],
      "env": {
        "MCP_DEBUG": "false"
      }
    }
  }
}
```

### Available Tools

#### 1. `print_file` - Print Documents

**Basic Document Printing**:
```
print_file(
  content: "# My Document\n\nThis is **important** text with a list:\n- Item 1\n- Item 2",
  filename: "My Document"
)
```

**4x6 Index Card Printing**:
```
print_file(
  content: "# Chocolate Chip Cookies\n\n## Ingredients:\n- 2 cups flour\n- 1 cup butter\n- 1 tsp vanilla\n\n## Instructions:\n1. Mix dry ingredients\n2. Cream butter and sugar\n3. Bake at 350°F for 12 minutes",
  filename: "Recipe Card",
  format4x6: true,
  printer_name: "My Printer"
)
```

**Full Parameters**:
- `content` (string, **required**) - Content to print (supports Markdown)
- `filename` (string, optional) - Document filename
- `format4x6` (boolean, default: false) - Enable 4x6 index card mode
- `printer_name` (string, optional) - Specific printer (uses default if not specified)
- `paper_size` (string: "letter"|"a4"|"legal"|"4x6") - Paper size
- `orientation` (string: "portrait"|"landscape") - Page orientation
- `debug` (boolean, default: false) - Enable debug output

#### 2. `list_printers` - Show Available Printers

```
list_printers()
```

Returns a formatted list of all available printers with status information.

#### 3. `test_print` - Print Test Page

**Standard Test Page**:
```
test_print()
```

**4x6 Test Page**:
```
test_print(format4x6: true, printer_name: "My Printer")
```

## 📝 Markdown Support

### Supported Formatting
- **Headers**: `# H1`, `## H2`, `### H3`
- **Emphasis**: `**bold**`, `*italic*`
- **Lists**: `- unordered`, `1. ordered`
- **Text**: Regular paragraphs and line breaks

### Example Content
```markdown
# Recipe: Chocolate Chip Cookies

## Ingredients
- 2 cups all-purpose flour
- 1 cup butter, softened
- 3/4 cup granulated sugar
- 1 tsp vanilla extract

## Instructions
1. **Preheat** oven to 375°F (190°C)
2. *Mix* dry ingredients in a bowl
3. Cream butter and sugar until fluffy
4. Combine all ingredients
5. Bake for 12-15 minutes

Enjoy your homemade cookies!
```

## 🔧 Configuration

### Environment Variables
- `MCP_DEBUG` - Set to "true", "1", or "yes" for debug output

### Printer Setup
1. **Install your printer** normally in Windows
2. **Configure paper sizes** in printer properties
3. **Test with `list_printers()`** to verify detection
4. **Use exact printer names** from the list output

### 4x6 Printer Configuration
For 4x6 index card printing:
1. **Load 4x6 paper/stock** in your printer
2. **Set paper size** to 4x6 in printer preferences
3. **Test with `test_print(format4x6:true)`** before printing important documents

## 🐛 Troubleshooting

### Enable Debug Mode
```python
print_file(
  content: "Test content",
  debug: true
)
```

### Common Issues

**"Printer not found"**:
- Run `list_printers()` to see available printers
- Use exact printer name from the output
- Ensure printer is powered on and connected

**"4x6 content doesn't fit"**:
- The auto-scaling will automatically adjust font size
- If content is too long, consider splitting into multiple cards
- Minimum font size is 6pt for readability

**"PDFtoPrinter error"**:
- Ensure PDFtoPrinter.exe is in the project directory
- Check printer has paper and is online
- Try printing a test page from Windows first

### Error Messages
- **"ReportLab is required"** - Install with `pip install reportlab`
- **"PyPDF2 is required"** - Install with `pip install PyPDF2`
- **"Mistune is required"** - Install with `pip install mistune`

## 🧪 Testing

The repository includes comprehensive test scripts:

```bash
# Test basic functionality
python test_simplified.py

# Test 4x6 auto-scaling
python test_verification.py

# Test with actual printer
python test_real_pdftoprinter.py
```

## 📊 How 4x6 Auto-Scaling Works

The intelligent auto-scaling algorithm:

1. **Content Analysis** - Estimates required space based on content length
2. **Initial Sizing** - Starts with optimal font size (12pt) and spacing
3. **PDF Creation** - Creates actual PDF with current settings
4. **Page Verification** - Counts actual pages using PyPDF2
5. **Recursive Adjustment** - Reduces font size first, then spacing
6. **Success** - When content fits on ≤2 pages with ≥6pt font

### Scaling Priority
1. **Font Size**: 12pt → 6pt (0.5pt increments)
2. **Line Spacing**: 0.85 → 0.6 (0.1 increments)
3. **Failed State**: Content too long even at minimums

## 📄 File Structure

```
4x6-printer-mcp/
├── server.py              # Main MCP server (50KB)
├── PDFtoPrinter.exe       # Windows printing utility (12.5MB)
├── requirements.txt       # Python dependencies
├── README.md             # This documentation
└── test_*.py             # Test and validation scripts
```

## 🔒 Security & Privacy

- **Local Processing** - All PDF generation happens locally
- **No Cloud Services** - Documents never leave your computer
- **Temp File Cleanup** - Automatic cleanup of temporary files
- **Printer Access** - Only accesses printers you specify

## 📈 Performance

- **PDF Generation**: <1 second for typical documents
- **4x6 Verification**: 2-3 iterations maximum
- **Printing**: Sub-second for most printers
- **Memory Usage**: Minimal (no large image processing)

## 🙏 Attribution

This project stands on the shoulders of an amazing utility that made reliable Windows printing possible:

### PDFtoPrinter.exe
**Author:** [emendelson](https://github.com/emendelson)
**Repository:** https://github.com/emendelson/pdftoprinter
**License:** AutoIt project for Windows PDF printing
**Installable via:** `winget install pdftoprinter`

> **This utility saved this project!** 🎯
> After struggling with complex PyMuPDF implementations and unreliable shell commands, PDFtoPrinter.exe provided the simple, robust Windows printing integration that actually works.
>
> Without emendelson's work, this MCP server would not exist in its current form. Thank you for creating such a reliable tool!

PDFtoPrinter.exe is an AutoIt-based command-line utility that provides direct PDF printing capabilities to Windows printers. It handles the complex Windows printing API interactions that would otherwise require extensive development effort.

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📜 License

MIT License - see LICENSE file for details

## 🆘 Support

If you encounter issues:

1. **Enable debug mode** and check the output
2. **Verify printer setup** with Windows test prints
3. **Check dependencies** are properly installed
4. **Run test scripts** to isolate the issue

---

**Perfect for printing**: Recipe cards, flash cards, instructions, labels, notes, and any content that needs to fit on compact 4x6 index cards! 🃏