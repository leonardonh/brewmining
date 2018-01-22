from django.http import HttpResponse
from .models import Batelada

def index(request):
	latest_question_list = Batelada.objects.order_by('-pub_date')[:5]
	output = ', '.join([q.batelada for q in latest_question_list])
	return HttpResponse(output)

def detail(request, question_id):
	return HttpResponse("You are looking at question %s." % question_id)
	
def results(request, question_id):
	return HttpResponse("You are looking at teh results of question %s." % question_id)

def vote(request, question_id):
	return HttpResponse("You are voting on question %s." % question_id)