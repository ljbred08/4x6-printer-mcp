#!/usr/bin/env python3
"""
Test script with content that should require exactly 2 pages
"""

import asyncio
import os
from server import PrinterMCPServer

async def test_2page_content():
    """Test with content that should require shrinking to fit on 2 pages."""
    print("=== 2-Page Content Test ===\n")

    server_instance = PrinterMCPServer()

    # Content that should be around 3+ pages without shrinking
    long_content = """# Comprehensive Bible Study Guide: Romans Chapter 8

## Introduction: The Greatest Chapter in the Bible

Romans 8 is often considered the greatest chapter in the Bible, describing the glorious life in the Spirit and the ultimate victory believers have in Christ. This chapter provides profound theological insights into:

- Our position in Christ
- The work of the Holy Spirit
- Freedom from condemnation
- Future glory and suffering
- God's unbreakable love

## Key Themes and Verses

### 1. No Condemnation (Romans 8:1)

**Therefore, there is now no condemnation for those who are in Christ Jesus**

This opening verse sets the tone for the entire chapter. The "therefore" connects to Romans 7 where Paul struggled with sin. The solution isn't trying harder but being "in Christ Jesus."

**Theological Implications:**
- Past condemnation is removed
- Present condemnation is absent
- Future condemnation is impossible
- This is our positional reality, not conditional on performance

### 2. The Law of the Spirit of Life (Romans 8:2)

**Because through Christ Jesus the law of the Spirit who gives life has set you free from the law of sin and death.**

Two laws are contrasted:
- **Law of sin and death**: The Mosaic Law that reveals sin but cannot save
- **Law of the Spirit of life**: The new covenant principle that gives life

**Practical Application:** We operate under a different principle now—not trying to keep rules, but walking in the Spirit's power.

### 3. God's Solution to Sin (Romans 8:3-4)

**For what the law was powerless to do because it was weakened by the flesh, God did by sending his own Son... in order that the righteous requirement of the law might be fully met in us, who do not live according to the flesh but according to the Spirit.**

**The Problem:** The Law was good but powerless because of human weakness.

**God's Solution:**
- He sent His own Son (incarnation)
- As a sin offering (atonement)
- To condemn sin in the flesh (victory over sin)
- So righteousness could be fulfilled in us (impartation)

### 4. Two Mindsets, Two Results (Romans 8:5-8)

**Those who live according to the flesh have their minds set on what the flesh desires; but those who live in accordance with the Spirit have their minds set on what the Spirit desires.**

**The Fleshly Mindset:**
- Focused on earthly things
- Results in death
- Hostile to God
- Cannot please God

**The Spiritual Mindset:**
- Focused on eternal things
- Results in life and peace
- Submissive to God
- Pleases God

**Self-Examination Questions:**
1. What dominates my thoughts throughout the day?
2. Where do I find my ultimate satisfaction?
3. How do I respond to difficulty and temptation?
4. What is my primary ambition in life?

### 5. The Spirit's Indwelling (Romans 8:9-11)

**You, however, are not in the realm of the flesh but are in the realm of the Spirit, if indeed the Spirit of God lives in you.**

**Three Proofs of the Spirit's Indwelling:**
1. **Positional Reality**: "You are not in the flesh but in the Spirit"
2. **Indwelling Presence**: "The Spirit of God lives in you"
3. **Life-Giving Power**: "The Spirit who raised Jesus from the dead lives in you"

**Practical Implications:**
- The same power that raised Christ lives in you
- Your mortal body can be given life
- You have obligation to live by the Spirit

### 6. Children and Heirs (Romans 8:12-17)

**For those who are led by the Spirit of God are the children of God.**

**Our Obligation (v. 12-13):**
- Not to the flesh (to live according to it)
- But to put to death the misdeeds of the body by the Spirit

**Our Adoption (v. 14-17):**
- **Led by the Spirit**: Evidence of being God's children
- **Spirit of adoption**: Not fear but intimacy ("Abba, Father")
- **Heirs with Christ**: Sharing in His suffering and glory

**The Adoption Process:**
1. **Legal adoption**: Made children of God
2. **Family relationship**: "Abba, Father" (intimate address)
3. **Inheritance rights**: Heirs of God and co-heirs with Christ

### 7. Future Glory and Present Suffering (Romans 8:18-25)

**I consider that our present sufferings are not worth comparing with the glory that will be revealed in us.**

**The Suffering-Glory Principle:**
- Present sufferings are temporary and light
- Future glory is eternal and weighty
- Creation itself eagerly awaits our glorification

**Creation's Groaning (v. 19-22):**
- **Bondage to decay**: All creation affected by the Fall
- **Eager expectation**: Creation waits for the sons of God to be revealed
- **Groaning together**: All creation experiences frustration

**Our Groaning (v. 23-25):**
- **Firstfruits**: We have the Spirit as guarantee
- **Groan inwardly**: We long for our full adoption
- **Wait eagerly**: We hope for what we don't yet see

### 8. The Spirit's Help in Our Weakness (Romans 8:26-27)

**In the same way, the Spirit helps us in our weakness. We do not know what we ought to pray for, but the Spirit himself intercedes for us through wordless groans.**

**Three Ministries of the Spirit in Prayer:**
1. **Helps in our weakness**: When we don't know how to pray
2. **Intercedes for us**: The Spirit prays for us
3. **Prays according to God's will**: Perfect alignment with God's purposes

**The Problem We Face:**
- We often don't know what's best for us
- We can't see the big picture
- Our emotions can cloud our judgment

**The Spirit's Solution:**
- Perfect knowledge of God's will
- Eternal perspective
- Pure motives and desires

### 9. God's Sovereign Plan (Romans 8:28-30)

**And we know that in all things God works for the good of those who love him, who have been called according to his purpose.**

**The Golden Chain of Redemption:**
1. **Foreknew**: God's foreknowledge and choice
2. **Predestined**: Determined to be conformed to Christ's image
3. **Called**: Effectual calling through the Gospel
4. **Justified**: Declared righteous through faith
5. **Glorified**: Future completion of salvation

**Key Observations:**
- This is past tense from God's perspective
- Each step guarantees the next
- The end goal is Christlikeness
- This applies to "those who love him"

### 10. God's Unfailing Love (Romans 8:31-39)

**If God is for us, who can be against us?**

**Five Unanswerable Questions (v. 31-34):**
1. **If God is for us, who can be against us?** (v. 31)
2. **He who did not spare His own Son... will He not also graciously give us all things?** (v. 32)
3. **Who will bring any charge against those whom God has chosen?** (v. 33)
4. **Who then is the one who condemns?** (v. 34)
5. **Who shall separate us from the love of Christ?** (v. 35)

**The Answer to All: NO ONE!**

**Nothing Can Separate Us (v. 35-39):**
- **Trouble or hardship**: External difficulties
- **Persecution or famine**: Religious and physical trials
- **Nakedness or danger**: Vulnerability and threats
- **Sword**: Execution and death
- **Neither death nor life**: The ultimate extremes
- **Neither angels nor demons**: The spiritual realm
- **Neither the present nor the future**: Time itself
- **Nor any powers**: All authorities
- **Nor height nor depth**: Geographic or spatial limitations
- **Nor anything else in all creation**: Complete, total coverage

**The Conclusion:** We are more than conquerors through Him who loved us!

## Practical Applications from Romans 8

### Daily Living

1. **Walk in the Spirit**: Live by His power, not your own strength
2. **Set your mind on things above**: Focus on eternal realities
3. **Remember your identity**: You are God's child, not a slave to fear
4. **Embrace suffering with purpose**: It's working for your glory
5. **Pray with confidence**: The Spirit is helping you

### Spiritual Warfare

1. **No condemnation**: Your identity is secure in Christ
2. **Spirit's power**: The same power that raised Christ lives in you
3. **Future focus**: Present trials can't compare with future glory
4. **God's sovereignty**: He's working all things for your good
5. **Love's security**: Nothing can separate you from God's love

### Eternal Perspective

1. **Adoption completed**: We're waiting for the full manifestation
2. **Creation restored**: All creation will be renewed
3. **Glorification guaranteed**: The golden chain ensures it
4. **Victory assured**: We're more than conquerors
5. **Love eternal**: Nothing can separate us from His love

## Conclusion: Living in Romans 8 Reality

Romans 8 isn't just theological truth—it's meant to be our daily experience. We are called to live as people who:

- Are free from all condemnation
- Walk in the Spirit's power
- Live as beloved children of God
- Endure suffering with future hope
- Pray with Spirit-given confidence
- Trust God's sovereign plan
- Rest in His unbreakable love

**The Challenge:** Will you live like this is true? Will you walk in the freedom, power, and love that Romans 8 describes?

This is our birthright as believers. This is the normal Christian life. This is living in the reality of Romans 8!

*Study Questions for Further Reflection:*
1. Which verse or section of Romans 8 speaks most to your current situation?
2. How would your daily life change if you fully believed Romans 8:1?
3. What practical steps can you take to "set your mind on things above"?
4. How does understanding God's sovereignty (Romans 8:28) change how you view trials?
5. In what area do you need to rest more fully in God's unfailing love?

*Memory Verses:*
- Romans 8:1 - "Therefore, there is now no condemnation for those who are in Christ Jesus"
- Romans 8:28 - "And we know that in all things God works for the good of those who love him"
- Romans 8:31 - "If God is for us, who can be against us?"
- Romans 8:37 - "No, in all these things we are more than conquerors through him who loved us"
- Romans 8:39 - "Neither height nor depth, nor anything else in all creation, will be able to separate us from the love of God"
"""

    print("Testing with long content that should require shrinking to fit on 2 pages...")
    print("This should demonstrate the iterative verification algorithm working.\n")

    try:
        result = await server_instance.print_file(
            content=long_content,
            filename="2-Page Content Test",
            printer_name="Microsoft Print to PDF",
            format4x6=True,
            debug=True
        )
        print(f"\nResult: {result}")

        if "Successfully printed" in result:
            print("\n[SUCCESS] 2-page content test completed!")
            print("The algorithm should have:")
            print("1. Started with estimation showing content too large")
            print("2. Created test PDFs and counted actual pages")
            print("3. Iteratively reduced font size and spacing")
            print("4. Stopped when content fit on exactly 2 pages")

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

    print("\n=== 2-Page Content Test Complete ===")

if __name__ == "__main__":
    asyncio.run(test_2page_content())