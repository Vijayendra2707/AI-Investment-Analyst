from pydantic import BaseModel, computed_field

class Company(BaseModel):

    input_name: str

    company_name: str

    ticker: str | None

    exchange: str

    currency: str | None = None

    country: str | None = None

    sector: str | None = None

    industry: str | None = None

    is_public: bool

    @computed_field
    @property
    def key(self) -> str:
        return self.ticker or self.input_name