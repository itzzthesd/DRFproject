from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class ReviewCreateThrottle( UserRateThrottle):
    scope = 'review-create'
    
class ReviewListThrottle( UserRateThrottle):
    scope = 'review-list'