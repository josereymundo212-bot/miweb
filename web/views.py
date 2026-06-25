from django.shortcuts import render

def home(request):
    mensaje = ""

    if request.method == "POST":
        accion = request.POST.get("accion")
        nombre = request.POST.get("nombre")

        if accion == "saludar" and nombre:
            mensaje = f"Hola, {nombre}"

        elif accion == "limpiar":
            mensaje = ""

    return render(request, "web/home.html", {"mensaje": mensaje})