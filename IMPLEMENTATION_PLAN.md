# Python MCP Printer Server Implementation Plan

## Project Overview
Build a simple, reliable Python MCP server for Windows printing with proper Markdown formatting and 4x6 index card support.

## Core Requirements (Based on Previous Attempts)

### 1. MCP Protocol Compliance
- ✅ Standard stdio MCP server (runnable with npx/pip)
- ✅ JSON communication only (no console.log to stdout)
- ✅ Proper tool schema with input validation
- ✅ Error handling and debugging capabilities

### 2. Windows Printing
- ✅ Windows-compatible printing commands (PowerShell/CMD)
- ✅ Multiple fallback methods for reliability
- ✅ Support for various file types (.txt, .pdf, .docx)
- ✅ Printer detection and listing

### 3. Markdown Formatting (Critical)
- ✅ **PROPER formatted printing** (not plain text)
- ✅ Headers with different font sizes
- ✅ Bold and italic text styling
- ✅ Lists and other Markdown elements
- ✅ Professional document output

### 4. 4x6 Index Card Support
- ✅ Optional 4x6 printing mode
- ✅ Optimized layout for index cards
- ✅ Smaller fonts and tighter spacing
- ✅ Easy toggle between standard and 4x6

## Technical Implementation Strategy

### Language Choice: Python
**Why Python over Node.js:**
- Better Windows printing integration
- Simpler subprocess handling
- More reliable text processing
- Built-in libraries for common tasks
- Easier debugging and testing

### Core Libraries
```python
# MCP Protocol
mcp (or direct stdio handling)

# Markdown Processing
markdown  # Convert Markdown to HTML

# PDF Generation
reportlab  # Professional PDF generation
# OR
weasyprint  # HTML to PDF with CSS support

# Windows Integration
subprocess  # PowerShell/CMD execution
pathlib     # File path handling
tempfile    # Temporary file management
```

## Architecture

### 1. MCP Server Structure
```python
class PrinterMCPServer:
    def __init__(self):
        self.transport = StdioServerTransport()
        self.server = Server(...)

    async def handle_list_tools(self):
        # Return available tools

    async def handle_call_tool(self, name, arguments):
        # Route to appropriate handler
```

### 2. Tool Definitions
```python
TOOLS = [
    {
        "name": "print_file",
        "description": "Print content with proper formatting",
        "input_schema": {
            "type": "object",
            "properties": {
                "content": {"type": "string"},
                "filename": {"type": "string"},
                "format4x6": {"type": "boolean", "default": False},
                "debug": {"type": "boolean", "default": False}
            },
            "required": ["content"]
        }
    },
    {
        "name": "list_printers",
        "description": "List available printers",
        "input_schema": {"type": "object", "properties": {}}
    }
]
```

### 3. Printing Pipeline
```
Input Content → File Type Detection → Processing → Temporary File → Windows Print → Cleanup
```

## Detailed Implementation Plan

### Phase 1: Basic MCP Server (Foundation)
1. **MCP Server Setup**
   - Basic stdio server structure
   - Tool registration and handling
   - JSON communication protocol
   - Error handling framework

2. **Basic Tools**
   - `print_file` with simple text printing
   - `list_printers` with PowerShell detection
   - Basic file I/O and cleanup

### Phase 2: Windows Printing Integration
1. **Printer Detection**
   ```python
   async def list_printers():
       # PowerShell: Get-Printer | Select-Object Name
       # Fallback: WMI queries
       # Return formatted list
   ```

2. **File Printing Methods**
   ```python
   async def print_file(content, filename, format4x6=False, debug=False):
       # Method 1: Windows Print verb
       # Method 2: Notepad for text files
       # Method 3: PowerShell Out-Printer
       # Method 4: Direct print command
   ```

### Phase 3: Markdown Formatting (Critical)
1. **Markdown Processing**
   ```python
   import markdown

   def process_markdown(content):
       # Convert to HTML
       # Apply formatting rules
       # Handle headers, bold, italic, lists
   ```

2. **PDF Generation**
   ```python
   from reportlab.pdfgen import canvas
   from reportlab.lib.pagesizes import letter, portrait

   def create_formatted_pdf(content, filename, format4x6=False):
       # Create PDF with proper formatting
       # Headers: 18pt, 16pt, 14pt
       # Body: 12pt (standard), 10pt (4x6)
       # Bold/italic styling
       # Page size: letter (standard), 4x6in (index card)
   ```

### Phase 4: 4x6 Index Card Support
1. **Index Card Layout**
   ```python
   def create_4x6_pdf(content):
       # Page size: 4" x 6" (288 x 432 points)
       # Margins: 0.25" all around
       # Font sizes: H1=14pt, H2=12pt, H3=11pt, Body=10pt
       # Tight line spacing and layout
   ```

2. **Content Optimization**
   - Auto-font sizing for long content
   - Smart text wrapping
   - Multi-card overflow handling

## Key Implementation Decisions

### 1. PDF vs HTML vs RTF
**Primary: PDF Generation with ReportLab**
- ✅ Reliable formatting control
- ✅ Cross-platform compatibility
- ✅ Professional output
- ✅ No browser dependencies

**Fallback: RTF for simplicity**
- ✅ Windows native support
- ✅ Basic formatting
- ✅ Smaller dependencies

### 2. Printing Methods (Priority Order)
1. **Shell Execute with Print Dialog** (most reliable)
   ```python
   subprocess.run(['powershell', '-Command',
       f'Invoke-Item "{pdf_file}"; sleep 2; '
       f'Add-Type -AssemblyName System.Windows.Forms; '
       f'[System.Windows.Forms.SendKeys]::SendWait("^p"); '
       f'sleep 1; [System.Windows.Forms.SendKeys]::SendWait("{ENTER}")'])
   ```

2. **Direct PDF Reader Commands**
   ```python
   # Adobe Reader, Edge, Chrome browser printing
   ```

3. **Windows Print Verb**
   ```python
   subprocess.run(['powershell', '-Command',
       f'Start-Process -FilePath "{file}" -Verb Print'])
   ```

### 3. Error Handling Strategy
- Multiple fallback methods
- Detailed error messages
- Debug mode with verbose logging
- Graceful degradation

## Implementation Decisions (Based on User Requirements)

### 1. Dependencies & PDF Generation
**CHOICE: Full-Featured Package**
- **ReportLab** for professional PDF generation (primary method)
- **markdown** library for Markdown processing
- **RTF generation** as fallback option
- Standard Python libraries for everything else
- Full functionality prioritized over minimal dependencies

### 2. User Experience
**CHOICE: All Features Included**
- Automatic print dialogs (primary workflow)
- Test print feature for setup verification
- Detailed error messages for troubleshooting
- Debug mode for advanced users

### 3. 4x6 Index Card Implementation
**CHOICE: Smart Auto-Scaling**
- Start with reasonable font size (9-11pt for 4x6)
- Auto-shrink if necessary to fit on two pages max
- Portrait orientation (standard index card format)
- 0.25" margins all around

### 4. Distribution Strategy
**CHOICE: Hybrid Approach**
- **Primary**: Clone git repo and run locally
- **Secondary**: PyPI publication ready (`pip install claude-printer-mcp`)
- **setup.py** and **pyproject.toml** for both use cases
- **requirements.txt** for local development

## Testing Strategy

### 1. Unit Tests
- Markdown parsing accuracy
- PDF generation validation
- Windows command execution

### 2. Integration Tests
- End-to-end printing workflow
- Multiple file type support
- 4x6 card formatting

### 3. Manual Tests
- Actual printer output verification
- Different Windows versions
- Various PDF readers

## Success Criteria
1. ✅ MCP server starts and communicates properly
2. ✅ Markdown renders with proper formatting (headers, bold, lists)
3. ✅ Print dialog opens reliably
4. ✅ 4x6 index cards format correctly
5. ✅ Backward compatibility with existing file types
6. ✅ Debug mode provides useful information
7. ✅ Clean error handling and user feedback

## Next Steps
1. **Review this plan** with any corrections or additional requirements
2. **Begin Phase 1**: Basic MCP server setup
3. **Test incrementally** at each phase
4. **Refine based on actual printing results**

---

**Ready for your review and feedback!**