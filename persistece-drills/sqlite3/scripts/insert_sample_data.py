import sys
import os
# Add the parent directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from product.product_class import Product

p = Product()
p.add_product("Pen", 10.5)
p.add_product("Notebook", 25.0)
p.list_all()