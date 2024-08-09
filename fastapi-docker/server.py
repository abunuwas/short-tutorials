import os


from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from starlette import status


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


class OrderModel(Base):
    __tablename__ = "order"

    product: Mapped[str]
    quantity: Mapped[int]


engine = create_engine(os.getenv("db_uri", "sqlite:///orders.db"))
Base.metadata.create_all(engine)
session_maker = sessionmaker(bind=engine)


fixture_orders = [
    {
        "product": "Cloak of invisibility",
        "quantity": 1,
    },
    {
        "product": "Deluminator",
        "quantity": 1,
    },
]

with session_maker() as session:
    if not list(session.scalars(select(OrderModel))):
        orders = [OrderModel(**order_details) for order_details in fixture_orders]
        session.add_all(orders)
        session.commit()


server = FastAPI()


class PlaceOrderSchema(BaseModel):
    product: str
    quantity: int


class GetOrderSchema(PlaceOrderSchema):
    id: int


class ListOrdersSchema(BaseModel):
    orders: list[GetOrderSchema]


@server.get("/orders", response_model=ListOrdersSchema)
def list_orders():
    with session_maker() as session:
        orders = session.scalars(select(OrderModel))
        return {"orders": list(orders)}


@server.post(
    "/orders", response_model=GetOrderSchema, status_code=status.HTTP_201_CREATED
)
def place_order(order_details: PlaceOrderSchema):
    with session_maker() as session:
        order = OrderModel(**order_details.dict())
        session.add(order)
        session.commit()
        return {
            "id": order.id,
            "product": order.product,
            "quantity": order.quantity,
        }
