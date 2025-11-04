#!/usr/bin/env python3
"""
Claude Printer MCP Server - Simplified Version
Uses PDFtoPrinter.exe for reliable Windows printing.
"""

import asyncio
import json
import sys
import subprocess
import tempfile
import os
import traceback
import re
from pathlib import Path
from typing import Dict, Any, Optional

# ReportLab for PDF generation
try:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
    from reportlab.lib.units import inch
    from reportlab.lib.colors import black
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False

# Markdown processing
try:
    import markdown
    from markdown.extensions import tables, fenced_code, nl2br
    MARKDOWN_AVAILABLE = True
except ImportError:
    MARKDOWN_AVAILABLE = False

class PrinterMCPServer:
    """Simplified MCP Server for Windows printing using PDFtoPrinter."""

    def __init__(self):
        self.name = "claude-printer-mcp"
        self.version = "2.0.0"  # Simplified version
        self.temp_files = []  # Track temporary files for cleanup
        self.pdf_printer_path = self._get_pdf_printer_path()

    def _get_pdf_printer_path(self) -> str:
        """Get the path to PDFtoPrinter.exe."""
        # Check if PDFtoPrinter.exe is in the current directory
        current_dir = Path(__file__).parent
        pdf_printer = current_dir / "PDFtoPrinter.exe"

        if pdf_printer.exists():
            return str(pdf_printer)
        else:
            raise FileNotFoundError("PDFtoPrinter.exe not found in the current directory")

    async def run(self):
        """Main server loop handling stdio communication."""
        debug = os.environ.get('MCP_DEBUG', '').lower() in ['true', '1', 'yes']

        if debug:
            print("Starting Simplified Printer MCP Server v2.0...", file=sys.stderr)

        try:
            while True:
                line = sys.stdin.readline()
                if not line:
                    break

                try:
                    message = json.loads(line.strip())
                    await self.handle_message(message, debug)
                except json.JSONDecodeError as e:
                    error_response = {
                        "jsonrpc": "2.0",
                        "id": None,
                        "error": {
                            "code": -32700,
                            "message": "Parse error",
                            "data": str(e)
                        }
                    }
                    print(json.dumps(error_response))
                    sys.stdout.flush()

        except KeyboardInterrupt:
            if debug:
                print("Server shutting down...", file=sys.stderr)
        finally:
            self.cleanup_temp_files()

    async def handle_message(self, message: Dict[str, Any], debug: bool = False):
        """Handle incoming JSON-RPC messages."""
        method = message.get("method")
        msg_id = message.get("id")

        if debug:
            print(f"Received message: {method}", file=sys.stderr)

        if method == "initialize":
            response = await self.handle_initialize(message.get("params", {}))
        elif method == "tools/list":
            response = await self.handle_list_tools()
        elif method == "tools/call":
            response = await self.handle_call_tool(message.get("params", {}))
        else:
            response = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {method}"
                }
            }

        if msg_id is not None:
            response["id"] = msg_id

        print(json.dumps(response))
        sys.stdout.flush()

    async def handle_initialize(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Handle MCP initialization."""
        return {
            "jsonrpc": "2.0",
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {}
                },
                "serverInfo": {
                    "name": self.name,
                    "version": self.version
                }
            }
        }

    async def handle_list_tools(self) -> Dict[str, Any]:
        """List available tools."""
        return {
            "jsonrpc": "2.0",
            "result": {
                "tools": [
                    {
                        "name": "print_file",
                        "description": "Print content with proper formatting using PDFtoPrinter",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "content": {
                                    "type": "string",
                                    "description": "Content to print (supports Markdown formatting)"
                                },
                                "filename": {
                                    "type": "string",
                                    "description": "Optional filename for the document"
                                },
                                "format4x6": {
                                    "type": "boolean",
                                    "description": "Format for 4x6 index card printing (sets custom paper size)",
                                    "default": False
                                },
                                "printer_name": {
                                    "type": "string",
                                    "description": "Specific printer to use (uses default if not specified)"
                                },
                                "paper_size": {
                                    "type": "string",
                                    "enum": ["letter", "a4", "legal", "4x6"],
                                    "description": "Paper size to use (letter, a4, legal, or 4x6)"
                                },
                                "orientation": {
                                    "type": "string",
                                    "enum": ["portrait", "landscape"],
                                    "description": "Page orientation (portrait or landscape)"
                                },
                                "debug": {
                                    "type": "boolean",
                                    "description": "Enable debug mode for troubleshooting",
                                    "default": False
                                }
                            },
                            "required": ["content"]
                        }
                    },
                    {
                        "name": "list_printers",
                        "description": "List available printers on this system",
                        "inputSchema": {
                            "type": "object",
                            "properties": {}
                        }
                    },
                    {
                        "name": "test_print",
                        "description": "Print a test page to verify printer setup",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "format4x6": {
                                    "type": "boolean",
                                    "description": "Format test page for 4x6 index card",
                                    "default": False
                                },
                                "printer_name": {
                                    "type": "string",
                                    "description": "Specific printer to use for test (uses default if not specified)"
                                }
                            }
                        }
                    }
                ]
            }
        }

    async def handle_call_tool(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Handle tool calls."""
        tool_name = params.get("name")
        arguments = params.get("arguments", {})

        try:
            if tool_name == "print_file":
                result = await self.print_file(**arguments)
            elif tool_name == "list_printers":
                result = await self.list_printers(**arguments)
            elif tool_name == "test_print":
                result = await self.test_print(**arguments)
            else:
                raise ValueError(f"Unknown tool: {tool_name}")

            return {
                "jsonrpc": "2.0",
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": result
                        }
                    ]
                }
            }

        except Exception as e:
            error_msg = f"Error in {tool_name}: {str(e)}\n{traceback.format_exc()}"
            return {
                "jsonrpc": "2.0",
                "error": {
                    "code": -1,
                    "message": error_msg
                }
            }

    async def print_file(self, content: str, filename: Optional[str] = None,
                        format4x6: bool = False, printer_name: Optional[str] = None,
                        paper_size: Optional[str] = None, orientation: Optional[str] = None,
                        debug: bool = False) -> str:
        """Print content using PDFtoPrinter."""
        if debug:
            print(f"print_file called with PDFtoPrinter: format4x6={format4x6}, printer={printer_name}", file=sys.stderr)

        # Check dependencies
        if not REPORTLAB_AVAILABLE:
            return "Error: ReportLab is required for PDF generation. Install with: pip install reportlab"

        try:
            # Create formatted PDF
            pdf_file = self.create_formatted_pdf(content, filename, format4x6, debug)
            if not pdf_file:
                return "Error: Failed to create PDF file"

            # Print using PDFtoPrinter
            result = await self.print_with_pdftoprinter(pdf_file, printer_name, debug)

            return result

        except Exception as e:
            # Return the full error with traceback for debugging
            error_msg = f"Error creating or printing PDF: {str(e)}"
            if debug:
                error_msg += f"\n{traceback.format_exc()}"
            return error_msg

    async def print_with_pdftoprinter(self, pdf_file: str, printer_name: Optional[str] = None, debug: bool = False) -> str:
        """Print PDF using PDFtoPrinter.exe."""
        try:
            if debug:
                print(f"Using PDFtoPrinter: {self.pdf_printer_path}", file=sys.stderr)

            # Build command with silent mode for automated printing
            if printer_name:
                cmd = [self.pdf_printer_path, "/s", pdf_file, printer_name]
                printer_display = printer_name
            else:
                cmd = [self.pdf_printer_path, "/s", pdf_file]
                printer_display = "default printer"

            if debug:
                print(f"Command: {' '.join(cmd)}", file=sys.stderr)

            # Execute PDFtoPrinter
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60,
                cwd=Path(__file__).parent
            )

            if debug:
                print(f"PDFtoPrinter return code: {result.returncode}", file=sys.stderr)
                if result.stdout:
                    print(f"PDFtoPrinter stdout: {result.stdout}", file=sys.stderr)
                if result.stderr:
                    print(f"PDFtoPrinter stderr: {result.stderr}", file=sys.stderr)

            if result.returncode == 0:
                return f"Successfully printed '{os.path.basename(pdf_file)}' on {printer_display}"
            else:
                return f"PDFtoPrinter error (code {result.returncode}): {result.stderr or 'Unknown error'}"

        except subprocess.TimeoutExpired:
            return "PDFtoPrinter timed out (60 seconds)"
        except Exception as e:
            return f"Error running PDFtoPrinter: {str(e)}"

    def create_formatted_pdf(self, content: str, filename: Optional[str] = None,
                            format4x6: bool = False, debug: bool = False) -> Optional[str]:
        """Create a formatted PDF from content."""
        if not REPORTLAB_AVAILABLE:
            return None

        try:
            # Create temporary PDF file
            temp_file = tempfile.NamedTemporaryFile(mode='wb', suffix='.pdf', delete=False)
            temp_file_path = temp_file.name
            temp_file.close()

            # Verify the file was created and is writable
            if not os.path.exists(temp_file_path):
                raise RuntimeError(f"Failed to create temporary file: {temp_file_path}")

            self.temp_files.append(temp_file_path)

            # Set up page size
            if format4x6:
                # 4x6 index cards are typically used in landscape orientation
                # So we make it 6" wide x 4" tall for proper use
                page_size = (6 * inch, 4 * inch)  # 6x4 inches (landscape 4x6)
                margin = 0.25 * inch
            else:
                page_size = letter
                margin = 0.75 * inch

            # Create PDF document
            doc = SimpleDocTemplate(
                temp_file_path,
                pagesize=page_size,
                leftMargin=margin,
                rightMargin=margin,
                topMargin=margin,
                bottomMargin=margin
            )

            # Get styles
            styles = getSampleStyleSheet()

            if format4x6:
                # 4x6 optimized font sizes
                title_style = ParagraphStyle(
                    'CustomTitle4x6',
                    parent=styles['Heading1'],
                    fontSize=14,
                    spaceAfter=12,
                    alignment=1  # Center
                )

                heading1_style = ParagraphStyle(
                    'CustomH1_4x6',
                    parent=styles['Heading1'],
                    fontSize=14,
                    spaceAfter=12,
                    spaceBefore=15
                )

                heading2_style = ParagraphStyle(
                    'CustomH2_4x6',
                    parent=styles['Heading2'],
                    fontSize=12,
                    spaceAfter=10,
                    spaceBefore=12
                )

                heading3_style = ParagraphStyle(
                    'CustomH3_4x6',
                    parent=styles['Heading3'],
                    fontSize=11,
                    spaceAfter=8,
                    spaceBefore=10
                )

                body_style = ParagraphStyle(
                    'CustomBody_4x6',
                    parent=styles['Normal'],
                    fontSize=10,
                    spaceAfter=6,
                    leading=12
                )
            else:
                # Standard document font sizes
                title_style = ParagraphStyle(
                    'CustomTitle',
                    parent=styles['Heading1'],
                    fontSize=18,
                    spaceAfter=20,
                    alignment=1  # Center
                )

                heading1_style = ParagraphStyle(
                    'CustomH1',
                    parent=styles['Heading1'],
                    fontSize=16,
                    spaceAfter=16,
                    spaceBefore=20
                )

                heading2_style = ParagraphStyle(
                    'CustomH2',
                    parent=styles['Heading2'],
                    fontSize=14,
                    spaceAfter=12,
                    spaceBefore=16
                )

                heading3_style = ParagraphStyle(
                    'CustomH3',
                    parent=styles['Heading3'],
                    fontSize=12,
                    spaceAfter=10,
                    spaceBefore=12
                )

                body_style = ParagraphStyle(
                    'CustomBody',
                    parent=styles['Normal'],
                    fontSize=12,
                    spaceAfter=8,
                    leading=14
                )

            # Build content
            story = []

            # Add title if filename provided
            if filename:
                story.append(Paragraph(filename, title_style))
                story.append(Spacer(1, 20 if not format4x6 else 15))

            # Process content
            if MARKDOWN_AVAILABLE:
                # Use markdown library for processing with enhanced list support
                md = markdown.Markdown(
                    extensions=['tables', 'fenced_code', 'nl2br', 'toc'],
                    output_format='html'
                )
                html_content = md.convert(content)

                # Convert HTML to paragraphs with enhanced list processing
                paragraphs = self._html_to_paragraphs(html_content, body_style, heading1_style, heading2_style, heading3_style)

                # For 4x6 cards, try to keep content together
                if format4x6 and len(paragraphs) <= 8:
                    story.append(KeepTogether(paragraphs))
                else:
                    story.extend(paragraphs)
            else:
                # Fallback: Enhanced markdown processing with list support
                lines = content.split('\n')
                in_list = False
                list_counter = 0
                ordered_list = False

                for line in lines:
                    original_line = line
                    line = line.strip()

                    if not line:
                        if not in_list:
                            story.append(Spacer(1, 6))
                        continue

                    # Check for ordered lists (1. 2. 3. etc.)
                    ordered_match = re.match(r'^(\d+)\.\s+(.*)', line)
                    if ordered_match:
                        if not in_list:
                            in_list = True
                            ordered_list = True
                            list_counter = int(ordered_match.group(1))
                        elif not ordered_list:
                            # Starting new ordered list
                            ordered_list = True
                            list_counter = int(ordered_match.group(1))
                        else:
                            list_counter += 1

                        content = ordered_match.group(2).strip()
                        content = content.replace('"', '&quot;').replace("'", '&#39;')
                        story.append(Paragraph(f"{list_counter}. {content}", body_style))
                        continue

                    # Check for unordered lists (-, *, +)
                    unordered_match = re.match(r'^[-\*+]\s+(.*)', line)
                    if unordered_match:
                        if not in_list:
                            in_list = True
                            ordered_list = False
                        elif ordered_list:
                            # Switching to unordered list
                            ordered_list = False

                        content = unordered_match.group(1).strip()
                        content = content.replace('"', '&quot;').replace("'", '&#39;')
                        story.append(Paragraph(f"• {content}", body_style))
                        continue

                    # If we were in a list and this isn't a list item, end the list
                    if in_list:
                        in_list = False
                        ordered_list = False
                        story.append(Spacer(1, 6))

                    # Handle headers
                    if line.startswith('# '):
                        heading_text = line[2:].strip()
                        heading_text = heading_text.replace('"', '&quot;').replace("'", '&#39;')
                        story.append(Paragraph(heading_text, heading1_style))
                    elif line.startswith('## '):
                        heading_text = line[3:].strip()
                        heading_text = heading_text.replace('"', '&quot;').replace("'", '&#39;')
                        story.append(Paragraph(heading_text, heading2_style))
                    elif line.startswith('### '):
                        heading_text = line[4:].strip()
                        heading_text = heading_text.replace('"', '&quot;').replace("'", '&#39;')
                        story.append(Paragraph(heading_text, heading3_style))
                    else:
                        # Simple formatting for bold and italic with sanitization
                        formatted_line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
                        formatted_line = re.sub(r'\*(.*?)\*', r'<i>\1</i>', formatted_line)
                        # Sanitize the final text
                        formatted_line = formatted_line.replace('"', '&quot;').replace("'", '&#39;')
                        if formatted_line:
                            story.append(Paragraph(formatted_line, body_style))

            # Build PDF
            doc.build(story)

            if debug:
                print(f"Created PDF: {temp_file_path}", file=sys.stderr)

            # Verify the PDF was created successfully
            if not os.path.exists(temp_file_path) or os.path.getsize(temp_file_path) == 0:
                raise RuntimeError("PDF file was not created or is empty")

            return temp_file_path

        except Exception as e:
            error_msg = f"Error creating PDF: {e}"
            if debug:
                import traceback
                error_msg += f"\nFull traceback: {traceback.format_exc()}"
            # Return the error as a string instead of printing to stderr
            raise Exception(error_msg)

    def _html_to_paragraphs(self, html_content: str, body_style, h1_style, h2_style, h3_style):
        """Convert HTML content to ReportLab paragraphs with enhanced list support."""
        paragraphs = []
        lines = html_content.split('\n')

        in_ul = False
        in_ol = False
        list_counter = 0

        def sanitize_text(text):
            """Sanitize text for ReportLab Paragraph objects."""
            # Remove or replace problematic characters
            text = text.replace('"', '&quot;')
            text = text.replace("'", '&#39;')
            # Ensure the text is properly escaped for XML/HTML
            import html
            return html.escape(text)

        for line in lines:
            line = line.strip()
            if not line:
                if not in_ul and not in_ol:
                    paragraphs.append(Spacer(1, 6))
                continue

            # Handle list containers
            if line == '<ul>':
                in_ul = True
                continue
            elif line == '</ul>':
                in_ul = False
                paragraphs.append(Spacer(1, 6))
                continue
            elif line == '<ol>':
                in_ol = True
                list_counter = 0
                continue
            elif line == '</ol>':
                in_ol = False
                paragraphs.append(Spacer(1, 6))
                continue

            # Handle headers
            if line.startswith('<h1>'):
                content = re.sub(r'</?h1>', '', line)
                content = sanitize_text(content)
                paragraphs.append(Paragraph(content, h1_style))
            elif line.startswith('<h2>'):
                content = re.sub(r'</?h2>', '', line)
                content = sanitize_text(content)
                paragraphs.append(Paragraph(content, h2_style))
            elif line.startswith('<h3>'):
                content = re.sub(r'</?h3>', '', line)
                content = sanitize_text(content)
                paragraphs.append(Paragraph(content, h3_style))
            elif line.startswith('<li>'):
                content = re.sub(r'</?li>', '', line)
                content = sanitize_text(content)

                if in_ul:
                    # Unordered list item
                    content = f"• {content}"
                elif in_ol:
                    # Ordered list item
                    list_counter += 1
                    content = f"{list_counter}. {content}"
                else:
                    # Standalone list item
                    content = f"• {content}"

                paragraphs.append(Paragraph(content, body_style))
            elif line.startswith('<p>'):
                content = re.sub(r'</?p>', '', line)
                content = sanitize_text(content)
                paragraphs.append(Paragraph(content, body_style))
            elif line.startswith('<div') or line.startswith('</div>'):
                continue  # Skip container tags
            else:
                # Regular paragraph - sanitize content
                if not line.startswith('<'):
                    content = sanitize_text(line)
                    paragraphs.append(Paragraph(content, body_style))
                else:
                    # HTML content - try to render as-is
                    try:
                        paragraphs.append(Paragraph(line, body_style))
                    except:
                        # If it fails, extract text and render as plain
                        text_content = re.sub(r'<[^>]+>', '', line)
                        text_content = sanitize_text(text_content)
                        if text_content:
                            paragraphs.append(Paragraph(text_content, body_style))

        return paragraphs

    async def list_printers(self) -> str:
        """List available printers using PowerShell."""
        try:
            result = subprocess.run([
                'powershell', '-Command',
                'Get-Printer | Select-Object Name, DriverName, Status | ConvertTo-Json'
            ], capture_output=True, text=True, timeout=10)

            if result.returncode == 0 and result.stdout.strip():
                try:
                    import json
                    printers_data = json.loads(result.stdout)
                    if isinstance(printers_data, list) and printers_data:
                        printer_info = []
                        for printer in printers_data:
                            name = printer.get('Name', 'Unknown')
                            driver = printer.get('DriverName', 'Unknown Driver')
                            status = printer.get('Status', 'Unknown') or 'Ready'
                            printer_info.append(f"- {name}\n   Driver: {driver}\n   Status: {status}")

                        return "Available Printers:\n" + "\n\n".join(printer_info)
                    elif isinstance(printers_data, dict):
                        name = printers_data.get('Name', 'Unknown')
                        driver = printers_data.get('DriverName', 'Unknown Driver')
                        status = printers_data.get('Status', 'Unknown') or 'Ready'
                        return f"Available Printers:\n- {name}\n   Driver: {driver}\n   Status: {status}"
                except json.JSONDecodeError:
                    pass

            # Fallback: Simple printer listing
            result = subprocess.run([
                'powershell', '-Command',
                'Get-WmiObject -Class Win32_Printer | Select-Object -ExpandProperty Name'
            ], capture_output=True, text=True, timeout=10)

            if result.returncode == 0 and result.stdout.strip():
                lines = [line.strip() for line in result.stdout.strip().split('\n') if line.strip()]
                if lines:
                    return "Available Printers:\n" + "\n".join(f"- {line}" for line in lines)

            return "No printers found or unable to list printers."

        except Exception as e:
            return f"Error listing printers: {str(e)}"

    async def test_print(self, format4x6: bool = False, printer_name: Optional[str] = None) -> str:
        """Print a test page."""
        if format4x6:
            test_content = """# 4x6 Index Card Test

This is a **test page** for 4x6 index card printing.

## Features Tested:
- *Italic text*
- **Bold text**
- Headers (H1, H2, H3)
- Lists

### Card Specifications:
- Size: 4" x 6"
- Auto-scaling enabled
- Optimized fonts

If you can read this clearly, your 4x6 setup is working!
"""
        else:
            test_content = """# Printer Test Page

This is a **test page** to verify your printer setup.

## Features Tested:
- **Bold text** formatting
- *Italic text* formatting
- Headers (H1, H2)
- Lists and spacing
- Page layout

## System Information:
- Printer MCP Server v2.0.0 (Simplified)
- PDFtoPrinter integration
- Direct PDF printing
- Markdown formatting supported

If this page prints correctly, your setup is working!
"""

        return await self.print_file(
            content=test_content,
            filename="test_page",
            format4x6=format4x6,
            printer_name=printer_name,
            debug=True
        )

    def cleanup_temp_files(self):
        """Clean up temporary files."""
        for temp_file in self.temp_files:
            try:
                if os.path.exists(temp_file):
                    os.unlink(temp_file)
            except Exception as e:
                print(f"Error cleaning up {temp_file}: {e}", file=sys.stderr)

async def main():
    """Main entry point."""
    server = PrinterMCPServer()
    await server.run()

if __name__ == "__main__":
    asyncio.run(main())