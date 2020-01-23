from django.shortcuts import get_object_or_404
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from .models import accounts
from .serializers import accountSerializer,bioSerializer
import hashlib
from django.utils.encoding import smart_str
# Create your views here.
@csrf_exempt
def ping(request):
    return JsonResponse({'status': "OK"},status=200)
def get_hexdigest(algorithm, salt, raw_password):
    """
    Returns a string of the hexdigest of the given plaintext password and salt
    using the given algorithm ('md5', 'sha1' or 'crypt').
    """
    raw_password, salt = smart_str(raw_password), smart_str(salt)
    if algorithm == 'crypt':
        try:
            import crypt
        except ImportError:
            raise ValueError('"crypt" password algorithm not supported in this environment')
        return crypt.crypt(raw_password, salt)

    if algorithm == 'md5':
        return hashlib.md5((salt + raw_password).encode('utf-8')).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1((salt + raw_password).encode('utf-8')).hexdigest()
    raise ValueError("Got unknown password algorithm type in password.")
@csrf_exempt
def accounts_list(request):
    if request.method=='GET':
        acc=accounts.objects.all()
        serializers=accountSerializer(acc,many=True)
        return JsonResponse(serializers.data,safe=False)
    elif request.method=='POST':
        data=JSONParser().parse(request)
        if len(data['password'])>=8:
            if accounts.objects.filter(username=data['username']).exists():
                return JsonResponse({'message': "Username already exist!"},status=400)
            else:
                import random
                algo = 'sha1'
                salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
                hsh = get_hexdigest(algo, salt, data['password'])
                data['salt']=salt
                data['password'] = '%s$%s$%s' % (algo, salt, hsh)
                serializers=accountSerializer(data=data)
                if serializers.is_valid():
                    serializers.save()
                    return JsonResponse({'message': "Registered Successfully!"},status=201)
                return JsonResponse(serializers.errors,status=400)
        else:
            return JsonResponse({'message': "Password must be of atleast 8 characters!"},status=400)

@csrf_exempt
def accounts_details(request):
    import random
    if request.method=='POST':
        data=JSONParser().parse(request)
        try:
            acc=accounts.objects.get(username=data['username'])
        except accounts.DoesNotExist:
            return HttpResponse({'message': "Account does not exist"},status=404)
        algo = 'sha1'
        salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
        hsh = get_hexdigest(algo, acc.salt, data['password'])
        hash_pass= '%s$%s$%s' % (algo, acc.salt, hsh)
        if hash_pass==acc.password:
            bio={'Name':acc.Name ,'Email':acc.Email ,'Phone':'+'+str(acc.Phone.country_code)+str(acc.Phone.national_number)}
            serializers=bioSerializer(data=bio)
            if serializers.is_valid():
                return JsonResponse(serializers.data,status=200)
            return JsonResponse(serializers.errors,status=400)
        else:
            return JsonResponse({'message':'Incorrect Password'},status=403)
            

        