#!/usr/bin/env python3
"""
Test script to verify PDF dimensions are correct for 4x6 format
"""

import asyncio
import os
from server import PrinterMCPServer

async def test_pdf_dimensions():
    """Test to verify PDF dimensions are correct."""
    print("=== PDF Dimensions Verification Test ===\n")

    server_instance = PrinterMCPServer()

    test_content = """# Test Content

This is a simple test to verify PDF dimensions.

## Section 1
Some content here.

## Section 2
More content here.

### Subsection
Even more content.

Final paragraph to test layout.
"""

    print("Creating PDF with format4x6=True...")
    print("Expected dimensions: 6\" x 4\" (432 x 288 points)\n")

    try:
        # Create PDF directly to check dimensions
        pdf_file = server_instance.create_formatted_pdf(
            content=test_content,
            filename="Dimensions Test",
            format4x6=True,
            debug=True
        )

        if pdf_file and os.path.exists(pdf_file):
            print(f"PDF created successfully: {pdf_file}")

            # Use PyPDF2 to check actual dimensions
            try:
                from PyPDF2 import PdfReader
                reader = PdfReader(pdf_file)
                page = reader.pages[0]

                # Get page dimensions in points
                width_pt = page.mediabox.width
                height_pt = page.mediabox.height

                # Convert to inches
                width_in = width_pt / 72
                height_in = height_pt / 72

                print(f"\nActual PDF dimensions:")
                print(f"  Points: {width_pt:.1f} x {height_pt:.1f}")
                print(f"  Inches: {width_in:.2f}\" x {height_in:.2f}\"")

                # Check if dimensions are correct
                expected_width_pt = 6 * 72  # 6 inches = 432 points
                expected_height_pt = 4 * 72  # 4 inches = 288 points

                if abs(width_pt - expected_width_pt) < 1 and abs(height_pt - expected_height_pt) < 1:
                    print("\n[SUCCESS] PDF dimensions are correct for 4x6 format!")
                else:
                    print(f"\n[ERROR] PDF dimensions are wrong!")
                    print(f"Expected: {expected_width_pt} x {expected_height_pt} points (6\" x 4\")")
                    print(f"Got: {width_pt} x {height_pt} points")

            except ImportError:
                print("\n[WARNING] PyPDF2 not available for dimension checking")
            except Exception as e:
                print(f"\n[ERROR] Error checking PDF dimensions: {e}")

            # Don't clean up so we can examine the file
            print(f"\nPDF file kept for manual inspection: {pdf_file}")

        else:
            print("[ERROR] Failed to create PDF")

    except Exception as e:
        print(f"[ERROR] Error: {e}")
        import traceback
        traceback.print_exc()

    print("\n=== PDF Dimensions Test Complete ===")

if __name__ == "__main__":
    asyncio.run(test_pdf_dimensions())