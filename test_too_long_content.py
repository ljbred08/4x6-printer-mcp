#!/usr/bin/env python3
"""
Test script with extremely long content that should trigger error handling
"""

import asyncio
import os
from server import PrinterMCPServer

async def test_too_long_content():
    """Test error handling with content that's too long for 2 pages."""
    print("=== Too Long Content Test (Should Return Error) ===\n")

    server_instance = PrinterMCPServer()

    # Generate extremely long content that won't fit even at 6pt font
    long_content = "# Extremely Long Document\n\n"

    # Add many chapters/sections
    for chapter in range(1, 31):  # 30 chapters!
        long_content += f"## Chapter {chapter}: Detailed Analysis\n\n"

        # Add detailed content for each chapter
        topics = ["Introduction", "Background", "Methodology", "Results", "Discussion",
                 "Conclusion", "References", "Appendix", "Further Reading", "Summary"]

        for topic in topics:
            long_content += f"### {topic}\n\n"

            # Add multiple paragraphs for each topic
            for para in range(3):
                long_content += f"This is paragraph {para+1} about {topic} in Chapter {chapter}. "
                long_content += "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                long_content += "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
                long_content += "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
                long_content += "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
                long_content += "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
                long_content += "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
                long_content += "culpa qui officia deserunt mollit anim id est laborum.\n\n"

        long_content += "---\n\n"

    print(f"Generated content with ~{len(long_content)} characters")
    print("Testing error handling with extremely long content...\n")

    try:
        result = await server_instance.print_file(
            content=long_content,
            filename="Too Long Content Test",
            printer_name="Microsoft Print to PDF",
            format4x6=True,
            debug=True
        )
        print(f"\nUnexpected success: {result}")
        print("This suggests the algorithm may still be too permissive.")

    except Exception as e:
        print(f"\nExpected error caught: {e}")

        if "too long to fit" in str(e).lower():
            print("\n[SUCCESS] Error handling working correctly!")
            print("The algorithm properly:")
            print("1. Detected content was too long")
            print("2. Returned an informative error message")
            print("3. Suggested solutions (reduce content or use regular format)")
        else:
            print("\n[PARTIAL] Error occurred but may not be the expected 'too long' error.")

    print("\n=== Too Long Content Test Complete ===")

if __name__ == "__main__":
    asyncio.run(test_too_long_content())