from crawler import crawl_data

def get_recommendations(city, limit):
    data = crawl_data(city)

    # Hybrid logic (content + popularity simulated)
    recommendations = sorted(data, key=lambda x: x["category"])

    return recommendations[:limit]
