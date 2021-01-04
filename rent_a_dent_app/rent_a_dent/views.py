from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.views.generic import UpdateView, DeleteView
from rest_framework import generics

from rent_a_dent.models import Visit
from rent_a_dent.forms import VisitForm, VisitPerDayForm
from rent_a_dent.serializers import VisitSerializer


# Create your views here.

class LandingPage(View):
    def get(self, request):
        return render(request, "main.html")


class VisitsList(View):
    def get(self, request):
        visits_lst = Visit.objects.all().order_by('day')
        return render(request, 'visits.html', {'visits': visits_lst})



# ADD VIEW

class AddVisit(View):
    def get(self, request):
        form = VisitForm()
        return render(request, 'add_visit.html', {'form': form})

    def post(self, request):
        form = VisitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visits_list')
        else:
            return render(request, 'add_visit.html', {'form': form})



# UPDATE & DELETE

class UpdateVisitView(PermissionRequiredMixin, UpdateView):
    permission_required = ['rent_a_dent.update_visit']
    model = Visit
    form_class = VisitForm
    template_name = 'add_visit.html'
    success_url = '/visits/'


class DeleteVisitView(PermissionRequiredMixin, DeleteView):
    permission_required = ['rent_a_dent.delete_visit']
    model = Visit
    template_name = "delete_view.html"
    success_url = '/visits/'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex.update({'button_name': 'DELETE'})
        return contex

    def post(self, request, *args, **kwargs):
        if request.POST['del'] == 'Abort':
            self.object = self.get_object()
            success_url = self.get_success_url()
            return redirect(success_url)
        return self.delete(request, *args, **kwargs)


# DETAILS VIEW

class VisitDetails(View):
    def get(self, request, visit_id):
        visit = Visit.objects.get(id=visit_id)
        context = {
            'visit': visit,
        }
        return render(request, 'details_visit.html', context)


# SERIALIZERS

class VisitListViewSerializer(generics.ListCreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer


class VisitViewSerializer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer



class PerDay(View):
    def get(self, request):
        form = VisitPerDayForm()
        return render(request, 'per_day_visit.html', {'form': form})

    def post(self, request):
        date_count = VisitPerDayForm(request.POST)
        if request.method == 'POST':
            form = VisitPerDayForm(request.POST)
            if form.is_valid():
                date1 = form.cleaned_data['day']
                date = str(date1)
                date_count = Visit.objects.filter(day=date)
                return render(request, 'per_day_visit.html', {'date_count': date_count})