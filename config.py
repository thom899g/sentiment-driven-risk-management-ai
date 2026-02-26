"""
Configuration module for Sentiment-Driven Risk Management AI
Centralized configuration with environment variable fallbacks
"""
import os
from dataclasses import dataclass
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

@dataclass
class FirebaseConfig:
    """Firebase configuration"""
    credential_path: str = os.getenv("FIREBASE_CREDENTIAL_PATH", "./credentials/firebase-service-account.json")
    project_id: str = os.getenv("FIREBASE_PROJECT_ID", "sentiment-risk-management")
    database_url: str = os.getenv("FIREBASE_DATABASE_URL", "")
    collection_name: str = os.getenv("FIREBASE_COLLECTION", "risk_parameters")

@dataclass
class APIConfig:
    """API configurations"""
    newsapi_key: Optional[str] = os.getenv("NEWSAPI_KEY")
    twitter_bearer_token: Optional[str] = os.getenv("TWITTER_BEARER_TOKEN")
    twitter_api_key: Optional[str] = os.getenv("TWITTER_API_KEY")
    twitter_api_secret: Optional[str] = os.getenv("TWITTER_API_SECRET")
    twitter_access_token: Optional[str] = os.getenv("TWITTER_ACCESS_TOKEN")
    twitter_access_secret: Optional[str] = os.getenv("TWITTER_ACCESS_SECRET")
    polygon_key: Optional[str] = os.getenv("POLYGON_API_KEY")
    
@dataclass
class TradingConfig:
    """Trading configuration"""
    exchange: str = os.getenv("TRADING_EXCHANGE", "binance")
    symbols: list = os.getenv("TRADING_SYMBOLS", "BTC/USDT,ETH/USDT").split(",")
    initial_risk_multiplier: float = float(os.getenv("INITIAL_RISK_MULTIPLIER", "1.0"))
    max_position_size: float = float(os.getenv("MAX_POSITION_SIZE", "10000.0"))
    min_position_size: float = float(os.getenv("MIN_POSITION_SIZE", "100.0"))
    update_interval_minutes: int = int(os.getenv("UPDATE_INTERVAL_MINUTES", "15"))

@dataclass
class SentimentConfig:
    """Sentiment analysis configuration"""
    vader_threshold_positive: float = 0.05
    vader_threshold_negative: float = -0.05
    min_confidence_score: float = 0.3
    max_text_length: int = 1000

@dataclass
class AppConfig:
    """Main application configuration"""
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    enable_trading: bool = os.getenv("ENABLE_TRADING", "False").lower() == "true"
    mock_mode: bool = os.getenv("MOCK_MODE", "True").lower() == "true"
    backup_file: str = os.getenv("BACKUP_FILE", "./backup/risk_params_backup.json")
    
    def __post_init__(self):
        """Validate configuration"""
        if not self.mock_mode and not self.enable_trading:
            print("WARNING: Both mock_mode and enable_trading are False - system will only analyze")
        
        # Create backup directory if it doesn't exist
        backup_dir = os.path.dirname