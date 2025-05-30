
from django.contrib import admin
from django.urls import path
from .views import *
from .subscription_views import *
from . webhook_views import webhook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('verify-order' , VerifyPaymentCourse.as_view()),
    path('gateway-register' , PaymentGatewayRegister.as_view()),
    path('create-order' , CreateCourseOrderView.as_view()),
    path('get-wallet' , WalletDetailsInAnalytics.as_view()),
    path('six-months-analytics' , TotalOrdersWeGotInSixMonths.as_view()),
    path('seven-day-analytics' , TotalOrdersWeGotInSevenDays.as_view()),
    path('previous-orders' ,PreviousOrderLogs.as_view()),
    path('check-connected',CheckConnectedPayment.as_view() ),


    # Subscription Views

    path('create-subscription', SubscriptionCreateView.as_view()),
    path('verify-subscription' , VerifyPayment.as_view()),
    path('cancel-subscription' , CancelSubscription.as_view()),


    # webhook
    path('webhook', webhook , name='webhook')


]
