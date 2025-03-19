# URL SHORTENER API DOCUMENTATION by Emmanuel
This API allows users to shorten URLs and redirect to the original links.

## Base URL
http://localhost:8000/

---

## 1️⃣ Shorten a URL
### **Endpoint:** POST  /api/shorten/
###	**Request body(JSON):**
```json
{ 
    "original_url": "https://example.com" 
}
```
###	**Response(JSON):**
```json
{  	"original_url":"https://google.com",
	"short_code":"6pBpRZ",
	"short_url":"http://localhost:8000/6pBpRZ"
}
```

## 2️⃣ Redirect to Original URls
###	**Endpoint:** GET /<short_code>/
###	**Example:** http://localhost:8000/6pBpRz/
	Redirects to: https://google.com