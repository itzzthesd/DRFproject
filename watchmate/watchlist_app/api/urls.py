from django.urls import path, include
from rest_framework.routers import DefaultRouter

from watchlist_app.api.views import  (WatchListAV, WatchDetailAV, 
                                      StreamPlatformAV, StreamDetailAV, 
                                      ReviewList, ReviewDetail,
                                      ReviewCreate, StreamPlatformVS,
                                      UserReview, WatchListGV)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')


urlpatterns = [
    path('list2/', WatchListGV.as_view(), name="watch-list2"),
    path('list/', WatchListAV.as_view(), name="watch-list"),
    path('<int:pk>/', WatchDetailAV.as_view(), name="watch-list-detail"),
    # path('stream/', StreamPlatformAV.as_view(), name="stream-platform"),
    # path('stream/<int:pk>/', StreamDetailAV.as_view(), name="stream-detail"),
    path('', include(router.urls)),
    
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name="review-create"),
    path('<int:pk>/review/', ReviewList.as_view(), name="review"),
    path('review/<int:pk>/', ReviewDetail.as_view(), name="review-detail"),
    
    # path('review/', ReviewList.as_view(), name="review-list"),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name="review-details"),
    path('reviews/<str:username>/', UserReview.as_view(), name="user-review"),


]