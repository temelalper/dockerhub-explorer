import requests

def search_dockerhub(query):
    url = f"https://hub.docker.com/v2/search/repositories/?query={query}"

    try:
        response = requests.get(url) #serialize işlevi
       #istek yollama
        if response.status_code != 200:
            return []

        data = response.json()
        results = []

        #deserialize işlevi
        for item in data.get('results', []):
            results.append({
                'name': item.get('repo_name'),
                'description': item.get('short_description'),
                'star_count': item.get('star_count')
            })

        return results

    except Exception as e:
        print(f"Hata: {e}")
        return []