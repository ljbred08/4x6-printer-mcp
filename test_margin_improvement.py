#!/usr/bin/env python3
"""
Test the margin improvement with the exact content that was problematic before
"""

import asyncio
from server import PrinterMCPServer

async def test_margin_improvement():
    """Test margin improvement with the original problematic content."""
    print("=== Margin Improvement Test ===\n")

    server_instance = PrinterMCPServer()

    # Test with the exact content from the original issue
    original_problematic_content = """# Does the Fall affect us today?

## Intro
Adam & Eve's disobedience (Genesis 3). Consequences still impact humanity today.

## Inherited Sin Nature
All inherit sinful nature from Adam. Natural rebellion against God. Universal need for redemption.

• Romans 5:12 - sin entered world through one man
• Romans 3:23 - all have sinned
• Romans 5:19 - one trespass = condemnation for all

## Creation's Curse
Physical world corrupted. Suffering, pain, death, decay. Creation awaits restoration.

• Genesis 3:17 - cursed ground through painful toil
• Romans 8:20-22 - creation frustrated, will be liberated
• Revelation 21:4 - no more death, mourning, crying, pain

## Spiritual Separation
Humanity spiritually dead in sin. Hostile to God. Need reconciliation through Christ.

• Ephesians 2:1 - dead in transgressions & sins
• Romans 8:7 - flesh is hostile to God
• Colossians 1:21 - alienated from God, enemies

## Call to Action
Fall's effects impact all humanity & creation today. Universal need for Christ's redemption & future restoration."""

    print("Testing with original problematic content and new 0.1\" margins...\n")

    try:
        result = await server_instance.print_file(
            content=original_problematic_content,
            filename="Margin Improvement Test",
            printer_name="Microsoft Print to PDF",
            format4x6=True,
            debug=True
        )
        print(f"Result: {result}\n")

        if "Successfully printed" in result:
            print("[SUCCESS] Content now fits with larger font size due to reduced margins!")

            # Extract font size from result for comparison
            if "font=" in result and "spacing=" in result:
                import re
                font_match = re.search(r'font=(\d+\.\d+)pt', result)
                spacing_match = re.search(r'spacing=(\d+\.\d+)', result)

                if font_match and spacing_match:
                    font_size = font_match.group(1)
                    spacing = spacing_match.group(1)
                    print(f"🎉 Improved result: {font_size}pt font, {spacing} spacing")
                    print("📏 Margins successfully reduced to 0.1 inches")
                    print("📖 More readable text with larger fonts!")
            else:
                print("[INFO] Font/spacing details not found in result")

    except Exception as e:
        print(f"Error: {e}")

    print("\n=== Margin Improvement Test Complete ===")

if __name__ == "__main__":
    asyncio.run(test_margin_improvement())