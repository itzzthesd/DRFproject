# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse

# def movie_list(request):
#     movies = Movie.objects.all()
#     print(movies)
#     data = {
#         'movies':list(movies.values())
#         }
    
#     return JsonResponse(data)

# def movie_detail(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         'name':movie.name,
#         'des':movie.descirption,
#         }
#     return JsonResponse(data)
    

