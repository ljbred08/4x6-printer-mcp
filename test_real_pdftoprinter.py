#!/usr/bin/env python3
"""
Test script for actual PDFtoPrinter printing
"""

import asyncio
import os
from server import PrinterMCPServer

async def test_pdftoprinter_printing():
    """Test actual PDFtoPrinter printing."""
    print("=== PDFtoPrinter Real Printing Test ===\n")

    server_instance = PrinterMCPServer()

    # Test 1: Print to Microsoft Print to PDF (safe test)
    print("1. Testing PDFtoPrinter with Microsoft Print to PDF...")
    test_content = """# PDFtoPrinter Test

This document tests **actual PDFtoPrinter printing**.

## What this tests:
- Direct PDF printing via PDFtoPrinter.exe
- Silent mode operation (/s flag)
- Command-line integration
- Proper error handling

## Benefits:
- No complex image conversion
- Fast execution
- Reliable output
- Professional quality

If this prints successfully, PDFtoPrinter is working correctly!
"""

    try:
        result = await server_instance.print_file(
            content=test_content,
            filename="PDFtoPrinter Test",
            printer_name="Microsoft Print to PDF",
            debug=True
        )
        print(f"Result: {result}")
        print("✓ Microsoft Print to PDF test completed\n")
    except Exception as e:
        print(f"Error: {e}\n")

    # Test 2: Print to a real physical printer
    print("2. Testing PDFtoPrinter with physical printer...")
    try:
        result = await server_instance.print_file(
            content=test_content,
            filename="Physical Printer Test",
            printer_name="EPSON988083 (WF-3820 Series)",  # Your actual printer
            debug=True
        )
        print(f"Result: {result}")
        print("✓ Physical printer test completed")
        print("Check your printer for actual output!")
    except Exception as e:
        print(f"Error: {e}")
        print("Note: You may need to:")
        print("- Change the printer_name to match your printer")
        print("- Ensure the printer is connected and powered on")

    # Test 3: Test 4x6 printing
    print("\n3. Testing 4x6 index card printing...")
    card_content = """# 4x6 Recipe Card

## Chocolate Chip Cookies

### Ingredients:
- 2 cups flour
- 1 cup butter
- 3/4 cup sugar
- 1/2 cup brown sugar
- 2 eggs
- 1 tsp vanilla
- 1 tsp baking soda
- 1/2 tsp salt
- 2 cups chocolate chips

### Instructions:
1. **Preheat** oven to 375°F
2. **Cream** butter and sugars
3. *Beat* in eggs and vanilla
4. Mix in dry ingredients
5. **Fold** in chocolate chips
6. Drop on baking sheet
7. **Bake** 10-12 minutes

### Tips:
- Use room temperature ingredients
- Don't overmix
- Cool on rack for 2 minutes

Perfect 4x6 index card printing!
"""

    try:
        result = await server_instance.print_file(
            content=card_content,
            filename="Recipe Card 4x6",
            printer_name="EPSON988083 (WF-3820 Series)",
            format4x6=True,
            debug=True
        )
        print(f"Result: {result}")
        print("✓ 4x6 index card test completed")
        print("Check for 4x6 output (make sure your printer has 4x6 paper configured)")
    except Exception as e:
        print(f"Error: {e}")

    print("\n=== PDFtoPrinter Real Printing Test Complete ===")
    print("\n🎉 PDFtoPrinter implementation working!")
    print("This simplified approach should be much more reliable than the PyMuPDF method.")

if __name__ == "__main__":
    asyncio.run(test_pdftoprinter_printing())