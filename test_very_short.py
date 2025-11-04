#!/usr/bin/env python3
"""
Test with very short content to verify the fix works
"""

import asyncio
from server import PrinterMCPServer

async def test_very_short():
    """Test with very short content that should fit easily."""
    print("=== Very Short Content Test ===\n")

    server_instance = PrinterMCPServer()

    # Very short content that should fit on 1 page
    very_short_content = """# Quick Note

Just a quick test.

## Status
Working great!

Perfect fit for 4x6.
"""

    print("Testing with very short content that should fit on 1-2 pages...\n")

    try:
        result = await server_instance.print_file(
            content=very_short_content,
            filename="Very Short Test",
            printer_name="Microsoft Print to PDF",
            format4x6=True,
            debug=True
        )
        print(f"\nResult: {result}")

        if "Successfully printed" in result:
            print("\n[SUCCESS] Very short content worked!")
            print("✅ Unified architecture working correctly")

    except Exception as e:
        print(f"Error: {e}")

    print("\n=== Very Short Content Test Complete ===")

if __name__ == "__main__":
    asyncio.run(test_very_short())