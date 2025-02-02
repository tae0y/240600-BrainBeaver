import ollama
from common.system.constants import Constants
from engage.llmroute.ollamaclient import OllamaClient
from engage.llmroute.openaiclient import OpenAIClient

class LLMRouter:
    """
    요청과 예산을 고려하여 적절한 API 클라이언트 선택
    """

    def __init__(self):
        constants = Constants.get_instance()
        self.clients = {}

        # ollama model client spawn
        for m in ollama.list().models:
            model_name = m.model
            self.clients[model_name] = OllamaClient(
                model_name = model_name,
                options = {}
            )

        # openai api client spawn
        self.clients['gpt-4o-mini'] = OpenAIClient(
            model_name = 'gpt-4o-mini',
            options = {
                'api_key' : constants.openai_api_key,
                'context_length' : 128000,
                'embedding_length' : None,
                'cost_per_token' : 0.15/1000000
            }
        )
        self.clients['text-embedding-3-small'] = OpenAIClient(
            model_name = 'text-embedding-3-small',
            options = {
                'api_key' : constants.openai_api_key,
                'context_length' : 8191,
                'embedding_length' : 1536,
                'cost_per_token' : 0.02/1000000
            }
        )

    def get_client_by_modelname(self, model_name):
        """
        모델 이름에 해당하는 클라이언트 반환
        """
        return self.clients[model_name]

    def get_clients_all(self):
        """
        모든 클라이언트 반환
        """
        return self.clients