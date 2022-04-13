from django.shortcuts import redirect


class RedirectToDashboard:
    def dispatch(self, request, *args, **kwargs):
        # диспатч се грижи за access-a към даденото view
        if request.user.is_authenticated:
            return redirect('dashboard')

        return super().dispatch(request, *args, **kwargs)
