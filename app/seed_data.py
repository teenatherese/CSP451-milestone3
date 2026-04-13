"""
CloudMart - Seed Data Script

Populates the products container with sample e-commerce products.

Run once:
    python -m app.seed_data
"""

import os
import sys
from azure.cosmos import CosmosClient

# Environment variables
COSMOS_ENDPOINT = os.getenv("COSMOS_ENDPOINT", "")
COSMOS_KEY = os.getenv("COSMOS_KEY", "")
DATABASE_NAME = "cloudmart"

# Sample product data
PRODUCTS = [
    {
        "id": "1",
        "name": "Wireless Bluetooth Headphones",
        "category": "Electronics",
        "price": 79.99,
        "description": "Premium noise-cancelling wireless headphones with 30-hour battery life.",
        "image_url": "https://img.icons8.com/3d-fluency/94/headphones.png",
        "in_stock": True
    },
    {
        "id": "2",
        "name": "USB-C Fast Charging Cable (3-Pack)",
        "category": "Electronics",
        "price": 19.99,
        "description": "Durable braided USB-C cables supporting fast charging.",
        "image_url": "https://img.icons8.com/3d-fluency/94/usb-c.png",
        "in_stock": True
    },
    {
        "id": "3",
        "name": "Mechanical Keyboard (RGB)",
        "category": "Electronics",
        "price": 129.99,
        "description": "Mechanical keyboard with RGB lighting and aluminum frame.",
        "image_url": "https://img.icons8.com/3d-fluency/94/keyboard.png",
        "in_stock": True
    },
    {
        "id": "4",
        "name": "Classic Denim Jacket",
        "category": "Clothing",
        "price": 89.99,
        "description": "Timeless denim jacket made from premium cotton.",
        "image_url": "https://img.icons8.com/3d-fluency/94/jacket.png",
        "in_stock": True
    },
    {
        "id": "5",
        "name": "Performance Running Shoes",
        "category": "Clothing",
        "price": 149.99,
        "description": "Lightweight running shoes with breathable design.",
        "image_url": "https://img.icons8.com/3d-fluency/94/running-shoe.png",
        "in_stock": True
    },
    {
        "id": "6",
        "name": "Organic Cotton T-Shirt",
        "category": "Clothing",
        "price": 34.99,
        "description": "Soft organic cotton t-shirt.",
        "image_url": "https://img.icons8.com/3d-fluency/94/t-shirt.png",
        "in_stock": True
    },
    {
        "id": "7",
        "name": "Cloud Computing Fundamentals",
        "category": "Books",
        "price": 49.99,
        "description": "Guide covering AWS, Azure, and GCP.",
        "image_url": "https://img.icons8.com/3d-fluency/94/book.png",
        "in_stock": True
    },
    {
        "id": "8",
        "name": "Python for DevOps",
        "category": "Books",
        "price": 44.99,
        "description": "Learn automation and DevOps with Python.",
        "image_url": "https://img.icons8.com/3d-fluency/94/literature.png",
        "in_stock": True
    },
    {
        "id": "9",
        "name": "Portable SSD 1TB",
        "category": "Electronics",
        "price": 109.99,
        "description": "High-speed portable SSD.",
        "image_url": "https://img.icons8.com/3d-fluency/94/ssd.png",
        "in_stock": True
    },
    {
        "id": "10",
        "name": "Networking & Security Handbook",
        "category": "Books",
        "price": 59.99,
        "description": "Reference for networking and cybersecurity.",
        "image_url": "https://img.icons8.com/3d-fluency/94/security-checked.png",
        "in_stock": True
    }
]


def seed_products():
    """Insert sample products into Cosmos DB."""

    if not COSMOS_ENDPOINT or not COSMOS_KEY:
        print("ERROR: Set COSMOS_ENDPOINT and COSMOS_KEY environment variables first.")
        sys.exit(1)

    try:
        # Connect to Cosmos DB
        client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
        database = client.get_database_client(DATABASE_NAME)
        container = database.get_container_client("products")

        print(f"Connected to database: {DATABASE_NAME}")
        print("Seeding products...\n")

        success_count = 0

        for product in PRODUCTS:
            try:
                container.upsert_item(body=product)
                print(f"✓ {product['name']} (${product['price']})")
                success_count += 1
            except Exception as e:
                print(f"✗ Error inserting {product['name']}: {e}")

        print("\n-----------------------------------")
        print(f"Done! Seeded {success_count}/{len(PRODUCTS)} products.")
        print(f"Categories: {len(set(p['category'] for p in PRODUCTS))}")

    except Exception as e:
        print(f"Connection error: {e}")


if __name__ == "__main__":
    seed_products()