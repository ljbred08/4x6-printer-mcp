#!/usr/bin/env python3
"""
Test script with short content that should use larger fonts
"""

import asyncio
import os
from server import PrinterMCPServer

async def test_short_content():
    """Test with short content that should maintain larger fonts."""
    print("=== Short Content Test (Should Use Larger Fonts) ===\n")

    server_instance = PrinterMCPServer()

    # Short content that should fit comfortably with larger fonts
    short_content = """# Recipe: Quick Chocolate Chip Cookies

## Ingredients
- 2 cups all-purpose flour
- 1 tsp baking soda
- 1 tsp salt
- 1 cup butter, softened
- 3/4 cup sugar
- 3/4 cup brown sugar
- 2 large eggs
- 2 tsp vanilla extract
- 2 cups chocolate chips

## Instructions
1. **Preheat** oven to 375°F
2. **Mix** flour, baking soda, and salt in bowl
3. **Cream** butter and sugars until fluffy
4. **Beat** in eggs and vanilla
5. **Gradually** blend in flour mixture
6. **Stir** in chocolate chips
7. **Drop** rounded tablespoons onto baking sheet
8. **Bake** 9-11 minutes until golden brown
9. **Cool** on baking sheet for 2 minutes
10. **Transfer** to wire rack

## Tips
- Use room temperature ingredients
- Don't overmix the dough
- Chill dough for 30 min for thicker cookies

Perfect for 4x6 index card!
"""

    print("Testing with short content that should use larger fonts (8-12pt range)...")
    print("This should demonstrate the readability-first approach.\n")

    try:
        result = await server_instance.print_file(
            content=short_content,
            filename="Short Content Test",
            printer_name="Microsoft Print to PDF",
            format4x6=True,
            debug=True
        )
        print(f"\nResult: {result}")

        if "Successfully printed" in result:
            print("\n[SUCCESS] Short content test completed!")
            print("The algorithm should have:")
            print("1. Started testing from 12pt font")
            print("2. Found a larger readable font (ideally 8-11pt)")
            print("3. Used appropriate spacing for readability")
            print("4. Fit comfortably on 2 pages with good readability")

    except Exception as e:
        print(f"Error: {e}")
        if "too long to fit" in str(e):
            print("This suggests there may still be an issue with the height estimation.")

    print("\n=== Short Content Test Complete ===")

if __name__ == "__main__":
    asyncio.run(test_short_content())