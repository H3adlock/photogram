from rest_framework.generics import ListAPIView, RetrieveAPIView

from report.models import Report
from .serializers import ReportSerializer


class ReportListView(ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportDetailView(RetrieveAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
