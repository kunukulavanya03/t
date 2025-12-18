from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db, engine

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Backend_Api_For_T API",
    description="Generated from Impact Analysis specifications",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "API is running",
        "endpoints": 20,
        "models": 7
    }

@app.get("/health")
def health():
    return {"status": "healthy", "service": "backend_api_for_t"}

# Generated API endpoints
@app.get("/users")
def users(db: Session = Depends(get_db)):
    # Get all items
    items = db.query(models.Users).all()
    return {"items": items, "total": len(items)}

@app.post("/users")
def users(item_data: schemas.UsersCreate, db: Session = Depends(get_db)):
    # Create new item
    new_item = models.Users(**item_data.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@app.get("/users/{id}")
def users_id(id: int, db: Session = Depends(get_db)):
    # Get single item by ID
    item = db.query(models.Users).filter(models.Users.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/users/{id}")
def users_id(id: int, item_data: schemas.UsersCreate, db: Session = Depends(get_db)):
    # Update item
    item = db.query(models.Users).filter(models.Users.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    for key, value in item_data.dict().items():
        setattr(item, key, value)
    
    db.commit()
    db.refresh(item)
    return item

@app.delete("/users/{id}")
def users_id(id: int, db: Session = Depends(get_db)):
    # Delete item
    item = db.query(models.Users).filter(models.Users.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}

@app.get("/products")
def products(db: Session = Depends(get_db)):
    # Get all items
    items = db.query(models.Users).all()
    return {"items": items, "total": len(items)}

@app.post("/products")
def products(item_data: schemas.UsersCreate, db: Session = Depends(get_db)):
    # Create new item
    new_item = models.Users(**item_data.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@app.get("/products/{id}")
def products_id(id: int, db: Session = Depends(get_db)):
    # Get single item by ID
    item = db.query(models.Users).filter(models.Users.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/products/{id}")
def products_id(id: int, item_data: schemas.UsersCreate, db: Session = Depends(get_db)):
    # Update item
    item = db.query(models.Users).filter(models.Users.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    for key, value in item_data.dict().items():
        setattr(item, key, value)
    
    db.commit()
    db.refresh(item)
    return item

@app.delete("/products/{id}")
def products_id(id: int, db: Session = Depends(get_db)):
    # Delete item
    item = db.query(models.Users).filter(models.Users.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}

@app.get("/orders")
def orders(db: Session = Depends(get_db)):
    # Get all items
    items = db.query(models.Users).all()
    return {"items": items, "total": len(items)}

@app.post("/orders")
def orders(item_data: schemas.UsersCreate, db: Session = Depends(get_db)):
    # Create new item
    new_item = models.Users(**item_data.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@app.get("/orders/{id}")
def orders_id(id: int, db: Session = Depends(get_db)):
    # Get single item by ID
    item = db.query(models.Users).filter(models.Users.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/orders/{id}")
def orders_id(id: int, item_data: schemas.UsersCreate, db: Session = Depends(get_db)):
    # Update item
    item = db.query(models.Users).filter(models.Users.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    for key, value in item_data.dict().items():
        setattr(item, key, value)
    
    db.commit()
    db.refresh(item)
    return item

@app.delete("/orders/{id}")
def orders_id(id: int, db: Session = Depends(get_db)):
    # Delete item
    item = db.query(models.Users).filter(models.Users.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}

@app.get("/payments")
def payments(db: Session = Depends(get_db)):
    # Get all items
    items = db.query(models.Users).all()
    return {"items": items, "total": len(items)}

@app.post("/payments")
def payments(item_data: schemas.UsersCreate, db: Session = Depends(get_db)):
    # Create new item
    new_item = models.Users(**item_data.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@app.get("/payments/{id}")
def payments_id(id: int, db: Session = Depends(get_db)):
    # Get single item by ID
    item = db.query(models.Users).filter(models.Users.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/payments/{id}")
def payments_id(id: int, item_data: schemas.UsersCreate, db: Session = Depends(get_db)):
    # Update item
    item = db.query(models.Users).filter(models.Users.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    for key, value in item_data.dict().items():
        setattr(item, key, value)
    
    db.commit()
    db.refresh(item)
    return item

@app.delete("/payments/{id}")
def payments_id(id: int, db: Session = Depends(get_db)):
    # Delete item
    item = db.query(models.Users).filter(models.Users.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
