class Settings:
    MONGO_URI: str
    DB_NAME: str

    class Config:
        env_file = ".env"


settings = Settings()
