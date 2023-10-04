from faststream import FastStream
from faststream.kafka import KafkaBroker
from pydantic import BaseModel, Field, PositiveInt

broker = KafkaBroker("localhost:9092")
app = FastStream(broker)


class User(BaseModel):
    user: str = Field(..., examples=["John"])
    user_id: PositiveInt = Field(..., examples=["1"])


@broker.subscriber("in-topic")
@broker.publisher("out-topic")
async def handle_msg(data: User) -> str:
    return f"User: {data.user} - {data.user_id} registered"
