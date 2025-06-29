import re

def extract_features(url):
    features = {
        'url_length': len(url),
        'has_https': int(url.startswith("https")),
        'has_ip': int(bool(re.match(r'https?://\d{1,3}\.', url))),
        'count_dots': url.count('.'),
        'has_at': int('@' in url),
        'has_dash': int('-' in url),
        'has_suspicious_words': int(any(word in url.lower() for word in ['login', 'free', 'verify', 'account', 'bank']))
    }
    return features
