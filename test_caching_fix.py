#!/usr/bin/env python3
"""
Test the caching fix to ensure each print job creates fresh content
"""

import asyncio
from server import PrinterMCPServer

async def test_caching_fix():
    """Test that different content creates fresh PDFs, not cached ones."""
    print("=== Caching Fix Test ===\n")

    server_instance = PrinterMCPServer()

    # First print job - short content
    content1 = """# First Test Content

This is the FIRST test content.
It should be printed exactly as written.

## Key Point 1
This content should appear in the first printout.
"""

    print("Testing first print job...")
    try:
        result1 = await server_instance.print_file(
            content=content1,
            filename="First Test",
            printer_name="Microsoft Print to PDF",
            format4x6=True,
            debug=True
        )
        print(f"First job result: {result1}\n")

    except Exception as e:
        print(f"First job error: {e}\n")

    # Second print job - different content
    content2 = """# SECOND Test Content

This is the COMPLETELY DIFFERENT second test content.
It should be printed instead of the first content.

## Key Point 2
This NEW content should appear in the second printout.
If the old content appears, there's a caching bug.
"""

    print("Testing second print job with different content...")
    try:
        result2 = await server_instance.print_file(
            content=content2,
            filename="Second Test",
            printer_name="Microsoft Print to PDF",
            format4x6=True,
            debug=True
        )
        print(f"Second job result: {result2}\n")

    except Exception as e:
        print(f"Second job error: {e}\n")

    # Third print job - yet different content
    content3 = """# THIRD Test Content

This is the YET ANOTHER different content.
It should be printed instead of any previous content.

## Key Point 3
This THIRD content should appear in the third printout.
Each printout should have unique, fresh content.
"""

    print("Testing third print job with yet different content...")
    try:
        result3 = await server_instance.print_file(
            content=content3,
            filename="Third Test",
            printer_name="Microsoft Print to PDF",
            format4x6=True,
            debug=True
        )
        print(f"Third job result: {result3}\n")

    except Exception as e:
        print(f"Third job error: {e}")

    print("=== Caching Fix Test Complete ===")
    print("Check the three PDF files to ensure they contain different content!")
    print("Each file should have unique text matching the content above.")

if __name__ == "__main__":
    asyncio.run(test_caching_fix())