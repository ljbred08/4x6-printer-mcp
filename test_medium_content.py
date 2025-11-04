#!/usr/bin/env python3
"""
Test script with medium-length content
"""

import asyncio
import os
from server import PrinterMCPServer

async def test_medium_content():
    """Test with medium-length content."""
    print("=== Medium Content Test ===\n")

    server_instance = PrinterMCPServer()

    # Medium content that should require some shrinking but not to minimum
    medium_content = """# Comprehensive Guide to Container Gardening

## Introduction
Container gardening is a versatile way to grow plants in limited space. Whether you have a small balcony, patio, or just want to add greenery to your home, containers offer flexibility and control.

## Choosing Containers

### Types of Containers
- **Terra cotta pots**: Classic, porous, good drainage
- **Plastic containers**: Lightweight, retain moisture well
- **Ceramic pots**: Attractive, heavy, good for stability
- **Fabric grow bags**: Excellent drainage, prevent root circling
- **Wooden planters**: Natural look, good insulation

### Size Considerations
- **Small containers (6-12 inches)**: Herbs, lettuce, radishes
- **Medium containers (12-18 inches)**: Bush beans, carrots, peppers
- **Large containers (18+ inches)**: Tomatoes, potatoes, small shrubs

## Soil Selection

### Container Mix Ingredients
- **Peat moss or coco coir**: Moisture retention
- **Perlite or vermiculite**: Aeration and drainage
- **Compost**: Nutrients and organic matter
- **Sand**: Improve drainage for heavy soils

### Recommended Soil Recipe
```
2 parts peat moss
1 part perlite
1 part compost
1/2 part sand
```

## Plant Selection

### Easy Vegetables for Containers
1. **Leafy greens**: Lettuce, spinach, kale
2. **Root vegetables**: Radishes, carrots, beets
3. **Fruiting plants**: Cherry tomatoes, peppers, eggplant
4. **Herbs**: Basil, mint, rosemary, thyme

### Container-Friendly Flowers
- **Annuals**: Petunias, marigolds, zinnias
- **Perennials**: Hostas, daylilies, coral bells
- **Trailing plants**: Ivy, petunias, sweet potato vine

## Planting Guidelines

### Spacing Recommendations
- **Small plants**: 4-6 inches apart
- **Medium plants**: 8-12 inches apart
- **Large plants**: 18-24 inches apart

### Planting Depth
- Plant at the same depth as in nursery pot
- For tomatoes, plant deeper (up to first leaves)
- Ensure proper root spreading

## Watering Strategies

### Frequency Guidelines
- **Hot weather**: Daily watering may be needed
- **Mild weather**: Every 2-3 days
- **Cool weather**: Every 4-5 days
- **Always check soil moisture first**

### Watering Techniques
- Water thoroughly until drainage occurs
- Water soil surface, not leaves
- Morning watering is ideal
- Use drip irrigation for consistent moisture

## Fertilizing Schedule

### Feeding Guidelines
- **Liquid fertilizer**: Every 2-4 weeks during growing season
- **Slow-release granules**: Every 2-3 months
- **Compost tea**: Monthly during active growth

### Nutrient Needs
- **Nitrogen (N)**: Leafy growth
- **Phosphorus (P)**: Root and flower development
- **Potassium (K)**: Overall plant health

## Common Problems and Solutions

### Pest Management
- **Aphids**: Spray with soapy water
- **Spider mites**: Increase humidity, use miticide
- **Whiteflies**: Yellow sticky traps, insecticidal soap

### Disease Prevention
- **Root rot**: Ensure proper drainage
- **Powdery mildew**: Improve air circulation
- **Fungal issues**: Avoid overhead watering

## Seasonal Care

### Spring Tasks
- Clean and disinfect containers
- Refresh potting soil
- Start cool-season crops
- Begin fertilizing schedule

### Summer Maintenance
- Increase watering frequency
- Provide afternoon shade for heat-sensitive plants
- Monitor for pests and diseases
- Harvest regularly to encourage production

### Fall Preparation
- Plant cool-season crops
- Reduce fertilizing
- Prepare tender plants for indoor overwintering
- Clean up dead plant material

### Winter Care
- Protect containers from freezing
- Reduce watering significantly
- Move sensitive plants indoors
- Plan for spring gardening

## Conclusion
Container gardening offers endless possibilities for growing plants in any space. With proper container selection, soil preparation, and regular care, you can create a thriving garden that provides beauty and fresh produce throughout the growing season.

Happy gardening!
"""

    print("Testing with medium-length content...")
    print("This should require some shrinking but maintain decent readability (7-10pt range).\n")

    try:
        result = await server_instance.print_file(
            content=medium_content,
            filename="Medium Content Test",
            printer_name="Microsoft Print to PDF",
            format4x6=True,
            debug=True
        )
        print(f"\nResult: {result}")

        if "Successfully printed" in result:
            print("\n[SUCCESS] Medium content test completed!")
            print("The algorithm should have found a balance between:")
            print("- Good readability (hopefully 7-10pt font)")
            print("- Proper fitting on 2 pages")
            print("- Appropriate spacing")

    except Exception as e:
        print(f"Error: {e}")
        if "too long to fit" in str(e):
            print("This suggests the content may be too long even with the improved algorithm.")

    print("\n=== Medium Content Test Complete ===")

if __name__ == "__main__":
    asyncio.run(test_medium_content())