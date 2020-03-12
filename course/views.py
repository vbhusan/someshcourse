from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, CreateView
from .forms import InfoForm
from django.urls import reverse_lazy


class Home(CreateView):
    form_class = InfoForm
    template_name = 'courseform.html'
    success_url = reverse_lazy('course:home')

    # def form_valid(self, form):
    #     result = super(Home, self).form_valid(form)
    #     cd  = form.cleaned_data
    #     return super().form_valid(result)


class Thank(CreateView):
    template_name = 'thankyou.html'