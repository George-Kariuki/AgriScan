        ┌───────────────┐
        │   Flutter     │
        │  (Mobile App) │
        └───────┬───────┘
                │ HTTP (JSON)
                ▼
        ┌────────────────────┐
        │     FastAPI        │
        │ /predict endpoint  │
        └─────────┬──────────┘
                  │
                  ▼
         ┌────────────────┐
         │  ML Model (TFL)│
         │  Cassava/maize │
         └────────────────┘
