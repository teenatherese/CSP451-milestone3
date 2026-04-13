from pydantic import BaseModel, Field
from typing import Optional, List

class Product(BaseModel):
    id: str
    name: str
    category: str
    price: float
    description: str
    image_url: Optional[str] = ""
    in_stock: bool = True

class CartItemRequest(BaseModel):
    product_id: str
    quantity: int = Field(default=1, ge=1, le=99)

class CartItem(BaseModel):
    id: str
    user_id: str
    product_id: str
    product_name: str
    price: float
    quantity: int
    subtotal: float

class OrderItem(BaseModel):
    product_id: str
    product_name: str
    price: float
    quantity: int
    subtotal: float

class Order(BaseModel):
    id: str
    user_id: str
    items: List[OrderItem]
    total: float
    status: str = "confirmed"
    created_at: str

class HealthResponse(BaseModel):
    status: str
    database: str
    cosmos_endpoint: str
    timestamp: str