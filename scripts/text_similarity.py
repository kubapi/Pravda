from semantic_text_similarity.models import WebBertSimilarity
from semantic_text_similarity.models import ClinicalBertSimilarity

web_model = WebBertSimilarity(device='cpu', batch_size=10) #defaults to GPU prediction

clinical_model = ClinicalBertSimilarity(device='cuda', batch_size=10) #defaults to GPU prediction

web_model.predict([("She won an olympic gold medal","The women is an olympic champion")])
