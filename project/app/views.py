from django.shortcuts import render,redirect
from app.forms import pictureform
from app.models import picture,like,kind
from django.contrib.auth.models import User
from django.db.models import Count
import pandas as pd
import plotly.express as px

# Create your views here.

def upload(request):
    topics = kind.objects.all()
    print("-----------")
    for tops in topics: 
        print(tops.name)   
    print("-----------")
    context = {'form':pictureform}
    if request.method == 'POST':
        form = pictureform(request.POST,request.FILES)
        if form.is_valid:
            item_kind = kind.objects.get(id = request.POST['kind'])
            item_kind.numbers = item_kind.numbers +1
            item_kind.save()
            form.save()
            
            return render(request,'app/upload.html',context)
    return render(request,'app/upload.html',context)

def home(request):

    pictures = picture.objects.all()
    context = {'pictures':pictures,}
    return render(request,'app/home.html',context)

def delete(request,pk):
    image = picture.objects.get(id=pk)
    print(image.kind)
    item_kind = kind.objects.get(name = image.kind.name)
    item_kind.numbers = item_kind.numbers - 1
    item_kind.save()
    image.delete()
    return redirect('/')

def like_pic(request,pk):
    user=request.user
    image = picture.objects.get(id=pk)
    liked = like.objects.filter(picture=image,user=user)
    

    if not liked:
        like.objects.create(picture=image,user=user,kind=image.kind)
        image.likes = image.likes + 1
        image.save()
        
    else:
        liked = like.objects.filter(picture = image,user=user,kind=image.kind)
        liked.delete()
        image.likes = image.likes - 1
        image.save()
    return redirect("/")

def profile(request,pk):
    user = User.objects.get(id=pk)
    uploads = user.picture_set.all()
    likes = like.objects.select_related('picture').filter(user=user)
    kinds = like.objects.filter(user=user).select_related('kind').values('kind').annotate(count=Count('kind'))
    print(kinds)
    print(pd.DataFrame(kinds))
    summery = pd.DataFrame(kinds)
    fig = px.pie(names=summery.kind,values=summery['count'] ,hole=0.3,width=400,color_discrete_sequence=px.colors.sequential.RdBu)
    fig.update_layout({
    'plot_bgcolor': 'rgba(10,0,0,0)',
    'paper_bgcolor': 'rgba(0,10,10,0)'})
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    
    context={'uploads':uploads,'user':user,'likes':likes,'kinds':kinds,'fig':fig.to_html}
    return render(request,'app/profile.html',context)



def show(request,pk):
        image = picture.objects.get(id=pk)
        context = {'image':image}
        return render(request,'app/show.html',context)
    
    
    
def loginpage(request):
    return render(request,'app/log_reg.html')