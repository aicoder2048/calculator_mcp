from pydantic import BaseModel, Field, field_validator
from typing import Optional, List, Literal
from datetime import datetime


class AddInput(BaseModel):
    a: float = Field(..., description="First operand")
    b: float = Field(..., description="Second operand")


class SubtractInput(BaseModel):
    a: float = Field(..., description="First operand")
    b: float = Field(..., description="Second operand")


class MultiplyInput(BaseModel):
    a: float = Field(..., description="First operand")
    b: float = Field(..., description="Second operand")


class DivideInput(BaseModel):
    a: float = Field(..., description="First operand")
    b: float = Field(..., description="Second operand")


class PowerInput(BaseModel):
    base: float = Field(..., description="Base number")
    exponent: float = Field(..., description="Power to raise to")


class RootInput(BaseModel):
    number: float = Field(..., description="Number to find root of")
    degree: float = Field(2.0, gt=0, description="Degree of root (default: 2 for square root)")


class ModInput(BaseModel):
    a: int = Field(..., description="Dividend (被除数)")
    b: int = Field(..., description="Divisor (除数, cannot be zero)")
    
    @field_validator("b")
    @classmethod
    def validate_divisor(cls, v):
        if v == 0:
            raise ValueError("Divisor cannot be zero")
        return v


class FactorialInput(BaseModel):
    n: int = Field(..., ge=0, le=20, description="Number to calculate factorial (0-20)")


class StatisticsInput(BaseModel):
    data: List[float] = Field(..., min_length=1, description="Data points for statistical calculation")


class CalculationRecord(BaseModel):
    """Model for storing calculation history."""
    id: str
    operation: str
    inputs: dict
    result: float
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    error: Optional[str] = None


class BatchCalculationInput(BaseModel):
    numbers: List[float] = Field(..., min_length=2, description="List of numbers to operate on")
    operation: Literal["sum", "product"] = Field(..., description="Batch operation type")


class EquationInput(BaseModel):
    """Model for equation solving."""
    equation_type: Literal["linear", "quadratic", "polynomial"]
    coefficients: List[float] = Field(..., description="Equation coefficients")

    @field_validator("coefficients")
    @classmethod
    def validate_coefficients(cls, v, info):
        equation_type = info.data.get("equation_type")
        if equation_type == "linear" and len(v) != 2:
            raise ValueError("Linear equation requires exactly 2 coefficients")
        elif equation_type == "quadratic" and len(v) != 3:
            raise ValueError("Quadratic equation requires exactly 3 coefficients")
        return v