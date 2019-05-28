from django.shortcuts import render, redirect
from .models import Profile
from .filters import ProfileFilter
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm


def profiles_list(request):
    profiles = Profile.objects.all()
    filter = ProfileFilter(request.GET, queryset=profiles)
    return render(request, 'app_users/profile_list.html', {'filter': filter})


@login_required
def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    context = {'profile': profile}
    return render(request, 'app_users/profile_detail.html', context)

@login_required
def update_profile(request):
    if request.method == 'POST':
        update_profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if update_profile_form.is_valid():
            update_profile_form.save()
            return redirect('profile_url', request.user.profile.pk)
    else:
        update_profile_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'app_users/profile_update.html', {'update_profile_form':update_profile_form})
