from django.shortcuts import render,HttpResponse,redirect
from app01.models import TServer,TService
from common.mymako import render_mako_context

# Create your views here.


def index(request):
    server_obj = TServer.objects.filter(server__contains="mfwlog",)
    return render(request,'index.html',locals())


def delete_tserver(request,node,server,division=None):
    if division == 'None':
        division=''
        TServer.objects.filter(node=node,server=server,division=division).delete()
    else:
        TServer.objects.filter(node=node, server=server, division=division).delete()
    return redirect('/app01/index/')


def create_tserver(request):
        if request.method == "GET":
            return render(request,'create_tserver.html',locals())
        else:
            app=request.POST.get("app")
            server=request.POST.get("server")
            division=request.POST.get("division")
            node=request.POST.get("node")
            status=request.POST.get("status")
            use_agent=request.POST.get("use_agent")

            if server == '' or node == '':
                return HttpResponse('Please enter the parameters')
            else:
                TServer.objects.create(app=app,server=server,division=division,node=node,status=status,use_agent=use_agent)
                return redirect('/app01/index/')


def change_tserver(request,old_app,old_server,old_division,old_node,old_status,old_use_agent):

    if old_division == 'None':
        old_division=''
        mfw_server_obj = TServer.objects.filter(node=old_node,server=old_server,division=old_division)
    else:
        mfw_server_obj = TServer.objects.filter(node=old_node, server=old_server, division=old_division)

    if request.method == "POST":
        new_app = request.POST.get("app")
        new_server = request.POST.get("server")
        new_division = request.POST.get("division")
        new_node = request.POST.get("node")
        new_status = request.POST.get("status")
        new_use_agent = request.POST.get("use_agent")

        TServer.objects.filter(app=old_app,server=old_server,division=old_division,node=old_node,status=old_status,use_agent=old_use_agent).update(app=new_app,server=new_server,division=new_division,node=new_node,status=new_status,use_agent=new_use_agent)
        return redirect('/app01/index/')
    return render(request,'change_tserver.html',locals())


def select_tserver(request):
    if request.method == "POST":
        node = request.POST.get("node")
        server = request.POST.get("server")
        division = request.POST.get("division")
        if node == "" and server == "" and division== "":
            return redirect('/app01/index/')
        else:
            server_obj = TServer.objects.filter(node__contains=node,server__contains=server,division__contains=division)

    return render(request,'index.html',locals())

