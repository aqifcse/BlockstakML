from rest_framework.views import APIView
from rest_framework.response import Response
import json

from .ml_functions import gaussianNaiveBayes, decisionTree



class MLModelOutputAPIView(APIView):
    def get(self, request):
        query = request.GET.get('query')

        if query == 'nb':
            model_output = gaussianNaiveBayes()
        
        if query == 'dt':
            model_output = decisionTree()

        if query == 'both':
            model_output = {
                "gaussian_naive_bayes_output": gaussianNaiveBayes(),
                "decision_tree_output": decisionTree()
            }

        return Response(model_output)