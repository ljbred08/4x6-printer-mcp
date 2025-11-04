#!/usr/bin/env python3
"""
Test with shorter content to ensure normal operation still works
"""

import asyncio
from server import PrinterMCPServer

async def test_short_validation():
    """Test validation fixes with shorter, reasonable content."""
    print("=== Short Content Validation Test ===\n")

    server_instance = PrinterMCPServer()

    short_content = """# Recipe: Quick Chocolate Chip Cookies

A simple recipe that should fit comfortably on 1-2 pages.

## Ingredients
- 2 cups flour
- 1 cup butter
- 3/4 cup sugar
- 2 eggs
- 1 tsp vanilla
- 2 cups chocolate chips

## Instructions
1. Preheat oven to 375°F
2. Mix dry ingredients
3. Cream butter and sugars
4. Add eggs and vanilla
5. Combine everything
6. Drop on baking sheet
7. Bake for 10-12 minutes

## Tips
- Use room temperature ingredients
- Don't overmix
- Cool on rack for 2 minutes

Perfect 4x6 index card size!
"""

    print("Testing with reasonable content that should fit on 2 pages...\n")

    try:
        result = await server_instance.print_file(
            content=short_content,
            filename="Short Validation Test",
            printer_name="Microsoft Print to PDF",
            format4x6=True,
            debug=True
        )
        print(f"\nResult: {result}")

        if "Successfully printed" in result:
            print("\n[SUCCESS] Short content validation working!")
            print("✅ All fixes working correctly for normal content")

    except Exception as e:
        print(f"Error: {e}")

    print("\n=== Short Content Validation Test Complete ===")

if __name__ == "__main__":
    asyncio.run(test_short_validation())