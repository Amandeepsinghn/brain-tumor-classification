from src.brain_tumor_classification.pipeline.stage_01_ingestion import data_ingestion_pipeline
from src.brain_tumor_classification.pipeline.stage_02_base_model import Model_pipeline
from src.brain_tumor_classification.pipeline.stage_03_model_training import training_pipeline
from src.brain_tumor_classification.pipeline.stage_04_evaluation import evaluation_pipeline
from src.brain_tumor_classification.pipeline.prediction import cancer_classification