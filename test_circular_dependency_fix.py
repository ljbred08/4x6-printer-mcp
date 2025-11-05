#!/usr/bin/env python3
"""
Test the fixed algorithm with the problematic content that was showing inconsistent behavior
"""

import asyncio
from server import PrinterMCPServer

async def test_circular_dependency_fix():
    """Test the fixed algorithm with problematic content."""
    print("=== Circular Dependency Fix Test ===\n")

    server_instance = PrinterMCPServer()

    # This is the longer content that couldn't fit even at 6pt before the fix
    longer_content = """# Does the Fall affect us today?

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

    # This is the shorter content that fit easily at 12pt before the fix
    shorter_content = """# Does the Fall affect us today?

Adam & Eve's disobedience (Genesis 3) still impacts humanity today.

## Inherited Sin Nature
All inherit sinful nature. Natural rebellion against God.

• Romans 5:12 - sin entered world through one man
• Romans 3:23 - all have sinned

## Creation's Curse
Physical world corrupted. Suffering, pain, death, decay.

• Genesis 3:17 - cursed ground through painful toil
• Romans 8:20-22 - creation will be liberated
• Revelation 21:4 - no more death, pain

## Spiritual Separation
Humanity spiritually dead in sin. Hostile to God.

• Ephesians 2:1 - dead in transgressions & sins
• Romans 8:7 - flesh is hostile to God
• Colossians 1:21 - alienated from God

## Call to Action
Fall's effects impact all today. Need Christ's redemption & restoration."""

    print("Testing longer content (should now find optimal font size correctly)...\n")

    try:
        result1 = await server_instance.print_file(
            content=longer_content,
            filename="Circular Dependency Test - Longer Content",
            printer_name="Microsoft Print to PDF",
            format4x6=True,
            debug=True
        )
        print(f"Longer content result: {result1}\n")

        if "Successfully printed" in result1:
            print("[SUCCESS] Longer content now works with proper font scaling!")
        else:
            print("[EXPECTED] Longer content properly rejected if it truly doesn't fit")

    except Exception as e:
        print(f"Longer content error: {e}\n")

    print("Testing shorter content (should still work but maybe with different font size)...\n")

    try:
        result2 = await server_instance.print_file(
            content=shorter_content,
            filename="Circular Dependency Test - Shorter Content",
            printer_name="Microsoft Print to PDF",
            format4x6=True,
            debug=True
        )
        print(f"Shorter content result: {result2}\n")

        if "Successfully printed" in result2:
            print("[SUCCESS] Shorter content still works!")
            # Check if font/spacing details are in the success message
            if "font=" in result2 and "spacing=" in result2:
                print("[SUCCESS] Font/spacing details included in success message!")
            else:
                print("[INFO] Font/spacing details not found in success message")

    except Exception as e:
        print(f"Shorter content error: {e}")

    print("\n=== Circular Dependency Fix Test Complete ===")

if __name__ == "__main__":
    asyncio.run(test_circular_dependency_fix())