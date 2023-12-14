from pydantic import BaseModel


class CaloricBreakdown(BaseModel):
    fat: float
    oil: float
    protein: float
    carbohydrates: float


class FoodItem(BaseModel):
    name: str
    caloric_breakdown: CaloricBreakdown


class FoodData(BaseModel):
    land_animal: list[FoodItem]
    ocean_animal: list[FoodItem]
    fruits: list[FoodItem]
    vegetables: list[FoodItem]