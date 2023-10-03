
queries = [
    {
        "keyword": "restaurants in delhi",
        "max_results" : 100,
        "has_phone": True,
        "select": ["title", "website", "phone" , "address", "owner"],
        "sort": {
            "by": "title",
            "order": "asc",
        },
    },
]

number_of_scrapers = 6