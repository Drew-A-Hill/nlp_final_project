from pathlib import Path

SEED = 42
DATA_DIR = Path("data")
CATEGORIES = ["Electronics", "Home_and_Kitchen"]
TOP_N_TOTAL = 200
SAMPLE_SIZE = 20_000
SHUFFLE_BUFFER = 10_000
DATASET_URL = "hf://datasets/McAuley-Lab/Amazon-Reviews-2023/raw"
REVIEW_COLUMNS = ["rating", "title", "text", "asin", "parent_asin", "user_id", "timestamp", "helpful_vote", "verified_purchase"]

REVIEWS_PER_SUMMARY = 50
MAX_WORDS_PER_REVIEW = 200
MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"
SUMMARY_INSTRUCTIONS = "Summarize what customers say about this product in one short paragraph."
MAX_SUMMARY_LENGTH = 250
SUMMARIES_PATH = DATA_DIR / "base_summaries_qwen.parquet"
