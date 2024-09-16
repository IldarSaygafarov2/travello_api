import os

import openpyxl
import pandas as pd
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from apps.users.models import User
from helpers.main import send_document_to_channel
from . import forms, models, utils
from .services.reports import DailyReportService


daily_report_service = DailyReportService()


def reports_index(request):
    if request.method == 'POST':
        form = forms.StaffAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('reports:reports_page')
    else:
        form = forms.StaffAuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'reports/index.html', context)


def reports_page(request):
    context = {
        'daily_report_form': forms.DailySalesForm(),
        'agent_report_form': forms.AgentReportForm(),
        'supplier_report_form': forms.SupplierReportForm(),
    }

    return render(request, 'reports/reports.html', context)


def create_daily_report(request):
    form = forms.DailySalesForm(data=request.POST)
    user = request.user
    if form.is_valid():
        form = form.save(commit=False)
        form.user = user
        form.save()
        new_obj = models.DailySales.objects.values().get(pk=form.pk)

        agent = models.Agent.objects.get(pk=new_obj['agent_id'])
        supplier = models.Supplier.objects.get(pk=new_obj['supplier_id'])

        msg = utils.create_report_message(
            report_type='Дневная оплата',
            serial_number=new_obj['serial_number'],
            date=new_obj['date'],
            agent=agent.name,
            supplier=supplier.name,
            agent_sum=new_obj['agent_sum'],
            supplier_sum=new_obj['supplier_sum'],
            direction=new_obj['direction'],
            comment=new_obj['comment'],
            marja=new_obj['marja']
        )
        # send message to telegram channel
        send_document_to_channel(msg=msg)
        # utils.create_report_file(report=msg)
        messages.success(request, 'Отчет добавлен')
        return redirect('reports:reports_page')
    else:
        messages.error(request, 'Ошибка')
        print(form.errors)
    return redirect('reports:reports_page')


def create_agent_report(request):
    form = forms.AgentReportForm(data=request.POST)
    user = request.user
    if form.is_valid():
        form = form.save(commit=False)
        form.user = user
        form.save()

        new_obj = models.AgentReport.objects.values().get(pk=form.pk)
        msg = utils.create_agent_report_message(
            repory_type='agent',
            serial_number=new_obj['serial_number'],
            date=new_obj['date'],
            agent_sum=new_obj['agent_sum'],
            direction=new_obj['direction'],
            comment=new_obj['comment'],
            balance=new_obj['balance'],
            agent_payment=new_obj['agent_payment'],
        )
        # send message to telegram channel
        send_document_to_channel(msg=msg)
        messages.success(request, 'Отчет добавлен')
        return redirect('reports:reports_page')
    else:
        print(form.errors)
        messages.error(request, 'Ошибка')
    return redirect('reports:reports_page')


def create_supplier_report(request):
    form = forms.SupplierReportForm(data=request.POST)
    user = request.user
    if form.is_valid():
        form = form.save(commit=False)
        form.user = user
        form.save()
        new_obj = models.SupplierReport.objects.values().get(pk=form.pk)
        msg = utils.create_agent_report_message(
            repory_type='supplier',
            serial_number=new_obj['serial_number'],
            date=new_obj['date'],
            agent_sum=new_obj['agent_sum'],
            direction=new_obj['direction'],
            comment=new_obj['comment'],
            balance=new_obj['balance'],
            agent_payment=new_obj['agent_payment'],
        )
        # send message to telegram channel
        send_document_to_channel(msg=msg)
        messages.success(request, 'отчет добавлен')
        return redirect('reports:reports_page')
    else:
        print(form.errors)
        messages.error(request, 'Ошибка')
    return redirect('reports:reports_page')


def download_reports(request):
    daily_reports = models.DailySales.objects.values().all()
    agent_reports = models.AgentReport.objects.values().all()

    # daily reports data
    columns_daily_reports = daily_report_service.collect_reports(daily_reports)

    if 'media' not in os.listdir(settings.BASE_DIR):
        os.mkdir(f'{settings.BASE_DIR}/media')

    data_daily_reports = pd.DataFrame(columns_daily_reports)
    data_daily_reports.to_excel(f'{settings.MEDIA_ROOT}/reports.xlsx', sheet_name='Дневная продажа')

    return render(request, 'reports/success.html')


def user_logout(request):
    logout(request)
    return redirect('reports:reports_index')