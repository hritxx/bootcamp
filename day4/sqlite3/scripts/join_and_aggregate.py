import sys
import os
# Add the parent directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from product.queries import fetch_products_with_categories, total_inventory_value

print("Products with Categories:")
print(fetch_products_with_categories())

print("Total inventory value:")
print(total_inventory_value())