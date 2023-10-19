"""BeYourSelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconflistadosInvDeportes
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Modulos.Academico.views import *
from Modulos.Principal.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('follow/<str:username>/', follow, name='follow'),
    path('unfollow/<str:username>/', unfollow, name='unfollow'),
    path('profile/', profile, name='profile'),
    path('profile/<str:username>/', profile, name='profile'),
    path('ViewFollow/', ViewFollow, name='ViewFollow'),
    path('ViewFollow/<str:username>/', ViewFollow, name='ViewFollow'),
    path('PostsPedidos/', PostsPedidos, name='PostsPedidos'),
    path('PostsPedidos/<str:username>/', PostsPedidos, name='PostsPedidos'),

    path('Login/', LoginView.as_view(template_name='loginMe.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='Presentacion'), name='logout'),
    path('Registro/', registrar_usuario, name="registrar_usuario"),
    path('Añadir_Datos/<codigo>/', AñadirDatos, name='AñadirDatos'),
    path('EditImagenPersonales/<codigo>/', EditImagenPersonales, name='EditImagenPersonales'),
    path('EditDatosPersonales/<str:username>/', EditDatosPersonales, name='EditDatosPersonales'),
    path('EditUsuario/<str:username>/', EditUsuario, name='EditUsuario'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    path('Home/Inventarios/InventarioMusica/', listadosInvMusica, name="InventarioMusica"),
    path('Home/AreaPersonal/PostMusicas/', PostMusicass, name='PostMusicass'),
    path('Home/AreaPersonal/PostMusicas/NewPostMusi', CrearPostMusi, name='NewPostMusi'),
    path('Home/AreaPersonal/PostMusicas/modificar_PostMusi/<codigo>/', modificar_PostMusi, name='modificar_PostMusi'),
    path('Home/AreaPersonal/PostMusicas/modificar_PostMusi2/<codigo>/', modificar_PostMusi2, name='modificar_PostMusi2'),
    path('Home/AreaPersonal/PostMusicas/eliminar_PostMusi/<codigo>/', eliminar_PostMusi, name='eliminar_PostMusi'),
    path('Home/AreaPersonal/PostMusicas/eliminar_PostMusi2/<codigo>/', eliminar_PostMusi2, name='eliminar_PostMusi2'),
    path('Home/Inventarios/InventarioMusica/Pedir-Musica/', Pedir_invMusica, name="Pedir_invMusica"),
    path('Home/Perfil/VerPMusica/', VerPMusica, name="VerPMusica"),
    path('Home/Perfil/VerPMusica/eliminar_PedidoMusi/<codigo>/', eliminar_PedidoMusi, name="eliminar_PedidoMusi"),
    path('Home/Perfil/VerPMusica/eliminar_PedidoMusi2/<codigo>/', eliminar_PedidoMusi2, name="eliminar_PedidoMusi2"),
    path('Home/Inventarios/InventarioMusica/AgregarMusica', AgregarInvMusica, name="AgregarInvMusica"),
    path('Home/Inventarios/InventarioMusica/ModificarMusica/<codigo>/', modificar_InvMusica, name="Modificar_InvMusica"),
    path('Home/Inventarios/InventarioMusica/EliminarMusica/<codigo>/', eliminar_InvMusica, name="eliminar_InvMusica"),
    path('Home/Inventarios/InventarioMusica/InvMusica_reportepdf', InvMusica_reportepdf, name='InvMusica_reportepdf'),

    path('Home/Inventarios/InventarioPintura/', listadosInvPintura, name="InventarioPintura"),
    path('Home/AreaPersonal/PostPintura/', PostPinturass, name='PostPinturass'),
    path('Home/AreaPersonal/PostPintura/NewPostPint', CrearPostPint, name='NewPostPint'),
    path('Home/AreaPersonal/PostPintura/modificar_PostPint/<codigo>/', modificar_PostPint, name='modificar_PostPint'),
    path('Home/AreaPersonal/PostPintura/modificar_PostPint2/<codigo>/', modificar_PostPint2, name='modificar_PostPint2'),
    path('Home/AreaPersonal/PostPintura/eliminar_PostPint/<codigo>/', eliminar_PostPint, name='eliminar_PostPint'),
    path('Home/AreaPersonal/PostPintura/eliminar_PostPint2/<codigo>/', eliminar_PostPint2, name='eliminar_PostPint2'),
    path('Home/Inventarios/InventarioPintura/Pedir-Pintura/', Pedir_invPintura, name="Pedir_invPintura"),
    path('Home/Perfil/VerPPintura/', VerPPintura, name="VerPPintura"),
    path('Home/Perfil/VerPPintura/eliminar_PedidoPint/<codigo>/', eliminar_PedidoPint, name="eliminar_PedidoPint"),
    path('Home/Perfil/VerPPintura/eliminar_PedidoPint2/<codigo>/', eliminar_PedidoPint2, name="eliminar_PedidoPint2"),
    path('Home/Inventarios/InventarioPintura/AgregarPint', AgregarInvPintura, name="AgregarInvPintura"),
    path('Home/Inventarios/InventarioPintura/ModificarPint/<codigo>/', modificar_InvPintura, name="modificar_InvPintura"),
    path('Home/Inventarios/InventarioPintura/EliminarPint/<codigo>/', eliminar_InvPintura, name="eliminar_InvPintura"),
    path('Home/Inventarios/InventarioPintura/Inv_Pintura_reportepdf', Inv_Pintura_reportepdf, name='Inv_Pintura_reportepdf'),

    path('Home/Inventarios/InventarioTA/', listadosInvTA, name="InventarioTA"),
    path('Home/AreaPersonal/PostTA/', PostTAss, name='PostTAss'),
    path('Home/AreaPersonal/PostTA/NewPostTA', CrearPostTA, name='NewPostTA'),
    path('Home/AreaPersonal/PostTA/modificar_PostTA/<codigo>/', modificar_PostTA, name='modificar_PostTA'),
    path('Home/AreaPersonal/PostTA/modificar_PostTA2/<codigo>/', modificar_PostTA2, name='modificar_PostTA2'),
    path('Home/AreaPersonal/PostTA/eliminar_PostTA/<codigo>/', eliminar_PostTA, name='eliminar_PostTA'),
    path('Home/AreaPersonal/PostTA/eliminar_PostTA2/<codigo>/', eliminar_PostTA2, name='eliminar_PostTA2'),
    path('Home/Inventarios/InventarioTA/Pedir-ExpresiónCorporal/', Pedir_InvTA, name="Pedir_InvTA"),
    path('Home/Perfil/VerPTA/', VerPTA, name="VerPTA"),
    path('Home/Perfil/VerPTA/eliminar_PedidoTA/<codigo>/', eliminar_PedidoTA, name="eliminar_PedidoTA"),
    path('Home/Perfil/VerPTA/eliminar_PedidoTA2/<codigo>/', eliminar_PedidoTA2, name="eliminar_PedidoTA2"),
    path('Home/Inventarios/InventarioTA/AgregarTA', AgregarInvTA, name="AgregarInvTA"),
    path('Home/Inventarios/InventarioTA/ModificarTA/<codigo>/', modificar_InvTA, name="modificar_InvTA"),
    path('Home/Inventarios/InventarioTA/EliminarTA/<codigo>/', eliminar_InvTA, name="eliminar_InvTA"),
    path('Home/Inventarios/InventarioTA/Inv_TA_reportepdf', Inv_TA_reportepdf, name='Inv_TA_reportepdf'),

    path('Home/Inventarios/InventarioDeportes/', listadosInvDeportes, name="InventarioDeportes"),
    path('Home/AreaPersonal/PostDeportes/', PostDeportess, name='PostDeportess'),
    path('Home/AreaPersonal/PostDeportes/NewPostDepo', CrearPostDepo, name='NewPostDepo'),
    path('Home/AreaPersonal/PostDeportes/modificar_PostDeportess/<codigo>/', modificar_PostDeportess, name='modificar_PostDeportess'),
    path('Home/AreaPersonal/PostDeportes/modificar_PostDeportess2/<codigo>/', modificar_PostDeportess2, name='modificar_PostDeportess2'),
    path('Home/AreaPersonal/PostDeportes/eliminar_PostDeportess/<codigo>/', eliminar_PostDeportess, name='eliminar_PostDeportess'),
    path('Home/AreaPersonal/PostDeportes/eliminar_PostDeportess2/<codigo>/', eliminar_PostDeportess2, name='eliminar_PostDeportess2'),
    path('Home/Inventarios/InventarioDeportes/Pedir-Deportes/', Pedir_InvDeportes, name="Pedir_InvDeportes"),
    path('Home/Perfil/VerPDeportes/', VerPDeportes, name="VerPDeportes"),
    path('Home/Perfil/VerPDeportes/eliminar_PedidoDepo/<codigo>/', eliminar_PedidoDepo, name="eliminar_PedidoDepo"),
    path('Home/Perfil/VerPDeportes/eliminar_PedidoDepo2/<codigo>/', eliminar_PedidoDepo2, name="eliminar_PedidoDepo2"),
    path('Home/Inventarios/InventarioDeportes/AgregarDeportes', AgregarInvDepo, name="AgregarInvDepo"),
    path('Home/Inventarios/InventarioDeportes/ModificarDeportes/<codigo>/', modificar_InvDepo, name="modificar_InvDepo"),
    path('Home/Inventarios/InventarioDeportes/EliminarDeportes/<codigo>/', eliminar_InvDepo, name="eliminar_InvDepo"),
    path('Home/Inventarios/InventarioDeportes/Inv_Deportes_reportepdf', Inv_Deportes_reportepdf, name='Inv_Deportes_reportepdf'),

    path('Home/Inventarios/InventarioDanzas/', listadosInvDanzas, name="InventarioDanzas"),
    path('Home/AreaPersonal/PostDanzas/', PostDanzass, name='PostDanzass'),
    path('Home/AreaPersonal/PostDanzas/NewPostDanza', CrearPostDanza, name='NewPostDanza'),
    path('Home/AreaPersonal/PostDanzas/modificar_PostDanzass/<codigo>/', modificar_PostDanzass, name='modificar_PostDanzass'),
    path('Home/AreaPersonal/PostDanzas/modificar_PostDanzass2/<codigo>/', modificar_PostDanzass2, name='modificar_PostDanzass2'),
    path('Home/AreaPersonal/PostDanzas/eliminar_PostDanzass/<codigo>/', eliminar_PostDanzass, name='eliminar_PostDanzass'),
    path('Home/AreaPersonal/PostDanzas/eliminar_PostDanzass2/<codigo>/', eliminar_PostDanzass2, name='eliminar_PostDanzass2'),
    path('Home/Inventarios/InventarioDeportes/Pedir-Danzas/', Pedir_InvDanzas, name="Pedir_InvDanzas"),
    path('Home/Perfil/VerPDanzas/', VerPDanzas, name="VerPDanzas"),
    path('Home/Perfil/VerPDanzas/eliminar_PedidoDanza/<codigo>/', eliminar_PedidoDanza, name="eliminar_PedidoDanza"),
    path('Home/Perfil/VerPDanzas/eliminar_PedidoDanza2/<codigo>/', eliminar_PedidoDanza2, name="eliminar_PedidoDanza2"),
    path('Home/Inventarios/InventarioDanzas/AgregarDanzas', AgregarInvDanza, name="AgregarInvDanza"),
    path('Home/Inventarios/InventarioDanzas/ModificarDanzas/<codigo>/', modificar_InvDanza, name="modificar_InvDanza"),
    path('Home/Inventarios/InventarioDanzas/EliminarDanzas/<codigo>/', eliminar_InvDanza, name="eliminar_InvDanza"),
    path('Home/Inventarios/InventarioDanzas/Inv_Danzas_reportepdf', Inv_Danzas_reportepdf, name='Inv_Danzas_reportepdf'),

    path('Home/Inventarios/InventarioFoto/', listadosInvFoto, name="InventarioFotografia"),
    path('Home/AreaPersonal/PostFotografia/', PostFotografias, name='PostFotografia'),
    path('Home/AreaPersonal/PostFotografia/NewPostFoto', CrearPostFoto, name='NewPostFoto'),
    path('Home/AreaPersonal/PostFotografia/modificar_PostFoto/<codigo>/', modificar_PostFoto, name='modificar_PostFoto'),
    path('Home/AreaPersonal/PostFotografia/modificar_PostFoto2/<codigo>/', modificar_PostFoto2, name='modificar_PostFoto2'),
    path('Home/AreaPersonal/PostFotografia/eliminar_PostFoto/<codigo>/', eliminar_PostFoto, name='eliminar_PostFoto'),
    path('Home/AreaPersonal/PostFotografia/eliminar_PostFoto2/<codigo>/', eliminar_PostFoto2, name='eliminar_PostFoto2'),
    path('Home/Inventarios/InventarioFotografia/Pedir-Fotografia/', Pedir_InvFoto, name="Pedir_InvFoto"),
    path('Home/Perfil/VerPFoto/', VerPFoto, name="VerPFoto"),
    path('Home/Perfil/VerPFoto/eliminar_PedidoFoto/<codigo>/', eliminar_PedidoFoto, name="eliminar_PedidoFoto"),
    path('Home/Perfil/VerPFoto/eliminar_PedidoFoto2/<codigo>/', eliminar_PedidoFoto2, name="eliminar_PedidoFoto2"),
    path('Home/Inventarios/InventarioFotografia/AgregarFoto', AgregarInvFoto, name="AgregarInvFoto"),
    path('Home/Inventarios/InventarioFotografia/ModificarFoto/<codigo>/', modificar_InvFoto, name="modificar_InvFoto"),
    path('Home/Inventarios/InventarioFotografia/EliminarFoto/<codigo>/', eliminar_InvFoto, name="eliminar_InvFoto"),
    path('Home/Inventarios/InventarioFotografia/Inv_Foto_reportepdf', Inv_Foto_reportepdf, name='Inv_Foto_reportepdf'),

    path('', Presentacion, name='Presentacion'),
    path('contactar/', contactar, name='contactar'),
    path('Home/', IndexView, name="IndexView"),
    path('Home/AreaPersonal/', Area_Personal, name="AreaPersonal"),
    path('Home/Inventarios/', Inventarios, name="Inventarios"),

    path('Home/Posts/', Postss, name='Post'),
    path('Home/Posts/CrearPosts/', CrearPost, name='CrearPost'),
    path('Home/Posts/CrearPosts/modificar_Post/<codigo>/', modificar_Post, name='modificar_Post'),
    path('Home/Posts/CrearPosts/eliminar_Post/<codigo>/', eliminar_Post, name='eliminar_Post'),

    path('Home/calendario/', CalendarView.as_view(), name='calendar'),
    path('event/new/', create_event, name='event_new'),
    path('event/edit/<int:pk>/', EventEdit.as_view(), name='event_edit'),
    path('event/<int:pk>/remove', eliminar_evento.as_view(), name="remove_event"),
    path('event/<int:event_id>/details/', event_details, name='event-detail'),
    
    

]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)