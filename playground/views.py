from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q,F,Value,Func,ExpressionWrapper,DecimalField
from django.db.models.aggregates import Count,Max,Min,Avg,Sum
from store.models import Product,Order,OrderItem,Customer,Collection
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem,TaggedItemManager


def say_hello(request):
    collection = Collection(pk=11)
    collection.featured_product = None
    collection.save()
    collection.id

    
    return render(request, 'hello.html', {'name': 'Aryan','result':list(queryset)})
