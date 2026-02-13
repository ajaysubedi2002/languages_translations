from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "API"
    
    #Models    
    Translate_model : str
       
    # Ollama configuration
    OLLAMA_API_URL: str 
    
    # Model paths
    model_path_nllb: str    
    model_path_facebook: str
     
   
    class Config:
        env_file = "env/.env"
        extra = "ignore"  # Allow extra fields from .env without errors

# Instantiate the settings
settings = Settings()

