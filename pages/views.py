from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Page
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PageForm

class PageListView(ListView):
    model = Page
    template_name = "pages/list.html"
    context_object_name = "pages"

class PageDetailView(DetailView):
    model = Page
    template_name = "pages/detail.html"
    context_object_name = "page"


class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = "pages/form.html"
    success_url = reverse_lazy("pages_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Crear página"
        return context


class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    template_name = "pages/form.html"
    fields = ["titulo", "subtitulo", "contenido", "imagen", "fecha"]
    success_url = reverse_lazy("pages_list")

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = "pages/confirm_delete.html"
    success_url = reverse_lazy("pages_list")
