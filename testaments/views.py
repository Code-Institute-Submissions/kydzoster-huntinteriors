from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, View
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Testament


# everyone can view a testimony
class TestamentListView(ListView):
    model = Testament
    template_name = 'testaments/testament_list.html'
    queryset = Testament.objects.filter(approved=True)


# everyone can view a testimony, but only registered users can add content
class TestamentDetailView(LoginRequiredMixin, DetailView):
    model = Testament
    template_name = 'testaments/testament_detail.html'


# only user who created a testimony can edit it
class TestamentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Testament
    fields = ('title', 'body',)
    template_name = 'testaments/testament_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


# only user who created a testimony can delete it
class TestamentDeleteView(LoginRequiredMixin, DeleteView):
    model = Testament
    template_name = 'testaments/testament_delete.html'
    success_url = reverse_lazy('testament_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


# this will create a new testament by a current user
class TestamentCreateView(LoginRequiredMixin, CreateView):
    model = Testament
    template_name = 'testaments/testament_add.html'
    fields = ('title', 'body',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TestamentReviewList(UserPassesTestMixin, ListView):

    model = Testament
    queryset = Testament.objects.filter(approved=False)
    template_name = 'testaments/testament_review_list.html'

    def test_func(self):
        return self.request.user.is_superuser


class TestamentApproveView(UserPassesTestMixin, View):
    def get(self, request, pk):
        testament = Testament.objects.get(pk=pk)
        testament.approved = True
        testament.save()

        messages.success(
            request, f'Testament {testament.title} has been approved!')
        return redirect('testament_review_list')

    def test_func(self):
        return self.request.user.is_superuser
