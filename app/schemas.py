from pydantic import BaseModel

class NecessityPrice(BaseModel):
    類別: str
    編號: int
    產品名稱: str
    規格: str
    統計值: str
    時間起點: str
    時間終點: str
