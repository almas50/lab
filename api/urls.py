from rest_framework.routers import DefaultRouter

from .views import OrganizationViewSet, BillViewSet, ClientViewSet, BillViewSetList


router = DefaultRouter()
router.register('organizations_upload', OrganizationViewSet, basename='organization_upload')
router.register('bills_upload', BillViewSet, basename='bill_upload')
router.register('clients', ClientViewSet, basename='client')
router.register('bills', BillViewSetList, basename='bill')
urlpatterns = router.urls
