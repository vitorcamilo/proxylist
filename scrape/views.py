from django.shortcuts import render
from .models import IPlist
from .proxyscraper import proxylist
from scrapy.crawler import CrawlerRunner
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from django.db import connection, transaction
from django.views.generic import View, TemplateView, CreateView, UpdateView, DetailView, ListView, DeleteView
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = "../templates/scrape/ip_list.html"


class IpListView(ListView):
    model = IPlist


class IPDetailView(DetailView):
    context_object_name = 'ip_details'
    model = IPlist


class CreateIPView(CreateView):
    fields = ('id', 'ipadress', 'port', 'protocol', 'anonymity', 'country',
              'region', 'city', 'uptime', 'runtime', 'transfer')
    model = IPlist


class UpdateIPView(UpdateView):
    model = IPlist
    fields = ('id', 'ipadress', 'port', 'protocol', 'anonymity', 'country',
              'region', 'city', 'uptime', 'runtime', 'transfer')
    success_url = '/'


class DeleteIPView(DeleteView):
    model = IPlist
    success_url = reverse_lazy('index')


def delete_ips(request):
    if request.method == "GET":
        dest = IPlist.objects.all()
        dest.delete()
        return render(request, 'scrape/iplist_list.html')


def run_ip_scraper(request):
    ProxylistSpider = proxylist.ProxylistSpider
    settings = get_project_settings()
    process = CrawlerRunner(settings)
    process.crawl(ProxylistSpider)
    return render(request, 'scrape/iplist_list.html')
