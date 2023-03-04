from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
api_view(["GET"])
def getRoutes(request):
    """
    Function untuk menampilkan halaman utama dari API. Halaman ini akan tampak seperti
    dokumentasi untuk para developer yang ingin mengakses data melalui API.
    """
    routes = {
        "anime" : [
            {
                "Endpoint" : "/anime/",
                "method" : "GET",
                "body" : None,
                "description" : "Menampilkan daftar anime yang terdapat di dalam database."
            },
            {
                "Endpoint" : "/anime/id/",
                "method" : "GET",
                "body" : None,
                "description" : "Menampilkan satu data anime berdasarkan primary key."
            },
            {
                "Endpoint" : "/anime/id/slug/",
                "method" : "GET",
                "body" : None,
                "description" : "Menampilkan satu data anime berdasarkan primary key dan slug."
            },
            {
                "Endpoint" : "/anime/create",
                "method" : "POST",
                "body" : {
                    "mal_id" : 0,
                    "anime_title" : "",
                    "anime_score" : 0.0,
                    "airing_time" : "",
                    "studio" : "",
                },
                "description" : "Menambahkan data anime baru melalui API."
            },
            {
                "Endpoint" : "/anime/id/update",
                "method" : "PUT",
                "body" : {
                    "mal_id" : 0,
                    "anime_title" : "",
                    "anime_score" : 0.0,
                    "airing_time" : "",
                    "studio" : "",
                },
                "description" : "Mengubah satu data anime berdasarkan primary key."
            },
            {
                "Endpoint" : "/anime/id/delete",
                "method" : "DELETE",
                "body" : None,
                "description" : "Menghapus satu data anime berdasarkan primary key."
            }
        ],
        "studio" : [
            "Akan dikerjakan lain waktu."
        ],
        "people" : [
            "Akan dikerjakan lain waktu."
        ],
        "member" : [
            "Akan dikerjakan lain waktu."
        ]
    }
    return Response(routes)
