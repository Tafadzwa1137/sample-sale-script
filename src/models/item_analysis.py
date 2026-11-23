# src/models/item_analysis.py
from pydantic import BaseModel
from typing import Optional

class ItemAnalysis(BaseModel):
    category: Optional[str] = None
    primary_colours: list[str] = []
    style_tags: list[str] = []
    likely_materials: list[str] = []
    formality: Optional[str] = None
    price_band: Optional[str] = None
    confidence: float = 0.0
    missing_fields: list[str] = []
    analysis_notes: Optional[str] = None