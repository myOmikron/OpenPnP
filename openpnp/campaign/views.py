from django.shortcuts import render
from django.views.generic import TemplateView


class CampaignView(TemplateView):
    template_name = "campaign/campaign.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
