#!/usr/bin/env python3
"""
Test script for the enhanced auto-shrinking with verification
"""

import asyncio
import os
from server import PrinterMCPServer

async def test_verification_algorithm():
    """Test the enhanced auto-shrinking with verification."""
    print("=== Enhanced Auto-Shrinking Verification Test ===\n")

    server_instance = PrinterMCPServer()

    # Test content that should be around 2-3 pages without shrinking
    test_content = """# The Fall of Man

The Fall refers to Adam and Eve's disobedience in Genesis 3 when they ate from the forbidden tree.

## Historical Context

Understanding the Fall requires examining the historical and theological context in which Genesis was written. The narrative reflects ancient Near Eastern concepts about:

### The Nature of Humanity

- **Original State**: Created in God's image (Genesis 1:26-27)
- **Original Purpose**: To fellowship with God and steward creation
- **Original Location**: The Garden of Eden

### The Forbidden Tree

The Tree of the Knowledge of Good and Evil represents:
- A moral boundary set by God
- A test of trust and obedience
- The choice between dependence on God or autonomy

## The Temptation

### The Serpent's Strategy

1. **Question God's Word**: "Did God really say...?" (Genesis 3:1)
2. **Contradict God's Word**: "You will not surely die" (Genesis 3:4)
3. **Question God's Motives**: "God knows that when you eat... you will be like God" (Genesis 3:5)

### Eve's Response

Eve's response shows several problems:
- **Addition**: She adds "touch" to God's command (Genesis 3:3)
- **Minimization**: She reduces the consequence to avoid death
- **Desire**: The fruit appears "good for food and pleasing to the eye"

## The Act and Immediate Consequences

### The Choice

Both Adam and Eve made a conscious choice to:
- Disobey God's clear command
- Trust the creature over the Creator
- Seek wisdom apart from God

### Immediate Results

1. **Shame**: They realized their nakedness (Genesis 3:7)
2. **Fear**: They hid from God (Genesis 3:8-10)
3. **Blame**: They refused responsibility (Genesis 3:11-13)

## The Curse and Judgment

### Serpent's Curse

- Physical: Crawl on belly, eat dust
- Theological: Enmity with humanity
- Messianic: Protoevangelium in Genesis 3:15

### Woman's Curse

- Pain in childbirth
- Desire for husband
- Husband will rule

### Man's Curse

- Ground cursed
- Painful toil
- Return to dust

### Universal Consequences

1. **Separation from God**: Removed from the Garden
2. **Loss of Fellowship**: No longer walking with God
3. **Mortality**: Physical death becomes reality
4. **Corruption**: Sin nature passed to descendants

## The Broader Theological Implications

### Original Sin

The Fall introduces:
- **Inherited guilt**: All humanity shares in Adam's sin
- **Depraved nature**: Inability to choose good without God
- **Spiritual death**: Separation from God's presence

### Covenant Impact

The Fall affects:
- **Noahic Covenant**: Preservation despite judgment
- **Abrahamic Covenant**: Blessing to all nations
- **Mosaic Covenant**: Law reveals sinfulness
- **Davidic Covenant**: Promise of eternal king
- **New Covenant**: Restoration through Christ

## Christ's Redemptive Work

### Romans 5:12-21

**Adam's trespass vs. Christ's obedience**:
- Sin entered through one man (Adam)
- Grace comes through one man (Christ)
- Condemnation for all vs. justification for many
- Death reigns vs. grace reigns

### 1 Corinthians 15:21-22

**Resurrection parallel**:
- Death through Adam
- Life through Christ
- Natural body vs. spiritual body

## Practical Applications

### Understanding Human Nature

The Fall explains:
- Why people struggle with sin
- Why relationships are difficult
- Why suffering exists
- Why we need a Savior

### Christian Living

Response to the Fall includes:
- **Humility**: Recognizing our fallen state
- **Dependence**: Relying on Christ's righteousness
- **Hope**: Anticipating full restoration
- **Mission**: Sharing the good news of redemption

### Eschatological Hope

The Fall will be fully reversed when:
- Christ returns and establishes His kingdom
- Creation is freed from its bondage
- believers receive glorified bodies
- God dwells with His people eternally

## Conclusion

The Fall of Man represents the pivotal moment in human history when sin entered the world through disobedience. Yet even in judgment, God provided hope through the promise of redemption in Genesis 3:15. This protoevangelium points forward to Christ's ultimate victory over sin and death, offering restoration to all who trust in Him.

The doctrine of the Fall provides essential context for understanding:
- The human condition and universal sinfulness
- The necessity of Christ's atoning work
- The Christian hope of future glorification
- The urgency of evangelism and missions

As we study the Fall, we're reminded of both the seriousness of sin and the greatness of God's grace—grace that reaches even into the deepest consequences of human rebellion to bring about redemption and restoration.
"""

    print("Testing enhanced auto-shrinking with verification...")
    print("This should create a PDF that fits on exactly 2 4x6 pages.\n")

    try:
        result = await server_instance.print_file(
            content=test_content,
            filename="Enhanced Verification Test",
            printer_name="Microsoft Print to PDF",
            format4x6=True,
            debug=True
        )
        print(f"\nResult: {result}")

        # Extract PDF file path from result if successful
        if "Successfully printed" in result:
            print("\n[SUCCESS] Enhanced auto-shrinking with verification test completed!")
            print("The algorithm should have:")
            print("1. Used estimation to get initial font/spacing values")
            print("2. Created test PDFs and counted actual pages")
            print("3. Iteratively adjusted until content fits on exactly 2 pages")
            print("4. Produced a final PDF with optimal sizing")

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

    print("\n=== Enhanced Verification Test Complete ===")

if __name__ == "__main__":
    asyncio.run(test_verification_algorithm())